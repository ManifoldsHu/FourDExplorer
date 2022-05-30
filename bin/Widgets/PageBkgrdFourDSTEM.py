# -*- coding: utf-8 -*-

"""
*-------------------------- PageBkgrdFourDSTEM.py ----------------------------*
对 4D-STEM 衍射图样进行抠背底的界面。

部件内容：
    - WidgetPlotDP 用于使用 matplotlib 显示衍射图样
    - WidgetPlotHist 用于展示衍射图样的直方图以及过滤窗口。

提升部件：
    - 提升类名 PageBkgrdFourDSTEM.py
    - 头文件 bin.Widgets.PageBkgrdFourDSTEM

作者:           胡一鸣
创建日期:       2022年5月30日

The GUI page to subtract background of diffraction patterns.

Contents:
    - WidgetPlotDP, to view the diffraction patterns by matplotlib
    - WidgetPlotHist, control the filter window.

Promoted Widget:
    - name of widget class: PageBkgrdFourDSTEM
    - header file: bin.Widgets.PageBkgrdFourDSTEM

author:         Hu Yiming
date:           May 30, 2022
*-------------------------- PageBkgrdFourDSTEM.py ----------------------------*
"""

from PySide6.QtWidgets import QWidget, QMessageBox, QDialog
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas)
from PySide6.QtGui import QRegularExpressionValidator
from matplotlib.figure import Figure 
from matplotlib.axes import Axes 
from matplotlib.image import AxesImage 
from matplotlib.lines import Line2D
import numpy as np

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFHandler, HDFGroupNode, reValidHDFName
from bin.TaskManager import TaskManager
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.Widgets.PageBaseFourDSTEM import PageBaseFourDSTEM
from lib.TaskCalibration import TaskFourDSTEMFiltering
from ui import uiPageBkgrdFourDSTEM
from ui import uiDialogCreateFourDSTEM

class PageBkgrdFourDSTEM(PageBaseFourDSTEM):
    """
    对 4D-STEM 衍射图样进行抠背底操作的部件类。

    Ui 文件地址：ROOTPATH/ui/uiPageAlignFourDSTEM

    Widget to subtract backgrounds of 4D-STEM dataset.

    The path of the ui file: ROOTPATH/ui/uiPageBkgrdFourDSTEM

    attributes:
        hdf_handler: (HDFHandler) The handler to manage the hdf file and the 
            objects inside it.

        data_object: (h5py.Dataset) The data object of 4D-STEM data.

        data_path: (str) The path of the data object.

        logger: (Logger) Use logger to record information.

        dp_canvas: (FigureCanvas) The canvas (widget) object to show 
            Diffraction patterns.

        dp_figure: (Figure) The Figure object of the diffraction patterns.

        dp_ax: (Axes) The Axes object of the diffraction patterns.

        colorbar_ax: (Axes) The Axes object of the colorbar.

        dp_object: (AxesImage) The image object of the diffraction patterns.

        colorbar_object: (Colorbar) The Colorbar object. This colorbar is atta-
            ched to the diffraction patterns.

        dp_blit_manager: (BlitManager) The blit manager of the diffraction 
            patterns. When the data, norm, colormap or other attributes of the 
            diffraction pattern change, use its update() method to plot the 
            updated images.

        scan_ii: (int) The i-coordinate of the current diffraction pattern in 
            the real space. This is also regarded as the row index in a matrix.

        scan_jj: (int) The j-coordinate of the current diffraction pattern in
            the real space. This is also regarded as the column index in a 
            matrix.

        
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageBkgrdFourDSTEM.Ui_Form()
        self.ui.setupUi(self)

        self._initBaseUi()
        self._initUi()

        self._min_cursor_object = None 
        self._max_cursor_object = None 

        self._createAxes()
    
    @property 
    def min_cursor_object(self) -> Line2D:
        return self._min_cursor_object

    @property 
    def max_cursor_object(self) -> Line2D:
        return self._max_cursor_object

    @property 
    def task_manager(self) -> TaskManager:
        global qApp 
        return qApp.task_manager 

    @property
    def hist_canvas(self) -> FigureCanvas:
        return self.ui.widget_hist.canvas 

    @property
    def hist_figure(self) -> Figure:
        return self.ui.widget_hist.figure 

    @property
    def hist_ax(self) -> Axes:
        return self.ui.widget_hist.axes 

    @property
    def hist_blit_manager(self) -> BlitManager:
        return self.ui.widget_hist.blit_manager

    def _initUi(self):
        """
        Initialize Uis
        """
        self.setWindowTitle('4D-STEM Filtering')
        self.ui.pushButton_start.setProperty('class', 'danger')
        self.ui.pushButton_start.clicked.connect(self.startCalculation)
        self.ui.pushButton_start.setText('Start to Apply Filter Window')

        self.hist_ax.set_axis_on()


    def setFourDSTEM(self, data_path: str):
        """
        Set the data path in HDF5 file, to show the diffraction patterns.

        Will set the data_path attribute. The FourDSTEM must be a 4D matrix.

        arguments:
            data_path: (str) the path of the 4D-STEM data.

        raises:
            TypeError, KeyError, ValueError
        """
        super(PageBkgrdFourDSTEM, self).setFourDSTEM(data_path)
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape
        scan_ii = max(0, min(scan_i, self.scan_ii)) # Avoid out of boundary
        scan_jj = max(0, min(scan_j, self.scan_jj))
        self.ui.widget_hist.drawHist(
            self.data_object[scan_ii, scan_jj, :, :]
        )
        # self.hist_ax.autoscale()
        # self.hist_blit_manager.update()

    def _updateDP(self):
        """
        Update the current diffraction pattern according to the location in
        the real space. Will also update the histogram.
        """
        if self.data_object is None:
            return None 

        scan_i, scan_j, dp_i, dp_j = self.data_object.shape
        scan_ii = max(0, min(scan_i, self.scan_ii)) # Avoid out of boundary
        scan_jj = max(0, min(scan_j, self.scan_jj))
        dp = self.data_object[scan_ii, scan_jj, :, :]
        self.dp_object.set_data(dp)
        self.ui.widget_hist.drawHist(dp)
        self.colorbar_object.update_normal(self.dp_object)
        self.dp_blit_manager.update()
    
    def startCalculation(self):
        pass 



