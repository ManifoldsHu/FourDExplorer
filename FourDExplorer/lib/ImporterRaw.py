# -*- coding: utf-8 -*-

"""
*---------------------------- ImporterEMPAD.py -------------------------------*
从二进制文件中读取数据的 Data importer.

用于二进制文件的 4D-STEM 数据集的 Data importer 没有解析器，因为二进制文件一般没有
头文件可言，所以需要由用户指定读取的参数，以做好将二进制文件中的数据复制进 HDF 文件的
准备。随后，importer 会创建一个任务，并把它提交到任务管理器中。

作者：          胡一鸣
创建时间：      2022年5月8日

Data importer from the EMPAD.

The Importers of 4D-STEM dataset from binary files have no parser, because for 
those binary files there are no header files. So, the users should assign the
key metadata themselves as a preparation for copying the whole dataset into the
HDF5 file. Then, the importer will create a Task object and submit it to the 
task manager.

author:             Hu Yiming
date:               May 8, 2022
*---------------------------- ImporterEMPAD.py -------------------------------*
"""

from logging import Logger
from xml.dom.minidom import Document, parse
import os 

from PySide6.QtCore import QObject

from bin.TaskManager import TaskManager
from lib.TaskLoadData import TaskLoadFourDSTEMFromRaw 

class ImporterRawFourDSTEM(QObject):
    """
    The importer of the raw dataset (binary files).
    """
    def __init__(self, 
        item_name: str, 
        item_parent_path: str, 
        parent: QObject = None
    ):
        """
        arguments:
            item_name: (str) the created Dataset's name as an HDF object.

            item_parent_path: (str) the path of the created Dataset's parent 
                group.

            parent: (QObject)
        """
        super().__init__(parent)
        
        self.item_name = item_name 
        self.item_parent_path = item_parent_path

        self.meta = {}

    @property
    def task_manager(self) -> TaskManager:
        global qApp
        return qApp.task_manager

    def setMeta(self, **kw):
        self.meta.update(kw)

    def loadData(self):
        # shape = (self.scan_i, self.scan_j, self.dp_i, self.dp_j)
        shape = (
            self.meta['scan_i'], 
            self.meta['scan_j'], 
            self.meta['dp_i'], 
            self.meta['dp_j'],
        )
        self.task = TaskLoadFourDSTEMFromRaw(
            shape = shape,
            file_path = self.meta['raw_path'],
            item_parent_path = self.item_parent_path,
            item_name = self.item_name,
            parent = self, 
            **self.meta,
        )
        self.task_manager.addTask(self.task)

