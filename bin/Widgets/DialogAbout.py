# -*- coding: utf-8 -*-

"""
*---------------------------- DialogAbout.py ---------------------------------*
软件的关于界面。

作者:           胡一鸣
创建日期:       2022年10月6日

The dialog to show the 'about' information.

author:         Hu Yiming
date:           Oct 6, 2022
*---------------------------- DialogAbout.py ---------------------------------*
"""

import os
from PySide6.QtWidgets import QDialog, QWidget
from PySide6.QtGui import QPixmap
from Constants import ROOT_PATH, APP_VERSION
from ui import uiDialogAbout, icon_rc 

class DialogAbout(QDialog):
    """
    用于查看软件信息的对话框。

    Dialog to view the information of the software.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogAbout.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('About')

        
        icon_path = os.path.join(ROOT_PATH, 'ui', 'resources', 'icons', '4D.png')
        _pic = QPixmap(icon_path)
        _pic.setDevicePixelRatio(4)
        self.ui.label_icon.setPixmap(_pic)
        # self.ui.graphicsView.setPixmap(_pic) 
        # self.ui.graphicsView.setStyleSheet(
        #     "border-image: url(:/WindowIcon/resources/icons/4D.png;"
        # )

        version = '.'.join([str(v) for v in (APP_VERSION)])
        self.ui.label_version.setText(version)
        self.ui.label_version_en.setText(version)
