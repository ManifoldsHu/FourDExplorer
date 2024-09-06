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

from PySide6.QtWidgets import QWidget
from ui import uiWidgetAlignmentRef

class WidgetAlignmentRef(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uiWidgetAlignmentRef()
        self.ui.setupUi(self)
