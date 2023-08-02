#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/8/2 16:55
@Author   : ji hao ran
@File     : tag.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import tag, TagItem


def sidebar():
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    align = st.selectbox('align', ["start", "center", "end"])
    direction = st.selectbox('direction', ["horizontal", "vertical"])
    kw = locals()
    kw.update(
        format_func=eval(format_func) if isinstance(format_func, str) and 'lambda' in format_func else format_func)
    return kw


def main(kw):
    st.subheader('demo1')
    tag(['tag1', 'tag2', 'tag3'], **kw)
    with st.expander('code'):
        st.code('''
        tag(['tag1', 'tag2', 'tag3'])
        ''')

    st.subheader('demo2')
    tag([
        TagItem(label='red', icon='house', color='red'),
        TagItem(label='blue', icon='gear', color='blue', bordered=False),
        TagItem(label='orange', icon='google', color='orange', bordered=False),
        TagItem(label='link', icon='twitter', color='cyan', link='https://ant.design/components/tag'),
    ], **kw)
    with st.expander('code'):
        st.code('''
        tag([
        TagItem(label='red', icon='house', color='red'),
        TagItem(label='blue', icon='gear', color='blue', bordered=False),
        TagItem(label='orange', icon='google', color='orange', bordered=False),
        TagItem(label='link', icon='twitter', color='cyan',link='https://ant.design/components/tag'),
    ]''')


def api():
    st.help(tag)
    st.help(TagItem)


TAG_DEMO = {
    'tag': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
