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


def sidebar():
    label = st.text_input('label', 'divider')
    icon = st.selectbox('icon', [None, 'house'], 1)
    align = st.selectbox('align', ['start', 'center', 'end'], help='label align')
    direction = st.selectbox('direction', ["horizontal", "vertical"])
    dashed = st.checkbox('dashed')
    bold = st.checkbox('bold', help='label font weight bold')
    return locals()


def main(kw):
    sac.divider(**kw)
    show_code(f'''
    sac.divider({code_kw(kw)})
    ''', True)


def api():
    st.help(sac.divider)


DIVIDER_DEMO = {
    'divider': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
