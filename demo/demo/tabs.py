#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/29 11:04
@Author   : ji hao ran
@File     : tabs.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    c = st.columns([1, 1.5, 1])
    index = show_index(c[0], [0, 1], key=key)
    format_func = show_format_func(c[1], key=key)
    height = c[2].selectbox('height(px)', [None, 150], help='available when position="right" or "left"')
    align = show_align(key=key)
    position = show_radio('position', ["top", "right", "bottom", "left"], key=key)
    size = show_size(key=key)
    variant = show_variant(['default', 'outline'], key=key)
    color = show_color(key=key)
    c = st.columns(2)
    use_container_width = show_checkbox('use_container_width', c[0], key=key)
    return_index = show_checkbox('return_index', c[1], key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    return_index = kw.get('return_index')

    with st.expander('demo', True):
        show_space()
        tab = sac.tabs([
            sac.TabsItem(label='apple'),
            sac.TabsItem(icon='google'),
            sac.TabsItem(label='github', icon='github'),
            sac.TabsItem(label='disabled', disabled=True),
        ], **kw)
        show_space()
        st.write(f'The selected tabs {"index" if return_index else "label"} is: {tab}')
    show_code(f'''
    sac.tabs([
        sac.TabsItem(label='apple'),
        sac.TabsItem(icon='google'),
        sac.TabsItem(label='github', icon='github'),
        sac.TabsItem(label='disabled', disabled=True),
    ], {code_kw(kw, sac.tabs)})
    ''', True)


def api():
    st.help(sac.tabs)
    st.help(sac.TabsItem)


TABS_DEMO = {
    'tabs': {
        'doc': 'A tabs component.',
        'params': params,
        'main': main,
        'api': api
    }
}
