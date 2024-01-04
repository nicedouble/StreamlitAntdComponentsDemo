#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/8/9 15:22
@Author   : ji hao ran
@File     : pagination.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    c = st.columns(3)
    total = c[0].number_input('total', 0, 200, 100, 50)
    index = show_index(c[1], [1, 2], key=key)
    page_size = c[2].number_input('page_size', 5, 20, 10, 5)
    align = st.radio('align', ["start", "center", "end"], 1, horizontal=True, key=key)
    size = show_size(key=key)
    radius = show_radius(key=key)
    variant = show_variant(['light', 'filled', 'outline'], index=2, key=key)
    color = show_color(key=key)
    c = st.columns(2)
    disabled = show_checkbox('disabled', c[0], key=key)
    jump = c[1].checkbox('jump', True)
    simple = c[0].checkbox('simple')
    show_total = c[1].checkbox('show_total', True)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    with st.expander('demo', True):
        show_space()
        r = sac.pagination(**kw)
        show_space()
        st.write(f'The selected pagination number is: {r}')
    show_code(f'''
    sac.pagination({code_kw(kw, sac.pagination)})
    ''', True)


def api():
    st.help(sac.pagination)


PAGINATION_DEMO = {
    'pagination': {
        'doc': 'A long list can be divided into several pages.',
        'params': params,
        'main': main,
        'api': api
    }
}
