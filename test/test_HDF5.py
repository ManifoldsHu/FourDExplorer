# -*- coding utf-8 -*-

'''
*------------------------------ test_HDF5.py ---------------------------------*
对 HDF5 文件进行读写操作的单元测试。使用 unittest 模块。将用于对 bin.BasicIO 模块内
部的类与函数进行测试。正面测试内容如下：
    - 初始化 HDF5Handler 类
    - 设置指向 HDF5 文件的路径
    - 创建 HDF5 文件
    - 初始化 HDF5 文件
    - 装填四维数据集
    - 装填四维数据集的元数据(扫描 size 以及衍射图样的 size)
    - 显示 HDF5 文件中的所有 Groups 以及 Datasets
    - 删除四维数据集的元数据
    - 删除四维数据集
    - 关闭 HDF5 文件
    - 删除 HDF5 文件

反面测试/异常处理如下：


Unittest towards Input/Output of HDF5 files. This test file corresponds to the 
functions and classes in bin.BasicIO module. The functions being tested include
    - initializing and Instantializing HDF5Handler class,
    - setting the path of the HDF5 file,
    - creating the HDF5 file,
    - initializing the HDF5 file,
    - loading the four-dimensional Dataset,
    - loading the metadata (attributes) of the four-dimensional Dataset,
    - displaying all the groups and datasets in the HDF5 file,
    - deleting one of the attribute of the Dataset,
    - deleting the four-dimensional Dataset,
    - closing HDF5 file,
    - and deleting HDF5 file.
*------------------------------ test_HDF5.py ---------------------------------*
'''
import sys
import os
sys.path.append(os.path.abspath('.'))


import unittest
from bin.BasicIO import HDF5Handler

import numpy as np





class TestHDF5Handler(unittest.TestCase):
    '''
    Test /bin/BasicIO.py
    '''

    @classmethod
    def setUpClass(cls) -> None:
        # cls.handler = HDF5Handler()
        print('Test initializing the HDF5Handler class.')
        return super().setUpClass()
    
    def testOneFullFlow(self):
        '''
        进行正面的测试。
        
        设置路径 -> 创建文件 -> 打开文件 -> 加载数据 -> 删除某项属性
        -> 输出文件结构 -> 删除数据集 -> 关闭文件 -> 删除文件

        The test flow: set path -> create file -> open file -> load data
        -> delete attribute -> display file architecture -> delete dataset
        -> close file -> delete file.
        '''

        self.handler = HDF5Handler()

        '''Set Path'''
        self.handler.path = 'simpleHDF5file.h5'
        print('The path: {0}'.format(self.handler.path))
        
        '''Create HDF5 File'''
        self.handler.createFile()
        self.assertTrue(self.handler.isPathValid())
        print('The created file: {0}'.format(self.handler.path))

        '''Open HDF5 File'''
        self.handler.openFile()
        print('The opened file: {0}'.format(self.handler.file))

        '''Load Dataset'''
        testdata = np.random.random((3,3,2,2))
        self.assertTrue(self.handler.createDataset((3,3,2,2)))
        for ii in range(3):
            for jj in range(3):
                self.handler.writeDataset((ii,jj), testdata[ii,jj,:,:])
        self.assertEqual(self.handler.file['/Dataset'].attrs['scan_i'], 3)
        self.assertEqual(self.handler.file['/Dataset'].attrs['dp_j'], 2)

        '''Delete One Attribute of Dataset'''
        self.handler.deleteDatasetAttribute('dp_i')
        attrlist = []
        for key in self.handler.file['/Dataset'].attrs:
            attrlist.append(key)
        print('Current attrs of Dataset: {0}'.format(attrlist))

        '''Output the File Structure'''
        nodelist = self.handler.traverseAllNodes()
        itemlist = []
        for node in nodelist:
            itemlist.append(node.name)
        print('Current file data structure: {0}'.format(itemlist))

        '''Delete the Dataset'''
        keylist = []
        for key in self.handler.file['/']:
            keylist.append(key)
        print('Before deleting dataset: {0}'.format(keylist))
        self.handler.deleteDataset()
        keylist = []
        for key in self.handler.file['/']:
            keylist.append(key)
        print('After deleting dataset: {0}'.format(keylist))

        '''Close the File'''
        self.assertTrue(self.handler.isFileOpened())
        self.handler.closeFile()
        self.assertFalse(self.handler.isFileOpened())

        '''Delete the File'''
        self.handler.deleteFile()
        self.assertFalse(os.path.isfile(self.handler.path))



if __name__ == '__main__':
    unittest.main(verbosity=2)


    
    
