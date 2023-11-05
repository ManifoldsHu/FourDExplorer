#-*- coding: utf-8 -*- 

"""
*---------------------------- MetadataFields.py ----------------------------*
使用 pint 管理元数据的单位

作者：          胡一鸣
创建时间：      2023年10月31日


*---------------------------- MetadataFields.py ----------------------------*
"""

from logging import Logger 
from PySide6.QtCore import QObject 
import pint 

class UnitManager(QObject):
    """
    管理元数据的单位，包括换算关系、显示。
    
    使用示例：
        unit_manager = UnitManager()
        converted_value = unit_manager.convert(10, 'mm', 'm')
        formatted_unit = unit_manager.format_unit('m^2', 'html') # m<sup>2</sup>
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._ureg = pint.UnitRegistry()
        self._registerStandardUnits() 

    def _registerStandardUnits(self):
        """
        Register standard units and our own units.
        """
        # example: self._ureg.define('angstrom = 1e-10 * meter')
        # 使用已经内置的基本单位
        # 如 m (米), s (秒), A (安培), K (开尔文), mol (摩尔), cd (坎德拉), kg (千克)
        # (国际单位制基本单位)

        # 定义非基本单位，但常用的单位
        self._ureg.define('nA = 1e-9 * A')  # 纳安
        self._ureg.define('kV = 1e3 * V')   # 千伏
        self._ureg.define('mm = 1e-3 * m')  # 毫米
        self._ureg.define('um = 1e-6 * m')  # 微米 (μm)
        self._ureg.define('nm = 1e-9 * m')  # 纳米

        # 对于更复杂的单位，如平方米，可以直接使用内置单位
        # m^2, nm^2 不需要特别定义

        # 定义角度单位
        self._ureg.define('rad = radian')  # 弧度
        self._ureg.define('deg = degree')  # 度
        self._ureg.define('mrad = 1e-3 * rad')  # 毫弧度

        # 定义时间单位
        self._ureg.define('ms = 1e-3 * s')  # 毫秒

        # 定义电场强度单位
        self._ureg.define('N/C = newton / coulomb')  # 牛顿每库仑
        self._ureg.define('V/m = volt / meter')  # 伏特每米

        # 定义能量单位
        self._ureg.define('eV = electron_volt')  # 电子伏

        # 定义空间频率单位
        self._ureg.define('m^-1 = 1 / meter')  # 每米

        # 添加埃（Ångström）
        self._ureg.define('angstrom = 1e-10 * meter')  # 埃

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
    
    def formatUnit(self, unit_str: str, context = "general") -> str:
        """
        Return a specific format of the unit.

        There are 3 kind of format: general, html, and TeX. The general form-
        atting is registered in pint, but may not be displayed to the user. The 
        html will be displayed in QLable, while TeX will be displayed in mat-
        plotlib widgets.

        arguments:
            unit_str: (str) the unit name 

            context: (str) must be one of "general", "html" and "TeX"

        returns:
            (str) the formatted unit str
        """
        unit = self._ureg.parse_units(unit_str)
        if context == "general":
            return "{0:~}".format(unit)
        elif context in ("html", "HTML"):
            return self._formatUnitHtml(unit)
        elif context in ("tex", "TeX", "TEX", "LaTeX", "LATEX", "latex"):
            return self._formatUnitTex(unit)
        else:
            raise ValueError("Invalid context for unit formatting")
        
    def _formatUnitHtml(self, unit: pint.Unit) -> str:
        """
        Format unit to html, for displaying in QLable

        arguments:
            unit: (Unit) the input unit to be formatted.

        returns:
            (str) the HTML formatted unit str
        """
        unit_str = str(unit)
        html_mappings = {
            'm^2': 'm<sup>2</sup>',
            'nm^2': 'nm<sup>2</sup>',
            'um': 'μm',
            'deg': '°',
            'm^-1': 'm<sup>-1</sup>',
        }
        return html_mappings.get(unit_str, unit_str) 
    
    def _formatUnitTex(self, unit: pint.Unit) -> str:
        """
        Format unit to TeX, for displaying in matplotlib widgets.

        NOTE: Here We deliberately leave a space in front of the unit to meet 
        scientific literature requirements, except degree "°".

        arguments:
            unit: (Unit) the input unit to be formatted.

        returns:
            (str) the TeX formatted unit str.
        """
        unit_str = str(unit)

        tex_mappings = {
        'm^2': ' m$^2$',
        'nm^2': ' nm$^2$',
        'um': ' μm',  # 使用 Unicode 字符
        'deg': '°',  # 对于角度单位不添加空格
        'm^-1': ' m$^{-1}$',
        }
        return tex_mappings.get(unit_str, ' ' + unit_str)
    
