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


import sys
import os

ROOTPATH = os.path.split(os.path.dirname(__file__))[0]
if not ROOTPATH in sys.path:
    sys.path.append(ROOTPATH)

import unittest
# from bin.BasicIO import HDF5Handler, IOThreadHandler
from bin.BackEnd import BackEnd
from bin.DataReaderEMPAD import readData, readMetaData
# from bin.Preview import PreviewHandler

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import time

from bin.BlitManager import BlitManager

class TestReadEMPAD(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        print('Test reading data from EMPAD')
        return super().setUpClass()

    def testReadingData(self):
        '''
        测试简单的读取数据的流程。

        初始化类 -> 读取 xml -> 创建 HDF5 文件并初始化 -> 启动 IO -> 
        输出图像 -> 删除 HDF5 文件

        Initialize classes -> read xml -> create HDF5 file and Dataset 
        -> start IO -> show virtual image -> delete HDF5 file
        '''
        # self.handler = HDF5Handler()
        # self.thread_handler = IOThreadHandler(self.handler)
        self.backend = BackEnd()
        self.handler = self.backend.hdf5_handler
        self.thread_handler = self.backend.io_thread_handler

        '''Set Path, Read XML, Create File, Open File, Create Dataset'''
        # self.handler.path = os.path.join(os.getcwd(), 'largeHDF5file.h5')
        self.handler.path = 'D:\\largeHDF5file.h5'
        self.handler.createFile()
        self.handler.openFile()
        test_file_dir = 'F:\\Projects\\20211015_DNA\\06'
        meta = readMetaData(os.path.join(test_file_dir, '06.xml'))
        self.handler.createDataset(
            (meta['scan_i'], meta['scan_j'], meta['dp_i'], meta['dp_j']),
        )
        for item in meta:
            # if not item in self.handler.file['/Dataset'].attrs:
                # self.handler.file['/Dataset'].attrs[item] = meta[item]
            self.handler.setDatasetAttribute(item, meta[item])
        
        '''Read the 4d data'''
        raw_path = os.path.join(
            test_file_dir,
            self.handler.file['/Dataset'].attrs['raw_file_name']
        )
        print('Start Reading')
        self.thread_handler.loadingData('EMPAD', raw_path)

        '''Wait for io'''
        self.thread_handler.reading_thread.join()
        self.thread_handler.loading_thread.join()
        print('Complete Reading')

        '''Plot a virtual image'''
        scan_i, scan_j, dp_i, dp_j = (
            self.handler.file['/Dataset'].attrs['scan_i'],
            self.handler.file['/Dataset'].attrs['scan_j'],
            self.handler.file['/Dataset'].attrs['dp_i'],
            self.handler.file['/Dataset'].attrs['dp_j'],
        )
        mask = np.zeros((dp_i, dp_j))
        for q_ii in range(dp_i):
            for q_jj in range(dp_j):
                q_sq = (q_ii - 64)**2 + (q_jj - 64)**2
                mask[q_ii, q_jj] = (q_sq > 45**2) and (q_sq < 60**2)
        
        haadf = np.zeros((scan_i, scan_j))
        for r_ii in range(scan_i):
            for r_jj in range(scan_j):
                haadf[r_ii, r_jj] = np.sum(
                    self.handler.file['/Dataset'][r_ii, r_jj, :, :] * mask
                )
        
        plt.imshow(haadf)
        plt.show()

        self.thread_handler.loading_thread.join()
        self.thread_handler.previewing_thread.join()

        '''Delete HDF5 File'''
        self.handler.deleteFile()

    def testPreviewingData(self):
        '''
        测试边读取数据边画图的流程

        初始化类 -> 读取 xml -> 创建 HDF5 文件并初始化 -> 启动 IO -> 主线程同时绘图
        -> 删除 HDF5 文件
        '''
        # self.handler = HDF5Handler()
        # self.thread_handler = IOThreadHandler(self.handler)
        # self.preview_handler = PreviewHandler(self.handler)
        self.backend = BackEnd()
        self.handler = self.backend.hdf5_handler
        self.thread_handler = self.backend.io_thread_handler
        self.preview_handler = self.backend.preview_handler

        '''Set Path, Read XML, Create File, Open File, Create Dataset'''
        # self.handler.path = os.path.join(os.getcwd(), 'largeHDF5file.h5')
        self.handler.path = 'D:\\largeHDF5file.h5'
        self.handler.createFile()
        self.handler.openFile()
        test_file_dir = 'F:\\Projects\\20211015_DNA\\06'
        meta = readMetaData(os.path.join(test_file_dir, '06.xml'))
        self.handler.createDataset(
            (meta['scan_i'], meta['scan_j'], meta['dp_i'], meta['dp_j']),
        )
        for item in meta:
            self.handler.setDatasetAttribute(item, meta[item])
        

        '''InitializePreview, Start IO, Update preview,'''
        # self.preview_handler.initializePreview()
        self.preview_handler.setInnerRadius(45)
        self.preview_handler.setOuterRadius(60)
        raw_path = os.path.join(
            test_file_dir,
            self.handler.file['/Dataset'].attrs['raw_file_name']
        )
        print('Start Reading')
        self.thread_handler.loadingData('EMPAD', raw_path)


        '''Drawing'''
        fig, ax = plt.subplots()
        HAADF_image = ax.imshow(self.preview_handler.preview)
        blit_manager = BlitManager(fig.canvas, [HAADF_image])
        plt.show(block = False)
        plt.pause(0.1)
        seconds = 0
        while seconds < 100:
            seconds += 0.1
            plt.pause(0.1)
            HAADF_image.set_data(self.preview_handler.preview)
            M = self.preview_handler.preview_max
            m = self.preview_handler.preview_min
            norm = mpl.colors.Normalize(vmin = m, vmax = M)
            mpl.artist.setp(HAADF_image, norm=norm)
            blit_manager.update()

        self.thread_handler.previewing_thread.join()
        self.thread_handler.reading_thread.join()
        # 必须等待这两个线程结束之后，再开启新的线程 (比如读取另一套数据集)
        HAADF_image.set_data(self.preview_handler.preview)
        blit_manager.update()

        '''Delete HDF5 File'''
        self.handler.deleteFile()
        


if __name__ == '__main__':
    unittest.main(verbosity=2)
