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
    label = c[0].selectbox('label', LABEL, 1, key=f'la-{key}')
    index = st.selectbox('index', [None, 0, [0, 1]], 2, key=f'in-{key}')
    format_func = st.selectbox('format_func', FORMAT, 1, key=f'ff-{key}')
    align = st.selectbox('align', ["start", "center", "end"], 1, key=f'al-{key}')
    position = c[1].selectbox('position', ['top', 'right', 'bottom', 'left'], help='label position', key=f'pos-{key}')
    check_all = st.checkbox('check_all', True, help='show check all box', key=f'ca-{key}')
    disabled = st.checkbox('disabled', key=f'dis-{key}')
    return_index = st.checkbox('return_index', key=f're-{key}')
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
        {code_kw(kw)}
    )
    ''', True)


def api():
    st.help(sac.checkbox)
    st.help(sac.CheckboxItem)


CHECKBOX_DEMO = {
    'checkbox': {
        'params': params,
        'main': main,
        'api': api
    }
}
