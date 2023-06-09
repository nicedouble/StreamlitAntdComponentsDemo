#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/29 10:17
@Author   : ji hao ran
@File     : buttons.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import buttons, ButtonsItem


def sidebar():
    index = st.selectbox('index', [0, 1, None])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    align = st.selectbox('align', ["start", "center", "end"])
    direction = st.selectbox('direction', ["horizontal", "vertical"])
    shape = st.selectbox('shape', ["default", "round", "circle"])
    compact = st.checkbox('compact')
    grow = st.checkbox('grow')
    return_index = st.checkbox('return_index')
    kw = dict(
        index=index,
        align=align,
        direction=direction,
        shape=shape,
        compact=compact,
        grow=grow,
        return_index=return_index,
        format_func=eval(format_func) if isinstance(format_func, str) and 'lambda' in format_func else format_func
    )
    return kw


def main(kw):
    return_index = kw.get('return_index')

    st.subheader('demo1')
    btn0 = buttons(['button1', 'button2', 'button3'], **kw)
    st.write(f'The selected button {"index" if return_index else "label"} is: {btn0}')
    with st.expander('code'):
        st.code('''
        buttons(['button1', 'button2', 'button3'])
        ''')

    st.subheader('demo2')
    btn1 = buttons([
        ButtonsItem(icon='chevron-bar-left'),
        ButtonsItem(icon='chevron-left'),
        ButtonsItem(icon='chevron-right'),
        ButtonsItem(icon='chevron-bar-right'),
    ], **kw)
    st.write(f'The selected button {"index" if return_index else "label"} is: {btn1}')
    with st.expander('code'):
        st.code('''
        buttons([
        ButtonsItem(icon='chevron-bar-left'),
        ButtonsItem(icon='chevron-left'),
        ButtonsItem(icon='chevron-right'),
        ButtonsItem(icon='chevron-bar-right'),
    ])
        ''')

    st.subheader('demo3')
    btn2 = buttons(
        items=[
            dict(label='apple', icon='apple'),
            dict(label='google', icon='google'),
            dict(label='github', icon='github'),
            dict(label='disabled', disabled=True),
            dict(label='link', href='https://ant.design/components/button', icon='link'),
        ], **kw
    )
    st.write(f'The selected button {"index" if return_index else "label"} is: {btn2}')
    with st.expander('code'):
        st.code('''
        buttons([
            dict(label='apple', icon='apple'),
            dict(label='google', icon='google'),
            dict(label='github', icon='github'),
            dict(label='disabled', disabled=True),
            dict(label='link', href='https://ant.design/components/button', icon='link'),
        ])
        ''')


def api():
    st.help(buttons)
    st.help(ButtonsItem)


BUTTONS_DEMO = {
    'buttons': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
