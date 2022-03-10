# -*- coding: utf-8 -*-

"""
*----------------------------- ExampleTask.py --------------------------------*
提供了一些构造并发任务的例子。

这些并发任务是用于 bin.TaskManager 的，一般是一些耗时较长的任务。构造好后，即可使用
TaskManager.addTask() 方法将其加入等待队列，即可自动执行。

作者：          胡一鸣
创建时间：      2022年3月10日


Here provides some examples for assembling concurrent tasks.

These concurrent tasks are used in bin.TaskManager, which usually last for a 
relatively long time. After we assemble a task, we can call TaskManager.addTask
method to enqueue the task. Wait a moment, the task will execute automatically.

author:         Hu Yiming
date:           Mar 10, 2022



Coding Example:
(Suppose we have a widget and a button. Click the button to execute the task.)

from PySide6.QtWidgets import QWidget
from bin.TaskManager import TaskManager
from ui import uiFile   # use Qt-designer and PySide6-uic to produce uiFile.py
from example.ExampleTask import ExampleSleep

class MyWidget(QWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiFile.Ui_Dialog()
        self.ui.setupUi(self)

        global qApp     # get the singleton QApplication instance
        self._task_manager = qApp.task_manager
        self.ui.pushButton.clicked.connect(self.executeTask)
    
    @property
    def task_manager(self) -> TaskManager:
        return self._task_manager

    def executeTask(self):
        task = ExampleSleep()
        self.task_manager.addTask(task)
        

Then, suppose the this widget will show somewhere when 4D-Explorer runs. When
we click the button of this widget, in the Task tab of the main window, will 
show how the example task is running.
*----------------------------- ExampleTask.py --------------------------------*
"""

import time
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, QObject
from bin.TaskManager import Task 
    
class ExampleSleep(Task):
    """
    一个子例化 Task 的例子。
    
    里面包含两个子任务，每个会睡眠不等时间。它们会并发地运行，因此当最长的子
    任务运行完成后该任务就完成了。

    An example of Task.

    There are 2 subtasks. They will sleep arbitrary seconds. They will execute
    concurrently.
    """
    def __init__(self, parent = None):
        super().__init__(parent)
        self.name = 'Sleep'
        self.comment = 'I am sleeping'

        self.addSubtaskWithProgress(        # Add a subtask that lasts longest. 
            'sleep 10s',                      # The function should be custom-made 
            self.test_func_with_progress,   # to show the progress correctly.
            10
        )


        self.addSubtask('sleep 5s', time.sleep, 5)

        # Do some preparation work.
        self.setPrepare(
            QMessageBox.information, 
            None, 
            'prepare', 
            'Will sleep 10 seconds.', 
            QMessageBox.Ok,
        )

        # Do some following work. The result of the subtasks can be gotten from
        # subtask.future.result()
        self.setFollow(
            QMessageBox.information,
            None,
            'follow',
            'I wake up',
            QMessageBox.Ok
        )

    def test_func_with_progress(self, signal: Signal, nums: int):
        """
        Sleep nums seconds.

        The first argument of this function must be the progress signal.

        arguments:
            signal: (Signal) when calling addSubtaskWithProgress, this 
                arguments is transferred automatically.

            nums: (int)
        """
        for second in range(nums):
            time.sleep(1)
            signal.emit(int((second + 1) / nums * 100))


class ExampleSleepWithoutProgress(Task):
    """
    一个子例化 Task 的例子。
    
    里面所有 Subtask 都没有设置进度条。这个例子也说明了如何从子任务中取得返回值。

    An example of Task, but all of the subtasks do not have progress. This
    example also shows how to get return values from the subtask.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.name = 'Sleep, no progress'
        self.comment = 'I am sleeping, and do not know how long.'

        self.addSubtask('Sleep 10s', time.sleep, 10)
        self.calc_subtask = self.addSubtask(
            'Calculation', 
            self.calculation, 
            100
        )

        self.setPrepare(
            self.showPrepareMessage
        )

        self.setFollow(
            self.showFollowMessage
        )

    def calculation(self, num):
        result = 0
        for ii in range(num):
            result += ii
        # raise Exception('An exception Occured')
        return result

    def showFollowMessage(self):
        QMessageBox.information(
            None, 
            'follow', 
            'I calculated from 0 to 99: {0}'.format(
                self.calc_subtask.result
            ),
            QMessageBox.Ok,
        )
        # raise Exception('An exception occured')

    def showPrepareMessage(self):
        QMessageBox.information(
            None, 
            'prepare', 
            'Will sleep 10 seconds.', 
            QMessageBox.Ok,
        )
        # raise Exception('An exception occured')