#-*- coding: utf-8 -*- 

"""
*-------------------------- WidgetAlignmentManual.py ----------------------------*

对 4D-STEM 衍射图样进行手动平移、合轴的部件。

提升部件：
    - 提升类名 WidgetAlignmentManual
    - 头文件 bin.Widgets.WidgetAlignmentManual

作者:           胡一鸣
创建日期:       2024年9月2日

The widget to align 4D-STEM dataset manually.

Promoted Widget:
    - name of widget class: WidgetAlignmentManual
    - header file: bin.Widgets.WidgetAlignmentManual

author:         Hu Yiming
date:           Sep 2, 2024
*-------------------------- WidgetAlignmentManual.py ----------------------------*
"""


from PySide6.QtWidgets import QWidget
from ui import uiWidgetAlignmentManual

class WidgetAlignmentManual(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uiWidgetAlignmentManual()
        self.ui.setupUi(self)
