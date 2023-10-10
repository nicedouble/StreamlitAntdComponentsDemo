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
    type = sac.segmented(label='type', items=['info', 'success', 'warning', 'error'], size='sm')
    height = st.selectbox('height', [None, 100])
    icon = st.checkbox('icon', True)
    closable = st.checkbox('closable', True)
    banner = st.checkbox('banner', True)
    return locals()


def main(kw):
    with st.expander('demo', True):
        sac.alert(**kw)
    show_code(f'''
        sac.alert({code_kw(kw, sac.alert)})
        ''', open=True)


def api():
    st.help(sac.alert)


ALERT_DEMO = {
    'alert': {
        'doc': 'Alert component for feedback.',
        'params': params,
        'main': main,
        'api': api
    }
}
