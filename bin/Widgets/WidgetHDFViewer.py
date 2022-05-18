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
    ActionCenterOfMass,
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

from bin.Widgets.WidgetBaseHDFViewer import WidgetBaseHDFViewer


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
        
        if not self.hdf_handler.isFileOpened():
            self._showFileMenu(pos)
        else:
            index = self.ui.treeView_HDF.currentIndex()
            chosen_type = index.data(
                role = ItemDataRoles.HDFTypeRole
            )
            if chosen_type == HDFType.Root:
                menu = HDFRootMenu(self, index)
                
            elif chosen_type == HDFType.Group:
                menu = HDFGroupMenu(self, index)
                
            elif chosen_type == HDFType.FourDSTEM:
                menu = HDFFourDSTEMMenu(self, index)
                
            elif chosen_type == HDFType.Image:
                menu = HDFImageMenu(self, index)
                
            elif chosen_type == HDFType.Data:
                menu = HDFDataMenu(self, index)
                
            else:
                menu = HDFItemMenu(self, index)
                
            menu.exec(self.ui.treeView_HDF.mapToGlobal(pos))


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
        self._action_center_of_mass = ActionCenterOfMass(self, index)
    
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
            self._action_virtual_image,
            self._action_center_of_mass,
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

        