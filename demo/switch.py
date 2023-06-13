#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/6/13 10:43
@Author   : ji hao ran
@File     : switch.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import switch, BsIcon


def sidebar():
    value = st.checkbox('value', True)
    checked = st.selectbox('checked', [None, 'checked', 'BsIcon("sun")'], 2)
    unchecked = st.selectbox('unchecked', [None, 'unchecked', 'BsIcon("moon")'], 2)
    size = st.selectbox('size', ["default", "small", "large"])
    disabled = st.checkbox('disabled')
    kw = dict(
        value=value,
        checked=eval(checked) if isinstance(checked, str) and checked.startswith('BsIcon') else checked,
        unchecked=eval(unchecked) if isinstance(unchecked, str) and unchecked.startswith('BsIcon') else unchecked,
        size=size,
        disabled=disabled,
    )
    return kw


def main(kw):
    s = switch(**kw)
    st.write(f'switch return value: {s}')


def api():
    st.help(switch)
    st.help(BsIcon)


SWITCH_DEMO = {
    'switch': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
