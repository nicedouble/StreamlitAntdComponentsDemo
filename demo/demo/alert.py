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


def params(key):
    message = st.selectbox(
        label='message',
        options=[
            'alert message',
            '**alert message**',
            '**alert message** <a href="https://ant.design/components/overview" target="_blank" class="badge badge-info">link</a>'
        ], index=1, key=f'me-{key}')
    description = st.selectbox('description', [None, 'alert description', '**alert description**'], key=f'de-{key}')
    type = st.selectbox('type', ['info', 'success', 'warning', 'error'], key=f'ty-{key}')
    height = st.selectbox('height', [None, 100], key=f'h-{key}')
    icon = st.checkbox('icon', True, key=f'i-{key}')
    closable = st.checkbox('closable', True, key=f'c-{key}')
    banner = st.checkbox('banner', True, key=f'b-{key}')
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
        'params': params,
        'main': main,
        'api': api
    }
}
