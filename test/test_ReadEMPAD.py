# -*- coding: utf-8 -*-

'''
*---------------------------- test_ReadEMPAD.py ------------------------------*
读取 EMPAD 生成的 4D-STEM 的数据与元数据。使用 unittest 模块。将用于对 bin.BasicIO
以及 bin.DataReaderEMPAD 内部的类与函数进行联合测试。正面测试内容如下：

1. 简单用法。传入 .xml 文件的路径开始，测试读取、写入数据的流程：
    - 初始化 HDF5Handler 类
    - 初始化 IOThreadHandler 类
    - 读取 .xml 文件，得到 meta
    - 根据 meta 创建 HDF5 文件并初始化
    - 装填四维数据集的元数据
    - 利用 IOThreadHandler 类初始化并启动 IO 线程
    - 完成 IO
    - 检验图像是否成功加载
    - 删除临时文件，结束

2. 简单用法。传入 .xml 文件的路径开始，测试读取、写入、实时更新数据的流程：
    - 初始化 HDFHandler 类
    - 初始化 IOThreadHandler 类
    - 读取 .xml 文件，得到 meta
    - 根据 meta 创建 HDF5 文件并初始化 
    - 装填四维数据集的元数据
    - 利用 IOThreadHandler 类初始化并启动 IO 线程
    - 进行 IO ，在主线程中读取 Dataset 并进行实时绘图
    - 完成 IO，删除临时文件，结束
*---------------------------- test_ReadEMPAD.py ------------------------------*
'''