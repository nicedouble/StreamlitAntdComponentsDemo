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


def params():
    index = st.selectbox('index', [0, 2])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    size = st.radio('size', ['middle', 'small', 'large'], horizontal=True)
    indent = st.slider('indent(px)', 0, 30, 24)
    open_index = st.selectbox('open_index', [None, [1, 3]])
    open_all = st.checkbox('open_all', True)
    return_index = st.checkbox('return_index')
    return update_kw(locals())


def main(kw):
    return_index = kw.get('return_index')

    with st.expander('demo', True):
        c = st.columns(3)
        with c[1]:
            item = sac.menu([
                sac.MenuItem('home', icon='house-fill'),
                sac.MenuItem('products', icon='box-fill', children=[
                    sac.MenuItem('apple', icon='apple', tag=sac.Tag('USA', color='green', bordered=False)),
                    sac.MenuItem('other', icon='git', children=[
                        sac.MenuItem('google', icon='google'),
                        sac.MenuItem('gitlab', icon='gitlab'),
                        sac.MenuItem('wechat' * 5, icon='wechat'),
                    ]),
                ]),
                sac.MenuItem('disabled', icon='send', disabled=True),
                sac.MenuItem(type='divider'),
                sac.MenuItem('reference', type='group', children=[
                    sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
                    sac.MenuItem('bootstrap-icon', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
                ]),
            ], **kw)
            st.write(f'The selected menu item {"index" if return_index else "label"} : {item}')
    show_code(f'''
    sac.menu([
        sac.MenuItem('home', icon='house-fill'),
        sac.MenuItem('products', icon='box-fill', children=[
            sac.MenuItem('apple', icon='apple', tag=sac.Tag('USA', color='green', bordered=False)),
            sac.MenuItem('other', icon='git', children=[
                sac.MenuItem('google', icon='google'),
                sac.MenuItem('gitlab', icon='gitlab'),
                sac.MenuItem('wechat' * 5, icon='wechat'),
            ]),
        ]),
        sac.MenuItem('disabled', icon='send', disabled=True),
        sac.MenuItem(type='divider'),
        sac.MenuItem('reference', type='group', children=[
            sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
            sac.MenuItem('bootstrap-icon', icon='bootstrap', href='https://icons.getbootstrap.com/'),
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
