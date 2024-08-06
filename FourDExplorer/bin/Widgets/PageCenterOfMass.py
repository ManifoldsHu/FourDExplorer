# -*- coding: utf-8 -*-

"""
*--------------------------- PageCenterOfMass.py -----------------------------*
用于计算 4D-STEM 质心成像的页面。

部件内容：
    - WidgetPlotDP 用于使用 matplotlib 来显示衍射图样
    - WidgetMaskCircle 用于绘制圆形区域
    - WidgetMaskRing 用于绘制环形区域
    - WidgetMaskWedge 用于绘制扇形区域
    - WidgetMaskRectangle 用于绘制矩形区域
    - WidgetMaskSegment2 用于绘制2分段环形区域
    - WidgetMaskSegment4 用于绘制4分段环形区域
    - WidgetMaskSegment6 用于绘制6分段环形区域
    - WidgetMaskSegment8 用于绘制8分段环形区域

提升部件：
    - 提升类名 PageCenterOfMass
    - 头文件 bin.Widgets.PageCenterOfMass

作者:           胡一鸣
创建日期:       2022年5月18日

The GUI page to calculate Center Of Mass images from 4D-STEM.

Contents:
    - WidgetPlotDP, to view the diffraction patterns
    - WidgetMaskCircle, to draw circular region
    - WidgetMaskRing, to draw annular region
    - WidgetMaskWedge, to draw fan-shaped region
    - WidgetMaskRectangle, to draw rectangular region
    - WidgetMaskSegment2, to draw 2-segmented annular regions
    - WidgetMaskSegment4, to draw 4-segmented annular regions
    - WidgetMaskSegment6, to draw 6-segmented annular regions
    - WidgetMaskSegment8, to draw 8-segmented annular regions

Promoted Widget:
    - name of widget class: PageCenterOfMass
    - header file: bin.Widget.PageCenterOfMass

author:         Hu Yiming
date:           May 18, 2022
*--------------------------- PageCenterOfMass.py -----------------------------*
"""

from PySide6.QtWidgets import QWidget, QDialog
from PySide6.QtGui import QRegularExpressionValidator

from bin.HDFManager import HDFGroupNode, HDFHandler, reValidHDFName
from bin.Widgets.PageVirtualImage import PageVirtualImage
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from lib.TaskReconstruction import TaskCenterOfMass
from ui import uiDialogCreateCoM

