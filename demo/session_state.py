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
    st.subheader('1.Get component value from session state')
    col = st.columns([1, 2])
    with col[0]:
        sac.buttons(['a', 'b', 'c'], key='sac.buttons')
        st.write(f"sac.buttons session value **{st.session_state['sac.buttons']}**")
    with col[1]:
        st.code('''
        import streamlit as st
        import streamlit_antd_components as sac

        sac.buttons(['a', 'b', 'c'], key='sac.buttons')
        st.write(f"sac.buttons session value **{st.session_state['sac.buttons']}**")
        ''')

    st.subheader('2.Interactive with native component')
    sac.divider('demo 1')
    col = st.columns([1, 2])
    with col[0]:
        sac.checkbox(['a', 'b', 'c'], label='set st.radio options', index=[0, 1], key='checkbox')
        st.radio('st.radio', st.session_state['checkbox'], horizontal=True)
    with col[1]:
        st.code('''
        import streamlit as st
        import streamlit_antd_components as sac
        
        sac.checkbox(['a', 'b', 'c'], label='set st.radio options', index=[0, 1], key='checkbox')
        st.radio('st.radio', st.session_state['checkbox'], horizontal=True)
        ''')
    sac.divider('demo 2')
    col = st.columns([1, 2])
    with col[0]:
        st.radio('set sac.checkbox index', [0, 1, 2, [1, 2]], key='radio', horizontal=True)
        sac.checkbox(['a', 'b', 'c'], label='sac.checkbox', index=st.session_state['radio'])
    with col[1]:
        st.code('''
        import streamlit as st
        import streamlit_antd_components as sac
        
        st.radio('set sac.checkbox index', [0, 1, 2, [1, 2]], key='radio', horizontal=True)
        sac.checkbox(['a', 'b', 'c'], label='sac.checkbox', index=st.session_state['radio'])
        ''')

    st.subheader('3.Change component value')
    col = st.columns([1, 2])
    with col[0]:
        menu_ph, btn_ph = st.empty(), st.empty()
        with btn_ph.container():
            c = st.columns(3)
            if c[0].button('set menu as menu1'):
                st.session_state['sac.menu'] = 'menu1'
            if c[1].button('set menu as menu2'):
                st.session_state['sac.menu'] = 'menu2'
            if c[2].button('set menu as menu3'):
                st.session_state['sac.menu'] = 'menu3'
        with menu_ph.container():
            sac.menu(['menu1', 'menu2', 'menu3'], key='sac.menu')
            st.write(f"sac.menu session value **{st.session_state['sac.menu']}**")
    with col[1]:
        st.code('''
        import streamlit as st
        import streamlit_antd_components as sac
        
        menu_ph, btn_ph = st.empty(), st.empty()
        with btn_ph.container():
            c = st.columns(3)
            if c[0].button('set menu as menu1'):
                st.session_state['sac.menu'] = 'menu1'
            if c[1].button('set menu as menu2'):
                st.session_state['sac.menu'] = 'menu2'
            if c[2].button('set menu as menu3'):
                st.session_state['sac.menu'] = 'menu3'
        with menu_ph.container():
            sac.menu(['menu1', 'menu2', 'menu3'], key='sac.menu')
            st.write(f"sac.menu session value **{st.session_state['sac.menu']}**")
        ''')
