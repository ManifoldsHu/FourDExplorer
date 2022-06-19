# -*- coding: utf-8 -*-

"""
*-------------------------- FourDSTEMActions.py ------------------------------*
针对 4D-STEM 的操作的 Action。

作者:           胡一鸣
创建日期:       2022年6月19日

This module includes actions towards 4D-STEM datasets.

author:         Hu Yiming
date:           Jun 19, 2022
*-------------------------- FourDSTEMActions.py ------------------------------*
"""

from PySide6.QtCore import QObject 
from PySide6.QtWidgets import QWidget 

from bin.Actions.EditActions import failLogging
from bin.Actions.DataActions import ActionOpenFourDSTEM
from bin.Actions.DataActions import ActionOpenData
from bin.HDFManager import HDFType
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.Widgets.PageAlignFourDSTEM import PageAlignFourDSTEM
from bin.Widgets.PageBkgrdFourDSTEM import PageBkgrdFourDSTEM
from bin.Widgets.PageCenterOfMass import PageCenterOfMass
from bin.Widgets.PageRotateFourDSTEM import PageRotateFourDSTEM
from bin.Widgets.PageViewFourDSTEM import PageViewFourDSTEM
from bin.Widgets.PageVirtualImage import PageVirtualImage

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




