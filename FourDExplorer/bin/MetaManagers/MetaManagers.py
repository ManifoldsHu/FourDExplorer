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
*------------------------------ MetaManagers.py ------------------------------*
"""

from logging import Logger 
import os 
import json
from typing import Iterable

from PySide6.QtCore import QObject

from Constants import ROOT_PATH
from bin.HDFManager import HDFHandler 
from bin.MetaManagers.MetadataFields import FloatField
from bin.MetaManagers.MetadataFields import IntField
from bin.MetaManagers.MetadataFields import StringField
from bin.MetaManagers.MetadataFields import MetadataFieldBase

class MetaManagerBase(QObject):
    """
    管理 4D-Explorer 预定义类型的 HDF5 数据集元数据的基类。

    The class that manages metadata of .4dstem datasets.
    """

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._schema = {}
        self._initializeSchema()

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler
    
    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger
    
    @property
    def schema_json_path(self) -> str:
        raise NotImplementedError(
            "No schema_json_path assigned. "
            "You should success MetaManagerBase and define the path of the json file.")

    def _initializeSchema(self):
        """
        Initialize all of the metadata. All values will be set to None.
        """
        with open(self.schema_json_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        self._parseSchema(parent_key = '/', definitions = json_data)

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
            
    def getField(self, key: str):
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


class MetaManagerFourDSTEM(MetaManagerBase):
    """
    管理 .4dstem 数据集的元数据的类 

    The meta manager of .4dstem datasets.
    """
    @property
    def schema_json_path(self) -> str:
        return os.path.join(ROOT_PATH, 'schema', 'MetaStructures', '4dstem.json')
    

class MetaManagerImg(MetaManagerBase):
    """
    管理 .img 数据集的元数据的类

    The meta manager of .img datasets.
    """
    @property
    def schema_json_path(self) -> str:
        return os.path.join(ROOT_PATH, 'schema', 'MetaStructures', 'img.json')
    

class MetaManagerVec(MetaManagerBase):
    """
    管理 .vec 数据集的元数据的类

    The meta manager of .vec datasets.
    """
    @property
    def schema_json_path(self) -> str:
        return os.path.join(ROOT_PATH, 'schema', 'MetaStructure', 'vec.json')
    