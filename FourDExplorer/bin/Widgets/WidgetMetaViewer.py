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
from PySide6.QtWidgets import QToolBar 
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QActionGroup 


from bin.Actions.MetaActions import ActionEditMeta

from bin.UIManager import ThemeHandler 
from bin.MetaManager import MetaManager
from bin.HDFManager import HDFHandler
# from bin.Widgets.WidgetMetaViewerBase import MetaToolBar
from bin.Widgets.WidgetMetaViewerBase import WidgetMetaViewerBase
from bin.Actions.MetaActions import ActionAddMeta
from bin.Actions.MetaActions import ActionDeleteMeta
from bin.Actions.MetaActions import ActionEditMeta
from bin.Actions.MetaActions import ActionRefreshMeta
from bin.Actions.MetaActions import ActionSearchMeta
from Constants import MetaDataRoles 

from ui import uiWidgetMetaViewer

class WidgetMetaViewer(QWidget):
    """
    用于显示元数据的组件。

    Widget to show metadata of a dataset or group.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetMetaViewer.Ui_Form()
        self.ui.setupUi(self)

        self.ui.widget_meta_viewer.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.widget_meta_viewer_not_pathlike.setContextMenuPolicy(
            Qt.CustomContextMenu
        )
        self.ui.widget_meta_viewer.customContextMenuRequested.connect(
            self.showMetaViewerContextMenu
        )
        self.ui.widget_meta_viewer.search_result_found.connect(
            lambda: self.ui.tabWidget.setCurrentIndex(0)
        )
        
        self.ui.widget_meta_viewer_not_pathlike.customContextMenuRequested.connect(
            self.showMetaViewerNotPathlikeContextMenu
        )
        self.ui.widget_meta_viewer_not_pathlike.search_result_found.connect(
            lambda: self.ui.tabWidget.setCurrentIndex(1)
        )
        self.ui.tabWidget.setCurrentIndex(0)
        self._item_path = ''
        
        self._action_edit = ActionEditMeta(self) 
        self._action_refresh = ActionRefreshMeta(self)
        # self._action_search = ActionSearchMeta(self)
        self._action_add = ActionAddMeta(self)
        self._action_delete = ActionDeleteMeta(self)
        # self._initMetaActions()

        self._search_toolbar = MetaToolBar(self)
        self.ui.verticalLayout_3.insertWidget(0, self._search_toolbar)
        self._initSearch()


    @property 
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger
    
    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler    
    
    @property
    def meta_manager(self) -> MetaManager:
        global qApp 
        return qApp.requireMetaManager(self.item_path)
    
    # @property
    # def meta_tree(self) -> MetaTree:
    #     return self.meta_manager.meta_tree 
    
    # @property
    # def meta_tree_model(self) -> MetaTreeModel:
    #     return self.meta_manager.meta_tree_model
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler 
    
    @property
    def item_path(self) -> str:
        return self._item_path 

    @property 
    def action_edit(self) -> ActionEditMeta:
        return self._action_edit 
    
    @property
    def action_refresh(self) -> ActionRefreshMeta:
        return self._action_refresh 
    
    @property
    def action_search(self) -> ActionSearchMeta:
        return self._action_search 
    
    @property 
    def action_add(self) -> ActionAddMeta:
        return self._action_add 
    
    @property
    def action_delete(self) -> ActionDeleteMeta:
        return self._action_delete 
    
    def setItemPath(self, item_path: str):
        """
        Set the item path whose metadata is displayed by this viewer. And 
        initialize the table model. 

        arguments:
            item_path: (str) The path of the dataset or group.
        """
        if not isinstance(item_path, str):
            raise TypeError(
                f"item_path must be a str, not {type(item_path).__name__}"
            )
        self._item_path = item_path 
        self.ui.widget_meta_viewer.setItemPath(item_path)
        self.ui.widget_meta_viewer_not_pathlike.setItemPath(item_path)

    def showMetaViewerContextMenu(self, pos: QPoint):
        """
        Show context menu in the treeview of metadata.

        attributes:
            pos: (QPoint) The position where context menu should be created
        """
        act_widget = self.ui.widget_meta_viewer 
        index = self.ui.widget_meta_viewer.ui.treeView_meta.currentIndex()
        meta_key = index.data(role = MetaDataRoles.KeyRole)
        self.action_add.initialize(item_path = self.item_path)
        self.action_delete.initialize(
            item_path = self.item_path,
            meta_key = meta_key,
            widget_viewer = self.ui.widget_meta_viewer,
            widget_viewer_not_path_like = self.ui.widget_meta_viewer_not_pathlike,
            active_widget_viewer = act_widget,
        )
        self.action_edit.initialize(
            item_path = self.item_path,
            meta_key = meta_key,
            widget_viewer = self.ui.widget_meta_viewer,
            widget_viewer_not_path_like = self.ui.widget_meta_viewer_not_pathlike,
            active_widget_viewer = act_widget, 
        )
        self.action_refresh.initialize(
            widget_viewer_base = self.ui.widget_meta_viewer,
            widget_viewer_base_not_pathlike = self.ui.widget_meta_viewer_not_pathlike, 
        )
        menu = QMenu(self)
        menu.addAction(self.action_refresh)
        menu.addSeparator()
        menu.addAction(self.action_add)
        menu.addAction(self.action_edit)
        menu.addAction(self.action_delete)
        menu.exec(self.ui.widget_meta_viewer.mapToGlobal(pos))
        

    def showMetaViewerNotPathlikeContextMenu(self, pos: QPoint):
        """
        Show context menu in the tableview of metadata.

        attributes:
            pos: (QPoint) The position where context menu should be created
        """
        act_widget = self.ui.widget_meta_viewer_not_pathlike 
        index = self.ui.widget_meta_viewer_not_pathlike.ui.treeView_meta_not_pathlike.currentIndex()
        meta_key = index.data(role = MetaDataRoles.KeyRole)
        self.action_add.initialize(item_path = self.item_path)
        self.action_delete.initialize(
            item_path = self.item_path,
            meta_key = meta_key,
            widget_viewer = self.ui.widget_meta_viewer,
            widget_viewer_not_path_like = self.ui.widget_meta_viewer_not_pathlike,
            active_widget_viewer = act_widget,
        )
        self.action_edit.initialize(
            item_path = self.item_path,
            meta_key = meta_key,
            widget_viewer = self.ui.widget_meta_viewer,
            widget_viewer_not_path_like = self.ui.widget_meta_viewer_not_pathlike,
            active_widget_viewer = act_widget, 
        )
        self.action_refresh.initialize(
            widget_viewer_base = self.ui.widget_meta_viewer,
            widget_viewer_base_not_pathlike = self.ui.widget_meta_viewer_not_pathlike, 
        )
        menu = QMenu(self)
        menu.addAction(self.action_refresh)
        menu.addSeparator()
        menu.addAction(self.action_add)
        menu.addAction(self.action_edit)
        menu.addAction(self.action_delete)
        menu.exec(self.ui.widget_meta_viewer_not_pathlike.mapToGlobal(pos))

    def _initSearch(self):
        """
        Initialize the search toolbar.
        """
        self._lineEdit_search = QLineEdit('', parent = self)
        self._action_search = ActionSearchMeta(self._search_toolbar)
        self._action_search.initialize(
            linked_line_edit = self._lineEdit_search,
            widget_viewer_base = self.ui.widget_meta_viewer,
            widget_viewer_base_not_pathlike = self.ui.widget_meta_viewer_not_pathlike
        ) 
        self._lineEdit_search.addAction(self._action_search, QLineEdit.LeadingPosition)
        self._search_toolbar.addWidget(self._lineEdit_search)
        self._lineEdit_search.editingFinished.connect(self._action_search.trigger)


    
    # def showContextMenu(self, pos: QPoint):
    #     """
    #     Show context menu in the treeview or tableview of metadata.

    #     In this slot, actions will se their belonging item path and key.

    #     attributes:
    #         pos: (QPoint) The position where context menu should be created.
    #     """
    #     pass # TODO 

    # def _initMetaActions(self):
    #     """
    #     Initialize the actions to edit meta.
    #     """
        # self._action_edit = ActionEditMeta(self)
        # self._action_edit.initialize(item_path = self.item_path)
        # self._action_add = ActionAddMeta(self)
        # self._action_add.initialize(item_path = self.item_path)


