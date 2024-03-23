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
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtWidgets import QWidget 
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QAction 

# from Constants import ItemDataRoles 
from Constants import MetaDataRoles

from bin.HDFManager import HDFHandler 
from bin.MetaManager import MetaManager 
from bin.MetaManager import MetaTreeModel
from bin.UIManager import ThemeHandler
from bin.Widgets.DialogEditMeta import DialogEditMeta 
from bin.Widgets.DialogAddMeta import DialogAddMeta
# from bin.Widgets.DialogDeleteMeta import DialogDeleteMeta



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
        # self._treeview = None 
        # self._tableview_not_pathlike = None 
        # self._activate_view = None 
        self._widget_viewer_base = None 
        self._widget_viewer_base_not_pathlike = None 
        self._active_widget_viewer = None 
        self.setEnabled(self.hdf_handler.isFileOpened())
        self.hdf_handler.file_opened.connect(self._onFileOpened)
        self.hdf_handler.file_closed.connect(self._onFileClosed)
        self.theme_handler.theme_changed.connect(
            self._updateIcon
        )

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
    
    @property
    def meta_manager(self) -> MetaManager:
        global qApp 
        return qApp.requireMetaManager(self.item_path)
    
    @property
    def treeview(self) -> QTreeView:
        # return self._treeview 
        if self._widget_viewer_base:
            return self._widget_viewer_base.ui.treeView_meta
        else:
            return None 
    
    @property 
    def treeview_not_pathlike(self) -> QTableView:
        # return self._tableview_not_pathlike
        if self._widget_viewer_base_not_pathlike:
            return self._widget_viewer_base_not_pathlike.ui.treeView_meta_not_pathlike
        else:
            return None 
    
    @property
    def active_view(self) -> QAbstractItemView:
        if self._widget_viewer_base or self._widget_viewer_base_not_pathlike:
            if self._active_widget_viewer is self._widget_viewer_base:
                return self.treeview
            elif self._active_widget_viewer is self._widget_viewer_base_not_pathlike:
                return self.treeview_not_pathlike
        else:
            return None 


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
            path: (str) Group or dataset's path 
        """
        if not isinstance(path, str):
            raise TypeError('path must be a str, not '
                '{0}'.format(type(path).__name__))
        self._item_path = path 

    def setKey(self, key: str):
        """
        Set the key of the metadata.

        arguments:
            key: (str) The key of the metadata 
        """
        if not isinstance(key, str):
            raise TypeError(f'key must be a str, not {type(key).__name__}')
        self._key = key 

    # def setTreeView(self, treeview: QTreeView):
    #     """
    #     Set the linked QTreeView that displays metadata whose keys are 
    #     path-like.

    #     arguments:
    #         treeview: (QTreeView)
    #     """
    #     self._treeview = treeview 

    # def setTableViewNotPathlike(self, tableview_not_pathlike: QTableView):
    #     """
    #     Set the linked QTableView that displays metadata whose keys are 
    #     not path-like.

    #     arguments:
    #         tableview: (QTableView)
    #     """
    #     self._tableview_not_pathlike = tableview_not_pathlike

    # def setActivateView(self, activate_view: QAbstractItemView):
    #     """
    #     Set the activated view that this action will read from.

    #     argumnets:
    #         activate_view: (QTableView|QTreeView)
    #     """
    #     self._activate_view = activate_view
        
    def setWidgetViewerBase(self, widget_viewer_base: QWidget):
        """
        Set the linked WidgetMetaViewerBase that displays metadata whose keys 
        are path-like.

        arguments:
            widget_viewer_base: (QWidget) The WidgetMetaViewerBase instance
        """
        self._widget_viewer_base = widget_viewer_base

    def setWidgetViewerBaseNotPathlike(self, widget_viewer_base_not_pathlike: QWidget):
        """
        Set the linked WidgetMetaViewerBaseNotPathlike that displays metadata 
        whose keys are not path-like.

        arguments:
            widget_viewer_base_not_pathlike: (QWidget) The 
                WidgetMetaViewerBaseNotPathlike instance
        """
        self._widget_viewer_base_not_pathlike = widget_viewer_base_not_pathlike

    def setActiveWidgetViewer(self, active_widget_viewer: QWidget):
        """
        Set the active widget viewer that this action will read from.

        arguments:
            active_widget_viewer: (QWidget) Must be one of the widget_viewer_base 
                or widget_viewer_base_not_pathlike
        """
        self._active_widget_viewer = active_widget_viewer

    def initIconResources(self, icon_name: str):
        """
        Initialize the resource of icons.

        arguments:
            icon_name: (str) the name of icon.
        """
        _path = ':/HDFEdit/resources/icons/' + icon_name
        icon = self.theme_handler.iconProvider(_path)
        self._icon_name = icon_name 
        self.setIcon(icon)

    def _updateIcon(self):
        """
        Will update the icon when the theme mode changes.
        """
        if self._icon_name:
            _path = ':/HDFEdit/resources/icons/' + self._icon_name
            icon = self.theme_handler.iconProvider(_path)
            self.setIcon(icon)


