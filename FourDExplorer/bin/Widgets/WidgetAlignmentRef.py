#-*- coding: utf-8 -*- 

"""
*-------------------------- WidgetAlignmentRef.py ----------------------------*

通过使用 Reference 对 4D-STEM 数据集进行平移、合轴的部件。

提升部件:
    - 提升类名 WidgetAlignmentRef 
    - 头文件 bin.Widgets.WidgetAlignmentRef

作者:           胡一鸣
创建日期:       2024年9月2日

The widget to align 4D-STEM dataset by using reference dataset.

Promoted Widget:
    - name of widget class: WidgetAlignmentRef
    - header file: bin.Widgets.WidgetAlignmentRef

author:         Hu Yiming
date:           Sep 2, 2024
*-------------------------- WidgetAlignmentRef.py ----------------------------*
"""

from logging import Logger

from PySide6.QtWidgets import QWidget

import numpy as np
from matplotlib.axes import Axes
from matplotlib.image import AxesImage
from h5py import Dataset

from bin.BlitManager import BlitManager

from ui import uiWidgetAlignmentRef

class WidgetAlignmentRef(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uiWidgetAlignmentRef.Ui_Form()
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