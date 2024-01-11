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
    label = show_label(key=key)
    icon = show_radio('icon', [None, 'house', 'sac.BsIcon("house",size=20)'], index=1, key=key)
    align = show_align(key=key)
    size = show_size(index=0, key=key)
    variant = show_variant(['solid', 'dashed', 'dotted'], key=key)
    color = show_color(none_color='lightgray', index=2, key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    if kw.get('icon') == 'sac.BsIcon("house",size=20)':
        kw.update(icon=sac.BsIcon("house", size=20))
    with st.expander('demo', True):
        show_space()
        sac.divider(**kw)
        show_space()
    show_code(f'''
    sac.divider({code_kw(kw, sac.divider).replace('BsIcon', 'sac.BsIcon').replace(', color=None', '')})
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
