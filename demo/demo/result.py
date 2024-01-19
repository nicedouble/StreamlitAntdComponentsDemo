#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/27 14:56
@Author   : ji hao ran
@File     : result.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    c = st.columns(2)
    label = show_label(c[0], key=key)
    description = show_description(c[1], value='description', key=key)
    status = show_radio('status', ['info', 'success', 'warning', 'error', 'empty', 403, 404, 500], key=key)
    icon = show_radio('icon', [None, 'house', "sac.BsIcon('house',size=30)"], key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    if kw.get('icon') == "sac.BsIcon('house',size=30)":
        kw.update(icon=sac.BsIcon('house', size=30))
    with st.expander('demo', True):
        show_space()
        sac.result(**kw)
        show_space()
    show_code(f'''
        sac.result({code_kw(kw, sac.result).replace('BsIcon', 'sac.BsIcon')})
        ''', open=True)


def api():
    st.help(sac.result)


RESULT_DEMO = {
    'result': {
        'doc': 'Used to feed back the results of a series of operational tasks.',
        'params': params,
        'main': main,
        'api': api
    }
}
