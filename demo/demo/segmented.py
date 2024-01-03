#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/11 16:22
@Author   : ji hao ran
@File     : segmented.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    c = st.columns(2)
    label = show_label(c[0], key=key)
    description = show_description(c[1], key=key)
    index = show_index(c[0], [0, 1], key=key)
    format_func = show_format_func(c[1], key=key)
    size = show_size(key=key)
    radius = show_radius(key=key)
    c = st.columns(2)
    with c[0]:
        color = show_color(key=key)
    with c[1]:
        bg_color = show_color(label='bg_color', options=(None, *MartineColor, 'transparent'), key=f'{key}-bg')
    align = show_align(key=key)
    direction = show_direction(key=key)
    c = st.columns(2)
    divider = show_checkbox('divider', c[0], True, key=key)
    use_container_width = show_checkbox('use_container_width', c[1], key=key)
    disabled = show_checkbox('disabled', c[0], key=key)
    readonly = show_checkbox('readonly', c[1], key=key)
    return_index = show_checkbox('return_index', c[0], key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    return_index = kw.get('return_index')
    with st.expander('demo', True):
        seg = sac.segmented(
            items=[
                sac.SegmentedItem(label='apple'),
                sac.SegmentedItem(icon='google'),
                sac.SegmentedItem(label='github', icon='github'),
                sac.SegmentedItem(label='link', icon='share-fill', href='https://mantine.dev/core/segmented-control/'),
                sac.SegmentedItem(label='disabled', disabled=True),
            ], **kw
        )
        st.write(f'The selected segmented {"index" if return_index else "label"} is: {seg}')
    show_code(f'''
    sac.segmented(
        items=[
            sac.SegmentedItem(label='apple'),
            sac.SegmentedItem(icon='google'),
            sac.SegmentedItem(label='github', icon='github'),
            sac.SegmentedItem(label='link', icon='share-fill', href='https://mantine.dev/core/segmented-control/'),
            sac.SegmentedItem(label='disabled', disabled=True),
        ], {code_kw(kw, sac.segmented)}
    )
    ''', True)


def api():
    st.help(sac.segmented)
    st.help(sac.SegmentedItem)


SEGMENTED_DEMO = {
    'segmented': {
        'doc': 'A linear set of two or more segments.',
        'params': params,
        'main': main,
        'api': api
    }
}
