# -*- coding: utf-8 -*-

"""
*------------------------- WidgetBaseHDFViewer.py ----------------------------*
对 HDF5 文件内部的层次结构进行显示的模块。

4D-Explorer 软件默认使用 HDF5 进行四维数据及其元数据的管理。其数据的组织方式类似于
Unix 目录。为此，我们使用 Qt 的 QTreeView 对这些四维数据进行管理。

这个 Widget 是用在主界面的，具有增删查改的功能。

作者：          胡一鸣
创建时间：      2022年2月18日

The Module to show HDF5 file structure.

4D-Explorer software use HDF5 to manage 4D-STEM data and its metadata. It looks
like Unix file system, so we use QTreeView to show the structures.

This widget is used in the main window, and hence have CRUD methods.

author:         Hu Yiming
date:           Feb 18, 2022
*------------------------- WidgetBaseHDFViewer.py ----------------------------*

"""

from logging import Logger
import sys
import os
import configparser

from PySide6.QtCore import QModelIndex, Qt, QPoint
from PySide6.QtWidgets import QMessageBox, QMenu, QWidget, QInputDialog
# from PySide6.QtGui import QRegularExpressionValidator

from bin.TabViewManager import TabViewManager
from bin.ItemActions import (
    ActionCreate,
    ActionMove,
    ActionRename,
    ActionCopy,
    ActionDelete,
    ActionAttributes,
    ActionChangeDataType,
    ActionShowData,
    ActionShowLine,
    ActionShowImage,
    ActionShowVectorField,
    ActionShowFourDSTEM,
    ActionVirtualImage,
)
from bin.Widgets.DialogAttrViewer import DialogAttrViewer
from bin.Widgets.DialogCreateItem import DialogHDFCreate
from bin.Widgets.DialogMoveItem import DialogHDFMove
from bin.Widgets.DialogCopyItem import DialogHDFCopy
from bin.Widgets.PageViewFourDSTEM import PageViewFourDSTEM
from bin.Widgets.PageViewLine import PageViewLine
from bin.Widgets.WidgetBaseHDFViewer import WidgetBaseHDFViewer
from bin.Widgets.PageViewImage import PageViewImage

from Constants import HDFType, ItemDataRoles

