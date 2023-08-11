#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/11 16:37
@Author   : ji hao ran
@File     : alert.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""

from ..utils import *


def sidebar():
    message = st.selectbox(
        label='message',
        options=[
            'alert message',
            '**markdown bold**',
            '**markdown bold** <span style="color:red">html tag</span>'
        ], index=1)
    description = st.selectbox('description', [None, 'alert description', '**markdown text**'])
    type = st.selectbox('type', ['info', 'success', 'warning', 'error'])
    height = st.selectbox('height', [None, 100])
    icon = st.checkbox('icon', True)
    closable = st.checkbox('closable', True)
    banner = st.checkbox('banner', True)
    return locals()


def main(kw):
    sac.alert(**kw)
    show_code(f'''
        sac.alert({code_kw(kw)})
        ''', open=True)


def api():
    st.help(sac.alert)


ALERT_DEMO = {
    'alert': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}
