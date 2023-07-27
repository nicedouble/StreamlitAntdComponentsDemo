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
    component = sac.menu(
        items=[
            sac.MenuItem('general', type='group', children=['buttons']),
            sac.MenuItem('layout', type='group', children=['divider']),
            sac.MenuItem('navigation', type='group', children=['menu', 'steps']),
            sac.MenuItem('data entry', type='group', children=['cascader', 'checkbox', 'rate', 'switch', 'transfer']),
            sac.MenuItem('data display', type='group', children=['segmented', 'tabs', 'tree']),
            sac.MenuItem('feedback', type='group', children=['alert', 'result']),
            sac.MenuItem('reference', type='group', children=[
                sac.MenuItem('Ant Design', icon='sign-intersection-y', href='https://ant.design/components/overview/'),
                sac.MenuItem('github', icon='github', href='https://github.com/nicedouble/StreamlitAntdComponents'),
                sac.MenuItem('bootstrap icons', icon='bootstrap', href='https://icons.getbootstrap.com/'),
            ])
        ],
        index=1,
        format_func='title')
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
