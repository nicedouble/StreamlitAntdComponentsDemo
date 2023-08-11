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


def sidebar():
    index = st.selectbox('index', [0, 1])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    height = st.selectbox('height(px)', [None, 150])
    align = st.selectbox('align', ["start", "center", "end"])
    position = st.selectbox('position', ["top", "right", "bottom", "left"])
    shape = st.selectbox('shape', ['default', 'card'])
    grow = st.checkbox('grow')
    return_index = st.checkbox('return_index')
    return update_kw(locals())


def main(kw):
    return_index = kw.get('return_index')

    st.subheader('demo1')
    tab0 = sac.tabs(['tab1', 'tab2', 'tab3'], **kw)
    st.write(f'The selected tab {"index" if return_index else "label"} is: {tab0}')
    show_code(f'''
    sac.tabs(['tab1', 'tab2', 'tab3'], {code_kw(kw)})
    ''')

    st.subheader('demo2')
    tab1 = sac.tabs([
        sac.TabsItem(icon='table'),
        sac.TabsItem(icon='pie-chart-fill'),
        sac.TabsItem(icon='graph-up-arrow'),
        sac.TabsItem(icon='bar-chart'),
    ], **kw)
    st.write(f'The selected tab {"index" if return_index else "label"} is: {tab1}')
    show_code(f'''
    sac.tabs([
        sac.TabsItem(icon='table'),
        sac.TabsItem(icon='pie-chart-fill'),
        sac.TabsItem(icon='graph-up-arrow'),
        sac.TabsItem(icon='bar-chart'),
    ], {code_kw(kw)})
    ''')

    st.subheader('demo3')
    tab2 = sac.tabs([
        dict(label='apple', icon='apple'),
        dict(label='google', icon='google'),
        dict(label='github', icon='github'),
        dict(label='disabled', disabled=True),
    ], **kw)
    st.write(f'The selected tab {"index" if return_index else "label"} is: {tab2}')
    show_code(f'''
    sac.tabs([
        dict(label='apple', icon='apple'),
        dict(label='google', icon='google'),
        dict(label='github', icon='github'),
        dict(label='disabled', disabled=True),
    ], {code_kw(kw)})
    ''')


def api():
    st.help(sac.tabs)
    st.help(sac.TabsItem)


TABS_DEMO = {
    'tabs': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
