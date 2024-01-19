#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/29 11:19
@Author   : ji hao ran
@File     : menu.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    c = st.columns(2)
    index = show_index(c[0], [0, 2], key=key)
    format_func = show_format_func(c[1], key=key)
    size = show_size(key=key)
    variant = show_variant(['light', 'filled', 'subtle', 'left-bar', 'right-bar'], key=key)
    color = show_color(key=key)
    indent = show_radio('indent(px)', [5, 10, 24, 30], index=2, key=key)
    c = st.columns(2)
    height = show_radio('height', [None, 300], c[0], key=key)
    open_index = show_radio('open_index', [None, [1, ]], c[1], key=key)
    open_all = show_checkbox('open_all', c[0], value=True, key=key)
    return_index = show_checkbox('return_index', c[1], key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    return_index = kw.get('return_index')

    with st.expander('demo', True):
        c = st.columns(3)
        with c[1]:
            item = sac.menu([
                sac.MenuItem('home', icon='house-fill',
                             tag=[sac.Tag('Tag1', color='green'), sac.Tag('Tag2', color='red')]),
                sac.MenuItem('products', icon='box-fill', children=[
                    sac.MenuItem('apple', icon='apple'),
                    sac.MenuItem('other', icon='git', description='other items', children=[
                        sac.MenuItem('google', icon='google', description='item description'),
                        sac.MenuItem('gitlab', icon='gitlab'),
                        sac.MenuItem('wechat', icon='wechat'),
                    ]),
                ]),
                sac.MenuItem('disabled', disabled=True),
                sac.MenuItem(type='divider'),
                sac.MenuItem('link', type='group', children=[
                    sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
                    sac.MenuItem('bootstrap-icon', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
                ]),
            ], **kw)
            st.write(f'The selected menu item {"index" if return_index else "label"} : {item}')
    show_code(f'''
    sac.menu([
        sac.MenuItem('home', icon='house-fill', tag=[sac.Tag('Tag1', color='green'), sac.Tag('Tag2', 'red')]),
        sac.MenuItem('products', icon='box-fill', children=[
            sac.MenuItem('apple', icon='apple'),
            sac.MenuItem('other', icon='git', description='other items', children=[
                sac.MenuItem('google', icon='google', description='item description'),
                sac.MenuItem('gitlab', icon='gitlab'),
                sac.MenuItem('wechat', icon='wechat'),
            ]),
        ]),
        sac.MenuItem('disabled', disabled=True),
        sac.MenuItem(type='divider'),
        sac.MenuItem('link', type='group', children=[
            sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
            sac.MenuItem('bootstrap-icon', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
        ]),
    ], {code_kw(kw, sac.menu)})
    ''')


def api():
    st.help(sac.menu)
    st.help(sac.MenuItem)


MENU_DEMO = {
    'menu': {
        'doc': 'A versatile menu for navigation.',
        'params': params,
        'main': main,
        'api': api
    }
}
