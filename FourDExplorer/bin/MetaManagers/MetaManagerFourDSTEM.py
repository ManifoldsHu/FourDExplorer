# -*- coding: utf-8 -*- 

"""
*-------------------------- MetaManagerFourDSTEM.py --------------------------*
管理 .4dstem 数据集的元数据。

注意，只有那些基本的量会被存储，而其他参数将被实时计算。例如，加速电压会被存储，而波长
会则由加速电压导出，从而被实时计算。

元数据会以树状的形式进行存储，其树枝节点用大驼峰的形式命名，而叶子节点则用下划线命名法。
当然，在程序中我们不会使用这个特性来决定一个节点是否为叶子节点。

在实际的操作中，我们期望为每项元数据都提供单独的修改界面，从而规范输入。这需要大量的工
作。

作者：          胡一鸣
创建时间：      2023年10月31日

Manages metadata for .4dstem datasets.

Note that only fundamental quantities are stored, whereas other parameters are
calculated in real-time. For example, the acceleration voltage is stored, while
the wavelength is derived from it and thus calculated on-the-fly.

Metadata is stored in a tree-like structure, with branch nodes named using Pa-
scalCase, and leaf nodes using snake_case. Of course, in the program, we will
not use this feature to determine whether a node is a leaf node or not.

In practical operations, we aim to provide individual modification interface 
for each piece of metadata, thereby standardizing input. This requires extens-
ive work.

author:         Hu Yiming
date:           Oct 31, 2023
*-------------------------- MetaManagerFourDSTEM.py --------------------------*
"""

from logging import Logger 
from typing import Type 

from PySide6.QtCore import QObject

from Constants import HDFType 
from bin.HDFManager import HDFHandler 
from bin.MetaManagers.MetadataFields import FloatField, IntField, StringField
from bin.MetaManagers.UnitManager import UnitManager

class MetaManagerFourDSTEM(QObject):
    """
    管理 .4dstem 数据集元数据的封装类。

    The class that manages metadata of .4dstem datasets.
    """


    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        # 需要在这里将所有涉及到的 attribute 进行初始化。例如，
        self._initializeMetadata()
        self._meta = {}
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler
    
    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger
    
    def _initializeMetadata(self):
        """
        Initialize all of the metadata. All values will be set to None.
        """
        pass