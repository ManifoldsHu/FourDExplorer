# -*- coding utf-8 -*-

'''
*------------------------------- HDFManager.py -------------------------------*
对 HDF5 文件进行读取与写入的操作。

4dExplorer 软件默认使用 HDF5 进行四维数据及其元数据的管理。对于其他格式的文件，例如由
EMPAD 所产生的数据，4dExplorer 将其转换为hdf5进行管理并生成临时文件，用户可自行决定是
否要保存该临时文件为 HDF5 数据集。出于对内存空间资源节约的考虑，所有有关四维数据的计算
都是基于硬盘 IO 的，而在代码层面上不会将数据一次性全部读入内存中(尽管操作系统会尝试这样
做，但即使是内存空间不足，也无需担心会对性能造成影响。)

这样，对于由仪器采集而来的数据，使用 4dExplorer 软件进行数据读取的步骤就是：
    - 在某个文件夹内创建临时 HDF5 数据文件，该文件的主要部分是原四维数据的副本；
    - 根据 HDF5 的特性进行内存映射；
    - 校正与分析，结果都将存储于 HDF5 文件中；
    - 输出分析结果；
    - 保存或删除 HDF5 文件。

在这样的工作流程中，将四维数据复制一份的时间代价较大。为节约后续分析的时间，可以保存 HDF5 
文件，后续重新打开该数据集时可直接建立内存映射，省下加载四维数据的时间开销。在后续打开时，
就将直接调用 HDFManager.py 中的代码。


作者：          胡一鸣
创建时间：      2021年8月21日

Basic IO operation of HDF5 files.

By default, the 4dExplorer software uses HDF5 to manage 4d data and metadata. 
For other files, such as the data generated by EMPAD, 4dExplorer converts them 
to HDF5 for management and generates temporary files. Users can decide whether 
to save the temporary files as HDF5 data sets or not. In order to save memory 
resources, all computation of the four-dimensional data is based on disk IO, a-
nd the data is not read into memory all at once at the code level (although the 
operating system will try to do this, there is no need to worry about the perf-
ormance impact of running out of memory).

In this way, for the data collected by the specific instrument, the steps of u-
sing 4dExplorer software to read the data are as follows:
    - Create a temporary HDF5 data file in some folder, the main part of which 
    is a copy of the original 4-dimensional data;
    - Memory mapping based on HDF5 features;
    - Calibration and analysis, the results will be stored in the HDF5 file;
    - Output the analysis result;
    - save or delete the HDF5 file.

In such a workflow, the time cost of making a copy of the four-dimensional data 
is large. In order to save the time of subsequent analysis, the HDF5 file can 
be saved, and the memory mapping can be directly established when the data set 
is reopened, saving the time cost of loading the four-dimensional data. On sub-
sequent opens, the code in HDFManager.py is called directly.

author:             Hu Yiming
date:               Aug 21, 2021

All rights reserved.

*------------------------------- HDFManager.py -------------------------------*
'''


from multiprocessing import parent_process
import os
from datetime import datetime
import re
import threading
import queue
import time
import traceback
from collections.abc import Mapping
from typing import Iterator

import h5py
import numpy as np

from PySide6.QtWidgets import QApplication 

from bin.Log import LogUtil
from Constants import APP_VERSION


# from bin import DataReaderEMPAD
# from bin.BackEnd import BackEnd
# from bin.Preview import PreviewHandler

logger = LogUtil(__name__)
reValidHDFName = re.compile(
    r'^[0-9a-zA-Z\_\-\.][0-9a-zA-Z\_\-\.\s]*$'
)   # A valid hdf_name must be able to match this regular expression.

