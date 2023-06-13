#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/6/13 11:11
@Author   : ji hao ran
@File     : divider.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import divider


def sidebar():
    label = st.text_input('label', 'divider')
    icon = st.selectbox('icon', [None, 'house'], 1)
    align = st.selectbox('align', ['right', 'center', 'left'], 1)
    direction = st.selectbox('direction', ["horizontal", "vertical"])
    dashed = st.checkbox('dashed')
    kw = dict(
        label=label,
        icon=icon,
        align=align,
        direction=direction,
        dashed=dashed,
    )
    return kw


def main(kw):
    divider(**kw)


def api():
    st.help(divider)


DIVIDER_DEMO = {
    'divider': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
