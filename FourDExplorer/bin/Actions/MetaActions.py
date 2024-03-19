# -*- coding: utf-8 -*- 

"""
*---------------------------- MetaActions.py ---------------------------------*
针对 Metadata 的各种操作的 Action。

作者:           胡一鸣
创建日期:       2024年1月22日

This module includes actions towards Metadata Trees.

author:         Hu Yiming 
date:           Jan 22, 2024
*---------------------------- MetaActions.py ---------------------------------*
"""

from logging import Logger 

from PySide6.QtCore import QObject 
from PySide6.QtCore import QModelIndex 
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QInputDialog
from PySide6.QtWidgets import QTreeView
from PySide6.QtWidgets import QTableView
from PySide6.QtGui import QAction 

# from Constants import ItemDataRoles 
from Constants import MetaDataRoles

from bin.HDFManager import HDFHandler 
from bin.MetaManager import MetaManager 
from bin.MetaManager import MetaTreeModel
from bin.UIManager import ThemeHandler
from bin.Widgets.DialogEditMeta import DialogEditMeta 



def failLogging(func):
    """
    Try to do something. If failed, log it.

    This is a decorator, used for these actions on-triggered functions.
    """
    def wrapper(self: ActionMetaBase, *args, **kw):
        try:
            func(*args, **kw)
        except Exception as e:
            self.logger.error('{0}'.format(e), exc_info = True)
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('An exception happened in '
                '{0}: {1}'.format(self.text(), e))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
    return wrapper 


class ActionMetaBase(QAction):
    """
    关于 Metadata 的 Action 的基类。

    The base class of actions for 
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._key = ''
        self._item_path = ''
        self.setEnabled(self.hdf_handler.isFileOpened())
        self.hdf_handler.file_opened.connect(self._onFileOpened)
        self.hdf_handler.file_closed.connect(self._onFileClosed)

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler
    
    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger 
    
    @property
    def item_path(self) -> str:
        return self._item_path 
    
    @property
    def key(self) -> str:
        return self._key 
    
    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler

    def _onFileOpened(self):
        """
        When file is opened, this action should be enabled.
        """
        self.setEnabled(True)

    def _onFileClosed(self):
        """
        When file is closed, this action should be disabled.
        """
        self.setEnabled(False)

    def setKeyFromIndex(self, index: QModelIndex):
        """
        Set the target item path from its model index.

        arguments:
            index: (QModelIndex)
        """
        if not isinstance(index, QModelIndex):
            raise TypeError(f'index must be a QModelIndex, not {type(index).__name__}')
        _key = index.data(MetaDataRoles.KeyRole)
        if _key is not None:
            self._key = _key
        else:
            self._key = '' 

    def setItemPath(self, path: str):
        """
        Set the item path (hdf path) whose metadata will be edited.

        arguments:
            path: (str) group or dataset's path 
        """
        if not isinstance(path, str):
            raise TypeError('path must be a str, not '
                '{0}'.format(type(path).__name__))
        self._item_path = path 

    def setKey(self, key: str):
        """
        Set the key of the metadata.

        arguments:
            key: (str) the key of the metadata 
        """
        if not isinstance(key, str):
            raise TypeError(f'key must be a str, not {type(key).__name__}')
        self._key = key 

    
class ActionEditMeta(ActionMetaBase):
    """
    编辑一般 Meta 的 Action。

    Action to edit metadata.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Edit')
        # self._table_view = None 
        self._treeview = None 
        self.triggered.connect(lambda: self.editMeta())

    # def setLinkedMetaTableView(self, table_view: QTableView):
    #     """
    #     Set the linked table view for metadata, such that it can show the result.

    #     arguments:
    #         table_view: (QTableView) The table view where this action works.
    #     """
    #     if not isinstance(table_view, QTableView):
    #         raise TypeError(f"table_view must be a QTableView, not 
    #                         {type(table_view).__name__}")
    #     self._table_view = table_view   
        
    @property
    def meta_manager(self) -> MetaManager:
        model: MetaTreeModel = self._treeview.model()
        return model.meta_manager

    def setLinkedTreeView(self, treeview: QTreeView):
        """
        Set the linked tree view for metadata, such that it can initialize itself.

        arguments:
            treeview: (QTreeView) The tree view where this action works.
        """
        self._treeview = treeview 


    def editMeta(self):
        """
        Open a dialog to edit metadata.
        """
        # if self._table_view is not None:
        #     self.setKeyFromIndex(self._table_view.currentIndex())

        # dialog_edit = DialogEditMeta()# TODO
        if self._treeview is not None:
            self.setKeyFromIndex(self._treeview.currentIndex())
            global qApp
            dialog_edit = DialogEditMeta(qApp.main_window)
            dialog_edit.setItemPath(self.item_path)
            dialog_edit.setMetaKey(self.key)
            dialog_edit.setMetaManager(self.meta_manager)
            dialog_edit.readMetaFromFile()
            dialog_edit.show()

    # def setMetaManager(self, meta_manager: MetaManager):
    #     """
    #     Set the meta manager that manages this item.

    #     arguments:
    #         meta_manager: (MetaManager)
    #     """
    #     self._meta_manager = meta_manager
