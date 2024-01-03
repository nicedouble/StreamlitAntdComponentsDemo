#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/6/13 11:17
@Author   : ji hao ran
@File     : sascader.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    c = st.columns(2)
    label = show_label(c[0], key=key)
    description = show_description(c[1], key=key)
    index = show_index(c[0], [None, 0, [1, 3, 6, 7]], 1, key=key)
    format_func = show_format_func(c[1], key=key)
    placeholder = st.text_input('placeholder', 'Please choose')
    color = show_color(key=key)
    c = st.columns(2)
    multiple = show_checkbox('multiple', c[0], True, key=key)
    disabled = show_checkbox('disabled', c[1], key=key)
    search = c[0].checkbox('search', True)
    clear = c[1].checkbox('clear', True)
    strict = c[0].checkbox('strict')
    return_index = show_checkbox('return_index', c[1], key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    return_index = kw.get('return_index')
    with st.expander('demo', True):
        item = sac.cascader(items=[
            sac.CasItem('home', icon='house'),
            sac.CasItem('app', icon='app', children=[
                sac.CasItem('store', icon='bag-check'),
                sac.CasItem('brand', icon='award', children=[
                    sac.CasItem('github', icon='github'),
                    sac.CasItem('google', icon='google'),
                    sac.CasItem('apple', icon='apple', children=[
                        sac.CasItem('admin', icon='person-circle'),
                        sac.CasItem('guest', icon='person'),
                        sac.CasItem('twitter' * 5, icon='twitter'),
                    ]),
                ]),
            ]),
            sac.CasItem('disabled', icon='send', disabled=True),
            sac.CasItem('other1'),
            sac.CasItem('other2'),
        ], **kw)
        st.write(f'The selected cascader item {"index" if return_index else "label"} : {item}')
    show_code(f'''
    sac.cascader(items=[
        sac.CasItem('home', icon='house'),
        sac.CasItem('app', icon='app', children=[
            sac.CasItem('store', icon='bag-check'),
            sac.CasItem('brand', icon='award', children=[
                sac.CasItem('github', icon='github'),
                sac.CasItem('google', icon='google'),
                sac.CasItem('apple', icon='apple', children=[
                    sac.CasItem('admin', icon='person-circle'),
                    sac.CasItem('guest', icon='person'),
                    sac.CasItem('twitter' * 5, icon='twitter'),
                ]),
            ]),
        ]),
        sac.CasItem('disabled', icon='send', disabled=True),
        sac.CasItem('other1'),
        sac.CasItem('other2')
    ], {code_kw(kw, sac.cascader)})
    ''', True)


def api():
    st.help(sac.cascader)
    st.help(sac.CasItem)


CASCADER_DEMO = {
    'cascader': {
        'doc': 'Cascade selection box.',
        'params': params,
        'main': main,
        'api': api
    }
}
