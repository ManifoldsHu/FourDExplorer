# -*- coding: utf-8 -*- 

# -*- coding: utf-8 -*-

"""
*------------------------- DiffractionAlignment.py ---------------------------*

提供了 4D-STEM 衍射图像的居中对齐所需要的算法。

作者:           胡一鸣
创建日期:       2024年9月18日

This module provides functions for aligning 4D-STEM diffraction patterns.

author:         Hu Yiming
date:           Sep 18, 2024

*------------------------- DiffractionAlignment.py ---------------------------*
"""

import numpy as np
from scipy.optimize import curve_fit

def linearModel(locations: np.ndarray, a, b, c) -> np.ndarray:
    """
    Linear model for fitting the shift map.
    
    arguments:
        locations: (np.ndarray) The locations in the format of (i, j).

        a, b, c: (float) The parameters of the linear model.
        
    returns:
        (np.ndarray) The fitted values.
    """
    i, j = locations
    return a * i + b * j + c

def fitLinearModel(locations: np.ndarray, shifts: np.ndarray) -> tuple:
    """
    Fit a linear model to the given locations and shifts.
    
    arguments:
        locations: (np.ndarray) The locations in the format of (i, j).
        shifts: (np.ndarray) The shifts corresponding to the locations.
        
    returns:
        (tuple) The optimized parameters for the linear model.
    """
    popt, _ = curve_fit(linearModel, locations.T, shifts)
    return popt

def generateShiftMapWithLinearModel(
    anchor_locations: np.ndarray, 
    anchor_shifts: np.ndarray, 
    scan_i: int, 
    scan_j: int
):
    """
    Generate the shift map using the fitted linear models.

    arguments:
        anchor_locations: (np.ndarray) The locations of the anchors.
        
        anchor_shifts: (np.ndarray) The shifts corresponding to the anchor locations.
        
        scan_i: (int) The number of scan positions in the i direction.
        
        scan_j: (int) The number of scan positions in the j direction.

    returns:
        (np.ndarray) The shift map with shape (2, scan_i, scan_j).
    """
    shift_map = np.zeros((2, scan_i, scan_j))

    i_params = fitLinearModel(anchor_locations, anchor_shifts[:, 0])
    j_params = fitLinearModel(anchor_locations, anchor_shifts[:, 1])

    # Generate the shift map using the fitted models
    i_grid, j_grid = np.meshgrid(np.arange(scan_i), np.arange(scan_j), indexing='ij')
    locations = np.vstack([i_grid.ravel(), j_grid.ravel()]).T
    shift_map[0] = linearModel(locations.T, *i_params).reshape(scan_i, scan_j)
    shift_map[1] = linearModel(locations.T, *j_params).reshape(scan_i, scan_j)

    return shift_map


def quadraticModel(locations: np.ndarray, a, b, c, d, e, f) -> np.ndarray:
    """
    Quadratic model for fitting the shift map.

    arguments:
        locations: (np.ndarray) The locations in the format of (i, j).
        
        a, b, c, d, e, f: (float) The parameters of the quadratic model.

    returns:
        (np.ndarray) The fitted values.
    """
    i, j = locations
    return a * i**2 + b * j**2 + c * i * j + d * i + e * j + f

def fitQuadraticModel(locations: np.ndarray, shifts: np.ndarray) -> tuple:
    """
    Fit a quadratic model to the given locations and shifts.

    arguments:
        locations: (np.ndarray) The locations in the format of (i, j).
        
        shifts: (np.ndarray) The shifts corresponding to the locations.

    returns:
        tuple: The optimized parameters for the quadratic model.
    """
    popt, _ = curve_fit(quadraticModel, locations.T, shifts)
    return popt


def generateShiftMapWithQuadraticModel(
    anchor_locations: np.ndarray, 
    anchor_shifts: np.ndarray, 
    scan_i: int, 
    scan_j: int,
):
    """
    Generate the shift map using the fitted quadratic models.

    arguments:
        anchor_locations: (np.ndarray) The locations of the anchors.
        
        anchor_shifts: (np.ndarray) The shifts corresponding to the anchor locations.
        
        scan_i: (int) The number of scan positions in the i direction.
        
        scan_j: (int) The number of scan positions in the j direction.

    returns:
        (np.ndarray) The shift map with shape (2, scan_i, scan_j).
    """
    shift_map = np.zeros((2, scan_i, scan_j))

    i_params = fitQuadraticModel(anchor_locations, anchor_shifts[:, 0])
    j_params = fitQuadraticModel(anchor_locations, anchor_shifts[:, 1])

    # Generate the shift map using the fitted models
    i_grid, j_grid = np.meshgrid(np.arange(scan_i), np.arange(scan_j), indexing='ij')
    locations = np.vstack([i_grid.ravel(), j_grid.ravel()]).T
    shift_map[0] = quadraticModel(locations.T, *i_params).reshape(scan_i, scan_j)
    shift_map[1] = quadraticModel(locations.T, *j_params).reshape(scan_i, scan_j)

    return shift_map