class WidgetHDFViewer(WidgetBaseHDFViewer):
    """
    用于显示 HDF5 文件结构的基础组件，包含一个 QTreeView。 

    Widget to show HDF file structure, which includes a QTreeView.
    """
    def __init__(self, parent: QWidget = None):
        """
        arguments:
            parent: (QWidget) The parent widget e.g. a dialog.
        """
        super().__init__(parent)

        self.ui.treeView_HDF.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeView_HDF.customContextMenuRequested.connect(
            self.showContextMenu
        )

    # @property
    # def tabWidget_view(self) -> QTabWidget:
    #     global qApp
    #     return qApp.tabWidget_view

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    @property
    def tabview_manager(self) -> TabViewManager:
        global qApp
        return qApp.tabview_manager

    def showContextMenu(self, pos: QPoint):
        """
        在 HDF5 树中显示鼠标右键菜单。

        Show Context Menu in the treeview of HDF5.

        attributes:
            pos: (QPoint) the position where the mouse is clicked.
        """
        # if self.isReadOnly():
        #     return None
        if not self.hdf_handler.isFileOpened():
            self._showFileMenu(pos)
        else:
            index = self.ui.treeView_HDF.currentIndex()
            chosen_type = index.data(
                role = ItemDataRoles.HDFTypeRole
            )
            if chosen_type == HDFType.Root:
                menu = HDFRootMenu(self, index)
                # self._showRootMenu(pos, index)
            elif chosen_type == HDFType.Group:
                menu = HDFGroupMenu(self, index)
                # self._showGroupMenu(pos, index)
            elif chosen_type == HDFType.FourDSTEM:
                menu = HDFFourDSTEMMenu(self, index)
                # self._showFourDSTEMMenu(pos, index)
            elif chosen_type == HDFType.Image:
                menu = HDFImageMenu(self, index)
                # self._showImageMenu(pos, index)
            elif chosen_type == HDFType.Data:
                menu = HDFDataMenu(self, index)
                # self._showDataMenu(pos, index)
            else:
                menu = HDFItemMenu(self, index)
                # self._showItemMenu(pos, index)
            menu.exec(self.ui.treeView_HDF.mapToGlobal(pos))

    # def _showRootMenu(self, pos: QPoint, index: QModelIndex = None):
    #     """
    #     Shows root menu and connect its actions.

    #     arguments:
    #         pos: (QPoint) the location where mouse is clicked

    #         index: (QModelIndex) the current index
    #     """
    #     menu = HDFRootMenu(self)
    #     menu.action_create.triggered.connect(
    #         lambda: self.showCreate(index)
    #     )
    #     menu.action_attributes.triggered.connect(
    #         lambda: self.showAttribute(index)
    #     )
    #     menu.exec(self.ui.treeView_HDF.mapToGlobal(pos))
    
    # def _showGroupMenu(self, pos: QPoint, index: QModelIndex = None):
    #     """
    #     Shows group menu and connect its actions.

    #     arguments:
    #         pos: (QPoint) the location where mouse is clicked

    #         index: (QModelIndex) the current index
    #     """
    #     menu = HDFGroupMenu(self)
    #     menu.action_attributes.triggered.connect(
    #         lambda: self.showAttribute(index)
    #     )
    #     menu.action_create.triggered.connect(
    #         lambda: self.showCreate(index)
    #     )
    #     menu.action_delete.triggered.connect(
    #         lambda: self.showDelete(index)
    #     )
    #     menu.action_move.triggered.connect(
    #         lambda: self.showMove(index)
    #     )
    #     menu.action_rename.triggered.connect(
    #         lambda: self.showRename(index)
    #     )
    #     menu.action_copy.triggered.connect(
    #         lambda: self.showCopy(index)
    #     )
    #     menu.exec(self.ui.treeView_HDF.mapToGlobal(pos))

    # def _showDataMenu(self, pos: QPoint, index: QModelIndex = None):
    #     """
    #     Shows data menu and connect its actions.

    #     arguments:
    #         pos: (QPoint) the location where mouse is clicked

    #         index: (QModelIndex) the current index
    #     """
    #     menu = HDFDataMenu(self)
    #     menu.action_attributes.triggered.connect(
    #         lambda: self.showAttribute(index)
    #     )
    #     menu.action_delete.triggered.connect(
    #         lambda: self.showDelete(index)
    #     )
    #     menu.action_move.triggered.connect(
    #         lambda: self.showMove(index)
    #     )
    #     menu.action_rename.triggered.connect(
    #         lambda: self.showRename(index)
    #     )
    #     menu.action_copy.triggered.connect(
    #         lambda: self.showCopy(index)
    #     )
    #     menu.action_show.triggered.connect(
    #         lambda: self.showPlotting(index)
    #     )
    #     menu.action_change_type.triggered.connect(
    #         lambda: self.showChangeDataType(index)
    #     )
    #     menu.exec(self.ui.treeView_HDF.mapToGlobal(pos))

    # def _showFourDSTEMMenu(self, pos: QPoint, index: QModelIndex = None):
    #     """
    #     Shows 4D-STEM menu and connect its actions.

    #     arguments:
    #         pos: (QPoint) the location where mouse is clicked

    #         index: (QModelIndex) the current index
    #     """
    #     menu = HDFFourDSTEMMenu(self)
    #     menu.action_attributes.triggered.connect(
    #         lambda: self.showAttribute(index)
    #     )
    #     menu.action_delete.triggered.connect(
    #         lambda: self.showDelete(index)
    #     )
    #     menu.action_move.triggered.connect(
    #         lambda: self.showMove(index)
    #     )
    #     menu.action_rename.triggered.connect(
    #         lambda: self.showRename(index)
    #     )
    #     menu.action_copy.triggered.connect(
    #         lambda: self.showCopy(index)
    #     )
    #     menu.action_show.triggered.connect(
    #         lambda: self.showPlotting(index)
    #     )
    #     menu.action_change_type.triggered.connect(
    #         lambda: self.showChangeDataType(index)
    #     )
        
    #     # return self._showDataMenu(pos, index)

    # def _showImageMenu(self, pos: QPoint, index: QModelIndex = None):
    #     """
    #     Shows Image menu and connect its actions.

    #     arguments:
    #         pos: (QPoint) the location where mouse is clicked

    #         index: (QModelIndex) the current index
    #     """
    #     return self._showDataMenu(pos, index)

    # def _showItemMenu(self, pos: QPoint, index: QModelIndex = None):
    #     """
    #     Shows general item menu and connect its actions.

    #     arguments:
    #         pos: (QPoint) the location where mouse is clicked

    #         index: (QModelIndex) the current index
    #     """
    #     menu = HDFItemMenu(self)
    #     menu.action_attributes.triggered.connect(
    #         lambda: self.showAttribute(index)
    #     )
    #     menu.action_delete.triggered.connect(
    #         lambda: self.showDelete(index)
    #     )
    #     menu.action_move.triggered.connect(
    #         lambda: self.showMove(index)
    #     )
    #     menu.action_rename.triggered.connect(
    #         lambda: self.showRename(index)
    #     )
    #     menu.action_copy.triggered.connect(
    #         lambda: self.showCopy(index)
    #     )
    #     menu.exec(self.ui.treeView_HDF.mapToGlobal(pos))

    # def _showFileMenu(self, pos: QPoint, index: QModelIndex = None):
    #     """
    #     When file is not opened, will not show menu.
    #     """
    #     return None 

    # def showCreate(self, index: QModelIndex = None):
    #     """
    #     Shows a dialog to create an item.

    #     arguments:
    #         index: (QModelIndex) the current index, used to initialize the 
    #             dialog.
    #     """
    #     dialog_create = DialogHDFCreate(self)
    #     if index:
    #         dialog_create.initNames(
    #             parent_path = index.data(role = ItemDataRoles.PathRole))

    #     dialog_code = dialog_create.exec()
    #     if not dialog_code == dialog_create.Accepted:
    #         return False
        
    #     item_type = dialog_create.getItemType()
    #     parent_path = dialog_create.getParentPath()
    #     name = dialog_create.getName()
    #     model = self.ui.treeView_HDF.model()
    #     parent_index = model.indexFromPath(parent_path)
    #     try:
    #     # if True:
    #         if item_type == HDFType.Group:
    #             model.insertGroup(parent_index, name)
    #             return True
    #         elif item_type == HDFType.Data:
    #             shape = dialog_create.getShape()
    #             dtype = dialog_create.getDType()
    #             model.insertData(
    #                 parent = parent_index, 
    #                 name = name,
    #                 shape = shape,
    #                 dtype = dtype,
    #             )
    #             return True
    #         else:
    #             return False
    #     except (ValueError, KeyError) as e:
    #         msg = QMessageBox(parent = self)
    #         msg.setWindowTitle('Warning')
    #         msg.setIcon(QMessageBox.Warning)
    #         msg.setText('Fail to create: {0}'.format(e))
    #         msg.setStandardButtons(QMessageBox.Ok)
    #         msg.exec()
    #         return False

    # def showDelete(self, index: QModelIndex = None) -> bool:
    #     """
    #     Shows a dialog to delete items.

    #     If the index indicates a group, all of the subitems will be also 
    #     deleted recursively.

    #     arguments:
    #         index: (QModelIndex)
    #     """
    #     if not index:
    #         index = self.ui.treeView_HDF.currentIndex()
    #     dialog_delete = QMessageBox(parent = self)
    #     dialog_delete.setIcon(QMessageBox.Question)
    #     dialog_delete.setWindowTitle('Delete Item')
    #     dialog_delete.setText(
    #         'Do you want to delete the item permanently?\n'
    #         '{0}'.format(index.data(role = ItemDataRoles.PathRole))
    #     )
    #     dialog_delete.setStandardButtons(
    #         QMessageBox.Ok|QMessageBox.Cancel
    #     )
        
        
    #     dialog_code = dialog_delete.exec()
    #     if not dialog_code == QMessageBox.Ok:
    #         return False
        
    #     model = self.ui.treeView_HDF.model()
    #     index = self.ui.treeView_HDF.currentIndex()
    #     try:
    #         model.removeItem(index)
    #         return True
    #     except (ValueError, KeyError) as e:
    #         msg = QMessageBox(parent = self)
    #         msg.setWindowTitle('Warning')
    #         msg.setIcon(QMessageBox.Warning)
    #         msg.setText('Fail to delete: {0}'.format(e))
    #         msg.setStandardButtons(QMessageBox.Ok)
    #         msg.exec()
    
    # def showMove(self, index: QModelIndex = None) -> bool:
    #     """
    #     Shows a dialog to move items.

    #     arguments:
    #         index: (QModelIndex)
    #     """
    #     dialog_move = DialogHDFMove(self)
    #     model = self.ui.treeView_HDF.model()
    #     if not index:
    #         index = self.ui.treeView_HDF.currentIndex()
    #     dialog_move.setItemPath(index.data(role = ItemDataRoles.PathRole))
    #     dialog_code = dialog_move.exec()
    #     if not dialog_code == dialog_move.Accepted:
    #         return False
    #     item_path = dialog_move.getItemPath()
    #     dest_path = dialog_move.getDestPath()
    #     try:
    #         model.moveItem(
    #             child = model.indexFromPath(item_path), 
    #             dest_parent = model.indexFromPath(dest_path),
    #         )
    #     except (KeyError, ValueError) as e:
    #         msg = QMessageBox(parent = self)
    #         msg.setWindowTitle('Warning')
    #         msg.setIcon(QMessageBox.Warning)
    #         msg.setText('Fail to move: {0}'.format(e))
    #         msg.setStandardButtons(QMessageBox.Ok)
    #         msg.exec()
    #         return False
         

    # def showRename(self, index: QModelIndex = None) -> bool:
    #     """
    #     Shows a dialog to rename an item.

    #     arguments:
    #         index: (QModelIndex)
    #     """
    #     if not index:
    #         index = self.ui.treeView_HDF.currentIndex()

    #     rename_dialog = QInputDialog(self)
    #     rename_dialog.setWindowTitle('Rename Item')
    #     rename_dialog.setInputMode(QInputDialog.TextInput)
    #     rename_dialog.setLabelText('Enter a new name')
    #     node = index.data(role = ItemDataRoles.NodeRole)
    #     rename_dialog.setTextValue(node.name)

    #     dialog_code = rename_dialog.exec()
    #     if not dialog_code == rename_dialog.Accepted:
    #         return False

    #     model = self.ui.treeView_HDF.model()
    #     new_name = rename_dialog.textValue()
    #     try:
    #         model.renameItem(index, new_name)
    #         return True
    #     except (ValueError, KeyError) as e:
    #         msg = QMessageBox(parent = self)
    #         msg.setWindowTitle('Warning')
    #         msg.setIcon(QMessageBox.Warning)
    #         msg.setText('Fail to rename: {0}'.format(e))
    #         msg.setStandardButtons(QMessageBox.Ok)
    #         msg.exec()
    #         return False


    # def showCopy(self, index: QModelIndex = None):
    #     """
    #     Shows a dialog to copy an item.

    #     arguments:
    #         index: QModelIndex()
    #     """
    #     dialog_copy = DialogHDFCopy(self)
    #     model = self.ui.treeView_HDF.model()
    #     if not index:
    #         index = self.ui.treeView_HDF.currentIndex()
    #     dialog_copy.setItemPath(index.data(role = ItemDataRoles.PathRole))
    #     dialog_code = dialog_copy.exec()
    #     if not dialog_code == dialog_copy.Accepted:
    #         return False
    #     item_path = dialog_copy.getItemPath()
    #     dest_path = dialog_copy.getDestPath()
    #     try:
    #         model.copyItem(
    #             child = model.indexFromPath(item_path),
    #             dest_parent = model.indexFromPath(dest_path),
    #         )
    #     except (KeyError, ValueError) as e:
    #         msg = QMessageBox(parent = self)
    #         msg.setWindowTitle('Warning')
    #         msg.setIcon(QMessageBox.Warning)
    #         msg.setText('Fail to copy: {0}'.format(e))
    #         msg.setStandardButtons(QMessageBox.Ok)
    #         msg.exec()
    #         return False


    # def showChangeDataType(self, index: QModelIndex = None):
    #     pass

    # def showPlotting(self, index: QModelIndex = None):
    #     """
    #     Choose a plot method for the data.

    #     There are following kinds of data can be plotted:
    #         - Line
    #         - Image
    #         - VecorField
    #         - FourDSTEM

    #     arguments:
    #         index: (QModelIndex)
    #     """
    #     path = index.data(role = ItemDataRoles.PathRole)
    #     node = self.hdf_handler.getNode(path)
    #     page = None
    #     if node.hdf_type == HDFType.Line:
    #         page = self._plotLine(path)
    #     elif node.hdf_type == HDFType.Image:
    #         page = self._plotImage(path)
    #     elif node.hdf_type == HDFType.VectorField:
    #         page = self._plotVectorField(path)
    #     elif node.hdf_type == HDFType.FourDSTEM:
    #         page = self._plotFourDSTEM(path)
    #     else:
    #         shape = self.hdf_handler.file[path].shape
    #         if len(shape) == 1:
    #             page = self._plotLine(path)
    #         elif len(shape) == 2 and shape[0] == 2:
    #             page = self._plotLine(path)
    #         elif len(shape) == 2:
    #             page = self._plotImage(path)
    #         elif len(shape) == 3 and shape[0] == 2:
    #             page = self._plotVectorField(path)
    #         elif len(shape) == 4:
    #             page = self._plotFourDSTEM(path)
    #         else:
    #             self.logger.error('Cannot plot data: {0}'.format(path))
    #             msg = QMessageBox(parent = self)
    #             msg.setWindowTitle('Warning')
    #             msg.setIcon(QMessageBox.Warning)
    #             msg.setStandardButtons(QMessageBox.Ok)
    #             msg.setText('Cannot plot this data.')
    #             msg.exec()
    #     if not page is None:
    #         self.tabview_manager.openTab(page)
        
        
    # def showAttribute(self, index: QModelIndex = None):
    #     """
    #     Shows a dialog to view attributions.

    #     arguments:
    #         index: QModelIndex()
    #     """
    #     dialog_attr = DialogAttrViewer(self)
    #     if not index:
    #         index = self.ui.treeView_HDF.currentIndex()
    #     dialog_attr.setItemPath(index.data(role = ItemDataRoles.PathRole))
    #     dialog_attr.show()


    # def _plotImage(self, path) -> PageViewImage:
    #     """
    #     To plot a image according to the path in the HDF5 file, return the page
    #     where the figure locates.

    #     arguments:
    #         path: (str) 

    #     returns:
    #         (PageViewImage) The page to view image. This page is added to the 
    #             tabWidget in the MainWindow.
    #     """
    #     page_image = PageViewImage()
    #     try:
    #         page_image.setImage(path)
    #     except (KeyError, ValueError) as e:
    #         self.logger.error(e, exc_info = True)
    #         msg = QMessageBox(parent = self)
    #         msg.setWindowTitle('Warning')
    #         msg.setIcon(QMessageBox.Warning)
    #         msg.setStandardButtons(QMessageBox.Ok)
    #         msg.setText('{0}'.format(e))
    #         msg.exec()
    #     return page_image

    # def _plotLine(self, path) -> PageViewLine:
    #     """
    #     To plot a line according to the path in the HDF5 file, return the page
    #     where the figure locates.

    #     arguments:
    #         path: (str)

    #     returns:
    #         (PageViewLine) The page to view line. This page is added to the 
    #             tabWidget in the MainWindow.
    #     """
    #     page_line = PageViewLine()
    #     try:
    #         page_line.addLine(path, update_title = True)
    #     except (KeyError, ValueError) as e:
    #         self.logger.error(e, exc_info = True)
    #         msg = QMessageBox(parent = self)
    #         msg.setWindowTitle('Warning')
    #         msg.setIcon(QMessageBox.Warning)
    #         msg.setStandardButtons(QMessageBox.Ok)
    #         msg.setText('{0}'.format(e))
    #         msg.exec()
    #     return page_line

    # def _plotVectorField(self, path):
    #     pass

    # def _plotFourDSTEM(self, path):
    #     page_fourdstem = PageViewFourDSTEM()
    #     try:
    #         page_fourdstem.setFourDSTEM(path)
    #     except (KeyError, ValueError) as e:
    #         self.logger.error(e, exc_info = True)
    #         msg = QMessageBox(parent = self)
    #         msg.setWindowTitle('Warning')
    #         msg.setIcon(QMessageBox.Warning)
    #         msg.setStandardButtons(QMessageBox.Ok)
    #         msg.setText('{0}'.format(e))
    #         msg.exec()
    #     return page_fourdstem


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
    def __init__(
        self, 
        parent: QWidget = None, 
        index: QModelIndex = QModelIndex(),
    ):
        if not isinstance(index, QModelIndex):
            raise TypeError('index must be QModelIndex, not '
                '{0}'.format(type(index).__name__))
        super().__init__(parent)
        self._model_index = index

        self._action_create = ActionCreate(self, index)
        self._action_copy = ActionCopy(self, index)
        self._action_move = ActionMove(self, index)
        self._action_rename = ActionRename(self, index)
        self._action_delete = ActionDelete(self, index)
        self._action_attributes = ActionAttributes(self, index)
        self._action_change_data_type = ActionChangeDataType(self, index)
        self._action_show_data = ActionShowData(self, index)
        self._action_show_line = ActionShowLine(self, index)
        self._action_show_image = ActionShowImage(self, index)
        self._action_show_vector_field = ActionShowVectorField(self, index)
        self._action_show_fourdstem = ActionShowFourDSTEM(self, index)
        self._action_virtual_image = ActionVirtualImage(self, index)
    
    @property
    def model_index(self) -> QModelIndex:
        return self._model_index

