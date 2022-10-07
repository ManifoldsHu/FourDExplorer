# -*- coding: utf-8 -*-

'''
*------------------------------ Constants.py ---------------------------------*
储存了常用的 Constants 以及枚举类。

作者:           胡一鸣
创建日期:       2022年2月19日

Constants and Enumerates.

author:         Hu Yiming
date:           Feb 19, 2022
*------------------------------ Constants.py ---------------------------------*
'''

# The version of the application
global APP_VERSION 
APP_VERSION = (0, 5, 8)

import logging
import os
import sys
from enum import Enum, IntEnum
from PySide6.QtCore import Qt 

# Absolutely path of FourDExplorer directory
global ROOT_PATH
ROOT_PATH = os.path.dirname(__file__)

# The absolute path of the configuration file
global CONFIG_PATH
CONFIG_PATH = os.path.join(ROOT_PATH, '.config')

class HDFType(IntEnum):
    """
    HDF item's type, Will be used when building Path Tree in HDFHandler.
    
    For practical Path Tree Nodes, only those groups will have childs, while o-
    ther nodes will only be Data Nodes.
    
    Although external links may be reference of groups, we see it as data, and 
    use special methods to handle them.

    For data with special types, we have extension name:
        FourDSTEM:      4d
        Line:           line
        Image:          img
        VectorField:    vec
    These extension name will act just like in the operation system, and is not
    a prerequisite for renderers or other algorithms. It is recommended to add 
    these extension, because 4D-Explorer will be able to recognize them.
    """
    Item = 1
    Root = 10
    Group = 11
    Data = 20           # Dataset, extension: no extension
    FourDSTEM = 21      # Dataset (data cube) of 4D-STEM, extension: 4d
    Line = 22           # One dimension matrix, extension: line
    Image = 23          # Two dimension matrix, extension: img
    VectorField = 24    # Matrix with shape (2, m, n), extension: vec
    String = 30         # String
    Reference = 40      # Reference


class ItemDataRoles(IntEnum):
    """
    Optional choice for getting data from QModelIndex.

    For more information of those roles in Qt, read the official document.
    """
    # General purpose roles
    DisplayRole = Qt.DisplayRole
    DecorationRole = Qt.DecorationRole
    EditRole = Qt.EditRole
    ToolTipRole = Qt.ToolTipRole
    StatusTipRole = Qt.StatusTipRole
    WhatsThisRole = Qt.WhatsThisRole
    SizeHintRole = Qt.SizeHintRole 
    NodeRole = Qt.UserRole          # Get the path node instance of the index
    PathRole = Qt.UserRole + 1      # Get the absolute path of the index
    HDFTypeRole = Qt.UserRole + 2    # Get the insider data's type of the index

    # Roles describing appearance and meta data (with associated types)
    FontRole = Qt.FontRole 
    TextAlignmentRole = Qt.TextAlignmentRole 
    BackgroundRole = Qt.BackgroundRole 
    ForegroundRole = Qt.ForegroundRole 
    CheckStateRole = Qt.CheckStateRole
    InitialSortOrderRole = Qt.InitialSortOrderRole

    # Accessibility roles (with associated types)
    AccessibleTextRole = Qt.AccessibleTextRole
    AccessibleDescriptionRole = Qt.AccessibleDescriptionRole


class UIThemeColor(IntEnum):
    """
    The primary color of ui. Default is Indigo.
    """
    Amber = 1000
    Blue = 1010
    BlueGray = 1020
    Brown = 1030
    Cyan = 1040
    DeepOrange = 1050
    DeepPurple = 1060
    Gray = 1070
    Green = 1080
    Indigo = 1090
    LightBlue = 1100
    LightGreen = 1110
    Lime = 1120
    Orange = 1130
    Pink = 1140
    Purple = 1150
    Red = 1160
    Teal = 1170
    Yellow = 1180
    PurpleNJU = 2000

    default = 1020

class UIThemeMode(IntEnum):
    """
    The mode of ui. Default is Light.
    """
    Light = 1
    Dark = 2
    Classical = 3

    default = 1


class UIThemeDensity(IntEnum):
    """
    The density of ui. Default is normal.
    """
    Large = 1
    Big = 0
    Normal = -1
    Small = -2
    Tiny = -3

    default = -1
    

class TaskState(IntEnum):
    """
    The state of Task object.
    """
    Initialized = 1     # The task is initialized
    Waiting = 2         # The task is added to waiting queue.
    Cancelled = 3       # The task in the waiting queue is cancelled
    Submitted = 4       # The task in the waiting queue is about to execute
    Completed = 5       # The task has executed and already completed.
    Aborted = 6         # The task is aborted when executing, forced by user.
    Excepted = 7        # The task is aborted when executing, due to exceptions.


class LogLevel(IntEnum):
    """
    The level of logging.
    """
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL
    FATAL = logging.FATAL















