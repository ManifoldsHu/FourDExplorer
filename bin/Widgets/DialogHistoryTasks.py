# -*- coding: utf-8 -*-
"""
*------------------------- DialogHistoryTasks.py -----------------------------*
用于显示历史任务的对话框。

作者：          胡一鸣
创建时间：      2022年3月10日

The module to show the history tasks.

author:         Hu Yiming
date:           Mar 10, 2022
*------------------------- DialogHistoryTasks.py -----------------------------*
"""

from PySide6.QtWidgets import QDialog, QWidget, QMenu
from PySide6.QtCore import Qt, QPoint, QModelIndex

from bin.TaskManager import TaskManager, HistoryTaskModel, Task
from bin.Widgets.DialogTaskDetail import DialogTaskDetail
# from bin.Log import LogUtil
from ui import uiDialogHistoryTasks

class DialogHistoryTasks(QDialog):
    """
    显示历史任务的对话框。

    包含一个 QListView 显示历史任务的列表。

    Dialog to show history tasks.

    It includes a QListView to show the list of tasks.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogHistoryTasks.Ui_Dialog()
        self.ui.setupUi(self)

        global qApp
        self._task_manager = qApp.task_manager

        self.refresh()
        self.ui.pushButton_refresh.clicked.connect(self.refresh)
        self.ui.pushButton_clear_all.clicked.connect(self.clearAll)
        self.ui.pushButton_OK.clicked.connect(self.accept)
        self.ui.pushButton_OK.setVisible(False)

        self.ui.listView_history_task.setContextMenuPolicy(
            Qt.CustomContextMenu
        )
        self.ui.listView_history_task.customContextMenuRequested.connect(
            self.showContextMenu
        )
    
        self.setWindowTitle('History Tasks')

    @property
    def task_manager(self) -> TaskManager:
        return self._task_manager

    def refresh(self):
        """
        Refresh the history list view.
        """
        model = HistoryTaskModel(self.task_manager)
        self.ui.listView_history_task.setModel(model)

    def clearAll(self):
        """
        Clear all of the history tasks.
        """
        self.task_manager.clearHistory()
        
    def showContextMenu(self, pos: QPoint):
        """
        Show context menu of the list view.

        arguments:
            pos: (QPoint)
        """
        menu = QMenu(self)
        index = self.ui.listView_history_task.currentIndex()
        if not index.isValid():
            return False
        task = self.task_manager.task_queue.history_list[index.row()]
        action_detail = menu.addAction('Detail')
        action_detail.triggered.connect(
            lambda: self.openDetail(task)
        )
        menu.exec(self.mapToGlobal(pos))

    def openDetail(self, task: Task):
        """
        Show detail information of the task.
        """
        dialog = DialogTaskDetail(self)
        dialog.setCurrentTask(task)
        dialog.exec()