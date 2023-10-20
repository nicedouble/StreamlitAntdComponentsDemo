#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/10/10 10:48
@Author   : ji hao ran
@File     : callback.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
import streamlit as st
import streamlit_antd_components as sac


def callback_usage():
    sac.alert('Attention', '''Use callback function in component by set component's `on_change`,`args`,`kwargs` parameters.
        and **`key` parameter must not be None** !''', icon=True)

    st.subheader('Counter')
    st.write('Store click times by callback.')

    if 'count' not in st.session_state:
        st.session_state['count'] = 0

    def counter():
        st.session_state['count'] += 1

    sac.segmented(['a', 'b', 'c'], key='segmented', on_change=counter)
    st.write(f"click times: {st.session_state['count']}")

    with st.expander('code', True):
        st.code('''
        import streamlit as st
        import streamlit_antd_components as sac
        
        if 'count' not in st.session_state:
            st.session_state['count'] = 0

        def counter():
            st.session_state['count'] += 1
        
        # key must not be None
        sac.segmented(['a', 'b', 'c'], key='segmented', on_change=counter)
        st.write(f"click times: {st.session_state['count']}")
        ''')
