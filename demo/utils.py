#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/8/9 17:07
@Author   : ji hao ran
@File     : utils.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from typing import Callable
import streamlit as st
import streamlit_antd_components as sac

FORMAT = [None, 'title', 'upper', "lambda x:f'A_{x}'"]
LABEL = [
    None,
    'label',
    '**label**',
    '**label** <span class="badge rounded-pill badge-info">Info</span>'
]


def update_kw(d: dict, remove_keys: list = None):
    ff = d.get("format_func")
    if isinstance(ff, str) and 'lambda' in ff:
        d.update({"format_func": eval(ff)})
    if remove_keys is not None:
        for i in remove_keys:
            if i in d.keys():
                del d[i]
    return d


def code_kw(d: dict):
    # dict to kw string
    return ", ".join(f'{k}={FORMAT[-1]}' if isinstance(v, Callable) else f'{k}={v!r}' for k, v in d.items())


def show_code(x: str, open: bool = False):
    with st.expander('Code', open):
        st.code(f'''
        import streamlit_antd_components as sac\n{x}
        ''', line_numbers=True)


def show_color(colors: list):
    s = sac.buttons(['select', 'picker'], label='color', size='small', compact=True, position='left', shape='round')
    if s == 'select':
        color = st.selectbox('color', colors, label_visibility='collapsed')
    else:
        color = st.color_picker('color', value='#25C3B0', label_visibility='collapsed')
    return color