class ActionEditMeta(ActionMetaBase):
    """
    编辑一般 Metadata 的 Action。

    Action to edit metadata.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Edit')
        self.initIconResources('edit')
        self.triggered.connect(self.editMeta)

    def initialize(
        self, 
        item_path: str, 
        meta_key: str = None,
        widget_viewer: QWidget = None,
        widget_viewer_not_path_like: QWidget = None,
        active_widget_viewer: QWidget = None, 
    ):
        """
        Initialize the action with necessary parameters.

        meta_key or activate_view should at least be given one.

        arguments:
            item_path: (str) The path of the dataset or group

            meta_key: (str) The key of the metadata ot be edited

            widget_viewer: (QWidget) The linked WidgetMetaViewerBase object
            
            widget_viewer_not_path_like: (QWidget) The linked 
                WidgetMetaViewerBaseNotPathlike object

            active_widget_viewer: (QWidget) The linked active view, of which 
                this action will be created in the menu.
        """
        if item_path:
            self.setItemPath(item_path)
        if meta_key:
            self.setKey(meta_key)
        if widget_viewer:
            self.setWidgetViewerBase(widget_viewer)
        if widget_viewer_not_path_like:
            self.setWidgetViewerBaseNotPathlike(widget_viewer_not_path_like)
        if active_widget_viewer:
            self.setActiveWidgetViewer(active_widget_viewer)

    def editMeta(self):
        """
        Open a dialog to edit metadata.
        """
        if self._active_widget_viewer is not None:
            self.setKeyFromIndex(self.active_view.currentIndex())
        global qApp 
        dialog_edit = DialogEditMeta(qApp.main_window)
        dialog_edit.setItemPath(self.item_path)
        dialog_edit.setMetaKey(self.key)
        dialog_edit.readMetaFromFile()
        dialog_edit.show()
            
        # if self._table_view is not None:
        #     self.setKeyFromIndex(self._table_view.currentIndex())

        # dialog_edit = DialogEditMeta()# TODO
        # if self._treeview is not None:
        #     self.setKeyFromIndex(self._treeview.currentIndex())
        #     global qApp
        #     dialog_edit = DialogEditMeta(qApp.main_window)
        #     dialog_edit.setItemPath(self.item_path)
        #     dialog_edit.setMetaKey(self.key)
        #     # dialog_edit.setMetaManager(self.meta_manager)
        #     dialog_edit.readMetaFromFile()
        #     dialog_edit.show()
            

class ActionAddMeta(ActionMetaBase):
    """
    添加一般 Metadata 的 Action

    Action to add metadata.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Add')
        self.initIconResources('file_add')
        self.triggered.connect(self.addMeta)

    def initialize(self, item_path: str):
        """
        Initialize the action with necessary parameters.

        arguments:
            item_path: (str) The path of the dataset or group
        """
        self.setItemPath(item_path)

    def addMeta(self):
        """
        Open a dialog to add metadata.
        """
        dialog_edit = DialogAddMeta(qApp.main_window)
        dialog_edit.setItemPath(self.item_path)
        dialog_edit.setMetaKey('')
        dialog_edit.show()  # TODO dialog_edit raise exception when there exists metadata.