class HDFItemMenu(HDFBaseItemMenu):
    """
    一般的 HDF5 文件对象都有的操作，包括：
        - 移动
        - 复制
        - 删除
        - 重命名
        - 属性
        

    All of the items in HDF5 files have these actions:
        - move
        - copy
        - delete
        - rename
        - attributes
    """
    def __init__(
        self, 
        parent: QWidget = None,
        index: QModelIndex = QModelIndex(),
    ):
        super().__init__(parent, index)

        self.addActions([
            self._action_move,
            self._action_copy,
            self._action_delete,
            self._action_rename,
        ])
        self.addSeparator()
        self.addActions([
            self._action_attributes,
        ])

class HDFRootMenu(HDFBaseItemMenu):
    """
    根目录所具有的操作。包括:
        - 创建
        - 属性

    The root of the HDF5 file has these actions:
        - create
        - attributes
    """
    def __init__(
        self, 
        parent: QWidget = None,
        index: QModelIndex = QModelIndex(),
    ):
        super().__init__(parent, index)

        self.addActions([
            self._action_create,
        ])
        self.addSeparator()
        self.addActions([
            self._action_attributes,
        ])

class HDFGroupMenu(HDFBaseItemMenu):
    """
    Group 具有的操作。包括：
        - 创建
        - 移动
        - 复制
        - 删除
        - 重命名
        - 属性

    Groups in HDF5 files have these actions:
        - create
        - move
        - copy
        - delete
        - rename
        - attributes
    """
    def __init__(
        self, 
        parent: QWidget = None,
        index: QModelIndex = QModelIndex(),
    ):
        super().__init__(parent, index)

        self.addActions([
            self._action_create,
        ])
        self.addSeparator()
        self.addActions([
            self._action_move,
            self._action_copy,
            self._action_delete,
            self._action_rename,
        ])
        self.addSeparator()
        self.addActions([
            self._action_attributes,
        ])

