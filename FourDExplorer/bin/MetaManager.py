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
from typing import Any
from typing import Iterator 
from collections.abc import Mapping
from collections.abc import Set
from collections.abc import Collection
import re 

from PySide6.QtCore import QObject
from PySide6.QtCore import QAbstractItemModel
from PySide6.QtCore import QModelIndex
from PySide6.QtCore import Qt 
from PySide6.QtCore import Signal 
import numpy as np

from Constants import ROOT_PATH
from Constants import APP_VERSION
# from Constants import ItemDataRoles
from Constants import MetaDataRoles
from Constants import HDFType
from bin.HDFManager import HDFHandler 
from bin.UnitManager import UnitManager
from bin.UIManager import ThemeHandler

 
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

    model_refreshed = Signal()

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._schema = {}
        self._item_path = None 
        self._schema_tree = None 
        self._meta_tree = None 
        self._meta_tree_model = None 
        self._meta_not_pathlike_table_model = None 

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

    @property
    def item_path(self) -> str:
        return self._item_path 

    @property
    def meta_tree(self) -> "MetaTree":
        return self._meta_tree
    
    @property
    def meta_tree_model(self) -> "MetaTreeModel":
        return self._meta_tree_model
    
    @property
    def meta_not_pathlike_table_model(self) -> "MetaNotPathLikeModel":
        return self._meta_not_pathlike_table_model 
    
    def setItemPath(self, item_path: str):
        """
        Set the item path of the meta manager.

        This function will also build the schema tree and value tree for the dataset.

        arguments:
            item_path: (str) the path of the attribute's dataset
        """
        self._item_path = item_path 

        # with open(self.schema_json_path, 'r', encoding='utf-8') as f:
        #     json_data = json.load(f)

        # self._parseSchema(parent_key = '', definitions = json_data)
        # self._schema_tree = SchemaTree(self._schema, parent = self)
        self.initializeSchema(self.hdf_handler.getNode(item_path).hdf_type)

        self._meta_tree = MetaTree(item_path, parent = self)
        self._meta_tree_model = MetaTreeModel(self)
        self._meta_not_pathlike_table_model = MetaNotPathLikeModel(self)

    def initializeSchema(self, hdf_type: HDFType):
        """
        Initialize meta manager according to the hdf_type.

        arguments:
            hdf_type: (HDFType) the type of the target dataset.
        """
        if hdf_type in self._hdf_meta_schema_file:
            with open(self.schema_json_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            self._parseSchema(parent_key = '', definitions = json_data)
            self._schema_tree = SchemaTree(self._schema, parent = self)
        else:
            raise ValueError(f"There is no predefined schema for the {hdf_type}")

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
                self._parseSchema(full_key, value)
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
            
    def getSchemaField(self, key: str) -> 'MetadataFieldBase':
        """
        Get the field in the predefined schema according to the key. 
        
        The field may have title, description, unit and so on.

        arguments:
            key: (str) The key of the metadata 

        returns:
            (MetadataFieldBase) metadata field
        """
        return self._schema[key]
    
    def listKeys(self) -> Set:
        """
        Get the keys of metadata mapping. Note that this is NOT a list.

        returns:
            (Set) The keys view of the metadata.
        """
        return self.hdf_handler.file[self.item_path].attrs.keys()
    
    def listSchemaKeys(self) -> Set:
        """
        Get the keys of schema mapping. Note that this is NOT a list.

        returns:
            (Set) The keys view of the schema. 
        """
        return self._schema.keys()
    
    def _getSchemaFields(self, key: str) -> "MetadataFieldBase":
        """
        Get the fields from schema according to the key of metadata.

        returns:
            (MetadataFieldBase) The field of the metadata.
        """
        return self._schema[key]
    
    def getSchemaDescription(self, key: str) -> str:
        """
        Get the description from predefined schema according to the key.

        arguments:
            (str) The key of the metadata. Must be path-like.

        returns:
            (str) The description of the metadata
        """
        return self._getSchemaFields(key).description
    
    def getSchemaUnit(self, key: str) -> str:
        """
        Get the unit of physical quantity in predefined schema. 
        
        The unit is managed by the UnitManager, and should be SI units.

        arguments:
            (str) The key of the metadata. Must be path-like.

        returns:
            (str) The unit of the metadata or None if there is no unit.
        """
        field = self._getSchemaFields(key)
        if isinstance(field, (IntField, FloatField)):
            return field.unit
        else:
            return None 
           
    def getSchemaDisplayUnit(self, key: str) -> str:
        """
        Get the displayed unit that is read friendly.

        arguments:
            (str) The key of the metadata. Must be path-like.

        returns:
            (str) The displayed unit or None if there is no display unit.
        """
        field = self._getSchemaFields(key)
        if isinstance(field, (IntField, FloatField)):
            return field.display_unit 
        else:
            return None 

    def getSchemaTitle(self, key: str) -> str:
        """
        Get the title of the metadata that is predefined in schema.

        arguments:
            (str) The key of the metadata. Must be path-like.

        returns:
            (str) The title of the metadata.
        """
        return self._getSchemaFields(key).title

    def getValue(self, key: str) -> Any:
        """
        Get the value of the metadata.

        arguments:
            (str) The key of the metadata.

        returns:
            (str) The value of the metadata.
        """
        return self.hdf_handler.file[self.item_path].attrs.get(key)
    
    def getNode(self, key: str) -> 'MetaTreeNode':
        """
        Get the node in the meta tree, according to the key.

        Note that if the key is not a valid path-like string, the node will 
        be a child of the root.

        arguments:
            (str) The key of the metadata.

        returns:
            (MetaTreeNode) the node in the meta tree.
        """
        # if key not in self.listKeys():
        #     raise KeyError(f"Key not found in metadata: {key}")
        if self.meta_tree.isValidPath(key):
            path_parts = key.lstrip('/').split('/')
            node = self.meta_tree.root 
            for part in path_parts:
                node = node[part]
            return node 
        else:
            # return self.meta_tree.root[key]
            raise KeyError(f"Key is not a valid path-like string: {key}.")
            
        
    def matchNodeGenerator(self, kw: str):
        """
        A generator that yields nodes whose metadata key or title matches the 
        key word.

        arguments:
            kw: (str) The key word to be matched.

        returns:
            (generator) Generate MetaTreeNode instance.
        """
        if not isinstance(kw, str):
            raise TypeError(f'kw must be a str, not {type(kw).__name__}')
        def _matchSubNode(node: 'MetaTreeNode'):
            for key in node:
                subnode: MetaTreeNode = node[key]
                if kw in key:
                    yield subnode
                elif subnode.path in self._schema:
                    if kw in self.getSchemaTitle(subnode.path):
                        yield subnode 
                elif len(subnode) > 0:
                    for subsubnode in _matchSubNode(subnode):
                        yield subsubnode 
        return _matchSubNode(self.meta_tree.root)
                
    def matchNumberGeneratorNotPathlike(self, kw: str):
        """
        A generator that yields number whose metadata key matches the key word.

        arguments:
            kw: (str) The key word to be matched.

        returns:
            (generator) Generating the number
        """
        if not isinstance(kw, str):
            raise TypeError(f'kw must be a str, not {type(kw).__name__}')
        def _matchNumber():
            for number, key in enumerate(self.meta_tree.not_path_like_attrs):
                if kw in key:
                    yield number 
        return _matchNumber()
    
    def refreshModel(self):
        """
        Refresh the models.
        """
        self.setItemPath(self.item_path)
        self.model_refreshed.emit()




class MetadataFieldBase(QObject):
    """
    各种元数据项共有的性质，主要是备注。
    """
    def __init__(self, title: str, description: str = "", parent: QObject = None):
        """
        Initialize a metadata field object.

        arguments:
            title: (str) the title of the attribute (for displaying)

            description: (str) the description of the attribute

            parent: (QObject) the parent QObject of the field
        """
        super().__init__(parent)
        self._title = title
        self._description = description 
    
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, desc: str):
        self._description = desc 

    @property
    def title(self) -> str:
        return self._title 
    
    @title.setter 
    def title(self, tt: str):
        self._title = tt


