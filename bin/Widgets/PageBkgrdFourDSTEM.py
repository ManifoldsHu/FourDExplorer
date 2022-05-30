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

from PySide6.QtWidgets import QWidget
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure 
from matplotlib.axes import Axes 
from matplotlib.lines import Line2D
import numpy as np

from bin.BlitManager import BlitManager
from bin.TaskManager import TaskManager
from bin.Widgets.DialogSaveFourDSTEM import DialogSaveFourDSTEM
from bin.Widgets.PageBaseFourDSTEM import PageBaseFourDSTEM
from lib.TaskCalibration import TaskFourDSTEMFiltering
from ui import uiPageBkgrdFourDSTEM

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

        self._min_cursor_object = None 
        self._max_cursor_object = None 

        self._createAxes()
        self._initCursor()

        self._initBaseUi()
        self._initUi()
    
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

    @property 
    def window_min(self) -> float:
        return self.ui.doubleSpinBox_window_min.value()

    @property
    def window_max(self) -> float:
        return self.ui.doubleSpinBox_window_max.value()

    def _initUi(self):
        """
        Initialize Uis
        """
        self.setWindowTitle('4D-STEM Filtering')
        self.ui.pushButton_start.setProperty('class', 'danger')
        self.ui.pushButton_start.clicked.connect(self.startCalculation)
        self.ui.pushButton_start.setText('Start to Apply Filter Window')

        self.hist_ax.set_axis_on()
        self.ui.doubleSpinBox_window_min.setRange(-2147483648, 2147483647)
        self.ui.doubleSpinBox_window_max.setRange(-2147483648, 2147483647)
        self.ui.doubleSpinBox_window_min.valueChanged.connect(
            self._moveHistCursor
        )
        self.ui.doubleSpinBox_window_max.valueChanged.connect(
            self._moveHistCursor
        )
        self.ui.doubleSpinBox_window_min.valueChanged.connect(
            self._updateDP
        )
        self.ui.doubleSpinBox_window_max.valueChanged.connect(
            self._updateDP 
        )
        self.ui.checkBox_apply_window_max.stateChanged.connect(
            self._updateDP 
        )
        self.ui.checkBox_apply_window_min.stateChanged.connect(
            self._updateDP 
        )
        
    def _initCursor(self):
        """
        Initialize cursors in the histogram.
        """
        self._min_cursor_object = self.hist_ax.axvline(x = self.window_min)
        self.hist_blit_manager.addArtist('min_cursor', self.min_cursor_object)

        self._max_cursor_object = self.hist_ax.axvline(x = self.window_max)
        self.hist_blit_manager.addArtist('max_cursor', self.max_cursor_object)
        self.hist_blit_manager.update()

    def _moveHistCursor(self):
        """
        Move the location of the cursor of the histogram.
        """
        self.min_cursor_object.set_xdata(self.window_min)
        self.max_cursor_object.set_xdata(self.window_max)
        self.hist_blit_manager.update()

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
        dp_data = self.data_object[scan_ii, scan_jj, :, :]
        self.ui.widget_hist.drawHist(dp_data)
        self.ui.doubleSpinBox_window_min.setValue(np.min(dp_data))
        self.ui.doubleSpinBox_window_max.setValue(np.max(dp_data))
        self.hist_blit_manager.update()

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

        if self.ui.checkBox_apply_window_max.isChecked():
            dp[dp > self.window_max] = self.window_max 
        if self.ui.checkBox_apply_window_min.isChecked():
            dp[dp < self.window_min] = 0

        self.dp_object.set_data(dp)
        self.ui.widget_hist.drawHist(dp)
        self.colorbar_object.update_normal(self.dp_object)
        self.dp_blit_manager.update()
    
    def startCalculation(self):
        """
        Start to apply the filtering window for all diffraction patterns.
        """
        dialog_save = DialogSaveFourDSTEM(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return 
        if dialog_save.getIsInplace():
            data_node = self.hdf_handler.getNode(self.data_path)
            output_name = data_node.name 
            output_parent_path = data_node.parent.path 
        else:
            output_name = dialog_save.getNewName()
            output_parent_path = dialog_save.getParentPath()
        
        meta = self.data_object.attrs 
        if 'filter_window_min' in meta:
            meta['filter_window_min'] = max(
                meta['filter_window_min'], 
                self.window_min
            )
        else:
            meta['filter_window_min'] = self.window_min 

        if 'filter_window_max' in meta:
            meta['filter_window_max'] = min(
                meta['filter_window_max'],
                self.window_max 
            )
        else:
            meta['filter_window_max'] = self.window_max 

        self.task = TaskFourDSTEMFiltering(
            self.data_path,
            output_parent_path,
            output_name,
            self.window_min,
            self.window_max,
            **meta,
        )
        self.task_manager.addTask(self.task)