class HDFDataMenu(HDFBaseItemMenu):
    """
    HDF 数据具有的操作，包括：
        - 显示
        - 更改数据类型
        - 移动
        - 复制
        - 删除
        - 重命名
        - 属性

    Datasets in HDF5 files have these actions:
        - show
        - change data type
        - move
        - copy
        - delete
        - rename
        - attributes
    """
    def __init__(
        self, 
        parent: QWidget = None,
        index: QModelIndex = QModelIndex(),
    ):
        super().__init__(parent, index)

        self.addActions([
            self._action_show_data,
            self._action_change_data_type,
        ])

        self.addSeparator()

        self.addActions([
            self._action_move,
            self._action_copy,
            self._action_delete,
            self._action_rename,
        ])

        self.addSeparator()

        self.addActions([
            self._action_attributes
        ])

class HDFLineMenu(HDFBaseItemMenu):
    """
    线性数据所具有的操作。包括：
        - 显示
        - 更改数据类型
        - 移动
        - 复制
        - 删除
        - 重命名
        - 属性

    Line data in HDF5 files have these actions:
        - show
        - change data type
        - move
        - copy
        - delete
        - rename
        - attributes
    """
    def __init__(
        self, 
        parent: QWidget = None,
        index: QModelIndex = QModelIndex(),
    ):
        super().__init__(parent, index)

        self.addActions([
            self._action_show_line,
            self._action_change_data_type,
        ])

        self.addSeparator()
        
        self.addActions([
            self._action_move,
            self._action_copy,
            self._action_delete,
            self._action_rename,
        ])

        self.addSeparator()

        self.addActions([
            self._action_attributes
        ])

