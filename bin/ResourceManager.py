# -*- coding: utf-8 -*-

"""
*---------------------------- ResourceManager.py -----------------------------*
用于管理文件资源 (诸如图标) 。

作者:           胡一鸣
创建日期:       2022年6月8日

Manage file resources like icons.

author:         Hu Yiming
date:           Jun 8, 2022
*---------------------------- ResourceManager.py -----------------------------*
"""

from PySide6.QtCore import QObject 
from PySide6.QtGui import QIcon 

from ui.resources import icon_rc

class ResourceManager(QObject):
    def __init__(self, parent: QObject):
        super().__init__(self)
