# -*- coding: utf-8 -*-

"""
*------------------------ DialogImportFourDSTEM.py ---------------------------*
用于导入 4D-STEM 数据的对话框。

部件内容：
    - WidgetImportEMPAD 用于导入 EMPAD 所产生的 4D-STEM 数据
    - WidgetImportEMPAD_NJU 用于导入南京大学 EMPAD 所产生的 4D-STEM 数据
    - WidgetImportRaw 用于导入二进制文件中存储的 4D-STEM 数据

作者:           胡一鸣
创建日期:       2022年5月5日

The dialog to import 4D-STEM dataset.

Contents:
    - WidgetImportEMPAD, to import 4D-STEM dataset produced by EMPAD
    - WidgetImportEMPAD_NJU, to import 4D-STEM dataset produced by EMPAD with 
        software version v0.51 that installed in Nanjing University.
    - WidgetImportRaw, to import 4D-STEM dataset stored in binary file.

author:         Hu Yiming
date:           May 5, 2022
*------------------------ DialogImportFourDSTEM.py ---------------------------*
"""

from logging import Logger

from PySide6.QtWidgets import QDialog, QWidget
from PySide6.QtGui import QRegularExpressionValidator

from bin.HDFManager import reValidHDFName, HDFHandler, HDFGroupNode
from bin.Widgets.DialogChooseItem import DialogHDFChoose  
from ui import uiDialogImportFourDSTEM


class DialogImportFourDSTEM(QDialog):
    """
    导入 4D-STEM 数据的对话框。包含以下功能：
        - 导入 EMPAD 所产生的 4D-STEM 数据
        - 导入二进制文件中存储的 4D-STEM 数据

    Ui 文件地址: ROOTPATH/ui/uiDialogImportFourDSTEM
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogImportFourDSTEM.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.comboBox_mode.setCurrentIndex(0)
        self.ui.comboBox_mode.currentIndexChanged.connect(self._changeMode)
        
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.pushButton_browse_parent.clicked.connect(self.browseParent)
        self.ui.lineEdit_parent_path.setReadOnly(True)

        self.ui.pushButton_ok.clicked.connect(self.accept)
        self.ui.pushButton_cancel.clicked.connect(self.reject)

        self.ui.lineEdit_name.setText('Untitled')
        self._validateNewName()
        
        self._hideOptions()     # some importer is not completed yet

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler

    def _changeMode(self, index: int):
        """
        Slots when import mode is changed.
        
        NOTE: 4 and 5 is not completed yet, and hence they are removed

        arguments:
            index: (int)    0   'EMPAD v1.0'
                            1   'EMPAD v0.51 (for NJU)'
                            2   'MerlinEM Medipix3 (.mib)'
                            3   'General Raw Data (Binary)'
                            4   'MATLAB 4D Matrix (.mat)'
                            5   'MATLAB Matrix Sequence'
                            6   'Numpy 4D Array (.npy)'
                            7   'Numpy Array Sequence'
                            8   'Digital Micrograph (.dm4)'
                            9   'Other HDF5 Dataset (.h5)'
        """
        self.ui.stackedWidget.setCurrentIndex(index)
    
    def _hideOptions(self):
        """
        Hide options for incomplete importers.

        This method removes the options for MATLAB 4D Matrix (.mat) and MATLAB 
        Matrix Sequence from the combo box and the corresponding widgets from 
        the stacked widget.
        
        TODO
        """
        self.ui.comboBox_mode.removeItem(5)
        self.ui.comboBox_mode.removeItem(4)
        self.ui.stackedWidget.removeWidget(self.ui.stackedWidget.widget(5))
        self.ui.stackedWidget.removeWidget(self.ui.stackedWidget.widget(4))
    
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
            self.ui.lineEdit_parent_path.setText(current_path)
            return True 
        else:
            return False 

    def setParentPath(self, item_path: str):
        """
        Set the parent group's path where imported dataset will locate.

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

    def getImportMode(self) -> int:
        """
        The import mode selected.

        returns:
            (int)   0   'EMPAD v1.0'
                    1   'EMPAD v0.51 (for NJU)'
                    2   'Medipix'
                    3   'General Raw Data (Binary)'
                    4   'MATLAB 4D Matrix (.mat)'
                    5   'MATLAB Matrix Sequence'
                    6   'Numpy 4D Array (.npy)'
                    7   'Numpy Array Sequence'
                    8   'Digital Micrograph (.dm4)'
        """
        return self.ui.comboBox_mode.currentIndex()

    def getNewName(self) -> str:
        """
        returns the new name of the imported dataset.

        Will add '.4dstem' automatically as the extension.
        """
        name = self.ui.lineEdit_name.text()
        if '.' in name:
            if name.split('.')[-1] == '4dstem':
                return name 
        return name + '.4dstem'

    def _validateNewName(self):
        """
        Set validator by regular expressioin for the name.
        """
        self.re_validator = QRegularExpressionValidator()
        self.re_validator.setRegularExpression(reValidHDFName.pattern)
        self.ui.lineEdit_name.setValidator(self.re_validator)

    def getPage(self, index: int) -> QWidget:
        """
        Returns the page according to the selected import mode.
        """
        return self.ui.stackedWidget.widget(index)


