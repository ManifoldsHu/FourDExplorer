# -*- coding: utf-8 -*-

"""
*--------------------------- WidgetImagePlot.py ------------------------------*
使用 matplotlib 显示二维图像的部件类。

提升部件：
    - 提升类名 WidgetImagePlot
    - 头文件 bin.Widgets.WidgetImagePlot

作者:           胡一鸣
创建日期:       2022年3月26日

The GUI widget to show 2D image by matplotlib.

Promoted Widget:
    - name of widget class: WidgetImagePlot
    - header file: bin.Widgets.WidgetImagePlot

author:         Hu Yiming
date:           Mar 26, 2022
*--------------------------- WidgetImagePlot.py ------------------------------*
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQT as FigureCanvas,
    FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure
import numpy as np

from bin.BlitManager import BlitManager


class WidgetImagePlot(QWidget):
    """
    使用 matplotlib 显示 2D 图像的部件。

    Widget to show 2D images by matplotlib.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self._figure = Figure(tight_layout = True)
        self._canvas = FigureCanvas(self._figure)
        self._ax = self._figure.subplots()
        self._ax.set_aspect('equal')
        
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(
            NavigationToolbar(self._canvas, self))
        self.vertical_layout.addWidget(self._canvas)
        self.setLayout(self.vertical_layout)
        self.showImage()


    def showImage(self, data: np.ndarray = None):
        # test
        data = np.zeros((128, 128))
        img = self._ax.imshow(data)

        self.blit_manager = BlitManager(
            self._canvas,
            [img]
        )
        self._canvas.draw()
        self._canvas.flush_events()
                


        