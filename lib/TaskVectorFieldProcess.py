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
from lib.VectorFieldOperators import Divergence2D, Curl2D, Potential2D

class TaskBaseVectorToVector(TaskBaseReconstruct):
    """
    从 Vector Field 中产生一个 Vector Field 的任务的基类。

    Base task of producing an vector field from a vector field.
    """
    def __init__(
        self,
        item_path: str,
        image_parent_path: str,
        image_name: str,
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
        self.comment = (
            '{0}.\n'
            'Vector Field dataset path: {1}\n'
            'Result is saved in: {2}\n'.format(
                self.name, self._item_path, self._image_name
            )
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

    def _showVectorField(self):
        """
        Will open the reconstructed image in the HDF5 object.

        This function works as the following function that will be called
        just after the task is completed.
        """
        self.logger.debug('Task {0} completed.'.format(self.name))


class TaskRotateVectorAngle(TaskBaseVectorToVector):
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

    def _calculateRotation(self):
        """
        returns:
            (h5py.Dataset)
        """
        data_object = self.hdf_handler.file[self.source_path]
        vec_i = data_object[0, :, :]
        vec_j = data_object[1, :, :]
        angle_rad = self._angle * np.pi / 180
        new_vec_i = vec_i * np.cos(angle_rad) - vec_j * np.sin(angle_rad)
        new_vec_j = vec_i * np.sin(angle_rad) + vec_j * np.cos(angle_rad)

        new_image = self.hdf_handler.file[self.image_path]
        new_image[0, :, :] = new_vec_i 
        new_image[1, :, :] = new_vec_j
        return new_image
        

class TaskSubtractVectorOffset(TaskBaseVectorToVector):
    """
    对矢量场中的每一个矢量都减去一个平均矢量。

    Subtract every vector by a mean vector.
    """
    def __init__(
        self,
        item_path: str,
        image_parent_path: str,
        image_name: str,
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

        self.name = 'Subtract Vector Field Offset'
        self.comment = (
            'Subtract every vector\'s offset.\n'
            'Source vector field dataset path: {0}\n'
            'Result is saved in: {1}\n'.format(
                self._item_path, self._image_name
            )
        )
        

        self.addSubtaskFunc(
            'Calculating Subtraction',
            self._calculateSubtraction,
        )

    def _calculateSubtraction(self):
        """
        returns:
            (h5py.Dataset)
        """
        data_object = self.hdf_handler.file[self.source_path]
        vec_i = data_object[0, :, :]
        vec_j = data_object[1, :, :]

        new_vec_i = vec_i - np.mean(vec_i)
        new_vec_j = vec_j - np.mean(vec_j)

        new_image = self.hdf_handler.file[self.image_path]
        new_image[0, :, :] = new_vec_i 
        new_image[1, :, :] = new_vec_j
        return new_image
        

class TaskFlipVectorField(TaskBaseVectorToVector):
    """
    将矢量场的 i,j 分量进行对换。

    Exchange the i, j components of the vector fields.
    """
    def __init__(
        self,
        item_path: str,
        image_parent_path: str,
        image_name: str,
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

        self.name = 'Flip Vector Field'
        self.comment = (
            'Exchange i,j Components of Vector Field.\n'
            'Source vector field dataset path: {0}\n'
            'Result is saved in: {1}\n'.format(
                self._item_path, self._image_name
            )
        )

        self.addSubtaskFunc(
            'Exchange Components',
            self._exchangeComponent,
        )

    def _exchangeComponent(self):
        """
        returns:
            (h5py.Dataset)
        """
        data_object = self.hdf_handler.file[self.source_path]
        vec_i = data_object[0, :, :]
        vec_j = data_object[1, :, :]
        new_image = self.hdf_handler.file[self.image_path]
        new_image[0, :, :] = vec_j 
        new_image[1, :, :] = vec_i
        return new_image 


class TaskBaseVectorToImage(TaskBaseReconstruct):
    """
    从 Vector Field 中产生一个图像的任务的基类。

    Base task of producing an image from a vector field.
    """
    def __init__(
        self, 
        item_path: str, 
        image_parent_path: str, 
        image_name: str, 
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
        self.setPrepare(self._createImage)
        self.setFollow(self._showImage)
        self.comment = (
            '{0}.\n'
            'Vector Field dataset path: {1}\n'
            'Result is saved in: {2}\n'.format(
                self.name, self._item_path, self._image_name
            )
        )

    @property
    def stem_path(self) -> None:
        """
        Will raise an Attribute Error. Use source_path instead.
        """
        raise AttributeError('There is no 4D-STEM path in this task.')

    @property
    def source_path(self) -> str:
        return self._item_path 

    def _createImage(self):
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
            (height, width),
            'float64',
        )

        for key, value in self._meta.items():
            self.hdf_handler.file[self.image_path].attrs[key] = value 

    def _showImage(self):
        """
        Will open the reconstructed image in the HDF5 object.

        This function works as the following function that will be called
        just after the task is completed.
        """
        self.logger.debug('Task {0} completed.'.format(self.name))


class TaskPotential(TaskBaseVectorToImage):
    """
    计算矢量场的势的 Task。

    Task to calculate potential of vector field.
    """
    def __init__(
        self, 
        item_path: str, 
        image_parent_path: str, 
        image_name: str, 
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

        self.name = 'Calcuate Potential'
        
        self.addSubtaskFunc(
            'Calculating Potential',
            self._calculatePotential,
        )

    def _calculatePotential(self):
        """
        returns:
            (h5py.Dataset)
        """
        data_object = self.hdf_handler.file[self.source_path]
        vec_i = data_object[0, :, :]
        vec_j = data_object[1, :, :]

        potential = Potential2D(vec_i, vec_j)

        new_image = self.hdf_handler.file[self.image_path]
        new_image[:] = potential
        return new_image



class TaskDivergence(TaskBaseVectorToImage):
    """
    计算矢量场的散度的 Task。

    Task to calculate divergence of vector field.
    """
    def __init__(
        self, 
        item_path: str, 
        image_parent_path: str, 
        image_name: str, 
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

        self.name = 'Calculate Divergence'

        self.addSubtaskFunc(
            'Calculating Divergence',
            self._calculateDivergence,
        )

    def _calculateDivergence(self):
        """
        returns:
            (h5py.Dataset)
        """
        data_object = self.hdf_handler.file[self.source_path]
        vec_i = data_object[0, :, :]
        vec_j = data_object[1, :, :]

        divergence = Divergence2D(vec_i, vec_j)

        new_image = self.hdf_handler.file[self.image_path]
        new_image[:] = divergence 
        return new_image


class TaskCurl(TaskBaseVectorToImage):
    """
    计算矢量场的旋度的 Task。

    Task to calculate curl of vector field.
    """
    def __init__(
        self, 
        item_path: str, 
        image_parent_path: str, 
        image_name: str, 
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

        self.name = 'Calculate Curl'

        self.addSubtaskFunc(
            'Calculating Curl',
            self._calculateCurl,
        )

    def _calculateCurl(self):
        """
        returns:
            (h5py.Dataset)
        """
        data_object = self.hdf_handler.file[self.source_path]
        vec_i = data_object[0, :, :]
        vec_j = data_object[1, :, :]

        divergence = Curl2D(vec_i, vec_j)

        new_image = self.hdf_handler.file[self.image_path]
        new_image[:] = divergence 
        return new_image


class TaskSliceI(TaskBaseVectorToImage):
    """
    计算矢量场 i 方向分量的任务

    Task to slice i-component of the vector field.
    """
    def __init__(
        self, 
        item_path: str, 
        image_parent_path: str, 
        image_name: str, 
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

        self.name = 'Slice Vector Field (i-component)'

        self.addSubtaskFunc(
            'Slicing',
            self._slicing_i,
        )

    def _slicing_i(self):
        """
        returns:
            (h5py.Dataset)
        """
        data_object = self.hdf_handler.file[self.source_path]
        vec_i = data_object[0, :, :]
        new_image = self.hdf_handler.file[self.image_path]
        new_image[:] = vec_i 
        return new_image 


class TaskSliceJ(TaskBaseVectorToImage):
    """
    计算矢量场 j 方向分量的任务

    Task to slice j-component of the vector field.
    """
    def __init__(
        self, 
        item_path: str, 
        image_parent_path: str, 
        image_name: str, 
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

        self.name = 'Slice Vector Field (j-component)'

        self.addSubtaskFunc(
            'Slicing',
            self._slicing_j,
        )

    def _slicing_j(self):
        """
        returns:
            (h5py.Dataset)
        """
        data_object = self.hdf_handler.file[self.source_path]
        vec_j = data_object[1, :, :]
        new_image = self.hdf_handler.file[self.image_path]
        new_image[:] = vec_j 
        return new_image 

