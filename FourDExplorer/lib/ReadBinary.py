# -*- coding: utf-8 -*-

"""
*----------------------------- ReadBinary.py ---------------------------------*
提供了读取二进制文件中的图像的一些函数。

作者：          胡一鸣
创建时间：      2022年4月29日

Here provides some functions to read binary raw files.

author:         Hu Yiming
date:           Apr 29, 2022
*----------------------------- ReadBinary.py ---------------------------------*
"""

from PySide6.QtCore import Signal 
import numpy as np
import h5py 

def getDType(
    scalar_type: str, 
    scalar_size: int, 
    little_endian: bool = True,
) -> str:
    """
    This function is used to get a dtype object in numpy, like dtype('<f4').

    arguments:
        scalar_type: (str) Must be one of these: (float, int, uint,)

        scalar_size: (int) How many bytes of one scalar number. Must be one of 
            these: (1, 2, 4, 8)

        little_endian: (bool) Is the byte order of the data little-endian?

    returns:
        (str)
    """
    scltp = {
        'float': 'f',
        'int': 'i',
        'uint': 'u',
        'f': 'f',
        'i': 'i',
        'u': 'u',
    }

    if scalar_type not in scltp:
        raise TypeError('scalar_type must be one of '
            '{0}'.format([key for key in scltp]))
    if little_endian:
        dt = '<' + scltp[scalar_type] + str(scalar_size)
    else:
        dt = '>' + scltp[scalar_type] + str(scalar_size)
    return dt 

def readImageSequenceFromRaw(
    raw_path: str, 
    dataset: h5py.Dataset,
    height: int,                    # number of rows of one image
    width: int,                     # number of columns of one image
    number_of_images: int,          # total number of images
    scalar_type: str = 'float',     # the scalar type
    scalar_size: int = 4,           # how many bytes is in one scalar
    offset_to_first_image: int = 0, # The offset bytes of the first image 
    gap_between_images: int = 0,    # The gap between every two images
    little_endian: bool = True,     # Is data in the file little-endian?
    progress_signal: Signal = None, # The progress signal of the task
):
    if len(dataset.shape) != 3:
        raise IndexError('dataset must be a 3-dimensional matrix')
    if progress_signal is None:
        progress_signal = Signal(int)
    dt = getDType(scalar_type, scalar_size, little_endian)
    with open(raw_path, 'rb') as fid:
        fid.seek(offset_to_first_image)
        for ii in range(number_of_images):
            data = np.nan_to_num(np.fromfile(
                fid,
                dtype = dt,
                count = width * height,
                sep = '',
                offset = bool(ii) * gap_between_images,
            )).reshape((height, width))
            dataset[ii,:,:] = data 
            progress_signal.emit(int((ii+1)/number_of_images*100))


def readFourDSTEMFromRaw(
    raw_path: str, 
    item_path: str,
    dp_i: int,                      # number of rows of one image
    dp_j: int,                      # number of columns of one image
    scan_i: int,                    # number of rows of the image arrays
    scan_j: int,                    # number of columns of image arrays
    scalar_type: str = 'float',     # the scalar type
    scalar_size: int = 4,           # how many bytes is in one scalar
    offset_to_first_image: int = 0, # The offset bytes of the first image 
    gap_between_images: int = 0,    # The gap between every two images
    little_endian: bool = True,     # Is data in the file little-endian?
    is_flipped: bool = False,       # Is chirality of 2D x 2D the same?
    rotate90: int = 0,              # Times every image should be rotated.
    progress_signal: Signal = None, # The progress signal of the task
):
    """
    This function will read data from a binary raw file. The Dataset object
    in the HDF5 file must be a 4-dimensional dataset, of which the first two 
    indices indicate the scanning location of the diffraction pattern.

    This function can also do some processing when loading. For example, it 
    can do transposing and rotate every diffraction patterns. NOTE: The process
    is always first transposing (if is_flipped is True), and then rotate (if 
    rot90 does not equal to 0).

    arguments:
        raw_path: (str) The absolute path of the raw file.

        item_path: (str) The dataset to be written. (The original data
            will be covered)

        dp_i: (int) number of rows of one image (height).

        dp_j: (int) number of columns of one image (width).

        scan_i: (int) number of rows of the scanning arrays of 4D-STEM.

        scan_j: (int) number of columns of the scanning arrays of 4D-STEM.

        scalar_type: (str) must be one of these: (float,int,uint,)

        scalar_size: (int) how many bytes of one scalar number. Must be one of 
            these: (1, 2, 4,)
            
        offset_to_first_image: (int) The offset bytes before the first image

        gap_between_images: (int) The offset bytes between two images.

        little_endian: (bool) default to be True. If false, will read with
            big_endian.

        rot90: (int) How many times should the data be rotated 90 counter-
            clockwise. Default is 0. In some cases, the coordinate of the 
            source data is xy, but in 4D-Explorer we use ij, so we must rotate 
            90° when loading the 4D-STEM dataset.
    """
    global qApp 
    hdf_handler = qApp.hdf_handler
    dataset = hdf_handler.file[item_path]

    if len(dataset.shape) != 4:
        raise IndexError('dataset must be a 4-dimensional matrix')

    dt = getDType(scalar_type, scalar_size, little_endian)
    if progress_signal is None:
        progress_signal = Signal(int)

    with open(raw_path, 'rb') as fid:
        fid.seek(offset_to_first_image)
        for ii in range(scan_i):
            for jj in range(scan_j):
                data = np.nan_to_num(np.fromfile(
                    fid,
                    dtype = dt,
                    count = dp_i * dp_j,
                    sep = '',
                    offset = bool(ii + jj) * gap_between_images,
                )).reshape((dp_i, dp_j))
                if is_flipped:
                    dataset[ii, jj, :, :] = np.rot90(data.T, rotate90)
                else:
                    dataset[ii, jj, :, :] = np.rot90(data, rotate90)
                    
            progress_signal.emit(int((ii+1)/scan_i*100))
    
    # print('is_flipped: ', is_flipped)

