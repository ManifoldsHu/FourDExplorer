# -*- coding: utf-8 -*-

"""
*---------------------------- EditActions.py ---------------------------------*
针对 HDF Tree 的各种操作的 Action。

作者:           胡一鸣
创建日期:       2022年6月14日

This module includes actions towards HDF Tree.

author:         Hu Yiming
date:           Jun 14, 2022
*---------------------------- EditActions.py ---------------------------------*
"""


from logging import Logger
import os 
import datetime
import time 

from PySide6.QtCore import QObject, QModelIndex
from PySide6.QtWidgets import QMessageBox, QInputDialog, QTreeView
from PySide6.QtGui import QAction
from Constants import ItemDataRoles, HDFType, APP_VERSION

from bin.HDFManager import HDFHandler
from bin.UIManager import ThemeHandler
from bin.Widgets.DialogChangeDataType import DialogChangeDataType
from bin.Widgets.DialogCreateItem import DialogHDFCreate
from bin.Widgets.DialogImportFourDSTEM import DialogImportFourDSTEM
from bin.Widgets.DialogMoveItem import DialogHDFMove
from bin.Widgets.DialogCopyItem import DialogHDFCopy
# from bin.Widgets.DialogAttrViewer import DialogAttrViewer
from bin.Widgets.DialogMetaViewer import DialogMetaViewer
from bin.Widgets.DialogImportImage import DialogImportImage
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.Widgets.WidgetImportEMPAD import WidgetImportEMPAD
from bin.Widgets.WidgetImportMerlin import WidgetImportMerlin 
from bin.Widgets.WidgetImportRaw import WidgetImportRaw 
from bin.Widgets.WidgetImportNumpy import WidgetImportNumpy 
from lib.ImporterEMPAD import ImporterEMPAD, ImporterEMPAD_NJU
from lib.ImporterRaw import ImporterRawFourDSTEM
from lib.ImporterMIB import ImporterMIB
from lib.ImporterNumpy import ImporterNumpy
from lib.TaskLoadData import TaskLoadTiff

class ActionEditBase(QAction):
    """
    关于编辑 HDF 对象的 Action 的基类。

    The base class of actions for editting HDF items.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._item_path = ''
        self._icon_name = ''
        self.theme_handler.theme_changed.connect(
            self._updateIcon
        )
        self.setEnabled(self.hdf_handler.isFileOpened())
        # self.hdf_handler.file_opened.connect(
        #     lambda: self.setEnabled(True)
        # )
        # self.hdf_handler.file_closed.connect(
        #     lambda: self.setEnabled(False)
        # )
        self.hdf_handler.file_opened.connect(
            self._onFileOpened
        )
        self.hdf_handler.file_closed.connect(
            self._onFileClosed
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

def failLogging(func):
    """
    Try to do something. If failed, log it.

    This is a decorator, used for these actions on-triggered functions.
    """
    def wrapper(self: ActionEditBase, *args, **kw):
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


class ActionNew(ActionEditBase):
    """
    创建 HDF 文件对象的 Action。

    Action to create HDF items.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('New')
        self.initIconResources('file_add')
        self.triggered.connect(lambda: self.createItem(self))
    
    @failLogging
    def createItem(self):
        """
        Open a dialog to create item (group or data).
        """
        if self._treeview is not None:
            self.setItemPathFromIndex(self._treeview.currentIndex())
        dialog_create = DialogHDFCreate()
        dialog_create.initNames(parent_path = self.item_path)
        dialog_code = dialog_create.exec()
        if not dialog_code == dialog_create.Accepted:
            return 
        item_type = dialog_create.getItemType()
        parent_path = dialog_create.getParentPath()
        name = dialog_create.getName()
        if item_type == HDFType.Group:
            self.hdf_handler.addNewGroup(parent_path, name)
        elif item_type == HDFType.Data:
            shape = dialog_create.getShape()
            dtype = dialog_create.getDType()
            self.hdf_handler.addNewData(
                parent_path = parent_path,
                name = name,
                shape = shape,
                dtype = dtype,
            )


