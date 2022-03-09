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

import os
import sys
from enum import Enum, IntEnum
from PySide6.QtCore import Qt 

# Absolutely path of FourDExplorer directory
global ROOT_PATH
ROOT_PATH = os.path.dirname(__file__)

# The version of the application
global APP_VERSION 
APP_VERSION = (0, 5, 0)

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
    """
    Item = 1
    Root = 10
    Group = 11
    Data = 20
    FourDSTEM = 21      # Dataset (data cube) of 4D-STEM
    Line = 22           # One dimension matrix
    Image = 23          # Two dimension matrix
    VectorField = 24    # Matrix with shape (2, m, n)
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


class UITheme(IntEnum):
    """
    The theme of ui. Default is light_blue
    """
    dark_amber = 110
    dark_blue = 120
    dark_cyan = 130
    dark_lightgreen = 140
    dark_pink = 150
    dark_purple = 160
    dark_red = 170
    dark_teal = 180
    dark_yellow = 190

    light_amber = 210
    light_blue = 220
    light_cyan = 230
    light_cyan_500 = 231
    light_lightgreen = 240
    light_pink = 250
    light_purple = 260
    light_red = 270
    light_teal = 280
    light_yellow = 290

    default = 220
    default_dark = 130


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








# class UIMode(Enum):
#     '''
#     The theme of ui. Default is light.
#     '''
#     Light = 1
#     Dark = 2

#     Default = 1

# class UIColor(Enum):
#     '''
#     The color of ui. Default is blue.
#     '''
#     Amber = 1
#     Blue = 2
#     Cyan = 3
#     LightGreen = 4
#     Pink = 5
#     Purple = 6
#     Red = 7
#     Teal = 8
#     Yellow = 9

#     Default = 1
#     CustomColor = 10















