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


def sidebar():
    label = st.selectbox('label', LABEL)
    index = st.selectbox('index', [0, 1, None], 1)
    format_func = st.selectbox('format_func', FORMAT, 1)
    align = st.selectbox('align', ["start", "center", "end"], 1)
    position = st.selectbox('position', ['top', 'right', 'bottom', 'left'], help='label position')
    size = st.selectbox('size', ['default', 'small', 'large'])
    direction = st.selectbox('direction', ["horizontal", "vertical"])
    shape = st.selectbox('shape', ["default", "round", "circle"], 1)
    compact = st.checkbox('compact')
    return_index = st.checkbox('return_index')
    return update_kw(locals())


def main(kw):
    return_index = kw.get('return_index')

    st.subheader('demo1')
    btn0 = sac.buttons(['button1', 'button2', 'button3'], **kw)
    st.write(f'The selected button {"index" if return_index else "label"} is: {btn0}')
    show_code(f'''
    sac.buttons(['button1', 'button2', 'button3'], {code_kw(kw)})
    ''')

    st.subheader('demo2')
    btn1 = sac.buttons([
        sac.ButtonsItem(icon='chevron-bar-left'),
        sac.ButtonsItem(icon='chevron-left'),
        sac.ButtonsItem(icon='chevron-right'),
        sac.ButtonsItem(icon='chevron-bar-right'),
    ], **kw)
    st.write(f'The selected button {"index" if return_index else "label"} is: {btn1}')
    show_code(f'''
    sac.buttons([
        sac.ButtonsItem(icon='chevron-bar-left'),
        sac.ButtonsItem(icon='chevron-left'),
        sac.ButtonsItem(icon='chevron-right'),
        sac.ButtonsItem(icon='chevron-bar-right'),
    ], {code_kw(kw)})
    ''')

    st.subheader('demo3')
    btn2 = sac.buttons([
        dict(label='apple', icon='apple'),
        dict(label='google', icon='google', color='orange'),
        dict(label='github', icon='github', color='#25C3B0'),
        dict(label='twitter', icon='twitter', color='var(--primary)'),
        dict(label='disabled', disabled=True),
        dict(label='link', href='https://ant.design/components/button', icon='link'),
    ], **kw)
    st.write(f'The selected button {"index" if return_index else "label"} is: {btn2}')
    show_code(f'''
    sac.buttons([
        dict(label='apple', icon='apple'),
        dict(label='google', icon='google', color='orange'),
        dict(label='github', icon='github', color='#25C3B0'),
        dict(label='twitter', icon='twitter', color='var(--primary)'),
        dict(label='disabled', disabled=True),
        dict(label='link', href='https://ant.design/components/button', icon='link'),
    ], {code_kw(kw)})
    ''')


def api():
    st.help(sac.buttons)
    st.help(sac.ButtonsItem)


BUTTONS_DEMO = {
    'buttons': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