class MetaToolBar(QToolBar):
    """
    The toolbar to search items in Meta tree.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setMovable(False)
        self.setFloatable(False)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        qss = self.theme_handler.getToolBarStyleSheet(self)
        self.setStyleSheet(qss)
        self.theme_handler.theme_changed.connect(self._update_style_sheet)

    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler 
    
    def _update_style_sheet(self):
        """
        When theme is changed, the style sheet must be updated.
        """
        qss = self.theme_handler.getToolBarStyleSheet(self)
        self.setStyleSheet(qss)




# class WidgetMetaViewer(WidgetMetaViewerBase):
#     """
#     用于显示元数据的组件。

#     Widget to show metadata of a dataset.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         # self.ui.treeView_meta.setModel()
#         self.ui.treeView_meta.setContextMenuPolicy(Qt.CustomContextMenu)
#         self.ui.treeView_meta.customContextMenuRequested.connect(self.showContextMenu)
#         self._action_edit = None 
#         self._initMetaActions()

#     @property 
#     def logger(self) -> Logger:
#         global qApp 
#         return qApp.logger 
    
#     @property
#     def theme_handler(self) -> ThemeHandler:
#         global qApp 
#         return qApp.theme_handler 
    
#     @property
#     def action_edit(self) -> ActionEditMeta:
#         return self._action_edit 
    
