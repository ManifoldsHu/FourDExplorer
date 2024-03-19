#-*- coding: utf-8 -*- 

"""
*---------------------------- WidgetMetaViewer.py ----------------------------*
通过树状视图 (QTreeView) 来展示具有层次结构的 Metadata。

作者：          胡一鸣
创建时间：      2023年11月15日

Displaying metadata using QTreeView.

author:         Hu Yiming
date:           Nov 15, 2023
*---------------------------- WidgetMetaViewer.py ----------------------------*
"""

# from logging import Logger 

# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QMenu, QWidget, QInputDialog, QWidgetAction, QTreeView, QTreeWidget
# from PySide6.QtGui import QActionGroup 

# from bin.MetaManagers.MetaManagers import MetaManagerFourDSTEM, MetaManagerImg, MetaManagerVec

# from bin.MetaManagers.UnitManager import UnitManager
# from bin.MetaManagers.MetadataFields import IntField, FloatField, StringField

# class WidgetMetaDataBase(QWidget):
#     """
#     浏览预定义的 Metadata 结构的基类
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self.tree_view = QTreeView(self)
#         # self.


from logging import Logger 

from PySide6.QtCore import Qt 
from PySide6.QtCore import QPoint 
from PySide6.QtWidgets import QMenu 
from PySide6.QtWidgets import QWidget 
from PySide6.QtGui import QActionGroup 

from bin.Actions.MetaActions import ActionEditMeta

from bin.UIManager import ThemeHandler 
from bin.Widgets.WidgetMetaViewerBase import MetaToolBar
from bin.Widgets.WidgetMetaViewerBase import WidgetMetaViewerBase
from Constants import MetaDataRoles 

class WidgetMetaViewer(WidgetMetaViewerBase):
    """
    用于显示元数据的组件。

    Widget to show metadata of a dataset.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.ui.treeView_meta.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeView_meta.customContextMenuRequested.connect(self.showContextMenu)
        self._action_edit = None 
        self._initMetaActions()

    @property 
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger 
    
    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler 
    
    @property
    def action_edit(self) -> ActionEditMeta:
        return self._action_edit 
    
    def showContextMenu(self, pos: QPoint):
        """
        Show context menu in the treeview of metadata.

        attributes:
            pos: (QPoint) The position where context menu should be created.
        """
        index = self.ui.treeView_meta.currentIndex()
        menu = MetaViewerMenu(self, index)
        menu.exec(self.ui.treeView_meta.mapToGlobal(pos))

    def _initMetaActions(self):
        """
        Initialize the actions to edit meta.
        """
        self._action_edit = ActionEditMeta(self)
        self._action_edit.setLinkedTreeView(self.ui.treeView_meta)
        


class MetaViewerMenu(QMenu):
    """
    当点到 MetaViewer 时的鼠标右键菜单。

    The context menu of meta tree view.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self._meta_viewer = None 
        

    @property
    def meta_viewer(self) -> WidgetMetaViewer:
        return self._meta_viewer 
    
    def setLinkedMetaViewer(self, meta_viewer: WidgetMetaViewer):
        """
        Set the meta viewer of the menu.

        arguments:
            meta_viewer: (WidgetMetaViewer)
        """
        self._meta_viewer = meta_viewer 
        self.addActions(self._meta_viewer.action_edit)

    # def addActionGroup(self, group: QActionGroup, separator: bool = )
