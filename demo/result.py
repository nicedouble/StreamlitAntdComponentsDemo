#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/27 14:56
@Author   : ji hao ran
@File     : result.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import result


def sidebar():
    title = st.selectbox('title', [None, 'title'])
    subtitle = st.selectbox('subtitle', [None, 'subtitle'], 1)
    status = st.selectbox('status', ['info', 'success', 'warning', 'error', 'empty', 403, 404, 500])
    icon = st.selectbox('icon', [None, 'house', 'google'])
    return locals()


def main(kw):
    result(**kw)


def api():
    st.help(result)


RESULT_DEMO = {
    'result': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
