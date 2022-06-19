# -*- coding: utf-8 -*-
"""
*---------------------------- WidgetPlotBase.py ------------------------------*
使用 matplotlib 进行绘制的部件基类。

作者:           胡一鸣
创建日期:       2022年3月26日

The GUI base widget to render data by matplotlib.

author:         Hu Yiming
date:           Mar 26, 2022
*---------------------------- WidgetPlotBase.py ------------------------------*
"""

# from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure
import numpy as np

from bin.BlitManager import BlitManager
from bin.UIManager import ThemeHandler

class WidgetPlotBase(QWidget):
    """
    使用 matplotlib 进行绘制的部件基类。

    Base widget to plot items by matplotlib.
    """
    # This is where icons is saved in the resource system of qt.
    icon_resource = u':/MatplotlibNavigation/icons/'
    
    # The icon's name of the corresponding actions.
    toolicon = {
            'Home': 'home',
            'Back': 'back',
            'Forward': 'forward',
            'Pan': 'move',
            'Zoom': 'zoom_to_rect',
            'Subplots': 'subplots',
            'Customize': 'qt4_editor_options',
            'Save': 'filesave',
    }

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self._figure = Figure()
        self._canvas = FigureCanvas(self._figure)
        self._blit_manager = BlitManager(self._canvas)
        
        self.vertical_layout = QVBoxLayout()
        self._navigation_toolbar = NavigationToolbar(self._canvas, self)
        self._setToolbarIcons()
        self.vertical_layout.addWidget(self._navigation_toolbar)
        self.vertical_layout.addWidget(self._canvas)
        self.setLayout(self.vertical_layout)
        
    @property
    def figure(self) -> Figure:
        return self._figure

    @property
    def canvas(self) -> FigureCanvas:
        return self._canvas

    @property
    def blit_manager(self) -> BlitManager:
        return self._blit_manager

    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp
        return qApp.theme_handler

    def setToolbarVisible(self, visible: bool = True):
        """
        Set whether the navigation tool bar of matplotlib to hide.

        If this method is never called, the default state of the tool bar will
        be visible. 

        arguments:
            visible: (bool)
        """
        self._navigation_toolbar.setVisible(visible)
    
    def _setToolbarIcons(self):
        """
        Set the icons of actions in the navigation tool bar.

        The original icons are invisible in dark theme. So here we provide 
        the different icons when dark theme mode is used.
        """
        for tool_action in self._navigation_toolbar.actions():
            action_text = tool_action.text()
            if action_text in self.toolicon:
                icon = self.theme_handler.iconProvider(
                    self.icon_resource + self.toolicon[action_text] + '.png'
                )
                tool_action.setIcon(icon)
