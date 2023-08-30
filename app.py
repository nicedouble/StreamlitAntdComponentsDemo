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
from demo.demo import DEMO
import streamlit_antd_components as sac

st.set_page_config(layout='wide', page_title='streamlit-antd-components')

with st.sidebar.container():
    # tag
    modified = sac.Tag('Modified', color='blue', bordered=False)
    new = sac.Tag('New', color='green', bordered=False)
    deprecated = sac.Tag('Deprecated', color='orange', bordered=False)

    st.header('Streamlit-antd-component')
    menu = sac.menu(
        items=[
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
                    'checkbox', 'rate', 'switch', 'transfer'
                ]
            ),
            sac.MenuItem(
                label='data display', type='group',
                children=[
                    sac.MenuItem('segmented'),
                    'tabs',
                    sac.MenuItem('tree', tag=modified),
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
            sac.MenuItem(type='divider'),
            sac.MenuItem('reference', type='group', children=[
                sac.MenuItem('Ant Design', icon='sign-intersection-y', href='https://ant.design/components/overview/'),
                sac.MenuItem('github', icon='github', href='https://github.com/nicedouble/StreamlitAntdComponents'),
                sac.MenuItem('bootstrap icons', icon='bootstrap', href='https://icons.getbootstrap.com/'),
            ])
        ],
        index=1,
        open_all=True,
        size='small',
        format_func='title')
    com_ = DEMO.get(menu)

with st.container():
    st.markdown(f'''
        <style>
        .stApp .main .block-container{{
            padding-top:30px
        }}
        iframe{{
            display:block;
        }}
        </style>
        ''', unsafe_allow_html=True)
    version_href = f"https://pypi.org/project/streamlit-antd-components/{sac.__VERSION__}/"
    sac.alert(
        message=f'Welcome to **Streamlit-antd-components**, the latest version : '
                f'**<a href="{version_href}" target="_blank" class="badge badge-success rounded-pill">{sac.__VERSION__}</a>**',
        banner=True, closable=True, type='success')

    tabs = sac.tabs([
        sac.TabsItem('demo', icon='easel'),
        sac.TabsItem('api', icon='cursor')
    ], align='center', format_func='title')

    if tabs == 'demo':
        col = st.columns([1, 3])
        with col[0].expander(f"{menu} params", True):
            kw = com_.get('sidebar')()
        with col[-1]:
            com_.get('main')(kw)
    else:
        com_.get('api')()
