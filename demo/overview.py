#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/9/6 14:13
@Author   : ji hao ran
@File     : overview.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
import streamlit_antd_components as sac


def redirect(item=0):
    st.session_state['menu'] = item


def overview():
    st.subheader('Introduce', False)
    st.info(f'''
    :heart: **[Streamlit-antd-components](https://github.com/nicedouble/StreamlitAntdComponents)** is inspired by
     [Ant Design](https://ant.design/components/overview/) and [Mantine](https://v6.mantine.dev/),
     has developed more than 10 custom components to extend streamlit.   
    :heart: All components are designed to fit streamlit theme style.   
    :heart: Support [Bootstrap Icon](https://icons.getbootstrap.com/)(`v1.10.5`).   
    :heart: Give me a :star:  on [Github](https://github.com/nicedouble/StreamlitAntdComponents) if you like this package.
    Issues can be discussed in [Github issues](https://github.com/nicedouble/StreamlitAntdComponents/issues) or [streamlit-community](https://discuss.streamlit.io/t/new-component-streamlit-antd-components-more-widgets-to-extend-streamlit/43313)
    ''')

    st.subheader('Component preview', False)
    c = st.columns(3)
    with c[0].expander('Buttons', True):
        sac.buttons(
            items=[
                sac.ButtonsItem('apple', 'apple'),
                sac.ButtonsItem('google', 'google'),
                sac.ButtonsItem('wechat', 'wechat')
            ],
            format_func='title', align='center',
        )
        st.button('Go to buttons', on_click=redirect, args=('buttons',))
    with c[0].expander('Segmented', True):
        sac.segmented(
            items=[
                sac.SegmentedItem('apple', 'apple'),
                sac.SegmentedItem('google', 'google'),
                sac.SegmentedItem('wechat', 'wechat')
            ],
            format_func='title', align='center', index=1,
        )
        st.button('Go to segmented', on_click=redirect, args=("segmented",))
    with c[0].expander('Chip', True):
        sac.chip(
            items=[
                sac.ChipItem('apple', 'apple'),
                sac.ChipItem('google', 'google'),
                sac.ChipItem('wechat', 'wechat')
            ],
            format_func='title', align='center', index=2,
        )
        st.button('Go to chip', on_click=redirect, args=("chip",))

    with c[1].expander('Menu', True):
        sac.menu(
            items=[
                sac.MenuItem('home', 'house-fill'),
                sac.MenuItem('products', 'box-fill', children=[
                    sac.MenuItem('apple', 'apple'),
                    sac.MenuItem('google', 'google'),
                ]),
            ],
            open_all=True, format_func='title', index=2
        )
        st.button('Go to menu', on_click=redirect, args=("menu",))
    with c[1].expander('Tree', True):
        sac.tree(
            items=[
                sac.TreeItem('home', 'house-fill'),
                sac.TreeItem('products', 'box-fill', children=[
                    sac.TreeItem('apple', 'apple'),
                    sac.TreeItem('google', 'google'),
                ]),
            ],
            open_all=True, format_func='title', checkbox=True, index=0
        )
        st.button('Go to tree', on_click=redirect, args=("tree",))

    with c[2].expander('Transfer', True):
        sac.transfer(
            items=[f'item{i}' for i in range(30)],
            index=[0, 1],
            reload=True,
            height=420
        )
        st.button('Go to transfer', on_click=redirect, args=("transfer",))
    st.caption('Click the sidebar menu to show more components detailed usage.')
