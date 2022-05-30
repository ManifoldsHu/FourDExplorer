# -*- coding: utf-8 -*-

"""
*------------------------- FourDSTEMModifying.py -----------------------------*
提供了整体修改 4D-STEM 数据集的函数。

作者：          胡一鸣
创建时间：      2022年5月27日

Here provides some functions to modify 4D-STEM dataset for calibration.

author:         Hu Yiming
date:           May 27, 2022

*------------------------- FourDSTEMModifying.py -----------------------------*
"""

from threading import Lock

from PySide6.QtCore import Signal
import numpy as np 
import h5py


def RollingDiffractionPattern(
    item_path,
    translation_vector,
    result_path,
    progress_signal: Signal = None,
) -> np.ndarray| h5py.Dataset:
    """
    Roll every diffraction pattern in 4D-STEM dataset to align.

    arguments:
        item_path: (str) the 4D-STEM data's path in HDF5 file.

        tranlation_vector: (tuple) the displacement vector of every diffraction
            pattern.

        result_path: (str) the HDF object path to store the result.  

    """
    global qApp
    hdf_handler = qApp.hdf_handler
    result_object = hdf_handler.file[result_path]
    data_object = hdf_handler.file[item_path]
    
    if not isinstance(data_object, (h5py.Dataset, np.ndarray)):
        raise TypeError('data object must be a np.ndarray or '
            'h5py.Dataset, not {0}'.format(type(data_object).__name__))
    if not isinstance(result_object, (h5py.Dataset, np.ndarray)):
        raise TypeError('result object must be a np.ndarray or '
            'h5py.Dataset, not {0}'.format(type(result_object).__name__))

    if result_object.shape != data_object.shape:
        raise ValueError('result object\'s shape must be the same as the '
            'source data object\'s shape.')
    
    scan_i, scan_j, dp_i, dp_j = data_object.shape 
    result_lock = Lock()
    for ii in range(scan_i):
        for jj in range(scan_j):
            with result_lock:
                result_object[ii, jj, :, :] = np.roll(
                    data_object[ii, jj, :, :],
                    translation_vector,
                    axis = (0, 1)
                )
        progress_signal.emit(int(ii/scan_i*100))

    return result_object 
        
    
def FilteringDiffractionPattern(
    item_path: str,
    result_path: str,
    window_min: float = None,
    window_max: float = None,
    progress_signal: Signal = None,
) -> np.ndarray| h5py.Dataset:
    """
    Roll every diffraction pattern in 4D-STEM dataset to align.

    arguments:
        item_path: (str) the 4D-STEM data's path in HDF5 file.

        window_min: (float) the minimum value of the filtering window.

        window_max: (float) the maximum value of the filtering window.

        result_path: (str) the HDF object path to store the result.  
    """
    global qApp
    hdf_handler = qApp.hdf_handler
    result_object = hdf_handler.file[result_path]
    data_object = hdf_handler.file[item_path]

    if not isinstance(data_object, (h5py.Dataset, np.ndarray)):
        raise TypeError('data object must be a np.ndarray or '
            'h5py.Dataset, not {0}'.format(type(data_object).__name__))
    if not isinstance(result_object, (h5py.Dataset, np.ndarray)):
        raise TypeError('result object must be a np.ndarray or '
            'h5py.Dataset, not {0}'.format(type(result_object).__name__))

    if result_object.shape != data_object.shape:
        raise ValueError('result object\'s shape must be the same as the '
            'source data object\'s shape.')

    scan_i, scan_j, dp_i, dp_j = data_object.shape 
    result_lock = Lock()
    for ii in range(scan_i):
        for jj in range(scan_j):
            with result_lock:
                dp = data_object[ii, jj, :, :]
                if window_max is not None:
                    dp[dp > window_max] = window_max
                if window_min is not None:
                    dp[dp < window_min] = 0
                result_object[ii, jj, :, :] = dp 
        progress_signal.emit(int(ii/scan_i*100))

    return result_object 

