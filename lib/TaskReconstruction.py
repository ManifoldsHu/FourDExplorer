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
from lib.FourDSTEMMapping import CalculateCenterOfMass, CalculateVirtualImage
from lib.VectorFieldOperators import Divergence2D, Potential2D, Curl2D

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

            image_parent_path: (str) the parent group's path of the new image.

            image_name: (str) the reconstructed image's name.

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
        self.setFollow(self._showImage)
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



class TaskCenterOfMass(Task):
    """
    进行使用质心法计算差分相位衬度像的任务。

    Task to calculate CoM vector fields.
    """
    def __init__(
        self,
        item_path: str,
        image_parent_path: str,
        calc_dict: dict,
        names_dict: dict,
        metas_dict: dict,
        mask: np.ndarray = None,
        is_com_inverted = False,
        is_mean_set_to_zero = True,
        parent: QObject = None,
    ):
        """
        arguments:
            item_path: (str) the 4D-STEM dataset path

            image_parent_path: (str) the group where results will be saved

            calc_dict: (dict) which modes should be calculated. There are 5
                modes: CoM, CoMi, CoMj, dCoM, iCoM

            names_dict: (dict) the result dataset's names of each mode.

            metas_dict: (dict) the result dataset's metadata of each mode.

            mask: (np.ndarray) the region of calculating. If None, all of the
                matrix will contribute to the result.

            is_com_inverted: (bool) whether the result vector field to be 
                follow inverted direction. If True, The vector field will 
                follow the direction of the projection electric field of the 
                sample. It is inverted from the center of mass, due to negative 
                charge of the electron beam.

            is_mean_set_to_zero: (bool) The vector field result will be 
                subtracted from the mean vector. 

            parent: (QObject)
        """
        super(TaskCenterOfMass, self).__init__(parent)
        self._item_path = item_path
        self._image_parent_path = image_parent_path
        self._calc_dict = calc_dict
        self._names_dict = names_dict
        self._metas_dict = metas_dict
        self._mask = mask 
        self._is_com_inverted = is_com_inverted
        self._is_mean_set_to_zero = is_mean_set_to_zero

        self.name = 'CoM Reconstruction'
        self.comment = (
            'Center of Mass Reconstruction From 4D-STEM.\n'
            '4D-STEM dataset path: {0}\n'
            'Reconstruction is saved in: {1}\n'.format(
                self._item_path, self._image_parent_path
            )
        )

        self.setPrepare(self._createImages)
        self._bindSubtask()
        self.setFollow(self._showImage)
    
    @property
    def stem_path(self) -> str:
        """
        The 4D-STEM dataset's path.
        """
        return self._item_path 

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler

    def _createImages(self):
        """
        Will create multiple datasets in HDF5 file according to the calc_dict.

        This function works as the preparing function that will be called just
        before the task is submitted.
        """
        data_object = self.hdf_handler.file[self.stem_path]
        scan_i, scan_j, dp_i, dp_j = data_object.shape
        for com_mode, is_calced in self._calc_dict.items():
            if is_calced:
                if com_mode == 'CoM':
                    shape = (2, scan_i, scan_j)
                else:
                    shape = (scan_i, scan_j)

                self.hdf_handler.addNewData(
                    self._image_parent_path,
                    self._names_dict[com_mode],
                    shape,
                    'float64',
                )

                for key, value in self._metas_dict[com_mode].items():
                    data_path = self._getDataPath(com_mode)
                    self.hdf_handler.file[data_path].attrs[key] = value

    def _getDataPath(self, com_mode: str) -> str:
        """
        Returns the path of the created dataset according to com_mode.

        arguments:
            com_mode: (str) must be one of 'CoM', 'CoMi', 'CoMj', 'dCoM' 
                and 'iCoM'.

        returns:
            (str)
        """
        if self._image_parent_path == '/':
            return self._image_parent_path + self._names_dict[com_mode]
        else:
            return self._image_parent_path + '/' + self._names_dict[com_mode]

    def _bindSubtask(self):
        """
        Add subtask, which is the practical worker.
        """
        self.addSubtaskFuncWithProgress(
            'Calculating Center of Mass',
            self._workerCenterOfMass,
        )

    def _workerCenterOfMass(self, progress_signal: Signal = None):
        """
        Calculate the Center of Mass (CoM) distribution of the 4D-STEM dataset.
        The origin of the diffraction plane is set to the center of the 
        diffraction patterns.
        """
        data_object = self.hdf_handler.file[self.stem_path]
        scan_i, scan_j, dp_i, dp_j = data_object.shape

        com_i, com_j = CalculateCenterOfMass(
            self.stem_path, 
            self._mask, 
            progress_signal,
        )
        
        if self._is_mean_set_to_zero:
            com_i = com_i - np.mean(com_i)
            com_j = com_j - np.mean(com_j)
        
        if self._is_com_inverted:
            com_i = - com_i 
            com_j = - com_j 

        com_vec = np.zeros((2, scan_i, scan_j))
        com_vec[0, :, :] = com_i 
        com_vec[1, :, :] = com_j 
        result_dict = {
            'CoM': com_vec,
            'CoMi': com_i,
            'CoMj': com_j,
            'dCoM': Divergence2D(com_i, com_j),
            'iCoM': Potential2D(com_i, com_j),
        }

        for com_mode, is_calced in self._calc_dict.items():
            if is_calced:
                data_path = self._getDataPath(com_mode)
                self.hdf_handler.file[data_path][:] = result_dict[com_mode]
                
    def _showImage(self):
        """
        Will open the reconstructed image in the HDF5 object.

        This function works as the following function that will be called
        just after the task is completed.
        """
        self.logger.debug('Task {0} completed.'.format(self.name))
        


