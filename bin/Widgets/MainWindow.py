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

from PySide6.QtWidgets import (
    QMainWindow, 
    QToolBar, 
    QWidget, 
    QToolButton, 
    QSizePolicy,
)
from PySide6.QtCore import Qt, QSize
from bin.Actions.FileActions import ActionCloseFile, ActionNewFile, ActionOpenFile, ActionQuit
# from PySide6.QtGui import 

from bin.TabViewManager import TabViewManager
from bin.Actions.ControlActions import ActionSettings, ControlActionGroup
from bin.UIManager import ThemeHandler
from bin.Widgets.PageSettings import PageSettings
from ui.uiMainWindow import Ui_MainWindow
from ui import icon_rc
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

        self._initControlPanel()

        self._initFile()
        self._initTask()
        self._initCalibration()
        self._initImage()
        self._initTabViewers()
        self._initSettings()
    
    @property
    def tabview_manager(self) -> TabViewManager:
        return self._tabview_manager
        
    def _initControlPanel(self):
        """
        Initialize the control panel on the left of the MainWindow.
        """
        self.control_tool_bar = ControlToolBar(self)
        self.control_tool_bar.initActions(self)
        self.addToolBar(Qt.LeftToolBarArea, self.control_tool_bar)
        self.ui.menuView_V.addActions(
            self.control_tool_bar.action_group.actions()
        )

    def _initFile(self):
        """
        Initialize the file menu.
        """
        self._action_new_file = ActionNewFile(self)
        self._action_open_file = ActionOpenFile(self)
        self._action_close_file = ActionCloseFile(self)
        self._action_quit = ActionQuit(self)
        self.ui.menuFile_F.addAction(self._action_new_file)
        self.ui.menuFile_F.addAction(self._action_open_file)
        self.ui.menuFile_F.addAction(self._action_close_file)
        self.ui.menuFile_F.addSeparator()
        self.ui.menuFile_F.addAction(self._action_quit)
        
    def _initSettings(self):
        """
        Initialize the settings menu.
        """
        self._action_settings = self.control_tool_bar._action_settings
        self.ui.menuSettings_S.addAction(self._action_settings)

    def _initTask(self):
        pass



    def _initCalibration(self):
        pass



    def _initImage(self):
        pass


    def _initTabViewers(self):
        """
        Initialize the viewers (tabWidgets)
        """
        self._tabview_manager = TabViewManager(self)
        self._tabview_manager.setTabWidget(self.ui.tabWidget_view)
        self._tabview_manager.initializeTabView()


class ControlToolBar(QToolBar):
    """
    This toolbar is used to show the control panel.

    A toolbar that do not show the border line.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setStyleSheet(
            "ControlToolBar{                            "
            "    border: none;                          "
            "    padding: 0px;                          "
            "}                                          "
            "ControlToolBar::separator{                 "
            "    width: 0px;                            "
            "}                                          "
            "ControlToolBar QToolButton{                "
            "    padding: 0;                            "
            "    margin: 0;                             "
            "    height: 54px;                          "
            "    width: 44px;                           "
            "}"
        )
        self._action_group = ControlActionGroup(self)
        self._action_settings = ActionSettings(self)
        self.setMovable(False)
        self.setContentsMargins(0,0,0,0)
        self.layout().setContentsMargins(0,0,0,0)
        self.setOrientation(Qt.Vertical)
        self.setIconSize(QSize(32, 32))
        self.setContextMenuPolicy(Qt.ActionsContextMenu)

    @property
    def action_group(self) -> ControlActionGroup:
        return self._action_group

    @property
    def action_settings(self) -> ActionSettings:
        return self._action_settings

    @property 
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler

    def initActions(self, main_window: MainWindow):
        """
        Initialize Actions to their corresponding widgets.
        """
        stacked_widget = main_window.ui.stackedWidget_control
        self.action_group.setStackedWidget(stacked_widget)
        for index, action in enumerate(self.action_group.actions()):
            action.setLinkedWidget(stacked_widget.widget(index))
            self.addAction(action)
        self.initSettingButton()

    def initSettingButton(self):
        """
        Initialize Setting Action.
        """
        self._setting_button = QToolButton(self)
        self._setting_button.setIcon(self._action_settings.icon())
        self._setting_button.clicked.connect(self._action_settings.trigger)
        self._vertical_spacer = QWidget(self)
        self._vertical_spacer.setSizePolicy(
            QSizePolicy.Preferred, 
            QSizePolicy.Expanding,
        )
        self.addWidget(self._vertical_spacer)
        self.addWidget(self._setting_button)
        self.theme_handler.theme_changed.connect(
            lambda: self._setting_button.setIcon(
                self._action_settings.icon()
            )
        )
        


    






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