class ActionMove(ActionEditBase):
    """
    创建 HDF 文件对象的 Action。

    Action to create HDF items.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Move')
        self.initIconResources('switch')
        self.triggered.connect(lambda: self.moveItem(self))

    @failLogging
    def moveItem(self):
        """
        Shows a dialog to move items.
        """
        if self._treeview is not None:
            self.setItemPathFromIndex(self._treeview.currentIndex())
        dialog_move = DialogHDFMove()
        dialog_move.setItemPath(self.item_path)
        dialog_code = dialog_move.exec()
        if not dialog_code == dialog_move.Accepted:
            return False 

        item_path = dialog_move.getItemPath()
        dest_path = dialog_move.getDestPath()
        self.hdf_handler.moveItem(item_path, dest_path)


class ActionRename(ActionEditBase):
    """
    重命名 HDF 文件对象的 Action。

    Action to rename HDF items.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Rename')
        self.initIconResources('edit')
        self.triggered.connect(lambda: self.renameItem(self))

    @failLogging
    def renameItem(self):
        """
        Shows a dialog to rename an item.
        """
        if self._treeview is not None:
            self.setItemPathFromIndex(self._treeview.currentIndex())
        rename_dialog = QInputDialog()
        rename_dialog.setWindowTitle('Rename Item')
        rename_dialog.setInputMode(QInputDialog.TextInput)
        rename_dialog.setLabelText('Enter a new name')
        rename_dialog.setTextValue(self.item_path.split('/')[-1])
        dialog_code = rename_dialog.exec()
        if not dialog_code == rename_dialog.Accepted:
            return False 
        new_name = rename_dialog.textValue()
        self.hdf_handler.renameItem(self.item_path, new_name)


class ActionCopy(ActionEditBase):
    """
    复制 HDF 文件对象的 Action。

    Action to copy items.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Copy')
        self.initIconResources('copy')
        self.triggered.connect(lambda: self.copyItem(self))

    @failLogging
    def copyItem(self):
        """
        Shows a dialog to copy an item.
        """
        if self._treeview is not None:
            self.setItemPathFromIndex(self._treeview.currentIndex())
        dialog_copy = DialogHDFCopy()
        dialog_copy.setItemPath(self.item_path)
        dialog_code = dialog_copy.exec()
        if not dialog_code == dialog_copy.Accepted:
            return False 
        item_path = dialog_copy.getItemPath()
        dest_path = dialog_copy.getDestPath()
        self.hdf_handler.copyItem(item_path, dest_path)


class ActionDelete(ActionEditBase):
    """
    用于删除 HDF 对象的 Action。

    Action to delete HDF items.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Delete')
        self.initIconResources('file_delete')
        self.triggered.connect(lambda: self.deleteItem(self))

    @failLogging
    def deleteItem(self):
        """
        Shows a dialog to delete items.

        If the index indicates a group, all of the subitems will be also 
        deleted recursively.
        """
        if self._treeview is not None:
            self.setItemPathFromIndex(self._treeview.currentIndex())
        if not self.item_path:
            dialog = DialogHDFChoose()
            dialog.setWindowTitle('Choose an item to delete')
            dialog_code = dialog.exec()
            if dialog_code == dialog.Accepted:
                self.setItemPath(dialog.getCurrentPath())
            else:
                return
            
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
            return False 
        self.hdf_handler.deleteItem(self.item_path)


class ActionChangeHDFType(ActionEditBase):
    """
    用于改变 HDF 数据集类型 (扩展名) 的 Action。

    Action to change the type (i.e. extension name) of hdf items.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Change Data Type')
        self.initIconResources('layers')
        self.triggered.connect(lambda: self.changeHDFType(self))

    @failLogging
    def changeHDFType(self):
        """
        Shows a dialog to change the HDFType of a Dataset.

        In fact, this function will only change the extension of the item.
        """
        if self._treeview is not None:
            self.setItemPathFromIndex(self._treeview.currentIndex())
        dialog_change = DialogChangeDataType()
        if self.item_path:
            dialog_change.setItemPath(self.item_path)
        dialog_code = dialog_change.exec()
        if not dialog_code == dialog_change.Accepted:
            return 
        
        target_path = dialog_change.item_path
        target_ext = dialog_change.getTargetExt()
        node = self.hdf_handler.getNode(target_path)
        if '.' in node.name:
            name_array = node.name.split('.')
            ext = name_array.pop()
            name = '.'.join(name_array)
            if target_ext == '':    # No specific type
                new_name = name 
            else:
                new_name = name + '.' + target_ext
        else:
            if target_ext == '':
                new_name = node.name 
            else:
                new_name = node.name + '.' + target_ext 
        
        self.hdf_handler.renameItem(target_path, new_name)


class ActionAttributes(ActionEditBase):
    """
    查看 HDF 文件对象属性的 Action。

    Action to view attributes of HDF items.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Attributes')
        self.initIconResources('attributes')
        self.triggered.connect(lambda: self.viewAttributes(self))

    @failLogging
    def viewAttributes(self):
        """
        Shows a dialog to view attributes of the item.
        """
        if self._treeview is not None:
            self.setItemPathFromIndex(self._treeview.currentIndex())
        
        if not self._item_path:
            dialog_choose_dataset = DialogHDFChoose()
            dialog_choose_dataset.setWindowTitle('Choose an item')
            dialog_code = dialog_choose_dataset.exec()
            if dialog_code == dialog_choose_dataset.Accepted:
                self.item_path = dialog_choose_dataset.getCurrentPath()
            else:
                return
        
        # Here we must bind the dialog to the main window. Otherwise,
        # the lifetime of the dialog will be ended just after this 
        # function is ended. 

        # This problem occurs only when we use dialog.show() method,
        # which will keep the dialog showing while let the code continue.
        # If we use dialog.exec(), the code will stop and wait for that 
        # function returning, which keeps the lifetime of the dialog.
        global qApp 
        # dialog_attr = DialogAttrViewer(qApp.main_window)
        dialog_attr = DialogMetaViewer(qApp.main_window)
        dialog_attr.setItemPath(self.item_path)
        dialog_attr.show()


