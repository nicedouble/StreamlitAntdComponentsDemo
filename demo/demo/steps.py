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
    c = st.columns(2)
    index = show_index(c[0], [0, 1], key=key)
    format_func = show_format_func(c[1], key=key)
    size = show_size(key=key)
    color = show_color(key=key)
    variant = show_variant(['default', 'navigation'], key=key)
    placement = st.radio('placement', ["horizontal", "vertical"], help='title placement', horizontal=True)
    direction = show_direction(key=key)
    c = st.columns(2)
    dot = c[0].checkbox('dot')
    return_index = show_checkbox('return_index', c[1], key=key)
    return update_kw(locals(), ['c', 'key'])


def main(kw):
    return_index = kw.get('return_index')

    with st.expander('demo', True):
        step = sac.steps(
            items=[
                sac.StepsItem(title='step 1', subtitle='extra msg', description='description text'),
                sac.StepsItem(title='step 2'),
                sac.StepsItem(title='step 3'),
                sac.StepsItem(title='step 4', disabled=True),
            ], **kw
        )
        st.write(f'The selected steps {"index" if return_index else "label"} is: {step}')
    show_code(f'''
    sac.steps(
        items=[
            sac.StepsItem(title='step 1', subtitle='extra msg', description='description text'),
            sac.StepsItem(title='step 2'),
            sac.StepsItem(title='step 3'),
            sac.StepsItem(title='step 4', disabled=True),
        ], {code_kw(kw, sac.steps)}
    )
    ''', True)


def api():
    st.help(sac.steps)
    st.help(sac.StepsItem)


STEPS_DEMO = {
    'steps': {
        'doc': 'A navigation bar that guides users through the steps of a task.',
        'params': params,
        'main': main,
        'api': api
    }
}
