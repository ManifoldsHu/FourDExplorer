# -*- coding: utf-8 -*- 

"""
*------------------------- CalibrationMiscs.py -------------------------------*
这里有一些常用的，用于计算 4D-STEM 空间关系及校正的函数。

作者:           胡一鸣
创建日期:       2023年12月12日

There are some functions used for calculating 4D-STEM space relationship and 
calibration.

author:         Hu Yiming
date:           Dec 12, 2023
*------------------------- CalibrationMiscs.py -------------------------------*
"""

h = 6.62e-34        # Plunck's constant 
e = 1.6e-19         # Charge of an electron
m_e = 9.1e-31       # Mass of an electron
c = 3.0e8           # Light speed

import numpy as np

def Voltage2WaveLength(voltage: float):
    """
    Calculate the wave length of the electron beams according to the accelerate 
    voltage.

    arguments:
        voltage: (float) the accelerate voltage of the beam. Unit: V

    returns:
        (float): the wavelength of the matter wave. Unit: m
    """
    return h*c/np.sqrt((e*voltage + 2*m_e*c**2) * e * voltage)

def WaveLength2Voltage(wave_length: float):
    """
    Calculate the accelerate voltage of the electron beams according to their 
    wavelength.

    arguments:
        wave_length: (float) the wave length of the matter wave. Unit: m 

    returns:
        (float): the accelerate voltage of the beam. Unit: V
    """
    return (np.sqrt((m_e * c**2)**2 + h*c / wave_length**2) - m_e * c**2) / e 

