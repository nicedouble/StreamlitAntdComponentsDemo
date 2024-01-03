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
    c = st.columns(2)
    label = show_label(c[0], key=key)
    description = show_description(c[1], 'description', key=key)
    size = show_size(key=key)
    color = show_color(options=('info', 'success', 'warning', 'error', *MartineColor, '#4682b4'), key=key)
    radius = show_radius(key=key)
    variant = show_variant(['light', 'filled', 'outline', 'transparent'], key=key)
    banner = st.radio('banner', [True, False, [True, False], [False, True]], horizontal=True, key=f'{key}-banner')
    icon = st.radio('icon', [True, False, 'house'], horizontal=True, key=f'{key}-icon')
    closable = st.checkbox('closable', True, key=f'{key}-close')
    return update_kw(locals(), ['c', 'key'])


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
