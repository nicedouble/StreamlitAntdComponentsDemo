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


def params(key):
    label = st.text_input('label', 'divider', key=f'la-{key}')
    icon = st.selectbox('icon', [None, 'house'], 1, key=f'ic-{key}')
    align = st.selectbox('align', ['start', 'center', 'end'], 1, help='label align', key=f'al-{key}')
    direction = st.selectbox('direction', ["horizontal", "vertical"], key=f'dir-{key}')
    dashed = st.checkbox('dashed', key=f'da-{key}')
    bold = st.checkbox('bold', help='label font weight bold', key=f'bo-{key}')
    return locals()


def main(kw):
    with st.expander('demo', True):
        sac.divider(**kw)
    show_code(f'''
    sac.divider({code_kw(kw)})
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