class FloatField(MetadataFieldBase):
    """
    浮点数字段类，具有存储单位、显示单位以及单位转换。
    """
    def __init__(
        self, 
        title: str,
        unit: str = None, 
        display_unit: str = None, 
        description: str = "", 
        parent: QObject = None
    ):
        super().__init__(title, description, parent)
        self._unit = unit 
        self._display_unit = display_unit 
        # TODO: Add unit converting 

    @property 
    def unit(self) -> str:
        return self._unit 
    
    @unit.setter 
    def unit(self, unt: str):
        # TODO: detect unit's alias name 
        self._unit = unt 
    
    @property
    def display_unit(self) -> str:
        return self._display_unit

    @display_unit.setter 
    def display_unit(self, dsp_unt: str):
        # TODO: detect unit's alias name 
        self._display_unit = dsp_unt 


class IntField(MetadataFieldBase):
    """
    整数字段类，目前和浮点数类一致，但大多数情况下它们都不需要单位
    """
    def __init__(
        self,
        title: str,
        unit: str = None,
        display_unit: str = None,
        description: str = "",
        parent: QObject = None,
    ):
        super().__init__(title, description, parent)
        self._unit = unit 
        self._display_unit = display_unit 
        # TODO: Add unit converting 

    @property 
    def unit(self) -> str:
        return self._unit 
    
    @unit.setter 
    def unit(self, unt: str):
        # TODO: detect unit's alias name 
        self._unit = unt 
    
    @property
    def display_unit(self) -> str:
        return self._display_unit

    @display_unit.setter 
    def display_unit(self, dsp_unt: str):
        # TODO: detect unit's alias name 
        self._display_unit = dsp_unt 


