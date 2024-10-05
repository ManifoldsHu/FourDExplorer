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

# from logging import Logger
# from xml.dom.minidom import Document, parse
# import os 
import datetime

from PySide6.QtCore import QObject

from Constants import APP_VERSION
from bin.TaskManager import TaskManager
from bin.DateTimeManager import DateTimeManager
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
        
        self._item_name = item_name 
        self._item_parent_path = item_parent_path

        self.meta = {}  

    @property
    def task_manager(self) -> TaskManager:
        global qApp
        return qApp.task_manager

    @property
    def datetime_manager(self) -> DateTimeManager:
        global qApp 
        return qApp.datetime_manager

    def setMeta(self, **kw):
        self.meta.update(kw)

    def setReadParameters(
        self,
        raw_path: str,
        scalar_type: str,
        scalar_size: int,
        dp_i: int,
        dp_j: int,
        scan_i: int,
        scan_j: int,
        offset_to_first_image: int,
        gap_between_images: int,
        little_endian: bool,
        rotate_90: int,
        is_flipped: bool,
    ):
        self._raw_path = raw_path 
        self._scalar_type = scalar_type
        self._scalar_size = scalar_size 
        self._dp_i = dp_i 
        self._dp_j = dp_j 
        self._scan_i = scan_i 
        self._scan_j = scan_j 
        self._offset_to_first_images = offset_to_first_image
        self._gap_between_images = gap_between_images
        self._little_endian = little_endian
        self._rotate_90 = rotate_90
        self._is_flipped = is_flipped

        self.meta['/General/fourd_explorer_version'] = '.'.join([str(i) for i in APP_VERSION])
        self.meta['/General/data_path'] = raw_path 
        self.meta['/General/date'] = self.datetime_manager.current_date
        self.meta['/General/time'] = self.datetime_manager.current_time
        self.meta['/General/time_zone'] = self.datetime_manager.current_timezone
        self.meta['/General/data_path'] = raw_path 
        self.meta['/Calibration/Space/dp_i'] = dp_i 
        self.meta['/Calibration/Space/dp_j'] = dp_j 
        self.meta['/Calibration/Space/scan_i'] = scan_i 
        self.meta['/Calibration/Space/scan_j'] = scan_j 




    def loadData(self):
        shape = (self._scan_i, self._scan_j, self._dp_i, self._dp_j)
        self.task = TaskLoadFourDSTEMFromRaw(
            shape = shape,
            file_path = self._raw_path,
            item_parent_path = self._item_parent_path,
            item_name = self._item_name,
            offset_to_first_image = self._offset_to_first_images,
            gap_between_images = self._gap_between_images,
            scalar_type = self._scalar_type,
            scalar_size = self._scalar_size,
            little_endian = self._little_endian,
            is_flipped = self._is_flipped,
            rotate90 = self._rotate_90,
            parent = self, 
            **self.meta,
        )
        self.task_manager.addTask(self.task)

