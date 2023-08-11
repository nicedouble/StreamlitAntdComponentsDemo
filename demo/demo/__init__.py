#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/8/9 17:06
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
from .transfer import TRANSFER_DEMO
from .segmented import SEGMENTED_DEMO
from .alert import ALERT_DEMO
from .steps import STEPS_DEMO
from .checkbox import CHECKBOX_DEMO
from .rate import RATE_DEMO
from .result import RESULT_DEMO
from .tag import TAG_DEMO
from .tags import TAGS_DEMO
from .pagination import PAGINATION_DEMO

DEMO = {
    **BUTTONS_DEMO,
    **TABS_DEMO,
    **SEGMENTED_DEMO,
    **MENU_DEMO,
    **TREE_DEMO,
    **CASCADER_DEMO,
    **TRANSFER_DEMO,
    **SWITCH_DEMO,
    **DIVIDER_DEMO,
    **ALERT_DEMO,
    **STEPS_DEMO,
    **RATE_DEMO,
    **CHECKBOX_DEMO,
    **RESULT_DEMO,
    **TAG_DEMO,
    **TAGS_DEMO,
    **PAGINATION_DEMO
}