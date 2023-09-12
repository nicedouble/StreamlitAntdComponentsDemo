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


def params(key):
    label = st.selectbox('label', LABEL, key=f'la-{key}')
    index = st.selectbox('index', [[0, 1], None], key=f'in-{key}')
    titles = st.selectbox('titles', [None, ['source', 'target'], ['source'], ['', 'target']], 1, key=f'ti-{key}')
    format_func = st.selectbox('format_func', FORMAT, 1, key=f'ff-{key}')
    width = st.selectbox('width', [None, '100%', 200], key=f'w-{key}')
    height = st.selectbox('height', [None, 400], key=f'h-{key}')
    c = st.columns(2)
    search = c[0].checkbox('search', True, key=f'se-{key}')
    pagination = c[1].checkbox('pagination', True, key=f'pa-{key}')
    oneway = c[0].checkbox('oneway', key=f'one-{key}')
    reload = c[1].checkbox('reload', True, key=f'reload-{key}')
    disabled = c[0].checkbox('disabled', key=f'dis-{key}')
    return_index = c[1].checkbox('return_index', key=f're-{key}')
    return update_kw(locals(), ['c'])


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
        'params': params,
        'main': main,
        'api': api
    }
}
