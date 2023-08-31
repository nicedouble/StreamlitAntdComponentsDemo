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


def sidebar():
    label = st.selectbox('label', LABEL)
    index = st.selectbox('index', [[0, 1], None])
    titles = st.selectbox('titles', [None, ['source', 'target'], ['source'], ['', 'target']], 1)
    format_func = st.selectbox('format_func', FORMAT, 1)
    width = st.selectbox('width', [None, '100%', 200])
    height = st.selectbox('height', [None, 400])
    col = st.columns(2)
    search = col[0].checkbox('search', True)
    pagination = col[1].checkbox('pagination', True)
    col1 = st.columns(2)
    oneway = col1[0].checkbox('oneway')
    reload = col1[1].checkbox('reload', True)
    col2 = st.columns(2)
    disabled = col2[0].checkbox('disabled')
    return_index = col2[1].checkbox('return_index')
    return update_kw(locals(), ['col', 'col1', 'col2'])


def main(kw):
    return_index = kw.get('return_index')
    t = sac.transfer(items=[f'item{i}' for i in range(30)], **kw)
    st.write(f'The transfer target item {"index" if return_index else "label"} : {t}')
    show_code(f'''
    sac.transfer(items=[f'item{{i}}' for i in range(30)], {code_kw(kw)})
    ''', True)


def api():
    st.help(sac.transfer)


TRANSFER_DEMO = {
    'transfer': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
