# -*- coding: utf-8 -*- 

"""
*--------------------------- WidgetImportDM4.py ------------------------------*
用来导入 .dm4 文件所包含 4D-STEM 数据的部件


作者：          胡一鸣
创建时间：      2024年10月12日

Widgets to import 4D-STEM dataset from .dm4 file.

author:         Hu Yiming
date:           Oct 12, 2024
*--------------------------- WidgetImportDM4.py ------------------------------*
"""

import os 

from PySide6.QtWidgets import QWidget 
from PySide6.QtWidgets import QFileDialog 

from ui import uiWidgetImportDM4

class WidgetImportDM4(QWidget):
    """
    用于导入 dm4 的 4D-STEM 数据集的部件
    
    Widget to import 4D-STEM dataset from .dm4 file.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uiWidgetImportDM4.Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.lineEdit_file_path.setReadOnly(True)
        self.ui.pushButton_browse.clicked.connect(self._browse)
        
    def _browse(self):
        """
        Select .dm4 file.
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Select Digital Micrograph DM4 file", 
            '/', 
            "DM4 Files (*.dm4)"
        )
        
        if file_path == '':
            return
        file_path = os.path.abspath(file_path)
        self.ui.lineEdit_file_path.setText(file_path)
        
    def getFilePath(self):
        """
        Get the file path of the selected .dm4 file.
        
        Returns:
            str: file path
        """
        return self.ui.lineEdit_file_path.text()
