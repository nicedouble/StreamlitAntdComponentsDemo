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


def sidebar():
    index = st.selectbox('index', [0, 2])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    size = st.selectbox('size', ['middle', 'small', 'large'])
    indent = st.slider('indent(px)', 0, 30, 24)
    open_index = st.selectbox('open_index', [None, [1, 3]])
    open_all = st.checkbox('open_all', True)
    return_index = st.checkbox('return_index')
    return update_kw(locals())


def main(kw):
    return_index = kw.get('return_index')

    col = st.columns([1, 0.1, 1])
    with col[0]:
        st.subheader('demo1')
        item0 = sac.menu([f'menu{i}' for i in range(10)], **kw)
        st.write(f'The selected menu item {"index" if return_index else "label"} : {item0}')
        show_code(f'''
        sac.menu([f'menu{{i}}' for i in range(10)], {code_kw(kw)})
        ''')

    with col[-1]:
        st.subheader('demo2')
        item1 = sac.menu([
            sac.MenuItem('home', icon='house', tag='Tag'),
            sac.MenuItem('app', icon='app', children=[
                sac.MenuItem('store', icon='bag-check'),
                sac.MenuItem('brand', icon='award', children=[
                    sac.MenuItem('github', icon='github'),
                    sac.MenuItem('apple', icon='apple'),
                ]),
            ]),
            sac.MenuItem('multipleline' * 10, icon='twitter'),
            sac.MenuItem('disabled', icon='send', disabled=True),
            sac.MenuItem(type='divider'),
            sac.MenuItem('reference', type='group', children=[
                sac.MenuItem('antd-menu', icon='heart', href='https://ant.design/components/menu#menu'),
                sac.MenuItem('bootstrap-icon', icon='bootstrap', href='https://icons.getbootstrap.com/'),
            ]),
        ], **kw)
        st.write(f'The selected menu item {"index" if return_index else "label"} : {item1}')
        show_code(f'''
        sac.menu([
            sac.MenuItem('home', icon='house', tag='Tag'),
            sac.MenuItem('app', icon='app', children=[
                sac.MenuItem('store', icon='bag-check'),
                sac.MenuItem('brand', icon='award', children=[
                    sac.MenuItem('github', icon='github'),
                    sac.MenuItem('apple', icon='apple'),
                ]),
            ]),
            sac.MenuItem('multipleline' * 10, icon='twitter'),
            sac.MenuItem('disabled', icon='send', disabled=True),
            sac.MenuItem(type='divider'),
            sac.MenuItem('reference', type='group', children=[
                sac.MenuItem('antd-menu', icon='heart', href='https://ant.design/components/menu#menu'),
                sac.MenuItem('bootstrap-icon', icon='bootstrap', href='https://icons.getbootstrap.com/'),
            ]),
        ], {code_kw(kw)})
        ''')


def api():
    st.help(sac.menu)
    st.help(sac.MenuItem)


MENU_DEMO = {
    'menu': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
