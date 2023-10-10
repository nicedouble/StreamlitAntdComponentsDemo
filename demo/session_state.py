#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/10/10 11:42
@Author   : ji hao ran
@File     : session state.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
import streamlit_antd_components as sac


def session_usage():
    st.subheader('Get component value from session state')
    st.write('Set `key` parameter in component,and then you can get value from `st.session_state`.')
    sac.buttons(['a', 'b', 'c'], key='buttons')
    st.write(f"sac.buttons value in session_state is : {st.session_state['buttons']}")
    with st.expander('code'):
        st.code('''
        import streamlit as st
        import streamlit_antd_components as sac

        sac.buttons(['a', 'b', 'c'], key='buttons')
        st.write(f"sac.buttons value in session_state is : {st.session_state['buttons']}")
        ''')

    st.subheader('Interactive with other component')
    st.write('Change other component parameter by session state.')
    sac.checkbox(['a', 'b', 'c'], label='sac.checkbox', index=[0, 1], key='checkbox')
    st.radio('st.radio', st.session_state['checkbox'])
    with st.expander('demo'):
        st.code('''
        import streamlit as st
        import streamlit_antd_components as sac
        
        sac.checkbox(['a', 'b', 'c'], label='sac.checkbox', index=[0, 1], key='checkbox')
        st.radio('st.radio', st.session_state['checkbox'])
        ''')
