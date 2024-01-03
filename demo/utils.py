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
LABEL = [
    None,
    'label',
    '**label**',
    '**label** <span class="badge rounded-pill badge-info">Info</span>'
]
MartineColor = ['dark', 'gray', 'red', 'pink', 'grape', 'violet', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime',
                'yellow', 'orange']
MartineSize = ['xs', 'sm', 'md', 'lg', 'xl']


def show_label(container=None, value='label', key=None):
    if container is not None:
        with container:
            return st.text_input('label', value, key=f'{key}-label')
    return st.text_input('label', value, key=f'{key}-label')


def show_description(container=None, value='', key=None):
    if container is not None:
        with container:
            return st.text_input('description', value, key=f'{key}-desc')
    return st.text_input('description', value, key=f'{key}-desc')


def show_index(container=None, option=None, index=0, key=None):
    if container is not None:
        with container:
            return st.selectbox('index', option, index=index, key=f'{key}-index')
    return st.selectbox('index', option, index=index, key=f'{key}-index')


def show_format_func(container=None, key=None):
    if container is not None:
        with container:
            return st.selectbox('format_func', FORMAT, 0, key=f'{key}-format')
    return st.selectbox('format_func', FORMAT, 0, key=f'{key}-format')


def show_color(index=0, label='color', options=(None, *MartineColor, '#4682b4', 'rgb(20,80,90)'), key=None):
    # return st.radio(label, options, index=index, horizontal=True, key=f'{key}-color')
    colors = {'info': 'rgb(0, 66, 128)', 'success': 'rgb(23, 114, 51)', 'warning': 'rgb(146, 108, 5)',
              'error': 'rgb(125, 53, 59)', 'transparent': 'lightgray'}
    btn = sac.buttons(
        items=[sac.ButtonsItem(
            label='None' if i is None else i,
            color=colors.get(i) if i in colors.keys() else i) for i in options], label=label, index=index,
        size='xs', key=f'{key}-color', variant='filled',
    )
    return None if btn == 'None' else btn


def show_size(index=2, include_int=True, key=None):
    return st.radio('size', options=MartineSize + [25] if include_int else MartineSize, index=index, horizontal=True,
                    key=f'{key}-size')


def show_radius(index=2, key=None):
    return st.radio('radius', MartineSize + [20, 2], index=index, horizontal=True, key=f'{key}-radius')


def show_variant(options, index=0, key=None):
    return st.radio('variant', options, index=index, horizontal=True, key=f'{key}-variant')


def show_align(index=1, key=None):
    return st.radio('align', ['start', 'center', 'end'], index=index, horizontal=True, key=f'{key}-align')


def show_direction(index=0, key=None):
    return st.radio('direction', ["horizontal", "vertical"], index=index, horizontal=True, key=f'{key}-direction')


def show_checkbox(label, container=None, value=False, key=None):
    if container is not None:
        with container:
            return st.checkbox(label, value=value, key=f'{key}-{label}')
    return st.checkbox(label, value=value, key=f'{key}-{label}')


def show_radio(label=None, options=None, container=None, index=0, key=None):
    if container is not None:
        with container:
            return st.radio(label, options=options, index=index, horizontal=True, key=f'{key}-{label}')
    return st.radio(label, options=options, index=index, horizontal=True, key=f'{key}-{label}')


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
