#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/29 11:19
@Author   : ji hao ran
@File     : menu.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import menu, MenuItem


def sidebar():
    index = st.selectbox('index', [0, 2])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    size = st.slider('size(px)', 10, 20, 16)
    indent = st.slider('indent(px)', 0, 30, 24)
    open_index = st.selectbox('open_index', [None, [1, 3]])
    open_all = st.checkbox('open_all', True)
    return_index = st.checkbox('return_index')
    kw = dict(
        index=index,
        format_func=eval(format_func) if isinstance(format_func, str) and 'lambda' in format_func else format_func,
        size=size,
        indent=indent,
        open_index=open_index,
        open_all=open_all,
        return_index=return_index,
    )
    return kw


def main(kw):
    return_index = kw.get('return_index')

    col = st.columns(4)
    with col[0]:
        st.subheader('demo1')
        item0 = menu([MenuItem(f'menu{i}') for i in range(10)], **kw)
        st.write(f'The selected menu item {"index" if return_index else "label"} : {item0}')
        with st.expander('code'):
            st.code("""
            menu([MenuItem(f'menu{i}') for i in range(10)])
            """)

    with col[2]:
        st.subheader('demo2')
        item1 = menu([
            MenuItem('home', icon='house'),
            MenuItem('app', icon='app', children=[
                MenuItem('store', icon='bag-check'),
                MenuItem('brand', icon='award', children=[
                    MenuItem('github', icon='github'),
                    MenuItem('google', icon='google'),
                    MenuItem('apple', icon='apple', children=[
                        MenuItem('admin', icon='person-circle'),
                        MenuItem('guest', icon='person'),
                        MenuItem('twitter' * 5, icon='twitter'),
                    ]),
                ]),
            ]),
            MenuItem('disabled', icon='send', disabled=True),
            MenuItem(type='divider'),
            MenuItem('reference', type='group', children=[
                MenuItem('antd-menu', icon='heart', href='https://ant.design/components/menu#menu'),
                MenuItem('bootstrap-icon', icon='bootstrap', href='https://icons.getbootstrap.com/'),
                MenuItem('streamlit-components-tutorial', icon='info-circle',
                         href='https://streamlit-components-tutorial.netlify.app/'),
            ]),
        ], **kw)
        st.write(f'The selected menu item {"index" if return_index else "label"} : {item1}')
        with st.expander('code'):
            st.code("""
            menu([
            MenuItem('home', icon='house'),
            MenuItem('app', icon='app', children=[
                MenuItem('store', icon='bag-check'),
                MenuItem('brand', icon='award', children=[
                    MenuItem('github', icon='github'),
                    MenuItem('google', icon='google'),
                    MenuItem('apple', icon='apple', children=[
                        MenuItem('admin', icon='person-circle'),
                        MenuItem('guest', icon='person'),
                    ]),
                ]),
            ]),
            MenuItem('disabled', icon='send', disabled=True),
            MenuItem(type='divider'),
            MenuItem('reference', type='group', children=[
                MenuItem('antd-menu', icon='heart', href='https://ant.design/components/menu#menu'),
                MenuItem('bootstrap-icon', icon='bootstrap', href='https://icons.getbootstrap.com/'),
                MenuItem('streamlit-components-tutorial', icon='info-circle',
                         href='https://streamlit-components-tutorial.netlify.app/'),
            ]),
        ])
            """)
    st.write('---')
    with st.expander('API'):
        st.help(menu)
        st.help(MenuItem)


MENU_DEMO = {
    'menu': {
        'sidebar': sidebar,
        'main': main
    }
}
