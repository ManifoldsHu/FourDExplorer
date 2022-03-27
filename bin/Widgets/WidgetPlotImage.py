# -*- coding: utf-8 -*-

"""
*--------------------------- WidgetPlotImage.py ------------------------------*
使用 matplotlib 显示二维图像的部件类。

提升部件：
    - 提升类名 WidgetPlotImage
    - 头文件 bin.Widgets.WidgetPlotImage

作者:           胡一鸣
创建日期:       2022年3月26日

The GUI widget to show 2D image by matplotlib.

Promoted Widget:
    - name of widget class: WidgetPlotImage
    - header file: bin.Widgets.WidgetPlotImage

author:         Hu Yiming
date:           Mar 26, 2022
*--------------------------- WidgetPlotImage.py ------------------------------*
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure
import numpy as np

from bin.BlitManager import BlitManager
from bin.Widgets.WidgetPlotBase import WidgetPlotBase

class WidgetPlotImage(WidgetPlotBase):
    """
    使用 matplotlib 显示 2D 图像的部件。

    Widget to show 2D images by matplotlib.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
    
    


# class WidgetPlotImage(QWidget):
#     """
#     使用 matplotlib 显示 2D 图像的部件。

#     Widget to show 2D images by matplotlib.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self._figure = Figure(tight_layout = True)
#         self._canvas = FigureCanvas(self._figure)
#         self._ax = self._figure.subplots()
#         self._ax.set_aspect('equal')
        
#         self.vertical_layout = QVBoxLayout()
#         self.vertical_layout.addWidget(
#             NavigationToolbar(self._canvas, self))
#         self.vertical_layout.addWidget(self._canvas)
#         self.setLayout(self.vertical_layout)
        
#         self._blit_manager = BlitManager(self._canvas)
        # self.showImage()


    # def showImage(self, data: np.ndarray = None):
    #     # test
    #     # data = np.zeros((128, 128))
    #     # img = self._ax.imshow(data)

    #     self.blit_manager = BlitManager(
    #         self._canvas,
    #         [img]
    #     )
    #     self._canvas.draw()
    #     self._canvas.flush_events()
                


        