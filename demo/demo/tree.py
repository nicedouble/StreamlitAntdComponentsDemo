#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/29 11:20
@Author   : ji hao ran
@File     : tree.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def sidebar():
    label = st.selectbox('label', [None, 'label'], 1)
    index = st.selectbox('index', [0, 2, [0, 2], None])
    format_func = st.selectbox('format_func', FORMAT, 1)
    icon = st.selectbox('icon', [None, 'table', 'database'], 1)
    height = st.selectbox('height(px)', [None, 300])
    open_index = st.selectbox('open_index', [None, [1, 3]])
    open_all = st.checkbox('open_all', True)
    checkbox = st.checkbox('checkbox', True)
    checkbox_strict = st.checkbox('checkbox_strict')
    multiple = st.checkbox('multiple')
    show_line = st.checkbox('show_line', True)
    return_index = st.checkbox('return_index')
    return update_kw(locals())


def main(kw):
    return_index = kw.get('return_index')

    col = st.columns(2)
    with col[0]:
        st.subheader('demo1')
        item0 = sac.tree(items=[f'item{i}' for i in range(10)], **kw)
        st.write(f'The selected tree item {"index" if return_index else "label"} : {item0}')
        show_code(f'''
        sac.tree(items=[f'item{{i}}' for i in range(10)], {code_kw(kw)})
        ''')
    with col[1]:
        st.subheader('demo2')
        item1 = sac.tree(items=[
            sac.TreeItem('item1'),
            sac.TreeItem('item2', icon='apple', children=[
                sac.TreeItem('item2-1', icon='github'),
                sac.TreeItem('item2-2', children=[
                    sac.TreeItem('item2-2-1'),
                    sac.TreeItem('item2-2-2'),
                    sac.TreeItem('item2-2-3', children=[
                        sac.TreeItem('item2-2-3-1'),
                        sac.TreeItem('item2-2-3-2'),
                        sac.TreeItem('item2-2-3-3'),
                    ]),
                ]),
            ]),
            sac.TreeItem('disabled', disabled=True),
            sac.TreeItem('item3', children=[
                sac.TreeItem('item3-1'),
                sac.TreeItem('item3-2'),
                sac.TreeItem('text' * 30),
            ]),
        ], **kw)
        st.write(f'The selected tree item {"index" if return_index else "label"} : {item1}')
        show_code(f'''
        sac.tree(items=[
            sac.TreeItem('item1'),
            sac.TreeItem('item2', icon='apple', children=[
                sac.TreeItem('item2-1', icon='github'),
                sac.TreeItem('item2-2', children=[
                    sac.TreeItem('item2-2-1'),
                    sac.TreeItem('item2-2-2'),
                    sac.TreeItem('item2-2-3', children=[
                        sac.TreeItem('item2-2-3-1'),
                        sac.TreeItem('item2-2-3-2'),
                        sac.TreeItem('item2-2-3-3'),
                    ]),
                ]),
            ]),
            sac.TreeItem('disabled', disabled=True),
            sac.TreeItem('item3', children=[
                sac.TreeItem('item3-1'),
                sac.TreeItem('item3-2'),
                sac.TreeItem('text' * 30),
            ]),
        ], {code_kw(kw)})''')


def api():
    st.help(sac.tree)
    st.help(sac.TreeItem)


TREE_DEMO = {
    'tree': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
