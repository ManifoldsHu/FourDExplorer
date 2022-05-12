# -*- coding: utf-8 -*-

"""
*---------------------------- TaskLoadData.py --------------------------------*
包含读取 4D-STEM 数据并计算虚拟成像的任务。

作者:           胡一鸣
创建日期:       2022年4月29日

This module includes tasks calculate Virtual Image of 4D-STEM dataset.

author:         Hu Yiming
date:           Apr 29, 2021
*---------------------------- TaskLoadData.py --------------------------------*
"""

from logging import Logger

from PySide6.QtCore import QObject, Signal 
import h5py
import numpy as np

from bin.TaskManager import Subtask, SubtaskWithProgress, Task
from bin.HDFManager import HDFHandler
from bin.Widgets.WidgetMasks import WidgetMaskBase
from lib.FourDSTEMMapping import MapFourDSTEM, CalculateVirtualImage

class TaskBaseReconstruct(Task):
    """
    从 4D-STEM 数据集进行重构成像的任务基类。

    The base task to reconstruct images from 4D-STEM dataset.
    """
    def __init__(
        self, 
        item_path: str, 
        image_parent_path: str, 
        image_name: str,
        parent: QObject = None, 
        **meta
    ):
        """
        arguments:
            item_path: (str) the 4D-STEM dataset path.

            parent: (QObject)

            **meta: (key word arguments) other meta data that should be stored
                in the attrs of reconstructed HDF5 object
        """
        super().__init__(parent)
        self._item_path = item_path
        self._image_parent_path = image_parent_path
        self._image_name = image_name 
        self._meta = meta 
        self.name = 'Image Reconstruction'
        self.comment = (
            'Image Reconstruction From 4D-STEM.\n'
            '4D-STEM dataset path: {0}\n'
            'Reconstruction is saved in: {1}\n'.format(
                self._item_path, self._image_name
            )
        )

    @property
    def stem_path(self) -> str:
        """
        The 4D-STEM dataset's path.
        """
        return self._item_path 

    @property
    def image_path(self) -> str:
        """
        The reconstruction image's path.
        """
        if self._image_parent_path == '/':
            return self._image_parent_path + self._image_name
        else:
            return self._image_parent_path + '/' + self._image_name

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


class TaskVirtualImage(TaskBaseReconstruct):
    """
    进行虚拟成像的 Task.

    Task to reconstruct virtual image.
    """
    def __init__(
        self, 
        item_path: str, 
        image_parent_path: str, 
        image_name: str,
        mask: np.ndarray,
        parent: QObject = None, 
        **meta,
    ):
        super().__init__(
            item_path, 
            image_parent_path, 
            image_name, 
            parent, 
            **meta,
        )

        self._mask = mask
        self.setPrepare(self._createImage)
        self._bindSubtask()

    def _createImage(self):
        """
        Will create a dataset in HDF5 file according to the image_path.

        This function works as the preparing function that will be called
        just before the task is submitted.
        """
        data_object = self.hdf_handler.file[self.stem_path]
        scan_i, scan_j, dp_i, dp_j = data_object.shape
        self.hdf_handler.addNewData(
            self._image_parent_path,
            self._image_name,
            (scan_i, scan_j),
            'float64',
        )

        for key, value in self._meta.items():
            self.hdf_handler.file[self.image_path].attrs[key] = value 

    def _bindSubtask(self):
        """
        Add subtask, which the practical worker.
        """
        self.addSubtaskFuncWithProgress(
            'Calculating Virtual Image',
            CalculateVirtualImage,
            item_path = self.stem_path,
            mask = self._mask,
            result_path = self.image_path,
        )

    def _showImage(self):
        """
        Will open the reconstructed image in the HDF5 object.

        This function works as the following function that will be called
        just after the task is completed.
        """
        self.logger.debug('Task {0} completed.'.format(self.name))

