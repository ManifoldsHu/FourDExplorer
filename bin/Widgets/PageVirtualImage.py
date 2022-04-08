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
from matplotlib.patches import Circle

import numpy as np
import h5py

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFHandler
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from ui import uiPageVirtualImage



