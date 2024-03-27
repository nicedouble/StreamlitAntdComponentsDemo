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
import inspect

FORMAT = [None, 'title', 'upper', "lambda x:f'A_{x}'"]

AntColor = {
    'magenta': '#c41d7f',
    'red': '#cf1322',
    'volcano': '#d4380d',
    'orange': '#d46b08',
    'gold': '#d48806',
    'lime': '#7cb305',
    'green': '#389e0d',
    'cyan': '#08979c',
    'blue': '#0958d9',
    'geekblue': '#1d39c4',
    'purple': '#531dab'
}



def show_color(index=0, label='color', options=(None, '#4682b4', 'rgb(20,80,90)'),
               none_color='--primary-color', key=None, martine=True):
    colors = {'info': 'rgb(0, 66, 128)', 'success': 'rgb(23, 114, 51)', 'warning': 'rgb(146, 108, 5)',
              'error': 'rgb(125, 53, 59)', 'transparent': 'lightgray', None: none_color}
    btn = sac.buttons(
        items=[sac.ButtonsItem(
            label='None' if i is None else i,
            color=colors.get(i) if i in colors.keys() else (i if martine else AntColor.get(i, i))) for i in options
        ],
        label=label, index=index,
        size='xs', gap='xs', variant='filled', radius='lg', key=f'{key}-color'
    )
    return None if btn == 'None' else btn


def show_radio(label=None, options=None, container=None, index=0, key=None):
    if container is not None:
        with container:
            return st.radio(label, options=options, index=index, horizontal=True, key=f'{key}-{label}')
    return st.radio(label, options=options, index=index, horizontal=True, key=f'{key}-{label}')


def show_space(number=3):
    st.markdown('<br>' * number, unsafe_allow_html=True)


def update_kw(d: dict, remove_keys: list = None):
    ff = d.get("format_func")
    if isinstance(ff, str) and 'lambda' in ff:
        d.update({"format_func": eval(ff)})
    label = d.get('label')
    if isinstance(label, str) and not label:
        d.update({'label': None})
    desc = d.get('description')
    if isinstance(desc, str) and not desc:
        d.update({'description': None})
    if remove_keys is not None:
        for i in remove_keys:
            if i in d.keys():
                del d[i]
    return d


def code_kw(kw: dict, _func):
    # func default kw
    default_kw = {
        k: v.default for k, v in inspect.signature(_func).parameters.items() if
        v.default is not inspect.Parameter.empty
    }
    # filter kw
    new_kw = {k: v for k, v in kw.items() if v != default_kw.get(k)}
    # dict to kw string
    return ", ".join(f'{k}={FORMAT[-1]}' if isinstance(v, Callable) else f'{k}={v!r}' for k, v in new_kw.items())


def show_code(x: str, open: bool = False):
    with st.expander('code', open):
        st.code(f'''
        import streamlit_antd_components as sac\n{x}
        ''', line_numbers=True)
