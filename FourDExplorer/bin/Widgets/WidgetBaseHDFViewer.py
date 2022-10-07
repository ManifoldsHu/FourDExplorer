# -*- coding: utf-8 -*-

"""
*--------------------------- WidgetHDFViewer.py ------------------------------*
对 HDF5 文件内部的层次结构进行显示的模块。

4D-Explorer 软件默认使用 HDF5 进行四维数据及其元数据的管理。其数据的组织方式类似于
Unix 目录。为此，我们使用 Qt 的 QTreeView 对这些四维数据进行管理。

这个 Widget 是用在小窗口的，只具有查找功能。

作者：          胡一鸣
创建时间：      2022年3月2日

The Module to show HDF5 file structure.

4D-Explorer software use HDF5 to manage 4D-STEM data and its metadata. It looks
like Unix file system, so we use QTreeView to show the structures.

This widget is used in the dialogs, and hence has only search method.

author:         Hu Yiming
date:           Mar 2, 2022
*--------------------------- WidgetHDFViewer.py ------------------------------*
"""

from logging import Logger

from PySide6.QtWidgets import QWidget, QMessageBox, QToolBar, QLineEdit, QTreeView, QWidgetAction, QToolButton
from PySide6.QtGui import QAction
from PySide6.QtCore import QObject, QModelIndex, QSize, Qt
# from bin.Actions.EditActions import ActionAttributes, ActionChangeHDFType, ActionCopy, ActionDelete, ActionMove, ActionNew, ActionOpenWith, ActionRefreshModel, ActionSearch
# from bin.Actions.EditActions import ActionSearch, ActionRefreshModel
from bin.HDFManager import HDFHandler, ItemDataRoles
from bin.UIManager import ThemeHandler
from ui import uiWidgetBaseHDFViewer

class WidgetBaseHDFViewer(QWidget):
    """
    查看 HDF5 文件内部结构的基类。
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetBaseHDFViewer.Ui_Form()
        self.ui.setupUi(self)
        self.search_toolbar = HDFToolBar(self)
        self.ui.verticalLayout.insertWidget(0, self.search_toolbar)
        self._initSearch()
        self._initRefresh()
        self.ui.treeView_HDF.setModel(self.hdf_handler.model)
        self.ui.treeView_HDF.setHeaderHidden(True)
        self.hdf_handler.model_created.connect(
            self._updateModel
        )

    @property 
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler

    def _initSearch(self):
        """
        Initialize search lineEdit and action.
        """
        self._lineEdit_search = QLineEdit('', parent = self)
        self._action_search = ActionSearch(self.search_toolbar)
        self._action_search.setLinkedLineEdit(self._lineEdit_search)
        self._action_search.setLinkedTreeView(self.ui.treeView_HDF)
        self._lineEdit_search.addAction(
            self._action_search, 
            QLineEdit.LeadingPosition
        )
        self.search_toolbar.addWidget(self._lineEdit_search)

    def _initRefresh(self):
        """
        Initialize refresh action.
        """
        self._action_refresh = ActionRefreshModel(self.search_toolbar)
        self._action_refresh.setLinkedTreeView(self.ui.treeView_HDF)
        self.search_toolbar.addAction(self._action_refresh)

    def _updateModel(self):
        """
        Update to the newest model when it is changed.
        """
        self.ui.treeView_HDF.setModel(self.hdf_handler.model)
        self.ui.treeView_HDF.expandToDepth(0)

class HDFToolBar(QToolBar):
    """
    The toolbar to search items in HDF tree.
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

        # self.setStyleSheet(
        #     "HDFToolBar{                    "
        #     "    border: none;              "
        #     "    padding: 0px;              "
        #     "}                              "
        #     "HDFToolBar::separator{         "
        #     "   width: 0px;                 "
        #     "}                              "
        #     "HDFToolBar QToolButton{        "
        #     "   padding: 0;                 "
        #     "   margin: 0px;                "
        #     "   height: 35px;               "
        #     "   width: 15px;                "
        #     "}                              "
        # )
        


