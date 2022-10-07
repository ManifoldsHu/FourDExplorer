# -*- coding: utf-8 -*-

"""
*---------------------------- FileActions.py ---------------------------------*
用于打开/关闭文件的各个 Action。

作者:           胡一鸣
创建日期:       2022年6月13日

This module includes actions for opening or closing files.

author:         Hu Yiming
date:           Jun 13, 2022
*---------------------------- FileActions.py ---------------------------------*
"""

import os

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QObject
from PySide6.QtGui import QAction

from bin.HDFManager import HDFHandler

class ActionFileBase(QAction):
    """
    The base action for opening or closing an HDF5 file.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler


class ActionOpenFile(ActionFileBase):
    """
    The action to open an HDF5 file.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.triggered.connect(self.openFile)
        self.setText('Open HDF5 File')
    
    def openFile(self):
        """
        Open a dialog, choose a file and open it.
        """
        _path = QFileDialog.getOpenFileName(
            None,
            caption = 'Open HDF5 file',
            dir = os.getcwd(),
            filter = 'HDF5 File (*.h5 *.hdf5 *.H5 *.HDF5);;All Files (*.*)',
            selectedFilter = 'HDF5 File (*.h5 *.hdf5 *.H5 *.HDF5)',
        )
        if _path[0] == '':
            return False 

        file_path = os.path.abspath(_path[0])
        self.hdf_handler.file_path = file_path
        self.hdf_handler.openFile()

class ActionCloseFile(ActionFileBase):
    """
    The action to close an HDF5 file.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Close File')
        self.triggered.connect(self.closeFile)
        self.setEnabled(self.hdf_handler.isFileOpened())
        self.hdf_handler.file_opened.connect(self.setState)
        self.hdf_handler.file_closed.connect(self.setState)
        

    def closeFile(self):
        """
        To close a file.
        """
        self.hdf_handler.closeFile()

    def setState(self):
        """
        When there is no files, this action will be forbidden.
        """
        self.setEnabled(self.hdf_handler.isFileOpened())
        

class ActionNewFile(ActionFileBase):
    """
    The action to create a new HDF5 file.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('New HDF5 File')
        self.triggered.connect(self.newFile)

    def newFile(self):
        """
        To open a dialog and create a new file.
        """
        _path = QFileDialog.getSaveFileName(
            None,
            caption = 'New HDF5 File',
            dir = os.path.join(os.getcwd(), 'untitled'),
            filter = 'HDF5 File (*.h5 *.hdf5 *.H5 *.HDF5);;All Files (*.*)',
            selectedFilter = 'HDF5 File (*.h5 *.hdf5 *.H5 *.HDF5)',
        )
        if _path[0] == '':
            return False 

        _path = os.path.abspath(_path[0])
        self.hdf_handler.file_path = _path 
        self.hdf_handler.createFile()
        action_open_file = ActionOpenFile(self)
        action_open_file.trigger()

class ActionQuit(ActionFileBase):
    """
    The action to quit 4D-Explorer
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Quit')
        self.triggered.connect(self.closeMainWindow)

    def closeMainWindow(self):
        global qApp 
        main_window = qApp.main_window 
        main_window.close()
