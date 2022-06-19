# -*- coding: utf-8 -*-

"""
*---------------------------- DataActions.py ---------------------------------*
针对各种 Dataset 的操作的 Action。

作者:           胡一鸣
创建日期:       2022年6月15日

This module includes actions towards Dataset.

author:         Hu Yiming
date:           Jun 15, 2022
*---------------------------- DataActions.py ---------------------------------*
"""

from logging import Logger 

from PySide6.QtCore import QObject, QModelIndex
from PySide6.QtWidgets import QMessageBox, QInputDialog, QTreeView, QWidget
from PySide6.QtGui import QAction 
from Constants import ItemDataRoles, HDFType 

from bin.Actions.EditActions import ActionEditBase, failLogging
from bin.HDFManager import HDFDataNode, HDFHandler 
from bin.UIManager import ThemeHandler
from bin.Widgets.DialogChangeDataType import DialogChangeDataType
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.Widgets.PageAlignFourDSTEM import PageAlignFourDSTEM
from bin.Widgets.PageBkgrdFourDSTEM import PageBkgrdFourDSTEM
from bin.Widgets.PageCenterOfMass import PageCenterOfMass
from bin.Widgets.PageRotateFourDSTEM import PageRotateFourDSTEM
from bin.Widgets.PageViewFourDSTEM import PageViewFourDSTEM
from bin.Widgets.PageViewImage import PageViewImage
from bin.Widgets.PageViewLine import PageViewLine
from bin.Widgets.PageViewVectorField import PageViewVectorField
from bin.Widgets.PageVirtualImage import PageVirtualImage


class ActionDataManipulateBase(ActionEditBase):
    """
    用来处理 Dataset 的 Action 的基类。

    The base class of actions for manipulating Dataset.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)

    @property
    def tabview_manager(self):
        global qApp 
        return qApp.tabview_manager

    def initIconResources(self, icon_name: str):
        """
        Initialize the resource of icons.

        arguments:
            icon_name: (str) the name of icon.
        """
        _path = ':/HDFItem/resources/icons/' + icon_name
        icon = self.theme_handler.iconProvider(_path)
        self._icon_name = icon_name 
        self.setIcon(icon)


class ActionOpenData(ActionDataManipulateBase):
    """
    用于展示 Dataset 的 Action。

    Action to open (show) dataset.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Open')
        self.triggered.connect(lambda: self.openData(self))

    @failLogging 
    def openData(self):
        """
        Try to open the data.
        """
        if self._treeview is not None:
            self.setItemPathFromIndex(self._treeview.currentIndex())
        if self.item_path == '':
            dialog_browse = DialogHDFChoose()
            dialog_browse.setWindowTitle('Choose a dataset to show')
            dialog_code = dialog_browse.exec()
            if dialog_code == dialog_browse.Accepted:
                item_path = dialog_browse.getCurrentPath()
                self.setItemPath(item_path)
            else:
                return 
        
        hdf_type = self.getOpenAsType()
        if hdf_type is None:
            return 
        page = self.openAs(hdf_type)
        self.tabview_manager.openTab(page)

    def getOpenAsType(self) -> HDFType:
        """
        Try to appoint a method to open the target dataset.

        returns:
            (HDFType or None)
        """
        node = self.hdf_handler.getNode(self.item_path)
        if not isinstance(node, HDFDataNode):
            raise TypeError('Only Dataset object can be showed.')
        elif node.hdf_type == HDFType.Data:
            dialog_open_as = DialogChangeDataType()
            dialog_open_as.setWindowTitle('Open As...')
            dialog_open_code = dialog_open_as.exec()
            if dialog_open_code != dialog_open_as.Accepted:
                return None
            hdf_type = dialog_open_as.getTargetType()
            if hdf_type == HDFType.Data:
                raise RuntimeError('Must appoint a method to show Dataset.')
        else:
            hdf_type = node.hdf_type
        return hdf_type

    def openAs(self, hdf_type: HDFType) -> QWidget:
        """
        Use the corresponding method to open the Dataset.

        arguments:
            hdf_type: (HDFType)
        """
        if hdf_type == HDFType.Image:
            page = PageViewImage()
            page.setImage(self.item_path)
        elif hdf_type == HDFType.FourDSTEM:
            page = PageViewFourDSTEM()
            page.setFourDSTEM(self.item_path)
        elif hdf_type == HDFType.VectorField:
            page = PageViewVectorField()
            page.setVectorField(self.item_path)
        elif hdf_type == HDFType.Line:
            page = PageViewLine()
            page.addLine(self.item_path, update_title = True)
        else:
            raise TypeError('Unknown Dataset type.')
        return page 
        

class ActionOpenDataAs(ActionOpenData):
    """
    Open a dialog to choose method to show the Dataset.
    """    
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Open As...')
        
    def getOpenAsType(self) -> HDFType:
        """
        Force to open a dialog to choose which method to open.
        """
        node = self.hdf_handler.getNode(self.item_path)
        if not isinstance(node, HDFDataNode):
            raise TypeError('Only Dataset object can be showed.')
        dialog_open_as = DialogChangeDataType()
        dialog_open_as.setWindowTitle('Open As...')
        dialog_open_code = dialog_open_as.exec()
        if dialog_open_code != dialog_open_as.Accepted:
            return None
        hdf_type = dialog_open_as.getTargetType()
        if hdf_type == HDFType.Data:
            raise RuntimeError('Must appoint a method to show Dataset.')
        return hdf_type 


class ActionOpenLine(ActionOpenData):
    """
    指定打开线的数据。

    Try opening a line data.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Open Line')
        self.initIconResources('line')

    def openAs(self, hdf_type: HDFType = None) -> PageViewLine:
        """
        Use the line viewing method to open the line.

        arguments:
            hdf_type: (HDFType) (does not work)
        """
        page = PageViewLine()
        if self.item_path not in ('', '/'):
            page.addLine(self.item_path)
        return page


class ActionOpenImage(ActionOpenData):
    """
    指定使用打开二维图像的方法打开数据。

    Try opening an image.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Open Image')
        self.initIconResources('picture')

    def openAs(self, hdf_type: HDFType = None) -> PageViewImage:
        """
        Use the image viewing method to open the data.

        arguments:
            hdf_type: (HDFType) (does not work)
        """
        page = PageViewImage()
        if self.item_path not in ('', '/'):
            page.setImage(self.item_path)
        return page 


class ActionOpenVectorField(ActionOpenData):
    """
    指定使用打开矢量场的方法来打开数据。

    Try opening a vector field.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Open Vector Field')
        self.initIconResources('particle_tracking')

    def openAs(self, hdf_type: HDFType = None) -> PageViewVectorField:
        """
        Use the vector field method to open the data.

        arguments:
            hdf_type: (HDFType) (does not work)
        """
        page = PageViewVectorField()
        if self.item_path not in ('', '/'):
            page.setVectorField(self.item_path)
        return page 


class ActionOpenFourDSTEM(ActionOpenData):
    """
    指定使用打开 4D-STEM 数据集的方法来打开数据。

    Try opening a 4D-STEM dataset.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Open 4D-STEM')
        self.initIconResources('cube')

    def openAs(self, hdf_type: HDFType = None) -> PageViewFourDSTEM:
        """
        Use the 4D-STEM method to open the data.

        arguments:
            hdf_type: (HDFType) (does not work)
        """
        page = PageViewFourDSTEM()
        if self.item_path not in ('', '/'):
            page.setFourDSTEM(self.item_path)
        return page 
