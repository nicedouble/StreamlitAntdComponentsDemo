#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/29 10:17
@Author   : ji hao ran
@File     : buttons.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    c = st.columns(2)
    label = show_label(c[0], key=key)
    description = show_description(c[1], key=key)
    index = show_index(c[0], [0, 1, None], key=key)
    format_func = show_format_func(c[1], key=key)
    with c[0]:
        align = show_align(key=key)
    with c[1]:
        direction = show_direction(key=key)
    size = show_size(key=key)
    radius = show_radius(key=key)
    variant = show_variant(['filled', 'outline', 'dashed', 'text', 'link'], index=1, key=key)
    color = show_color(key=key)
    c = st.columns(2)
    compact = c[0].checkbox('compact')
    return_index = show_checkbox('return_index', c[1], key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    return_index = kw.get('return_index')

    with st.expander('demo', True):
        show_space()
        btn = sac.buttons([
            sac.ButtonsItem(label='button'),
            sac.ButtonsItem(icon='apple'),
            sac.ButtonsItem(label='google', icon='google', color='#25C3B0'),
            sac.ButtonsItem(label='wechat', icon='wechat'),
            sac.ButtonsItem(label='disabled', disabled=True),
            sac.ButtonsItem(label='link', icon='share-fill', href='https://ant.design/components/button'),
        ], **kw)
        show_space()
        st.write(f'The selected button {"index" if return_index else "label"} is: {btn}')
    show_code(f'''
    sac.buttons([
        sac.ButtonsItem(label='button'),
        sac.ButtonsItem(icon='apple'),
        sac.ButtonsItem(label='google', icon='google', color='#25C3B0'),
        sac.ButtonsItem(label='wechat', icon='wechat'),
        sac.ButtonsItem(label='disabled', disabled=True),
        sac.ButtonsItem(label='link', icon='share-fill', href='https://ant.design/components/button'),
    ], {code_kw(kw, sac.buttons)})
    ''', True)


def api():
    st.help(sac.buttons)
    st.help(sac.ButtonsItem)


BUTTONS_DEMO = {
    'buttons': {
        'doc': 'A group of buttons component.',
        'params': params,
        'main': main,
        'api': api
    }
}
