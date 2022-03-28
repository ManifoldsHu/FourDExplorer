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

class WidgetPlotBase(QWidget):
    """
    使用 matplotlib 进行绘制的部件基类。

    Base widget to plot items by matplotlib.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self._figure = Figure()
        self._canvas = FigureCanvas(self._figure)
        self._blit_manager = BlitManager(self._canvas)
        
        self.vertical_layout = QVBoxLayout()
        self._navigation_tool_bar = NavigationToolbar(self._canvas, self)
        self.vertical_layout.addWidget(self._navigation_tool_bar)
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

    def setToolBarVisible(self, visible: bool = True):
        """
        Set whether the navigation tool bar of matplotlib to hide.

        If this method is never called, the default state of the tool bar will
        be visible. 

        arguments:
            visible: (bool)
        """
        self._navigation_tool_bar.setVisible(visible)
    