class HDFHandler(object):
    """
    使用 HDF5 文件处理的封装类。其应当包含以下方法：

        - 设置指向的 h5 文件的路径
        - 创建 h5 文件并初始化
        - 读取 h5 文件，对不合规的文件进行初始化
        - 删除 h5 文件            # 安全性问题？

        - 生成 HDFTree，用于对 HDF5 文件内部的路径进行管理
        - 根据 HDFTree 生成用于 Qt 的 Model。
        - 根据 hdf_path 取到对应的 HDFTree 中的 HDFTreeNode
        - 根据 hdf_path 取到对应的 HDFTree 中的 HDFTreeNode 在同级 Node 中的序号
        - 根据 hdf_path 增加 Group，同时修改对应的 HDFTree
        - 根据 hdf_path 增加 Data，同时修改对应的 HDFTree
        - 根据 hdf_path 删除 Group 或 Data，同时修改对应的 HDFTree
        - 根据 hdf_path 移动 Group 或 Data，同时修改对应的 HDFTree
        - 根据 hdf_path 重命名 Group 或 Data，同时修改对应的 HDFTree
        - (不提供复制的功能，原因是这很耗时，应当作为一个任务提交给 TaskManager)


    注意，这个类使用单例模式，如果已经有一个这个类的实例，那么再次创建该类的实例的时
    候就直接返回已有的那个实例。

    初始化完成的h5文件应当有如下结构：
        /Dataset                            四维数据集。

        /Calibration                        作为 Group ，其 Attribution 内有各种
                                            校正操作类。

        /Reconstruction                     作为Group，储存每一次的计算结果。

        /Reconstruction/1_iCoM/Matrix       某一次重构的计算结果，作为二维矩阵。其
                                            Attribute 包含了数据类型、计算类型、计
                                            算参数、计算时所使用的 Calibration 配
                                            置。“1_iCoM” 指的是计算任务名字，其为 
                                            “数字-算法” 的结构。

        /Reconstruction/1_iCoM/1_imshow     作为 Group，其 Attribution 保存的是封
                                            装的画图类，储存了对这次重构得到的结果
                                            进行画图所使用的参数。

        /tmp                                临时数据，用来保存当 Calibration 不变
                                            时，上一次计算得到的 CoM 矢量，及其他未
                                            来可能出现的中间结果。关闭时应当删除该 
                                            Group 下所有数据。

          
    This is the encapsulated classes that use HDF5 file processing. It should 
    contain the following methods:    
        - set the path of the h5 file,
        - create the h5 file and initialize,
        - read the h5 file, and initialize those invalid files,
        - delete the h5 file (will be used to delete temp files),

        - create HDFTree, in order to manage the hdf path,
        - according to the HDFTree, create model for Qt (Model-View structure),
        - according to the hdf_path, get Node in the HDFTree,
        - according to the hdf_path, get row of the node in the HDFTree,
        - according to the hdf_path, create group and fix HDFTree,
        - according to the hdf_path, create data and fix HDFTree,
        - according to the hdf_path, remove items and fix HDFTree,
        - according to the hdf_path, move items and fix HDFTree,
        - according to the hdf_path, rename items and fix HDFTree,
        - (there is no copy api, because it is time-consumed and should be a t-
        ask to be submitted to the TaskManager)
    

        

    NOTE: there is only SINGLE instance (Singleton). If there has been one ins-
    tance of this class, the existing instance will be returned.

    An initialized h5 file should have the following structure:

    /Dataset                                Four-dimensional data set.

    /Calibration                            As a group, there are various cali-
                                            bration classes inside its attribu-
                                            tion.

    /Reconstruction                         As a group, each calculation are s-
                                            aved here.

    /Reconstruction/1_iCoM/Matrix           The result of a reconstruction, as 
                                            a two-dimensional matrix. Attribute 
                                            contains the data type, calculation 
                                            type, calculation parameters, and 
                                            the Calibration configuration used 
                                            in the calculation.  "1_iCoM" is t-
                                            he name of the calculation task, w-
                                            hich is a "number-algorithm" struc-
                                            ture.  

    /Reconstruction/1_iCoM/1_imshow         As a Group, its attribution preser-
                                            ves the encapsulated drawing class 
                                            that stores the parameters to use 
                                            to draw the results of the matrix. 

    /tmp                                    Temporary group, used to store the 
                                            CoM vector from the last calculati-
                                            on when the Calibration is unchang-
                                            ed, as well as other intermediate 
                                            results that may occur in the futu-
                                            re. When closing, all data in this 
                                            Group should be deleted.



    Attributes:
        file_path: (str) the HDF5 file path.
        file: (h5py.File) the OPENED HDF5 file, or NoneType.
    """

    _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls, app: QApplication):
        """There is only one instance allowed to exist. 
        
        (This is a singleton class)

        arguments:
            app: (QApplication) the main QApplication.
        """
        with cls._instance_lock:
            if cls._instance is None:
                cls._instance = object.__new__(cls)
                cls._instance.__init__(app)
            return cls._instance

    def __init__(self, app: QApplication):
        """
        arguments:
            app: (QApplication)
        """
        self._app = app 
        self._file = None
        self._file_path = ''
        self._lock = threading.Lock()
        self._root_node = HDFGroupNode()

    @property
    def file_path(self):
        """
        Get the current h5 file path.

        returns:
            (str) the current h5 file path. If there is no file opened,
                returns ''.
        """
        return self._file_path

    @file_path.setter
    def file_path(self, value: str):
        """
        Set the h5 file path. Will close the current file.

        arguments:
            value: (str) the absolute path of the new h5 file.

        """
        if not isinstance(value, str):
            raise TypeError('Expected a string.')
        if value != self.file_path and self.isFileOpened():
            self.file.close()

        self._file_path = value


    def isFilePathValid(self) -> bool:
        """
        Return whether the file is a valid h5 file.

        returns:
            (bool)
        """
        try:
            with h5py.File(self.file_path, mode = 'r') as file:
                is_valid = isinstance(file, h5py.File)
            return is_valid
        except OSError as e:
            logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
            return False
          
     
    @property
    def file(self) -> h5py.File:
        """
        Returns opened file. if the file is not opened, returns NoneType.

        Returns:
            (h5py.File)
        """
        if self.isFileOpened():
            return self._file
        else:
            return None

    @file.setter
    def file(self, h5_file: h5py.File):
        """
        Set the h5 file.

        arguments:
            h5_file: (h5py.File) Must be h5py.File or NoneType.
        """
        if h5_file == None or isinstance(h5_file, h5py.File):
            self._file = h5_file
        else:
            raise TypeError('file must be a h5py.File or None.')
               

    def createFile(self) -> bool:
        """
        Create a new standard h5 file according to the file_path attribute.
        
        Fail if there exists.

        returns:
            (bool) whether the file is created.
        """
        try:
            with h5py.File(self.file_path, mode = 'w-') as file: # create, 
                                                            # fail if exists
                self._initializeFile(file)
        except OSError as e:
            logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
            return False
        return True


    def _initializeFile(self, file: h5py.File):
        """
        Initialize a h5 file. Some groups and attributes will be added.

        arguments:
            file: (h5py.File) the file object being initialized.
        """
                    
        if 'Reconstruction' not in file:
            file.create_group('Reconstruction')
        if 'Calibration' not in file:
            file.create_group('Calibration')
        if 'tmp' not in file:
            file.create_group('tmp')

        root = file['/']
        root.attrs['4D-Explorer'] = True
        root.attrs['FileCreateTime'] = '{0}'.format(datetime.now)
        root.attrs['Version'] = str(APP_VERSION)
          
     
    def openFile(self):
        """
        Open a h5 file. 
        
        Fail if there is no file corresponding to the file_path attribute. 
        The file must be opened before it is handled by HDFManager modules.

        Returns:
            (h5py.File) the opened file.
        """
        try:
            if not self.isFileOpened():
                # Read/write, file must exist
                self.file = h5py.File(self.file_path, mode='r+')  
        except OSError as e:
            logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
            return None
        return self.file


    def closeFile(self):
        """
        Close the h5 file. 
        
        The file must be closed before:
            - the file_path is changed
            - the file is deleted
            - the application is exit
        """
        if self.isFileOpened():
            self.file.close()
        self.file = None
          

    def isFileOpened(self) -> bool:
        """
        Returns whether the hdf5 file is opened.

        returns:
            (bool) 
        """
        if self.file is None:
            return False
        if self.file.id: 
            # It seems in h5py they use this to estimate if the file is closed.   
            return True
        else:
            return False


    def deleteFile(self) -> bool:
        """
        Delete the h5 file. Fail if there is no file.

        returns:
            (bool)
        """
        if self.isFileOpened():
            self.file.close()
        if self.isFilePathValid():
            try:
                os.remove(self.file_path)
                return True
            except OSError as e:
                logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
                return False


    def createModel(self):
        """
        Create a FileStructureModel for 
        """
        pass

    @property
    def root_node(self) -> 'HDFGroupNode':
        return self._root_node

    def buildHDFTree(self):
        """
        Build an HDFTree according to the current HDF5 file.

        Will add child nodes recursively for the root_node and its childs.
        """
        if not self.file:
            raise OSError('Must open a file before build HDFTree.')
        
        def _addChildDeepFirst(parent: 'HDFGroupNode'):
            if isinstance(parent, HDFGroupNode):
                for key in self.file[parent.path]:
                    if isinstance(self.file[parent.path][key], h5py.Group):
                        parent.addChild(HDFGroupNode(key, parent))
                    elif isinstance(self.file[parent.path][key], h5py.Dataset):
                        parent.addChild(HDFDataNode(key, parent))

        _addChildDeepFirst(self.root_node)

    def getNode(self, hdf_path: str) -> 'HDFTreeNode':
        """
        Get Node with the absolute path of the HDF5 items.

        The path must start with '/', and end with the items' name.

        arguments:
            hdf_path: (str) absolute path of the HDF5 items.

        returns:
            (HDFTreeNode) 
        """
        if not isinstance(hdf_path, str):
            raise TypeError(('hdf_path must be str, not '
                '{0}'.format(type(hdf_path).__name__)))
        elif hdf_path == '':
            raise KeyError('hdf_path can not be null string')
        elif hdf_path[0] != '/':
            raise KeyError('hdf_path must start with slash /')
        elif len(hdf_path) > 1 and hdf_path[-1] == '/':
            raise KeyError('hdf_path cannot end with slash /')
        elif hdf_path == '/':
            return self.root_node
        else:
            keys_array = hdf_path.split('/')[1:]
            node = self.root_node
            for key in keys_array:
                if key in node:
                    node = node[key]
                else:
                    raise KeyError(('There is no key '
                        '{0} in {1}'.format(key, node.name)))

    def getRank(self, hdf_path: str = '') -> int:
        """
        Get the rank of the node among its mates.

        In the hash table, the rank is not fixed. Here we will get the rank by 
        the keysview of the dict. It is usually used to show items in a table.

        arguments:
            hdf_path: (str) absolute path of the HDF5 items

        returns:
            (int) rank of the node among its mates.
        """
        if hdf_path == '/':
            return 0
        else:
            this = self.getNode(hdf_path)
            key = hdf_path.split('/').pop()
            rank = list(this.parent.keys()).index(key)
            return rank

    def addNewGroup(self, parent_path: str, name: str):
        """
        Add a group in the parent_path.

        Will add a group in the HDF5 file and add a HDFGroupNode in HDFTree.

        arguments:
            parent_path: (str) absolute path of the HDF5 group.

            name: (str) name of the new group
        """
        if not isinstance(parent_path, str):
            raise TypeError(('parent_path must be str, not '
                '{0}'.format(type(parent_path).__name__)))
        elif not isinstance(name, str):
            raise TypeError(('name must be str, not '
                '{0}'.format(type(name).__name__)))
        parent_node = self.getNode(parent_path)
        if name in parent_node:
            raise ValueError(('name {0} exists in {1}\n'
                'path: {2}'.format(name, parent_node.name, parent_path)))
        self.file[parent_path].create_group(name)
        parent_node.addChild(HDFGroupNode(name))

    def addNewData(self, 
        parent_path: str, 
        name: str, 
        shape: tuple, 
        dtype: str = 'float32',
        compression: str = 'gzip',):
        """
        Create a dataset in the parent_path.

        Will add a dataset in the HDF5 file and add a HDFDataNode in HDFTree.

        arguments:
            parent_path: (str) absolute path of the HDF5 group

            name: (str) name of the new dataset
        """
        if not isinstance(parent_path, str):
            raise TypeError(('parent_path must be str, not '
                '{0}'.format(type(parent_path).__name__)))
        elif not isinstance(name, str):
            raise TypeError(('name must be str, not '
                '{0}'.format(type(name).__name__)))
        parent_node = self.getNode(parent_path)
        if name in parent_node:
            raise ValueError(('name {0} exists in {1}\n'
                'path: {2}'.format(name, parent_node.name, parent_path)))
        self.file[parent_path].create_dataset(
            name, 
            shape = shape, 
            dtype = dtype, 
            compression = compression)
        parent_node.addChild(HDFDataNode(name, parent_node))

    def deleteItem(self, hdf_path: str):
        """
        Delete the item with the hdf_path.

        Will delete the item in the practical HDF5 file, and delete the node in 
        HDFTree. If the item is a group, and there are subitems in the item, 
        all of the subitems will be removed recursively.

        arguments:
            hdf_path: (str) absolute path of hdf5 item.
        """
        pass

    def moveItem(self, item_path: str, dest_path: str):
        pass

    def renameItem(self, hdf_path: str, new_name: str):
        pass

