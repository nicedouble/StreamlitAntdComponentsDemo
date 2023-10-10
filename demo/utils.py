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
import base64
from pathlib import Path

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


@st.cache_data
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


def show_color(colors: list):
    s = sac.buttons(['select', 'picker'], label='color', size='small', compact=True, position='left', shape='round')
    if s == 'select':
        color = st.selectbox('color', colors, label_visibility='collapsed')
    else:
        color = st.color_picker('color', value='#25C3B0', label_visibility='collapsed')
    return color


def show_image(img_path, width: str = None, height: str = None, svg=False):
    img_path = Path(img_path) if isinstance(img_path, str) else img_path
    img_str = base64.b64encode(img_path.read_bytes()).decode()
    default_css = "text-align:center"
    if svg:
        img_src = f'data:image/svg+xml;base64,{img_str}'
    else:
        img_src = f'data:image/png;base64,{img_str}'
    img_html = f"""
    <div>
    <img src={img_src} width={width} height={height}>
    </div>
    """
    st.markdown(img_html, unsafe_allow_html=True)
