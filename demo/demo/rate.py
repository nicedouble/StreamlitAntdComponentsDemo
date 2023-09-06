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


def callback():
    if st.session_state['half']:
        st.session_state['kv'] = {'min_value': .0, 'max_value': 3.0, 'value': 1.5, 'step': .5}
    else:
        st.session_state['kv'] = {'min_value': 0, 'max_value': 3, 'value': 2}


def sidebar():
    if 'kv' not in st.session_state:
        st.session_state['kv'] = {'min_value': 0, 'max_value': 3, 'value': 2}

    c = st.columns(2)
    label = c[0].selectbox('label', LABEL, 1)
    value = st.number_input('value', **st.session_state['kv'])
    count = st.number_input('count', 5, 100, 5, 5)
    symbol = st.selectbox('symbol', [None, 'A', sac.BsIcon("bell-fill")])
    align = st.selectbox('align', ["start", "center", "end"], 1)
    position = c[1].selectbox('position', ['top', 'right', 'bottom', 'left'], help='label position')
    size = st.number_input('size', 10, 50, 20, 5)
    color = show_color([None, 'orange', 'green'])
    c1 = st.columns([1, 1, 1.5])
    half = c1[0].checkbox('half', on_change=callback, key='half')
    clear = c1[1].checkbox('clear')
    readonly = c1[2].checkbox('readonly')
    return update_kw(locals(), ['c', 'c1'])


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
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
