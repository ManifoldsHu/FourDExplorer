# -*- coding: utf-8 -*-

"""
*---------------------------- TaskLoadData.py --------------------------------*
包含从外部文件加载数据进入 HDF5 文件中的任务。

作者:           胡一鸣
创建日期:       2022年4月29日

This module includes tasks to load data from outside files to HDF5 objects.

author:         Hu Yiming
date:           Apr 29, 2021
*---------------------------- TaskLoadData.py --------------------------------*
"""

from logging import Logger
import os
from typing import Iterable, Mapping, Tuple  
from PIL import Image

from PySide6.QtCore import QObject, Signal 
import h5py
import numpy as np
# from bin.ItemActions import ActionShowFourDSTEM

from bin.TaskManager import Subtask, SubtaskWithProgress, Task
from bin.HDFManager import HDFHandler
from lib.ReadBinary import getDType, readFourDSTEMFromRaw

class TaskBaseLoadData(Task):
    """
    从外部文件中加载数据的 Task 的基类。

    将自动在 HDF5 文件中创建一个 Object 并导入数据。

    The task to load data from ouside file.

    Will create an object in the HDF5 file automatically.
    """
    def __init__(self, 
        shape: Tuple,
        file_path: str,
        item_parent_path: str,
        item_name: str,
        parent: QObject = None,
        **meta,
    ):
        """
        arguments:
            file_path: (str) The absolute path of the ouside raw file.

            item_parent_path: (str) The path of the parent group of the Dataset 
                item in the HDF file.

            item_name: (str) The name of the new Dataset item in the HDF file.

            parent: (QObject)

            **meta: (key word arguments) other meta data that should be stored
                in the attrs of HDF5 object.
        """
        super().__init__(parent)
        self._shape = shape 
        self._file_path = file_path    # The ouside file path where data from
        self._item_parent_path = item_parent_path    # The parent group path inside HDF5 file.
        self._item_name = item_name 
        self._meta = meta 
        self.name = 'Load Data'
        self.comment = (
            'Load data\n'
            'Data File path: {0}\n'
            'To Dataset Object: {1}\n'.format(
                self._file_path, self._item_name 
            )
        )
    
    @property
    def item_path(self) -> str:
        """
        The new dataset's path. It must be a non-exist object before the 
        dataset is created.
        """
        if self._item_parent_path == '/':
            return self._item_parent_path + self._item_name
        else:
            return self._item_parent_path + '/' + self._item_name

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler
        
    def setShape(self, shape: tuple[int]):
        """
        arguments:
            shape: (Tuple)
        """
        if not isinstance(shape, Iterable):
            raise TypeError('shape must be a tuple, not '
                '{0}'.format(type(shape).__name__))
        self._shape = shape 

    def setFilePath(self, path: str):
        """
        arguments:
            path: (str) The absolute path of the ouside file.
        """
        if not isinstance(path, str):
            raise TypeError('path must be a str, not '
                '{0}'.format(type(path).__name__))
        
        if not os.path.isfile(path):
            raise OSError('path is not a file: {0}'.format(path))

        self._file_path = path 

    def setItemParentPath(self, path: str):
        """
        arguments:
            path: (str) The path of the parent group of the Dataset item in the
                HDF file.
        """
        if not isinstance(path, str):
            raise TypeError('path must be a str, not '
                '{0}'.format(type(path).__name__))

        self._item_parent_path = path 

    def setItemName(self, name: str):
        """
        arguments:
            name: (str) The name of the new Dataset item in the HDF file.
        """
        if not isinstance(name, str):
            raise TypeError('name must be a str, not '
                '{0}'.format(type(name).__name__))

        self._item_name = name 

    def updateMeta(self, **meta):
        """
        Update metadata. The new attributes will be added.
        """
        for key in meta:
            self._meta[key] = meta[key]
    
