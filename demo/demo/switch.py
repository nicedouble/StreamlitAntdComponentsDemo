#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/6/13 10:43
@Author   : ji hao ran
@File     : switch.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def sidebar():
    label = st.selectbox('label', [None, 'label'])
    value = st.checkbox('value', True)
    checked = st.selectbox('checked', [None, 'yes', 'BsIcon("sun")'])
    unchecked = st.selectbox('unchecked', [None, 'no', 'BsIcon("moon")'])
    align = st.selectbox('align', ["start", "center", "end"])
    position = st.selectbox('position', ["top", "right", "bottom", "left"], help='label position')
    size = st.selectbox('size', ["default", "small", "large"])
    disabled = st.checkbox('disabled')
    return update_kw(locals())


def main(kw):
    s = sac.switch(**kw)
    st.write(f'switch return value: {s}')
    show_code(f'''
    sac.switch({code_kw(kw)})
    ''', True)


def api():
    st.help(sac.switch)
    st.help(sac.BsIcon)


SWITCH_DEMO = {
    'switch': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
