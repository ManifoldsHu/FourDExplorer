# -*- coding: utf-8 -*-

"""
*------------------------ DialogFindRotationAngle.py -------------------------*
寻找矢量场旋转角度(来把它转成保守场)的对话框。

部件内容：
    - WidgetPlotLine

作者:           胡一鸣
创建日期:       2022年6月2日

Dialog to find the rotation angle of the vector field (to correct it to be a 
convergent field).

Contents:
    - WidgetPlotLine

author:         Hu Yiming
date:           Jun 2, 2022
*------------------------ DialogFindRotationAngle.py -------------------------*
"""

from PySide6.QtWidgets import QDialog, QWidget
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas
)
from matplotlib.figure import Figure 
from matplotlib.axes import Axes 
from matplotlib.lines import Line2D
import numpy as np

from bin.BlitManager import BlitManager
from ui import uiDialogFindRotationAngle

class DialogFindRotationAngle(QDialog):
    """
    寻找矢量场旋转角度的部件类。

    Ui 文件地址: ROOTPATH/ui/uiDialogFindRotationAngle.ui

    Dialog to find the rotation angle of vector field.

    The path of the ui file: ROOTPATH/ui/uiDialogFindRotationAngle.ui

    attributes:

    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogFindRotationAngle.Ui_Dialog()
        self.ui.setupUi(self)

        self._createAxes()

    @property
    def curve_canvas(self) -> FigureCanvas:
        return self.ui.widget_curve.canvas 

    @property
    def curve_figure(self) -> Figure:
        return self.ui.widget_curve.figure 

    @property
    def curve_ax(self) -> Axes:
        return self._curve_ax 

    @property
    def curve_blit_manager(self) -> BlitManager:
        return self.ui.widget_curve.blit_manager

    def _createAxes(self):
        """
        Create the axes that contains the curve.
        """
        if self._curve_ax is None:
            self._curve_ax = self.curve_figure.add_subplot()
            self.curve_blit_manager.addArtist('curve_axes', self._curve_ax)

    def setVectorField(self, vec_path: str):
        """
        Set the data path in HDF5 file, to calculate the dcom-theta and curl
        com-theta curve.

        arguments:
            vec_path: (str) the path of the vector field.

        raises:
            TypeError, KeyError, ValueError
        """

    

