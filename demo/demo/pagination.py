#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/8/9 15:22
@Author   : ji hao ran
@File     : pagination.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    total = st.number_input('total', 0, 200, 100, 50, key=f'to-{key}')
    index = st.selectbox('index', [1, 2], key=f'in-{key}')
    page_size = st.number_input('page_size', 5, 20, 10, 5, key=f'ps-{key}')
    align = st.selectbox('align', ["start", "center", "end"], 1, key=f'al-{key}')
    circle = st.checkbox('circle', key=f'ci-{key}')
    disabled = st.checkbox('disabled', key=f'dis-{key}')
    jump = st.checkbox('jump', True, key=f'ju-{key}')
    simple = st.checkbox('simple', key=f'si-{key}')
    show_total = st.checkbox('show_total', True, key=f'sh-{key}')
    return locals()


def main(kw):
    with st.expander('demo', True):
        r = sac.pagination(**kw)
        st.write(f'The selected pagination number is: {r}')
    show_code(f'''
    sac.pagination({code_kw(kw)})
    ''', True)


def api():
    st.help(sac.pagination)


PAGINATION_DEMO = {
    'pagination': {
        'params': params,
        'main': main,
        'api': api
    }
}
