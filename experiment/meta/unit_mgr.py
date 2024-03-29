# -*- coding: utf-8 -*- 
import pint

ureg = pint.UnitRegistry()

# 示例量
ureg.define('nA = 1e-9 * A')  # 纳安
ureg.define('kV = 1e3 * V')   # 千伏
ureg.define('mm = 1e-3 * m')  # 毫米
# ureg.define('um = 1e-6 * m')  # 微米 (μm)
# ureg.define('μm = 1e-6 * m')  # 微米
ureg.define('nm = 1e-9 * m')  # 纳米
ureg.define('Å = 1e-10 * m')  # 埃
ureg.define('rad = radian')  # 弧度
# ureg.define('deg = degree')  # 度
# ureg.define('mrad = 1e-3 * rad')  # 毫弧度
ureg.define('ms = 1e-3 * s')  # 毫秒
# ureg.define('eV = electron_volt')  # 电子伏

if __name__ == '__main__':
    q1 = 3 * ureg.parse_units('mrad')
    print(q1.to(ureg.parse_units('deg')))
    print(f"{q1:~L}")
    q2 = 2 * ureg.parse_units('angstrom') ** 2
    print(f"{q2:~P}")

