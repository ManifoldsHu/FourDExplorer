# -*- coding: utf-8 -*- 

"""
*--------------------------- ImporterHDF5.py ---------------------------------*
从其他 HDF5 文件中导入数据的 Data importer.

作者:           胡一鸣
创建时间:       2024年10月13日

Data importer for importing data from other HDF5 files.

author:         Hu Yiming 
date:           13 Oct. 2024
*--------------------------- ImporterHDF5.py ---------------------------------*
"""

from logging import Logger 
import os 
import datetime 

from PySide6.QtCore import QObject 
import h5py
import numpy as np

from bin.TaskManager import TaskManager 
from bin.MetaManager import MetaManager 
from bin.DateTimeManager import DateTimeManager 
from lib.TaskLoadData import TaskLoadDataFromHDF5 
from Constants import APP_VERSION 

class ImporterHDF5(QObject):
    """
    支持从任意的 HDF5 文件中加载任意形状的数据集。
    
    Importer to copy dataset from other hdf5 file with arbitrary shape into this 
    dataset.
    """
    def __init__(self, item_name: str, item_parent_path: str, parent: QObject = None):
        """
        Initializes the ImporterHDF5 object.

        arguments:
            item_name (str): The name of the item to be imported.
            
            item_parent_path (str): The parent path of the item in the HDF5 file.
            
            parent (QObject, optional): The parent QObject. Defaults to None.
        """
        super().__init__(parent)
        self.item_name = item_name 
        self.item_parent_path = item_parent_path 
        self.file_path = ''
        self.dataset_path = ''
        
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

    def setFileAndDatasetPath(self, file_path: str, dataset_path: str):
        """
        Sets the file path and dataset path for the HDF5 importer.

        arguments:
            file_path (str): The path to the HDF5 file.
            
            dataset_path (str): The path to the dataset within the HDF5 file.

        raises:
            FileNotFoundError: If the specified file path does not exist.
            
            ValueError: If dataset path is not found in the HDF5 file.
            
            ValueError: If the dataset is not a 4D-STEM dataset.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist.")
        
        with h5py.File(file_path, 'r') as hdf_file:
            if dataset_path not in hdf_file:
                raise ValueError(f"Dataset path {dataset_path} not found in HDF5 file.")
            
            dataset = hdf_file[dataset_path]
            if len(dataset.shape) != 4:
                raise ValueError(f"Dataset at {dataset_path} is not a 4D-STEM dataset.")
        
        self.file_path = file_path
        self.dataset_path = dataset_path


    def loadData(self):
        """
        This method will submit a load task to the task manager.
        
        Before this method is called, setFileAndDatasetPath() need be called.
        """
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"File {self.file_path} does not exist.")
        self.task = TaskLoadDataFromHDF5(
            file_path = self.file_path,
            dataset_path = self.dataset_path,
            item_parent_path = self.item_parent_path,
            item_name = self.item_name,
            **self.meta,
        )
        self.task_manager.addTask(self.task)

        
