#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/26 15:12
@Author   : ji hao ran
@File     : checkbox.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    c = st.columns(2)
    label = show_label(c[0], key=key)
    description = show_description(c[1], key=key)
    index = show_index(c[0], [None, 0, [0, 1]], 2, key=key)
    format_func = show_format_func(c[1], key=key)
    align = show_align(key=key)
    size = show_size(key=key, index=1)
    radius = show_radius(index=1)
    color = show_color(key=key)
    check_all = show_radio('check_all', [False, True, 'Select all'], key=key)
    c = st.columns(2)
    disabled = show_checkbox('disabled', c[0], key=key)
    return_index = show_checkbox('return_index', c[1], key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    return_index = kw.get('return_index')
    with st.expander('demo', True):
        show_space()
        c = sac.checkbox(
            items=[
                'item1',
                'item2',
                'item3',
                sac.CheckboxItem('item4', disabled=True)
            ],
            **kw
        )
        show_space()

        st.write(f'The selected checkbox {"index" if return_index else "label"} is: {c}')
    show_code(f'''
    sac.checkbox(
        items=[
            'item1',
            'item2',
            'item3',
            sac.CheckboxItem('item4', disabled=True)
        ],
        {code_kw(kw, sac.checkbox)}
    )
    ''', True)


def api():
    st.help(sac.checkbox)
    st.help(sac.CheckboxItem)


CHECKBOX_DEMO = {
    'checkbox': {
        'doc': 'A group of checkbox.',
        'params': params,
        'main': main,
        'api': api
    }
}
