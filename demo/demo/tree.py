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


def params(key):
    label = st.selectbox('label', LABEL, 1, key=f'la-{key}')
    index = st.selectbox('index', [0, 2, [0, 2], None], key=f'in-{key}')
    format_func = st.selectbox('format_func', FORMAT, 1, key=f'ff-{key}')
    icon = st.selectbox('icon', [None, 'table', 'database'], 1, key=f'ic-{key}')
    height = st.selectbox('height(px)', [None, 300], key=f'h-{key}')
    open_index = st.selectbox('open_index', [None, [1, 3]], key=f'oi-{key}')
    c = st.columns([1, 1.5])
    open_all = c[0].checkbox('open_all', True, key=f'oa-{key}')
    checkbox = c[0].checkbox('checkbox', True, key=f'ch-{key}')
    show_line = c[1].checkbox('show_line', True, key=f'sl-{key}')
    checkbox_strict = c[1].checkbox('checkbox_strict', key=f'cs-{key}')
    return_index = st.checkbox('return_index', key=f're-{key}')
    return update_kw(locals(), ['c'])


def main(kw):
    return_index = kw.get('return_index')

    col = st.columns([1, 1.5])
    with col[0].expander('demo', True):
        item1 = sac.tree(items=[
            sac.TreeItem('item1', tag=sac.Tag('tag', color='red', bordered=False), tooltip='item1 tooltip'),
            sac.TreeItem('item2', icon='apple', tooltip='item2 tooltip', children=[
                sac.TreeItem('item2-1', icon='github', tag='tag0'),
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
    with col[1]:
        show_code(f'''
        sac.tree(items=[
            sac.TreeItem('item1', tag=sac.Tag('tag', color='red', bordered=False), tooltip='item1 tooltip'),
            sac.TreeItem('item2', icon='apple', tooltip='item2 tooltip', children=[
                sac.TreeItem('item2-1', icon='github', tag='tag0'),
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
        ], {code_kw(kw)})''', True)


def api():
    st.help(sac.tree)
    st.help(sac.TreeItem)


TREE_DEMO = {
    'tree': {
        'params': params,
        'main': main,
        'api': api
    }
}
