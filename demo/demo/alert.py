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


def params():
    message = st.selectbox(
        label='message',
        options=[
            'alert message',
            '**alert message**',
            '**alert message** <a href="https://ant.design/components/overview" target="_blank" class="badge badge-info">link</a>'
        ], index=1)
    description = st.selectbox('description', [None, 'alert description', '**alert description**'])
    type = st.radio('type', ['info', 'success', 'warning', 'error'], horizontal=True)
    height = st.selectbox('height', [None, 100])
    icon = st.checkbox('icon', True)
    closable = st.checkbox('closable', True)
    banner = st.checkbox('banner', True)
    return locals()


def main(kw):
    with st.expander('demo', True):
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
