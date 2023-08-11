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


def sidebar():
    label = st.selectbox('label', [None, 'label'], 1)
    index = st.selectbox('index', [None, 0, [0, 1]])
    format_func = st.selectbox('format_func', FORMAT, 1)
    align = st.selectbox('align', ["start", "center", "end"])
    position = st.selectbox('position', ['top', 'right', 'bottom', 'left'], help='label position')
    check_all = st.checkbox('check_all', True, help='show check all box')
    disabled = st.checkbox('disabled')
    return_index = st.checkbox('return_index')
    return update_kw(locals())


def main(kw):
    return_index = kw.get('return_index')

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
        {code_kw(kw)}
    )
    ''', True)


def api():
    st.help(sac.checkbox)
    st.help(sac.CheckboxItem)


CHECKBOX_DEMO = {
    'checkbox': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
