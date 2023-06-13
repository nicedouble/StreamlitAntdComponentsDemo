#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/6/13 11:17
@Author   : ji hao ran
@File     : sascader.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import cascader, CasItem


def sidebar():
    index = st.selectbox('index', [None, 0, [1, 3, 6, 7]])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    placeholder = st.text_input('placeholder', 'Please choose')
    multiple = st.checkbox('multiple')
    disabled = st.checkbox('disabled')
    search = st.checkbox('search')
    clear = st.checkbox('clear')
    strict = st.checkbox('strict')
    return_index = st.checkbox('return_index')
    kw = dict(
        index=index,
        format_func=eval(format_func) if isinstance(format_func, str) and 'lambda' in format_func else format_func,
        placeholder=placeholder,
        multiple=multiple,
        disabled=disabled,
        search=search,
        clear=clear,
        strict=strict,
        return_index=return_index,
    )
    return kw


def main(kw):
    return_index = kw.get('return_index')

    item = cascader([
        CasItem('home', icon='house'),
        CasItem('app', icon='app', children=[
            CasItem('store', icon='bag-check'),
            CasItem('brand', icon='award', children=[
                CasItem('github', icon='github'),
                CasItem('google', icon='google'),
                CasItem('apple', icon='apple', children=[
                    CasItem('admin', icon='person-circle'),
                    CasItem('guest', icon='person'),
                    CasItem('twitter' * 5, icon='twitter'),
                ]),
            ]),
        ]),
        CasItem('disabled', icon='send', disabled=True),
    ], **kw)
    st.write(f'The selected cascader item {"index" if return_index else "label"} : {item}')
    with st.expander('code'):
        st.code("""
        cascader([
        CasItem('home', icon='house'),
        CasItem('app', icon='app', children=[
            CasItem('store', icon='bag-check'),
            CasItem('brand', icon='award', children=[
                CasItem('github', icon='github'),
                CasItem('google', icon='google'),
                CasItem('apple', icon='apple', children=[
                    CasItem('admin', icon='person-circle'),
                    CasItem('guest', icon='person'),
                    CasItem('twitter' * 5, icon='twitter'),
                ]),
            ]),
        ]),
        CasItem('disabled', icon='send', disabled=True),
    ])
        """)


def api():
    st.help(cascader)
    st.help(CasItem)


CASCADER_DEMO = {
    'cascader': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