class HDFImageMenu(HDFBaseItemMenu):
    """
    图像数据所具有的操作。包括：
        - 显示
        - 更改数据类型
        - 移动
        - 复制
        - 删除
        - 重命名
        - 属性

    Image data in HDF5 files have these actions:
        - show
        - change data type
        - move
        - copy
        - delete
        - rename
        - attributes
    """
    def __init__(
        self, 
        parent: QWidget = None,
        index: QModelIndex = QModelIndex(),
    ):
        super().__init__(parent, index)

        self.addActions([
            self._action_show_image,
            self._action_change_data_type,
        ])

        self.addSeparator()
        
        self.addActions([
            self._action_move,
            self._action_copy,
            self._action_delete,
            self._action_rename,
        ])

        self.addSeparator()

        self.addActions([
            self._action_attributes
        ])
    
class HDFVectorFieldMenu(HDFBaseItemMenu):
    """
    矢量场数据所具有的操作。包括：
        - 显示
        - 更改数据类型
        - 移动
        - 复制
        - 删除
        - 重命名
        - 属性

    Vector field data in HDF5 files have these actions:
        - show
        - change data type
        - move
        - copy
        - delete
        - rename
        - attributes
    """
    def __init__(
        self, 
        parent: QWidget = None,
        index: QModelIndex = QModelIndex(),
    ):
        super().__init__(parent, index)

        self.addActions([
            self._action_show_vector_field,
            self._action_change_data_type,
        ])

        self.addSeparator()
        
        self.addActions([
            self._action_move,
            self._action_copy,
            self._action_delete,
            self._action_rename,
        ])

        self.addSeparator()

        self.addActions([
            self._action_attributes
        ])

