#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2024/1/10 14:42
@Author   : ji hao ran
@File     : icon.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""

from .utils import *


def icon():
    st.subheader('icon', anchor=False)
    st.info('''
    Currently, sac support [Boostrap icon](https://icons.getbootstrap.com/) and [Ant icon](https://ant.design/components/icon).  
    The default setting of the icon parameter is `string` to display Boostrap icons, 
    but it can also be set to class `AntIcon` and class `BsIcon` to display ant icons and more style settings.
    ''')

    tabs = sac.tabs([sac.TabsItem('Demo', icon='easel'), sac.TabsItem('Api', icon='cursor')], size='sm')
    if tabs == 'Demo':
        c = st.columns([2.2, 1])
        with c[1].expander('params', True):
            icon_ = sac.chip(['Bootstrap', 'Ant'], index=0, label='icon', size='sm')
            name = st.text_input(f'{icon_} icon name', 'house' if icon_ == 'Bootstrap' else 'HomeOutlined')
            size = show_radio('size', [None, 'xs', 'sm', 'md', 'lg', 'xl', 50], index=6, key='bs-icon')
            color = show_color(none_color='--text-color', key='bs-icon')
            kw = {k: v for k, v in dict(name=name, size=size, color=color).items() if v is not None}
        with c[0].expander('demo', True):
            show_space(2)
            sac.buttons([
                sac.ButtonsItem(icon=sac.BsIcon(**kw) if icon_ == 'Bootstrap' else sac.AntIcon(**kw)),
            ], align='center', variant='text', index=None)
            show_space(2)
        with c[0]:
            show_code(f'''
        sac.buttons([sac.ButtonsItem(icon=sac.{"Bs" if icon_ == 'Bootstrap' else 'Ant'}Icon({code_kw(kw, sac.BsIcon)}))], align='center', variant='text', index=None)
        ''', True)
    else:
        st.help(sac.BsIcon)
        st.help(sac.AntIcon)
