#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/26 22:14
@Author   : ji hao ran
@File     : app.py
@Project  : StreamlitAntdComponents
@Software : PyCharm
"""
from typing import Literal, get_origin, Union

from demo.demo_ import methods
from demo.icon import icon
from demo.overview import overview
from demo.utils import *

st.set_page_config(layout='wide', page_title='streamlit-antd-components')

st.markdown(f'''
    <style>
    .stApp .main .block-container{{
        padding:30px 50px
    }}
    .stApp [data-testid='stSidebar']>div:nth-child(1)>div:nth-child(2){{
        padding-top:50px
    }}
    iframe{{
        display:block;
    }}
    .stRadio div[role='radiogroup']>label{{
        margin-right:5px
    }}
    </style>
    ''', unsafe_allow_html=True)

with st.sidebar.container():
    # tag
    modified = sac.Tag('Modified', color='blue', bordered=False)
    new = sac.Tag('New', color='green', bordered=False)
    deprecated = sac.Tag('Deprecated', color='orange', bordered=False)
    redesign = sac.Tag('Redesign', color='purple', bordered=False)
    # title
    st.subheader(f'Streamlit-antd-components')
    method = sac.menu(
        items=[
            sac.MenuItem('overview'),
            sac.MenuItem('icon', tag=new),
            sac.MenuItem('general', type='group', children=[
                sac.MenuItem('buttons')
            ]),
            sac.MenuItem('layout', type='group', children=[sac.MenuItem('divider')]),
            sac.MenuItem(
                label='navigation', type='group', children=[
                    sac.MenuItem('menu', tag=modified),
                    sac.MenuItem('pagination'),
                    'steps'
                ]
            ),
            sac.MenuItem(
                label='data entry', type='group',
                children=[
                    sac.MenuItem('cascader'),
                    sac.MenuItem('checkbox'),
                    sac.MenuItem('chip'),
                    'rate',
                    sac.MenuItem('switch'),
                    sac.MenuItem('transfer')
                ]
            ),
            sac.MenuItem(
                label='data display', type='group',
                children=[
                    sac.MenuItem('segmented'),
                    sac.MenuItem('tabs', tag=modified),
                    sac.MenuItem('tree'),
                    sac.MenuItem('tags'),
                ],
            ),
            sac.MenuItem(
                label='feedback', type='group', children=[
                    sac.MenuItem('alert', tag=modified),
                    sac.MenuItem('result')
                ]
            ),
            sac.MenuItem(label='Advanced Usage', type='group', children=[
                sac.MenuItem('session state'),
                sac.MenuItem('callback'),
            ]),
        ],
        key='menu',
        open_all=True, indent=20,
        format_func='title',
    )
    sac.divider('Environment', color='gray')
    sac.tags(
        [sac.Tag(f'streamlit=={st.__version__}', size='xs', color='cyan'),
         sac.Tag(f'streamlit-antd-components=={sac.__VERSION__}', size='xs', color='blue')])


def get_args(func):
    sig = inspect.signature(func)
    return {param.name: param.annotation for param in sig.parameters.values()}


def show_code(x: str, open: bool = False):
    with st.expander('code', open):
        st.code(f'''
        import streamlit_antd_components as sac\n{x}
        ''', line_numbers=True)


with st.container():
    if method == 'overview':
        overview()
        st.stop()
    elif method == 'icon':
        icon()
        st.stop()
    if method not in methods.keys():
        raise ValueError(f'unsupported method {method}')
    # if method == 'buttons':
    st.subheader(method.title(), anchor=False)
    func = getattr(sac, method)
    args = get_args(func)
    doc = func.__doc__
    doc_ = doc.split(':param')[0].strip()
    st.markdown(doc_)

    # component demo and api
    # tabs = sac.tabs([sac.TabsItem('Demo', icon='easel'), sac.TabsItem('Api', icon='cursor')], size='sm')
    # if tabs == 'Demo':
    c0, c1 = st.columns([2.2, 1])
    params = {}
    with c1.expander(f"{method} params", True):
        c1_ = st.columns(2)
        n = 0
        for name, annotation in args.items():
            print(f"{name=}")
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
                params[name] = c1_[n].text_input(name, name)
            elif annotation is bool:
                params[name] = c1_[n].checkbox(name, False)
            elif get_origin(annotation) is Literal:
                params[name] = c1_[n].selectbox(name, annotation.__args__)
            else:
                continue
            n += 1
    with c0:
        params_str = {f"{k}={v!r}" for k, v in params.items()}
        params_str = ", ".join(params_str)
        code = methods[method].format(params_str=params_str)
        # with st.tabs(['demo', 'api']):
        with st.expander('demo', True):
            out = eval(code)
            st.markdown(f"The selected button label is: {out}")

        with st.expander('code', True):
            code = f"import streamlit_antd_components as sac\n{code}"
            st.code(code, line_numbers=True)


