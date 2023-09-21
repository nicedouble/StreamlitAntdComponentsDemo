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


def params():
    c = st.columns(2)
    label = c[0].selectbox('label', LABEL)
    position = c[1].selectbox('position', ['top', 'right', 'bottom', 'left'], help='label position')
    index = st.selectbox('index', [0, 1])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    radius = st.radio('radius', ['xs', 'sm', 'md', 'lg', 'xl'], 2, horizontal=True)
    size = st.radio('size', ['xs', 'sm', 'md', 'lg', 'xl'], 2, horizontal=True)
    align = st.radio('align', ["start", "center", "end"], 1, horizontal=True)
    direction = st.radio('direction', ["horizontal", "vertical"], horizontal=True)
    c = st.columns(2)
    grow = c[0].checkbox('grow')
    disabled = c[0].checkbox('disabled')
    readonly = c[1].checkbox('readonly')
    return_index = c[1].checkbox('return_index')
    return update_kw(locals(), ['c'])


def main(kw):
    return_index = kw.get('return_index')
    with st.expander('demo', True):
        seg = sac.segmented(
            items=[
                sac.SegmentedItem(label='apple'),
                sac.SegmentedItem(icon='google'),
                sac.SegmentedItem(label='github', icon='github'),
                sac.SegmentedItem(label='link', icon='link', href='https://mantine.dev/core/segmented-control/'),
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
            sac.SegmentedItem(label='link', icon='link', href='https://mantine.dev/core/segmented-control/'),
            sac.SegmentedItem(label='disabled', disabled=True),
        ], {code_kw(kw, sac.segmented)}
    )
    ''', True)


def api():
    st.help(sac.segmented)
    st.help(sac.SegmentedItem)


SEGMENTED_DEMO = {
    'segmented': {
        'params': params,
        'main': main,
        'api': api
    }
}
