# -*- coding: utf-8 -*-

"""
*------------------------------ WidgetTask.py --------------------------------*
管理任务及系统状态的部件类。

部件内容：
    - WidgetTaskManager 用于显示线程池执行的任务
    - WidgetSystemInfo 用于显示系统信息，如CPU、内存、磁盘占用

提升部件：
    - 提升类名 WidgetTask
    - 头文件 bin.Widgets.WidgetTask

作者:           胡一鸣
创建日期:       2022年3月10日


The GUI widget to manage concurrent tasks and view system states.

Contents:
    - WidgetTaskManager, to view the task of the threading pool
    - WidgetSystemInfo, to view information of system, like CPU, memories

Promoted Widget:
    - name of widget class: WidgetTask
    - header file: bin.Widgets.WidgetTask

author:         Hu Yiming
date:           Mar 10, 2022
*------------------------------ WidgetTask.py --------------------------------*
"""

import os

from PySide6.QtWidgets import QWidget
from ui import uiWidgetTask
# from bin.Log import LogUtil

class WidgetTask(QWidget):
    """
    管理并发任务以及系统信息的部件。

    Ui 文件地址：ROOT_PATH/ui/uiWidgetTask.ui

    Widget to manage concurrent tasks and system information.

    The path of the ui file: ROOT_PATH/ui/uiWidgetTask.ui
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetTask.Ui_Form()
        self.ui.setupUi(self)

        # self._log_util = LogUtil(__name__)
        # self.logger = self._log_util.logger

        global qApp
        self._task_manager = qApp.task_manager

