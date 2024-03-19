# -*- coding: utf-8 -*-

"""
*------------------------ DialogSaveFourDSTEM.py -----------------------------*
用于保存计算所得 4D-STEM 数据集的对话框。提供覆盖保存选项。

作者:           胡一鸣
创建日期:       2022年5月31日

Dialog to save the calculated 4D-STEM dataset. Providing in-place mode.

author:         Hu Yiming
date:           May 31, 2022
*------------------------ DialogSaveFourDSTEM.py -----------------------------*
"""

from tkinter import dialog
from PySide6.QtWidgets import QDialog, QWidget, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator

from bin.HDFManager import HDFHandler, HDFGroupNode, reValidHDFName
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from ui import uiDialogCreateFourDSTEM

class DialogSaveFourDSTEM(QDialog):
    """
    选择在 HDF 文件中保存应用了平移之后的 4D-STEM 数据集的对话框。

    Dialog to choose where to save the calibrated 4D-STEM dataset.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogCreateFourDSTEM.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.lineEdit_name.setText('Untitled')
        self._validateNewName()

        self.ui.checkBox_inplace.stateChanged.connect(
            self._changePathInputState
        )

        self.ui.pushButton_ok.clicked.connect(self.ok)
        self.ui.pushButton_cancel.clicked.connect(self.reject)

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

    def getIsInplace(self) -> bool:
        return self.ui.checkBox_inplace.isChecked()

    def _changePathInputState(self):
        """
        Change the state of the path input widgets.

        If the modification is inplace, those widgets will be unusable.
        """
        _inplace = self.ui.checkBox_inplace.isChecked()
        self.ui.lineEdit_name.setDisabled(_inplace)
        self.ui.lineEdit_parent_path.setDisabled(_inplace)
        self.ui.pushButton_browse.setDisabled(_inplace)

    def ok(self):
        """
        When Ok button is pushed, this method is called.
        """
        if self.getIsInplace():
            dialog_code = QMessageBox.warning(
                self, 
                'In-place Warning',
                'In-place modification will change your 4D-STEM\n'
                'dataset forever. MAKE SURE you have a replica\n'
                'of current 4D-STEM dataset.\n'
                'Continue?',
                QMessageBox.Ok,
                QMessageBox.Cancel,
            )
            if dialog_code != QMessageBox.Ok:
                return 
        self.accept()

