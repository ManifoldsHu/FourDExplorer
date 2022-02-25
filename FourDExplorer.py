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
import traceback

from Constants import ROOT_PATH
from bin.app import App 
from bin.Widgets.MainWindow import MainWindow
from bin.Log import LogUtil


        
if __name__ == '__main__':
    if not ROOT_PATH in sys.path:
        sys.path.append(ROOT_PATH)

    app = App(sys.argv)

    ''' Initialize Log'''
    logger = LogUtil(__name__)
    logger.info('4D-Explorer is launched.')
    
    ''' Initialize UI theme'''
    app.theme_handler.initializeTheme()

    try:
        window = MainWindow()
        window.show()
        quit = app.exec()
        if quit == 0:
            logger.info('4D-Explorer exits.')
    except BaseException as e:  # Any exceptions and their tracebacks will be 
                                # recorded in logs.
        exc_type, exc_value, exc_obj = sys.exc_info()
        logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
    finally:
        app._hdf_handler.closeFile()
        sys.exit()