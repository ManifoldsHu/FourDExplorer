# -*- coding: utf-8 -*-

"""
*-------------------------- WidgetImportEMPAD.py -----------------------------*
用于导入 EMPAD 所产生的 4D-STEM 数据的部件。

作者：          胡一鸣
创建时间：      2022年5月5日

Widgets to import 4D-STEM dataset produced by EMPAD.

author:         Hu Yiming
date:           May 5, 2022
*-------------------------- WidgetImportEMPAD.py -----------------------------*
"""

from logging import Logger
import os
from xml.dom.minidom import parse, Document

from PySide6.QtWidgets import QWidget, QFileDialog

from ui import uiWidgetImportEMPAD

class WidgetImportEMPAD(QWidget):
    """
    用于导入 EMPAD 数据的部件。

    包含选择 .xml 头文件的对话框。会自动根据 .xml 文件选择 .raw 文件。

    Widget to import EMPAD dataset.

    This includes a dialog to choose the xml header file. It gets raw file 
    automatically according to the xml file. 
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetImportEMPAD.Ui_Form()
        self.ui.setupUi(self)

        self.ui.lineEdit_xml_path.setReadOnly(True)
        self.ui.lineEdit_raw_path.setReadOnly(True)
        
        self.ui.pushButton_browse.clicked.connect(self._chooseXML)
        

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger 

    def _chooseXML(self):
        """
        Open a dialog to choose xml file.
        """
        xml_path, _ = QFileDialog.getOpenFileName(
            self, 
            'Open EMPAD XML File', 
            './', 
            'EMPAD XML Files (*.xml);;All Files(*)',
        )
        if xml_path == '':
            return 

        xml_path = os.path.abspath(xml_path)
        self.ui.lineEdit_xml_path.setText(xml_path)

        # pre-parse raw file path to show.
        try:
            dir_path = os.path.dirname(xml_path)
            dom_tree = parse(xml_path)
            root = dom_tree.documentElement
            rf = root.getElementsByTagName('raw_file')[0]
            raw_name = rf.getAttribute('filename')
            raw_path = os.path.join(dir_path, raw_name)
            self.ui.lineEdit_raw_path.setText(raw_path)
        except BaseException as e:
            self.logger.error('Cannot find parse location of raw file:\n'
                '{0}'.format(e), exc_info = True)
            

    def getHeaderPath(self) -> str:
        return self.ui.lineEdit_xml_path.text()

    def getRawPath(self) -> str:
        return self.ui.lineEdit_raw_path.text()

        

    

class WidgetImportEMPAD_NJU(WidgetImportEMPAD):
    """
    用于导入 EMPAD 数据的组件。

    包含选择 .xml 头文件的对话框。会自动根据 .xml 文件选择 .raw 文件。该组件用于
    选取 v0.51 版本的 EMPAD 软件所产生的文件，南京大学特供。

    Widget to import EMPAD dataset.

    This includes a dialog to choose the xml header file. It gets raw file 
    automatically according to the xml file. This widget is used to choose
    the file produced by EMPAD software with version 0.51, and is provided
    for Nanjing University only.
    """
    pass 