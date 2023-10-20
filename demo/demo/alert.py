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
            'Alert Message',
            'Alert Message <a href="https://ant.design/components/overview" target="_blank" class="badge badge-info">link</a>'
        ])
    description = st.selectbox('description', [None, 'description text ' * 10], 1)
    type = st.radio('type', ['info', 'success', 'warning', 'error'], horizontal=True)
    radius = st.radio('radius', ['xs', 'sm', 'md', 'lg', 'xl'], 2, horizontal=True)
    banner = st.selectbox('banner', [True, False, [True, False], [False, True]])
    icon = st.checkbox('icon', True)
    closable = st.checkbox('closable', True)
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
