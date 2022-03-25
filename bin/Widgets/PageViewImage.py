# -*- coding: utf-8 -*-

"""
*---------------------------- PageViewImage.py -------------------------------*
显示二维图像(单通道)的页面。

部件内容：
    - WidgetImagePlot 用于使用 Matplotlib 来显示图像
    - WidgetImageHistPlot 用于使用 Matplotlib 来显示图像的直方图

提升部件：
    - 提升类名 PageViewImage
    - 头文件 bin.Widgets.PageViewImage

作者:           胡一鸣
创建日期:       2022年3月25日

The GUI page to view 2D images (single channel).

Contents:
    - WidgetImagePlot, to view the 2D image
    - WidgetImageHistPlot, to view the histogram of the image

Promoted Widget:
    - name of widget class: PageViewImage
    - header file: bin.Widget.PageViewImage

author:         Hu Yiming
date:           Mar 25, 2022
*---------------------------- PageViewImage.py -------------------------------*
"""

from PySide6.QtWidgets import QWidget
from ui import uiPageViewImage

class PageViewImage(QWidget):
    """
    显示二维图像的部件类。

    Ui 文件地址：ROOT_PATH/ui/uiPageViewImage.ui

    Widget to view 2D images.

    The path of the ui file: ROOT_PATH/ui/uiPageViewImage.ui
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageViewImage.Ui_Form()
        self.ui.setupUi(self)
    