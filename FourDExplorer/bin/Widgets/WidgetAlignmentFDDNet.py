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

from PySide6.QtWidgets import QWidget
from ui import uiWidgetAlignmentFDDNet

class WidgetAlignmentFDDNet(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uiWidgetAlignmentFDDNet.Ui_Form()
        self.ui.setupUi(self)
        
    