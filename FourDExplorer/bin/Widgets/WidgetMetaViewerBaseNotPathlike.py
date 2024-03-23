# -*- coding: utf-8 -*-

"""
*------------------- WidgetMetaViewerBaseNotPathlike.py ----------------------*
用于展示元数据中，不是类似于路径的那些元数据的 Widget，里面包含一个 QTableView。
具体来说，不是类似于路径的元数据包括：
- 不以 / 开头的
- 含有连续斜杠 / 的
- 以 / 结尾的 (除单独的 / 以外) 
至于那些类似于路径的元数据，则由 WidgetMetaViewerBase 来显示。

作者：          胡一鸣
创建时间：      2024年3月20日

A Widget for displaying metadata other than metadata like paths, which contains a QTableView.

Specifically, metadata that is not path-like include:
- Ones that don't start with /
- Those with continuous slash /
- Ending in/(except the separate /)

The WidgetMetaViewerBase displays metadata like paths.

author:         Hu Yiming
date:           Mar 20, 2024
*------------------- WidgetMetaViewerBaseNotPathlike.py ----------------------*
"""

from logging import Logger 

from PySide6.QtWidgets import QWidget 
from PySide6.QtWidgets import QToolBar
from PySide6.QtWidgets import QTableView
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QTreeView
from PySide6.QtGui import QAction 
from PySide6.QtCore import Qt
from PySide6.QtCore import QObject
from PySide6.QtCore import QModelIndex
from PySide6.QtCore import Signal

from bin.MetaManager import MetaManager 
from bin.MetaManager import MetaTree 
from bin.MetaManager import MetaNotPathLikeModel
from bin.HDFManager import HDFHandler
from bin.UIManager import ThemeHandler
from Constants import MetaDataRoles

from ui import uiWidgetMetaViewerBaseNotPathlike

class WidgetMetaViewerBaseNotPathlike(QWidget):
    """
    查看非路径形式的元数据的基类。

    The base widget to view metadata whose keys are not path-like.
    """

    search_result_found = Signal()  # The search action has a result

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetMetaViewerBaseNotPathlike.Ui_Form()
        self.ui.setupUi(self)

        self._item_path = ''
        self._last_kw = ''
        self._result_generator = None 

    @property
    def meta_manager(self) -> MetaManager:
        global qApp 
        return qApp.requireMetaManager(self.item_path)
    
    @property
    def meta_tree(self) -> MetaTree:
        return self.meta_manager.meta_tree 
    
    @property
    def meta_not_pathlike_table_model(self) -> MetaNotPathLikeModel:
        return self.meta_manager.meta_not_pathlike_table_model 
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler 
    
    @property
    def item_path(self) -> str:
        return self._item_path 
    
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
        self.meta_manager.model_refreshed.connect(self.resetModel)
        self.ui.treeView_meta_not_pathlike.setModel(
            self.meta_not_pathlike_table_model
        )
        self.ui.treeView_meta_not_pathlike.expandAll()  # Without which search won't work properly

        # Only after model is set, header can be set.
        header = self.ui.treeView_meta_not_pathlike.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)

    def refreshModel(self):
        """
        Refresh the metadata tableview.
        """
        self.meta_manager.refreshModel()

    def resetModel(self):
        """
        On meta manager refresh the model, this function should be called.
        """
        self.ui.treeView_meta_not_pathlike.setModel(
            self.meta_not_pathlike_table_model
        )
        self.ui.treeView_meta_not_pathlike.expandAll()

    def searchItem(self, kw: str):
        """
        Search metadata using given keyword in table indexes.

        Metadata that has keyword included in key will be given. The current 
        index will be moved to the searched one.

        arguments:
            kw: (str) The keyword to be searched.

        returns:
            (int) Whether there is a result of searching:
                0       a result is found
                -1      kw is empty
                -2      no valid result generator
                -3      no more results
        """
        model = self.meta_not_pathlike_table_model
        if kw == '':
            return -1 
        if kw != self._last_kw:
            # When the user changes the key word, we need to rebuild 
            # the generator and search from the beggining of the table.
            self._last_kw = kw 
            self._result_generator = model.matchIndexGenerator(kw)
        if self._result_generator is None:
            return -2 
        try:
            index = next(self._result_generator)
            self.search_result_found.emit()
            self.ui.treeView_meta_not_pathlike.setCurrentIndex(index)
            return 0 
        except StopIteration:
            self._last_kw = ''
            return -3



# class WidgetMetaViewerBaseNotPathlike(QWidget):
#     """
#     查看非路径形式的元数据的基类。

#     The base widget to view metadata whose keys are not path-like.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self.ui = uiWidgetMetaViewerBaseNotPathlike.Ui_Form()
#         self.ui.setupUi(self)
#         self._item_path = ''
#         self.search_toolbar = QToolBar()    # It will not show .
#         # self._initSearch()
#         # self._initRefresh()
#         # self._meta_manager = None 

#     @property
#     def meta_manager(self) -> MetaManager:
#         global qApp 
#         return qApp.requireMetaManager(self.item_path)
    
#     @property
#     def item_path(self) -> str:
#         return self._item_path 
    
#     @property
#     def meta_tree(self) -> MetaTree:
#         return self.meta_manager.meta_tree 
    
#     @property
#     def meta_not_pathlike_table_model(self) -> MetaNotPathLikeTableModel:
#         return self.meta_manager.meta_not_pathlike_table_model 

#     @property
#     def hdf_handler(self) -> HDFHandler:
#         global qApp 
#         return qApp.hdf_handler 
    
#     def _initMetaNotPathLikeTableView(self):
#         """
#         Initialize meta not path-like table model.
#         """
#         self.ui.tableView_meta_not_pathlike.setModel(self.meta_not_pathlike_table_model)
#         header = self.ui.tableView_meta_not_pathlike.horizontalHeader()
#         header.setSectionResizeMode(0, QHeaderView.ResizeToContents)

#     # def _initMetaManager()
#     def setItemPath(self, item_path: str):
#         """
#         Initialize the meta manager according to the path of the item.

#         arguments:
#             item_path: (str) the path of hte dataset or group.
#         """
#         self._item_path = item_path 

#     def initMetaViewer(self, item_path: str):
#         """
#         Initialize the meta viewer according to the path of the item.

#         arguments:
#             item_path: (str) the path of hte dataset or group.
#         """
#         self.setItemPath(item_path)
#         self._initMetaNotPathLikeTableView()

#     def _initRefresh(self):
#         """
#         Initialize refresh action.
#         """
#         self._action_refresh = ActionRefreshMetaNotPathlikeModel(self.search_toolbar)
#         self._action_refresh = setLinkedTreeView(self.ui.tableView_meta_not_pathlike)
#         self.search_toolbar.addAction(self._action_refresh)

#     def _initSearch(self):
#         """
#         Initialize search lineEdit and action.
#         """
#         self._lineEdit_search = QLineEdit('', parent = self)
#         self._action_search = ActionSearch(self.search_toolbar)
#         self._action_search.setLinkedTreeView(self.ui.tableView_meta_not_pathlike)
#         self._lineEdit_search.addAction(
#             self._action_search, 
#             QLineEdit.LeadingPosition
#         )
#         self.search_toolbar.addWidget(self._lineEdit_search)

#     def _updateModel(self):
#         """
#         Update to the newest model when it is changed.
#         """
#         self._initMetaNotPathLikeTableView()
        

# # class 

