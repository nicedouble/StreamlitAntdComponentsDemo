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


def params(key):
    label = st.text_input('label', 'Tag', key=f'la-{key}')
    color = show_color([None, 'green', 'gold', 'blue'], key=f'co-{key}')
    icon = st.selectbox('icon', [None, 'house', 'twitter'], 1, key=f'ic-{key}')
    link = st.selectbox('link', [None, 'https://ant.design/components/tag'], key=f'li-{key}')
    bordered = st.checkbox('bordered', True, key=f'bo-{key}')
    closable = st.checkbox('closable', True, key=f'cl-{key}')
    return update_kw(locals())


def main(kw):
    with st.expander('demo', True):
        sac.tag(**kw)
    show_code(f'''
    sac.tag({code_kw(kw)})
    ''', open=True)


def api():
    st.help(sac.tag)


TAG_DEMO = {
    'tag': {
        'params': params,
        'main': main,
        'api': api
    }
}
