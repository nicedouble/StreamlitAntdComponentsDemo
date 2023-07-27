#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/26 14:36
@Author   : ji hao ran
@File     : steps.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
from streamlit_antd_components import steps, StepsItem


def sidebar():
    index = st.selectbox('index', [0, 1])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    placement = st.selectbox('placement', ["horizontal", "vertical"], help='title placement')
    size = st.selectbox('size', ["default", "small"])
    direction = st.selectbox('direction', ["horizontal", "vertical"])
    type = st.selectbox('type', ['default', 'navigation', 'inline'])
    dot = st.checkbox('dot')
    return_index = st.checkbox('return_index')
    kw = locals()
    kw.update(
        format_func=eval(format_func) if isinstance(format_func, str) and 'lambda' in format_func else format_func)
    return kw


def main(kw):
    return_index = kw.get('return_index')

    st.subheader('demo1')
    s0 = steps(['item1', 'item2', 'item3'], **kw)
    st.write(f'The selected steps {"index" if return_index else "label"} is: {s0}')
    with st.expander('code'):
        st.code('''
        steps(['item1', 'item2', 'item3'])
        ''')

    st.subheader('demo2')
    s2 = steps(
        items=[
            StepsItem(title='step 1', subtitle='extra msg', description='description text'),
            dict(title='step 2'),
            dict(title='step 3'),
            dict(title='step 4', disabled=True),
        ], **kw
    )
    st.write(f'The selected steps {"index" if return_index else "label"} is: {s2}')
    with st.expander('code'):
        st.code('''
        steps(
        items=[
            StepsItem(title='step 1', subtitle='extra msg', description='description text'),
            dict(title='step 2'),
            dict(title='step 3'),
            dict(title='step 4', disabled=True),
        ])
        ''')


def api():
    st.help(steps)
    st.help(StepsItem)


STEPS_DEMO = {
    'steps': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
