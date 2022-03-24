# -*- coding: utf-8 -*-

"""
*-------------------------- WidgetTaskManager.py -----------------------------*
用于显示并发任务管理器的模块。

这个 Widget 是用在主界面的，可以用来查看当前任务的名字、注释、运行进度。它也可以查看
任务队列以及历史任务，并取消等待队列中的任务。

作者：          胡一鸣
创建时间：      2022年3月10日


The module to show concurrent task manager.

This widget is used in the main window. It shows the name, comment and progress
of the current task. We can also view waiting queue and history tasks from this
widget, and cancel the tasks inside the waiting queue.

author:         Hu Yiming
date:           Mar 10, 2022
*-------------------------- WidgetTaskManager.py -----------------------------*
"""

from PySide6.QtWidgets import QWidget, QMenu
from PySide6.QtCore import Qt, QPoint, QModelIndex

from bin.TaskManager import TaskManager, Task
from example.ExampleTask import ExampleSleep, ExampleSleepWithoutProgress
# from bin.Log import LogUtil
from bin.Widgets.DialogTaskDetail import DialogTaskDetail
from bin.Widgets.DialogHistoryTasks import DialogHistoryTasks
from ui import uiWidgetTaskManager

class WidgetTaskManager(QWidget):
    """
    管理并发任务的组件。
    
    包含一个 QListView 用于显示任务队列，以及一些按钮、进度条用来显示当前任务。

    Widget to manage concurrent tasks.

    It includes a QListView to show the task queue, and some buttons and a 
    progress bar to show some information of the current task.
    """
    def __init__(self, parent: QWidget = None):
        """
        arguments:
            parent: (QWidget) the parent widget.
        """
        super().__init__(parent)
        self.ui = uiWidgetTaskManager.Ui_Form()
        self.ui.setupUi(self)

        global qApp
        self._task_manager = qApp.task_manager

        self._initCurrent()
        self._initTaskQueue()

        # self.ui.pushButton_history.clicked.connect(self.testFunc)   # 放个按钮作为测试任务
        self._test_count = 0
        self.ui.pushButton_detail.clicked.connect(self.showCurrentDetail)
        self.ui.pushButton_history.clicked.connect(self.showHistory)

    @property 
    def task_manager(self) -> TaskManager:
        return self._task_manager

    def _initCurrent(self):
        self.task_manager.task_info_refresh.connect(self.refreshCurrent)
        self.task_manager.progress_updated.connect(self.refreshProgress)
        self.refreshCurrent()

    def _initTaskQueue(self):
        self.ui.listView_waiting_queue.setModel(
            self.task_manager.model_waiting
        )
        self.ui.listView_waiting_queue.setContextMenuPolicy(
            Qt.CustomContextMenu
        )
        self.ui.listView_waiting_queue.customContextMenuRequested.connect(
            self.showTaskQueueContextMenu
        )

    def refreshCurrent(self):
        """
        refresh current task information according to the task manager.
        """
        if self.task_manager.current_task is None:
            self.ui.label_current_task_name.setText('None')
            self.ui.progressBar_task.setValue(0)
            self.ui.progressBar_task.setVisible(False)
            self.ui.pushButton_detail.setEnabled(False)
        else:
            self.ui.label_current_task_name.setText(
                self.task_manager.current_task.name 
            )
            self.ui.progressBar_task.setVisible(True)
            self.ui.pushButton_detail.setEnabled(True)
            self.ui.progressBar_task.setValue(
                self.task_manager.current_task.progress
            )

            if self.task_manager.current_task.hasProgress():
                self.ui.progressBar_task.setRange(0, 100) # Percentage of step
            else:
                self.ui.progressBar_task.setRange(0, 0) # Busy indicator

    def refreshProgress(self):
        """
        refresh the progress according to the progress of the task
        """
        self.ui.progressBar_task.setValue(
            self.task_manager.current_task.progress
        )


    def testFunc(self):
        """
        Test function in order to test whether the task manager works.
        """
        self._test_count += 1
        if self._test_count % 2 == 1:
            self.task_manager.addTask(ExampleSleep(parent = self))
        elif self._test_count % 2 == 0:
            self.task_manager.addTask(ExampleSleepWithoutProgress(parent = self))


    def showDetail(self, task):
        """
        Shows the dialog to view the detail information of the task.

        attributes:
            task: (Task)
        """
        dialog = DialogTaskDetail(self)
        dialog.setCurrentTask(task)
        dialog.exec()


    def showCurrentDetail(self):
        """
        Shows the dialog to view the detail information of the current task.
        """
        dialog = DialogTaskDetail(self)
        dialog.setCurrentTask(self.task_manager.current_task)
        dialog.exec()

    def showTaskQueueContextMenu(self, pos: QPoint):
        """
        Show context menu in the list view of waiting task queue.

        attributes:
            pos: (QPoint) the position where the mouse is clicked.
        """
        index = self.ui.listView_waiting_queue.currentIndex()
        if not index.isValid():
            return False
        task = self.task_manager.task_queue[index.row()]
        menu = QMenu(self)
        menu.action_cancel = menu.addAction('Cancel')
        menu.action_cancel.triggered.connect(
            lambda: self.cancelTask(index)
        )

        menu.action_detail = menu.addAction('Detail')
        menu.action_detail.triggered.connect(
            lambda: self.showDetail(task)
        )
        menu.exec(self.mapToGlobal(pos))

    def cancelTask(self, index: QModelIndex):
        """
        Try cancelling a task. Fail if the task has been submitted.

        attributes:
            index: (QModelIndex)
        """
        self.task_manager.cancelTask(index)

    def showHistory(self):
        """
        Show a dialog to view the history tasks.
        """
        dialog = DialogHistoryTasks(self)
        dialog.exec()