# -*- coding: utf-8 -*- 

"""
*----------------------------- MetaTrees.py -----------------------------*
用于构建元数据的树状结构。

它包含三个类：
- SchemaTree 为预定义的元数据结构
- ValueTree 为实际数据集的元数据结构 
- DisplayTree 为用于实际展示的树结构。其根节点为各 SchemaTree 的一级子节点，再
加上 SchemaTree 中未定义的、但又出现在了 ValueTree 中的节点。

作者：          胡一鸣
创建日期：      2023年11月17日

Manages the tree structure of metadatas.

It includes:
- SchemaTree, predifined metadata structures (predefined schema)
- ValueTree, actual metadata of HDF5 datasets
- DisplayTree, the trees to be displayed. Each DisplayTree corresponds to 
the first child node of the SchemaTree. There is also a DisplayTree that 
manages nodes that are not defined in SchemaTree, while do exist in 
ValueTree.

author:         Hu Yiming
date:           Nov 17, 2023 
*----------------------------- MetaTrees.py -----------------------------*
"""

from logging import Logger 
from typing import Iterable, Iterator
from collections.abc import Mapping
import re 

from PySide6.QtCore import QObject, QAbstractItemModel, QModelIndex, Qt 

from bin.HDFManager import HDFHandler
from Constants import APP_VERSION, ItemDataRoles

reValidMetaName = re.compile(
    r'[0-9a-zA-Z\_\-\.][0-9a-zA-Z\_\-\.\s]*$'
)

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
    def __init__(self, display_tree: DisplayTree, parent: QObject = None):
        """
        Initialize the display tree model.

        arguments:
            display_tree: (DisplayTree) the backend display_tree of the model

            parent: (QObject)
        """
        super(DisplayTreeModel, self).__init__(parent)
        self._display_tree = display_tree
        self._root_node = display_tree.root 

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
            parent_node = self._root_node 
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
            if node.path in self._display_tree._schema_tree.schema_keys:
                return self._display_tree._schema_tree.
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
            parent_node = self._root_node
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

        if parent_node is self._root_node:
            return QModelIndex()
        
        return self.createIndex(self._display_tree.getRowOfNode(child_node), 0, parent_node)
        
   