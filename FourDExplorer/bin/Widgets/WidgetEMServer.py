# -*- coding: utf-8 -*-

"""
*---------------------------- WidgetEMServer.py ------------------------------*
管理与电镜服务器及相机进行通信的页面。

提升部件：
    - 提升类名 WidgetEMServer
    - 头文件 bin.Widgets.WidgetEMServer

作者：          胡一鸣
创建时间：      2022年6月13日

The GUI Widget to manage connections to TEM Server and camera.

Promoted Widget:
    - name of widget class: WidgetEMServer
    - header file: bin.Widgets.WidgetEMServer

author:         Hu Yiming
date:           Jun 13, 2022
*---------------------------- WidgetEMServer.py ------------------------------*
"""

from PySide6.QtWidgets import QWidget

class WidgetEMServer(QWidget):
    # TODO
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

