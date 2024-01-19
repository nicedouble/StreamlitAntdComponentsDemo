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
    radius = show_radius(key=key)
    variant = show_variant(['light', 'filled', 'outline', 'transparent', 'quote', 'quote-light'], key=key)
    color = show_color(options=('info', 'success', 'warning', 'error', *MartineColor, '#4682b4'), key=key)
    banner = show_radio(
        label='banner',
        options=[True, False, [True, False], [False, True], "sac.Banner(direction='right',speed=150)"],
        key=f'{key}')
    icon = st.radio('icon', [True, False, 'house', "sac.BsIcon('house',size=50)"], horizontal=True, key=f'{key}-icon')
    closable = st.checkbox('closable', True, key=f'{key}-close')
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    if kw.get('banner') == "sac.Banner(direction='right',speed=150)":
        kw.update(banner=sac.Banner(direction='right', speed=150))
    if kw.get('icon') == "sac.BsIcon('house',size=50)":
        kw.update(icon=sac.BsIcon('house', size=50))

    with st.expander('demo', True):
        show_space()
        sac.alert(**kw)
        show_space()
    show_code(f'''
        sac.alert({code_kw(kw, sac.alert).replace('Banner', 'sac.Banner').replace('BsIcon', 'sac.BsIcon')})
        ''', open=True)


def api():
    st.help(sac.alert)
    st.help(sac.Banner)


ALERT_DEMO = {
    'alert': {
        'doc': 'Alert component for feedback.',
        'params': params,
        'main': main,
        'api': api
    }
}
