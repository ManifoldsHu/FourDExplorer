# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
from bin.MainWindow import MainWindow

import sys
import os
from bin.Log import LogUtil
import traceback
# import logging
# import time

'''
*--------------------------------- app.py -----------------------------------*

这是4dExplorer主程序。4dExplorer是一个用于4D-STEM的可视化四维数据加载、校正、计算、
分析的软件。

This is 4dExplorer Main Application. 4dExplorer is a software that can be used 
to load, calibrate, calculate and anaylize 4D-STEM dataset with an easy-to-use 
graphic user interface. 

作者:           胡一鸣
创建日期:       2021年8月3日

author:         Hu Yiming
date:           Aug 3, 2021

All rights reserved.

*--------------------------------- app.py -----------------------------------*

开发规范:
    开发要尽可能遵循模块化、前后端分离、高内聚低耦合的原则。
     - 所有源代码都应当以UTF-8编码，每个文件都应当以
       # -*- coding: utf-8 -*-
       的形式开头，以表明该文件是使用UTF-8编码的。

     - 当函数的参数过多时，应当换行，且每一个参数占用一行，如:
        def example(
            argument1,
            argument2,
            optional_argument3 = optional_argument3,
        )

     - 当

命名规范: 
     - 文件夹名: 全部小写。

     - 模块(文件名): 大驼峰。

     - 类名: 大驼峰。应当以其类型简称作为第一个单词，从大到小逐级命名。比如:
            o WidgetPatchCircle         Widget表明这是UI控件，Patch表明这是控制图
                                        形的，Circle表明这是圆形
            o BlitManager               表明这是用于帮助管理位图传送的类

     - 函数、方法名: 一般使用小驼峰。私有函数应当以下划线'_'开头。比如: 
            o setRadius                 设置半径的函数
            o _updatePatch              私有方法，更新图形

     - 变量名: 一般使用全部小写加下划线。私有属性应当以下划线'_'开头。

     - 循环变量一般使用ii, jj, kk, ll等，不使用i, j, k, l等。

     - 严禁使用单字母变量。

     - 在代码部分中，使用i,j表示矩阵的第一、第二指标(行指标、列指标)。但在代码部分中与
       Matplotlib交互的部分，且Matplotlib中指明了使用 (x,y) 表示坐标的地方，与Matp-
       lotlib保持一致。

     - 在UI显示部分(比如控件的标签)中，则使用 y 表示 j ， x 表示 i 。 

     - 常见第三方库使用如下约定: 
             o import numpy as np
             o import matplotlib as mpl

注释规范:
    良好的代码注释是软件开发的关键所在。在每一个模块、每一个类、每一个方法下面都应当按照
    如下规范编写注释。注释中每行的列数不应超过80列。
     - 模块(文件)的注释应当给出模块的用途、作者、创建日期。例如: 
            *-------------- filename -----------------*
            这是该模块的描述。

            作者：          名字
            创建时间：      2021年8月3日 

            This is the description of this module.

            author:         Name
            date:           Aug 3, 2021
            *-------------- filename -----------------*

     - 函数的注释应当给出函数的描述、输入参数及输出参数。例如: 
            这是该函数或方法的描述
            This is the description of this function/method

            arguments       type        description     #输入参数
            ----------------------------------------------------------------
            name1           type        This is the description of the input 
                                        parameter

            name2           type        This is the description of the input 
                                        parameter
            ----------------------------------------------------------------

            returns         type        description     #返回值
            -----------------------------------------------------------------
            name1           type        This is the description of the return 
                                        value

            name2           type        This is the description of the return 
                                        value
            -----------------------------------------------------------------
     - 行内注释一般用 # 开头，可任意放置。长度不应当超过80列。

     - 废弃代码应当使用行内注释将其废弃，而不应当直接删除。直到长期不使用、使用Git更
       新版本之后、将要发布时才能删除。

版本管理规范: 
    使用 Git 进行版本管理。master是主分支，仅在发布时使用。进行开发时，一般使用dev分
    支，进行小步迭代。



'''

global SOFTWAREPATH
SOFTWAREPATH = os.path.abspath('.')

app = QApplication(sys.argv)
logger = LogUtil(__name__)
logger.info('4dExplorer is launched.')
try:
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
except SystemExit as e: 
    logger.info('System Exit: 4dExplorer is closed')
    sys.exit()
except BaseException as e:
    exc_type, exc_value, exc_obj = sys.exc_info()
    logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
    sys.exit()