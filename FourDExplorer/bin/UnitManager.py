#-*- coding: utf-8 -*- 

"""
*---------------------------- MetadataFields.py ----------------------------*
使用 pint 管理元数据的单位

作者：          胡一鸣
创建日期：      2023年10月31日

Use pint to manage units of metadata.

author:         Hu Yiming
date:           Oct 31, 2023
*---------------------------- MetadataFields.py ----------------------------*
"""

from logging import Logger 
from PySide6.QtCore import QObject 
import pint 

class UnitManager(QObject):
    """
    管理元数据的单位，包括换算关系、显示。

    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._ureg = pint.UnitRegistry()
        # self._ureg.define('pix')
        # self._registerStandardUnits() 

    # def _registerStandardUnits(self):
    #     """
    #     Register standard units and our own units.
    #     """
    #     # example: self._ureg.define('angstrom = 1e-10 * meter')
    #     # 使用已经内置的基本单位
    #     # 如 m (米), s (秒), A (安培), K (开尔文), mol (摩尔), cd (坎德拉), kg (千克)
    #     # (国际单位制基本单位)

    #     # 定义非基本单位，但常用的单位
    #     self._ureg.define('nA = 1e-9 * A')  # 纳安
    #     self._ureg.define('kV = 1e3 * V')   # 千伏
    #     self._ureg.define('mm = 1e-3 * m')  # 毫米
    #     self._ureg.define('um = 1e-6 * m')  # 微米 (μm)
    #     self._ureg.define('μm = 1e-6 * m')  # 微米
    #     self._ureg.define('nm = 1e-9 * m')  # 纳米
    #     self._ureg.define('Å = 1e-10 * m')  # 埃

    #     # 对于更复杂的单位，如平方米，可以直接使用内置单位
    #     # m^2, nm^2 不需要特别定义

    #     # 定义角度单位
    #     self._ureg.define('rad = radian')  # 弧度
    #     self._ureg.define('deg = degree')  # 度
    #     self._ureg.define('mrad = 1e-3 * rad')  # 毫弧度

    #     # 定义时间单位
    #     self._ureg.define('ms = 1e-3 * s')  # 毫秒

    #     # 定义电场强度单位
    #     self._ureg.define('N/C = newton / coulomb')  # 牛顿每库仑
    #     self._ureg.define('V/m = volt / meter')  # 伏特每米

    #     # 定义能量单位
    #     self._ureg.define('eV = electron_volt')  # 电子伏

    #     # 定义空间频率单位
    #     # self._ureg.define('m^-1 = 1 / meter')  # 每米

    #     # 添加埃（Ångström）
    #     # self._ureg.define('angstrom = 1e-10 * meter')  # 埃

    def registerUnit(self, definition: str):
        """
        Register new unit and its convert relationship between existing units.

        arguments:
            definition: (str) the definition of the new unit. 
                e.g. "new_unit = 1000 * base_unit"

        exceptions:
            pint.errors.DefinitionSyntaxError: invalid unit 

            pint.errors.RedefinitionError: attempt to redefine an existing unit
        """
        self._ureg.define(definition)

    @property 
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Converting unit.

        arguments:
            value: (float) current value of the physical quantity

            from_unit: (str) current unit of the physical quantity

            to_unit: (str) the wanted unit of the physical quantity

        returns:
            (float) the value corresponding to the wanted unit
        """
        # TODO: 判断 from_unit 和 to_unit 是否注册，如果没有注册，报 ValueError
        if from_unit not in self._ureg:
            raise ValueError("Unit is not recognized: {0}".format(from_unit))
        if to_unit not in self._ureg:
            raise ValueError("Unit is not recognized: {0}".format(to_unit))
        quantity = self._ureg.Quantity(value, from_unit)
        return quantity.to(to_unit).magnitude 
    
    def formatUnit(self, unit_str: str, value: float = None, context = "general") -> str:
        """
        Return a specific format of the unit.

        There are 3 kind of format: general, unicode, and TeX. The general form-
        atting is registered in pint, but may not be displayed to the user. The 
        unicode will be displayed in QLable, while TeX will be displayed in mat-
        plotlib widgets.

        arguments:
            unit_str: (str) the unit name 

            value: (float) the physical value

            context: (str) should be one of "general", "unicode" or "TeX"

        returns:
            (str) the formatted unit str
        """
        try:
            unit = self._ureg.parse_units(unit_str)

            if context in ("general", None, ''):
                return self._formatUnitGeneral(unit, value)
            elif context in ("tex", "TeX", "TEX", "LaTeX", "LATEX", "latex"):
                return self._formatUnitTex(unit, value)
            elif context in ("Unicode", "unicode", "utf-8", "UTF-8"):
                return self._formatUnitUnicode(unit, value)
            else:
                raise ValueError("Invalid context for unit formatting")
        except pint.errors.UndefinedUnitError as e:
            return f"{value} {unit_str}"

    def _formatUnitGeneral(self, unit: pint.Unit, value: float = None) -> str:
        """
        Format unit in general cases.

        arguments:
            unit: (Unit) the input unit to be formatted

            value: (float) the physical value

        returns:
            (str) General formatted unit str.
        """
        if value:
            return f"{value * unit:P}"
        return f"{unit:P}"
    
    def _formatUnitTex(self, unit: pint.Unit, value: float = None) -> str:
        """
        Format unit to TeX, for displaying in matplotlib widgets.

        NOTE: Here We deliberately leave a space in front of the unit to meet 
        scientific literature requirements, except degree "°".

        arguments:
            unit: (Unit) the input unit to be formatted.

            value: (float) the physical value

        returns:
            (str) the TeX formatted unit str.
        """
        if value:
            return f"{value * unit:~L}"
        return f"{unit:~L}"
    
    def _formatUnitUnicode(self, unit: pint.Unit, value: float = None) -> str:
        """
        Format unit to Unicode, for displaying in plain text.

        arguments:
            unit: (Unit) the input unit to be formatted.

            value: (float) the physical value

        returns:
            (str) the unicode formatted unit str.
        """
        if value:
            return f"{value * unit:~P}"
        return f"{unit:~P}"
    
    def isUnitLength(self, unit_str: str) -> bool:
        """
        Determines whether the dimension of a unit is a length.

        arguments:
            unit_str: (str) The inspected unit, e.g. 'nm'

        returns:
            (bool) True if the unit is a length, False otherwise.
        """
        try:
            unit = self._ureg.parse_units(unit_str)
            dim = unit.dimensionality
            length_dim = self._ureg.meter.dimensionality
            return dim == length_dim 
        except pint.errors.UndefinedUnitError as e:
            return False 
        
    
    def isUnitSpaceFrequency(self, unit_str: str) -> bool:
        """
        Determins whether the dimension of a unit is a space frequency.

        arguments:
            unit_str: (str) The unit to checked, e.g. 'm ** -1'

        returns:
            (bool) True is the unit is a space frequency, False otherwise.
        """
        if '^' in unit_str:
            unit_str = unit_str.replace('^', '**')
        try:
            unit = self._ureg.parse_units(unit_str)
            dim = unit.dimensionality 
            space_frequency_dim = (1 / self._ureg.meter).dimensionality
            return dim == space_frequency_dim
        except pint.errors.UndefinedUnitError as e:
            return False 
