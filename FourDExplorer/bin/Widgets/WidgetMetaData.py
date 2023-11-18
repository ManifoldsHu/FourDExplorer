#-*- coding: utf-8 -*- 

"""
*----------------------------- WidgetMetaData.py -----------------------------*
通过树状视图 (QTreeView) 来展示具有层次结构的 Metadata。

作者：          胡一鸣
创建时间：      2023年11月15日

Displaying metadata using QTreeView.

author:         Hu Yiming
date:           Nov 15, 2023
*----------------------------- WidgetMetaData.py -----------------------------*
"""

from logging import Logger 

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMenu, QWidget, QInputDialog, QWidgetAction, QTreeView, QTreeWidget
from PySide6.QtGui import QActionGroup 

from bin.MetaManagers.MetaManagers import MetaManagerFourDSTEM, MetaManagerImg, MetaManagerVec

from bin.MetaManagers.UnitManager import UnitManager
from bin.MetaManagers.MetadataFields import IntField, FloatField, StringField

class WidgetMetaDataBase(QWidget):
    """
    浏览预定义的 Metadata 结构的基类
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.tree_view = QTreeView(self)
        # self.