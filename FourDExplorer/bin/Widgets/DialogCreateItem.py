# -*- coding: utf-8 -*-

"""
*--------------------------- DialogCreateItem.py -----------------------------*
在 h5 文件中创建 Item 的对话框。

作者：          胡一鸣
创建时间：      2022年3月2日


The dialog to create items in the h5 file.

author:             Hu Yiming
date:               Mar 2, 2022
*--------------------------- DialogCreateItem.py -----------------------------*
"""

from tkinter import dialog
from PySide6.QtWidgets import QDialog, QWidget, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from bin.Widgets.DialogChooseItem import DialogHDFChoose

from ui import uiDialogHDFCreateItem
from Constants import HDFType 
from bin.HDFManager import reValidHDFName

class DialogHDFCreate(QDialog):
    """
    用于新建 Group 或者 Data 的对话框。

    Dialog to create a new group or data.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogHDFCreateItem.Ui_Dialog()
        self.ui.setupUi(self)

        global qApp 
        self._hdf_handler = qApp.hdf_handler

        self.setWindowTitle('Create Item')
        
        self.ui.lineEdit_parent_path.setReadOnly(True)

        self.ui.comboBox_type.currentIndexChanged.connect(
            self._setCreateItemType)
        self._validateNewName()
    
        self.initNames()

        self._list_spinboxes = [
            self.ui.spinBox_dim_1,
            self.ui.spinBox_dim_2,
            self.ui.spinBox_dim_3,
            self.ui.spinBox_dim_4,
        ]
        self._initDataDimensions()

        self.ui.pushButton_browse.clicked.connect(self.browseParent)
        self.ui.pushButton_cancel.clicked.connect(self.reject)
        self.ui.pushButton_ok.clicked.connect(self._OK)

    def initNames(self,
        hdf_type: HDFType = HDFType.Group,
        new_name: str = 'untitled',
        parent_path: str = '/', 
    ):
        """
        Initialize the name, type and parent_path shown in the dialog.

        arguments:
            hdf_type: (HDFType) the HDFType of the item to be created

            new_name: (str) the item's name

            parent_path: (str) the group where the item will be created
        """
        if hdf_type == HDFType.Group:
            self.ui.comboBox_type.setCurrentIndex(0)
            self.ui.stackedWidget.setCurrentIndex(0)
        elif hdf_type == HDFType.Data:
            self.ui.comboBox_type.setCurrentIndex(1)
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.comboBox_type.setCurrentIndex(0)
            self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.lineEdit_name.setText(new_name)
        self.ui.lineEdit_parent_path.setText(parent_path)

    def _setCreateItemType(self):
        """
        Shows related widget according to the type chosen by the user.
        """
        type_index = self.ui.comboBox_type.currentIndex()
        self.ui.stackedWidget.setCurrentIndex(type_index)

    def _validateNewName(self):
        """
        Set validator by regular expression for the name.
        """
        self.re_validator = QRegularExpressionValidator()
        self.re_validator.setRegularExpression(reValidHDFName.pattern)
        self.ui.lineEdit_name.setValidator(self.re_validator)

    def _initDataDimensions(self):
        """
        Initialize the widget to choose the shape of the new data.
        """
        self.ui.comboBox_dimensions.setCurrentIndex(2)
        self.ui.comboBox_dimensions.currentIndexChanged.connect(
            self._setDimensionSpinBox
        )
        self._setDimensionSpinBox()
        for box in self._list_spinboxes:
            box.setMaximum(16384)
            box.setMinimum(1)

    def _setDimensionSpinBox(self):
        """
        Hide those spinboxes whose dimensions is not chosen.
        """
        dims = int(self.ui.comboBox_dimensions.currentText())
        self.ui.label_shape.setVisible(dims > 0)
        for ii, box in enumerate(self._list_spinboxes):
            box.setVisible(ii < dims)

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


    def getParentPath(self) -> str:
        """
        returns:
            (str) the parent group's path where the item will be created.
        """
        return self.ui.lineEdit_parent_path.text()

    def getItemType(self) -> HDFType:
        """
        returns:
            (HDFType) the HDFType of the item to be created.
        """
        type_index = self.ui.comboBox_type.currentIndex()
        if type_index == 0:   # Group
            return HDFType.Group
        elif type_index == 1:
            return HDFType.Data
        else:
            return HDFType.Data

    def getName(self) -> str:
        """
        returns:
            (str) the name of the item to be created.
        """
        return self.ui.lineEdit_name.text()

    def getDimensions(self) -> int:
        """
        returns:
            (int) the dimensions of the item to be created. 
                It should be used only when a data is created.
        """
        return int(self.ui.comboBox_dimensions.currentText())

    def getShape(self):
        """
        returns:
            (tuple) the shape of the created data.
        """
        dims = int(self.ui.comboBox_dimensions.currentText())
        tmp = []
        for ii, box in enumerate(self._list_spinboxes):
            if ii < dims:
                tmp.append(box.value())
        return tuple(tmp)

    def getDType(self):
        """
        returns:
            (str) the dtype of the data.
        """
        dtype_index = self.ui.comboBox_dtype.currentIndex()
        if dtype_index == 0:
            return 'float32'

    def _OK(self):
        """
        When OK button is clicked, check whether the state is valid.

        returns:
            (bool) whether the dialog is accepted.
        """
        name = self.ui.lineEdit_name.text()
        if name == '':
            msg = QMessageBox(text = 'Empty name')
            msg.exec()
            return False
        elif reValidHDFName.fullmatch(name) is None:
            msg = QMessageBox(text = 'Invalid name')
            msg.exec()
            return False
        else:
            self.accept()
            return True
