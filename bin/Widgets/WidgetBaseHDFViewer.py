# -*- coding: utf-8 -*-

'''
*------------------------- WidgetBaseHDFViewer.py ----------------------------*
对 HDF5 文件内部的层次结构进行显示的模块。使用时，在 UI 中可以直接添加 Widget，然后
将其提升为 WidgetBaseHDFViewer。

4D-Explorer 软件默认使用 HDF5 进行四维数据及其元数据的管理。其数据的组织方式类似于
Unix 目录。为此，我们使用 Qt 的 QTreeView 对这些四维数据进行管理。

作者：          胡一鸣
创建时间：      2022年2月18日
*------------------------- WidgetBaseHDFViewer.py ----------------------------*

'''

import sys
import os

from PySide6.QtCore import QModelIndex, Qt, QAbstractItemModel, QPoint
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QMenu, QWidget
from PySide6.QtGui import QRegularExpressionValidator


from ui import uiWidgetBaseHDFViewer
from bin.HDFManager import HDFHandler
from bin.Log import LogUtil

import configparser
from app import ROOTPATH

# import h5py
# from collections.abc import Mapping
# from qt_material import apply_stylesheet


class WidgetBaseHDFViewer(QWidget):
    '''
        用于显示 HDF5 文件结构的基础组件，包含一个 QLineEdit 和一个 QTreeView。 
    '''
    def __init__(self, parent: QWidget, hdf_handler: HDFHandler):
        '''
        arguments           type                description
        -----------------------------------------------------------------------
        parent              QWidget             The parent widget (like a dial-
                                                og or the main window).

        hdf_handler         HDFHandler          The global variable. I will get
                                                information (especially models 
                                                and file structure) from the h-
                                                andler.
        -----------------------------------------------------------------------
        '''
        super().__init__(parent)
        self._hdf_handler = HDFHandler
        self.ui = uiWidgetBaseHDFViewer.Ui_Form()
        self.ui.setupUi(self)



    @property
    def hdf_handler(self):
        return self._hdf_handler