#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/7/26 14:36
@Author   : ji hao ran
@File     : steps.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def params(key):
    index = st.selectbox('index', [0, 1], key=f'in-{key}')
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1, key=f'ff-{key}')
    placement = st.selectbox('placement', ["horizontal", "vertical"], help='title placement', key=f'pl-{key}')
    size = st.selectbox('size', ["default", "small"], key=f'si-{key}')
    direction = st.selectbox('direction', ["horizontal", "vertical"], key=f'dir-{key}')
    type = st.selectbox('type', ['default', 'navigation', 'inline'], key=f'ty-{key}')
    dot = st.checkbox('dot', key=f'dot-{key}')
    return_index = st.checkbox('return_index', key=f're-{key}')
    return update_kw(locals())


def main(kw):
    return_index = kw.get('return_index')

    st.subheader('demo1', False)
    s0 = sac.steps(['item1', 'item2', 'item3'], **kw)
    st.write(f'The selected steps {"index" if return_index else "label"} is: {s0}')
    show_code(f'''
    sac.steps(['item1', 'item2', 'item3'], {code_kw(kw)})
    ''', True)

    st.subheader('demo2', False)
    s2 = sac.steps(
        items=[
            sac.StepsItem(title='step 1', subtitle='extra msg', description='description text'),
            dict(title='step 2'),
            dict(title='step 3'),
            dict(title='step 4', disabled=True),
        ], **kw
    )
    st.write(f'The selected steps {"index" if return_index else "label"} is: {s2}')
    show_code(f'''
    sac.steps(
        items=[
            sac.StepsItem(title='step 1', subtitle='extra msg', description='description text'),
            dict(title='step 2'),
            dict(title='step 3'),
            dict(title='step 4', disabled=True),
        ], {code_kw(kw)}
    )
    ''', True)


def api():
    st.help(sac.steps)
    st.help(sac.StepsItem)


STEPS_DEMO = {
    'steps': {
        'params': params,
        'main': main,
        'api': api
    }
}
