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
from bin.app import App 
from bin.Widgets.MainWindow import MainWindow
# from bin.Log import LogUtil


        
if __name__ == '__main__':
    if not ROOT_PATH in sys.path:
        sys.path.append(ROOT_PATH)

    app = App(sys.argv)

    ''' Initialize Log'''
    logger = app.logger
    
    ''' Initialize Clean-up code'''
    app.aboutToQuit.connect(app.hdf_handler.closeFile())
    app.aboutToQuit.connect(app.task_manager.shutDown())
    app.aboutToQuit.connect(lambda: logger.info('4D-Explorer exits'))

    ''' Initialize UI theme'''
    app.theme_handler.initializeTheme()


    window = MainWindow()
    window.show()
    logger.info('4D-Explorer is launched.')
    quit = app.exec()
    sys.exit(quit)
