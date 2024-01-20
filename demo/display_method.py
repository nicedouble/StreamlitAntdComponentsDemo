import inspect
from typing import get_origin, Union, Literal

import streamlit as st
import streamlit_antd_components as sac

from demo.method_code import methods_code


def get_args_dict(func):
    sig = inspect.signature(func)
    return {param.name: param.annotation for param in sig.parameters.values()}


def display_method(method):
    if method not in methods_code.keys():
        raise ValueError(f'unsupported method {method}')

    st.subheader(method.title(), anchor=False)
    func = getattr(sac, method)
    args = get_args_dict(func)
    doc = func.__doc__
    doc_ = doc.split(':param')[0].strip()
    st.markdown(doc_)

    # component demo and api
    # tabs = sac.tabs([sac.TabsItem('Demo', icon='easel'), sac.TabsItem('Api', icon='cursor')], size='sm')
    # if tabs == 'Demo':
    c0, c1 = st.columns([2.2, 1])
    params = {}
    with c1.expander(f"{method} params", True):
        c1_ = st.columns(2)
        n = 0
        for name, annotation in args.items():
            # print(f"{name=}")
            if n > 1:
                n = 0
                c1_ = st.columns(2)
            if get_origin(annotation) is Union:
                annotation_args = annotation.__args__
                annotation_args_literal = [v for v in annotation_args if get_origin(v) is Literal]
                if len(annotation_args_literal) == 0:
                    annotation = annotation_args[0]
                else:
                    annotation = annotation_args_literal[0]

            if annotation is str:
                params[name] = c1_[n].text_input(name, name)
            elif annotation is bool:
                params[name] = c1_[n].checkbox(name, False)
            elif get_origin(annotation) is Literal:
                params[name] = c1_[n].selectbox(name, annotation.__args__)
            else:
                continue
            n += 1
    with c0:
        # tabs = sac.tabs([sac.TabsItem('Demo', icon='easel'), sac.TabsItem('Api', icon='cursor')], size='sm')
        tabs = 'Demo'
        if tabs == 'Demo':
            params_str = {f"{k}={v!r}" for k, v in params.items()}
            params_str = ", ".join(params_str)
            code = methods_code[method].format(params_str=params_str)
            # with st.tabs(['demo', 'api']):
            with st.expander('demo', True):
                out = eval(code)
                st.markdown(f"The selected button label is: {out}")

            with st.expander('code', True):
                code = f"import streamlit_antd_components as sac\n{code}"
                st.code(code, line_numbers=True)
        else:
            st.write('tbd')


