# -*- coding: utf-8 -*-

"""
*----------------------------- transcolor.py ---------------------------------*
这个脚本可生成用于夜间模式的图标。

其只能转换 png 格式的 RGBA 图片，并且要求这些图片中除了画线部分，其他位置均为透明，
也就是 A = 0。对于划线部分，也要求其为单色。

转换后所得的图片将保留透明度分布，而会将所有不透明的地方都涂成白色。

作者:           胡一鸣
创建日期:       2022年6月10日

This script can be used to produce icons for dark-theme.

The icons are RGBA-png images, so we choose those points whose alpha is non-
zero, and set their color to be white. Then the icons can be used in the dark 
themes.

This script can only used to transform png RGBA images.

author:         Hu Yiming
date:           Jun 10, 2022
*----------------------------- transcolor.py ---------------------------------*
"""

import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def convertColor(image_rgba: np.ndarray) -> np.ndarray:
    """
    This function will convert icons to dark-mode.

    The icons are RGBA-png images, so we choose those points whose alpha is 
    non-zero, and set their color to be white. Then, those icons can be used 
    in the dark themes.

    arguments:
        (np.ndarray) must be 2D image with 4 channels (RGBA).
    
    returns:
        (np.ndarray)
    """
    image_rgba[image_rgba[:,:,3] > 1e-6] = 1
    return image_rgba

def imageProvider(dir_path: str):
    """
    This generator will produce valid image names and their matrices.

    arguments:
        dir_path: (str) the path of directory where images locate.
    """
    for name in os.listdir(dir_path):
        path = os.path.join(dir_path, name)
        if os.path.isfile(path):
            if os.path.splitext(path)[1] == '.png':
                yield name, plt.imread(path)

if __name__ == '__main__':
    dir_path = './ui/resources/icons/'
    for name, image in imageProvider(dir_path):
        print(name)
        image_light = convertColor(image)
        name_light = os.path.splitext(name)[0] + '_light.png'
        path_light = os.path.join(dir_path, name_light)
        plt.imsave(path_light, image_light)