class ActionImportFourDSTEM(ActionEditBase):
    """
    导入 4D-STEM 数据集的 Action。

    Action to import 4D-STEM dataset.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Import 4D-STEM dataset')
        self.triggered.connect(lambda: self.importFourDSTEM(self))

    @failLogging
    def importFourDSTEM(self):
        """
        Open a dialog to choose a 4D-STEM dataset, and submit the import task.
        """
        if self._treeview is not None:
            self.setItemPathFromIndex(self._treeview.currentIndex())
        dialog_import = DialogImportFourDSTEM()
        if self.item_path:
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
            page: WidgetImportEMPAD
            xml_path = page.getHeaderPath()
            importer.parseHead(xml_path)
            importer.loadData()
        
        elif mode == 1:
            importer = ImporterEMPAD_NJU(new_name, parent_path)
            page: WidgetImportEMPAD
            xml_path = page.getHeaderPath()
            importer.parseHead(xml_path)
            importer.loadData()

        elif mode == 2:
            importer = ImporterMIB(new_name, parent_path)
            page: WidgetImportMerlin
            mib_path = page.getMibPath()
            # hdr_path = page.getHeaderPath()
            importer.parseMibHead(mib_path)
            importer.scan_i = page.scan_i
            importer.scan_j = page.scan_j 
            importer.loadData()

            # importer.parseHdrFile(hdr_path)


        elif mode == 3:
            importer = ImporterRawFourDSTEM(new_name, parent_path)
            page: WidgetImportRaw
            importer.setReadParameters(
                raw_path = page.getRawPath(),
                scalar_type = page.getScalarType(),
                scalar_size = page.getScalarSize(),
                dp_i = page.getDp_i(),
                dp_j = page.getDp_j(),
                scan_i = page.getScan_i(),
                scan_j = page.getScan_j(),
                offset_to_first_image = page.getOffsetToFirstImage(),
                gap_between_images = page.getGapBetweenImages(),
                little_endian = page.getLittleEndian(),
                rotate_90 = page.getRotate90(),
                is_flipped = page.getIsFlip(),
            )

            importer.loadData()
            
        elif mode == 4:
            # .mat file 
            pass # TODO
            
        elif mode == 5:
            # .mat file sequences 
            pass 
        
        elif mode == 6:
            # .npy/.npz file
            importer = ImporterNumpy(new_name, parent_path)
            page: WidgetImportNumpy 
            importer.setReadParameters(
                file_path = page.getFilePath(),
                npz_data_name = page.getNpzKey(), 
            )
            importer.loadData()
            
            
        
        elif mode == 7:
            # .npy file sequences 
            pass 
        
        elif mode == 8:
            # .dm4 file 
            pass 
        
        elif mode == 9:
            # from other h5 file 
            pass 
            
        
        

class ActionImportImage(ActionEditBase):
    """
    导入图像的 Action。

    Action to import images.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Import Image')
        self.triggered.connect(lambda: self.importImage(self))

    @property
    def task_manager(self):
        global qApp
        return qApp.task_manager

    @failLogging
    def importImage(self):
        """
        Open a dialog to choose an image to load.
        """
        if self._treeview is not None:
            self.setItemPathFromIndex(self._treeview.currentIndex())
        dialog_import = DialogImportImage()
        if self.item_path:
            dialog_import.setParentPath(self.item_path)
        dialog_code = dialog_import.exec()
        if not dialog_code == dialog_import.Accepted:
            return 
        new_name = dialog_import.getNewName()
        parent_path = dialog_import.getParentPath()
        mode = dialog_import.getImportMode()

        if mode == 0:
            tiff_path = dialog_import.getFilePath()
            self.task = TaskLoadTiff(tiff_path, parent_path, new_name)
            self.task_manager.addTask(self.task)

        # page = dialog_import.getPage(mode)





# class ActionOpenWith(ActionEditBase):
#     """
#     尝试以某种方式打开数据集的 Action。

#     Action to open Dataset by some method.
#     """
#     def __init__(self, parent: QObject = None):
#         super().__init__(parent)
#         self.setText('Open With...')
#         self.triggered.connect(lambda: self.openWith(self))

#     @property
#     def tabview_manager(self):
#         global qApp
#         return qApp.tabview_manager

#     @failLogging
#     def openWith(self):
#         """
#         Try to open the Dataset, by a method appointed by the user.
#         """
#         if self._treeview is not None:
#             self.setItemPathFromIndex(self._treeview.currentIndex())
#         pass 

        


