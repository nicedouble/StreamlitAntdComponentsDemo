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


def redirect(index=0):
    st.session_state['index'] = index


def overview():
    st.subheader('Introduce', False)
    st.markdown('''
    :heart: This package is mainly inspired by [Ant Design](https://ant.design/components/overview/) and has developed more than 10 components to extend streamlit,
    and help users have more choices to display their data.   
    :heart: All components are designed to fit streamlit theme style.   
    :heart: Support latest version [Bootstrap Icon](https://icons.getbootstrap.com/)(`v1.10.5`).   
    :heart: Give me a :star:  on [Github](https://github.com/nicedouble/StreamlitAntdComponents) if you like this package.
    Issues can be discussed in [Github issues](https://github.com/nicedouble/StreamlitAntdComponents/issues) or [streamlit-community](https://discuss.streamlit.io/t/new-component-streamlit-antd-components-more-widgets-to-extend-streamlit/43313)
    ''')

    st.subheader('Install', False)
    st.code('pip install streamlit-antd-components', language='shell')

    st.subheader('Components', False)
    c = st.columns(3)
    with c[0].expander(':rainbow[Buttons]', True):
        st.write('use `sac.buttons` to display a group of buttons.')
        sac.buttons(
            items=[
                sac.ButtonsItem('btn1', 'house'),
                sac.ButtonsItem('btn2', 'gear', color='orange'),
                sac.ButtonsItem('btn3', 'person', disabled=True)
            ],
            format_func='title', align='center', shape='round'
        )
        st.button('Go to buttons', on_click=redirect, args=(2,))
    with c[0].expander(':rainbow[Checkbox]', True):
        st.write('use `sac.checkbox` to display a group of checkbox.')
        sac.checkbox(
            items=[
                sac.CheckboxItem('apple'),
                sac.CheckboxItem('google'),
                sac.CheckboxItem('twitter', disabled=True)
            ],
            format_func='title', align='center', check_all=True
        )
        st.button('Go to checkbox', on_click=redirect, args=(11,))

    with c[1].expander(':rainbow[Menu]', True):
        st.write('use `sac.menu` to display a nested menu items.')
        sac.menu(
            items=[
                sac.MenuItem('home', 'house', tag='Tag'),
                sac.MenuItem('setting', 'gear', children=[
                    sac.MenuItem('plot', 'bar-chart'),
                    sac.MenuItem('data', 'table')
                ]),
                sac.MenuItem('admin', 'person')
            ],
            open_all=True, format_func='title',
        )
        st.button('Go to menu', on_click=redirect, args=(6,))
    with c[2].expander(':rainbow[Transfer]', True):
        st.write('use `sac.transfer` to display double column choice box.')
        sac.transfer(
            items=[f'item{i}' for i in range(30)],
            index=[0, 1], reload=True,
            format_func='title')
        st.button('Go to transfer', on_click=redirect, args=(15,))
    st.caption('Click the sidebar menu to show more components detailed usage.')
