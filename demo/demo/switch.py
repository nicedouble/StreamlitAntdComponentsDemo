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


def params(key):
    c = st.columns(2)
    label = show_label(c[0], key=key)
    description = show_description(c[1], key=key)
    on_label = c[0].selectbox('on_label', [None, 'On', 'sac.BsIcon("sun")'])
    off_label = c[1].selectbox('off_label', [None, 'Off', 'sac.BsIcon("moon")'])
    c = st.columns(2)
    with c[0]:
        align = show_align(key=key)
    with c[1]:
        position = show_radio('position', ["right", "left"], key=key)
    size = show_size(include_int=False, key=key)
    radius = show_radius(index=3, key=key)
    c = st.columns(2)
    with c[0]:
        on_color = show_color(label='on_color', key=f'{key}-on')
    with c[1]:
        off_color = show_color(label='off_color', none_color='--secondary-background-color', key=f'{key}-off')
    value = show_checkbox('value', c[0], key=key)
    disabled = show_checkbox('disabled', c[1], key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    if kw.get('on_label') == 'sac.BsIcon("sun")':
        kw.update(on_label=sac.BsIcon("sun"))
    if kw.get('off_label') == 'sac.BsIcon("moon")':
        kw.update(off_label=sac.BsIcon("moon"))

    with st.expander('demo', True):
        show_space()
        s = sac.switch(**kw)
        show_space()
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