class HDFFourDSTEMMenu(HDFBaseItemMenu):
    """
    4D-STEM 数据具有的操作。包括：
        - 显示
        - 更改数据类型
        - 校准
            |- 查看实验参数
            |- 合轴
            |- 背景校正
            |- 角度校正
        - 重构
            |- 虚拟成像
            |- 差分相位衬度 (DPC)
            |- 质心成像 (CoM)
            |- 叠层电子衍射重构 (Ptychography)
        - 移动
        - 复制
        - 删除
        - 重命名
        - 属性
    """
    def __init__(
        self, 
        parent: QWidget = None,
        index: QModelIndex = QModelIndex(),
    ):
        super().__init__(parent, index)

        self.addActions([
            self._action_show_fourdstem,
            self._action_change_data_type,
        ])

        self.addSeparator()
    
        menu_calibrate = self.addMenu('Calibrate')
        menu_reconstruct = self.addMenu('Reconstruct')
        menu_reconstruct.addActions([
            self._action_virtual_image
        ])
        
        self.addSeparator()

        self.addActions([
            self._action_move,
            self._action_copy,
            self._action_delete,
            self._action_rename,
        ])

        self.addSeparator()

        self.addActions([
            self._action_attributes,
        ])

        

# class HDFBaseItemMenu(QMenu):
#     """
#     当点到 HDFTreeView 时的鼠标右键菜单。

