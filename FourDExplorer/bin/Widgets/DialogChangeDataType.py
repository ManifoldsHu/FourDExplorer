# -*- coding: utf-8 -*-

"""
*------------------------- DialogChangeDataType.py ---------------------------*
修改 Dataset 的类型的对话框。实际上就是改扩展名。

作者：          胡一鸣
创建时间：      2022年6月15日

The dialog to change dataset's HDFType. Actually it only modifies extension.

author:             Hu Yiming
date:               Jun 15, 2022
*------------------------- DialogChangeDataType.py ---------------------------*
"""

from PySide6.QtWidgets import QDialog, QWidget, QMessageBox
from Constants import HDFType
from bin.HDFManager import HDFDataNode, HDFHandler

from ui import uiDialogChangeDataType
from bin.Widgets.DialogChooseItem import DialogHDFChoose

class DialogChangeDataType(QDialog):
    """
    用于更换 Dataset 的类型的对话框。

    Dialog to change the type of the Dataset.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogChangeDataType.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Change Data\'s Type')
        self.ui.lineEdit_item_path.setText('/')
    
        self.ui.pushButton_ok.clicked.connect(self.accept)

        self.ui.comboBox_target_type.currentIndexChanged.connect(
            self._setIntroduce
        )
        self.ui.pushButton_cancel.clicked.connect(self.reject)
        self.ui.pushButton_browse.clicked.connect(self._browseItem)

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler

    @property
    def item_path(self) -> str:
        return self.ui.lineEdit_item_path.text()

    def _browseItem(self):
        """
        Open a dialog to choose the item to be moved.

        returns:
            (bool)
        """
        dialog_browse = DialogHDFChoose(self)
        dialog_code = dialog_browse.exec()
        if dialog_code == dialog_browse.Accepted:
            item_path = dialog_browse.getCurrentPath()
            self.setItemPath(item_path)

    def setItemPath(self, item_path: str):
        """
        Set the item_path to change the type.

        arguments:
            item_path: (str) must be path of a Dataset.
        """
        if not isinstance(item_path, str):
            raise TypeError('item_path must be a str, not '
                '{0}'.format(type(item_path).__name__))
        node = self.hdf_handler.getNode(item_path)
        if not isinstance(node, HDFDataNode):
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Only Dataset can be set these types.')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return 

        self.ui.lineEdit_item_path.setText(item_path)
        self._updateExt()

    def _updateExt(self):
        """
        Update the type of current dataset according to its extension.
        """
        node = self.hdf_handler.getNode(self.item_path)
        if '.' in node.name:
            ext = node.name.split('.').pop()
            if ext in HDFDataNode.ext_to_type:
                hdf_type = HDFDataNode.ext_to_type[ext]
            else:
                hdf_type = HDFType.Data 
        else:
            hdf_type = HDFType.Data 
        
        self.ui.lineEdit_current_type.setText(hdf_type.name)

    def getTargetType(self) -> HDFType:
        """
        Get the target HDFType of the dataset.

        returns:
            (HDFType)
        """
        text = self.ui.comboBox_target_type.currentText()
        return HDFType[text]

    def getTargetExt(self) -> str:
        """
        Get the target ext of the dataset.

        returns:
            (str)
        """
        return HDFDataNode.type_to_ext[self.getTargetType()]

    def _setIntroduce(self):
        """
        Change the introduction text for the type.
        """
        self.ui.stackedWidget_introduce.setCurrentIndex(
            self.ui.comboBox_target_type.currentIndex()
        )
    
            



