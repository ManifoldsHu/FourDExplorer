# -*- coding: utf-8 -*-

'''
*------------------------- WidgetBaseHDFViewer.py ----------------------------*
对 HDF5 文件内部的层次结构进行显示的模块。使用时，在 UI 中可以直接添加 Widget，然后
将其提升为 WidgetBaseHDFViewer。

4D-Explorer 软件默认使用 HDF5 进行四维数据及其元数据的管理。其数据的组织方式类似于
Unix 目录。为此，我们使用 Qt 的 QTreeView 对这些四维数据进行管理。

作者：          胡一鸣
创建时间：      2022年2月18日
*------------------------- WidgetBaseHDFViewer.py ----------------------------*

'''

import sys
import os
import configparser

from PySide6.QtCore import QModelIndex, Qt, QAbstractItemModel, QPoint
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QMenu, QWidget
from PySide6.QtGui import QRegularExpressionValidator


from ui import uiWidgetBaseHDFViewer
from bin.HDFManager import HDFHandler, HDFTreeModel
from bin.Log import LogUtil

from Constants import HDFType
# from app import ROOTPATH

# import h5py
# from collections.abc import Mapping
# from qt_material import apply_stylesheet


class WidgetBaseHDFViewer(QWidget):
    """
        用于显示 HDF5 文件结构的基础组件，包含一个 QTreeView。 
    """
    def __init__(self, parent: QWidget):
        """
        arguments:
            parent: (QWidget) The parent widget e.g. a dialog.
        """
        super().__init__(parent)

        self.ui = uiWidgetBaseHDFViewer.Ui_Form()
        self.ui.setupUi(self)

        self._is_read_only = False

        global qApp     # QApplication instance
        self._hdf_handler = qApp.hdf_handler
        self._hdf_handler.file_state_changed.connect(
            self.changeStateByFileState)

        self.ui.pushButton_check_attr.setEnabled(
            self._hdf_handler.isFileOpened()
        )
        self.ui.pushButton_refresh.setEnabled(
            self._hdf_handler.isFileOpened()
        )
        self.ui.pushButton_search.setEnabled(
            self._hdf_handler.isFileOpened()
        )
        
        self.ui.pushButton_refresh.clicked.connect(self.refresh)
        self.ui.pushButton_check_attr.clicked.connect(self.checkAttr)
        self.ui.pushButton_search.clicked.connect(self.search)

        self.ui.treeView_HDF.setModel(self._hdf_handler.model)
        self.ui.treeView_HDF.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeView_HDF.customContextMenuRequested.connect(self.showMenu)

    @property
    def hdf_handler(self):
        return self._hdf_handler

    def changeStateByFileState(self):
        """
        Reactions (Slot) of file widgets if the file state is changed 
        (opened or close).
        """
        self.ui.pushButton_check_attr.setEnabled(
            self._hdf_handler.isFileOpened()
        )
        self.ui.pushButton_refresh.setEnabled(
            self._hdf_handler.isFileOpened()
        )
        self.ui.pushButton_search.setEnabled(
            self._hdf_handler.isFileOpened()
        )
        self.refresh()


    def refresh(self):
        """
        Will rebuild the HDFTree and then create a new model.
        """
        self._hdf_handler.buildHDFTree()
        self._hdf_handler._createModel()
        self.ui.treeView_HDF.setModel(self._hdf_handler.model)
        
        
    def search(self):
        pass

    def checkAttr(self):
        pass

    def showMenu(self, pos: QPoint):
        """
        在 HDF5 树中显示鼠标右键菜单。

        Show Context Menu in the treeview of HDF5.

        attributes:
            pos: (QPoint) the position where the mouse is clicked.
        """
        if self.isReadOnly():
            return None
        elif not self.hdf_handler.isFileOpened():
            self._showFileNotOpenContextMenu(pos)
        else:
            index = self.ui.treeView_HDF.currentIndex()
            chosen_type = index.data(
                role = HDFTreeModel.DataRoles.HDFTypeRole
            )
            if chosen_type == HDFType.Root:
                self._showRootMenu(pos, index)
            elif chosen_type == HDFType.Group:
                self._showGroupMenu(pos, index)
            elif chosen_type == HDFType.FourDSTEM:
                self._showFourDSTEMMenu(pos, index)
            elif chosen_type == HDFType.Image:
                self._showImageMenu(pos, index)
            elif chosen_type == HDFType.Data:
                self._showDataMenu(pos, index)
            else:
                self._showItemMenu(pos, index)
            
    def setReadOnly(self, is_read_only: bool):
        """
        Set the viewer read-only.

        If the viewer is read-only, the context menu is forbidden, and only bu-
        ttons like refreshing, checking attribution and searching are allowed.

        attributes:
            is_read_only: (bool)
        """
        if not isinstance(is_read_only, bool):
            raise TypeError(('is_read_only must be bool, not '
                '{0}'.format(type(is_read_only).__name__)))
        self._is_read_only = is_read_only
        
    def isReadOnly(self) -> bool:
        """
        return if the viewer is read-only.
        """
        return self._is_read_only

    def _showRootMenu(self, pos: QPoint, index: QModelIndex = None):
        """
        Shows root menu and connect its actions.

        arguments:
            pos: (QPoint) the location where mouse is clicked

            index: (QModelIndex) the current index
        """
        menu = HDFRootMenu(self)
        menu.action_attributes.connect()

