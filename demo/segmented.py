#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/11 16:22
@Author   : ji hao ran
@File     : segmented.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import segmented, SegmentedItem


def sidebar():
    index = st.selectbox('index', [0, 1])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    size = st.selectbox('size', ["small", "middle", "large"], 1)
    align = st.selectbox('align', ["start", "center", "end"])
    grow = st.checkbox('grow')
    disabled = st.checkbox('disabled')
    return_index = st.checkbox('return_index')
    kw = dict(
        index=index,
        size=size,
        align=align,
        disabled=disabled,
        grow=grow,
        return_index=return_index,
        format_func=eval(format_func) if isinstance(format_func, str) and 'lambda' in format_func else format_func
    )
    return kw


def main(kw):
    return_index = kw.get('return_index')

    st.subheader('demo1')
    s0 = segmented(['item1', 'item2', 'item3'], **kw)
    st.write(f'The selected segmented {"index" if return_index else "label"} is: {s0}')
    with st.expander('code'):
        st.code('''
        segmented(['item1', 'item2', 'item3'])
        ''')

    st.subheader('demo2')
    s1 = segmented([
        SegmentedItem(icon='chevron-bar-left'),
        SegmentedItem(icon='chevron-left'),
        SegmentedItem(icon='chevron-right'),
        SegmentedItem(icon='chevron-bar-right'),
    ], **kw)
    st.write(f'The selected segmented {"index" if return_index else "label"} is: {s1}')
    with st.expander('code'):
        st.code('''
        segmented([
        SegmentedItem(icon='chevron-bar-left'),
        SegmentedItem(icon='chevron-left'),
        SegmentedItem(icon='chevron-right'),
        SegmentedItem(icon='chevron-bar-right'),
    ])
        ''')

    st.subheader('demo3')
    s2 = segmented(
        items=[
            dict(label='apple', icon='apple'),
            dict(label='google', icon='google'),
            dict(label='github', icon='github'),
            dict(label='disabled', disabled=True),
        ], **kw
    )
    st.write(f'The selected segmented {"index" if return_index else "label"} is: {s2}')
    with st.expander('code'):
        st.code('''
        segmented(items=[
            dict(label='apple', icon='apple'),
            dict(label='google', icon='google'),
            dict(label='github', icon='github'),
            dict(label='disabled', disabled=True),
            dict(label='link', href='https://ant.design/components/button', icon='link'),
        ])
        ''')


def api():
    st.help(segmented)
    st.help(SegmentedItem)


SEGMENTED_DEMO = {
    'segmented': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
