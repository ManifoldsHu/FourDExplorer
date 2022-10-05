# -*- coding: utf-8 -*-

"""
*---------------------------- HelpActions.py ---------------------------------*
帮助栏的各种 Action。

作者:           胡一鸣
创建日期:       2022年10月6日

This module includes actions in the help menu.
author:         Hu Yiming
date:           Oct 6, 2022
*---------------------------- HelpActions.py ---------------------------------*
"""

import os 
from PySide6.QtCore import QObject 
from PySide6.QtWidgets import QMessageBox 
from PySide6.QtGui import QAction, QIcon 

from Constants import ROOT_PATH
from bin.Widgets.DialogAbout import DialogAbout 

class ActionAbout(QAction):
    """
    打开软件的“关于”界面。

    Open the "about" window.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.triggered.connect(self.openDialogAbout)
        self.setText('About')
        icon_path = os.path.join(ROOT_PATH, 'ui', 'resources', 'icons', '4D.ico')
        _pic = QIcon()
        _pic.addFile(icon_path)
        self.setIcon(_pic)

    def openDialogAbout(self):
        dialog = DialogAbout()
        dialog.exec()
        

