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


def params():
    c = st.columns(2)
    label = c[0].selectbox('label', LABEL, 1)
    position = c[1].selectbox('position', ['top', 'right', 'bottom', 'left'], help='label position')
    index = st.selectbox('index', [0, [0, 1], None])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    radius = st.selectbox('radius', ['xs', 'sm', 'md', 'lg', 'xl'], 3)
    size = st.selectbox('size', ['xs', 'sm', 'md', 'lg', 'xl'], 2)
    align = st.selectbox('align', ["start", "center", "end"], 1)
    direction = st.selectbox('direction', ["horizontal", "vertical"])
    variant = st.selectbox('variant', ['outline', 'light', 'filled'], 2)
    multiple = st.checkbox('multiple')
    return_index = st.checkbox('return_index')
    return update_kw(locals(), ['c'])


def main(kw):
    return_index = kw.get('return_index')
    with st.expander('demo', True):
        seg = sac.chip(
            items=[
                sac.ChipItem(label='apple'),
                sac.ChipItem(icon='google'),
                sac.ChipItem(label='github', icon='github'),
                sac.ChipItem(label='twitter', icon='twitter'),
                sac.ChipItem(label='disabled', disabled=True),
            ], **kw
        )
        st.write(f'The selected segmented {"index" if return_index else "label"} is: {seg}')
    show_code(f'''
    sac.segmented(
        items=[
            sac.SegmentedItem(label='apple'),
            sac.SegmentedItem(icon='google'),
            sac.SegmentedItem(label='github', icon='github'),
            sac.SegmentedItem(label='link', icon='link', href='https://mantine.dev/core/segmented-control/'),
            sac.SegmentedItem(label='disabled', disabled=True),
        ], {code_kw(kw)}
    )
    ''', True)


def api():
    st.help(sac.segmented)
    st.help(sac.SegmentedItem)


CHIP_DEMO = {
    'chip': {
        'params': params,
        'main': main,
        'api': api
    }
}
