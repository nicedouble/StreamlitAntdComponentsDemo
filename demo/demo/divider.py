#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/6/13 11:11
@Author   : ji hao ran
@File     : divider.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    c = st.columns(2)
    label = show_label(c[0], key=key)
    icon = c[1].selectbox('icon', [None, 'house'], 1, key=f'{key}-icon')
    align = show_align(key=key)
    size = show_size(index=0, key=key)
    color = show_color(key=key)
    variant = show_variant(['solid', 'dashed', 'dotted'], key=key)
    label_style = st.selectbox('label_style', [None, {'font-size': '20px', 'font-weight': 'bold'}])
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    with st.expander('demo', True):
        st.markdown('<br>' * 3, unsafe_allow_html=True)
        sac.divider(**kw)
        st.markdown('<br>' * 3, unsafe_allow_html=True)
    show_code(f'''
    sac.divider({code_kw(kw, sac.divider)})
    ''', True)


def api():
    st.help(sac.divider)


DIVIDER_DEMO = {
    'divider': {
        'doc': 'A divider line separates different content.',
        'params': params,
        'main': main,
        'api': api
    }
}