class StringField(MetadataFieldBase):
    """
    字符串字段类，目前不需要额外的属性或方法，但保留扩展的可能性 
    """
    pass 


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
    def __init__(self, name: str, parent: 'MetaTreeNode' = None):
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
        # elif self.isSubNode(parent):
        elif parent.isSubNode(self):
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

    def keys(self) -> Set:
        """
        Get the set of keys of the child nodes.

        returns:
            (Set) The key view of the current node.
        """
        return self._mapping.keys()
    
    def values(self) -> Collection:
        """
        Get the values collection of the child nodes.

        returns:
            (Collection) The value view of the current node.
        """
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
    def __init__(self, schema_keys: Set, parent: QObject = None):
        super().__init__(parent)
        self._schema_keys = schema_keys 
        self._root = self._buildTree(self._schema_keys)

    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger
    
    @property
    def root(self) -> MetaRootNode:
        return self._root 
    
    @property
    def schema_keys(self) -> Set:
        return self._schema_keys

    def _buildTree(self, schema_keys: Set) -> MetaRootNode:
        """
        Build the tree structure from the predefined schema keys.

        arguments:
            schema_keys: Set of path-like strings represending schema keys

        returns:
            (MetaRootNode) The root node of the constructed schema tree.
        """
        root = MetaRootNode()
        for key in schema_keys:
            if self.isValidPath(key):
                path_parts = key.lstrip('/').split('/')
                self._addPathToTree(root, path_parts)
                # self._addPathToTree(root, key)
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
        
    def _addPathToTree(self, parent: MetaTreeNode, path_parts: list[str]):
        """
        Add an attribute to the tree, creating nodes as necessary.

        arguments:
            parent: (MetaTreeNode) The parent node to add child recursively.

            path_parts: (list[str]) The paths of the attribute. 
                e.g. ['Calibration', 'Space', 'dp_i']
        """
        if len(path_parts) == 0:
            return None 
        
        part = path_parts[0]
        if part not in parent:
            new_node = MetaTreeNode(part, parent)
            parent.addChild(new_node)
        self._addPathToTree(parent[part], path_parts[1:])


