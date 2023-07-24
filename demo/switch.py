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
    label = st.selectbox('label', [None, 'switch label'], 1)
    value = st.checkbox('value')
    checked = st.selectbox('checked', [None, 'yes', 'BsIcon("sun")'])
    unchecked = st.selectbox('unchecked', [None, 'no', 'BsIcon("moon")'])
    align = st.selectbox('align', ["start", "center", "end"])
    position = st.selectbox('position', ["top", "right", "bottom", "left"], help='label position')
    size = st.selectbox('size', ["default", "small", "large"])
    disabled = st.checkbox('disabled')
    kw = dict(
        label=label,
        value=value,
        checked=eval(checked) if isinstance(checked, str) and checked.startswith('BsIcon') else checked,
        unchecked=eval(unchecked) if isinstance(unchecked, str) and unchecked.startswith('BsIcon') else unchecked,
        align=align,
        position=position,
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