class PageCenterOfMass(PageVirtualImage):
    """
    进行虚拟成像的部件类。

    Ui 文件地址：ROOTPATH/ui/uiPageVirtualImage

    Widget to calculate Virtual Image.

    The path of the ui file: ROOTPATH/ui/uiPageVirtualImage

    attributes:
        hdf_handler: (HDFHandler) The handler to manage the hdf file and the
            objects inside it.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setWindowTitle('Center Of Mass')
        self.setToolTip(
            'Generate differential phase contrast (DPC) images by calculating '
            '\nCenter of Mass (CoM) distribution of the 4D-STEM dataset.'
        )
        self.ui.pushButton_start.setText(
            'Start to Calculate Center of Mass (CoM)'
        )
        

    def startCalculation(self):
        """
        Start calculate Center Of Mass of 4D-STEM.

        When the button 'Start Calculation' is clicked, this function will be 
        called. 
        """
        dialog_create = DialogCreateCoM(self)
        dialog_create.setParentPath(self.data_path)
        dialog_code = dialog_create.exec()
        if not dialog_code == dialog_create.Accepted:
            return 
        
        parent_path = dialog_create.getParentPath()
        calc_dict = dialog_create.getCalcDict()

        names = {
            'CoM': dialog_create.getCoMName(),
            'CoMi': dialog_create.getCoMiName(),
            'CoMj': dialog_create.getCoMjName(),
            'dCoM': dialog_create.getDCoMName(),
            'iCoM': dialog_create.getICoMName(),
        }

        metas = {
            'CoM': self._generateCoMMeta(),
            'CoMi': self._generateCoMiMeta(),
            'CoMj': self._generateCoMjMeta(),
            'dCoM': self._generateDCoMMeta(),
            'iCoM': self._generateICoMMeta(),
        }

        is_com_inverted = dialog_create.getIsCoMInverted()
        is_mean_set_to_zero = dialog_create.getIsMeanSetToZero()
        for com_mode, meta in metas.items():
            meta['com_inverted'] = is_com_inverted
            meta['com_mean_set_to_zero'] = is_mean_set_to_zero

        mask = self.calcMask()
        self.task = TaskCenterOfMass(
            item_path = self.data_path,
            image_parent_path = parent_path,
            calc_dict = calc_dict,
            names_dict = names,
            metas_dict = metas,
            mask = mask,
            is_com_inverted = is_com_inverted,
            is_mean_set_to_zero = is_mean_set_to_zero,
        )

        self.task_manager.addTask(self.task)

    def _generateCoMMeta(self) -> dict:
        """
        Generate metadata for center of mass vector field.
        """
        meta = self._generateImageMeta()
        
        meta['/General/notes'] = 'Center of Mass' 
        return meta 
        
        # meta['image_mode'] = 'Center of Mass'
        # attrs = self.data_object.attrs
        
        # if 'dp_pixel_size' in attrs:
        #     meta['com_unit_per_value_i'] = attrs['dp_pixel_size']
        #     meta['com_unit_per_value_j'] = attrs['dp_pixel_size']
        #     meta['com_unit'] = 'rad'
        # else:
        #     if 'dp_pixel_size_i' in attrs:
        #         meta['com_unit_per_value_i'] = attrs['dp_pixel_size_i']
        #         meta['com_unit'] = 'rad'
        #     if 'dp_pixel_size_j' in attrs:
        #         meta['com_unit_per_value_j'] = attrs['dp_pixel_size_j']
        #         meta['com_unit'] = 'rad'
        
        # return meta 

    def _generateCoMiMeta(self) -> dict:
        """
        Generate metadata for vertical direction component of CoM.
        """
        meta = self._generateImageMeta()
        meta['/General/notes'] = 'Center of Mass (i-component)'
         
        # meta['image_mode'] = 'Center of Mass (i-component)'
        # attrs = self.data_object.attrs 
        # if 'dp_pixel_size' in attrs:
        #     meta['com_unit_per_value_i'] = attrs['dp_pixel_size']
        #     meta['com_unit'] = 'rad'
        # elif 'dp_pixel_size_i' in attrs:
        #     meta['com_unit_per_value_i'] = attrs['dp_pixel_size_i']
        #     meta['com_unit'] = 'rad'
        return meta

    def _generateCoMjMeta(self) -> dict:
        """
        Generate metadata for horizontal direction component of CoM.
        """
        meta = self._generateImageMeta()
        meta['/General/notes'] = 'Center of Mass (j-component)'
        
        # meta['image_mode'] = 'Center of Mass (j-component)'
        # attrs = self.data_object.attrs 
        # if 'dp_pixel_size' in attrs:
        #     meta['com_unit_per_value_j'] = attrs['dp_pixel_size']
        #     meta['com_unit'] = 'rad'
        # elif 'dp_pixel_size_j' in attrs:
        #     meta['com_unit_per_value_j'] = attrs['dp_pixel_size_j']
        #     meta['com_unit'] = 'rad'
        return meta

    def _generateDCoMMeta(self) -> dict:
        """
        Generate metadata for differentiated center of mass.
        """
        meta = self._generateImageMeta()
        meta['/General/notes'] = 'Differentiated Center of Mass'
        return meta 
    
    def _generateICoMMeta(self) -> dict:
        """
        Generate metadata for integrated center of mass.
        """
        meta = self._generateImageMeta()
        meta['/General/notes'] = 'Integrated Center of Mass'
        return meta
    

class DialogCreateCoM(QDialog):
    """
    用于选取计算质心映射的模式的对话框。

    The Dialog to choose modes when calculating CoM.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogCreateCoM.Ui_Dialog()
        self.ui.setupUi(self)

        self._initUi()
        self._validateNewName()
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler

    def _initUi(self):
        """
        Initialize Uis.
        """
        self.ui.pushButton_browse.clicked.connect(self.browseParent)
        self.ui.pushButton_ok.clicked.connect(self.accept)
        self.ui.pushButton_cancel.clicked.connect(self.reject)

        self.ui.checkBox_normalize.setChecked(True)
        self.ui.checkBox_normalize.setToolTip(
            'The vector field result will '
            'be subtracted from the mean vector'
        )

        self.ui.radioButton_use_CoM.setToolTip(
            'The vector field will follow the same direction as the center\n'
            'of mass of the 4D-STEM dataset. In other words, the direction\n'
            'that electron beam is deflected.'
        )

        self.ui.radioButton_use_electric.setToolTip(
            'The vector field will follow the direction of the projection \n'
            'electric field. It is inverted from the center of mass, due to\n'
            'negative charge of the electron beam.'
        )
        self.ui.radioButton_use_electric.setChecked(True)

        self.ui.checkBox_CoM.setChecked(True)
        self.ui.checkBox_CoM.stateChanged.connect(self._checkCoM)
        self.ui.checkBox_CoMi.setChecked(True)
        self.ui.checkBox_CoMi.stateChanged.connect(self._checkCoMi)
        self.ui.checkBox_CoMj.setChecked(True)
        self.ui.checkBox_CoMj.stateChanged.connect(self._checkCoMj)
        self.ui.checkBox_dCoM.setChecked(True)
        self.ui.checkBox_dCoM.stateChanged.connect(self._checkDCoM)
        self.ui.checkBox_iCoM.setChecked(True)
        self.ui.checkBox_iCoM.stateChanged.connect(self._checkICoM)

        self.ui.lineEdit_CoM.setEnabled(True)
        self.ui.lineEdit_CoM.setText('CoM')
        self.ui.lineEdit_CoMi.setEnabled(True)
        self.ui.lineEdit_CoMi.setText('CoMi')
        self.ui.lineEdit_CoMj.setEnabled(True)
        self.ui.lineEdit_CoMj.setText('CoMj')
        self.ui.lineEdit_dCoM.setEnabled(True)
        self.ui.lineEdit_dCoM.setText('dCoM')
        self.ui.lineEdit_iCoM.setEnabled(True)
        self.ui.lineEdit_iCoM.setText('iCoM')

        
        
    
    def browseParent(self) -> bool:
        """
        Open a dialog to browse a group to be parent.

        returns:
            (bool) whether a new path is set.
        """
        dialog_browse = DialogHDFChoose(self, only_group = True)
        dialog_code = dialog_browse.exec()
        if dialog_code == dialog_browse.Accepted:
            current_path = dialog_browse.getCurrentPath()
            if current_path:
                self.ui.lineEdit_parent_path.setText(current_path)
            return True 
        else:
            return False 

    def setParentPath(self, item_path: str):
        """
        Set the parent group's path where created images will locate.

        arguments:
            item_path: (str)
        """
        if not isinstance(item_path, str):
            raise TypeError('item_path must be a str, not '
                '{0}'.format(type(item_path).__name__))
        
        node = self.hdf_handler.getNode(item_path)
        if not isinstance(node, HDFGroupNode):
            self.ui.lineEdit_parent_path.setText(node.parent.path)
        else:
            self.ui.lineEdit_parent_path.setText(item_path)

    def getParentPath(self) -> str:
        """
        Return the parent group's path where imported dataset will locate.

        returns:
            (str)
        """
        return self.ui.lineEdit_parent_path.text()

    def _validateNewName(self):
        """
        Set validators by regular expression for the names.
        """
        self.re_validator = QRegularExpressionValidator()
        self.re_validator.setRegularExpression(reValidHDFName.pattern)

        self.ui.lineEdit_CoM.setValidator(self.re_validator)
        self.ui.lineEdit_CoMi.setValidator(self.re_validator)
        self.ui.lineEdit_CoMj.setValidator(self.re_validator)
        self.ui.lineEdit_dCoM.setValidator(self.re_validator)
        self.ui.lineEdit_iCoM.setValidator(self.re_validator)
        
    def _checkCoM(self):
        self.ui.lineEdit_CoM.setEnabled(self.ui.checkBox_CoM.isChecked())

    def _checkCoMi(self):
        self.ui.lineEdit_CoMi.setEnabled(self.ui.checkBox_CoMi.isChecked())

    def _checkCoMj(self):
        self.ui.lineEdit_CoMj.setEnabled(self.ui.checkBox_CoMj.isChecked())

    def _checkDCoM(self):
        self.ui.lineEdit_dCoM.setEnabled(self.ui.checkBox_dCoM.isChecked())

    def _checkICoM(self):
        self.ui.lineEdit_iCoM.setEnabled(self.ui.checkBox_iCoM.isChecked())

    def _addNameExt(self, name: str, ext: str = 'img'):
        """
        Add a extension to the name.

        If there has been a correct extension in name, do nothing.

        arguments:
            name: (str) the original name

            ext: (str) the extension. Should be 'img' or 'vec'.
        """
        if '.' in name:
            if name.split('.')[-1] == ext:
                return name
        return name + '.' + ext 

    def getCoMName(self) -> str:
        return self._addNameExt(self.ui.lineEdit_CoM.text(), 'vec')

    def getCoMiName(self) -> str:
        return self._addNameExt(self.ui.lineEdit_CoMi.text(), 'img')

    def getCoMjName(self) -> str:
        return self._addNameExt(self.ui.lineEdit_CoMj.text(), 'img')

    def getDCoMName(self) -> str:
        return self._addNameExt(self.ui.lineEdit_dCoM.text(), 'img')

    def getICoMName(self) -> str:
        return self._addNameExt(self.ui.lineEdit_iCoM.text(), 'img')

    def getIsMeanSetToZero(self) -> bool:
        """
        Returns whether the result vector field to be subtracted from its mean
        vector field strength. 
        """
        return self.ui.checkBox_normalize.isChecked()

    def getIsCoMInverted(self) -> bool:
        """
        Returns whether the result vector field to be inverted direction.
        """
        return self.ui.radioButton_use_electric.isChecked()

    def getCalcDict(self) -> dict:
        """
        Returns which calculating modes are selected.
        """
        calc_dict = {
            'CoM': self.ui.checkBox_CoM.isChecked(),
            'CoMi': self.ui.checkBox_CoMi.isChecked(),
            'CoMj': self.ui.checkBox_CoMj.isChecked(),
            'dCoM': self.ui.checkBox_dCoM.isChecked(),
            'iCoM': self.ui.checkBox_iCoM.isChecked(),
        }
        return calc_dict

    