class ActionDeleteMeta(ActionMetaBase):
    """
    删除一般 Metadata 的 Action

    Action to delete metadata.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Delete')
        self.initIconResources('file_delete')
        self.triggered.connect(self.deleteMeta)

    def initialize(
        self, 
        item_path: str, 
        meta_key: str = None,
        widget_viewer: QWidget = None,
        widget_viewer_not_path_like: QWidget = None,
        active_widget_viewer: QWidget = None, 
    ):
        """
        Initialize the action with necessary parameters.

        meta_key or activate_view should at least be given one.

        arguments:
            item_path: (str) The path of the dataset or group

            meta_key: (str) The key of the metadata ot be edited

            widget_viewer: (QWidget) The linked WidgetMetaViewerBase object
            
            widget_viewer_not_path_like: (QWidget) The linked 
                WidgetMetaViewerBaseNotPathlike object

            active_widget_viewer: (QWidget) The linked active view, of which 
                this action will be created in the menu.
        """
        if item_path:
            self.setItemPath(item_path)
        if meta_key:
            self.setKey(meta_key)
        if widget_viewer:
            self.setWidgetViewerBase(widget_viewer)
        if widget_viewer_not_path_like:
            self.setWidgetViewerBaseNotPathlike(widget_viewer_not_path_like)
        if active_widget_viewer:
            self.setActiveWidgetViewer(active_widget_viewer)

    def deleteMeta(self):
        """
        Open a dialog to delete metadata.
        """
        if self._active_widget_viewer is not None:
            self.setKeyFromIndex(self.active_view.currentIndex())
        # dialog_delete = DialogDeleteMeta(qApp.main_window)
        # dialog_delete.setItemPath(self.item_path)
        # dialog_delete.setMetaKey(self.key)
        # dialog_delete.show()
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirm Deletion")
        msg_box.setText(
            f"Are you sure to delete metadata <code>{self.key}</code> from item (Dataset or Group) <code>{self.item_path}</code>?"
        )
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        response = msg_box.exec()
        if response == QMessageBox.Yes:
            del self.hdf_handler.file[self.item_path].attrs[self.key]
            self.meta_manager.refreshModel()
        return 

    
class ActionRefreshMeta(ActionMetaBase):
    """
    刷新 Metadata 的 Action

    Action to refresh metadata.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Refresh')
        self.initIconResources('refresh.png')
        self.triggered.connect(self.refreshMeta)

    def initialize(
        self, 
        widget_viewer_base: QWidget = None, 
        widget_viewer_base_not_pathlike: QWidget = None,
    ):
        """
        Initialize the action with necessary parameters.

        arguments:
            widget_viewer_base: (QWidget) The WidgetMetaViewerBase instance

            widget_viewer_base_not_pathlike: (QWidget) The 
                WidgetMetaViewerBaseNotPathlike instance
        """
        self._widget_viewer_base = widget_viewer_base
        self._widget_viewer_base_not_pathlike = widget_viewer_base_not_pathlike

    def refreshMeta(self):
        """
        Refresh the treeview and the tableview.
        """
        if self._widget_viewer_base is not None:
            self._widget_viewer_base.refreshModel()
        if self._widget_viewer_base_not_pathlike is not None:
            self._widget_viewer_base_not_pathlike.refreshModel()

