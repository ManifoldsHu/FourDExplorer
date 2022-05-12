# -*- coding: utf-8 -*-

"""
*----------------------------- ReadBinary.py ---------------------------------*
提供了将 4D-STEM 数据集映射为二维图像的一些函数。

作者：          胡一鸣
创建时间：      2022年4月29日

Here provides some functions to map 4D-STEM to 2D images.

author:         Hu Yiming
date:           Apr 29, 2022
*----------------------------- ReadBinary.py ---------------------------------*
"""

from typing import Iterable
from threading import Lock

from PySide6.QtCore import Signal
import h5py
import numpy as np



def MapFourDSTEM(
    item_path: str, 
    filters: Iterable[np.ndarray|h5py.Dataset],
    results: Iterable[np.ndarray|h5py.Dataset],
    progress_signal: Signal = None,
) -> list[np.ndarray]:
    """
    Map 4D-STEM dataset into a 2D image, according to the distribution dist.

    The result are calculated by this proceed:
        - Calculate the product of diffraction patterns and the filter (number 
            by number). This gives modulated patterns.
            
        - Calculate the sum of each pattern. Now every pattern is map to a new
            number.

        - Those numbers are the elements of the result image.

    Considering the fact that in some cases the dtype of the 4D-STEM dataset is
    like 'uint8' or something else. When doing calculation, result numbers may
    exceed the maximum of the dtype (stack overflow) especially for integers. 
    So here the dtype of the result is set to 'float64'. And whatever the dtype
    of the 4D-STEM is, it will be casted to 'float64'.

    arguments:
        item_path: (str) the 4D-STEM data's path in HDF5 file.

        filters: (Iterable[np.ndarray, h5py.Dataset]) the distribution of 
            mapping. The shape must be the same as the last two dimensions of 
            the 4D-STEM dataset. If is str, will use the data_object in the
            HDF file.

        results: (Iterable[np.ndarray, h5py.Dataset]) the result matrices where 
            calculation result will be saved. In these result matrices there 
            may exist other thread reading or writing concurrently.

    returns:
        (list[np.ndarray]) a list of mapped image whose shape is the same as 
            the first two dimensions (scanning coordinates) of the 4D-STEM 
            dataset.
    """
    global qApp 
    hdf_handler = qApp.hdf_handler
    dataset = hdf_handler.file[item_path]
    if len(dataset.shape) != 4:
        raise IndexError('dataset must be a 4-dimensional matrix')
    if progress_signal is None:
        progress_signal = Signal(int)

    scan_i, scan_j, dp_i, dp_j = dataset.shape
    
    for filter in filters:
        if not isinstance(filter, (np.ndarray, h5py.Dataset)):
            raise TypeError('filter must be a list of np.ndarray, not'
                '{0}'.format(type(filter).__name__))
        if (filter.shape[0] != dp_i or filter.shape[1] != dp_j):
            raise IndexError('the shape of the filter must be the same as '
                'the diffraction patterns shape of the 4D-STEM dataset.')

    for result in results:
        if not isinstance(result, (np.ndarray, h5py.Dataset)):
            raise TypeError('result must a list of np.ndarray, not'
                '{0}'.format(type(result).__name__))
        if (result.shape[0] != scan_i or result.shape[1] != scan_j):
            raise IndexError('the shape of the result matrices must be the'
                'same as the scanning coordinates of the 4D-STEM dataset')

    # if isinstance(filters, (np.ndarray, h5py.Dataset, str)):
    #     filters = [filters]
    # for filter in filters:
    #     if isinstance(filter, str):
    #         filter = hdf_handler.file[filter]
    

    
    # if results is None:
    #     results = [np.zeros((scan_i, scan_j)) for _ in filters]
    # elif isinstance(results, (np.ndarray, h5py.Dataset, str)):
    #     results = [results]

    # _results = []

    # for result in results:
    #     if isinstance(result, str):
    #         _results.append(hdf_handler.file[result])
    #     else:
            
    #         _results.append(result)

    result_lock = Lock()
    for ii in range(scan_i):
        for jj in range(scan_j):
            dp = np.asarray(dataset[ii, jj, :, :], dtype = 'float64')
            for result, filter in zip(results, filters):
                with result_lock:
                    result[ii, jj] = np.sum(dp*filter)
        progress_signal.emit(int(ii/scan_i*100))

    return results