class HDFTreeNode(Mapping):
    """
    HDFTree 路径树的节点。
    
    这是一个基类，要实例化的话，请使用 HDFGroupNode 和 HDFDataNode 这些子类。

    根节点的名字强制为空字符串 ''。除此之外，其他节点的命名规则是：
        - 不能为空字符串
        - 只能包含数字、英文字母、下划线 '_'、短横杠 '-'、点号 '.' 以及空格
        - 不能以空格开头。


    The Node of HDFTree. 
    
    It is not recommended to instantiate HDFTreeNode, but to instantiate its 
    subclass like HDFGroupNode and HDFDataNode. 
    
    
    The name of the root node is forced to be null str '', while other nodes h-
    ave their own names. Except the root node, others' name follow these rules:
        - cannot be a null string
        - can only include numbers, English characters, underline '_', dashline
        '-', dot '.', and space ' '
        - cannot start with space ' '.
    

    attributes:
        name: (str) The name of the node. if the name is null string (''), it 
            is the root node of the HDFTree.

        parent: (HDFTreeNode) The parent node of this node.

        path: (str) The hdf_path of this node. like '/foo/abc' 
    """

    def __init__(self, name: str, parent: 'HDFTreeNode'):
        """
        arguments:
            name: (str) only root's name can and must be null string ''. Usual-
                ly, to instantiate a root node, use HDFGroupNode rather than 
                HDFTreeNode. 

            parent: (HDFTreeNode or NoneType)
        """
        self.name = name
        self.parent = parent

    def __str__(self) -> str:
        return '<HDFTreeNode> name: {0}'.format(self.name)

    def __repr__(self) -> str:
        return self.__str__()

    @property 
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        """
        Give a new name to this node. The name here must be a string that:
            - can only include numbers, characters, underline '_', dash '-', 
                dot '.' and space ' '.
            - cannot start as space ' '.
        Otherwise a ValueError is raised.

        arguments:
            new_name: (str) give a new name to this node. User must change the
                practical item's name in the HDF file at the same time. Otherw-
                ise, after a flush the name change will be lost.
        """
        if new_name == '':
            self._name = ''
        else:
            # valid_name_pattern = r'^[0-9a-zA-Z\_\-\.][0-9a-zA-Z\_\-\.\s]*$'
            if not isinstance(new_name, str):
                raise TypeError(('new_name must be a str, not '
                    '{0}'.format(type(new_name))))
            elif not reValidHDFName.match(new_name):
                raise ValueError('Invalid name: {0}'.format(new_name))
            else:
                self._name = new_name
                
    
    @property 
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent: 'HDFGroupNode'):
        """
        Set the parent node of this node.

        arguments:
            parent: (HDFTreeNode) either also an HDFTreeNode or NoneType. In 
            most cases, if the parent is None, the node's name should be '', 
            which indicates that this is a root node.
        """
        if parent is None:
            self._parent = None
        elif not isinstance(parent, HDFGroupNode):
            raise TypeError(('parent must be HDFTreeNode or NoneType,'
                ' not {0}'.format(type(parent))))
        else:
            self._parent = parent

    @property 
    def path(self) -> str:
        """
        Indicates the full hdf_path of this node inside the file. Like:
        '/', (root)
        '/foo/abc' (maybe a group or a data)

        returns:
            (str) the full hdf_path of this node.
        """
        if self._getPathInTree() == '':
            return '/'
        else:
            return self._getPathInTree()

    def _getPathInTree(self) -> str:
        if self.parent == None:
            return ''
        else:
            return self.parent._getPathInTree() + '/' + self.name

    
