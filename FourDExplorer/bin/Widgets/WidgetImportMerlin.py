# -*- coding: utf-8 -*- 

"""
*-------------------------- WidgetImportMerlin.py -----------------------------*
用于导入 MerlinEM (Medipix3) 所产生的 4D-STEM 数据 (.mib 文件) 的部件。

作者：          胡一鸣
创建时间：      2024年1月19日

Widgets to import 4D-STEM dataset produced by MerlinEM (Medipix3) from the .mib 
files.

author:         Hu Yiming
date:           Jan 19, 2024
*-------------------------- WidgetImportMerlin.py -----------------------------*
"""

from logging import Logger 
import os 

from PySide6.QtWidgets import QWidget 
from PySide6.QtWidgets import QFileDialog 
from PySide6.QtWidgets import QMessageBox

from ui import uiWidgetImportMerlin 

class WidgetImportMerlin(QWidget):
    """
    用于导入 MerlinEM 数据的部件。

    包含选择 .mib 文件和 .hdr 文件的对话框。会自动根据 .mib 文件或 .hdr 文件选择对应的
    文件。

    Widget to import MerlinEM dataset.

    This includes dialogs to choose the .mib file and .hdr file. It can get .mib 
    file or .hdr file according to the chosen companion file.  
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetImportMerlin.Ui_Form()
        self.ui.setupUi(self)

        self.ui.lineEdit_hdr_path.setReadOnly(True)
        self.ui.lineEdit_mib_path.setReadOnly(True)
        self.ui.pushButton_browse_hdr.clicked.connect(self._chooseHDR)
        self.ui.pushButton_browse_mib.clicked.connect(self._chooseMIB)

        # self.ui.checkBox_default_scan.checked.connect(self._disableSetScan)
        # self.ui.checkBox_default_scan.unchecked.connect(self._enableSetScan)
        self.ui.checkBox_default_scan.stateChanged.connect(self._setScan)
        self.ui.checkBox_default_scan.setChecked(True)

        self.ui.spinBox_scan_i.setMaximum(2**20)
        self.ui.spinBox_scan_j.setMaximum(2**20)
        self.ui.spinBox_scan_i.setMinimum(1)
        self.ui.spinBox_scan_j.setMinimum(1)

        self._has_get_file_automatically = False 

    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger 
    
    def _chooseHDR(self):
        """
        Open a dialog to choose .hdr file.

        If it is the first time to choose .hdr file, it will automatically set 
        the companion .mib file with the same file name, and try parsing the 
        scanning coordinate length (scan_i and scan_j).
        """
        hdr_path, _ = QFileDialog.getOpenFileName(
            self, 
            'Open MerlinEM (Medipix3) HDR File',
            './',
            'MerlinEM HDR Files (*.hdr);;All Files(*)', 
        )
        if hdr_path == '':
            return 
        
        hdr_path = os.path.abspath(hdr_path)
        self.ui.lineEdit_hdr_path.setText(hdr_path)

        # try getting the companion .mib file 
        if not self._has_get_file_automatically:
            hdr_name, _ = os.path.splitext(hdr_path)
            mib_path = hdr_name + '.mib'
            self.ui.lineEdit_mib_path.setText(mib_path)
            self._has_get_file_automatically = True 
        
        try:
            self._setAutoScan()
        except Exception as e:
            self.logger.error(f'Cannot parse .hdr file: {e}', exc_info = True)
            self._warnToSetScanManually()
            
            
        
    def _chooseMIB(self):
        """
        Open a dialog to choose .mib file.

        If it is the first time to choose .mib file, it will automatically set
        the companion .hdr file with the same file name, and try parsing the 
        scanning coordinate length (scan_i and scan_j).
        """
        mib_path, _ = QFileDialog.getOpenFileName(
            self, 
            'Open MerlinEM (Medipix3) MIB File',
            './',
            'MerlinEM MIB Files (*.mib);;All Files(*)', 
        )

        if mib_path == '':
            return 
        
        mib_path = os.path.abspath(mib_path)
        self.ui.lineEdit_mib_path.setText(mib_path)

        # try getting the companion .hdr file 
        if not self._has_get_file_automatically:
            mib_name, _ = os.path.splitext(mib_path)
            hdr_path = mib_name + '.hdr'
            self.ui.lineEdit_hdr_path.setText(hdr_path)
            self._has_get_file_automatically = True 
            try:
                self._setAutoScan()
            except Exception as e:
                self.logger.error(f'Cannot parse .hdr file: {e}', exc_info = True)
                self._warnToSetScanManually()


    def _warnToSetScanManually(self):
        """
        Open a message box to remind the user to set scanning coordinates 
        (scan_i, scan_j) manually.
        """
        self.ui.checkBox_default_scan.setChecked(False)
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Cannot parse .hdr file. You need to set scanning coordinates manually.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
        

    def getHeaderPath(self) -> str:
        return self.ui.lineEdit_hdr_path.text()
    
    def getMibPath(self) -> str:
        return self.ui.lineEdit_mib_path.text()
    
    @property
    def hdr_path(self) -> str:
        return self.ui.lineEdit_hdr_path.text()
    
    @property
    def raw_path(self) -> str:
        return self.ui.lineEdit_mib_path.text()
    
    @property
    def scan_i(self) -> int:
        return self.ui.spinBox_scan_i.value()
    
    @property
    def scan_j(self) -> int:
        return self.ui.spinBox_scan_j.value()

    def _setAutoScan(self):
        """
        Automatically set scanning coordinates (scan_i, scan_j) from .hdr file.
        """
        # _hdr_meta = {}
        with open(self.hdr_path, encoding = 'utf-8') as hdr_file:
            total_image_number = 0
            scan_j_test = 0
            for line in hdr_file:
                if line.startswith("HDR") or line.startswith("END"):
                    continue 
                key, value = line.split('\t')
                key = key.rstrip(':')
                value = value.rstrip('\n')
                if key == "Frames in Acquisition (Number)":
                    total_image_number = int(value) 
                elif key == "Frames per Trigger (Number)":
                    scan_j_test = int(value)
            
            if total_image_number > 0 and scan_j_test > 0:
                scan_i = total_image_number // scan_j_test 
                scan_j = scan_j_test 
                self.ui.spinBox_scan_i.setValue(scan_i)
                self.ui.spinBox_scan_j.setValue(scan_j)
                # self.ui.checkBox_default_scan.setChecked(True)
            else:
                raise LookupError("Cannot find valid scanning coordinate in the .hdr file.")
            
    def _setScan(self):
        """
        Enable or disable to set scanning coordinate manually.

        This function should work as a slot of the checkBox_default_scan 
        stateChaned signal.
        """
        is_auto_scan_disabled = not self.ui.checkBox_default_scan.isChecked()
        self.ui.spinBox_scan_i.setEnabled(is_auto_scan_disabled)
        self.ui.spinBox_scan_j.setEnabled(is_auto_scan_disabled)

    # def _disableSetScan(self):
    #     """
    #     Disable to set scanning coordinate manually. 

    #     This function should work as a slot of the checkBox_default_scan checked.
    #     """
    #     self.ui.spinBox_scan_i.setEnabled(False)
    #     self.ui.spinBox_scan_j.setEnabled(False)

    # def _enableSetScan(self):
    #     """
    #     Enable to set scanning coordinate manually.

    #     This function should work as a slot of the checkBox_default_scan unchecked.
    #     """
    #     self.ui.spinBox_scan_i.setEnabled(True)
    #     self.ui.spinBox_scan_j.setEnabled(True)

    
        

          

            
            
            