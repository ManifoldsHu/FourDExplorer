# -*- coding: utf-8 -*-

"""
*---------------------------- FourDExplorer.py -------------------------------*

这是4D-Explorer主程序。4D-Explorer是一个用于四维扫描透射电子显微术 (4D-STEM) 的可视
化四维数据加载、校正、计算和分析的软件。

4D-STEM 是一种新颖的技术。它通常使用会聚电子束在样品上进行扫描，并使用电子相机记录下每
个扫描位置所对应的电子束衍射成像。因此，4D-STEM 数据集在计算机中通常表现为四维数组，其
中前两个指标对应于扫描坐标，而后两个指标则对应于每个衍射图像。

作者:           胡一鸣
创建日期:       2021年8月3日

This is 4D-Explorer Main Application. 4D-Explorer is a software to load, 
calibrate, calculate and anaylize Four-dimensional scanning transmission electron 
microscopy (4D-STEM) dataset with an easy-to-use graphic user interface. 

4D-STEM is a novel technique. It typically uses a convergent electron beam to scan 
the sample and records the electron beam diffraction imaging corresponding to each 
scan position using an electron camera. Therefore, the 4D-STEM dataset is usually 
represented as a four-dimensional array in the computer, where the first two 
indices correspond to the scan coordinates, and the latter two indices correspond 
to each diffraction image.


author:         Hu Yiming
date:           Aug 3, 2021

All rights reserved.

*---------------------------- FourDExplorer.py -------------------------------*
"""

import sys
import os 
ROOT_PATH = os.path.dirname(__file__)
if not ROOT_PATH in sys.path:
    sys.path.append(ROOT_PATH)

import matplotlib.style as mplstyle
mplstyle.use('fast')

from bin.Widgets.SplashScreenStart import SplashScreenStart

from bin.app import App 

def run():


    ''' start app '''
    app = App(sys.argv)

    ''' start loading screen '''
    loading_screen = SplashScreenStart()
    loading_screen.show()
    app.processEvents()

    ''' start backend managers '''
    app.startBackEnds()
    logger = app.logger
    app.theme_handler.initTheme() 

    ''' start main window '''
    from bin.Widgets.MainWindow import MainWindow
    main_window = MainWindow()
    app.main_window = main_window
    main_window.show()
    loading_screen.finish(main_window)
    
    quit = app.exec()
    logger.info('4D-Explorer exits.')
    sys.exit(quit)


if __name__ == '__main__':
    run()

