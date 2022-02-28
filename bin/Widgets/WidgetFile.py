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
import traceback
# from PySide6.QtCore import QDir 
from PySide6.QtWidgets import QWidget, QFileSystemModel, QFileDialog
from ui import uiWidgetFile 
from bin.Log import LogUtil

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

        self._logger = LogUtil(__name__)
        
        global qApp
        self._hdf_handler = qApp.hdf_handler
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
        self._hdf_handler.file_state_changed.connect(
            self.changeStateByFileState)
        self.ui.pushButton_new_or_close_file.clicked.connect(self.newFile)
        self.changeStateByFileState()


    def newFile(self):
        """
        Open a dialog, choose a path and name, and create a new file.
        """
        save_return = QFileDialog.getSaveFileName(self, 
            caption='Create an HDF5 File', 
            dir = os.path.join(os.getcwd(), 'untitled'),
            filter = 'HDF File (*.h5 *.hdf5 *.H5 *.HDF5);;All Files (*.*)',
            selectedFilter = 'HDF File (*.h5 *.hdf5 *.H5 *.HDF5)',
        )
        if save_return[0] == '':
            return False

        file_path = os.path.abspath(save_return[0])
        self._newFile(file_path)

    def _newFile(self, file_path: str):
        """
        Create file, and open it.

        arguments:
            file_path: (str) the created file path.
        """
        self._hdf_handler.file_path = file_path
        self._hdf_handler.createFile()
        self._openFile(file_path)

    def changeStateByFileState(self):
        """
        Reactions (Slot) of file widgets if the file state is changed 
        (opened or close). 
        """
        if self._hdf_handler.isFileOpened():
            self.ui.lineEdit_working_directory.setText(
                os.getcwd()
            )
            self.ui.listView_working_directory.setRootIndex(
                self._file_model.index(os.getcwd())
            )

            self.ui.pushButton_import_data.setDisabled(False)
            self.ui.pushButton_export_data.setDisabled(False)
            self.ui.pushButton_new_or_close_file.setText('Close File')
            self.ui.pushButton_new_or_close_file.clicked.connect(
                self.closeFile
            )
            try:
                self.ui.pushButton_new_or_close_file.clicked.disconnect(
                    self.newFile
                )
            except RuntimeError:
                pass
        else:
            self.ui.pushButton_import_data.setDisabled(True)
            self.ui.pushButton_export_data.setDisabled(True)
            self.ui.pushButton_new_or_close_file.setText('New File')
            self.ui.pushButton_new_or_close_file.clicked.connect(
                self.newFile
            )
            try:
                self.ui.pushButton_new_or_close_file.clicked.disconnect(
                    self.closeFile
                )
            except RuntimeError:
                pass


    def openFile(self):
        """
        Open a dialog, choose a file and open it.
        """
        open_return = QFileDialog.getOpenFileName(
            parent = self,
            caption = 'Open an HDF5 file',
            dir = os.getcwd(),
            filter = 'HDF File (*.h5 *.hdf5 *.H5 *.HDF5);;All Files (*.*)',
            selectedFilter = 'HDF File (*.h5 *.hdf5 *.H5 *.HDF5)',
        )
        if open_return[0] == '':
            return False
        
        file_path = os.path.abspath(open_return[0])
        self._openFile(file_path)

    def _openFile(self, file_path: str):
        """
        Open a file.

        arguments:
            file_path: (str) the path of the file to be opened.
        """
        self._hdf_handler.file_path = file_path
        self._hdf_handler.openFile()
    
    def closeFile(self):
        """
        Close the current HDF5 file.
        """
        self._hdf_handler.closeFile()