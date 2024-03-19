# -*- coding: utf-8 -*-

"""
*--------------------------- DialogChooseItem.py -----------------------------*
在 h5 文件中选取 Item 的对话框。

作者：          胡一鸣
创建时间：      2022年3月2日

The dialog to choose items in the h5 file.

author:             Hu Yiming
date:               Mar 2, 2022
*--------------------------- DialogChooseItem.py -----------------------------*
"""

from PySide6.QtWidgets import QDialog, QWidget 

from ui import uiDialogHDFChooseItem
from Constants import HDFType

class DialogHDFChoose(QDialog):
    """
    用于选取 Group 或者 Data 的对话框。

    Dialog to choose group or data.
    """
    def __init__(self, parent: QWidget = None, only_group: bool = False):
        super().__init__(parent)
        self.ui = uiDialogHDFChooseItem.Ui_Dialog()
        self.ui.setupUi(self)

        global qApp
        self._hdf_handler = qApp.hdf_handler

        self._only_group = only_group
        
        if self.only_group:
            self.setWindowTitle('Choose a Group')
        else:
            self.setWindowTitle('Choose an Item')

        self.ui.widget_viewer.ui.treeView_HDF.clicked.connect(
            self.setCurrentPath
        )

        self.ui.pushButton_ok.clicked.connect(self.accept)
        self.ui.pushButton_cancel.clicked.connect(self.reject)

    @property
    def only_group(self) -> bool:
        return self._only_group

    @only_group.setter
    def only_group(self, is_only_group):
        self._only_group = bool(is_only_group)

    def setCurrentPath(self):
        """
        Set the path according to the chosen index.

        If the dialog is set to groups-only, the path will be a group 
        automatically.
        """
        model = self.ui.widget_viewer.ui.treeView_HDF.model()
        index = self.ui.widget_viewer.ui.treeView_HDF.currentIndex()
        if self.only_group:
            hdf_type = index.data(role = model.DataRoles.HDFTypeRole)
            if hdf_type in (HDFType.Group, HDFType.Root):
                current_path = index.data(
                    role = model.DataRoles.PathRole)
            else:
                current_path = index.parent().data(
                    role = model.DataRoles.PathRole)
        else:
            current_path = index.data(role = model.DataRoles.PathRole)

        self.ui.lineEdit_parent_path.setText(current_path)
        
    def getCurrentPath(self) -> str:
        """
        returns:
            (str) the current chosen path.
        """
        return self.ui.lineEdit_parent_path.text()