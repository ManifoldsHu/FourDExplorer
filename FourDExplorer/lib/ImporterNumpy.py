# -*- coding: utf-8 -*- 


"""
*---------------------------- ImporterNumpy.py -------------------------------*
导入 .npy 或者 .npz 数据集的类

作者:           胡一鸣
创建日期:       2024年10月11日

The class to import .npy or .npz dataset.

author:         Hu Yiming
date:           Oct 11, 2024
*---------------------------- ImporterNumpy.py -------------------------------*
"""

from logging import Logger 
import os 
import datetime 
from dateutil import parser as dt_parser 

from PySide6.QtCore import QObject 

import numpy as np

from bin.TaskManager import TaskManager 
from bin.MetaManager import MetaManager 
from bin.DateTimeManager import DateTimeManager 
from Constants import APP_VERSION 

class ImporterNumpy(QObject):
    """
    The importer of .npy or .npz file. The array must be of dimension 4, as 
    4D-STEM dataset. 
    """
    
    _available_file_types = ['npy', 'npz']
    
    def __init__(self, item_name: str, item_parent_path: str, parent: QObject = None):
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
        
        self._scan_i = 1
        self._scan_j = 1 
        self._dp_i = 1
        self._dp_j = 1
        
        self._file_type = 'npy'
        self._file_path = ''
        self._dtype = 'float'
        
        self._is_flipped = False 
        self._rotate90 = 0
        
        self.meta = {
            '/General/fourd_explorer_version': '.'.join([str(i) for i in APP_VERSION]),
            '/General/date': self.datetime_manager.current_date,
            '/General/time': self.datetime_manager.current_time,
            '/General/time_zone': self.datetime_manager.current_timezone,
        }
        
    @property
    def scan_i(self) -> int:
        return self._scan_i
    
    @property
    def scan_j(self) -> int:
        return self._scan_j
    
    @property
    def dp_i(self) -> int:
        return self._dp_i
    
    @property
    def dp_j(self) -> int:
        return self._dp_j
    
    @property
    def file_type(self) -> str:
        return self._file_type
    
    @property
    def file_path(self) -> str:
        return self._file_path
    
    @property
    def dtype(self) -> str:
        return self._dtype
    
    @property
    def is_flipped(self) -> bool:
        return self._is_flipped
    
    @property
    def rotate90(self) -> int:
        return self._rotate90
    
    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger
    
    @property
    def task_manager(self) -> TaskManager:
        global qApp
        return qApp.task_manager
    
    @property
    def datetime_manager(self) -> DateTimeManager:
        global qApp
        return qApp.datetime_manager
    
    def _parseNpzDataNames(self):
        """
        Parse the data names in the .npz file.
        """
        with np.load(self.file_path) as data:
            self._data_names = list(data.keys())
        

