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
    radius = st.radio('radius', ['xs', 'sm', 'md', 'lg', 'xl'], 2, horizontal=True)
    size = st.radio('size', ['xs', 'sm', 'md', 'lg', 'xl'], 2, horizontal=True)
    align = st.radio('align', ["start", "center", "end"], 1, horizontal=True)
    direction = st.radio('direction', ["horizontal", "vertical"], horizontal=True)
    variant = st.radio('variant', ['outline', 'light', 'filled'], 2, horizontal=True)
    c = st.columns(2)
    multiple = c[0].checkbox('multiple')
    return_index = c[1].checkbox('return_index')
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
        st.write(f'The selected chip {"index" if return_index else "label"} is: {seg}')
    show_code(f'''
    sac.chip(
        items=[
            sac.ChipItem(label='apple'),
            sac.ChipItem(icon='google'),
            sac.ChipItem(label='github', icon='github'),
            sac.ChipItem(label='twitter', icon='twitter'),
            sac.ChipItem(label='disabled', disabled=True),
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
