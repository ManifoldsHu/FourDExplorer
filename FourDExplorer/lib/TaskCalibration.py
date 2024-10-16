# -*- coding: utf-8 -*-

"""
*---------------------------- TaskCalibration.py --------------------------------*
包含读取 4D-STEM 数据、计算 Calibration 并产生新的 4D-STEM 的任务。

作者:           胡一鸣
创建日期:       2022年5月26日

This module includes tasks calculate Virtual Image of 4D-STEM dataset.

author:         Hu Yiming
date:           May 26, 2022
*---------------------------- TaskCalibration.py --------------------------------*
"""

from logging import Logger

from PySide6.QtCore import QObject, Signal 
import h5py
import numpy as np

from bin.TaskManager import Subtask, SubtaskWithProgress, Task
from bin.HDFManager import HDFHandler
from bin.Widgets.WidgetMasks import WidgetMaskBase
from lib.FourDSTEMModifying import FilteringDiffractionPattern
from lib.FourDSTEMModifying import RollingDiffractionPattern
from lib.FourDSTEMModifying import TranslatingDiffractionPattern
from lib.FourDSTEMModifying import RotatingDiffractionPattern
from lib.FourDSTEMModifying import SubtractBackground


class TaskBaseFourDSTEMModify(Task):
    """
    对 4D-STEM 数据集进行修改的任务。

    The base task to modify 4D-STEM dataset.
    """
    def __init__(
        self, 
        item_path: str, 
        output_parent_path: str,
        output_name: str,
        parent: QObject = None,
        meta: dict = None 
    ):
        """
        arguments:
            item_path: (str) the source 4D-STEM dataset path.

            output_parent_path: (str) the parent group's path of the modified 
                4D-STEM dataset.

            output_name: (str) the new modified 4D-STEM dataset's name.

            parent: (QObject)

            **meta: (key word arguments) other meta data that should be stored
                in the attrs of reconstructed HDF5 object
        """
        super().__init__(parent)
        self._item_path = item_path 
        self._output_parent_path = output_parent_path
        self._output_name = output_name 
        self._meta = {}
        if meta:
            self._meta.update(meta) 
        self.name = '4D-STEM Modifying'
        self.comment = (
            '4D-STEM Modifying.\n'
            'Source 4D-STEM dataset path: {0}\n'
            'Modified 4D-STEM is saved in: {1}\n'.format(
                self._item_path, self._output_name
            )
        )
        self.setPrepare(self._createFourDSTEM)
        self.setFollow(self._showFourDSTEM)

    @property
    def source_path(self) -> str:
        """
        The 4D-STEM dataset's path.
        """
        return self._item_path

    @property 
    def output_path(self) -> str:
        """
        The output (modified) 4D-STEM dataset path.
        """
        if self._output_parent_path == '/':
            return self._output_parent_path + self._output_name
        else:
            return self._output_parent_path + '/' + self._output_name

    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger 
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler 

    def updateMeta(self, **meta):
        """
        Update metadata. The new attributes will be added.
        """
        for key in meta:
            try:
                self._meta[key] = meta[key]
            except Exception as e:
                self.logger.error(f'Failed to update metadata for key {key}: {e}')

    def _createFourDSTEM(self):
        """
        Will create a dataset in HDF5 file according to the output path.

        If the output path is the same as the item_path, the source dataset 
        will be covered. Otherwise, if there has existed an item at the 
        output path, hdf_handler will raise an exception.

        This function works as the preparing function that will be called 
        just before the task is submitted.
        """
        print('output_path: {0}'.format(self.output_path))
        
        if self.output_path != self.source_path:
            data_object = self.hdf_handler.file[self.source_path]
            # scan_i, scan_j, dp_i, dp_j = data_object.shape 
            self.hdf_handler.addNewData(
                self._output_parent_path,
                self._output_name,
                shape = data_object.shape,
                dtype = data_object.dtype,
            )

        for key, value in self._meta.items():
            try:
                self.hdf_handler.file[self.output_path].attrs[key] = value
            except Exception as e:
                self.logger.error(f'Failed to set attribute {key} for dataset {self.output_path}: {e}')

    def _showFourDSTEM(self):
        """
        TODO

        This function works as the following function that will be called just 
        after the task is completed.
        """
        self.logger.debug('Task {0} completed.'.format(self.name))


class TaskFourDSTEMAlign(TaskBaseFourDSTEMModify):
    """
    对 4D-STEM 数据集进行合轴的任务。

    Task to align the 4D-STEM dataset.
    """
    def __init__(
        self,
        item_path: str,
        output_parent_path: str,
        output_name: str,
        translation_vector: tuple,
        parent: QObject = None,
        meta: dict = None,
    ):
        """
        arguments:
            item_path: (str) the source 4D-STEM dataset path.

            output_parent_path: (str) the parent group's path of the modified 
                4D-STEM dataset.

            output_name: (str) the new modified 4D-STEM dataset's name.

            translation_vector: (tuple) the displacement vector of every 
                diffraction pattern.

            parent: (QObject)

            **meta: (key word arguments) other meta data that should be stored
                in the attrs of reconstructed HDF5 object
        """
        super().__init__(
            item_path, 
            output_parent_path, 
            output_name, 
            parent, 
            meta,
        )
        self._translation_vector = translation_vector
        
        self.name = '4D-STEM Alignment'

        self.addSubtaskFuncWithProgress(
            'Rolling Diffraction Patterns',
            RollingDiffractionPattern,
            item_path = self.source_path,
            translation_vector = self._translation_vector,
            result_path = self.output_path,
        )


