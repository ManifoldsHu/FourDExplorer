# -*- coding: utf-8 -*-

"""
*-------------------------- SplashScreenStart.py -----------------------------*
这是 4D-Explorer 的启动加载页面。

作者：          胡一鸣
创建日期：      2022年6月23日

This is the splash screen showing when the software is started.

author:         Hu Yiming
date:           Jun 23, 2022
*-------------------------- SplashScreenStart.py -----------------------------*
"""

import os 

from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QPixmap 

from Constants import ROOT_PATH

class SplashScreenStart(QSplashScreen):
    """
    程序启动加载页面。

    The screen showing when starting the software.
    """
    def __init__(self):
        super().__init__()
        _image_path = os.path.join(
            ROOT_PATH, 
            'ui', 
            'resources', 
            'images', 
            'start_image_full.png'
        )
        _pic = QPixmap(_image_path)
        _pic.setDevicePixelRatio(3.125) # 800x640
        self.setPixmap(_pic)
        


