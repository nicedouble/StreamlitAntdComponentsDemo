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


def params():
    format_func = st.selectbox('format_func', FORMAT, 1)
    align = st.selectbox('align', ["start", "center", "end"], 1)
    direction = st.selectbox('direction', ["horizontal", "vertical"])
    checkable = st.checkbox('checkable', help='tags checkable mode')
    return update_kw(locals())


def main(kw):
    with st.expander('demo', True):
        t1 = sac.tags([
            sac.Tag(label='tag'),
            sac.Tag(label='blue', icon='gear', color='blue', bordered=False),
            sac.Tag(label='orange', icon='google', color='orange', closable=True),
            sac.Tag(label='link', icon='twitter', color='cyan', link='https://ant.design/components/tag'),
        ], **kw)
        st.write(f"The selected tags item label : {t1}")
    show_code(f'''
    sac.tags([
        sac.Tag(label='tag'),
        sac.Tag(label='blue', icon='gear', color='blue', bordered=False),
        sac.Tag(label='orange', icon='google', color='orange', closable=True),
        sac.Tag(label='link', icon='twitter', color='cyan', link='https://ant.design/components/tag'),
    ], {code_kw(kw)})''', open=True)


def api():
    st.help(sac.tags)
    st.help(sac.Tag)


TAGS_DEMO = {
    'tags': {
        'params': params,
        'main': main,
        'api': api
    }
}
