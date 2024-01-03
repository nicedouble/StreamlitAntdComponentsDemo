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
    c = st.columns(2)
    label = show_label(c[0], key=key)
    description = show_description(c[1], key=key)
    index = show_index(c[0], [[0, 1], None], key=key)
    format_func = show_format_func(c[1], key=key)
    titles = c[0].selectbox('titles', [None, ['source', 'target'], ['source'], ['', 'target']], 1)
    reload = c[1].selectbox('reload', [True, False, 'reload data'])
    align = show_align(key=key)
    color = show_color(key=key)
    c = st.columns(2)
    width = show_radio('width', [None, 200], c[0], key=key)
    height = show_radio('height', [None, 400], c[1], key=key)
    search = c[0].checkbox('search', True)
    pagination = c[1].checkbox('pagination', True)
    oneway = c[0].checkbox('oneway')
    disabled = show_checkbox('disabled', c[1], key=key)
    use_container_width = show_checkbox('use_container_width', c[0], key=key)
    return_index = show_checkbox('return_index', c[1], key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    return_index = kw.get('return_index')
    with st.expander('demo', True):
        t = sac.transfer(items=[f'item{i}' for i in range(30)], **kw)
        st.write(f'The transfer target item {"index" if return_index else "label"} : {t}')
    show_code(f'''
    sac.transfer(items=[f'item{{i}}' for i in range(30)], {code_kw(kw, sac.transfer)})
    ''')


def api():
    st.help(sac.transfer)


TRANSFER_DEMO = {
    'transfer': {
        'doc': 'Double column transfer choice box.',
        'params': params,
        'main': main,
        'api': api
    }
}
