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
    c = st.columns(2)
    label = show_label(c[0], key=key)
    description = show_description(c[1], key=key)
    index = show_index(c[0], [None, 0, 2, [0, 2]], index=1, key=key)
    format_func = show_format_func(c[1], key=key)
    align = show_align(key=key)
    size = show_size(key=key)
    color = show_color(key=key)
    c = st.columns(2)
    width = show_radio('width(px)', [None, 350], c[0], key=key)
    height = show_radio('height(px)', [None, 300], c[1], key=key)
    icon = show_radio('icon', [None, 'table'], c[0], index=1, key=key)
    open_index = show_radio('open_index', [None, [1, 3]], c[1], key=key)
    open_all = c[0].checkbox('open_all', True)
    checkbox = c[1].checkbox('checkbox', True)
    show_line = c[0].checkbox('show_line', True)
    checkbox_strict = c[1].checkbox('checkbox_strict')
    return_index = show_checkbox('return_index', key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    return_index = kw.get('return_index')

    with st.expander('demo', True):
        item1 = sac.tree(items=[
            sac.TreeItem('item1', tag=[sac.Tag('Tag', color='red'), sac.Tag('Tag2', color='cyan')]),
            sac.TreeItem('item2', icon='apple', description='item description', children=[
                sac.TreeItem('tooltip', icon='github', tooltip='item tooltip'),
                sac.TreeItem('item2-2', children=[
                    sac.TreeItem('item2-2-1'),
                    sac.TreeItem('item2-2-2'),
                    sac.TreeItem('item2-2-3'),
                ]),
            ]),
            sac.TreeItem('disabled', disabled=True),
            sac.TreeItem('item3', children=[
                sac.TreeItem('item3-1'),
                sac.TreeItem('item3-2'),
            ]),
        ], **kw)
        st.write(f'The selected tree item {"index" if return_index else "label"} : {item1}')
    show_code(f'''
    sac.tree(items=[
        sac.TreeItem('item1', tag=[sac.Tag('Tag', color='red'), sac.Tag('Tag2', color='cyan')]),
        sac.TreeItem('item2', icon='apple', description='item description', children=[
            sac.TreeItem('tooltip', icon='github', tooltip='item tooltip'),
            sac.TreeItem('item2-2', children=[
                sac.TreeItem('item2-2-1'),
                sac.TreeItem('item2-2-2'),
                sac.TreeItem('item2-2-3'),
            ]),
        ]),
        sac.TreeItem('disabled', disabled=True),
        sac.TreeItem('item3', children=[
            sac.TreeItem('item3-1'),
            sac.TreeItem('item3-2'),
        ]),
    ], {code_kw(kw, sac.tree)})''')


def api():
    st.help(sac.tree)
    st.help(sac.TreeItem)


TREE_DEMO = {
    'tree': {
        'doc': 'A hierarchical list structure component.',
        'params': params,
        'main': main,
        'api': api
    }
}
