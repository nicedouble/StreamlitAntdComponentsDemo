#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/26 15:12
@Author   : ji hao ran
@File     : rate.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    c = st.columns(2)
    label = show_label(c[0], key=key)
    description = show_description(c[1], key=key)
    container = st.container()
    c1 = st.columns([1, 1, 1.5])
    half = show_checkbox('half', c1[0], key=key)
    with container:
        c = st.columns(2)
        value = c[0].number_input('value', min_value=.0, max_value=5.0, value=2.0, step=0.5 if half else 1.0)
        count = c[1].number_input('count', 5, 100, 5, 5)
        symbol = show_radio('symbol', [None, 'A', 'sac.BsIcon("bell-fill")'], key=key)
        align = show_align(key=key)
        size = show_size(key=key)
        color = show_color(key=key)
    return update_kw(locals(), ['c', 'c1', 'container', 'key'])


def main(kw):
    if kw.get('symbol') == 'sac.BsIcon("bell-fill")':
        kw.update(symbol=sac.BsIcon("bell-fill"))
    with st.expander('demo', True):
        show_space()
        r = sac.rate(**kw)
        show_space()
        st.write(f'The rate value is: {r}')
    show_code(f'''
    sac.rate({code_kw(kw, sac.rate).replace('BsIcon', 'sac.BsIcon').replace('name=', '')})
    ''', True)


def api():
    st.help(sac.rate)


RATE_DEMO = {
    'rate': {
        'doc': 'Rate component.',
        'params': params,
        'main': main,
        'api': api
    }
}
