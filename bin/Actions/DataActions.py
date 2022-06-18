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


class ActionVirtualImage(ActionOpenData):
    """
    计算 4D-STEM 虚拟成像的 Action。

    Action to calculate 4D-STEM virtual images.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Virtual Image')

    def openAs(self, hdf_type: HDFType = None) -> PageVirtualImage:
        """
        Use the virtual image method to open the Dataset.

        arguments:
            hdf_type: (HDFType) (does not work)
        """
        page = PageVirtualImage()
        page.setFourDSTEM(self.item_path)
        return page  


class ActionCenterOfMass(ActionOpenData):
    """
    计算 4D-STEM 质心法差分相位衬度的 Action。

    Action to calculate differentiated phase contrast (CoM).
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Center of Mass')

    def openAs(self, hdf_type: HDFType = None) -> PageCenterOfMass:
        """
        Use the center of mass method to open the Dataset.

        arguments:
            hdf_type: (HDFType) (does not work)
        """
        page = PageVirtualImage()
        page.setFourDSTEM(self.item_path)
        return page 


class ActionAlign(ActionOpenData):
    """
    对 4D-STEM 数据集进行平移合轴的 Action。

    Action to align 4D-STEM dataset.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Diffraction Alignment')

    def openAs(self, hdf_type: HDFType = None) -> PageAlignFourDSTEM:
        """
        Use the diffraction alignment method to open the Dataset.

        arguments:
            hdf_type: (HDFType) 
        """
        page = PageAlignFourDSTEM()
        page.setFourDSTEM(self.item_path)
        return page 


class ActionBackground(ActionOpenData):
    """
    对 4D-STEM 数据进行抠背底操作的 Action。

    Action to subtract 4D-STEM's background.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Background Subtraction')

    def openAs(self, hdf_type: HDFType = None) -> PageBkgrdFourDSTEM:
        """
        Use the background subtraction method to open the Dataset.

        arguments:
            hdf_type: (HDFType)
        """
        page = PageBkgrdFourDSTEM()
        page.setFourDSTEM(self.item_path)
        return page 


class ActionRotate(ActionOpenData):
    """
    对 4D-STEM 数据进行旋转操作的 Action。

    Action to rotate 4D-STEM's diffraction pattern.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Diffraction Rotation')

    def openAs(self, hdf_type: HDFType = None) -> PageRotateFourDSTEM:
        """
        Use the diffraction rotation method to open the Dataset.

        arguments:
            hdf_type: (HDFType)
        """
        page = PageRotateFourDSTEM()
        page.setFourDSTEM(self.item_path)
        return page 
