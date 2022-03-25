# -*- coding: utf-8 -*-

"""
*------------------------------- PageHome.py ---------------------------------*
主页。

作者:           胡一鸣
创建日期:       2022年3月25日

The home page.

author:         Hu Yiming
date:           Mar 25, 2022
*------------------------------- PageHome.py ---------------------------------*
"""

from PySide6.QtWidgets import QWidget
from ui import uiPageHome


class PageHome(QWidget):
    """
    主页。

    Ui 文件地址：ROOT_PATH/ui/uiPageHome.ui

    The home page.

    The path of the ui file: ROOT_PATH/ui.uiPageHome.ui
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageHome.Ui_Form()
        self.ui.setupUi(self)

    