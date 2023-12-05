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
    color = st.selectbox('color', [None] + MartineColor)
    variant = st.radio('variant', ['solid', 'dashed', 'dotted'], horizontal=True)
    size = st.radio('size', MartineSize, horizontal=True)
    label_style = st.selectbox('label_style', [None, {'font-size': '20px', 'font-weight': 'bold'}])
    return locals()


def main(kw):
    with st.expander('demo', True):
        st.markdown('<br>' * 3, unsafe_allow_html=True)
        sac.divider(**kw)
        st.markdown('<br>' * 3, unsafe_allow_html=True)
    show_code(f'''
    sac.divider({code_kw(kw, sac.divider)})
    ''', True)


def api():
    st.help(sac.divider)


DIVIDER_DEMO = {
    'divider': {
        'doc': 'A divider line separates different content.',
        'params': params,
        'main': main,
        'api': api
    }
}
