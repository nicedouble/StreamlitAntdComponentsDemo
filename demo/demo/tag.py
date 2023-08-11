#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/8/2 16:55
@Author   : ji hao ran
@File     : tag.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""

from ..utils import *


def sidebar():
    label = st.text_input('label', 'Tag')
    color = show_color([None, 'green', 'gold', 'blue'])
    icon = st.selectbox('icon', [None, 'house', 'twitter'], 1)
    link = st.selectbox('link', [None, 'https://ant.design/components/tag'])
    bordered = st.checkbox('bordered', True)
    closable = st.checkbox('closable', True)
    return update_kw(locals())


def main(kw):
    sac.tag(**kw)
    show_code(f'''
    sac.tag({code_kw(kw)})
    ''', open=True)


def api():
    st.help(sac.tag)


TAG_DEMO = {
    'tag': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
