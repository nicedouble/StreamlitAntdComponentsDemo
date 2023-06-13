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
from demo import DEMO
import streamlit_antd_components as sac

st.set_page_config(layout='wide', page_title='streamlit-antd-components')

with st.sidebar.container():
    st.header('Streamlit-antd-component')
    component = sac.menu(list(DEMO.keys()) + [
        sac.MenuItem('reference', type='group', children=[
            sac.MenuItem('Ant Design',icon='sign-intersection-y', href='https://ant.design/components/overview/'),
            sac.MenuItem('github', icon='github', href='https://github.com/nicedouble/StreamlitAntdComponents')
        ])
    ], format_func='title')
    com_ = DEMO.get(component)

with st.container():
    tabs = st.tabs(['demo', 'api'])
    with tabs[0]:
        col = st.columns([1, 0.2, 3])
        with col[0].expander(f'{component} params', True):
            kw = com_.get('sidebar')()
        with col[-1]:
            com_.get('main')(kw)
    with tabs[1]:
        com_.get('api')()
