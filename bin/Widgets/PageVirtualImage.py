# -*- coding: utf-8 -*-

"""
*--------------------------- PageVirtualImage.py -----------------------------*
用于计算 4D-STEM 虚拟成像的页面。

部件内容：
    - WidgetPlotDP 用于使用 matplotlib 来显示衍射图样
    - WidgetMaskCircle 用于绘制圆形区域
    - WidgetMaskRing 用于绘制环形区域
    - WidgetMaskWedge 用于绘制扇形区域
    - WidgetMaskRectangle 用于绘制矩形区域
    - WidgetMaskSegment2 用于绘制2分段环形区域
    - WidgetMaskSegment4 用于绘制4分段环形区域
    - WidgetMaskSegment6 用于绘制6分段环形区域
    - WidgetMaskSegment8 用于绘制8分段环形区域

提升部件：
    - 提升类名 PageVirtualImage
    - 头文件 bin.Widgets.PageVirtualImage

作者:           胡一鸣
创建日期:       2022年4月8日

The GUI page to calculate virtual images from 4D-STEM.

Contents:
    - WidgetPlotDP, to view the diffraction patterns
    - WidgetMaskCircle, to draw circular region
    - WidgetMaskRing, to draw annular region
    - WidgetMaskWedge, to draw fan-shaped region
    - WidgetMaskRectangle, to draw rectangular region
    - WidgetMaskSegment2, to draw 2-segmented annular regions
    - WidgetMaskSegment4, to draw 4-segmented annular regions
    - WidgetMaskSegment6, to draw 6-segmented annular regions
    - WidgetMaskSegment8, to draw 8-segmented annular regions

Promoted Widget:
    - name of widget class: PageVirtualImage
    - header file: bin.Widget.PageVirtualImage

author:         Hu Yiming
date:           Apr 8, 2022
*--------------------------- PageVirtualImage.py -----------------------------*
"""

from logging import Logger
# from typing import List, Tuple

from PySide6.QtWidgets import QWidget, QMessageBox

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.colorbar import Colorbar, make_axes
from matplotlib.colors import Normalize, SymLogNorm
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.image import AxesImage
from matplotlib.axis import Axis
from matplotlib.lines import Line2D
from matplotlib.patches import Circle, Rectangle, Wedge

import numpy as np
import h5py

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFHandler
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.Widgets.PageBaseFourDSTEM import PageBaseFourDSTEM
from ui import uiPageVirtualImage

