# -*- coding: utf-8 -*-

"""
*-------------------------- DialogImportImage.py -----------------------------*
用于导入二维图像的对话框。

作者:           胡一鸣
创建日期:       2022年6月18日

The dialog to import gray images.

author:         Hu Yiming
date:           Jun 18, 2022
*-------------------------- DialogImportImage.py -----------------------------*
"""

from logging import Logger 
import os

from PySide6.QtWidgets import QDialog, QWidget, QFileDialog
from PySide6.QtGui import QRegularExpressionValidator

from bin.HDFManager import reValidHDFName, HDFHandler, HDFGroupNode
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from ui import uiDialogImportImage

class DialogImportImage(QDialog):
    """
    导入图像的对话框。包含以下功能：
        - 导入 TIFF

    UI 文件地址：ROOTPATH/ui/uiDialogImportImage

    Dialog to import image. It includes following methods:
        - import TIFF

    UI file path: ROOTPATH/ui/uiDialogImportImage
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogImportImage.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.comboBox_mode.setCurrentIndex(0)
        
        self.ui.lineEdit_parent_path.setReadOnly(True)
        self.ui.pushButton_browse_parent.clicked.connect(self.browseParent)

        self.ui.pushButton_ok.clicked.connect(self.accept)
        self.ui.pushButton_cancel.clicked.connect(self.reject)

        self.ui.lineEdit_name.setText('Untitled')
        self._validateNewName()

        self.ui.pushButton_browse_file.clicked.connect(self._chooseFile)

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler 

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
            (int)   0   'TIFF'
        """
        return self.ui.comboBox_mode.currentIndex()

    def getNewName(self) -> str:
        """
        returns the new name of the imported dataset.

        Will add '.img' automatically as the extension.
        """
        name = self.ui.lineEdit_name.text()
        if '.' in name:
            if name.split('.')[-1] == 'img':
                return name 
        return name + '.img'

    def _validateNewName(self):
        """
        Set validator by regular expressioin for the name.
        """
        self.re_validator = QRegularExpressionValidator()
        self.re_validator.setRegularExpression(reValidHDFName.pattern)
        self.ui.lineEdit_name.setValidator(self.re_validator)

    def _chooseFile(self):
        """
        Open a dialog to choose which file to be imported.
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Open TIFF File',
            './',
            'TIFF Image (*.tif *.tiff);;All Files(*)'
        )
        if file_path == '':
            return 

        file_path = os.path.abspath(file_path)
        self.ui.lineEdit_image_path.setText(file_path)

    def getFilePath(self) -> str:
        return self.ui.lineEdit_image_path.text()
        