class TaskFourDSTEMAlignMapping(TaskBaseFourDSTEMModify):
    """
    使用已有的衍射盘偏移矢量分布映射，对数据集进行合轴的任务。
    
    Task to align the 4D-STEM dataset using an existing diffraction disk offset vector distribution map.
    """
    def __init__(
        self,
        item_path: str,
        output_parent_path: str,
        output_name: str,
        shift_mapping: np.ndarray | h5py.Dataset,
        parent: QObject = None,
        meta: dict = None,
    ):
        super().__init__(item_path, output_parent_path, output_name, parent, meta)
        self._shift_mapping = shift_mapping 
        self.name = '4D-STEM Alignment With Shift Mapping'
        
        self.addSubtaskFuncWithProgress(
            'Translating Diffraction Patterns',
            TranslatingDiffractionPattern,
            item_path = self.source_path,
            shift_mapping = shift_mapping,
            result_path = self.output_path
        )
        
    


class TaskFourDSTEMFiltering(TaskBaseFourDSTEMModify):
    """
    对 4D-STEM 数据集进行抠背底的任务。

    Task to subtract background for 4D-STEM dataset (by filtering).
    """
    def __init__(
        self,
        item_path: str,
        output_parent_path: str,
        output_name: str,
        window_min: float = None,
        window_max: float = None,
        parent: QObject = None,
        meta: dict = None,
    ):
        """
        arguments:
            item_path: (str) the source 4D-STEM dataset path.

            output_parent_path: (str) the parent group's path of the modified 
                4D-STEM dataset.

            output_name: (str) the new modified 4D-STEM dataset's name.

            window_min: (float) the minimum value of the window. Any value in 
                the dataset that smaller than this will be set to zero. If it
                is None, no minimum edge is applied.

            window_max: (float) the maximum value of the window. Any value in
                the dataset that larger than this will be set to the window_max
                value. If it is None, no maximum edge is applied.

            parent: (QObject)

            **meta: (key word arguments) other meta data that should be stored
                in the attrs of reconstructed HDF5 object
        """
        super().__init__(
            item_path, 
            output_parent_path, 
            output_name, 
            parent, 
            meta
        )

        self.name = '4D-STEM Background Subtraction'
        self._window_min = window_min
        self._window_max = window_max 
        self.addSubtaskFuncWithProgress(
            'Window Filtering Diffraction Patterns',
            FilteringDiffractionPattern,
            item_path = self.source_path,
            window_min = self._window_min,
            window_max = self._window_max,
            result_path = self.output_path,
        )
    

class TaskFourDSTEMRotate(TaskBaseFourDSTEMModify):
    """
    对 4D-STEM 数据集进行旋转的任务。

    Task to rotate diffraction patterns for 4D-STEM dataset.
    """
    def __init__(
        self,
        item_path: str,
        output_parent_path: str,
        output_name: str,
        rotation_angle: float,
        parent: QObject = None,
        meta: dict = None,
    ):
        """
        arguments:
            item_path: (str) the source 4D-STEM dataset path.

            output_parent_path: (str) the parent group's path of the modified 
                4D-STEM dataset.

            output_name: (str) the new modified 4D-STEM dataset's name.

            rotation_angle: (float) the rotation angle of every diffraction 
                pattern. (Unit: deg) 

            parent: (QObject)

            **meta: (key word arguments) other meta data that should be stored
                in the attrs of reconstructed HDF5 object
        """
        super().__init__(
            item_path, 
            output_parent_path, 
            output_name, 
            parent, 
            meta
        )
        self.name = '4D-STEM Rotate'
        self._rotation_angle = rotation_angle
        self.addSubtaskFuncWithProgress(
            'Rotate Diffraction Patterns',
            RotatingDiffractionPattern,
            item_path = self.source_path,
            rotation_angle = self._rotation_angle,
            result_path = self.output_path,
        )


class TaskFourDSTEMSubtractRef(TaskBaseFourDSTEMModify):
    """
    对 4D-STEM 数据集进行背景减去任务
    
    Task to subtract background for 4D-STEM dataset.
    """
    def __init__(
        self,
        item_path: str,
        output_parent_path: str,
        output_name: str,
        background_path: str,
        parent: QObject = None,
        meta: dict = None,
    ):
        """
        arguments:
            item_path: (str) the source 4D-STEM dataset path.
            
            output_parent_path: (str) the parent group's path of the modified 
                4D-STEM dataset.
            
            output_name: (str) the new modified 4D-STEM dataset's name.
            
            background_path: (str) the background dataset path.
            
            parent: (QObject)
            
            meta: (key word arguments) other meta data that should be stored
                in the attrs of reconstructed HDF5 object
        """
        super().__init__(
            item_path, 
            output_parent_path, 
            output_name, 
            parent, 
            meta
        )
        self.name = '4D-STEM Background Subtraction'
        self.addSubtaskFuncWithProgress(
            'Subtract Background',
            SubtractBackground,
            item_path = self.source_path,
            background_path = background_path,
            result_path = self.output_path,
        )




