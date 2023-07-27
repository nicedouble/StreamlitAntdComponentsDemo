#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/26 15:12
@Author   : ji hao ran
@File     : checkbox.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import checkbox, CheckboxItem


def sidebar():
    index = st.selectbox('index', [None, 0, [0, 1]])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    check_all = st.checkbox('check_all', help='show check all box')
    check_all_label = st.text_input('check_all_label', 'Check all')
    check_all_position = st.selectbox('check_all_position', ["top", "right", "bottom", "left"])
    align = st.selectbox('align', ["start", "center", "end"])
    direction = st.selectbox('direction', ["horizontal", "vertical"])
    disabled = st.checkbox('disabled')
    return_index = st.checkbox('return_index')
    kw = locals()
    kw.update(
        format_func=eval(format_func) if isinstance(format_func, str) and 'lambda' in format_func else format_func
    )
    return kw


def main(kw):
    return_index = kw.get('return_index')

    c = checkbox(
        items=['item1', 'item2', 'item3', CheckboxItem('item4', disabled=True)],
        **kw
    )
    st.write(f'The selected checkbox {"index" if return_index else "label"} is: {c}')
    with st.expander('code'):
        st.code('''
        checkbox(['item1', 'item2', 'item3', CheckboxItem('item4', disabled=True)])
        ''')


def api():
    st.help(checkbox)
    st.help(CheckboxItem)


CHECKBOX_DEMO = {
    'checkbox': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
