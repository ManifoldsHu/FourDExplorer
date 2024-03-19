# -*- coding: utf-8 -*-

"""
*----------------------------- ItemActions.py --------------------------------*
针对 HDF5 文件中的各个 Object 的各个 Actions。

已废弃

作者:           胡一鸣
创建日期:       2022年4月11日

This module includes actions towards objects of HDF5.

DEPRECATED

author:         Hu Yiming
date:           Apr 11, 2022
*----------------------------- ItemActions.py --------------------------------*
"""

from logging import Logger
import sys
import os

from PySide6.QtCore import QModelIndex, Qt, QObject
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMessageBox, QWidget, QInputDialog

from bin.HDFManager import HDFHandler, HDFType
from bin.TaskManager import Task
# from bin.TabViewManager import TabViewManager
from bin.Widgets.DialogAttrViewer import DialogAttrViewer
from bin.Widgets.DialogCopyItem import DialogHDFCopy
from bin.Widgets.DialogCreateItem import DialogHDFCreate
from bin.Widgets.DialogImportFourDSTEM import DialogImportFourDSTEM
from bin.Widgets.DialogMoveItem import DialogHDFMove
from bin.Widgets.PageAlignFourDSTEM import PageAlignFourDSTEM
from bin.Widgets.PageBkgrdFourDSTEM import PageBkgrdFourDSTEM
from bin.Widgets.PageRotateFourDSTEM import PageRotateFourDSTEM
from bin.Widgets.PageViewFourDSTEM import PageViewFourDSTEM
from bin.Widgets.PageViewLine import PageViewLine
from bin.Widgets.PageViewImage import PageViewImage
from bin.Widgets.PageViewVectorField import PageViewVectorField
from bin.Widgets.PageVirtualImage import PageVirtualImage
from bin.Widgets.PageCenterOfMass import PageCenterOfMass 

from Constants import HDFType, ItemDataRoles
from lib.ImporterEMPAD import ImporterEMPAD, ImporterEMPAD_NJU
from lib.ImporterRaw import ImporterRawFourDSTEM


