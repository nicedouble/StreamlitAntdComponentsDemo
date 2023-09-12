#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/6/13 10:43
@Author   : ji hao ran
@File     : switch.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *
from streamlit_antd_components.utils.data_class import BsIcon


def params(key):
    c = st.columns(2)
    label = c[0].selectbox('label', LABEL, 1, key=f'la-{key}')
    value = st.checkbox('value', True, key=f'va-{key}')
    checked = st.selectbox('checked', [None, 'yes', BsIcon("sun")], 2, key=f'ch-{key}')
    unchecked = st.selectbox('unchecked', [None, 'no', BsIcon("moon")], 2, key=f'un-{key}')
    align = st.selectbox('align', ["start", "center", "end"], 1, key=f'al-{key}')
    position = c[1].selectbox('position', ["top", "right", "bottom", "left"], help='label position', key=f'pos-{key}')
    size = st.selectbox('size', ["default", "small", "large"], key=f'si-{key}')
    disabled = st.checkbox('disabled', key=f'dis-{key}')
    return update_kw(locals(), ['c'])


def main(kw):
    with st.expander('demo', True):
        s = sac.switch(**kw)
        st.write(f'switch return value: {s}')
    show_code(f'''from streamlit_antd_components.utils.data_class import BsIcon

sac.switch({code_kw(kw)})
    ''', True)


def api():
    st.help(sac.switch)
    st.help(sac.BsIcon)


SWITCH_DEMO = {
    'switch': {
        'params': params,
        'main': main,
        'api': api
    }
}
