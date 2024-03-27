import inspect
from typing import get_origin, Union, Literal

import streamlit as st
import streamlit_antd_components as sac

from demo.method_code import methods_code
import webcolors

def get_args_dict(func):
    sig = inspect.signature(func)
    out = []
    for param in sig.parameters.values():
        default = param.default
        name = param.name

        if name == 'color' and default is None:
            default = st.get_option('theme.primaryColor') or 'red'
        elif name == 'background_color' and default is None:
            default = st.get_option('theme.backgroundColor') or 'white'
        elif name == 'font' and default is None:
            default = st.get_option('theme.font') or 'arial'
        elif name == 'size' and default is None:
            default = 'md'

        if (default is inspect.Parameter.empty or default is None) and param.annotation is str:
            default = name

        if name == 'symbol':
            default = None

        if func.__name__ == 'BsIcon' and name == 'name':
            default = 'house'
        if func.__name__ == 'AntIcon' and name == 'name':
            default = 'HomeOutlined'

        out.append({'name': name,
                    'annotation': param.annotation,
                    'default': default})
    # print(out)
    return out


def get_demo(method, params):
    params_str = {f"{k}={v!r}" for k, v in params.items()}
    params_str = ", ".join(params_str)
    code = methods_code[method].format(params_str=params_str)
    code = code.strip()
    # with st.tabs(['demo', 'api']):
    with st.expander('demo', True):
        out = eval(code)
        st.markdown(f"The selected {method} item is: {out}")

    with st.expander('code', True):
        code = f"import streamlit_antd_components as sac\n{code}"
        st.code(code, line_numbers=True)


def get_api(func):
    doc = inspect.getsource(func)
    st.code(doc)


def selectbox_color(label, options, index, c1):
    with c1:
        sac.menu([
            sac.MenuItem('', tag=[sac.Tag(color, color=color)]) for color in options
        ], index=index)



def get_hex(color_name):
    if color_name.startswith('#'):
        return color_name
    try:
        rgb_tuple = webcolors.name_to_rgb(color_name)
        hex_value = "#{:02x}{:02x}{:02x}".format(*rgb_tuple)
        return hex_value
    except ValueError:
        return f"Color '{color_name}' not found"



def get_params(func):
    if func.__name__ in ['BsIcon', 'AntIcon']:
        icon = sac.chip(['Bootstrap', 'Ant'], index=0, label='icon', size='sm')
        if icon != st.session_state['icon']:
            st.session_state['icon'] = icon
            st.rerun()
    args = get_args_dict(func)
    params = {}
    c1_ = st.columns(2)
    n = 0
    for args_ in args:
        name = args_['name']
        annotation = args_['annotation']
        default = args_['default']
        # print(f"{name=}")
        if n > 1:
            n = 0
            c1_ = st.columns(2)
        if get_origin(annotation) is Union:
            annotation_args = annotation.__args__
            annotation_args_literal = [v for v in annotation_args if get_origin(v) is Literal]
            if len(annotation_args_literal) == 0:
                annotation = annotation_args[0]
            else:
                annotation = annotation_args_literal[0]

        if annotation is str:
            params[name] = c1_[n].text_input(name, default)
        elif annotation is int or annotation is float:
            params[name] = c1_[n].number_input(name, value=default)
        elif annotation is bool:
            params[name] = c1_[n].checkbox(name, default)
        elif get_origin(annotation) is Literal:
            if default in annotation.__args__:
                index = annotation.__args__.index(default)
            else:
                index = 0
            if 'color' in name:
                params[name] = c1_[n].color_picker(name, get_hex(default))
            else:
                params[name] = c1_[n].selectbox(name, annotation.__args__, index)
        else:
            continue
        n += 1
    return params


def get_doc_str(func):
    doc = func.__doc__
    doc_ = doc.split(':param')[0].strip()
    st.markdown(doc_)


def display_method(method):
    if method == 'Bootstrap':
        method = 'BsIcon'
    elif method == 'Ant':
        method = 'AntIcon'

    if method not in methods_code.keys():
        raise ValueError(f'unsupported method {method}')

    st.subheader(method.title(), anchor=False)

    func = getattr(sac, method)
    get_doc_str(func)

    tab = sac.tabs(['Demo', 'Api'], size='sm')

    if tab == 'Demo':
        c0, c1 = st.columns([2.2, 1])
        with c1.expander(f"{method} params", True):
            params = get_params(func)
        with c0:
            get_demo(method, params)
    elif tab == 'Api':
        get_api(func)
    else:
        raise ValueError(f'unsupported tab {tab}')
