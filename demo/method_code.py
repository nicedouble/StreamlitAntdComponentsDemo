methods_code = dict(
    alert="""
sac.alert({params_str})
""",
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
    ], {params_str})
""",
    BsIcon="""
sac.buttons([sac.ButtonsItem(icon=sac.BsIcon({params_str}))], align='center', variant='text', index=None)
""",
    AntIcon="""
sac.buttons([sac.ButtonsItem(icon=sac.AntIcon({params_str}))], align='center', variant='text', index=None)
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
sac.divider({params_str})
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
    pagination="""
sac.pagination({params_str})
""",
    rate="""
sac.rate({params_str})
""",
    result="""
sac.result({params_str})
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
    ], {params_str}
)
""",
    switch="""
sac.switch({params_str})
""",
    #     tabs="""
    # sac.tabs([
    #     sac.TabsItem(label='apple', tag="10"),
    #     sac.TabsItem(icon='google'),
    #     sac.TabsItem(label='github', icon='github'),
    #     sac.TabsItem(label='disabled', disabled=True),
    # ], {params_str})
    # """,
    tabs="""
sac.tabs(
    ['apple', 'google','github','disabled'],
    {params_str})
""",
    tags="""
sac.tags([
    sac.Tag(label='tag'),
    sac.Tag(label='no border', bordered=False),
    sac.Tag(label='closable', closable=True),
    sac.Tag(label='link', icon='send', link='https://ant.design/components/tag'),
], {params_str})""",
    transfer="""
sac.transfer(items=[f'item{{i}}' for i in range(30)], {params_str})
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
], {params_str})
"""
)
