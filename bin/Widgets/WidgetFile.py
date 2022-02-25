# -*- coding: utf-8 -*-

"""
*------------------------------ WidgetFile.py --------------------------------*
管理 HDF5 文件的部件类。

部件内容：
    - WidgetBaseHDFViewer，可用于查看、编辑 HDF5 文件内部的结构
    - 打开/新建文件、导入数据、导出数据等按钮
    - 查看当前工作文件夹的内容

提升部件：
    - 提升类名 WidgetFile
    - 头文件 bin.Widgets.WidgetFile.h

作者：          胡一鸣
创建时间：      2022年2月24日

The GUI Widget to manage HDF5 file.

Contents:
    - WidgetBaseHDFViewer, to view and edit HDF5 file heirarchical structure
    - Buttons to open/new file, import data and export data
    - View current working directory. 

Promoted Widget:
    - name of widget class: WidgetFile
    - header file: bin.Widgets.WidgetFile.h

author:             Hu Yiming
date:               Feb 24, 2022
*------------------------------ WidgetFile.py --------------------------------*
"""

import os 
import sys 
# from PySide6.QtCore import QDir 
from PySide6.QtWidgets import QWidget, QFileSystemModel, QFileDialog 
from bin.HDFManager import HDFHandler 
from ui import uiWidgetFile 


class WidgetFile(QWidget):
    """
    管理 HDF5 文件的部件。

    Ui 文件地址: ROOT_PATH/ui/uiWidgetFile.ui

    Widget to manage HDF5 files.

    The path of Ui file: ROOT_PATH/ui/uiWidgetFile.ui
    """
    def __init__(self, parent: QWidget = None):
        """
        arguments:
            parent: (QWidget)
        """
        super().__init__(parent)
        self.ui = uiWidgetFile.Ui_Form()
        self.ui.setupUi(self)
        
        self._hdf_handler = HDFHandler()    # Singleton
        self._hdf_model = None

        self._initCWD()
        self._initHDF()
    
    def _initCWD(self):
        """
        Initialize Current Work Directory Views
        """
        self.ui.lineEdit_working_directory.setText(os.getcwd())
        self.ui.lineEdit_working_directory.setReadOnly(True)

        self._file_model = QFileSystemModel()
        self._file_model.setReadOnly(True)
        self._file_model.setRootPath(os.getcwd())

        self.ui.listView_working_directory.setModel(self._file_model)
        self.ui.listView_working_directory.setRootIndex(
            self._file_model.index(os.getcwd())
        )
        

    def _initHDF(self):
        """
        Initialize HDF file views.
        """
        try:
            self._hdf_model = self._hdf_handler.createModel()
        except OSError:
            return None
        else:
            self.ui.widget_HDFTreeView.ui.treeView_HDF.setModel(self._hdf_model)

        # if not self._hdf_handler.isFileOpened():
        #     self.ui.pushButton_new_file.setText('New H5 File')
        #     self.ui.pushButton_new_file.clicked.connect(self.newFile)
        # else:
        #     self.ui.pushButton_new_file.setText('Close H5 File')
        #     self.ui.pushButton_new_file.clicked.connect(self.closeFile)

        
        self._hdf_handler.file_opened.connect(self.openFile)
        self._hdf_handler.file_closed.connect(self.closeFile)
    
        self.ui.pushButton_new_or_close_file.clicked.connect(self.newFile)
        

    def newFile(self):
        """
        To create a new h5 file.
        """
        directory_path = QFileDialog.getExistingDirectory(self, 
            caption='Choose Directory', 
            dir = os.getcwd(), 
            options = QFileDialog.ShowDirsOnly|QFileDialog.DontResolveSymlinks,
        )

    def openFile(self):
        pass

    def closeFile(self):
        pass