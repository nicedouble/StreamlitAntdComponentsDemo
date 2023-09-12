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
    index = st.selectbox('index', [0, 1], key=f'in-{key}')
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1, key=f'ff-{key}')
    radius = st.selectbox('radius', ['xs', 'sm', 'md', 'lg', 'xl'], 2, key=f'rad-{key}')
    size = st.selectbox('size', ['xs', 'sm', 'md', 'lg', 'xl'], 2, key=f'si-{key}')
    align = st.selectbox('align', ["start", "center", "end"], 1, key=f'al-{key}')
    direction = st.selectbox('direction', ["horizontal", "vertical"], key=f'dir-{key}')
    c = st.columns(2)
    grow = c[0].checkbox('grow', key=f'grow-{key}')
    disabled = c[0].checkbox('disabled', key=f'dis-{key}')
    readonly = c[1].checkbox('readonly', key=f'read-{key}')
    return_index = c[1].checkbox('return_index', key=f're-{key}')
    return update_kw(locals(), ['c'])


def main(kw):
    return_index = kw.get('return_index')

    st.subheader('demo1', False)
    s0 = sac.segmented(['item1', 'item2', 'item3'], **kw)
    st.write(f'The selected segmented {"index" if return_index else "label"} is: {s0}')
    show_code(f'''
    sac.segmented(['item1', 'item2', 'item3'], {code_kw(kw)})
    ''')

    st.subheader('demo2', False)
    s1 = sac.segmented([
        sac.SegmentedItem(icon='chevron-bar-left'),
        sac.SegmentedItem(icon='chevron-left'),
        sac.SegmentedItem(icon='chevron-right'),
        sac.SegmentedItem(icon='chevron-bar-right'),
    ], **kw)
    st.write(f'The selected segmented {"index" if return_index else "label"} is: {s1}')
    show_code(f'''
    sac.segmented([
        sac.SegmentedItem(icon='chevron-bar-left'),
        sac.SegmentedItem(icon='chevron-left'),
        sac.SegmentedItem(icon='chevron-right'),
        sac.SegmentedItem(icon='chevron-bar-right'),
    ], {code_kw(kw)}
    )
    ''')

    st.subheader('demo3', False)
    s2 = sac.segmented(
        items=[
            dict(label='apple', icon='apple'),
            dict(label='google', icon='google'),
            dict(label='github', icon='github'),
            dict(label='link', icon='link', href='https://mantine.dev/core/segmented-control/'),
            dict(label='disabled', disabled=True),
        ], **kw
    )
    st.write(f'The selected segmented {"index" if return_index else "label"} is: {s2}')
    show_code(f'''
    sac.segmented(
        items=[
            dict(label='apple', icon='apple'),
            dict(label='google', icon='google'),
            dict(label='github', icon='github'),
            dict(label='link', icon='link', href='https://mantine.dev/core/segmented-control/'),
            dict(label='disabled', disabled=True),
        ], {code_kw(kw)}
    )
    ''')


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
