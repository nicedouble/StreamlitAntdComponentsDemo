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


def params():
    c = st.columns(2)
    label = c[0].selectbox('label', LABEL, 1)
    position = c[1].selectbox('position', ['top', 'right', 'bottom', 'left'], help='label position')
    container = st.container()
    c1 = st.columns([1, 1, 1.5])
    half = c1[0].checkbox('half')
    clear = c1[1].checkbox('clear')
    readonly = c1[2].checkbox('readonly')
    with container:
        value = st.number_input('value', min_value=.0, max_value=5.0, value=2.0, step=0.5 if half else 1.0)
        count = st.number_input('count', 5, 100, 5, 5)
        symbol = st.selectbox('symbol', [None, 'A', 'sac.BsIcon("bell-fill")'])
        align = st.radio('align', ["start", "center", "end"], 1, horizontal=True)
        size = st.number_input('size', 10, 50, 20, 5)
        color = show_color([None, 'orange', 'green'])
    return update_kw(locals(), ['c', 'c1', 'container'])


def main(kw):
    if kw.get('symbol') == 'sac.BsIcon("bell-fill")':
        kw.update(symbol=sac.BsIcon("bell-fill"))
    with st.expander('demo', True):
        r = sac.rate(**kw)
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
