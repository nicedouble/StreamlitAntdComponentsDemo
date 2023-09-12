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


def params():
    c = st.columns(2)
    label = c[0].selectbox('label', LABEL, 1)
    value = st.checkbox('value', True)
    checked = st.selectbox('checked', [None, 'yes', BsIcon("sun")], 2)
    unchecked = st.selectbox('unchecked', [None, 'no', BsIcon("moon")], 2)
    align = st.selectbox('align', ["start", "center", "end"], 1)
    position = c[1].selectbox('position', ["top", "right", "bottom", "left"], help='label position')
    size = st.selectbox('size', ["default", "small", "large"])
    disabled = st.checkbox('disabled')
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
