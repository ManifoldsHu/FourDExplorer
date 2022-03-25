# -*- coding: utf-8 -*-

"""
*------------------------------ MainWindow.py --------------------------------*

4D-Explorer 程序主界面。

作者：          胡一鸣
创建时间：      2021年8月21日

The Main Window of the 4D-Explorer software.

author:             Hu Yiming
date:               Feb 24, 2022
*------------------------------ MainWindow.py --------------------------------*
"""

import sys
import os
from PySide6.QtWidgets import QMainWindow
from ui.uiMainWindow import Ui_MainWindow
from bin.Widgets.PageHome import PageHome




class MainWindow(QMainWindow):
    """
    4D-Explorer 主界面类。

    Ui 文件地址: ROOT_PATH/ui/uiMainWindow.ui

    This is the class to control the main window of 4D-Explorer.

    The path of Ui file: ROOT_PATH/ui/uiMainWindow.ui
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global qApp
        self._app = qApp

        self.setWindowTitle('4D-Explorer')

        self._page_home = PageHome(self)

        self._initFile()
        self._initTask()
        self._initCalibration()
        self._initImage()
        self._initViewers()
    
        

    def _initFile(self):
        self.ui.actionNew.triggered.connect(
            self.ui.tab_File.newFile
        )
        self.ui.actionOpen.triggered.connect(
            self.ui.tab_File.openFile
        )
        self.ui.actionClose.triggered.connect(
            self.ui.tab_File.closeFile
        )
        



    def _initTask(self):
        pass



    def _initCalibration(self):
        pass



    def _initImage(self):
        pass


    def _initViewers(self):
        """
        Initialize the viewers (tabWidgets)
        """
        self.ui.tabWidget_view.addTab(self._page_home, 'HOME')
        self.ui.tabWidget_view.setTabsClosable(True)
        self.ui.tabWidget_view.tabCloseRequested.connect(self._close_view_tab)

    def _close_view_tab(self, index):
        self.ui.tabWidget_view.removeTab(index)
        if self.ui.tabWidget_view.count() == 0:
            self.ui.tabWidget_view.addTab(self._page_home, 'HOME')












# class MainWindow(QMainWindow, QtStyleTools):
#     def __init__(self):
#         super().__init__()
#         self.ui = QUiLoader().load('uiMainWindow.ui', self)
#         self.apply_stylesheet(self.ui, theme = 'light_blue.xml')


# if __name__ == '__main__':
    
#     # dirname = os.path.dirname(PySide6.__file__)
#     # plugin_path = os.path.join(dirname, 'plugins', 'platforms')
#     # os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     # apply_stylesheet(app, theme='light_blue.xml')
#     # apply_stylesheet(app, theme='dark_blue.xml')
#     # apply_stylesheet(app, theme = 'dark_amber.xml')
#     sys.exit(app.exec())

