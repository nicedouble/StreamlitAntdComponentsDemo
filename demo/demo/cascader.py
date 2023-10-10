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


def params():
    label = st.selectbox('label', LABEL, 1)
    index = st.selectbox('index', [None, 0, [1, 3, 6, 7]], 1)
    format_func = st.selectbox('format_func', FORMAT, 1)
    placeholder = st.text_input('placeholder', 'Please choose')
    multiple = st.checkbox('multiple', True)
    disabled = st.checkbox('disabled')
    search = st.checkbox('search', True)
    clear = st.checkbox('clear', True)
    strict = st.checkbox('strict')
    return_index = st.checkbox('return_index')
    return update_kw(locals())


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