#     允许对 Item 进行修改操作。在使用时请根据取到的 QModelIndex 选择其合适的子类。

#     The context menu of HDF tree view.

#     Allowing modification operations of items. Use its subclass according to
#     the current QModelIndex.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self._model_index = QModelIndex()

#     @property
#     def model_index(self) -> QModelIndex:
#         return self._model_index

#     def setModelIndex(self, index: QModelIndex):
#         """
#         Set the model index that this menu should handle.
#         """
#         if not isinstance(index, QModelIndex):
#             raise TypeError('index must be QModelIndex object, not '
#                 '{0}'.format(type(index).__name__))
#         self._model_index = index

#     def addModifyActions(self):
#         """
#         Add move, copy, delete, rename actions.
#         """
#         self.addSeparator()
#         act_str_list = [action.text() for action in self.actions()]
#         if not 'Move' in act_str_list:
#             self.action_move = self.addAction('Move')
#         if not 'Copy' in act_str_list:
#             self.action_copy = self.addAction('Copy')
#         if not 'Delete' in act_str_list:
#             self.action_delete = self.addAction('Delete')
#         if not 'Rename' in act_str_list:
#             self.action_rename = self.addAction('Rename')
            
    
#     def addAtributeActions(self):
#         """
#         Add check attribute actions
#         """
#         self.addSeparator()
#         act_str_list = [action.text() for action in self.actions()]
#         if not 'Attributes' in act_str_list:
#             self.action_attributes = self.addAction('Attributes')