# class HDFReadOnlyMenu(QMenu):
#     """
#     当点到 HDFTreeView 时的鼠标右键菜单。

#     允许对 Item 进行只读操作。除了主窗口处的 Viewer 以外，建议都使用这个右键菜单。

#     The context menu of HDF tree view.

#     This includes read-only operations of items. It is recommended to use this
#     context menu for viewers, except the viewer in the main window.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self.action_refresh = self.addAction('Refresh')
        
class HDFBaseItemMenu(QMenu):
    """
    当点到 HDFTreeView 时的鼠标右键菜单。

    允许对 Item 进行修改操作。在使用时请根据取到的 QModelIndex 选择其合适的子类。

    The context menu of HDF tree view.

    Allowing modification operations of items. Use its subclass according to
    the current QModelIndex.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

    def addModifyActions(self):
        """
        Add move, copy, delete, rename actions.
        """
        self.addSeparator()
        act_str_list = [action.text() for action in self.actions()]
        if not 'Move' in act_str_list:
            self.action_move = self.addAction('Move')
        if not 'Copy' in act_str_list:
            self.action_copy = self.addAction('Copy')
        if not 'Delete' in act_str_list:
            self.action_delete = self.addAction('Delete')
        if not 'Rename' in act_str_list:
            self.action_rename = self.addAction('Rename')
    
    def addAtributeActions(self):
        """
        Add check attribute actions
        """
        self.addSeparator()
        act_str_list = [action.text() for action in self.actions()]
        if not 'Attributes' in act_str_list:
            self.action_attributes = self.addAction('Attributes')

class HDFItemMenu(HDFBaseItemMenu):
    """
    当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Item。

    The context menu of HDF tree view when current index is item.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.addModifyActions()
        self.addAtributeActions()


class HDFRootMenu(HDFBaseItemMenu):
    """
    当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Root。

    The context menu of HDF tree view when current index is root.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.addAtributeActions()

class HDFGroupMenu(HDFBaseItemMenu):
    """
    当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Group。

    The context menu of HDF tree view when current index is group.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.action_create = self.addAction('Create')
        self.addModifyActions()
        self.addAtributeActions()

class HDFDataMenu(HDFBaseItemMenu):
    """
    当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Data。

    The context menu of HDF tree view when current index is data.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.action_show = self.addAction('Show')
        self.action_change_type = self.addAction('Change Type')
        self.addModifyActions()
        self.addAtributeActions()
        
class HDFLineMenu(HDFBaseItemMenu):
    """
    当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Line。

    The context menu of HDF tree view when current index is line.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.action_show = self.addAction('Show')
        self.action_change_type = self.addAction('Change Type')
        self.addModifyActions()
        self.addAtributeActions()


class HDFImageMenu(HDFBaseItemMenu):
    """
    当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Image。

    The context menu of HDF tree view when current index is image.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.action_show = self.addAction('Show')
        self.action_change_type = self.addAction('Change Type')
        self.addModifyActions()
        self.addAtributeActions()


class HDFVectorFieldMenu(HDFBaseItemMenu):
    """
    当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Vector Field。

    The context menu of HDF tree view when current index is vector field.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.action_show = self.addAction('Show')
        self.action_change_type = self.addAction('Change Type')
        self.addModifyActions()
        self.addAtributeActions()


class HDFFourDSTEMMenu(HDFBaseItemMenu):
    """
    当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 4D-STEM 数据集。

    The context menu of HDF tree view when current index is 4D-STEM datacube.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.action_show = self.addAction('Show')
        self.action_change_type = self.addAction('Change Type')
        self.addSeparator()
        self.action_calibrate = self.addAction('Calibrate')
        self.action_reconstruct = self.addAction('Reconstruct')
        self.addModifyActions()
        self.addAtributeActions()
