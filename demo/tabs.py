#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/29 11:04
@Author   : ji hao ran
@File     : tabs.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import tabs, TabsItem


def sidebar():
    index = st.selectbox('index', [0, 1])
    format_func = st.selectbox('format_func', ["None", 'lambda x:x.title()', 'lambda x:x.upper()'], 1)
    height = st.selectbox('height(px)', [None, 150])
    align = st.selectbox('align', ["start", "center", "end"])
    position = st.selectbox('position', ["top", "right", "bottom", "left"])
    shape = st.selectbox('shape', ['default', 'card'])
    grow = st.checkbox('grow')
    return_index = st.checkbox('return_index')
    kw = dict(
        index=index,
        align=align,
        position=position,
        shape=shape,
        height=height,
        grow=grow,
        return_index=return_index,
        format_func=eval(format_func)
    )
    return kw


def main(kw):
    return_index = kw.get('return_index')

    st.subheader('demo1')
    tab0 = tabs(['tab1', 'tab2', 'tab3'], **kw)
    st.write(f'The selected tab {"index" if return_index else "label"} is: {tab0}')
    with st.expander('code'):
        st.code("tabs(['tab1', 'tab2', 'tab3']")

    st.subheader('demo2')
    tab1 = tabs([
        TabsItem(icon='table'),
        TabsItem(icon='pie-chart-fill'),
        TabsItem(icon='graph-up-arrow'),
        TabsItem(icon='bar-chart'),
    ], **kw)
    st.write(f'The selected tab {"index" if return_index else "label"} is: {tab1}')
    with st.expander('code'):
        st.code("""
        tabs([
        TabsItem(icon='table'),
        TabsItem(icon='pie-chart-fill'),
        TabsItem(icon='graph-up-arrow'),
        TabsItem(icon='bar-chart'),
    ])
        """)

    st.subheader('demo3')
    tab2 = tabs([
        TabsItem('apple', icon='apple'),
        TabsItem('google', icon='google'),
        TabsItem('github', icon='github'),
        TabsItem('disabled', disabled=True),
    ], **kw)
    st.write(f'The selected tab {"index" if return_index else "label"} is: {tab2}')
    with st.expander('code'):
        st.code("""
        tabs([
        TabsItem('apple', icon='apple'),
        TabsItem('google', icon='google'),
        TabsItem('github', icon='github'),
        TabsItem('disabled', disabled=True),
    ])
        """)

    st.write('---')
    with st.expander('API'):
        st.help(tabs)
        st.help(TabsItem)


TABS_DEMO = {
    'tabs': {
        'sidebar': sidebar,
        'main': main
    }
}
