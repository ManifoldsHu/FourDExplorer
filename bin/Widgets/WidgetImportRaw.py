# -*- coding: utf-8 -*-

"""
*--------------------------- WidgetImportRaw.py ------------------------------*
用来导入二进制文件所包含的 4D-STEM 数据的部件。

作者：          胡一鸣
创建时间：      2022年5月5日

Widgets to import 4D-STEM dataset from binary raw file.

author:         Hu Yiming
date:           May 5, 2022
*--------------------------- WidgetImportRaw.py ------------------------------*
"""

import os 

from PySide6.QtWidgets import QWidget, QFileDialog

from ui import uiWidgetImportRaw

class WidgetImportRaw(QWidget):
    """
    用于导入二进制数据的部件。

    Widget to import binary 4D-STEM data.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetImportRaw.Ui_Form()
        self.ui.setupUi(self)

        self.ui.lineEdit_raw_path.setReadOnly(True)
        self.ui.pushButton_browse.clicked.connect(self._chooseRawFile)

    def _chooseRawFile(self):
        """
        Open a dialog to choose raw file.
        """
        raw_path, _ = QFileDialog.getOpenFileName(
            self, 
            'Open Binary Raw File', 
            './', 
            'All Files(*)',
        )
        if raw_path == '':
            return 
        raw_path = os.path.abspath(raw_path)
        self.ui.lineEdit_raw_path.setText(raw_path)

    def getRawPath(self) -> str:
        return self.ui.lineEdit_raw_path.text()

    def getScalarType(self) -> str:
        _map = {
            'integer': 'int',
            'unsigned integer': 'uint',
            'float': 'float',
        }
        return _map[self.ui.comboBox_scalar_type.currentText()]

    def getScalarSize(self) -> int:
        _map = {
            '8 bit': 1,
            '16 bit': 2,
            '32 bit': 4,
        }
        return _map[self.ui.comboBox_scalar_size.currentText()]

    def getDp_i(self) -> int:
        return self.ui.spinBox_dp_i.value()

    def getDp_j(self) -> int:
        return self.ui.spinBox_dp_j.value()

    def getScan_i(self) -> int:
        return self.ui.spinBox_scan_i.value()

    def getScan_j(self) -> int:
        return self.ui.spinBox_scan_j.value()

    def getOffsetToFirstImage(self) -> int:
        return self.ui.spinBox_offset_to_first_image.value()

    def getGapBetweenImages(self) -> int:
        return self.ui.spinBox_gap_between_images.value()

    def getLittleEndian(self) -> bool:
        return self.ui.checkBox_little_endian.isChecked()