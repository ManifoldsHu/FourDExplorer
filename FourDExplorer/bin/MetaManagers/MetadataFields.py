#-*- coding: utf-8 -*- 

"""
*---------------------------- MetadataFields.py ----------------------------*
定义各类预定义的元数据项所具有的性质，包括类型、存储单位、显示单位、备注等。

作者：          胡一鸣
创建时间：      2023年10月31日


*---------------------------- MetadataFields.py ----------------------------*
"""

from PySide6.QtCore import (
    QObject,
)

class MetadataFieldBase(QObject):
    """
    各种元数据项共有的性质，主要是备注。
    """
    def __init__(self, value, description = "", parent: QObject = None):
        super().__init__(parent)
        self._value = value 
        self._description = description 

    @property 
    def value(self):
        return self._value 
    
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, desc: str):
        self._description = desc 


class FloatField(MetadataFieldBase):
    """
    浮点数字段类，具有存储单位、显示单位以及单位转换。
    """
    def __init__(
        self, 
        value: float, 
        unit = None, 
        display_unit = None, 
        description = "", 
        parent = None
    ):
        super().__init__(value, description, parent)
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
    整数字段类，目前不需要额外的属性或方法，但保留扩展的可能性 
    """
    pass 


class StringField(MetadataFieldBase):
    """
    字符串字段类，目前不需要额外的属性或方法，但保留扩展的可能性 
    """
    pass 


