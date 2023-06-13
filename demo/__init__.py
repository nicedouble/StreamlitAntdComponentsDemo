#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/5/29 10:17
@Author   : ji hao ran
@File     : __init__.py.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from .buttons import BUTTONS_DEMO
from .tabs import TABS_DEMO
from .menu import MENU_DEMO
from .tree import TREE_DEMO
from .switch import SWITCH_DEMO
from .divider import DIVIDER_DEMO
from .cascader import CASCADER_DEMO

DEMO = {**BUTTONS_DEMO, **TABS_DEMO, **MENU_DEMO, **TREE_DEMO, **CASCADER_DEMO, **SWITCH_DEMO, **DIVIDER_DEMO}
