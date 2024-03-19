# -*- coding: utf-8 -*-

"""
*------------------------------ WidgetLog.py ---------------------------------*
将Logger的输出打印到这个文字浏览器里。

这个部件是放在主界面的。

作者：          胡一鸣
创建时间：      2022年3月24日

The module to print the logs.

This widget is used in the MainWindow.

author:         Hu Yiming
date:           Mar 24, 2022
*------------------------------ WidgetLog.py ---------------------------------*
"""

import os
from PySide6.QtWidgets import QWidget 
from PySide6.QtGui import QTextCursor
from bin.Log import LogUtil
from ui import uiWidgetLog

class WidgetLog(QWidget):
    """
    用于显示日志信息的部件，包含一个 QTextBrowser。

    Widget to show logs, which includes a QTextBrowser.
    """
    def __init__(self, parent: QWidget = None):
        """
        arguments:
            parent: (QWidget)
        """
        super().__init__(parent)
        self.ui = uiWidgetLog.Ui_Form()
        self.ui.setupUi(self)
        self._initLogger()

        self.ui.pushButton_open_log_directory.clicked.connect(
            self.openLogDir
        )
        self.ui.pushButton_open_log_directory.setVisible(False)
        self.ui.pushButton_clear_log.clicked.connect(self.clearLog)
    
    @property
    def log_util(self) -> LogUtil:
        global qApp
        return qApp.log_util

    def _initLogger(self):
        """
        Initialize the logger, set the stream.
        """
        # stream = self.log_util.widget_handler.stream
        stream = self.log_util.stream
        stream.print_signal.connect(self.printLog)

    def printLog(self, string: str):
        """
        This function make the textBrowser to print logs.

        arguments:
            string: str
        """
        cursor = self.ui.textBrowser_log.textCursor()
        self.ui.textBrowser_log.moveCursor(cursor.MoveOperation.End)
        cursor.insertText(string)
        self.ui.textBrowser_log.setTextCursor(cursor)
        self.ui.textBrowser_log.ensureCursorVisible()
    
    def openLogDir(self):
        """
        Open the logging directory.
        """
        path = self.log_util.log_dir_path
        os.startfile(path)
    
    def clearLog(self):
        """
        Clear the log textBrowser.
        """
        self.ui.textBrowser_log.clear()