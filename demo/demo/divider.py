#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/6/13 11:11
@Author   : ji hao ran
@File     : divider.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params():
    label = st.text_input('label', 'divider')
    icon = st.selectbox('icon', [None, 'house'], 1)
    align = st.radio('align', ['start', 'center', 'end'], 1, help='label align', horizontal=True)
    direction = st.radio('direction', ["horizontal", "vertical"], horizontal=True)
    dashed = st.checkbox('dashed')
    bold = st.checkbox('bold', help='label font weight bold')
    return locals()


def main(kw):
    with st.expander('demo', True):
        sac.divider(**kw)
    show_code(f'''
    sac.divider({code_kw(kw, sac.divider)})
    ''', True)


def api():
    st.help(sac.divider)


DIVIDER_DEMO = {
    'divider': {
        'params': params,
        'main': main,
        'api': api
    }
}
