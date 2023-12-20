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


def params():
    c = st.columns(2)
    label = c[0].selectbox('label', LABEL, 1)
    position = c[1].selectbox('position', ['top', 'right', 'bottom', 'left'], help='label position')
    index = st.selectbox('index', [None, 0, [0, 1]], 2)
    format_func = st.selectbox('format_func', FORMAT, 1)
    check_all = st.selectbox('check_all', [False, True, 'Select all'])
    align = st.radio('align', ["start", "center", "end"], 1, horizontal=True)
    disabled = st.checkbox('disabled')
    return_index = st.checkbox('return_index')
    return update_kw(locals(), ['c'])


def main(kw):
    return_index = kw.get('return_index')
    with st.expander('demo', True):
        c = sac.checkbox(
            items=[
                'item1',
                'item2',
                'item3',
                sac.CheckboxItem('item4', disabled=True)
            ],
            **kw
        )
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
