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
    index = st.selectbox('index', [0, 1, None])
    format_func = st.selectbox('format_func', FORMAT, 1)
    align = st.selectbox('align', ["start", "center", "end"], 1)
    position = c[1].selectbox('position', ['top', 'right', 'bottom', 'left'], help='label position')
    size = st.selectbox('size', ['small', 'default', 'large'], 1)
    direction = st.selectbox('direction', ["horizontal", "vertical"])
    c1 = st.columns(2)
    shape = c1[0].selectbox('shape', ["default", "round", "circle"], 1)
    type = c1[1].selectbox('type', ['primary', 'default', 'dashed', 'text', 'link'], 1)
    compact = c1[0].checkbox('compact')
    return_index = c1[1].checkbox('return_index')
    return update_kw(locals(), ['c', 'c1'])


def main(kw):
    return_index = kw.get('return_index')

    with st.expander('demo', True):
        btn = sac.buttons([
            sac.ButtonsItem(label='check'),
            sac.ButtonsItem(icon='facebook'),
            sac.ButtonsItem(label='github', icon='github', color='#25C3B0'),
            sac.ButtonsItem(label='twitter', icon='twitter', color='var(--primary)'),
            sac.ButtonsItem(label='disabled', disabled=True),
            sac.ButtonsItem(label='link', href='https://ant.design/components/button', icon='link'),
        ], **kw)
        st.write(f'The selected button {"index" if return_index else "label"} is: {btn}')
    show_code(f'''
    sac.buttons([
        sac.ButtonsItem(label='check'),
        sac.ButtonsItem(icon='facebook'),
        sac.ButtonsItem(label='github', icon='github', color='#25C3B0'),
        sac.ButtonsItem(label='twitter', icon='twitter', color='var(--primary)'),
        sac.ButtonsItem(label='disabled', disabled=True),
        sac.ButtonsItem(label='link', href='https://ant.design/components/button', icon='link'),
    ], {code_kw(kw)})
    ''', True)


def api():
    st.help(sac.buttons)
    st.help(sac.ButtonsItem)


BUTTONS_DEMO = {
    'buttons': {
        'params': params,
        'main': main,
        'api': api
    }
}