class HDFGroupNode(HDFTreeNode):
    """
    用来表示 Group 的节点。

    可以为其添加、删除子节点。为了支持类似于 Mapping 风格 (类似于 dict) 的读取方式，
    我们应当实现以下魔法方法：
        - __contains__(self, key: str) -> bool
        - __getitem__(self, key: str) -> obj
        - __setitem__(self, key: str, child: HDFTreeNode)
        - __iter__(self) -> iterator
        - __len__(self) -> int
        - keys(self) -> KeysView
        - items(self) -> ItemsView
        - values(self) -> ValuesView

    注意，与 h5py 中表现得不同，不能通过 hdf_path 取到其子节点：
        node['/foo/abc']            (No)
        node['foo']                 (Yes)
    此外，对 Node 的子节点进行修改时，不建议直接使用
        node['foo'] = child_node
    的方式，因为这样可能会有如下副作用：
        - 将 child_node 从其 parent 的子节点中删除
        - 将现有的 node['foo'] 的 parent 属性改成 None
        - 将现有的 node['foo'] 从子节点中删除
        - 将 child_node 的 parent 属性改成 node
        - 将 child_node 的 name 属性改成 'foo'
    因此，建议使用 addChild() 和 deleteChild() 方法，并且由用户手动控制这个过程。


    This node is to indicate Groups in HDF5 files. 
    
    We can add or remove its child. In order to support mapping style (like 
    dict in python), we need to reimplement the following methods:
        - __contains__(self, key: str) -> bool
        - __getitem__(self, key: str) -> obj
        - __iter__(self) -> iterator
        - __len__(self) -> int
        - keys(self) -> KeysView
        - items(self) -> ItemsView
        - values(self) -> ValuesView

    NOTE: Unlike mapping interface in h5py, we cannot get subitem from hdf_path
    like this:
        node['/foo/abc']            (No)
        node['foo']                 (Yes)
    Also, when we need to change subnodes, it is NOT recommended to use
        node['foo'] = child_node
    because it may has following side-effect:
        - delete child_node from its parent's subitems
        - change the 'parent' attribute of current node['foo'] to None
        - delete the current node['foo'] from this subitems
        - change the 'parent' attribute of child_node to this
        - change the 'name' attribute of child_node to 'foo'
    Hence, use addChild() and deleteChild() method instead.


    attributes:
        name: (str) only root's name can and must be null string ''. 

        parent: (HDFTreeNode or NoneType)
    """

    def __init__(self, name: str = '', parent: 'HDFGroupNode' = None):
        """
        arguments:
            name: [optional](str) only root's name can and must be a null stri-
                ng 
            
        parent: [optional](HDFTreeNode or NoneType) only root's parent can and
        must be NoneType.
        """
        super().__init__(name, parent)
        self._mapping = {}
    
    def __getitem__(self, key: str) -> 'HDFTreeNode':
        return self._mapping[key]

    def __iter__(self) -> Iterator:
        return iter(self._mapping)

    def __len__(self) -> int:
        return len(self._mapping)

    def __setitem__(self, key: str, child: HDFTreeNode):
        """
        NOTE: this method may have following side-effect:
            - delete the original child from this node, 
            - change the original child's parent attribute to None
            - delete new child from its original parent,
            - change new child's parent attribute to this,
            - change new child's name to the key

        It is not recommended to use this method to set child. Use addChild()
        and deleteChild() methods instead.
        """
        
        if not isinstance(key, str):
            raise TypeError(('Key must be a string, not '
                '{0}'.format(type(key).__name__)))
        if not isinstance(child, HDFTreeNode):
            raise TypeError(('child must be a HDFTreeNode, not '
                '{0}'.format(type(child).__name__)))

        if key == '':
            raise ValueError('Cannot set child name as a null string')
        elif not reValidHDFName.match(key):
            raise ValueError('Invalid child name: {0}'.format(key))

        if key in self._mapping:    # delete original child from this
            original_child = self._mapping[key]
            original_child.parent = None
            del self._mapping[key]

        self._mapping[child.name] = child

        if child.parent:            # delete child from its original parent
            del child.parent[child.name]
        child.name = key
        child.parent = self

    def __delitem__(self, key: str):
        del self._mapping[key]

    def __contains__(self, key: str) -> bool:
        return key in self._mapping
    
    def addChild(self, child: HDFTreeNode):
        """
        Add a child to this node. Will change child's parent attribute.

        arguments:
            child: (HDFTreeNode)
        """
        if not isinstance(child, HDFTreeNode):
            raise TypeError(('child must be a HDFTreeNode, not '
                '{0}'.format(type(child).__name__)))
        if child.name == '':
            raise ValueError('Cannot set child name as a null string')
        if child.name in self:
            raise ValueError(('Child name already exists: '
                '{0}'.format(child.name)))
        else:
            self._mapping[child.name] = child
            child.parent = self

    def deleteChild(self, child: HDFTreeNode) -> HDFTreeNode:
        """
        Delete a child of this node. Will change child's parent attribute.

        arguments:
            child: (HDFTreeNode)

        returns:
            (HDFTreeNode) the deleted child
        """
        if not isinstance(child, HDFTreeNode):
            raise TypeError(('child must be an HDFTreeNode, not '
                '{0}'.format(type(child).__name__)))
        elif not child.name in self:
            raise KeyError(('child name not found in this node: '
                '{0}'.format(child.name)))
        elif child.parent != self:
            raise ValueError('The parent of child is not this')
        else:
            del self[child.name]
            child.parent = None
            return child

    def keys(self):
        return self._mapping.keys()

    def values(self):
        return self._mapping.values()

    def items(self):
        return self._mapping.items()


