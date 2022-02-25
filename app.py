# -*- coding: utf-8 -*-

"""
*--------------------------------- app.py -----------------------------------*

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
        ):

     - 根据 PEP-484，应当在定义函数时给出类型提示。如果要使用一个当前模块尚未定义的类
       名，可以使用字符串。比如
       class MyClass(object):
           def __init__(self, parent: 'MyClass') -> None

     - 所有公有函数或方法都应当编写文档字符串 (docstring)。文档字符串以三个双引号起头
       及结尾。

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

     - 循环变量一般使用 ii, jj, kk, ll 等，不使用 i, j, k, l 等 (以与复数区分)。

     - 严禁使用单字母变量，除以下两种情形：
            o 使用 with 语句临时打开文件
              with open(path, 'r') as f:
                  ...
            o 进行临时的异常处理时
              except BaseException as e:

     - 在代码部分中，使用 i, j 表示矩阵的第一、第二指标(行指标、列指标)。但在代码部分
       中与 Matplotlib 交互的部分，且 Matplotlib 中指明了使用 (x,y) 表示坐标的地方，
       与 Matplotlib保持一致。

     - 一般约定对于 4D-STEM 数据集，使用 (scan_i, scan_j, dp_i, dp_j) 表示其尺寸：
            o scan_i 表示扫描 i 方向的像素个数
            o scan_j 表示扫描 j 方向的像素个数
            o dp_i 表示衍射图样 i 方向的像素个数
            o dp_j 表示衍射图样 j 方向的像素个数

     - 在对图像或者四维数据进行循环时，应当在变量名中体现物理意义。例如：
            o 实空间的 i 方向，使用 r_ii 作为循环变量
            o 实空间的 j 方向，使用 r_jj 作为循环变量
            o 倒空间/动量空间/频域的 i 方向，使用 q_ii 或者 k_ii 等作为循环变量
            o 倒空间/动量空间/频域的 j 方向，使用 q_jj 或者 k_ii 等作为循环变量
       因此，一种常见的对 4D-STEM 的数据进行遍历的方式为：
            for r_ii in range(scan_i):
                for r_jj in range(scan_j):
                    for q_ii in range(dp_i):
                        for q_jj in range(dp_j):
                            dataset[r_ii, r_jj, q_ii, q_jj] = ...

     - 在 UI 显示部分(比如控件的标签)中，如果一定要使用 (x, y) 坐标系，则使用 y 
       表示 j ， x 表示 i。因此在这里，(x, y) 坐标系和 (i, j) 坐标系都是右手系。

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

            arguments:
                name1: (type) This is the description of the input parameter
                name2: (type) This is a loooooooonger description of the input
                    parameter.
            
            returns:
                (type) This is the description of the returns. For example:
                    ...(examples)

            raises:
                IOError: This is the description of the error raised by this
                    function.
                
     - 行内注释一般用 # 开头，可任意放置。长度不应当超过80列。

     - 废弃代码应当使用行内注释将其废弃，而不应当直接删除。直到长期不使用、使用Git更
       新版本之后、将要发布时才能删除。

版本管理规范: 
    使用 Git 进行版本管理。master是主分支，仅在发布时使用。进行开发时，一般使用dev分
    支，进行小步迭代。



"""

import sys
import os
from Constants import ROOT_PATH, CONFIG_PATH

from PySide6.QtWidgets import QApplication
from bin.HDFManager import HDFHandler
from bin.Widgets.MainWindow import MainWindow

from bin.Log import LogUtil
import traceback

from bin.UIManager import ThemeHandler

if __name__ == '__main__':
    if not ROOT_PATH in sys.path:
        sys.path.append(ROOT_PATH)

    app = QApplication(sys.argv)

    ''' Initialize Log'''
    logger = LogUtil(__name__)
    logger.info('4D-Explorer is launched.')
    app.logger = logger
    
    ''' Initialize UI theme'''
    theme_handler = ThemeHandler(app)
    theme_handler.initializeTheme()
    app.theme_handler = theme_handler

    ''' Initialize HDF Manager'''
    hdf_handler = HDFHandler()
    app.hdf_handler = hdf_handler

    try:
        window = MainWindow(app)
        window.show()
        quit = app.exec()
        if quit == 0:
            logger.info('System Exit: 4D-Explorer quits.')
    except BaseException as e:
        # Any exceptions and their tracebacks will be recorded in logs.
        exc_type, exc_value, exc_obj = sys.exc_info()
        logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
    finally:
        hdf_handler.closeFile()
        sys.exit()