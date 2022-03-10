# -*- coding: utf-8 -*-

"""
*-------------------------- WidgetSystemInfo.py ------------------------------*
对系统信息进行显示的模块。

这个 Widget 是用在主界面的，使用 QTimer 每隔一定时间刷新一次 CPU 占用、内存占用、磁
盘占用以及磁盘IO速度。

作者：          胡一鸣
创建时间：      2022年3月10日

The module to show system information

This widget is used in the main window. It use QTimer to refresh CPU, memory,
disk and IO rate information.

author:         Hu Yiming
date:           Mar 10, 2022
*-------------------------- WidgetSystemInfo.py ------------------------------*
"""

import os

from PySide6.QtWidgets import QWidget 

from ui import uiWidgetSystemInfo
from bin.HDFManager import HDFHandler

class WidgetSystemInfo(QWidget):
    """
    用于显示系统信息的模块。包含 3 个进度条以及一些标签。

    Widget to show system information (in Task tab). It includes 3 progress bars
    and some labels.
    """
    def __init__(self, parent: QWidget = None):
        """
        arguments:
            parent: (QWidget)
        """
        super().__init__(parent)
        self.ui = uiWidgetSystemInfo.Ui_Form()
        self.ui.setupUi(self)
        