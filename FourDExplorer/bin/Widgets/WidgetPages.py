# -*- coding: utf-8 -*-

"""
*------------------------------ WidgetPages.py -------------------------------*
管理由 Tabview Manager 打开的页面。

提升部件：
    - 提升类名 WidgetPages
    - 头文件 bin.Widgets.WidgetPages

作者：          胡一鸣
创建时间：      2022年6月13日

The GUI Widget to manage pages opened by Tabview Manager.

Promoted Widget:
    - name of widget class: WidgetPages
    - header file: bin.Widgets.WidgetPages

author:         Hu Yiming
date:           Jun 13, 2022
*------------------------------ WidgetPages.py -------------------------------*
"""

from PySide6.QtCore import QAbstractListModel, QObject, QModelIndex, Qt
from PySide6.QtWidgets import QWidget 
from bin.TabViewManager import TabViewManager

from ui import uiWidgetPages

class WidgetPages(QWidget):
    # TODO
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetPages.Ui_Form()
        self.ui.setupUi(self)
        

    # @property 
    # def tabview_manager(self) -> TabViewManager:
    #     global qApp 
    #     return qApp.tabview_manager 

    def initModel(self):
        self.model = ModelTabs(self)
        self.ui.listView_pages.setModel(self.model)

    


class ModelTabs(QAbstractListModel):
    """
    Displaying opened pages.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)

    @property 
    def tabview_manager(self) -> TabViewManager:
        global qApp 
        return qApp.tabview_manager 

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return self.tabview_manager.tabWidget_view.count()

    def data(self, index: QModelIndex, role: int):
        row = index.row()
        if row >= 0 and row < self.tabview_manager.tabWidget_view.count():
            if role == Qt.DisplayRole:
                return self.tabview_manager.getTab(row).windowTitle()

    def headerData(self, section: int = 0, orientation: Qt.Orientation = Qt.Horizontal, role: int = Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return 'Pages'