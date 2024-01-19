#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/26 22:14
@Author   : ji hao ran
@File     : app.py
@Project  : StreamlitAntdComponents
@Software : PyCharm
"""

from demo.demo import DEMO
from demo.overview import overview
from demo.callback import callback_usage
from demo.session_state import session_usage
from demo.icon import icon
from demo.utils import *

st.set_page_config(layout='wide', page_title='streamlit-antd-components')

st.markdown(f'''
    <style>
    .stApp .main .block-container{{
        padding:30px 50px
    }}
    .stApp [data-testid='stSidebar']>div:nth-child(1)>div:nth-child(2){{
        padding-top:50px
    }}
    iframe{{
        display:block;
    }}
    .stRadio div[role='radiogroup']>label{{
        margin-right:5px
    }}
    </style>
    ''', unsafe_allow_html=True)

with st.sidebar.container():
    # tag
    modified = sac.Tag('Modified', color='blue', bordered=False)
    new = sac.Tag('New', color='green', bordered=False)
    deprecated = sac.Tag('Deprecated', color='orange', bordered=False)
    redesign = sac.Tag('Redesign', color='purple', bordered=False)
    # title
    st.subheader(f'Streamlit-antd-components')
    # menu
    menu = sac.menu(
        items=[
            sac.MenuItem('overview'),
            sac.MenuItem('icon', tag=new),
            sac.MenuItem('general', type='group', children=[
                sac.MenuItem('buttons')
            ]),
            sac.MenuItem('layout', type='group', children=[sac.MenuItem('divider')]),
            sac.MenuItem(
                label='navigation', type='group', children=[
                    sac.MenuItem('menu', tag=modified),
                    sac.MenuItem('pagination'),
                    'steps'
                ]
            ),
            sac.MenuItem(
                label='data entry', type='group',
                children=[
                    sac.MenuItem('cascader'),
                    sac.MenuItem('checkbox'),
                    sac.MenuItem('chip'),
                    'rate',
                    sac.MenuItem('switch'),
                    sac.MenuItem('transfer')
                ]
            ),
            sac.MenuItem(
                label='data display', type='group',
                children=[
                    sac.MenuItem('segmented'),
                    sac.MenuItem('tabs', tag=modified),
                    sac.MenuItem('tree'),
                    sac.MenuItem('tags'),
                ],
            ),
            sac.MenuItem(
                label='feedback', type='group', children=[
                    sac.MenuItem('alert', tag=modified),
                    sac.MenuItem('result')
                ]
            ),
            sac.MenuItem(label='Advanced Usage', type='group', children=[
                sac.MenuItem('session state'),
                sac.MenuItem('callback'),
            ]),
        ],
        key='menu',
        open_all=True, indent=20,
        format_func='title',
    )
    sac.divider('Environment', color='gray')
    sac.tags(
        [sac.Tag(f'streamlit=={st.__version__}', size='xs', color='cyan'),
         sac.Tag(f'streamlit-antd-components=={sac.__VERSION__}', size='xs', color='blue')])

with st.container():
    if menu == 'overview':
        overview()
    elif menu == 'callback':
        callback_usage()
    elif menu == 'session state':
        session_usage()
    elif menu == 'icon':
        icon()
    else:
        com_ = DEMO.get(menu)
        # component introduce
        st.subheader(menu.title(), anchor=False)
        st.write(com_.get('doc'))
        # component demo and api
        tabs = sac.tabs([sac.TabsItem('Demo', icon='easel'), sac.TabsItem('Api', icon='cursor')], size='sm')
        if tabs == 'Demo':
            col = st.columns([2.2, 1])
            with col[-1].expander(f"{menu} params", True):
                kw = com_.get('params')(key=menu)
            with col[0]:
                com_.get('main')(kw)
        else:
            com_.get('api')()
