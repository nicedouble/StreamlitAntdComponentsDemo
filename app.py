#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/26 22:14
@Author   : ji hao ran
@File     : app.py
@Project  : StreamlitAntdComponents
@Software : PyCharm
"""

from demo.demo import DEMO
from demo.overview import overview
from demo.callback import callback_usage
from demo.session_state import session_usage
from demo.utils import *

st.set_page_config(layout='wide', page_title='streamlit-antd-components')

st.markdown(f'''
    <style>
    .stApp .main .block-container{{
        padding-top:30px
    }}
    .stApp [data-testid='stSidebar']>div:nth-child(1)>div:nth-child(2){{
        padding-top:50px
    }}
    iframe{{
        display:block;
    }}
    </style>
    ''', unsafe_allow_html=True)

if 'index' not in st.session_state:
    st.session_state['index'] = 0

with st.sidebar.container():
    # tag
    modified = sac.Tag('Modified', color='blue', bordered=False)
    new = sac.Tag('New', color='green', bordered=False)
    deprecated = sac.Tag('Deprecated', color='orange', bordered=False)
    c = st.columns([1, 12])
    with c[0]:
        # logo
        show_image(Path(__file__).parent.joinpath('logo.svg'), svg=True, height=25)
    with c[1]:
        # title
        st.subheader(f'Streamlit-antd-components `v{sac.__VERSION__}`')
    # menu
    menu = sac.menu(
        items=[
            sac.MenuItem('overview'),
            sac.MenuItem('general', type='group', children=[sac.MenuItem('buttons')]),
            sac.MenuItem('layout', type='group', children=['divider']),
            sac.MenuItem(
                label='navigation', type='group', children=[
                    sac.MenuItem('menu'),
                    sac.MenuItem('pagination'),
                    'steps'
                ]
            ),
            sac.MenuItem(
                label='data entry', type='group',
                children=[
                    sac.MenuItem('cascader'),
                    'checkbox',
                    sac.MenuItem('chip'),
                    'rate', 'switch',
                    sac.MenuItem('transfer')
                ]
            ),
            sac.MenuItem(
                label='data display', type='group',
                children=[
                    sac.MenuItem('segmented'),
                    'tabs',
                    sac.MenuItem('tree'),
                    sac.MenuItem('tags'),
                ],
            ),
            sac.MenuItem(
                label='feedback', type='group', children=[
                    sac.MenuItem('alert'),
                    sac.MenuItem('result')
                ]
            ),
            sac.MenuItem(type='divider'),
            sac.MenuItem('session state usage', tag=new),
            sac.MenuItem('callback usage', tag=new),
        ],
        index=st.session_state['index'],
        open_all=True,
        size='small',
        format_func='title',
    )

with st.container():
    if menu == 'overview':
        overview()
    elif menu == 'callback usage':
        callback_usage()
    elif menu == 'session state usage':
        session_usage()
    else:
        com_ = DEMO.get(menu)
        st.subheader(menu.title(), anchor=False)
        st.write(com_.get('doc'))
        tabs = sac.tabs([sac.TabsItem('Demo', icon='easel'), sac.TabsItem('Api', icon='cursor')], align='start')
        if tabs == 'Demo':
            col = st.columns([3, 1])
            with col[-1].expander(f"{menu} params", True):
                kw = com_.get('params')()
            with col[0]:
                com_.get('main')(kw)
        else:
            com_.get('api')()
