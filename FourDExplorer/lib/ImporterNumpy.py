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
from lib.TaskLoadData import TaskLoadNumpy 
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
    
    # def _parseNpzDataNames(self):
    #     """
    #     Parse the data names in the .npz file.
    #     """
    #     with np.load(self.file_path) as data:
    #         self._data_names = list(data.keys())
            
    def setFilePath(self, path: str):
        """
        arguments:
            path: (str) The absolute path of the outside file.
        """
        if not isinstance(path, str):
            raise TypeError('path must be a str, not '
                '{0}'.format(type(path).__name__))
        
        if not os.path.isfile(path):
            raise OSError('path is not a file: {0}'.format(path))
        
        self._file_path = path
        
    def setReadParameters(self, file_path: str, npz_data_name: str = None,):
        """
        arguments:
            file_path: (str) The absolute path of the outside file.
            
            npz_data_name: (str) The data name in the .npz file. If not 
                specified, the first data will be loaded.
        """
        self.setFilePath(file_path)
        self._npz_data_name = npz_data_name
        

    def varifyData(self) -> bool:
        """
        Return True if the data is a valid 4D-STEM dataset.
        """
        # 检查文件路径是否存在
        if not self._file_path:
            return False

        # 处理 npy 文件
        if self._file_path.endswith('.npy'):
            try:
                # 使用 with np.load 风格加载文件头部并检查维度
                data = np.load(self._file_path, mmap_mode='r')
                if data.ndim == 4:
                    return True
            except Exception as e:
                self.logger.error(f"Error loading .npy file: {e}")
            return False

        # 处理 npz 文件
        elif self._file_path.endswith('.npz'):
            try:
                # 获取当前选择的键
                selected_key = self._npz_data_name
                # 使用 mmap_mode='r' 延迟加载选定数组
                npz_data = np.load(self._file_path, mmap_mode='r')
                selected_data = npz_data[selected_key]
                if selected_data.ndim == 4:
                    return True
            except Exception as e:
                self.logger.error(f"Error loading .npz file: {e}")
            return False
        return False
        
    def parseShapeAndDtype(self) -> tuple:
        """
        Return the shape and dtype of the data.
        For .npy files, directly read the shape and dtype using memory mapping.
        For .npz files, read the shape and dtype of the selected array from the combobox.
        
        returns:
            shape: (tuple[int]) The shape of the data.
            dtype: (str) The dtype of the data.
        """
        # 检查文件路径是否存在
        if not self._file_path:
            return None, None

        # 处理 npy 文件
        if self._file_path.endswith('.npy'):
            try:
                # 使用 mmap_mode='r' 只获取形状和 dtype 信息
                data = np.load(self._file_path, mmap_mode='r')
                return data.shape, data.dtype
            except Exception as e:
                print(f"Error loading .npy file: {e}")
                return None, None

        # 处理 npz 文件
        elif self._file_path.endswith('.npz'):
            try:
                # 获取当前选择的键
                selected_key = self.ui.comboBox_array_name.currentText()
                if selected_key in self._npz_keys:
                    # 使用 mmap_mode='r' 延迟加载选定数组并获取形状和 dtype
                    with np.load(self._file_path, mmap_mode='r') as npz_data:
                        selected_data = npz_data[selected_key]
                        return selected_data.shape, selected_data.dtype
            except Exception as e:
                print(f"Error loading .npz file: {e}")
                return None, None

        return None, None


        
        
    def loadData(self):
        """
        This method will submit a load task to the task manager.
        """
        if not self._file_path:
            raise RuntimeError("No file is assigned.")
        if not self.varifyData():
            raise RuntimeError("Invalid 4D-STEM data. The data must be 4-dimensional.")
        shape, dtype = self.parseShapeAndDtype()
        if (shape is None) or (dtype is None):
            raise RuntimeError("Failed to parse the shape of the data.")
        
        self.task = TaskLoadNumpy(
            shape, 
            self._file_path, 
            self.item_parent_path, 
            self.item_name, 
            self.meta,
            dtype
        ) 
        self.task_manager.addTask(self.task)
