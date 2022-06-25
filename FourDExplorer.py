# -*- coding: utf-8 -*-

"""
*---------------------------- FourDExplorer.py -------------------------------*

这是4D-Explorer主程序。4D-Explorer是一个用于4D-STEM的可视化四维数据加载、校正、计算
和分析的软件。

作者:           胡一鸣
创建日期:       2021年8月3日

This is 4D-Explorer Main Application. 4D-Explorer is a software to load, calib-
rate, calculate and anaylize 4D-STEM dataset with an easy-to-use graphic user 
interface. 

author:         Hu Yiming
date:           Aug 3, 2021

All rights reserved.

*---------------------------- FourDExplorer.py -------------------------------*
"""

import sys

from Constants import ROOT_PATH
from bin.Widgets.SplashScreenStart import SplashScreenStart

from bin.app import App 

        
if __name__ == '__main__':
    if not ROOT_PATH in sys.path:
        sys.path.append(ROOT_PATH)

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