class ActionSearchMeta(ActionMetaBase):
    """
    搜索 Metadata 的 Action

    Action to search metadata.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Search')
        self.initIconResources('search.png')
        self._linked_line_edit = None 
        # self._kw = ''
        self.triggered.connect(self.searchMeta)

    @property
    def kw(self) -> str:
        return self._linked_line_edit.text()

    def initialize(
        self,
        linked_line_edit: QLineEdit = None,
        widget_viewer_base: QWidget = None,
        widget_viewer_base_not_pathlike: QWidget = None,
    ):
        """
        Initialize the action with necessary parameters.

        arguments:
            kw: (str) The keyword to be searched

            widget_viewer_base: (QWidget) The WidgetMetaViewerBase instance

            widget_viewer_base_not_pathlike: (QWidget) The 
                WidgetMetaViewerBaseNotPathlike instance
        """
        # if kw:
        #     self._kw = kw 
        if linked_line_edit:
            self._linked_line_edit = linked_line_edit
        if widget_viewer_base:
            self._widget_viewer_base = widget_viewer_base 
        if widget_viewer_base_not_pathlike:
            self._widget_viewer_base_not_pathlike = widget_viewer_base_not_pathlike

    # def setKeyWord(self, kw: str):
    #     """
    #     Set the key word to be searched.

    #     arguments:
    #         kw: (str) The keyword to be searched
    #     """
    #     self._kw = kw 


    def searchMeta(self):
        """
        Search the metadata that includes keyword.
        """
        # if self._widget_viewer_base and self._widget_viewer_base_not_pathlike:
        #     ret1 = self._widget_viewer_base.searchItem(self._kw)
        #     if ret1 == 0:       # A result is found 
        #         return 
        #     elif ret1 == -1:    # kw is empty 
        #         return 
        #     elif ret1 == -2:
        #         raise RuntimeError("No valid result generator within tree model.")
        #     elif ret1 == -3:
        #         pass 
        #     ret2 = self._widget_viewer_base_not_pathlike.searchItem(self._kw)
        #     if ret2 == 0:       # A result is found 
        #         return 
        #     elif ret2 == -1:    # kw is empty 
        #         return 
        #     elif ret2 == -2:
        #         raise RuntimeError("No valid result generator within table model.")
        #     elif ret2 == -3:    # no result is found
        #         msg = QMessageBox()
        #         msg.setWindowTitle('Search')
        #         msg.setIcon(QMessageBox.Information)
        #         msg.setText('No more results.')
        #         msg.setStandardButtons(QMessageBox.Ok)
        #         msg.exec()
        #         return 

        if self._widget_viewer_base:
            ret1 = self._widget_viewer_base.searchItem(self.kw)
            if ret1 == 0:
                return 
            elif ret1 == -1:
                return 
            elif ret1 == -2:
                raise RuntimeError("No valid result generator within tree model.")
            elif ret1 == -3:
                if not self._widget_viewer_base_not_pathlike:
                    msg = QMessageBox()
                    msg.setWindowTitle('Search')
                    msg.setIcon(QMessageBox.Information)
                    msg.setText('No more results.')
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec()
                    return 

        if self._widget_viewer_base_not_pathlike:
            ret2 = self._widget_viewer_base_not_pathlike.searchItem(self.kw)
            if ret2 == 0:
                return 
            elif ret2 == -1:
                return 
            elif ret2 == -2:
                raise RuntimeError("No valid result generator within table model.")
            elif ret2 == -3:
                msg = QMessageBox()
                msg.setWindowTitle('Search')
                msg.setIcon(QMessageBox.Information)
                msg.setText('No more results.')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return 

        

    
# class ActionEditMeta(ActionMetaBase):
#     """
#     编辑一般 Meta 的 Action。

#     Action to edit metadata.
#     """
#     def __init__(self, parent: QObject = None):
#         super().__init__(parent)
#         self.setText('Edit')
#         # self._table_view = None 
#         self._treeview = None 
#         self.triggered.connect(lambda: self.editMeta())

#     # def setLinkedMetaTableView(self, table_view: QTableView):
#     #     """
#     #     Set the linked table view for metadata, such that it can show the result.

#     #     arguments:
#     #         table_view: (QTableView) The table view where this action works.
#     #     """
#     #     if not isinstance(table_view, QTableView):
#     #         raise TypeError(f"table_view must be a QTableView, not 
#     #                         {type(table_view).__name__}")
#     #     self._table_view = table_view   
        
#     # @property
#     # def meta_manager(self) -> MetaManager:
#     #     model: MetaTreeModel = self._treeview.model()
#     #     return model.meta_manager

#     def setLinkedTreeView(self, treeview: QTreeView):
#         """
#         Set the linked tree view for metadata, such that it can initialize itself.

#         arguments:
#             treeview: (QTreeView) The tree view where this action works.
#         """
#         self._treeview = treeview 


#     def editMeta(self):
#         """
#         Open a dialog to edit metadata.
#         """
#         # if self._table_view is not None:
#         #     self.setKeyFromIndex(self._table_view.currentIndex())

#         # dialog_edit = DialogEditMeta()# TODO
#         if self._treeview is not None:
#             self.setKeyFromIndex(self._treeview.currentIndex())
#             global qApp
#             dialog_edit = DialogEditMeta(qApp.main_window)
#             dialog_edit.setItemPath(self.item_path)
#             dialog_edit.setMetaKey(self.key)
#             # dialog_edit.setMetaManager(self.meta_manager)
#             dialog_edit.readMetaFromFile()
#             dialog_edit.show()

#     # def setMetaManager(self, meta_manager: MetaManager):
#     #     """
#     #     Set the meta manager that manages this item.

#     #     arguments:
#     #         meta_manager: (MetaManager)
#     #     """
#     #     self._meta_manager = meta_manager
