# -*- coding: utf-8 -*- 

"""
*------------------------------ MetaManagers.py ------------------------------*
管理 .4dstem 数据集的元数据。

注意，只有那些基本的量会被存储，而其他参数将被实时计算。例如，加速电压会被存储，而波长
会则由加速电压导出，从而被实时计算。

元数据会以树状的形式进行存储，其树枝节点用大驼峰的形式命名，而叶子节点则用下划线命名法。
当然，在程序中我们不会使用这个特性来决定一个节点是否为叶子节点。

在实际的操作中，我们期望为每项元数据都提供单独的修改界面，从而规范输入。这需要大量的工
作。

此外，该文件中还定义了用于构建元数据的树状结构，包含三个类：
- SchemaTree 为预定义的元数据结构
- ValueTree 为实际数据集的元数据结构 
- DisplayTree 为用于实际展示的树结构。其根节点为各 SchemaTree 的一级子节点，再
加上 SchemaTree 中未定义的、但又出现在了 ValueTree 中的节点。

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

In addition, in this file there are tree structures of metadata, including:
- SchemaTree, predifined metadata structures (predefined schema)
- ValueTree, actual metadata of HDF5 datasets
- DisplayTree, the trees to be displayed. Each DisplayTree corresponds to 
the first child node of the SchemaTree. There is also a DisplayTree that 
manages nodes that are not defined in SchemaTree, while do exist in 
ValueTree.

author:         Hu Yiming
date:           Oct 31, 2023
*------------------------------ MetaManagers.py ------------------------------*
"""

from logging import Logger 
import os 
import json
from typing import Iterable
from typing import Iterator 
from collections.abc import Mapping
import re 

from PySide6.QtCore import QObject
from PySide6.QtCore import QAbstractItemModel
from PySide6.QtCore import QModelIndex
from PySide6.QtCore import Qt 

from Constants import ROOT_PATH
from Constants import APP_VERSION
from Constants import ItemDataRoles
from Constants import HDFType
from bin.HDFManager import HDFHandler 
from bin.MetaManagers.MetadataFields import FloatField
from bin.MetaManagers.MetadataFields import IntField
from bin.MetaManagers.MetadataFields import StringField
from bin.MetaManagers.MetadataFields import MetadataFieldBase

reValidMetaName = re.compile(
    r'[0-9a-zA-Z\_\-\.][0-9a-zA-Z\_\-\.\s]*$'
)


