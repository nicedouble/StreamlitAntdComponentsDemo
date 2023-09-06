#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/26 22:14
@Author   : ji hao ran
@File     : app.py
@Project  : StreamlitAntdComponents
@Software : PyCharm
"""

import streamlit as st
import streamlit_antd_components as sac
from demo.demo import DEMO
from demo.overview import overview

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

    # menu
    st.subheader('Streamlit-antd-components')
    menu = sac.menu(
        items=[
            sac.MenuItem('overview'),
            sac.MenuItem('general', type='group', children=[sac.MenuItem('buttons', tag=modified)]),
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
                    'checkbox', 'rate', 'switch',
                    sac.MenuItem('transfer', tag=modified)
                ]
            ),
            sac.MenuItem(
                label='data display', type='group',
                children=[
                    sac.MenuItem('segmented', tag=modified),
                    'tabs',
                    sac.MenuItem('tree'),
                    sac.MenuItem('tag', children=[
                        sac.MenuItem('tag'),
                        sac.MenuItem('tags'),
                    ])
                ]
            ),
            sac.MenuItem(
                label='feedback', type='group', children=[
                    sac.MenuItem('alert'),
                    sac.MenuItem('result')
                ]
            ),
        ],
        index=st.session_state['index'],
        open_all=True,
        size='small',
        format_func='title',
        indent=30,
    )

with st.container():
    version_href = f"https://pypi.org/project/streamlit-antd-components/{sac.__VERSION__}/"
    sac.alert(
        message=f'Welcome to **Streamlit-antd-components**, the latest version : '
                f'**<a href="{version_href}" target="_blank" class="badge badge-success rounded-pill">{sac.__VERSION__}</a>**',
        banner=True, closable=True, type='success')
    if menu == 'overview':
        overview()
    else:
        com_ = DEMO.get(menu)
        tabs = sac.tabs([sac.TabsItem('Demo', icon='easel'), sac.TabsItem('Api', icon='cursor')], align='center')
        if tabs == 'Demo':
            col = st.columns([1, 3])
            with col[0].expander(f"{menu} params", True):
                kw = com_.get('sidebar')()
            with col[-1]:
                com_.get('main')(kw)
        else:
            com_.get('api')()
