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

st.set_page_config(layout='wide', page_title='streamlit-antd-components')

with st.sidebar.container():
    st.header('Streamlit-antd-component')
    component = st.radio('Select a component', DEMO.keys(), label_visibility='collapsed')
    st.subheader(f'{component} params')
    kw = DEMO.get(component).get('sidebar')()

with st.container():
    DEMO.get(component).get('main')(kw)