class MetaTree(QObject):
    """
    将具有类似于路径名称的元数据键，按照树的形式组织起来。

    注意，对于那些不为合法的路径的元数据 key，例如不以 / 开头的，我们将其放进 not_path_like_attrs 这个 dict 里。

    Let metadata, whose keys are similar to path names, organize in the form of 
    trees.

    Note that for those keys which are not valid paths, such as strings not 
    beginning with /, we put them into the not_path_like_attrs dict.
    """
    def __init__(self, item_path: str, parent: QObject = None):
        super().__init__(parent)
        self._item_path = item_path 
        self._root = MetaRootNode()
        self._not_path_like_attrs = {}
        self._buildTree() 

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler
    
    @property
    def attributes(self) -> Mapping:
        return self.hdf_handler.file[self._item_path].attrs

    @property
    def not_path_like_attrs(self) -> Mapping:
        return self._not_path_like_attrs
    
    @property
    def root(self) -> MetaRootNode:
        return self._root 

    def _buildTree(self):
        """
        Recursively build the tree according to path lists.
        """
        for key, value in self.attributes.items():
            if self.isValidPath(key):
                path_parts = key.lstrip('/').split('/')
                self._addAttributeToTree(self._root, path_parts)
            else:
                # if key not in self.root:    
                #     # Add those items that is not path like to the root.
                #     new_node = MetaTreeNode(key, self.root)
                #     self.root.addChild(new_node)
                self._not_path_like_attrs[key] = value

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
        
    def _addAttributeToTree(self, parent: MetaTreeNode, path_parts: list[str]):
        """
        Add an attribute to the tree, creating nodes as necessary.

        arguments
            parent: (MetaTreeNode) The parent node to add child recursively.

            path_parts: (list[str]) The paths of the attribute. 
                e.g. ['Calibration', 'Space', 'dp_i']
        """
        if len(path_parts) == 0:
            return None 
        
        part = path_parts[0]
        if part not in parent:
            new_node = MetaTreeNode(part, parent)
            parent.addChild(new_node)
        # Recursively add child nodes 
        self._addAttributeToTree(parent[part], path_parts[1:])

                

    def getNodeByRow(self, parent_node: MetaTreeNode, row: int) -> MetaTreeNode:
        """
        Given a node, return its row number under its parent.

        arguments:
            node: (MetaTreeNode) The node to find the row number for.

        returns:
            (int) The row number of the node under its parent.
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
            # In QAbstractModel, the row index of the root node should be 0
            raise ValueError("root node does not have row index")   # or returns 0? 
            
        return list(node.parent.values()).index(node)


class MetaTreeModel(QAbstractItemModel):
    """
    MetaTreeModel 用于在 QTreeView 控件中展示 MetaTree 的数据。

    本模型类继承自 QAbstractModel，提供了与 MetaTree 数据交互所需的界面，使得
    MetaTree 中的数据可以在 QTreeView 控件中被正确显示和管理。

    MetaTreeModel 主要处理节点数据的检索、节点层次关系的定义，以及如何在视图中呈现
    这些数据。

    注意：对于那些定义于 schema 中的项，在显示时我们将给出其名字、单位和注释。

    MetaTreeModel is designed for displaying MetaTree data in a QTreeView 
    widget.

    This model class, inheriting from QAbstractItemModel, provides the necessary
    interface to interact with the MetaTree data, ensuring that the data from 
    the MetaTree can be correctly displayed and managed within a QTreeView 
    widget.

    MetaTreeModel mainly deals with retrieving node data, defining the hierar-
    chical relationship of nodes, and how to present these data in the view.

    NOTE: For those items defined in the schema, we will display their name, 
    unit and comments, despite their keys and values.
    """
    def __init__(self, meta_manager: MetaManager, parent: QObject = None):
        """
        Initialize the value tree model.

        arguments:
            meta_manager: (MetaManager) the meta manager of the attrs of the dataset

            parent: (QObject)
        """
        super(MetaTreeModel, self).__init__(parent)
        self._meta_manager = meta_manager 

    @property
    def meta_manager(self) -> MetaManager:
        return self._meta_manager
    
    @meta_manager.setter 
    def meta_manager(self, meta_mgr: MetaManager):
        self._meta_manager = meta_mgr 

    @property
    def meta_tree(self) -> MetaTree:
        return self._meta_manager.meta_tree 
    
    @property
    def root_node(self) -> MetaRootNode:
        return self._meta_manager.meta_tree.root 
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler 
    
    @property
    def unit_manager(self) -> UnitManager:
        global qApp 
        return qApp.unit_manager
    
    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler
    
    
    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Returns the number of rows under the given parent. When the parent is valid,
        rowCount() returns the number of children of parent. When the parent is 
        QModelIndex(), rowCount() returns the number of top-level items.

        arguments:
            parent: (QModelIndex) The parent index.

        returns:
            (int): The number of rows under the given parent.
        """
        if not parent.isValid():
            parent_node = self.root_node 
        else:
            parent_node = parent.internalPointer()
        return len(parent_node)
    
    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Returns the number of columns for the children of the given parent. In 
        most subclasses, the number of columns is independent of the parent.

        arguments:
            parent: (QModelIndex) The parent index.

        returns:
            (int) the number of columns for the given parent.
        """
        return 2
    
    def data(self, index: QModelIndex, role: int = MetaDataRoles.DisplayRole):
        """
        Returns the data stored under the given role for the item refered to by 
        the index.

        arguments:
            index: (QModelIndex) The index of the item.

            role: (int) The role for which data is requested.

        returns:
            (Any) The data stored under the given role for the item referred to 
                by the index.
        """
        if not index.isValid():
            return None 
        node: MetaTreeNode = index.internalPointer()
        schema_keys = self.meta_manager.listSchemaKeys()
        value = self.meta_manager.getValue(node.path)
        column = index.column()

        if role == MetaDataRoles.DisplayRole and column == 0:
            if node.path in schema_keys:
                return self.meta_manager.getSchemaTitle(node.path)
            else:
                return node.name 
        elif role == MetaDataRoles.DisplayRole and column == 1:
            return self._makeDisplayValue(index)
        elif role == MetaDataRoles.ToolTipRole:
            if node.path in schema_keys:
                return self.meta_manager.getSchemaDescription(node.path)
            elif isinstance(value, np.ndarray):
                return f'<numpy.ndarray shape: {value.shape}>'
            else:
                return f'<{type(value).__name__}: {self.data(index, Qt.DisplayRole)}>'

        elif role == MetaDataRoles.NodeRole:
            return node 
        elif role == MetaDataRoles.KeyRole:
            return node.path 
        elif role == MetaDataRoles.ValueRole:
            return value
        elif role == MetaDataRoles.ValueTypeRole:
            raise NotImplementedError(f"Unsupported role: {role}")
        elif role == MetaDataRoles.DecorationRole and column == 0:
            _path = ":/HDFItem/resources/icons/"
            if len(node) > 0:
                icon_name = 'folder'
            else:
                icon_name = 'file'
            return self.theme_handler.iconProvider(_path + icon_name)
            # _path = ":/HDFItem/resources/icons/file"
            # return self.theme_handler.iconProvider(_path)

        return None 
    

    def index(
        self,
        row: int,
        column: int,
        parent: QModelIndex = QModelIndex()
    ) -> QModelIndex:
        """
        Returns the index of the item in the model specified by the given row, 
        column and parent index.

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
        
        if row >= 0 and row < len(parent_node):
            # child_node = self.value_tree.getNodeByRow(parent_node, row)
            child_node = self.meta_tree.getNodeByRow(parent_node, row)
            return self.createIndex(row, column, child_node)
        else:
            return QModelIndex()
        

    def parent(self, index: QModelIndex) -> QModelIndex:
        """
        Returns the parent of the model item with the given index. If the item 
        has no parent, an invalid QModelIndex is returned.

        arguments:
            index: (QModelIndex) The index of the item.

        returns:
            (QModelIndex) The parent index of the specified item.
        """
        if not index.isValid():
            return QModelIndex()
        child_node = index.internalPointer()
        parent_node = child_node.parent 
        if parent_node is self.root_node:
            return QModelIndex()
        return self.createIndex(self.meta_tree.getRowOfNode(child_node), 0, parent_node)
    

    def _makeDisplayValue(self, index: QModelIndex) -> str:
        """
        Returns the proper string according to the type of metadata value.

        If the metadata item has predefined unit in schema, it will append the 
        unit after the value.

        argument:
            index: (QModelIndex) the model index of the item.

        returns:
            (str) the displayed string of the value. 
        """
        node: MetaTreeNode = index.internalPointer()
        schema_keys = self.meta_manager.listSchemaKeys()
        attrs = self.hdf_handler.file[self.meta_manager.item_path].attrs 
        value = attrs.get(node.path)
        if value is None:
            return ""
        if node.path not in schema_keys:
            if isinstance(value, np.ndarray):
                if len(value) > 5:
                    return f'<numpy.ndarray> shape: {value.shape}'
            return f"{value}"
        
        # The actual unit of the stored metadata value. (e.g. 'm')
        real_unit = self.meta_manager.getSchemaUnit(node.path)    
        if real_unit is None:
            return f"{value}"
        
        # The displayed unit of the value. (e.g. 'nm')
        display_unit = self.meta_manager.getSchemaDisplayUnit(node.path)
        if display_unit is None:
            # TODO: Format displaying with rich text
            # return f"{value:.4g} {real_unit}"  
            return self.unit_manager.formatUnit(real_unit, value, context = 'unicode')
        try:
            display_value = self.unit_manager.convert(value, real_unit, display_unit)
        except ValueError:
            # return f"{value:.4g} {real_unit}"
            return self.unit_manager.formatUnit(real_unit, value, context = 'unicode')
        else:
            return self.unit_manager.formatUnit(display_unit, display_value, context = 'unicode')
            # return f"{display_value:.4g} {display_unit}"    #TODO: Format displying with rich text.


    def indexFromKey(self, key: str) -> QModelIndex:
        """
        Get the model index from a key.

        arguments:
            key: (str) The key of the meta data item.

        returns:
            (QModelIndex) Must be the index of column 0.
        """
        if not isinstance(key, str):
            raise TypeError(f'key must be a str, not {type(key).__name__}')
        node = self.meta_manager.getNode(key)
        if node is self.root_node:
            return QModelIndex()
        row = list(node.parent.keys()).index(node.name)
        return self.createIndex(row, 0, node)
    

    def keyFromIndex(self, index: QModelIndex) -> str:
        """
        Get the key from a model index.

        arguments:
            index: (QModelIndex) The index of the item.

        returns:
            (str) The key of the metadata.
        """
        return self.data(index, role = MetaDataRoles.KeyRole)


    def headerData(
        self, section: int, 
        orientation: Qt.Orientation = Qt.Horizontal, 
        role: int = Qt.DisplayRole
    ) -> str:
        """
        Write the header data of the metadata tree.

        arguments:
            section: (int) The column of the header

            orientation: (Qt.Orientation) The column or row head 

            role: (int) 

        returns:
            (str) The head string of the metadata tree.
        """
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return 'KEY'
            elif section == 1:
                return 'VALUE'
            
    def matchIndexGenerator(self, kw: str):
        """
        A generator that yields the indexes matching the keywords.

        arguments:
            kw: (str) The key words for matching

        returns:
            (generator) A generator that generates QModelIndex that has the 
                same substring in its name as the kw. 
        """
        for node in self.meta_manager.matchNodeGenerator(kw):
            node: MetaTreeNode
            yield self.indexFromKey(node.path)
            


