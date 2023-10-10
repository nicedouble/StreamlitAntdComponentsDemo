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


def params():
    index = st.selectbox('index', [0, 1])
    format_func = st.selectbox('format_func', [None, 'title', 'upper', "lambda x: f'A_{x}'"], 1)
    placement = st.radio('placement', ["horizontal", "vertical"], help='title placement', horizontal=True)
    size = st.radio('size', ["default", "small"], horizontal=True)
    direction = st.radio('direction', ["horizontal", "vertical"], horizontal=True)
    type = st.radio('type', ['default', 'navigation', 'inline'], horizontal=True)
    dot = st.checkbox('dot')
    return_index = st.checkbox('return_index')
    return update_kw(locals())


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