class TaskLoadFourDSTEMFromRaw(TaskBaseLoadData):
    """
    从外部文件加载 4D-STEM 数据的 Task。

    将自动在 HDF5 文件中创建一个 Object 并导入数据。

    Load 4D-STEM data from outside file.

    Will create an object in the HDF5 file automatically.
    """
    def __init__(
        self, 
        shape: Tuple,
        file_path: str,
        item_parent_path: str,
        item_name: str,
        offset_to_first_image: int = 0,
        gap_between_images: int = 0,
        scalar_type: str = 'float',
        scalar_size: int = 4,
        little_endian: bool = True,
        is_flipped = False,
        rotate90: int = 0,
        parent: QObject = None, 
        **meta,
    ):
        """
        arguments:
            parent: (QObject)

            shape: (Tuple) The shape of the 4D-STEM dataset, must be like
                (scan_i, scan_j, dp_i, dp_j)

            file_path: (str) The absolute path of the ouside raw file.

            item_parent_path: (str) The path of the parent group of the Dataset 
                item in the HDF file.

            item_name: (str) The name of the new Dataset item in the HDF file.

            offset_to_first_image: (int) The offset bytes before the first image.

            gap_between_images: (int) The offset bytes between two images.

            scalar_type: (str) Must be one of these: ('float', 'int', 'uint',)

            scalar_size: (int) How many bytes of one scalar number. Must be one 
                of these: (1, 2, 4,)

            little_endian: (bool) Is the raw data little-endian or big-endian? 
                Default is True.

            is_flipped: (bool) Whether the data should be transposed when 
                reading. Default is False.

            rotate90: (int) How many times should the data be rotated 90 degree
                counter-clockwise. Default is 0. In some cases, the coordinate 
                of the source data is xy, but in 4D-Explorer we use ij, so we 
                must rotate every diffraction pattern 90° when loading the 
                4D-STEM dataset.

            **meta: (key word arguments) other meta data that should be stored
                in the attrs of HDF5 object.
        """
        super().__init__(
            shape,
            file_path, 
            item_parent_path, 
            item_name, 
            parent, 
            **meta,
        )

        self._scalar_type = scalar_type
        self._scalar_size = scalar_size
        self._little_endian = little_endian
        self._offset_to_first_image = offset_to_first_image
        self._gap_between_images = gap_between_images
        self._is_flipped = is_flipped
        self._rotate90 = rotate90 

        self.name = 'Load 4D-STEM data'
        self.comment = (
            'Load 4D-STEM data\n'
            'Data File path: {0}\n'
            'To Dataset Object: {1}\n'.format(
                self._file_path, self._item_name 
            )
        )

        self.setPrepare(self._createDataset)

        self._bindSubtask()
        
    @property 
    def dtype(self) -> str:
        return getDType(
            self._scalar_type, 
            self._scalar_size, 
            self._little_endian
        )

    # def setHeaderPath(self, path: str):
    #     """
    #     arguments:
    #         path: (str) The absolute path of the header file of 4D-STEM data.
    #             This attribute can be the same as the file_path, although this
    #             usually indicates a header file that descripte experimental
    #             parameters of the 4D-STEM dataset. 
    #     """
    #     if not isinstance(path, str):
    #         raise TypeError('path must be a str, not '
    #             '{0}'.format(type(path).__name__))
        
    #     if not os.path.isfile(path):
    #         raise OSError('path is not a file: {0}'.format(path))
        
    #     self._header_path = path 

    def setShape(self, shape: tuple[int]):
        """
        arguments:
            shape: (scan_i, scan_j, dp_i, dp_j) Must be a tuple with length 4.
        """
        return super(TaskLoadFourDSTEMFromRaw, self).setShape(shape)

    # def setMeta(self, meta: dict):
    #     """
    #     arguments:
    #         meta: (dict) The experimental parameters of the 4D-STEM data.
    #     """
    #     if not isinstance(meta, Mapping):
    #         raise TypeError('meta must be a dict, not '
    #             '{0}'.format(type(meta).__name__))
    #     self._meta = meta 
   
    def _createDataset(self):
        """
        Will create a dataset in HDF5 file according to the item_path.

        This function works as the preparing function that will be called
        just before the task is submitted.
        """
        
        self.hdf_handler.addNewData(
            self._item_parent_path,
            self._item_name,
            self._shape,
            self.dtype,
        )

        for key, value in self._meta.items():
            self.hdf_handler.file[self.item_path].attrs[key] = value 

    def _bindSubtask(self):
        """
        Add subtask, which is the practical worker.
        """
        scan_i, scan_j, dp_i, dp_j = self._shape
        self.addSubtaskFuncWithProgress(
            'Copy Data', 
            readFourDSTEMFromRaw,
            raw_path = self._file_path,
            item_path = self.item_path,
            dp_i = dp_i,
            dp_j = dp_j,
            scan_i = scan_i,
            scan_j = scan_j,
            scalar_type = self._scalar_type,
            scalar_size = self._scalar_size,
            offset_to_first_image = self._offset_to_first_image,
            gap_between_images = self._gap_between_images,
            little_endian = self._little_endian,
            is_flipped = self._is_flipped,
            rotate90 = self._rotate90,
        )

    def _showFourDSTEM(self):
        """
        Will open the 4D-STEM dataset in the HDF5 object.

        This function works as the following function that will be called
        just after the task is completed.
        """
        self.logger.debug('Task {0} completed.'.format(self.name))
        # action = ActionShowFourDSTEM(item_path = self.item_path)
        # action.trigger()