def CalculateVirtualImage(
    item_path: str,
    mask: np.ndarray|h5py.Dataset,
    result_path: str,
    progress_signal: Signal = None,
) -> np.ndarray:
    """
    Calculate the Virtual Image of the 4D-STEM dataset.

    arguments:
        item_path: (str) the 4D-STEM data's path in HDF5 file.

        mask: (np.ndarray or h5py.Dataset) the integration region of the 
            virtual electron detector. The shape must be the same as the last 
            two dimensions of the 4D-STEM dataset.

        result: (str) the HDF object path to store the result.

    returns:
        (np.ndarray) the reconstructed virtual image whose shape is the same as
            the first two dimensions (scanning coordinates) of the 4D-STEM 
            dataset.
    """
    global qApp
    hdf_handler = qApp.hdf_handler
    result_object = hdf_handler.file[result_path]
    return MapFourDSTEM(item_path, [mask], [result_object], progress_signal)

    # if result is None:
    #     result, = MapFourDSTEM(item_path, (mask,), progress_signal)
    # else:
    #     result, = MapFourDSTEM(item_path, (mask,), (result,), progress_signal)
    # return result


def CalculateCenterOfMass(
    item_path: str,
    mask: np.ndarray|h5py.Dataset|str = None,
    result_com_i: np.ndarray|h5py.Dataset|str = None,
    result_com_j: np.ndarray|h5py.Dataset|str = None,
    progress_signal: Signal = None,
) -> tuple[np.ndarray]:
    """
    Calculate the Center of Mass (CoM) distribution of the 4D-STEM dataset.
    The origin of the diffraction plane is set to the center of the diffraction
    patterns.

    arguments:
        item_path: (str) the 4D-STEM data's path in HDF5 file.

        mask: (np.ndarray or h5py.Dataset) the region of diffraction patterns
            that contributes to the center of mass distributions.

        result_com_i: (np.ndarray or h5py.Dataset) the array to store the 
            result of i-direction center of mass distribution.

        result_com_j: (np.ndarray or h5py.Dataset) the array to store the 
            result of j-direction center of mass distribution.

    returns:
        (tuple[np.ndarray]) this function will return two matrices CoM_i and 
            CoM_j. Both matrices' shapes are the same as the first two 
            dimensions (scanning coordinates) of the 4D-STEM dataset. 
    """
    global qApp 
    hdf_handler = qApp.hdf_handler
    dataset = hdf_handler.file[item_path]
    if len(dataset.shape) != 4:
        raise IndexError('dataset must be a 4-dimensional matrix')
    
    scan_i, scan_j, dp_i, dp_j = dataset.shape
    center_i = (dp_i - 1)/2
    center_j = (dp_j - 1)/2
    array_i = np.linspace(- center_i, dp_i - center_i - 1, dp_i)
    array_j = np.linspace(- center_j, dp_j - center_j - 1, dp_j)
    vec_i, vec_j = np.meshgrid(array_i, array_j, indexing = 'ij')

    if mask is None:
        mask = np.ones(dp_i, dp_j)
    filters = (vec_i*mask, vec_j*mask)

    if result_com_i is None:
        result_com_i = np.zeros((scan_i, scan_j))
    if result_com_j is None:
        result_com_j = np.zeros((scan_i, scan_j))
    results = (result_com_i, result_com_j)

    return MapFourDSTEM(item_path, filters, results, progress_signal)

