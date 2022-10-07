# -*- coding: utf-8 -*-

"""
*---------------------------- DialogMoveItem.py ------------------------------*
在 h5 文件中移动 Item 的对话框。

作者：          胡一鸣
创建时间：      2022年3月2日

The dialog to move items in the h5 file.

author:             Hu Yiming
date:               Mar 2, 2022
*---------------------------- DialogMoveItem.py ------------------------------*
"""

from PySide6.QtWidgets import QDialog, QWidget 

from ui import uiDialogHDFMoveItem
from bin.Widgets.DialogChooseItem import DialogHDFChoose

class DialogHDFMove(QDialog):
    """
    用于移动 Item 的对话框。

    Dialog to choose group or data.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogHDFMoveItem.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Move Item')
        self.ui.lineEdit_item_path.setText('/')
        self.ui.lineEdit_dest_path.setText('/')
        self.ui.pushButton_browse_item.clicked.connect(self.browseItem)
        self.ui.pushButton_browse_dest.clicked.connect(self.browseDest)
        self.ui.pushButton_cancel.clicked.connect(self.reject)
        self.ui.pushButton_ok.clicked.connect(self.accept)


    def setItemPath(self, hdf_path: str):
        """
        Initialize the path of the item to be moved.

        arguments:
            hdf_path: (str) the item's path
        """
        self.ui.lineEdit_item_path.setText(hdf_path)

    def setDestPath(self, hdf_path: str):
        """
        Initialize the destination of the item.

        arguments:
            hdf_path: (str) the destination path
        """
        self.ui.lineEdit_dest_path.setText(hdf_path)

    def browseItem(self) -> bool:
        """
        Open a dialog to choose the item to be moved.

        returns:
            (bool)
        """
        dialog_browse = DialogHDFChoose(self, only_group = False)

        treeview_HDF = dialog_browse.ui.widget_viewer.ui.treeView_HDF
        model = treeview_HDF.model()
        current_path = self.ui.lineEdit_item_path.text()
        index = model.indexFromPath(current_path)
        treeview_HDF.setCurrentIndex(index)
        dialog_browse.setCurrentPath()

        dialog_code = dialog_browse.exec()
        if dialog_code == dialog_browse.Accepted:
            item_path = dialog_browse.getCurrentPath()
            self.ui.lineEdit_item_path.setText(item_path)
            return True
        else:
            return False

    def browseDest(self) -> bool:
        """
        Open a dialog to choose the destination group.

        returns:
            (bool)
        """
        dialog_browse = DialogHDFChoose(self, only_group = True)
        dialog_code = dialog_browse.exec()
        if dialog_code == dialog_browse.Accepted:
            current_path = dialog_browse.getCurrentPath()
            self.ui.lineEdit_dest_path.setText(current_path)
            return True
        else:
            return False
        
    # def _OK(self):
    #     """
    #     When OK button is clicked, check whether the state is valid.

    #     returns:
    #         (bool) whether the dialog is accepted.
    #     """
    #     self.accept()

    def getItemPath(self) -> str:
        """
        returns the item's path to be moved.

        returns:
            (str)
        """
        return self.ui.lineEdit_item_path.text()

    def getDestPath(self) -> str:
        """
        returns the destination's path.

        returns:
            (str)
        """
        return self.ui.lineEdit_dest_path.text()