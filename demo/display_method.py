import inspect
from typing import get_origin, Union, Literal

import streamlit as st
import streamlit_antd_components as sac

from demo.method_code import methods_code


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

        out.append({'name': name,
                    'annotation': param.annotation,
                    'default': default})
    # print(out)
    return out


def display_method(method):
    if method not in methods_code.keys():
        raise ValueError(f'unsupported method {method}')

    st.subheader(method.title(), anchor=False)
    func = getattr(sac, method)
    args = get_args_dict(func)
    doc = func.__doc__
    doc_ = doc.split(':param')[0].strip()
    st.markdown(doc_)

    #  demo and api
    c0, c1 = st.columns([2.2, 1])
    params = {}
    with c1.expander(f"{method} params", True):
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
                params[name] = c1_[n].selectbox(name, annotation.__args__, index)
            else:
                continue
            n += 1
    with c0:
        # tabs = sac.tabs([sac.TabsItem('Demo', icon='easel'), sac.TabsItem('Api', icon='cursor')], size='sm')
        tabs = sac.tabs(['Demo', 'Api'], size='sm')

        if tabs == 'Demo':
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
        elif tabs == 'Api':
            doc = inspect.getdoc(func)
            st.code(doc)
        else:
            raise ValueError(f'unsupported tab {tabs}')