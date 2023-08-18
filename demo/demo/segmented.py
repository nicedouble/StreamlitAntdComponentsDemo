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


def sidebar():
    index = st.selectbox('index', [0, 1])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    size = st.selectbox('size', ["small", "middle", "large"], 1)
    align = st.selectbox('align', ["start", "center", "end"])
    grow = st.checkbox('grow')
    disabled = st.checkbox('disabled')
    return_index = st.checkbox('return_index')
    return update_kw(locals())


def main(kw):
    sac.alert(message='Warning',
              description='**segmented** will be deprecated in next version! The same effect can be achieved using **buttons** by set `compact=True`',
              type='warning', icon=True, closable=True)
    return_index = kw.get('return_index')

    st.subheader('demo1')
    s0 = sac.segmented(['item1', 'item2', 'item3'], **kw)
    st.write(f'The selected segmented {"index" if return_index else "label"} is: {s0}')
    show_code(f'''
    sac.segmented(['item1', 'item2', 'item3'], {code_kw(kw)})
    ''')

    st.subheader('demo2')
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

    st.subheader('demo3')
    s2 = sac.segmented(
        items=[
            dict(label='apple', icon='apple'),
            dict(label='google', icon='google'),
            dict(label='github', icon='github'),
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
            dict(label='disabled', disabled=True),
        ], {code_kw(kw)}
    )
    ''')

def api():
    st.help(sac.segmented)
    st.help(sac.SegmentedItem)


SEGMENTED_DEMO = {
    'segmented': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