# class MetaTableModel(QAbstractTableModel):
#     """
#     用于在表格中展示 Metadata 所需的 Model。

#     HDF5 的数据集与 Group 具有 attrs 属性，这是一个类似于 Mapping 的数据结构。在该表格中，
#     有两列，左列是 key，右列是 value。

#     为了实现只读的、显示与数据分离的架构，这个 Model 类必须实现如下方法：
#         - rowCount(self, parent: QModelIndex) -> int
#             返回相应的 parent 之下有多少行

#         - data(self, index: QModelIndex, role: int)
#             根据 role 的不同，返回数据结构中内部存储的数据

#     注意，实践证明，不能使用 HDF5 本身的对象作为 ptr，原因不明，可能与 HDF5 采用的锁
#     机制有关；所以，唯一方案便是自己创建一个 meta 副本，而只在修改时访问 HDF5 文件。

#     This is a model for viewing attributions of HDF5 objects.

#     Attributions of HDF5 objects are like Mapping (dict in python), So we use
#     a table to show them. There are 2 columns in the table, the left contains
#     keys, while the right contains values.

#     This is a part of Model/View architecture of Qt. If we want to display the
#     path tree, we can instantiate QTreeView, and call its setModel() method.

#     In order to realize a read-only and data-display decoupled architecture, we
#     need to reimplement the following methods:
#         - rowCount(self, parent: QModelIndex) -> int
#             Get number of rows under the parent