class ActionItemBase(QAction):
    """
    所有有关 HDF 对象的 Action 的基类。

    The base class of actions about HDF items.
    """
    def __init__(
        self, 
        parent: QObject = None,
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in 
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        if not isinstance(item_index, QModelIndex):
            raise TypeError('item_index must be QModelIndex, not '
                '{0}'.format(type(item_index).__name__))
        if not isinstance(item_path, str):
            raise TypeError('item_path msut be a str, not '
                '{0}'.format(type(item_path).__name__))
        super().__init__(parent)
        self._item_index = item_index
        self._item_path = item_path

    @property
    def item_index(self) -> QModelIndex:
        return self._item_index

    @property
    def item_path(self) -> str:
        if self._item_path:
            return self._item_path
        elif self.item_index.isValid():
            return self.item_index.data(
                role = ItemDataRoles.PathRole
            )
        else:
            return ''
        

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger


class ActionCreate(ActionItemBase):
    """
    创建 HDF 文件对象的 Action。

    Action to create HDF items.
    """
    def __init__(self, 
        parent: QObject = None,
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in 
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Create')
        self.triggered.connect(self.createItem)

    def createItem(self):
        """
        Shows a dialog to create an item.
        """
        dialog_create = DialogHDFCreate()
        dialog_create.initNames(parent_path = self.item_path)
        dialog_code = dialog_create.exec()
        if not dialog_code == dialog_create.Accepted:
            return 
        item_type = dialog_create.getItemType()
        parent_path = dialog_create.getParentPath()
        name = dialog_create.getName()
        model = self.hdf_handler.model
        parent_index = model.indexFromPath(parent_path)
        try:
            if item_type == HDFType.Group:
                model.insertGroup(parent_index, name) 
            elif item_type == HDFType.Data:
                shape = dialog_create.getShape()
                dtype = dialog_create.getDType()
                model.insertData(
                    parent = parent_index, 
                    name = name,
                    shape = shape,
                    dtype = dtype,
                ) 
        except (ValueError, KeyError) as e:
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Fail to create: {0}'.format(e))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return False
        

class ActionMove(ActionItemBase):
    """
    移动 HDF 文件对象的 Action。

    Action to move HDF items.
    """
    def __init__(self, 
        parent: QObject = None,
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in 
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Move')
        self.triggered.connect(self.moveItem)

    def moveItem(self):
        """
        Shows a dialog to move items.
        """
        dialog_move = DialogHDFMove()
        model = self.hdf_handler.model
        index = model.indexFromPath(self.item_path)
        dialog_move.setItemPath(self.item_path)
        dialog_code = dialog_move.exec()
        if not dialog_code == dialog_move.Accepted:
            return False
        item_path = dialog_move.getItemPath()
        dest_path = dialog_move.getDestPath()
        try:
            model.moveItem(
                child = model.indexFromPath(item_path), 
                dest_parent = model.indexFromPath(dest_path),
            )
        except (KeyError, ValueError) as e:
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Fail to move: {0}'.format(e))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return False

class ActionRename(ActionItemBase):
    """
    重命名 HDF 文件对象的 Action。

    Action to rename HDF items.
    """
    def __init__(self, 
        parent: QObject = None,
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in 
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Rename')
        self.triggered.connect(self.renameItem)

    def renameItem(self):
        """
        Shows a dialog to rename an item.

        arguments:
            index: (QModelIndex)
        """
        model = self.hdf_handler.model
        index = model.indexFromPath(self.item_path)
        rename_dialog = QInputDialog()
        rename_dialog.setWindowTitle('Rename Item')
        rename_dialog.setInputMode(QInputDialog.TextInput)
        rename_dialog.setLabelText('Enter a new name')
        node = index.data(role = ItemDataRoles.NodeRole)
        rename_dialog.setTextValue(node.name)
        dialog_code = rename_dialog.exec()
        if not dialog_code == rename_dialog.Accepted:
            return 
        new_name = rename_dialog.textValue()
        try:
            model.renameItem(index, new_name)
        except (ValueError, KeyError) as e:
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Fail to rename: {0}'.format(e))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return False

class ActionCopy(ActionItemBase):
    """
    复制 HDF 对象的 Action。

    Actions to copy items.
    """
    def __init__(self, 
        parent: QObject = None,
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in 
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Copy')
        self.triggered.connect(self.copyItem)

    def copyItem(self):
        """
        Shows a dialog to copy an item.
        """
        dialog_copy = DialogHDFCopy()
        model = self.hdf_handler.model
        index = model.indexFromPath(self.item_path)
        dialog_copy.setItemPath(self.item_path)
        dialog_code = dialog_copy.exec()
        if not dialog_code == dialog_copy.Accepted:
            return
        item_path = dialog_copy.getItemPath()
        dest_path = dialog_copy.getDestPath()
        try:
            model.copyItem(
                child = model.indexFromPath(item_path),
                dest_parent = model.indexFromPath(dest_path),
            )
        except (KeyError, ValueError) as e:
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Fail to copy: {0}'.format(e))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return False

class ActionDelete(ActionItemBase):
    """
    用于删除 HDF 对象的 Action。

    Action to delete HDF items.
    """
    def __init__(self, 
        parent: QObject = None,
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in 
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Delete')
        self.triggered.connect(self.deleteItem)

    def deleteItem(self):
        """
        Shows a dialog to delete items.

        If the index indicates a group, all of the subitems will be also 
        deleted recursively.
        """
        model = self.hdf_handler.model
        index = model.indexFromPath(self.item_path)
        dialog_delete = QMessageBox()
        dialog_delete.setIcon(QMessageBox.Question)
        dialog_delete.setWindowTitle('Delete Item')
        dialog_delete.setText(
            'Do you want to delete the item permanently?\n'
            '{0}'.format(self.item_path)
        )
        dialog_delete.setStandardButtons(
            QMessageBox.Ok|QMessageBox.Cancel
        )
        dialog_code = dialog_delete.exec()
        if not dialog_code == QMessageBox.Ok:
            return 
        try:
            model.removeItem(index)
        except (ValueError, KeyError) as e:
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Fail to delete: {0}'.format(e))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

class ActionAttributes(ActionItemBase):
    """
    查看 HDF 文件对象属性的 Action。

    Action to view attributes of HDF items.
    """
    def __init__(self, 
        parent: QObject = None,
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in 
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Attributes')
        self.triggered.connect(self.viewAttributes)

    def viewAttributes(self):
        """
        Shows a dialog to view attrbutes of the item.
        """
        global qApp
        dialog_attr = DialogAttrViewer(qApp.main_window)
        dialog_attr.setItemPath(self.item_path)
        dialog_attr.show()

class ActionChangeDataType(ActionItemBase):
    """
    更改 HDF 文件对象类型的 Action

    Action to change the data type of HDF items.
    """
    def __init__(self, 
        parent: QObject = None,
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in 
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Change Data Type')
        self.triggered.connect(self.changeDataType)

    def changeDataType(self):
        """
        TODO Shows a dialog to change data type.
        """
        pass


class ActionShowData(ActionItemBase):
    """
    展示数据的 Action。

    Actions to show data.
    """
    def __init__(self, 
        parent: QObject = None, 
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in 
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Show')
        self.triggered.connect(self.plotData)

    @property
    # def tabview_manager(self) -> TabViewManager:
    def tabview_manager(self):
        global qApp
        return qApp.tabview_manager


    def setItemPath(self, item_path: str):
        """
        Set the item's path handled by this action.
        """
        if not isinstance(item_path, str):
            raise TypeError('item_path msut be a str, not '
                '{0}'.format(type(item_path).__name__))
        self._item_path = item_path

    def plotData(self):
        """
        Choose a plot method for the data.

        There are following kinds of data can be plotted:
            - Line
            - Image
            - VectorField
            - FourDSTEM

        arguments:
            index: (QModelIndex)
        """
        node = self.hdf_handler.getNode(self.item_path)
        page = None
        if node.hdf_type == HDFType.Line:
            page = self._plotLine(self.item_path)
        elif node.hdf_type == HDFType.Image:
            page = self._plotImage(self.item_path)
        elif node.hdf_type == HDFType.VectorField:
            page = self._plotVectorField(self.item_path)
        elif node.hdf_type == HDFType.FourDSTEM:
            page = self._plotFourDSTEM(self.item_path)
        else:
            shape = self.hdf_handler.file[self.item_path].shape
            if len(shape) == 1:
                page = self._plotLine(self.item_path)
            elif len(shape) == 2 and shape[0] == 2:
                page = self._plotLine(self.item_path)
            elif len(shape) == 2:
                page = self._plotImage(self.item_path)
            elif len(shape) == 3 and shape[0] == 2:
                page = self._plotVectorField(self.item_path)
            elif len(shape) == 4:
                page = self._plotFourDSTEM(self.item_path)
            else:
                self.logger.error(
                    'Cannot plot data: {0}'.format(self.item_path)
                )
                msg = QMessageBox()
                msg.setWindowTitle('Warning')
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setText('Cannot plot this data.')
                msg.exec()
    
        if not page is None:
            self.tabview_manager.openTab(page)

    def _plotImage(self, path) -> PageViewImage:
        """
        To plot a image according to the path in the HDF5 file, return the page
        where the figure locates.

        arguments:
            path: (str) 

        returns:
            (PageViewImage) The page to view image. This page is added to the 
                tabWidget in the MainWindow.
        """
        page_image = PageViewImage()
        try:
            page_image.setImage(path)
        except (KeyError, ValueError) as e:
            self.logger.error(e, exc_info = True)
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('{0}'.format(e))
            msg.exec()
        return page_image

    def _plotLine(self, path) -> PageViewLine:
        """
        To plot a line according to the path in the HDF5 file, return the page
        where the figure locates.

        arguments:
            path: (str)

        returns:
            (PageViewLine) The page to view line. This page is added to the 
                tabWidget in the MainWindow.
        """
        page_line = PageViewLine()
        try:
            page_line.addLine(path, update_title = True)
        except (KeyError, ValueError) as e:
            self.logger.error(e, exc_info = True)
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('{0}'.format(e))
            msg.exec()
        return page_line

    def _plotVectorField(self, path):
        """
        To plot a vector field according to the path in the HDF5 file, return
        the page where the figure locates.

        arguments:
            path: (str)

        returns:
            (PageViewVectorField) The page to view the vector field. This page
                is added to the tabWidget in the MainWindow.
        """
        page_vector = PageViewVectorField()
        try:
            page_vector.setVectorField(path)
        except (KeyError, ValueError) as e:
            self.logger.error(e, exc_info = True)
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('{0}'.format(e))
            msg.exec()
        return page_vector

    def _plotFourDSTEM(self, path):
        """
        To plot a 4D-STEM dataset according to the path in the HDF5 file, and
        return the page where the figure locates.

        arguments:
            path: (str)

        returns:
            (PageViewFourDSTEM) The page to view 4D-STEM. This page is added to
                the tabWidget in the MainWindow.
        """
        page = PageViewFourDSTEM()
        try:
            page.setFourDSTEM(path)
        except (KeyError, ValueError) as e:
            self.logger.error(e, exc_info = True)
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('{0}'.format(e))
            msg.exec()
        return page

class ActionShowLine(ActionShowData):
    """
    绘制曲线的 Action。

    When the index is a line, use this action.
    """
    def plotData(self):
        """
        Force to use plot line method.
        """
        page = self._plotLine(self.item_path)
        self.tabview_manager.openTab(page)

class ActionShowImage(ActionShowData):
    """
    绘制二维图像的 Action。

    When the index is an image, use this action.
    """
    def plotData(self):
        """
        Force to use plot image method.
        """
        page = self._plotImage(self.item_path)
        self.tabview_manager.openTab(page)

class ActionShowVectorField(ActionShowData):
    """
    绘制二维矢量场的 Action。

    When the index is a vector field, use this action.
    """
    def plotData(self):
        """
        Force to use plot vector field method.
        """
        page = self._plotVectorField(self.item_path)
        self.tabview_manager.openTab(page)

class ActionShowFourDSTEM(ActionShowData):
    """
    绘制 4D-STEM 的 Action。

    When the index is a 4D-STEM dataset, use this action.
    """
    def plotData(self):
        """
        Force to use plot 4D-STEM method.
        """
        page = self._plotFourDSTEM(self.item_path)
        self.tabview_manager.openTab(page)

class ActionVirtualImage(ActionShowData):
    """
    计算 4D-STEM 虚拟成像的 Action。

    Action to calculate 4D-STEM virtual images.
    """
    def __init__(self, 
        parent: QObject = None, 
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in 
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Virtual Image')
        

    def plotData(self):
        """
        Force to use virtual image method.
        """
        page = self._openVirtualImage(self.item_path)
        self.tabview_manager.openTab(page)

    def _openVirtualImage(self, path: str):
        """
        Open a page to calculate virtual images.

        arguments:
            path: (str) The 4D-STEM path to calculate virtual images.
        """
        page = PageVirtualImage()
        page.setFourDSTEM(path)
        return page

class ActionImportFourDSTEM(ActionItemBase):
    """
    导入 EMPAD 的 4D-STEM 数据的 Action。

    Action to import 4D-STEM dataset from EMPAD.
    """
    def __init__(self, 
        parent: QObject = None, 
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in 
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Import 4D-STEM dataset')
        self.triggered.connect(self.importFourDSTEM)

    def importFourDSTEM(self):
        """
        Shows a dialog to import 4D-STEM dataset.
        """
        dialog_import = DialogImportFourDSTEM()
        if self.item_path == '':
            dialog_import.setParentPath('/')
        else:
            dialog_import.setParentPath(self.item_path)

        dialog_code = dialog_import.exec()
        if not dialog_code == dialog_import.Accepted:
            return 
        new_name = dialog_import.getNewName()

        parent_path = dialog_import.getParentPath()

        mode = dialog_import.getImportMode()
        page = dialog_import.getPage(mode)
        if mode == 0:
            importer = ImporterEMPAD(new_name, parent_path)
            xml_path = page.getHeaderPath()
            importer.parseHead(xml_path)
            importer.loadData()
        elif mode == 1:
            importer = ImporterEMPAD_NJU(new_name, parent_path)
            xml_path = page.getHeaderPath()
            importer.parseHead(xml_path)
            importer.loadData()

        elif mode == 3:
            importer = ImporterRawFourDSTEM(new_name, parent_path)
            meta = {
                'raw_path': page.getRawPath(),
                'scalar_type': page.getScalarType(),
                'dp_i': page.getDp_i(),
                'dp_j': page.getDp_j(),
                'scan_i': page.getScan_i(),
                'scan_j': page.getScan_j(),
                'offset_to_first_image': page.getOffsetToFirstImage(),
                'gap_between_images': page.getGapBetweenImages(),
                'little_endian': page.getLittleEndian(),
            }
            importer.setMeta(**meta)
            importer.loadData()

        else:
            pass 


class ActionCenterOfMass(ActionShowData):
    """
    计算 4D-STEM 虚拟成像的 Action。

    Action to calculate 4D-STEM virtual images.
    """
    def __init__(self,
        parent: QObject = None,
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in 
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Center Of Mass')

    def plotData(self):
        """
        Force to use CoM method.
        """
        page = self._openCenterOfMass(self.item_path)
        self.tabview_manager.openTab(page)

    def _openCenterOfMass(self, path: str):
        """
        Open a page to calculate virtual images.

        arguments:
            path: (str) The 4D-STEM path to calculate virtual images.
        """
        page = PageCenterOfMass()
        page.setFourDSTEM(path)
        return page
    

class ActionAlign(ActionShowData):
    """
    对 4D-STEM 数据集进行平移合轴的 Action。

    Action to align 4D-STEM dataset.
    """
    def __init__(self,
        parent: QObject = None,
        item_index = QModelIndex(),
        item_path = '',    
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Alignment')

    def plotData(self):
        """
        Force to use PageAlignFourDSTEM.
        """
        page = self._openAlign(self.item_path)
        self.tabview_manager.openTab(page)

    def _openAlign(self, path: str):
        """
        Open a page to align the 4D-STEM dataset.
        """
        page = PageAlignFourDSTEM()
        page.setFourDSTEM(path)
        return page 

class ActionBkgrd(ActionShowData):
    """
    对 4D-STEM 数据进行抠背底操作的 Action。

    Action to subtract background of 4D-STEM data.
    """
    def __init__(self,
        parent: QObject = None,
        item_index = QModelIndex(),
        item_path = '',     
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Background Filtering')

    def plotData(self):
        """
        Force to use PageBkgrdFourDSTEM.
        """
        page = self._openBkgrd(self.item_path)
        self.tabview_manager.openTab(page)

    def _openBkgrd(self, path: str):
        """
        Open a page to filter the background for 4D-STEM dataset.
        """
        page = PageBkgrdFourDSTEM()
        page.setFourDSTEM(path)
        return page 

class ActionRotate(ActionShowData):
    """
    对 4D-STEM 进行旋转 DP 操作的 Action。

    Action to rotate diffraction patterns of 4D-STEM data.
    """
    def __init__(self,
        parent: QObject = None,
        item_index = QModelIndex(),
        item_path = '',
    ):
        """
        arguments:
            parent: (QObject)

            item_index: (QModelIndex) must be the index of the HDF model, in
                which there exist a valid item path.

            item_path: (str) the item's path handled by this action.
        """
        super().__init__(parent, item_index, item_path)
        self.setText('Rotational Offset Calibrating')

    def plotData(self):
        """
        Force to use PageBkgrdFourDSTEM.
        """
        page = self._openRotate(self.item_path)
        self.tabview_manager.openTab(page)

    def _openRotate(self, path):
        """
        Open a page to find the rotational angle.
        """
        page = PageRotateFourDSTEM()
        page.setFourDSTEM(path)
        return page 