class PageVirtualImage(PageBaseFourDSTEM):
    """
    进行虚拟成像的部件类。

    Ui 文件地址：ROOTPATH/ui/uiPageVirtualImage

    Widget to calculate Virtual Image.

    The path of the ui file: ROOTPATH/ui/uiPageVirtualImage

    attributes:
        hdf_handler: (HDFHandler) The handler to manage the hdf file and the
            objects inside it.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageVirtualImage.Ui_Form()
        self.ui.setupUi(self)

        self._initBaseUi()

        self.ui.comboBox_mode.currentIndexChanged.connect(
            self.changeMode
        )
        self._max_segment_num = 10      # The maximum number of segmented ring.
        self._mask_widgets = []         # Must be the same order as the mode.
        self._initMasks()
        self.setWindowTitle('Virtual Image')
        

    @property
    def mask_index(self) -> int:
        """
        Indicates which mask is used:
            0       Circle
            1       Ring
            2       Wedge
            3       Rectangle
            4       Segmented Ring
        """
        return self.ui.comboBox_mode.currentIndex()

    def _initMasks(self):
        """
        Initialize all of the mask patches, and add them to the axes.
        """
        self.ui.comboBox_mode.setCurrentIndex(0)
        self.ui.stackedWidget_masks.setCurrentIndex(self.mask_index)
        self.ui.comboBox_mode.currentIndexChanged.connect(self._changeMode)

        self._initCircle()
        self._initRing()
        self._initWedge()
        self._initRectangle()
        self._initSegments()
        

    def _initCircle(self):
        """
        Initialize the circle patch and its managers.
        """
        self._patch_circle = Circle(
            (0, 0),
            radius = 5,
            edgecolor = None,
            facecolor = 'black',
            alpha = 0.3,
            visible = False,
            fill = True,
        )
        
        self.ui.page_circle.setPatch(self._patch_circle)
        self.ui.page_circle.setBlitManager(self.dp_blit_manager)
        self._mask_widgets.append(self.ui.page_circle)

    def _initRing(self):
        """
        Initialize the ring patch and its managers.
        """
        self._patch_ring = Wedge(
            (0, 0),
            r = 5,                  # outer radius
            theta_1 = 0,
            theta_2 = 360,
            width = 3,              # outer radius - inner radius
            edgecolor = None,
            facecolor = 'black',
            alpha = 0.3,
            visible = False,
            fill = True,
        )
        
        self.ui.page_ring.setPatch(self._patch_ring)
        self.ui.page_ring.setBlitManager(self.dp_blit_manager)
        self._mask_widgets.append(self.ui.page_ring)

    def _initWedge(self):
        """
        Initialize the wedge patch and its managers.
        """
        self._patch_wedge = Wedge(
            (0, 0),
            r = 5,
            theta_1 = 0,
            theta_2 = 120,
            width = 3,
            edgecolor = None,
            facecolor = 'black',
            alpha = 0.3,
            visible = False,
            fill = True,
        )
        self.dp_blit_manager.addArtist(self._patch_wedge)
        self.ui.page_wedge.setBlitManager(self.dp_blit_manager)
        self._mask_widgets.append(self.ui.page_wedge)

    def _initRectangle(self):
        """
        Initialize the rectangle patch and its managers.
        """
        self._patch_rectangle = Rectangle(
            (0, 0),
            width = 5,
            height = 3,
            edgecolor = None,
            facecolor = 'black',
            alpha = 0.3,
            visible = False,
            fill = True,
        )
        self.dp_blit_manager.addArtist(self._patch_rectangle)
        self.ui.page_rectangle.setBlitManager(self.dp_blit_manager)
        self._mask_widgets.append(self.ui.page_rectangle)

    def _initSegments(self):
        """
        Initialize the segmented patches and their managers.
        """
        self._patch_segments = []
        for ii in range(self._max_segment_num):
            _wedge = Wedge(
                (0, 0),
                r = 5,
                theta_1 = 0,
                theta_2 = 180,
                width = 3,
                edgecolor = None,
                face_color = 'black',
                alpha = 0.3,
                visible = False,
                fill = True,
            )
            self._patch_segments.append(_wedge)
            self.dp_blit_manager.addArtist(_wedge)
        self.ui.page_segment_ring.setBlitManager(self.dp_blit_manager)
        self._mask_widgets.append(self.ui.page_segment_ring)


    def setFourDSTEM(self, data_path: str):
        """
        Set the data path in HDF5 file, to show the diffraction patterns.

        Will set the data_path attribute. The FourDSTEM must be a 4D matrix.

        arguments:
            data_path: (str) the path of the 4D-STEM data.

        raises:
            TypeError, KeyError, ValueError
        """
        super(PageVirtualImage, self).setFourDSTEM(data_path)
        scan_i, scan_j, dp_i, dp_j = self.hdf_handler.file[data_path].shape
        for widget in self._mask_widgets:
            widget.setCenter(
                ((dp_j - 1)/2, (dp_i - 1)/2)
            )
        
    def changeMode(self):
        """
        Change mask patch's mode according to mask index.
        """
        self.ui.stackedWidget_masks.setCurrentIndex(self.mask_index)

        # Set the patch visible according to the index
        for ii, widget in enumerate(self._mask_widgets):
            widget.setMaskActivate(ii == self.mask_index)

    def calcMask(self):
        pass
        
        

    

        
        




