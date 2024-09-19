# -*- coding: utf-8 -*-

"""
*-------------------------- WidgetAlignmentFDDNet.py ----------------------------*
对 4D-STEM 衍射图像，利用 FDDNet 进行明场衍射盘测量的界面。

提升部件:
    - 提升类名 WidgetAlignmentFDDNet
    - 头文件 bin.Widgets.WidgetAlignmentFDDNet

作者:           胡一鸣
创建日期:       2024年9月2日

The widget to measure the diffraction disk position by FDDNet.

Promoted Widget:
    - name of widget class: WidgetAlignmentFDDNet
    - header file: bin.Widgets.WidgetAlignmentFDDNet

author:         Hu Yiming
date:           Sep 2, 2024
*-------------------------------------------------------------------------------*
"""

from logging import Logger

from PySide6.QtWidgets import QWidget

from matplotlib.axes import Axes
from matplotlib.image import AxesImage

from h5py import Dataset

from bin.BlitManager import BlitManager
from ui import uiWidgetAlignmentFDDNet

class WidgetAlignmentFDDNet(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uiWidgetAlignmentFDDNet.Ui_Form()
        self.ui.setupUi(self)
        
    @property
    def current_dp_location(self):
        return (self.scan_ii, self.scan_jj)
    
    def setParentAlignPage(self, align_page: QWidget):
        """
        Set the parent alignment page.

        arguments:
            align_page: (PageAlignFourDSTEM) The parent alignment page containing the 4D-STEM data and UI elements.
        """
        self._align_page = align_page
        
    @property
    def dp_object(self) -> AxesImage:
        return self._align_page.dp_object
    
    @property
    def ax(self) -> Axes:
        return self._align_page.dp_ax
    
    @property
    def blit_manager(self) -> BlitManager:
        return self._align_page.dp_blit_manager
    
    @property
    def data_object(self) -> Dataset:
        return self._align_page.data_object
    
    @property
    def scan_ii(self) -> int:
        return self._align_page.scan_ii
    
    @property
    def scan_jj(self) -> int:
        return self._align_page.scan_jj
    
    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger
    
    
    
        