# class SubtaskLoadFourDSTEMFromRaw(SubtaskWithProgress):
#     """
#     The subtask to load 4D-STEM dataset from
#     """
#     def __init__(self, parent = None,):
#         super().__init__(parent)
    
#     def setArgs(
#         self, 

#     )

    
class TaskLoadTiff(TaskBaseLoadData):
    """
    把外部 Tiff 图片中加载进 HDF5 文件中的任务。

    Task to load tiff image into the HDF5 file.
    """
    def __init__(self,
        file_path: str,
        item_parent_path: str,
        item_name: str,
        parent: QObject = None,
        **meta,
    ):
        """
        arguments:
            file_path: (str) The absolute path of the ouside raw file.

            item_parent_path: (str) The path of the parent group of the Dataset 
                item in the HDF file.

            item_name: (str) The name of the new Dataset item in the HDF file.

            parent: (QObject)

            **meta: (key word arguments) other meta data that should be stored
                in the attrs of HDF5 object.
        """
        super().__init__(
            (1,), 
            file_path, 
            item_parent_path, 
            item_name, 
            parent, 
            **meta
        )
        self.name = 'Load TIFF data'
        self.comment = (
            'Load TIFF data\n'
            'Data File path: {0}\n'
            'To Dataset Object: {1}\n'.format(
                self._file_path, self._item_name 
            )
        )
        self.setPrepare(self._createDataset)
        self.addSubtaskFunc(
            'Copy Data',
            self.copyFromTiff,
            file_path = self._file_path,
            item_path = self.item_path,
        )

    def _createDataset(self):
        """
        Will create a dataset in HDF5 file according to the item_path.

        This function works as the preparing function that will be called
        just before the task is submitted.
        """
        with Image.open(self._file_path) as im:
            self.setShape((im.height, im.width))

        self.hdf_handler.addNewData(
            self._item_parent_path,
            self._item_name,
            self._shape,
        )

        for key, value in self._meta.items():
            self.hdf_handler.file[self.item_path].attrs[key] = value 

    def copyFromTiff(self, file_path: str, item_path: str):
        """
        Do the actual copy-data work.

        arguments:
            file_path: (str) the image's path in the file system.

            item_path: (str) the loaded image's path in HDF5 file.
        """
        with Image.open(file_path) as im:
            dataset = self.hdf_handler.file[item_path]
            dataset[:] = np.asarray(im) 

    def _showImage(self):
        """
        Will open the 4D-STEM dataset in the HDF5 object.

        This function works as the following function that will be called
        just after the task is completed.
        """
        self.logger.debug('Task {0} completed.'.format(self.name))
