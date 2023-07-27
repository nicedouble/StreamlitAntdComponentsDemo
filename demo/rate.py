#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/26 15:12
@Author   : ji hao ran
@File     : rate.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import rate, BsIcon


def callback():
    if st.session_state['half']:
        st.session_state['kv'] = {'min_value': .0, 'max_value': 3.0, 'value': .0, 'step': .5}
    else:
        st.session_state['kv'] = {'min_value': 0, 'max_value': 3, 'value': 0}


def sidebar():
    if 'kv' not in st.session_state:
        st.session_state['kv'] = {'min_value': 0, 'max_value': 3, 'value': 0}

    value = st.number_input('value', **st.session_state['kv'])
    count = st.number_input('count', 5, 100, 5, 5)
    symbol = st.selectbox('symbol', [None, 'A', BsIcon("bell-fill")])
    align = st.selectbox('align', ["start", "center", "end"])
    half = st.checkbox('half', on_change=callback, key='half')
    clear = st.checkbox('clear')
    readonly = st.checkbox('readonly')
    size = st.number_input('size', 10, 50, 20, 5)
    color = st.selectbox('color', [None, 'orange', 'green'])
    kw = locals()
    return kw


def main(kw):
    r = rate(**kw)
    st.write(f'The rate value is: {r}')


def api():
    st.help(rate)


RATE_DEMO = {
    'rate': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