#         - data(self, index: QModelIndex, role: int)
#             Return the internal data according to the role

#     NOTE: Practice shows that it seems we cannot use h5py.AttributeManager 
#     itself as the ptr, and I don't know why. So here we create a replica: meta
#     as a dict, which will always conserves the same as the attrs. Only when we
#     need to modify the attribution, we use attrs.

#     attributes:
#         hdf_handler: (HDFHandler)

#         item_path: (str) the corresponding h5py object's path

#         attrs: (h5py.AttributeManager) the AttributeManager of the h5py object

#         meta: (dict) replica. always conserves the same as self.attrs
#     """

#     def __init__(self, parent: QObject = None):
#         super().__init__(parent)
#         self._item_path = '/'
#         self._meta = {}

#     @property
#     def hdf_handler(self) -> HDFHandler:
#         global qApp 
#         return qApp.hdf_handler

#     @property
#     def item_path(self) -> str:
#         return self._item_path

#     @item_path.setter
#     def item_path(self, path: str):
#         self.hdf_handler.getNode(path)
#         self._item_path = path 

#     @property
#     def meta(self):
#         return self._meta

#     @property
#     def attrs(self) -> h5py.AttributeManager:
#         return self.hdf_handler.file[self.item_path].attrs

#     @property
#     def logger(self) -> Logger:
#         global qApp
#         return qApp.logger
    
#     def initialize(self, item_path: str):
#         """
#         Initialize the model, copy items from h5py.AttributeManager to 
#         self._meta dict.

#         arguments:
#             item_path: (str) the path of the dataset or group.
#         """
#         self.item_path = item_path
#         self.beginRemoveRows(QModelIndex(), 0, self.rowCount())
#         self._meta = {}
#         self.endRemoveRows()
#         self.beginInsertRows(QModelIndex(), 0, len(self.attrs))
#         for key in self.attrs:
#             self.meta[key] = self.attrs[key]
#         self.endInsertRows()

#     def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
#         """
#         The number of columns.

#         arguments:
#             parent: (QModelIndex)

#         returns:
#             (int) 2. left is key, right is value.
#         """
#         return 2
    
#     def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
#         """
#         The number of rows.
#         """
#         return len(self.meta)
    
#     def data(self, index: QModelIndex, role: int):
#         """
#         The data of the attributions.

#         arguments:
#             index: (QModelIndex)

#             role: int (ItemDataRoles)
#         """
#         if not index.isValid():
#             return None
#         row = index.row()
#         column = index.column()
#         key = list(self.meta.keys())[row]
#         value = self.meta[key]
#         if role == Qt.DisplayRole:
#             if column == 0:
#                 return f'{key}'
#             elif column == 1:
#                 if isinstance(value, np.ndarray):
#                     if len(value) > 5:
#                         return f'<numpy.ndarray> shape: {value.shape}'
#                 return f'{value}'
#             else:
#                 return None
#         elif role == Qt.ToolTipRole:
#             if isinstance(value, np.ndarray):
#                 return f'<numpy.ndarray shape: {value.shape}>'
#             else:
#                 return f'<{type(value).__name__}: {self.data(index, Qt.DisplayRole)}>'
#         else:
#             return None
        
#     def headerData(
#         self, 
#         section: int, 
#         orientation: Qt.Orientation = Qt.Horizontal, 
#         role: int = Qt.DisplayRole
#     ):
#         """
#         Write the header data of the table.

#         arguments:
#             section: (int)

#             orientation: (Qt.Orientation)

#             role: (int)

#         returns:
#             (str) 'KEY' or 'VALUE' or ''.
#         """
#         if role == Qt.DisplayRole and orientation == Qt.Horizontal:
#             if section == 0:
#                 return 'KEY'
#             elif section == 1:
#                 return 'VALUE'
#         return None
    
#     def indexFromKey(self, key: str) -> QModelIndex:
#         """
#         Get the index from a key.

#         arguments:
#             key: (str)

#         returns:
#             (QModelIndex) must be the index of column 0.
#         """
#         if not isinstance(key, str):
#             raise TypeError('key must be a str, not '
#                 '{0}'.format(type(key).__name__))
#         if not key in self.meta:
#             raise KeyError('Key not founded.')
        
#         row = list(self.meta.keys()).index(key)
#         column = 0
#         return self.createIndex(row, column)
    
#     def keyFromIndex(self, index: QModelIndex) -> str:
#         """
#         Get the key from the index.

#         arguments:
#             index: (QModelIndex)

