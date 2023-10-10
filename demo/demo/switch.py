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


def params():
    c = st.columns(2)
    label = c[0].selectbox('label', LABEL, 1)
    value = st.checkbox('value', True)
    checked = st.selectbox('checked', [None, 'yes', 'sac.BsIcon("sun")'])
    unchecked = st.selectbox('unchecked', [None, 'no', 'sac.BsIcon("moon")'])
    align = st.radio('align', ["start", "center", "end"], 1, horizontal=True)
    position = c[1].selectbox('position', ["top", "right", "bottom", "left"], help='label position')
    size = st.radio('size', ["default", "small", "large"], horizontal=True)
    disabled = st.checkbox('disabled')
    return update_kw(locals(), ['c'])


def main(kw):
    if kw.get('checked') == 'sac.BsIcon("sun")':
        kw.update(checked=sac.BsIcon("sun"))
    if kw.get('unchecked') == 'sac.BsIcon("moon")':
        kw.update(unchecked=sac.BsIcon("moon"))

    with st.expander('demo', True):
        s = sac.switch(**kw)
        st.write(f'switch return value: {s}')

    show_code(f'''
        sac.switch({code_kw(kw, sac.switch).replace('BsIcon', 'sac.BsIcon').replace('name=', '')})
        ''', True)


def api():
    st.help(sac.switch)
    st.help(sac.BsIcon)


SWITCH_DEMO = {
    'switch': {
        'doc': 'Switching between two states or on-off state.',
        'params': params,
        'main': main,
        'api': api
    }
}