class MetaManager(QObject):
    """
    管理 4D-Explorer 预定义类型的 HDF5 数据集元数据的基类。

    The class that manages metadata of .4dstem datasets.
    """

    _hdf_meta_schema_file = {
        HDFType.FourDSTEM: "4dstem.json",
        HDFType.VectorField: "vec.json",
        HDFType.Image: "img.json",
    }

    _schema_dir_path = os.path.join(ROOT_PATH, 'schema', 'MetaStructures')

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._schema = {}
        self._item_path = None 
        self._schema_tree = None 
        self._value_tree = None 
        self._display_tree = None 
        self._display_tree_model = None 

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler
    
    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger
    
    @property
    def hdf_type(self) -> HDFType:
        return self.hdf_handler.getNode(self._item_path).hdf_type
    
    @property
    def schema_json_path(self) -> str:
        schema_file_name = self._hdf_meta_schema_file[self.hdf_type]
        return os.path.join(self._schema_dir_path, schema_file_name)
        # raise NotImplementedError(
        #     "No schema_json_path assigned. "
        #     "You should success MetaManagerBase and define the path of the json file.")
    
    # def initializeTreeStructures(self, )

    @property
    def display_tree(self) -> "DisplayTree":
        return self._display_tree

    @property
    def display_tree_model(self) -> "DisplayTreeModel":
        return self._display_tree_model

    def initializeMetas(self, item_path: str):
        """
        Initialize schema, value and display trees, and its model.

        arguments:
            item_path: (str) the path of the attribute's dataset
        """
        # hdf_type: HDFType = self.hdf_handler.getNode(item_path).hdf_type
        self._item_path = item_path 

        with open(self.schema_json_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        self._parseSchema(parent_key = '/', definitions = json_data)

        self._schema_tree = SchemaTree(self._schema, parent = self)
        self._value_tree = ValueTree(item_path, parent = self)
        self._display_tree = DisplayTree(
            self._schema_tree, 
            self._value_tree, 
            parent = self,
        )

        self._display_tree_model = DisplayTreeModel(self._display_tree, self)
        self._display_tree_model.meta_manager = self 


    # def createModel(self) -> "DisplayTreeModel":
    #     """
    #     Create a DisplayTreeModel instance
    #     """
    #     self._display_tree_model = DisplayTreeModel(self._display_tree, self)
    #     self._display_tree_model.meta_manager = self 
    #     return self._display_tree_model

    def updateMetas(self) -> "DisplayTreeModel":
        """
        Update meta managers, along with its schema and models.

        returns:
            (DisplayTreeModel) the updated display tree model.
        """
        self.initializeMetas(self._item_path)
        return self._display_tree_model


    # def _initializeSchema(self):
    #     """
    #     Initialize all of the metadata. All values will be set to None.
    #     """
    #     with open(self.schema_json_path, 'r', encoding='utf-8') as f:
    #         json_data = json.load(f)
        
    #     self._parseSchema(parent_key = '/', definitions = json_data)

    def _parseSchema(self, parent_key: str, definitions: dict):
        """
        Recursively parse definitions to handle nested structures.

        arguments:
            definitions: (dict) The current definition (maybe branch or leaf) 
                in the attribute tree

            parent_key: (str) The parent key of the current definition

        returns:
            (dict) the current metadata
        """
        # meta = self._schema
        for key, value in definitions.items():
            full_key = f"{parent_key}/{key}"
            if isinstance(value, dict) and 'type' in value:
                # Assuming that if 'type' is in the dictionary, it is a metadata field
                self._createFieldInstance(full_key, value)
            elif isinstance(value, dict):
                # It is a nested structure, so we need to go deeper
                self._parseSchema(parent_key, value)
            else:
                raise ValueError(f"Invalid format for metadata schema at {full_key}")
    
    def _createFieldInstance(self, full_key: str, field_instance: dict):
        """
        Create field instances depending on field type.

        arguments:
            full_key: (str) The full key of the attribute. 

            field_instance: (dict) the field definition dict parsed from json file
        """
        if field_instance['type'] == 'str':
            field = StringField(
                field_instance.get('title'), 
                field_instance.get('description'),
                parent = self,
            )
            self._schema[full_key] = field
        elif field_instance['type'] == 'int':
            field = IntField(
                field_instance.get('title'),
                field_instance.get('unit'),
                field_instance.get('display_unit'),
                field_instance.get('description'),
                parent = self,
            )
            self._schema[full_key] = field
        elif field_instance['type'] == 'float':
            field = FloatField(
                field_instance.get('title'),
                field_instance.get('unit'),
                field_instance.get('display_unit'),
                field_instance.get('description'),
                parent = self,
            )
            self._schema[full_key] = field
        else:
            raise TypeError(
                f"Invalid type {field_instance['type']} of the field: {full_key}"
            )
            
    def getSchemaField(self, key: str):
        return self._schema[key]
    
    def listKeys(self) -> Iterable:
        return self._schema.keys()
    
    def getSchemaKeys(self):
        return self._schema.keys()
    
    def _getSchemaFields(self, key: str) -> MetadataFieldBase:
        return self._schema[key]
    
    def getSchemaDescription(self, key: str) -> str:
        return self._getSchemaFields(key).description
    
    def getSchemaUnit(self, key: str) -> str:
        field = self._getSchemaFields(key)
        if isinstance(field, (IntField, FloatField)):
            return field.unit
        else:
            return None 
        
    def getSchemaDisplayUnit(self, key: str) -> str:
        field = self._getSchemaFields(key)
        if isinstance(field, (IntField, FloatField)):
            return field.display_unit 
        else:
            return None 

    def getSchemaTitle(self, key: str) -> str:
        return self._getSchemaFields(key).title


# class MetaManagerFourDSTEM(MetaManagerBase):
#     """
#     管理 .4dstem 数据集的元数据的类 

#     The meta manager of .4dstem datasets.
#     """
#     @property
#     def schema_json_path(self) -> str:
#         return os.path.join(ROOT_PATH, 'schema', 'MetaStructures', '4dstem.json')
    

# class MetaManagerImg(MetaManagerBase):
#     """
#     管理 .img 数据集的元数据的类

#     The meta manager of .img datasets.
#     """
#     @property
#     def schema_json_path(self) -> str:
#         return os.path.join(ROOT_PATH, 'schema', 'MetaStructures', 'img.json')
    

# class MetaManagerVec(MetaManagerBase):
#     """
#     管理 .vec 数据集的元数据的类

#     The meta manager of .vec datasets.
#     """
#     @property
#     def schema_json_path(self) -> str:
#         return os.path.join(ROOT_PATH, 'schema', 'MetaStructure', 'vec.json')
    

class MetaTreeNode(Mapping):
    """
    MetaData Schema 路径树的节点。

    所有定义于 Schema 中的 Path 都具有如下特征：
        - 以 '/' 开头
        - 不以 '/' 结尾
        - 不存在连续的 '//'

    Schema Tree 中只需要考虑插入，而不需要考虑修改、删除。毕竟，Schema 是在程序中预
    先定义好的。所有不在 Schema 中的属性都会被扔到 Undefined 中。

    当它没有子节点的时候，它就是个叶子节点。尽管在标准的 Schema 中，合法的属性 key 
    必然是叶子节点。但在我们的实现中，即使不是叶子节点，也可以作为合法的属性 key 使用。

    The node of Metadata Schema Path Tree.

    All of the paths predefined in schema:
        - start with '/'
        - do not end with '/'
        - do not contain '//'
    
    In schema trees, we need only considering insert method. After all, schema 
    are predefined in configure files and should not be changed in runtime. Ot-
    her attriubtes will be listed in Undefined list.
    """
    def __init__(self, name: str, parent: 'MetaTreeNode'|None = None):
        self._name = name 
        self._parent = parent 
        self._mapping = {}

    def __getitem__(self, key: str) -> 'MetaTreeNode':
        return self._mapping[key]
    
    def __iter__(self) -> Iterator:
        return iter(self._mapping)
    
    def __len__(self) -> int:
        return len(self._mapping)
    
    def __str__(self) -> str:
        return f'<MetaTreeNode> name: {self.name}'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    @property
    def name(self) -> str:
        return self._name 
    
    @name.setter 
    def name(self, new_name: str):
        """
        Give a new name to this node. The name here must be a string that:
            - can only includ numbers, characters, underline '_', dash '-', 
            dot '.' and space ' '
            - cannot start with space ' ', end with dot '.'
        Otherwise a ValueError is raised.

        arguments:
            new_name: (str) give a new name to this node. User must change the
                practical item's name in the HDF file at the same time. Otherw-
                ise, after a flush the name change will be lost.
        """
        if not isinstance(new_name , str):
            raise TypeError(f"new_name must be a str, not {type(new_name).__name__}")
        elif new_name == '':
            raise ValueError("New name empty.")
        elif reValidMetaName.fullmatch(new_name) is None:
            raise ValueError(f"Invalid name: {new_name}")
        elif new_name[-1] == '.':
            raise ValueError(f"Invalid name: {new_name}")
        else:
            self._name = new_name 

    @property
    def parent(self):
        return self._parent 
    
    @parent.setter 
    def parent(self, parent: 'MetaTreeNode'):
        """
        Set the parent node of this node.

        arguments:
            parent: (MetaGroupNode) either an MetaTreeNode or MetaRootNode.
        """
        if parent is None:
            self._parent = None 
        elif not isinstance(parent, MetaTreeNode):
            raise TypeError(
                f"parent must be MetaTreeNode or NoneType, not {type(parent)}"
            )
        elif self.isSubNode(parent):
            raise RuntimeError("Loop in meta tree!")
        else:
            self._parent = parent 
            
    @property
    def path(self) -> str:
        """
        Indicates the full meta_path of this node inside the file. Like:
            '/', (root)
            '/foo/abc' (a data node)

            returns:
                (str) the full meta_path of this node
        """
        if self._path_in_tree == '':
            return '/'
        else:
            return self._path_in_tree 
        
    @property
    def _path_in_tree(self) -> str:
        if self.parent is None or self.name == '':
            return ''
        elif self.parent is None and self.name != '':
            return self.name 
        else:
            return self.parent._path_in_tree + '/' + self.name 

    def isSubNode(self, node: 'MetaTreeNode') -> bool:
        """
        Returns whether node is the ancestor of this node.

        If node is just this node, returns True.
        If node is root (does not have parent), returns True.

        arguments:
            node: (MetaTreeNode) potential ancestor node

        returns:
            (bool)
        """
        if not isinstance(node, MetaTreeNode):
            raise TypeError(f"node must be a MetaTreeNode, not {type(node).__name__}")
        
        if node is self:
            return True 
        ancestor = self 
        while not ancestor is None:
            if ancestor is node:
                return True 
            ancestor = ancestor.parent 
        return False 
    
    def addChild(self, child: 'MetaTreeNode'):
        """
        Add a child to this node. Will change child's parent attribute.

        arguments:
            child: (MetaTreeNode)
        """
        if not isinstance(child, MetaTreeNode):
            raise TypeError(f"child must be a MetaTreeNode, not {type(child).__name__}")
        elif child.name == '':
            raise ValueError('Cannot set child name as a null string')
        if child.name in self:
            raise ValueError(f'Child name already exists: {child.name}')
        else:
            self._mapping[child.name] = child 
            child.parent = self 

    def keys(self):
        return self._mapping.keys()
    
    def values(self):
        return self._mapping.values()
    
    def items(self):
        return self._mapping.items()
    
    def __contains__(self, key: str) -> bool:
        return key in self._mapping 


class MetaRootNode(MetaTreeNode):
    def __init__(self):
        super().__init__('', None)
    
    @property
    def name(self) -> str:
        return ''
    
    @property
    def parent(self) -> None:
        return None 


class SchemaTree(QObject):
    def __init__(self, schema_keys: Mapping, parent: QObject = None):
        super().__init__(parent)
        self._schema_keys = schema_keys 
        self._root = self._buildTree()

    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger
    
    @property
    def root(self) -> MetaRootNode:
        return self._root 
    
    @property
    def schema_keys(self) -> Mapping:
        return self._schema_keys

    def _buildTree(self, schema_keys: Mapping) -> MetaRootNode:
        """
        Build the tree structure from the predefined schema keys.

        arguments:
            schema_keys: Iterable of path-like strings represending schema keys

        returns:
            (MetaRootNode) The root node of the constructed schema tree.
        """
        root = MetaRootNode()

        for key in schema_keys:
            if self.isValidPath():
                self._addPathToTree(root, key)

        return root 
    
    def isValidPath(self, path: str) -> bool:
        """
        Check if the given path is a valid schema path.

        arguments:
            path: (str) The path to be checked.

        returns:
            (bool) 
        """
        if path == '/':
            return True 
        elif not path.startswith('/'):
            return False 
        elif '//' in path:
            return False 
        elif path.endswith('/'):
            return False 
        else:
            return True 

    def _addPathToTree(self, root: MetaTreeNode, path: str):
        """
        Add a path to the schema tree, creating intermediate nodes as necessary.

        arguments:
            root: (MetaTreeNode) the root of the schema tree 
            
            path: (str) the path to be added to the tree 
        """
        current_node = root 
        path_parts = path.split('/')[1:]    # split the path and ignore the first
        for part in path_parts:
            if part not in current_node:
                new_node = MetaRootNode(part, current_node)
                current_node.addChild(new_node)

    # def _insertNode(self, current_node: dict, path_parts: list[str]):
    #     """
    #     Recursively insert a node into the tree. 

    #     path            path_parts          path_parts[1:]
    #     /sample         ['', 'sample']      ['sample']
    #     sample          ['sample']          []
    #     sample/         ['sample', '']      ['']
        
    #     """
    #     if not path_parts:  # current node is the last leaf
    #         return 
    #     elif path_parts[0] == '': # current node end with /
    #         return 
        
    #     if path_parts[0] not in current_node:
    #         current_node[path_parts[0]] = {}

    #     self._insertNode(current_node[path_parts[0]], path_parts[1:])


    # def getFirstBranchNodes(self):
    #     """
    #     Get the first level branch nodes of the tree.
    #     """


class ValueTree(QObject):
    def __init__(self, item_path: str, parent: QObject = None):
        super().__init__(parent)
        self._item_path = item_path 
        self._root = MetaRootNode()
        self._undefined_attributes = {}
        self._buildTree() 

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler
    
    @property
    def attributes(self) -> Mapping:
        return self.hdf_handler.file[self._item_path].attrs

    @property
    def undefined_attributes(self) -> Mapping:
        return self._undefined_attributes
    
    @property
    def root(self) -> MetaRootNode:
        return self._root 

    def _buildTree(self):
        for key, value in self.attributes.items():
            if self.isValidPath(key):
                self._addAttributeToTree(self._root, key, value)
            else:
                self._undefined_attributes[key] = value

    def isValidPath(self, path: str) -> bool:
        """
        Check if the given path is a valid schema path.

        arguments:
            path: (str) The path to be checked.

        returns:
            (bool) 
        """
        if path == '/':
            return True 
        elif not path.startswith('/'):
            return False 
        elif '//' in path:
            return False 
        elif path.endswith('/'):
            return False 
        else:
            return True     
        
    def _addAttributeToTree(self, root: MetaRootNode, path: str, value):
        """
        Add an attribute to the tree, creating nodes as necessary.

        arguments
            path: (str) the path of the attribute

            value: (Any) the value of the attribute
        """
        current_node = root
        path_parts = path.split('/')[1:]    # split the path and ignore the first
        for part in path_parts:
            if part not in current_node:
                new_node = MetaRootNode(part, current_node)
                current_node.addChild(new_node)


class DisplayTree(QObject):
    def __init__(
        self, 
        schema_tree: SchemaTree, 
        value_tree: ValueTree, 
        parent:QObject = None,
    ):
        super().__init__(parent)
        self._schema_tree = schema_tree 
        self._value_tree = value_tree 
        self._root = self._buildDisplayTree()

    @property
    def root(self) -> MetaRootNode:
        return self._root 
    
    @property
    def schema_tree(self) -> SchemaTree:
        return self._schema_tree 
    
    @property
    def value_tree(self) -> ValueTree:
        return self._value_tree 
    
    def _buildDisplayTree(self) -> MetaRootNode:
        """
        Build the display tree by combining schema and value trees.

        returns:
            (MetaRootNode)
        """
        root = MetaRootNode()
        self._addSchemaBranches(root, self._schema_tree.root)
        self._addUndefinedAttributes(root)
        return root 
    
    def _addSchemaBranches(self, display_root: MetaTreeNode, schema_root: MetaTreeNode):
        """
        Recursively add branches from the schema tree to the display tree.

        arguments:
            display_root: (MetaTreeNode) The root of the display tree 

            schema_root: (MetaTreeNode) The root of the schema tree
        """
        for child_name, child_node in schema_root.items():
            new_node = MetaTreeNode(child_name, display_root)
            display_root.addChild(new_node)
            self._addSchemaBranches(new_node, child_node)

    def _addUndefinedAttributes(self, display_root: MetaTreeNode):
        """
        Add undefined attributes from the value tree to the display tree.

        arguments:
            display_root: (MetaTreeNode) The root of the display tree
        """
        undefined_node = MetaTreeNode("Undefined", display_root)
        display_root.addChild(undefined_node)
        for key in self._value_tree.attributes:
            if key not in self._schema_tree.schema_keys:
                new_node = MetaTreeNode(key, undefined_node)
                undefined_node.addChild(new_node)
 
    def getNodeByRow(self, parent_node: MetaTreeNode, row: int) -> MetaTreeNode:
        """
        Given a parent node and a row number, return the corresponding child node.

        arguments:
            parent_node: (MetaTreeNode) The parent node

            row: (int) The row number of the child node

        returns:
            (MetaTreeNode) the child node at the given row under the parent node
        """
        if parent_node is None or not isinstance(parent_node, MetaTreeNode):
            raise TypeError("parent_node must be a MetaTreeNode")
        elif row < 0 or row >= len(parent_node):
            raise ValueError("row must be between 0 and len(parent_node)")
        return list(parent_node.values())[row]
    
    def getRowOfNode(self, node: MetaTreeNode) -> int:
        """
        Given a node, return its row number under its parent.

        arguments:
            node: (MetaTreeNode) The node to find the row number for.

        returns:
            (int) The row number of the node under its parent.
        """
        if node.parent is None:
            raise ValueError("root node does not have row index")   # or returns 0?
        return list(node.parent.values()).index(node)

    # def rowCount(self, parent_node: MetaTreeNode) -> int:
    #     return len(parent_node)
    
    # def columnCount(self, parent_node: MetaTreeNode) -> int:
    #     return 1

    # def updateDisplay(self, updated_attributes):
    #     pass 

    # def getAttributeValue(self, key: str):
    #     return self._value_tree.attributes[key]
    
    # def getAttributeTitle(self, key: str):
    #     return self._schema_tree.


class DisplayTreeModel(QAbstractItemModel):
    """
    DisplayTreeModel 用于在 QTreeView 控件中展示 DisplayTree 数据。

    本模型类继承自 QAbstractItemModel，提供了与 DisplayTree 数据交互所需的界面，使
    得 DisplayTree 中的数据可以在 QTreeView 控件中被正确显示和管理。

    DisplayTreeModel 主要处理节点数据的检索、节点层次关系的定义，以及如何在视图中呈现
    这些数据。

    注意：该模型假设 DisplayTree 的节点对象 (MetaTreeNode) 具有 name 属性作为显示名
    称，并且已经实现了 getNodeByRow 和 getRowOfNode 方法。

    DisplayTreeModel is designed for displaying DisplayTree data in a QTreeView
    widget.

    This model class, inheriting from QAbstractItemModel, provides the necessary 
    interface to interact with the DisplayTree data, ensuring that the data from 
    the DisplayTree can be correctly displayed and managed within a QTreeView 
    widget.

    DisplayTreeModel mainly deals with retrieving node data, defining the hier-
    archical relationship of nodes, and how to present these data in the view.

    Note: The model assumes that the node object of DisplayTree (MetaTreeNode) 
    has a name attribute for display and that the methods getNodeByRow and 
    getRowOfNode are already implemented.
    """
    # def __init__(self, display_tree: DisplayTree, meta, parent: QObject = None):
    def __init__(self, meta_manager: MetaManager, parent: QObject = None):
        """
        Initialize the display tree model.

        arguments:
            display_tree: (DisplayTree) the backend display_tree of the model

            parent: (QObject)
        """
        super(DisplayTreeModel, self).__init__(parent)
        # self._display_tree = display_tree
        # self._root_node = display_tree.root
        # self._meta_manager = None 

        self._meta_manager = meta_manager  
        
    
    @property
    def meta_manager(self) -> MetaManager:
        return self._meta_manager 
    
    @meta_manager.setter
    def meta_manager(self, meta_mgr: MetaManager):
        self._meta_manager = meta_mgr

    @property
    def display_tree(self) -> DisplayTree:
        return self._meta_manager._display_tree
    
    @property
    def root_node(self) -> MetaRootNode:
        return self._meta_manager.display_tree.root 

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Returns the number of rows under the given parent. When the parent is valid,
        rowCount() returns the number of children of parent. When the parent is 
        QModelIndex(), rowCount() returns the number of top-level items.

        arguments:
            parent: (QModelIndex) The parent index.

        Returns:
            (int) The number of rows under the given parent.
        """
        if not parent.isValid():
            parent_node = self.root_node 
        else:
            parent_node = parent.internalPointer()
        return len(parent_node)
    
    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Returns the number of columns for the children of the given parent.
        In most subclasses, the number of columns is independent of the parent.

        arguments:
            parent: (QModelIndex) The parent index.

        returns:
            (int) The number of columns for the given parent.
        """
        return 1
    
    def data(self, index: QModelIndex, role: int = ItemDataRoles.DisplayRole):
        """
        Returns the data stored under the given role for the item referred to by the index.

        arguments:
            index: (QModelIndex) The index of the item.

            role: (int) The role for which data is requested.

        returns:
            (Any) The data stored under the given role for the item referred to by the index.
        """
        
        if not index.isValid():
            return None 
        node: MetaTreeNode = index.internalPointer()
        if role == ItemDataRoles.DisplayRole:
            # if node.path in self.display_tree.schema_tree.schema_keys:
            if node.path in self.meta_manager.getSchemaKeys():
                return self.meta_manager.getSchemaTitle(node.path)
            return node.name
        
    def index(
        self, 
        row: int, 
        column: int, 
        parent: QModelIndex = QModelIndex()
    ) -> QModelIndex:
        """
        Returns the index of the item in the model specified by the given row, column, and parent index.

        arguments:
            row: (int) The row number of the item.

            column: (int) The column number of the item.

            parent: (QModelIndex) The parent index of the item.

        returns:
            (QModelIndex) The index of the specified item.
        """
        if not parent.isValid():
            parent_node = self.root_node
        else:
            parent_node = parent.internalPointer()

        child_node = self._display_tree.getNodeByRow(row)
        if row >= 0 and row < len(parent_node):
            self.createIndex(row, column, child_node)
        else:
            return QModelIndex()
        
    def parent(self, index: QModelIndex) -> QModelIndex:
        """
        Returns the parent of the model item with the given index. If the item
        has no parent, an invalid QModelIndex is returned.

        arguments:
            index: (QModelIndex) The index of the item.

        Returns:
            (QModelIndex) The parent index of the specified item.
        """
        if not index.isValid():
            return QModelIndex()
        
        child_node = index.internalPointer()
        parent_node = child_node.parent

        if parent_node is self.root_node:
            return QModelIndex()
        
        return self.createIndex(self._display_tree.getRowOfNode(child_node), 0, parent_node)
        
   