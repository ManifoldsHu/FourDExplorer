# -*- coding: utf-8 -*- 

"""
*-------------------------- DialogSaveItem.py --------------------------------*
用于保存 Dataset 至 HDF5 文件内的对话框。

作者:           胡一鸣
创建日期:       2024年9月20日

Dialog to save dataset to HDF5 file.

author:         Hu Yiming
date:           Sept 20, 2024
*-------------------------- DialogSaveItem.py --------------------------------*
"""

from PySide6.QtWidgets import QDialog 
from PySide6.QtWidgets import QWidget 
from PySide6.QtGui import QRegularExpressionValidator

from bin.HDFManager import HDFHandler
from bin.HDFManager import HDFGroupNode
from bin.HDFManager import reValidHDFName
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from ui import uiDialogCreateImage

class DialogSaveImage(QDialog):
    """
    选择在 HDF 文件中保存重构图像路径的对话框。
    
    与 DialogSaveFourDSTEM 不同的是，不提供覆盖保存的选项。

    Dialog to choose where to save the reconstructed image in the HDF file.
    
    Different from DialogSaveFourDSTEM, no overwrite option is provided.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogCreateImage.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_ok.clicked.connect(self.accept)
        self.ui.pushButton_cancel.clicked.connect(self.reject)
        self.ui.pushButton_browse.clicked.connect(self.browseParent)

        self.ui.lineEdit_name.setText('Untitled')
        self._validateNewName()

        
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



class DialogSaveVectorField(DialogSaveImage):
    """
    选择在 HDF 文件中保存矢量场的路径。
    
    与 DialogSaveFourDSTEM 不同的是，不提供覆盖保存的选项。

    Dialog to choose where to save the reconstructed image in the HDF file.
    
    Different from DialogSaveFourDSTEM, no overwrite option is provided.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
    
    def getNewName(self) -> str:
        """
        returns the new name of the imported dataset.

        Will add '.img' automatically as the extension.
        """
        name = self.ui.lineEdit_name.text()
        if '.' in name:
            if name.split('.')[-1] == 'vec':
                return name 
        return name + '.vec'