class ActionViewItemBase(QAction):
    """
    用于查看 HDF 中 Item 的 Action 的基类。

    The base action for viewing items in HDF file.
    """
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self._item_path = ''
        self._icon_name = ''
        self.theme_handler.theme_changed.connect(
            self._updateIcon
        )
        self.hdf_handler.file_opened.connect(
            lambda: self.setEnabled(True)
        )
        self.hdf_handler.file_closed.connect(
            lambda: self.setEnabled(False)
        )
        self._treeview = None 

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler 

    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp
        return qApp.theme_handler 

    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger

    @property
    def item_path(self) -> str:
        return self._item_path 

    @property
    def item_index(self) -> QModelIndex:
        return self.hdf_handler.model.indexFromPath(self.item_path)

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
        

    def setItemPath(self, path: str):
        """
        Set the target item path.

        arguments:
            path: (str)
        """
        if not isinstance(path, str):
            raise TypeError('path must be a str, not '
                '{0}'.format(type(path).__name__))
        self._item_path = path

    def setItemPathFromIndex(self, index: QModelIndex):
        """
        Set the target item path from its model index.

        arguments:
            index: QModelIndex
        """
        if not isinstance(index, QModelIndex):
            raise TypeError('index must be a QModelIndex, not '
                '{0}'.format(type(index).__name__))
        _path = index.data(ItemDataRoles.PathRole)
        if _path is not None:
            self._item_path = _path
        else:
            self._item_path = ''

    def _updateIcon(self):
        """
        Will update the icon when the theme mode changes.
        """
        if self._icon_name:
            _path = ':/HDFEdit/resources/icons/' + self._icon_name
            icon = self.theme_handler.iconProvider(_path)
            self.setIcon(icon)

    def setLinkedTreeView(self, treeview: QTreeView):
        """
        Set the linked treeview, so that it can show the result.
        """
        if not isinstance(treeview, QTreeView):
            raise TypeError('treeview must be a QTreeView, not '
                '{0}'.format(type(treeview).__name__))
        self._treeview = treeview 


def failLogging(func):
    """
    Try to do something. If failed, log it.

    This is a decorator, used for these actions on-triggered functions.
    """
    def wrapper(self: ActionViewItemBase, *args, **kw):
        try:
            func(*args, **kw)
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('An exception happened in '
                '{0}: {1}'.format(self.text(), e))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
    return wrapper 


class ActionRefreshModel(ActionViewItemBase):
    """
    用于刷新文件列表的 Action。

    Action to refresh HDF items.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Refresh')
        self.initIconResources('refresh.png')
        self.triggered.connect(lambda: self.refreshModel(self))

    @failLogging
    def refreshModel(self):
        """
        Will rebuild the HDFTree and then create a new model.
        """
        if self._treeview is not None:
            self.setItemPathFromIndex(self._treeview.currentIndex())
        self.hdf_handler.buildHDFTree()
        if self._treeview is not None:
            self._treeview.setModel(self.hdf_handler.model)
            _index = self.hdf_handler.model.indexFromPath(self.item_path)
            self._treeview.setCurrentIndex(_index)

class ActionSearch(ActionViewItemBase):
    """
    用于查找下一个匹配的 HDF 对象的 Action。

    Action to search HDF items.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Search')
        self.initIconResources('search.png')
        self.triggered.connect(self.searchItem)
        self._last_kw = ''
        self._result_generator = None

    def setLinkedTreeView(self, treeview: QTreeView):
        """
        Set the linked treeview, so that it can show the result.
        """
        self._treeview = treeview 

    def setLinkedLineEdit(self, line_edit: QLineEdit):
        """
        Set the linked line edit, so that it can get the word to search.
        """
        self._line_edit = line_edit

    def searchItem(self):
        """
        Find the next search result and show it in the treeview.
        """
        kw = self._line_edit.text()
        if kw == '':
            return False 
        if kw != self._last_kw:
            # When the user changes the key word, we need to rebuild the 
            # generator and search from the beginning of the tree.
            self._last_kw = kw 
            model = self._treeview.model()
            self._result_generator = model.matchIndexGenerator(kw)
        if self._result_generator is None:
            return False 
        try:
            index = next(self._result_generator)
            self._treeview.setCurrentIndex(index)
            return True 
        except StopIteration:
            msg = QMessageBox()
            msg.setWindowTitle('Search')
            msg.setIcon(QMessageBox.Information)
            msg.setText('No more results.')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self._last_kw = ''
            return False 


