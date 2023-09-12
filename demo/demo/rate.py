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
    label = c[0].selectbox('label', LABEL, 1, key=f'la-{key}')
    position = c[1].selectbox('position', ['top', 'right', 'bottom', 'left'], help='label position', key=f'pos-{key}')
    container = st.container()
    c1 = st.columns([1, 1, 1.5])
    half = c1[0].checkbox('half', key='half')
    clear = c1[1].checkbox('clear', key=f'cl-{key}')
    readonly = c1[2].checkbox('readonly', key=f'read-{key}')
    with container:
        value = st.number_input('value', min_value=.0, max_value=5.0, value=2.0, step=0.5 if half else 1.0,
                                key=f'va-{key}')
        count = st.number_input('count', 5, 100, 5, 5, key=f'co-{key}')
        symbol = st.selectbox('symbol', [None, 'A', sac.BsIcon("bell-fill")], key=f'sy-{key}')
        align = st.selectbox('align', ["start", "center", "end"], 1, key=f'al-{key}')
        size = st.number_input('size', 10, 50, 20, 5, key=f'si-{key}')
        color = show_color([None, 'orange', 'green'], key=f'co-{key}')
    return update_kw(locals(), ['c', 'c1', 'container'])


def main(kw):
    with st.expander('demo', True):
        r = sac.rate(**kw)
        st.write(f'The rate value is: {r}')
    show_code(f'''
    sac.rate({code_kw(kw)})
    ''', True)


def api():
    st.help(sac.rate)


RATE_DEMO = {
    'rate': {
        'params': params,
        'main': main,
        'api': api
    }
}