#     def showContextMenu(self, pos: QPoint):
#         """
#         Show context menu in the treeview of metadata.

#         In this slot, actions will set their belonging item path and key.

#         attributes:
#             pos: (QPoint) The position where context menu should be created.
#         """
#         self._action_edit.setItemPath(self.meta_manager.item_path)
#         index = self.ui.treeView_meta.currentIndex()
#         self._action_edit.setKeyFromIndex(index)
#         # menu = MetaViewerMenu(self)
#         menu = QMenu(self)
#         # menu.setLinkedMetaViewer(self)
#         menu.addAction(self._action_edit)
#         menu.exec(self.ui.treeView_meta.mapToGlobal(pos))

#     def _initMetaActions(self):
#         """
#         Initialize the actions to edit meta.
#         """
#         self._action_edit = ActionEditMeta(self)
#         self._action_edit.setLinkedTreeView(self.ui.treeView_meta)
        


# class MetaViewerMenu(QMenu):
#     """
#     当点到 MetaViewer 时的鼠标右键菜单。

#     The context menu of meta tree view.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self._meta_viewer = None 
        

#     @property
#     def meta_viewer(self) -> WidgetMetaViewer:
#         return self._meta_viewer 
    
#     def setLinkedMetaViewer(self, meta_viewer: WidgetMetaViewer):
#         """
#         Set the meta viewer of the menu.

#         arguments:
#             meta_viewer: (WidgetMetaViewer)
#         """
#         self._meta_viewer = meta_viewer 
#         # action_edit = self._meta_viewer.action_edit
#         # action_edit.setItemPath(self.meta_viewer.meta_manager.item_path)
#         # action_edit.setKeyFromIndex(
#         #     self._meta_viewer.ui.treeView_meta.currentIndex()
#         # )
#         self.addAction(self._meta_viewer.action_edit)
        

#     # def addActionGroup(self, group: QActionGroup, separator: bool = )
