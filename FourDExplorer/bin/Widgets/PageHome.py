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
from bin.TaskManager import TaskManager
# from bin.ItemActions import ActionImportFourDSTEM

from bin.Actions.EditActions import ActionImportFourDSTEM 
from bin.Actions.EditActions import ActionImportImage
from bin.Actions.FileActions import ActionNewFile 
from bin.Actions.FileActions import ActionOpenFile 

from ui import uiPageHome
from example.ExampleTask import ExampleSleepWithoutProgress, ExampleSleep


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

        self.setWindowTitle('Home')

        self.ui.commandLinkButton_tutorials.clicked.connect(self._testTask)
        self.ui.commandLinkButton_work.clicked.connect(self._testTask2)

        self.ui.pushButton_import_fourDSTEM.clicked.connect(
            self._importFourDSTEM
        )
        self.ui.pushButton_new_file.clicked.connect(
            self._newFile
        )
        self.ui.pushButton_calibration.setVisible(False)        # TODO
        self.ui.pushButton_import_fourDSTEM.setVisible(False)   # TODO 
        self.ui.pushButton_import_image.setVisible(False)       # TODO 
        self.ui.pushButton_new_file.setVisible(False)           # TODO
        self.ui.pushButton_open_file.setVisible(False)          # TODO
        self.ui.commandLinkButton_tutorials.setVisible(False)   # TODO
        self.ui.commandLinkButton_work.setVisible(False)        # TODO

    @property
    def task_manager(self) -> TaskManager:
        global qApp
        return qApp.task_manager

    def _testTask(self):
        task = ExampleSleepWithoutProgress(self)
        self.task_manager.addTask(task)

    def _testTask2(self):
        task = ExampleSleep(self)
        self.task_manager.addTask(task)

    def _importFourDSTEM(self):
        self.import_action = ActionImportFourDSTEM(self)
        self.import_action.trigger()

    def _newFile(self):
        self.new_file_action = ActionNewFile(self)
        self.new_file_action.trigger()

    def _openFile(self):
        self.open_file_action = ActionOpenFile(self)
        self.open_file_action.trigger()

    def _importImage(self):
        self.import_image_action = ActionImportImage(self)
        self.import_image_action.trigger()

