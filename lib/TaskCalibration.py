# -*- coding: utf-8 -*-

"""
*---------------------------- TaskCalibration.py --------------------------------*
包含读取 4D-STEM 数据、计算 Calibration 并产生新的 4D-STEM 的任务。

作者:           胡一鸣
创建日期:       2022年4月29日

This module includes tasks calculate Virtual Image of 4D-STEM dataset.

author:         Hu Yiming
date:           Apr 29, 2021
*---------------------------- TaskCalibration.py --------------------------------*
"""

from logging import Logger

from PySide6.QtCore import QObject, Signal 
import h5py
import numpy as np

from bin.TaskManager import Subtask, SubtaskWithProgress, Task
from bin.HDFManager import HDFHandler
from bin.Widgets.WidgetMasks import WidgetMaskBase
from lib.FourDSTEMModifying import FilteringDiffractionPattern, RollingDiffractionPattern


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
        **meta
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
        self._meta = meta 
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
            self._meta[key] = meta[key]

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
            self.hdf_handler.file[self.output_path].attrs[key] = value 

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
        **meta,
    ):
        super().__init__(
            item_path, 
            output_parent_path, 
            output_name, 
            parent, 
            **meta
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
        window_min: float,
        window_max: float,
        parent: QObject = None,
        **meta,
    ):
        super().__init__(
            item_path, 
            output_parent_path, 
            output_name, 
            parent, 
            **meta
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
    

    