# class HDFItemMenu(HDFBaseItemMenu):
#     """
#     当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Item。

#     The context menu of HDF tree view when current index is item.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self.addModifyActions()
#         self.addAtributeActions()


# class HDFRootMenu(HDFBaseItemMenu):
#     """
#     当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Root。

#     The context menu of HDF tree view when current index is root.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self.action_create = self.addAction('Create')
#         self.addAtributeActions()
        

# class HDFGroupMenu(HDFBaseItemMenu):
#     """
#     当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Group。

#     The context menu of HDF tree view when current index is group.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self.action_create = self.addAction('Create')
#         self.addModifyActions()
#         self.addAtributeActions()

# class HDFDataMenu(HDFBaseItemMenu):
#     """
#     当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Data。

#     The context menu of HDF tree view when current index is data.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self.action_show = self.addAction('Show')
#         self.action_change_type = self.addAction('Change Type')
#         self.addModifyActions()
#         self.addAtributeActions()
        
# class HDFLineMenu(HDFBaseItemMenu):
#     """
#     当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Line。

#     The context menu of HDF tree view when current index is line.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self.action_show = self.addAction('Show')
#         self.action_change_type = self.addAction('Change Type')
#         self.addModifyActions()
#         self.addAtributeActions()


# class HDFImageMenu(HDFBaseItemMenu):
#     """
#     当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Image。

#     The context menu of HDF tree view when current index is image.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self.action_show = self.addAction('Show')
#         self.action_change_type = self.addAction('Change Type')
#         self.addModifyActions()
#         self.addAtributeActions()


# class HDFVectorFieldMenu(HDFBaseItemMenu):
#     """
#     当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 Vector Field。

#     The context menu of HDF tree view when current index is vector field.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)
#         self.action_show = self.addAction('Show')
#         self.action_change_type = self.addAction('Change Type')
#         self.addModifyActions()
#         self.addAtributeActions()


# class HDFFourDSTEMMenu(HDFBaseItemMenu):
#     """
#     当点到 HDFTreeView 时的鼠标右键菜单。此时 Index 为 4D-STEM 数据集。

#     The context menu of HDF tree view when current index is 4D-STEM datacube.
#     """
#     def __init__(self, parent: QWidget = None):
#         super().__init__(parent)

#         self.action_show = self.addAction('Show')
#         self.action_change_type = self.addAction('Change Type')
#         self.addSeparator()

#         self.submenu_calibrate = self.addMenu('Calibrate')
#         self.action_parameters = self.submenu_calibrate.addAction(
#             'Optical Parameters'
#         )
#         self.action_align = self.submenu_calibrate.addAction('Align')
#         self.action_bkgrd_substract = self.submenu_calibrate.addAction(
#             'Backgroun Substract'
#         )
#         self.action_angle_correct = self.submenu_calibrate.addAction(
#             'Angular Offset Correct'
#         )

#         self.submenu_reconstruct = self.addMenu('Reconstruct')
#         self.action_virtual_image = self.submenu_reconstruct.addAction(
#             'Virtual Image'
#         )
#         self.action_DPC = self.submenu_reconstruct.addAction(
#             'Differentiated Phase Contrast (DPC)'
#         )
#         self.action_CoM = self.submenu_reconstruct.addAction(
#             'Center of Mass (CoM)'
#         )


#         self.addModifyActions()
#         self.addAtributeActions()


