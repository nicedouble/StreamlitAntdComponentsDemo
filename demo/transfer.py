#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/10 13:57
@Author   : ji hao ran
@File     : transfer.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import transfer


def sidebar():
    index = st.selectbox('index', [[0, 1], None])
    label = st.selectbox('label', [None, ['source', 'target'], ['source'], ['', 'target']])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    search = st.checkbox('search')
    pagination = st.checkbox('pagination')
    oneway = st.checkbox('oneway')
    disabled = st.checkbox('disabled')
    width = st.selectbox('width', [None, '100%', 200])
    height = st.selectbox('height', [None, 400])
    return_index = st.checkbox('return_index')
    kw = dict(
        index=index,
        label=label,
        format_func=eval(format_func) if isinstance(format_func, str) and 'lambda' in format_func else format_func,
        search=search,
        pagination=pagination,
        oneway=oneway,
        disabled=disabled,
        width=width,
        height=height,
        return_index=return_index,
    )
    return kw


def main(kw):
    return_index = kw.get('return_index')
    t = transfer(items=[f'item{i}' for i in range(30)], **kw)
    st.write(f'The transfer target item {"index" if return_index else "label"} : {t}')
    with st.expander('code'):
        st.code("transfer(items=[f'item{i}' for i in range(30)], **kw)")


def api():
    st.help(transfer)


TRANSFER_DEMO = {
    'transfer': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