#         returns:
#             (str) the key of the corresponding index, regardless the column.
#         """
#         row = index.row()
#         return list(self.meta.keys())[row]
    
#     def createItem(self, key: str, value):
#         """
#         Add an item.
        
#         arguments:
#             key: (str)

#             value: Any (str, int, float, np.ndarray)
#         """
#         if not isinstance(key, str):
#             raise TypeError('key must be a str, not '
#                 '{0}'.format(type(key).__name__))
#         if key in self.meta:
#             raise ValueError('key already exists.')

#         self.beginInsertRows(
#             QModelIndex(), 
#             self.rowCount(), 
#             self.rowCount(),
#         )
        
#         self.attrs.create(key, value)
#         self.meta[key] = value
#         self.endInsertRows()
#         self.logger.debug(f'Create Attrbute {key} in {self.item_path}')

#     def deleteItem(self, index: QModelIndex):
#         """
#         Delete an item according to the index.

#         arguments:
#             index: (QModelIndex)
#         """
#         if not isinstance(index, QModelIndex):
#             raise TypeError('index must be QModelIndex, not '
#                 '{0}'.format(type(index).__name__))
#         if not index.isValid():
#             return None
#         key = self.keyFromIndex(index)
#         row = index.row()
#         self.beginRemoveRows(QModelIndex(), row, row)
#         del self.attrs[key]
#         del self.meta[key]
#         self.endRemoveRows()
#         self.logger.debug('Delete Attribute {0} in {1}'.format(
#             key, self.item_path
#         ))

#     def modifyValue(self, index: QModelIndex, value):
#         """
#         Modify an item. The type should not be changed.

#         arguments:
#             index: (QModelIndex)

#             value: Any (must conserve the type of the original item)
#         """
#         if not isinstance(index, QModelIndex):
#             raise TypeError('index must be QModelIndex, not '
#                 '{0}'.format(type(index).__name__))
#         if not index.isValid():
#             return None
#         key = self.keyFromIndex(index)
#         self.attrs.modify(key, value)
#         self.meta[key] = value
#         self.dataChanged.emit(QModelIndex(), index)
#         self.logger.debug('Change the value of attribute {0} in {1}'.format(
#             key, self.item_path
#         ))


