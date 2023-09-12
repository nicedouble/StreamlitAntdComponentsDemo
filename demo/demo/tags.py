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
    format_func = st.selectbox('format_func', FORMAT, 1, key=f'ff-{key}')
    align = st.selectbox('align', ["start", "center", "end"], 1, key=f'al-{key}')
    direction = st.selectbox('direction', ["horizontal", "vertical"], key=f'dir-{key}')
    checkable = st.checkbox('checkable', help='tags checkable mode', key=f'che-{key}')
    return update_kw(locals())


def main(kw):
    st.subheader('demo1')
    t = sac.tags(items=['tag1', 'tag2', 'tag3'], **kw)
    st.write(f"The selected tags item label : {t}")

    show_code(f'''
    sac.tags(['tag1', 'tag2', 'tag3'],{code_kw(kw)})
    ''', open=True)

    st.subheader('demo2')
    t1 = sac.tags([
        sac.Tag(label='red', icon='house', color='red'),
        sac.Tag(label='blue', icon='gear', color='blue', bordered=False),
        sac.Tag(label='orange', icon='google', color='orange', closable=True),
        sac.Tag(label='link', icon='twitter', color='cyan', link='https://ant.design/components/tag'),
    ], **kw)
    st.write(f"The selected tags item label : {t1}")
    show_code(f'''
    sac.tags([
        sac.Tag(label='red', icon='house', color='red'),
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