method_code = dict(
    buttons="""
sac.buttons([
    sac.ButtonsItem(label='button'),
    sac.ButtonsItem(icon='apple'),
    sac.ButtonsItem(label='google', icon='google', color='#25C3B0'),
    sac.ButtonsItem(label='wechat', icon='wechat'),
    sac.ButtonsItem(label='disabled', disabled=True),
    sac.ButtonsItem(label='link', icon='share-fill', href='https://ant.design/components/button'),
], {params_str})
""",
    cascader="""
    sac.cascader(items=[
        sac.CasItem('home', icon='house'),
        sac.CasItem('app', icon='app', children=[
            sac.CasItem('store', icon='bag-check'),
            sac.CasItem('brand', icon='award', children=[
                sac.CasItem('github', icon='github'),
                sac.CasItem('google', icon='google'),
                sac.CasItem('apple', icon='apple', children=[
                    sac.CasItem('admin', icon='person-circle'),
                    sac.CasItem('guest', icon='person'),
                    sac.CasItem('twitter' * 5, icon='twitter'),
                ]),
            ]),
        ]),
        sac.CasItem('disabled', icon='send', disabled=True),
        sac.CasItem('other1'),
        sac.CasItem('other2')
    ], {params_str)
    """,
    checkbox="""
    sac.checkbox(
        items=[
            'item1',
            'item2',
            'item3',
            sac.CheckboxItem('item4', disabled=True)
        ],
        {params_str}
    )
    """,
    chip="""
sac.chip(
    items=[
        sac.ChipItem(label='apple'),
        sac.ChipItem(icon='google'),
        sac.ChipItem(label='github', icon='github'),
        sac.ChipItem(label='twitter', icon='twitter'),
        sac.ChipItem(label='disabled', disabled=True),
    ], {params_str}
)
""",
    divider="""
sac.divider({params_str(kw, sac.divider).replace('BsIcon', 'sac.BsIcon').replace(', color=None', '')})
""",
    menu="""
sac.menu([
    sac.MenuItem('home', icon='house-fill', tag=[sac.Tag('Tag1', color='green'), sac.Tag('Tag2', 'red')]),
    sac.MenuItem('products', icon='box-fill', children=[
        sac.MenuItem('apple', icon='apple'),
        sac.MenuItem('other', icon='git', description='other items', children=[
            sac.MenuItem('google', icon='google', description='item description'),
            sac.MenuItem('gitlab', icon='gitlab'),
            sac.MenuItem('wechat', icon='wechat'),
        ]),
    ]),
    sac.MenuItem('disabled', disabled=True),
    sac.MenuItem(type='divider'),
    sac.MenuItem('link', type='group', children=[
        sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
        sac.MenuItem('bootstrap-icon', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
    ]),
], {params_str})
""",
    icon="""
            sac.buttons([sac.ButtonsItem(icon=sac.{"Bs" if icon_ == 'Bootstrap' else 'Ant'}Icon({code_kw(kw, sac.BsIcon)}))], align='center', variant='text', index=None)
            """,
    pagination="""
 sac.pagination({params_str})
 """,
    rate="""
sac.rate({params_str(kw, sac.rate).replace('BsIcon', 'sac.BsIcon').replace('name=', '')})

""",
    result="""
    sac.result({params_str(kw, sac.result).replace('BsIcon', 'sac.BsIcon')})
    """,
    segmented="""
sac.segmented(
    items=[
        sac.SegmentedItem(label='apple'),
        sac.SegmentedItem(icon='google'),
        sac.SegmentedItem(label='github', icon='github'),
        sac.SegmentedItem(label='link', icon='share-fill', href='https://mantine.dev/core/segmented-control/'),
        sac.SegmentedItem(label='disabled', disabled=True),
    ], {params_str}
)
""",
    steps="""
sac.steps(
    items=[
        sac.StepsItem(title='step 1', subtitle='extra msg', description='description text'),
        sac.StepsItem(title='step 2'),
        sac.StepsItem(title='step 3'),
        sac.StepsItem(title='step 4', disabled=True),
    ], {params_str(kw, sac.steps)}
)
""",
    switch="""

sac.switch({params_str(kw, sac.switch).replace('BsIcon', 'sac.BsIcon').replace('name=', '')})

""",
    tabs="""
sac.tabs([
    sac.TabsItem(label='apple', tag="10"),
    sac.TabsItem(icon='google'),
    sac.TabsItem(label='github', icon='github'),
    sac.TabsItem(label='disabled', disabled=True),
], {params_str})
""",
    tags="""
sac.tags([
    sac.Tag(label='tag'),
    sac.Tag(label='no border', bordered=False),
    sac.Tag(label='closable', closable=True),
    sac.Tag(label='link', icon='send', link='https://ant.design/components/tag'),
], {params_str})""",
    transfer="""
sac.transfer(items=[f'item{{i}}' for i in range(30)], {params_str(kw, sac.transfer)})

""",
    tree="""
sac.tree(items=[
    sac.TreeItem('item1', tag=[sac.Tag('Tag', color='red'), sac.Tag('Tag2', color='cyan')]),
    sac.TreeItem('item2', icon='apple', description='item description', children=[
        sac.TreeItem('tooltip', icon='github', tooltip='item tooltip'),
        sac.TreeItem('item2-2', children=[
            sac.TreeItem('item2-2-1'),
            sac.TreeItem('item2-2-2'),
            sac.TreeItem('item2-2-3'),
        ]),
    ]),
    sac.TreeItem('disabled', disabled=True),
    sac.TreeItem('item3', children=[
        sac.TreeItem('item3-1'),
        sac.TreeItem('item3-2'),
    ]),
], {params_str})"""
)