class MetaNotPathLikeModel(QAbstractItemModel):
    """
    用于在表格中展示非合法路径的 Metadata 所需的 Model。

    HDF5 的数据集与 Group 具有 attrs 属性，这是一个类似于 Mapping 的数据结构。在该表格中，
    有两列，左列是 key，右列是 value。

    为了实现只读的、显示与数据分离的架构，这个 Model 类必须实现如下方法：
        - rowCount(self, parent: QModelIndex) -> int
            返回相应的 parent 之下有多少行

        - data(self, index: QModelIndex, role: int)
            根据 role 的不同，返回数据结构中内部存储的数据

    注意，实践证明，不能使用 HDF5 本身的对象作为 ptr，原因不明，可能与 HDF5 采用的锁
    机制有关；所以，唯一方案便是自己创建一个 meta 副本，而只在修改时访问 HDF5 文件。

    This is a model for viewing attributions of HDF5 objects whose keys are not 
    path like.

    Attributions of HDF5 objects are like Mapping (dict in python), So we use
    a table to show them. There are 2 columns in the table, the left contains
    keys, while the right contains values.

    This is a part of Model/View architecture of Qt. If we want to display the
    path tree, we can instantiate QTreeView, and call its setModel() method.

    In order to realize a read-only and data-display decoupled architecture, we
    need to reimplement the following methods:
        - rowCount(self, parent: QModelIndex) -> int
            Get number of rows under the parent

        - data(self, index: QModelIndex, role: int)
            Return the internal data according to the role

    NOTE: Practice shows that it seems we cannot use h5py.AttributeManager 
    itself as the ptr, and I don't know why. So here we create a replica: meta
    as a dict, which will always conserves the same as the attrs. Only when we
    need to modify the attribution, we use attrs.

    attributes:
        hdf_handler: (HDFHandler)

        item_path: (str) the corresponding h5py object's path

        attrs: (h5py.AttributeManager) the AttributeManager of the h5py object

        meta: (dict) replica. always conserves the same as self.attrs
    """
    def __init__(self, meta_manager: MetaManager, parent: QObject = None):
        super(MetaNotPathLikeModel, self).__init__(parent)
        self._meta_manager = meta_manager

    @property
    def meta_manager(self) -> MetaManager:
        return self._meta_manager
    
    @meta_manager.setter 
    def meta_manager(self, meta_mgr: MetaManager):
        self._meta_manager = meta_mgr 

    @property
    def meta_tree(self) -> MetaTree:
        return self._meta_manager.meta_tree 

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler

    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler
    
    @property
    def meta_not_pathlike(self) -> Mapping:
        return self.meta_tree.not_path_like_attrs

    # @property
    # def item_path(self) -> str:
    #     return self._item_path
    
    # @item_path.setter
    # def item_path(self, path: str):
    #     self.hdf_handler.getNode(path)
    #     self._item_path = path 

    # @property
    # def meta(self) -> Mapping:
    #     return self._meta
    
    # @property
    # def attrs(self) -> h5py.AttributeManager:
    #     return self.hdf_handler.file[self.item_path].attrs

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Returns the number of rows under the given parent. When the parent is valid,
        rowCount() returns the number of children of parent. When the parent is 
        QModelIndex(), rowCount() returns the number of top-level items.

        In MetaNotPathlikeModel, the row count is always the same as the length of 
        meta_not_pathlike mapping.

        arguments:
            parent: (QModelIndex) The parent index.

        returns:
            (int): The number of rows under the given parent.
        """
        if not parent.isValid():
            return len(self.meta_not_pathlike)
        else:
            return 0
    
    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return 2
    
    def data(self, index: QModelIndex, role: int = MetaDataRoles.DisplayRole):
        if not index.isValid():
            return None 
        row = index.row()
        column = index.column()
        key = list(self.meta_not_pathlike.keys())[row]
        value = self.meta_not_pathlike[key]
        if role == MetaDataRoles.DisplayRole and column == 0:
                return f'{key}'
        elif role == MetaDataRoles.DisplayRole and column == 1:
            if isinstance(value, np.ndarray):
                if len(value) > 5:
                    return f'<numpy.ndarray> shape: {value.shape}'
            return f'{value}'
        elif role == MetaDataRoles.ToolTipRole:
            if isinstance(value, np.ndarray):
                return f'<numpy.ndarray shape: {value.shape}>'
            else:
                return f'<{type(value).__name__}: {self.data(index, Qt.DisplayRole)}>'
        elif role == MetaDataRoles.KeyRole:
            return key 
        elif role == MetaDataRoles.ValueRole:
            return value
        elif role == MetaDataRoles.ValueTypeRole:
            raise NotImplementedError(f"Unsupported role: {role}")
        elif role == MetaDataRoles.NodeRole:
            raise NotImplementedError(f"Unsupported role: {role}")
        elif role == MetaDataRoles.DecorationRole and column == 0:
            _path = ":/HDFItem/resources/icons/file"
            return self.theme_handler.iconProvider(_path)
        return None
        
    def index(
        self,
        row: int,
        column: int,
        parent: QModelIndex = QModelIndex()
    ) -> QModelIndex:
        """
        Returns the index of the item in the model specified by the given row, 
        column and parent index.

        arguments:
            row: (int) The row number of the item.

            column: (int) The column number of the item.

            parent: (QModelIndex) The parent index of the item.

        returns:
            (QModelIndex) The index of the specified item.
        """
        if not parent.isValid():
            key = list(self.meta_not_pathlike.keys())[row]
            return self.createIndex(row, column, self.meta_not_pathlike[key])
        else:
            return QModelIndex()
        
    def parent(self, index: QModelIndex) -> QModelIndex:
        """
        Returns the parent of the model item with the given index. If the item 
        has no parent, an invalid QModelIndex is returned.

        arguments:
            index: (QModelIndex) The index of the item.

        returns:
            (QModelIndex) The parent index of the specified item.
        """
        return QModelIndex()

    def headerData(
        self, section: int, 
        orientation: Qt.Orientation = Qt.Horizontal, 
        role: int = Qt.DisplayRole
    ) -> str:
        """
        Write the header data of the metadata tree.

        arguments:
            section: (int) The column of the header

            orientation: (Qt.Orientation) The column or row head 

            role: (int) 

        returns:
            (str) The head string of the metadata tree.
        """
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return 'KEY'
            elif section == 1:
                return 'VALUE'
            
    def indexFromKey(self, key: str) -> QModelIndex:
        """
        Get the index from a key.

        arguments:
            key: (str)

        returns:
            (QModelIndex) must be the index of column 0.
        """
        if not isinstance(key, str):
            raise TypeError('key must be a str, not '
                '{0}'.format(type(key).__name__))
        if not key in self.meta_not_pathlike:
            raise KeyError('Key not founded.')
        row = list(self.meta_not_pathlike.keys()).index(key)
        column = 0
        return self.createIndex(row, column, self.meta_not_pathlike[key])
    
    def keyFromIndex(self, index: QModelIndex) -> QModelIndex:
        """
        Get the key from the index.

        arguments:
            index: (QModelIndex)

        returns:
            (str) the key of the corresponding index, regardless the column.
        """
        row = index.row()
        return list(self.meta_not_pathlike.keys())[row]
    
    def matchIndexGenerator(self, kw: str):
        """
        A generator that yields the indexes matching the keywords.

        arguments:
            kw: (str) The key words for matching

        returns:
            (generator) A generator that generates QModelIndex that has the 
                same substring included in its name as the kw.
        """
        for number in self.meta_manager.matchNumberGeneratorNotPathlike(kw):
            yield self.createIndex(number, 0)
    

        

    
