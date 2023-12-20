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
    label = c[0].selectbox('label', [None, 'label'], 1)
    description = c[1].selectbox('description', [None, 'description'])
    value = st.checkbox('value')
    on_label = c[0].selectbox('on_label', [None, 'On', 'sac.BsIcon("sun")'])
    off_label = c[1].selectbox('off_label', [None, 'Off', 'sac.BsIcon("moon")'])
    align = st.radio('align', ["start", "center", "end"], 1, horizontal=True)
    position = st.radio('position', ["right", "left"], horizontal=True)
    size = st.radio('size', MartineSize, index=1, horizontal=True)
    radius = st.radio('radius', MartineSize, index=4, horizontal=True)
    on_color = c[0].selectbox('on_color', [None] + MartineColor)
    off_color = c[1].selectbox('off_color', [None] + MartineColor)
    disabled = st.checkbox('disabled')
    return update_kw(locals(), ['c'])


def main(kw):
    if kw.get('on_label') == 'sac.BsIcon("sun")':
        kw.update(on_label=sac.BsIcon("sun"))
    if kw.get('off_label') == 'sac.BsIcon("moon")':
        kw.update(off_label=sac.BsIcon("moon"))

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
