#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/29 10:17
@Author   : ji hao ran
@File     : buttons.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params():
    c = st.columns(2)
    label = c[0].selectbox('label', LABEL)
    position = c[1].selectbox('position', ['top', 'right', 'bottom', 'left'], help='label position')
    index = c[0].selectbox('index', [0, 1, None])
    format_func = c[1].selectbox('format_func', FORMAT, 1)
    align = st.radio('align', ["start", "center", "end"], 1, horizontal=True)
    size = st.radio('size', ['small', 'middle', 'large'], 1, horizontal=True)
    direction = st.radio('direction', ["horizontal", "vertical"], horizontal=True)
    shape = st.radio('shape', ["default", "round", "circle"], horizontal=True)
    type = sac.segmented(label='type', items=['default', 'primary', 'dashed', 'text', 'link'], size='sm')
    compact = st.checkbox('compact')
    return_index = st.checkbox('return_index')
    return update_kw(locals(), ['c'])


def main(kw):
    return_index = kw.get('return_index')

    with st.expander('demo', True):
        btn = sac.buttons([
            sac.ButtonsItem(label='button'),
            sac.ButtonsItem(icon='apple'),
            sac.ButtonsItem(label='google', icon='google', color='#25C3B0'),
            sac.ButtonsItem(label='wechat', icon='wechat'),
            sac.ButtonsItem(label='disabled', disabled=True),
            sac.ButtonsItem(label='link', icon='share-fill', href='https://ant.design/components/button'),
        ], **kw)
        st.write(f'The selected button {"index" if return_index else "label"} is: {btn}')
    show_code(f'''
    sac.buttons([
        sac.ButtonsItem(label='button'),
        sac.ButtonsItem(icon='apple'),
        sac.ButtonsItem(label='google', icon='google', color='#25C3B0'),
        sac.ButtonsItem(label='wechat', icon='wechat'),
        sac.ButtonsItem(label='disabled', disabled=True),
        sac.ButtonsItem(label='link', icon='share-fill', href='https://ant.design/components/button'),
    ], {code_kw(kw, sac.buttons)})
    ''', True)


def api():
    st.help(sac.buttons)
    st.help(sac.ButtonsItem)


BUTTONS_DEMO = {
    'buttons': {
        'doc': 'A group of buttons component.',
        'params': params,
        'main': main,
        'api': api
    }
}