class HDFDataNode(HDFTreeNode):
    """
    用来表示 Dataset 的节点。它没有子节点。

    Node used to indicate dataset in HDF5 file. It does not have subnodes.
    """
    def __init__(self, name: str, parent: HDFGroupNode):
        """
        arguments:
            name: (str) the name cannot be null string
            parent: (HDFGroupNode)
        """
        super().__init__(name, parent)
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        """
        Give a new name to this node. The name here must be a string that:
            - can only include numbers, characters, underline '_', dash '-', 
                dot '.' and space ' '.
            - cannot start as space ' '.
        Otherwise a ValueError is raised.

        As an HDFDataNode, its name cannot be a null string.

        arguments:
            new_name: (str) give a new name to this node. User must change the
                practical item's name in the HDF file at the same time. Otherw-
                ise, after a flush the name change will be lost.
        """
        
        # valid_name_pattern = r'^[0-9a-zA-Z\_\-\.][0-9a-zA-Z\_\-\.\s]*$'
        if not isinstance(new_name, str):
            raise TypeError(('new_name must be a str, not '
                '{0}'.format(type(new_name))))
        elif new_name == '':
            raise ValueError(
                'HDFDataNode name attribute cannot set as null string'
            )
        elif not reValidHDFName.match(new_name):
            raise ValueError('Invalid name: {0}'.format(new_name))
        else:
            self._name = new_name


    