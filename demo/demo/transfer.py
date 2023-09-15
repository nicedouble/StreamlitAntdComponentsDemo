#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/10 13:57
@Author   : ji hao ran
@File     : transfer.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params():
    label = st.selectbox('label', LABEL)
    index = st.selectbox('index', [[0, 1], None])
    titles = st.selectbox('titles', [None, ['source', 'target'], ['source'], ['', 'target']], 1)
    format_func = st.selectbox('format_func', FORMAT, 1)
    width = st.selectbox('width', [None, '100%', 200], 1)
    height = st.selectbox('height', [None, 400])
    c = st.columns(2)
    search = c[0].checkbox('search', True)
    pagination = c[1].checkbox('pagination', True)
    oneway = c[0].checkbox('oneway')
    reload = c[1].checkbox('reload', True)
    disabled = c[0].checkbox('disabled')
    return_index = c[1].checkbox('return_index')
    return update_kw(locals(), ['c'])


def main(kw):
    return_index = kw.get('return_index')
    with st.expander('demo', True):
        c = st.columns([1, 2, 1])
        with c[1]:
            t = sac.transfer(items=[f'item{i}' for i in range(30)], **kw)
            st.write(f'The transfer target item {"index" if return_index else "label"} : {t}')
    show_code(f'''
    sac.transfer(items=[f'item{{i}}' for i in range(30)], {code_kw(kw)})
    ''')


def api():
    st.help(sac.transfer)


TRANSFER_DEMO = {
    'transfer': {
        'params': params,
        'main': main,
        'api': api
    }
}
