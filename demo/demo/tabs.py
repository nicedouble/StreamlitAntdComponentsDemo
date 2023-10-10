#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/29 11:04
@Author   : ji hao ran
@File     : tabs.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params():
    index = st.selectbox('index', [0, 1])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    height = st.selectbox('height(px)', [None, 150], help='available when position="right" or position="left"')
    align = st.radio('align', ["start", "center", "end"], 1, horizontal=True)
    position = st.radio('position', ["top", "right", "bottom", "left"], horizontal=True)
    shape = st.radio('shape', ['default', 'card'], horizontal=True)
    grow = st.checkbox('grow')
    return_index = st.checkbox('return_index')
    return update_kw(locals())


def main(kw):
    return_index = kw.get('return_index')

    with st.expander('demo', True):
        tab = sac.tabs([
            sac.TabsItem(label='apple'),
            sac.TabsItem(icon='google'),
            sac.TabsItem(label='github', icon='github'),
            sac.TabsItem(label='disabled', disabled=True),
        ], **kw)
        st.write(f'The selected tabs {"index" if return_index else "label"} is: {tab}')
    show_code(f'''
    sac.tabs([
        sac.TabsItem(label='apple'),
        sac.TabsItem(icon='google'),
        sac.TabsItem(label='github', icon='github'),
        sac.TabsItem(label='disabled', disabled=True),
    ], {code_kw(kw, sac.tabs)})
    ''', True)


def api():
    st.help(sac.tabs)
    st.help(sac.TabsItem)


TABS_DEMO = {
    'tabs': {
        'doc': 'A tabs component.',
        'params': params,
        'main': main,
        'api': api
    }
}
