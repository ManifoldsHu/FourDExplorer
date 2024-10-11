# -*- coding: utf-8 -*- 

"""
*-------------------------- WidgetImportNumpy.py -----------------------------*
用来导入 numpy .npy 文件或 .npz 文件的部件。

作者:           胡一鸣
创建时间:       2024年10月12日

Widgets to import 4D-STEM dataset from numpy .npy file or .npz file.

author:         Hu Yiming
date:           Oct 12, 2024    
*-------------------------- WidgetImportNumpy.py -----------------------------*
"""

import os 

from PySide6.QtWidgets import QWidget 
from PySide6.QtWidgets import QFileDialog 
import numpy as np

from ui import uiWidgetImportNumpy 

class WidgetImportNumpy(QWidget):
    """ 
    导入 numpy 文件的部件。对于 npz 文件，提供一个选择框用于选择要加载其中哪个数据。
    不论是 npy 还是 npz 的数据，都必须是四维的。

    Widget to import numpy files. For npz file, provide a selection box to 
    choose which data to load. The data must be 4-dimensional.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uiWidgetImportNumpy.Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.lineEdit_file_path.setReadOnly(True)
        self.ui.pushButton_browse_file.clicked.connect(self.browseFile)
        self.ui.stackedWidget.setCurrentIndex(1)    # 0: npz, 1: npy
        
        self._npz_keys = {}
        self._file_path = ''
        
    def browseFile(self):
        """
        Open a dialog to choose npz or npy file.
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Open numpy npy/npz file',
            './',
            'npy (*.npy);;npz (*.npz)',
        )
        if file_path == '':
            return 
        
        file_path = os.path.abspath(file_path)
        
        if file_path.endswith('.npz'):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.comboBox_array_name.clear()
            with open(file_path, 'rb') as f:
                npz_data = np.load(f, mmap_mode='r')
                self._npz_keys = {}
                for key in npz_data.keys():
                    self.ui.comboBox_array_name.addItem(key)
                    self._npz_keys[key] = npz_data[key]
                    
        elif file_path.endswith('.npy'):
            self.ui.stackedWidget.setCurrentIndex(1)
        
        
        self._file_path = file_path
        self.ui.lineEdit_file_path.setText(file_path)

        
    def getFilePath(self) -> str:
        return self._file_path 
    
    def getNpzKey(self) -> str:
        return self.ui.comboBox_array_name.currentText()
    
    
        