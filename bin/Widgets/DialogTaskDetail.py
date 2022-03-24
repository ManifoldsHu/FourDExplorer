# -*- coding: utf-8 -*-

"""
*-------------------------- DialogTaskDetail.py ------------------------------*
用于显示当前任务的详细信息的对话框。

作者：          胡一鸣
创建时间：      2022年3月10日


The module to show the detail information of a task.

author:         Hu Yiming
date:           Mar 10, 2022
*-------------------------- DialogTaskDetail.py ------------------------------*
"""

from PySide6.QtWidgets import QDialog, QWidget
from bin.TaskManager import TaskManager, Task, Subtask, SubtaskListModel
# from bin.Log import LogUtil 
from ui import uiDialogTaskDetail

class DialogTaskDetail(QDialog):
    """
    显示当前任务详细信息的对话框。

    包含一个 QListView 显示子任务，一个 QPlainTextEdit 用来显示注释。

    Dialog to show the detail information of current task.

    It includes a QListView to show subtasks, and a QPlainTextEdit to show the
    comments of the task.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogTaskDetail.Ui_Dialog()
        self.ui.setupUi(self)

        global qApp
        self._task_manager = qApp.task_manager
        self._task = None
        
        self.ui.pushButton_refresh.clicked.connect(self.refresh)
        self.ui.pushButton_OK.clicked.connect(self.accept)

        self.ui.plainTextEdit_comment.setReadOnly(True)

        self.setWindowTitle('Task Details')
        
        

    @property
    def task_manager(self) -> TaskManager:
        return self._task_manager

    @property
    def task(self) -> Task:
        return self._task

    def setCurrentTask(self, task: Task):
        self._task = task
        self.refresh()
        
    def refresh(self):
        """
        Update the information of the current task.
        """
        self.ui.label_task_name.setText(self.task.name)
        state_string = str(self.task.state).split('.')[1]
        self.ui.label_task_state.setText(state_string)
        self.ui.plainTextEdit_comment.setPlainText(self.task.comment)
        model = SubtaskListModel(self.task)
        self.ui.listView_subtask.setModel(model)
        
        

