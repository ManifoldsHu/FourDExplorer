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
from bin.Actions.EditActions import ActionEditBase
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
from bin.Widgets.DialogEditParaFourDSTEM import DialogEditParaFourDSTEM

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
        page = PageCenterOfMass()
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


class ActionPlotCTF(ActionOpenData):
    """
    绘制 4D-STEM 数据集相同参数的相应 CTF 曲线的页面。
    
    通过这个页面打开时，会使用其相应的 4D-STEM 数据集的实验参数作为计算 CTF 的参数。
    如果不想预先给定这些参数，而是让用户手动设置的话，使用 ActionPlotCTFManual
    
    Action to plot CTF curves of the same parameters of 4D-STEM data.
    
    When opening this page, the parameters of the 4D-STEM data will be used as
    parameters to calculate CTF. If you want to manually set the parameters, use
    ActionPlotCTFManual instead.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Plot CTF')
        
    # def openAs(self, hdf_type: HDFType = None) -> 'PagePlotCTF':
    #     """
    #     Use the plot CTF page to open the Dataset.
        
    #     arguments:
    #         hdf_type: (HDFType)
    #     """
    #     page = PagePlotCTF()
    #     page.setFourDSTEM(self.item_path)
    #     return page 


class ActionEditParam(ActionEditBase):
    """
    引导用户编辑 4D-STEM Dataset 的属性的对话框。
    
    Action to guide user to edit the parameters of 4D-STEM dataset.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText("Edit 4D-STEM Parameters")
        self.initIconResources('attributes')
        self.triggered.connect(lambda: self.viewParaFourDSTEM(self))
        
    @failLogging
    def viewParaFourDSTEM(self):
        """
        Shows a dialog to view attributes of 4D-STEM dataset.
        """
        if self._treeview is not None:
            self.setItemPathFromIndex(self._treeview.currentIndex())
        
        if not self._item_path:
            dialog_choose_dataset = DialogHDFChoose()
            dialog_choose_dataset.setWindowTitle('Choose a 4D-STEM dataset')
            dialog_code = dialog_choose_dataset.exec()
            if dialog_code == dialog_choose_dataset.Accepted:
                self.setItemPath(dialog_choose_dataset.getCurrentPath())
            else:
                return

        # Here we must bind the dialog to the main window, in case it is 
        # garbage collected.
        global qApp 
        dialog_para = DialogEditParaFourDSTEM(qApp.main_window)
        dialog_para.setFourDSTEM(self.item_path)
        dialog_para.show()
        
