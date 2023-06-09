#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/29 11:20
@Author   : ji hao ran
@File     : tree.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import tree, TreeItem


def sidebar():
    index = st.selectbox('index', [0, 2, [0, 2], None])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    icon = st.selectbox('icon', [None, 'google', 'twitter'])
    height = st.selectbox('height(px)', [None, 300])
    open_index = st.selectbox('open_index', [None, [1, 11]])
    open_all = st.checkbox('open_all', True)
    checkbox = st.checkbox('checkbox', True)
    checkbox_strict = st.checkbox('checkbox_strict')
    multiple = st.checkbox('multiple')
    show_line = st.checkbox('show_line', True)
    return_index = st.checkbox('return_index')
    kw = dict(
        index=index,
        format_func=eval(format_func) if isinstance(format_func, str) and 'lambda' in format_func else format_func,
        icon=icon,
        height=height,
        open_index=open_index,
        open_all=open_all,
        checkbox=checkbox,
        checkbox_strict=checkbox_strict,
        multiple=multiple,
        show_line=show_line,
        return_index=return_index,
    )
    return kw


def main(kw):
    return_index = kw.get('return_index')

    col = st.columns(2)
    with col[0]:
        st.subheader('demo1')
        item0 = tree([TreeItem(f'item{i}') for i in range(10)], **kw)
        st.write(f'The selected tree item {"index" if return_index else "label"} : {item0}')
        with st.expander('code'):
            st.code("""tree([TreeItem(f'item{i}') for i in range(10)])""")
    with col[1]:
        st.subheader('demo2')
        item1 = tree([
            TreeItem('item1'),
            TreeItem('item2', icon='apple', children=[
                TreeItem('item2-1', icon='github'),
                TreeItem('item2-2', children=[
                    TreeItem('item2-2-1'),
                    TreeItem('item2-2-2'),
                    TreeItem('item2-2-3', children=[
                        TreeItem('item2-2-3-1'),
                        TreeItem('item2-2-3-2'),
                        TreeItem('item2-2-3-3'),
                    ]),
                ]),
            ]),
            TreeItem('disabled', disabled=True),
            TreeItem('item3', children=[
                TreeItem('item3-1'),
                TreeItem('item3-2'),
                TreeItem('text'*30),
            ]),
        ], **kw)
        st.write(f'The selected tree item {"index" if return_index else "label"} : {item1}')
        with st.expander('code'):
            st.code("""
            tree([
                TreeItem('item1'),
                TreeItem('item2', icon='apple', children=[
                    TreeItem('item2-1', icon='github'),
                    TreeItem('item2-2', children=[
                        TreeItem('item2-2-1'),
                        TreeItem('item2-2-2'),
                        TreeItem('item2-2-3', children=[
                            TreeItem('item2-2-3-1'),
                            TreeItem('item2-2-3-2'),
                            TreeItem('item2-2-3-3'),
                        ]),
                    ]),
                ]),
                TreeItem('disabled', disabled=True),
                TreeItem('item3', children=[
                    TreeItem('item3-1'),
                    TreeItem('item3-2'),
                ]),
            ])
            """)
    st.write('---')
    with st.expander('API'):
        st.help(tree)
        st.help(TreeItem)


pass

TREE_DEMO = {
    'tree': {
        'sidebar': sidebar,
        'main': main
    }
}
