# -*- coding: utf-8 -*-

"""
*----------------------- TaskVectorFieldProcess.py ---------------------------*
提供了用于矢量场计算的一些任务。

作者：          胡一鸣
创建时间：      2022年5月21日

Here provides some functions to calculate vector field processing.

author:         Hu Yiming
date:           May 21, 2022
*----------------------- TaskVectorFieldProcess.py ---------------------------*
"""

from logging import Logger 

from PySide6.QtCore import QObject, Signal

import h5py 
import numpy as np

from bin.TaskManager import Task 
from bin.HDFManager import HDFHandler
from lib.TaskReconstruction import TaskBaseReconstruct
from lib.VectorFieldOperators import Divergence2D, Curl2D

class TaskRotateVectorAngle(TaskBaseReconstruct):
    """
    旋转矢量场中每一个矢量的角度。

    The task to rotate every vector's angle.
    """
    def __init__(
        self,
        item_path: str,
        image_parent_path: str,
        image_name: str,
        angle: float = 0,
        parent: QObject = None,
        **meta,
    ):
        """
        arguments:
            item_path: (str) the Vector Field dataset path.

            image_parent_path: (str) the parent group's path of the new vector
                field.

            image_name: (str) the reconstructed vector field's name.

            angle: (float) the rotation angle. Unit: degree.

            parent: (QObject)

            **meta: (key word arguments) other meta data that should be stored
                in the attrs of reconstructed HDF5 object
        """
        super().__init__(
            item_path, 
            image_parent_path, 
            image_name, 
            parent, 
            **meta
        )

        self.name = 'Rotate Vector Field Angle'
        self.comment = (
            'Rotate every vector\'s angle.\n'
            'Source vector field dataset path: {0}\n'
            'Result is saved in: {1}\n'.format(
                self._item_path, self._image_name
            )
        )
        self._angle = angle 

        self.addSubtaskFunc(
            'Calculating Rotation',
            self._calculateRotation,
        )
        self.setPrepare(self._createVectorField)
        self.setFollow(self._showVectorField)

    @property
    def stem_path(self) -> None:
        """
        Will raise an Attribute Error. Use source_path instead.
        """
        raise AttributeError('There is no 4D-STEM path in this task.')

    @property
    def source_path(self) -> str:
        return self._item_path 

    def _createVectorField(self):
        """
        Will create a dataset in HDF5 file according to the image_path.

        This function works as the preparing function that will be called
        just before the task is submitted.
        """
        data_object = self.hdf_handler.file[self.source_path]
        _, height, width = data_object.shape 
        self.hdf_handler.addNewData(
            self._image_parent_path,
            self._image_name,
            (2, height, width),
            'float64',
        )

        for key, value in self._meta.items():
            self.hdf_handler.file[self.image_path].attrs[key] = value 

    # def _bindSubtask(self):
    #     """
    #     Add subtask, which is the practical worker.
    #     """
    #     self.addSubtaskFunc(
    #         'Calculating Rotation',
    #         self._calculateRotation,
    #     )
    
    def _calculateRotation(self):
        """
        """
        data_object = self.hdf_handler.file[self.source_path]
        vec_i = data_object[0, :, :]
        vec_j = data_object[1, :, :]
        angle_rad = self._angle * np.pi / 180
        new_vec_i = vec_i * np.cos(angle_rad) + vec_j * np.sin(angle_rad)
        new_vec_j = - vec_i * np.sin(angle_rad) + vec_j * np.cos(angle_rad)

        new_image = self.hdf_handler.file[self.image_path]
        new_image[0, :, :] = new_vec_i 
        new_image[1, :, :] = new_vec_j
        
    def _showVectorField(self):
        """
        Will open the reconstructed image in the HDF5 object.

        This function works as the following function that will be called
        just after the task is completed.
        """
        self.logger.debug('Task {0} completed.'.format(self.name))



