# -*- coding: utf-8 -*-

"""
*--------------------------- ControlActions.py -------------------------------*
针对主界面左侧控制面板的各个 Object 的各个 Actions。

作者:           胡一鸣
创建日期:       2022年6月13日

This module includes actions towards left control tabs in the MainWindow.

author:         Hu Yiming
date:           Jun 13, 2022
*--------------------------- ControlActions.py -------------------------------*
"""

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget, QStackedWidget
from PySide6.QtGui import QActionGroup, QAction

from bin.UIManager import ThemeHandler
from bin.Widgets.PageSettings import PageSettings

class ControlActionGroup(QActionGroup):
    """
    The action group of left control tabs in the MainWindow.
    """
    def __init__(self, parent: QObject):
        super().__init__(parent)
        
        self._control_actions = [
            ActionFile(self),
            ActionPages(self),
            ActionTask(self),
            ActionComputer(self),
            ActionEMServer(self),
        ]
        for action in self._control_actions:
            self.addAction(action)

        self._stacked_widget = None 
        self.setExclusionPolicy(self.ExclusionPolicy.ExclusiveOptional)
        self._control_actions[0].toggle()
    
    def setStackedWidget(self, stacked_widget: QStackedWidget):
        """
        Set the stacked_widget that contains controlling tabs.
        """
        self._stacked_widget = stacked_widget 
        for action in self._control_actions:
            action.setStackedWidget(self._stacked_widget)
    

class ActionControlBase(QAction):
    """
    The base action of controll tabs in the MainWindow.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setCheckable(True)
        self.toggled.connect(self.openWidget)
        self._linked_widget = None 
        self._stacked_widget = None 
        self._icon_name = ''
        self.theme_handler.theme_changed.connect(
            self._updateIcon
        )

    
    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler

    def initIconResource(self, icon_name: str):
        """
        Initialize the resource of icons.

        arguments:
            icon_name: (str) the name of icon.
        """
        _path = ':/ControlPanel/resources/icons/' + icon_name
        icon = self.theme_handler.iconProvider(_path)
        self._icon_name = icon_name 
        self.setIcon(icon)

    def setStackedWidget(self, stacked_widget: QStackedWidget):
        """
        Set the stacked_widget that contains controlling tabs.
        """
        self._stacked_widget = stacked_widget 

    def setLinkedWidget(self, widget: QWidget):
        """
        Set the linked widget which will appears when this is triggered.

        arguments:
            widget: (QWidget)
        """
        self._linked_widget = widget 
        
    def openWidget(self, is_toggled: bool):
        """
        When this action is triggered, this slot will be called.

        The linked widget will be opened or closed in the stacked widget.

        arguments:
            is_toggled: (bool) whether this action is toggled.
        """
        if self._stacked_widget is None:
            return
        if self._linked_widget is None:
            return 
        if is_toggled:
            self._stacked_widget.setVisible(True)
            self._stacked_widget.setCurrentWidget(self._linked_widget)
        else:
            self._stacked_widget.setVisible(False)

    def _updateIcon(self):
        """
        Will update the icon when the theme mode changes.
        """
        _path = ':/ControlPanel/resources/icons/' + self._icon_name
        icon = self.theme_handler.iconProvider(_path)
        self.setIcon(icon)


class ActionFile(ActionControlBase):
    """
    When this action is triggered, the 'File' tab will be opened.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('File')
        self.initIconResource('folder_open')

class ActionPages(ActionControlBase):
    """
    When this action is triggered, the 'Pages' tab will be opened.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Pages')
        self.initIconResource('image_text')
        
class ActionTask(ActionControlBase):
    """
    When this action is triggered, the 'Task' tab will be opened.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Task')
        self.initIconResource('work')

class ActionComputer(ActionControlBase):
    """
    When this action is triggered, the 'System Info' tab will be opened.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('System Information')
        self.initIconResource('computer')

class ActionEMServer(ActionControlBase):
    """
    When this action is triggered, the 'EMServer' tab will be opened.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Microscopy Server')
        self.initIconResource('server')

class ActionSettings(ActionControlBase):
    """
    When this action is triggered, will show a page for settings.
    """

    @property
    def tabview_manager(self):
        global qApp
        return qApp.tabview_manager

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Settings')
        self.initIconResource('setting')
        self.triggered.connect(self.openSettings)

    def openSettings(self):
        """
        Will open a page for settings.
        """
        page = PageSettings()
        self.tabview_manager.openTab(page)
        
        
        

