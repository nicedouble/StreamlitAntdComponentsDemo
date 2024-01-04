#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/9/15 16:16
@Author   : ji hao ran
@File     : chip.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    c = st.columns(2)
    label = show_label(c[0], key=key)
    description = show_description(c[1], key=key)
    index = show_index(c[0], [0, [0, 2], None], 1, key=key)
    format_func = show_format_func(c[1], key=key)
    with c[0]:
        align = show_align(key=key)
    with c[1]:
        direction = show_direction(key=key)
    size = show_size(key=key)
    radius = show_radius(key=key)
    variant = show_variant(['outline', 'light', 'filled'], 2, key=key)
    color = show_color(key=key)
    c = st.columns(2)
    multiple = show_checkbox('multiple', c[0], True, key=key)
    return_index = show_checkbox('return_index', c[1], key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    return_index = kw.get('return_index')
    with st.expander('demo', True):
        show_space()
        seg = sac.chip(
            items=[
                sac.ChipItem(label='apple'),
                sac.ChipItem(icon='google'),
                sac.ChipItem(label='github', icon='github'),
                sac.ChipItem(label='twitter', icon='twitter'),
                sac.ChipItem(label='disabled', disabled=True),
            ], **kw
        )
        show_space()
        st.write(f'The selected chip {"index" if return_index else "label"} is: {seg}')
    show_code(f'''
    sac.chip(
        items=[
            sac.ChipItem(label='apple'),
            sac.ChipItem(icon='google'),
            sac.ChipItem(label='github', icon='github'),
            sac.ChipItem(label='twitter', icon='twitter'),
            sac.ChipItem(label='disabled', disabled=True),
        ], {code_kw(kw, sac.chip)}
    )
    ''', True)


def api():
    st.help(sac.segmented)
    st.help(sac.SegmentedItem)


CHIP_DEMO = {
    'chip': {
        'doc': 'Pick one or multiple values with inline controls.',
        'params': params,
        'main': main,
        'api': api
    }
}
