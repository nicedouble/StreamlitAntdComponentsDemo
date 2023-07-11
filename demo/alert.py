#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/11 16:37
@Author   : ji hao ran
@File     : alert.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import alert


def sidebar():
    message = st.text_input('message', 'alert message')
    description = st.text_input('description', 'alert description')
    type = st.selectbox('type', ['info', 'success', 'warning', 'error'])
    height = st.selectbox('height', [None, 100], 1)
    icon = st.checkbox('icon', True)
    closable = st.checkbox('closable', True)
    banner = st.checkbox('banner', True)
    kw = dict(
        message=message,
        description=description,
        type=type,
        height=height,
        icon=icon,
        closable=closable,
        banner=banner,
    )
    return kw


def main(kw):
    alert(**kw)


def api():
    st.help(alert)


ALERT_DEMO = {
    'alert': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
