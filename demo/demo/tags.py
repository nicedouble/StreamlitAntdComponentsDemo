#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/8/2 16:55
@Author   : ji hao ran
@File     : tag.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""

from ..utils import *


def params(key):
    format_func = show_format_func(key=key)
    align = show_align(key=key)
    direction = show_direction(key=key)
    size = show_size(key=key, index=1)
    radius = show_radius(key=key)
    color = show_color(options=(None, *AntColor.keys(), '#4682b4'), none_color='--text-color', martine=False, key=key)
    return update_kw(locals(), ['key'])


def main(kw):
    with st.expander('demo', True):
        show_space()
        sac.tags([
            sac.Tag(label='tag'),
            sac.Tag(label='no border', bordered=False),
            sac.Tag(label='closable', closable=True),
            sac.Tag(label='link', icon='send', link='https://ant.design/components/tag'),
        ], **kw)
        show_space()
    show_code(f'''
    sac.tags([
        sac.Tag(label='tag'),
        sac.Tag(label='no border', bordered=False),
        sac.Tag(label='closable', closable=True),
        sac.Tag(label='link', icon='send', link='https://ant.design/components/tag'),
    ], {code_kw(kw, sac.tags)})''', open=True)


def api():
    st.help(sac.tags)
    st.help(sac.Tag)


TAGS_DEMO = {
    'tags': {
        'doc': 'Tag for categorizing or markup.',
        'params': params,
        'main': main,
        'api': api
    }
}
