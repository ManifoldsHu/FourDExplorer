# -*- coding: utf-8 -*- 

"""
*--------------------------- DialogEditMeta.py -------------------------------*
DialogEditMeta 用于编辑 HDF5 文件中 Group 或者 Dataset 的元数据/属性 attrs。

需要注意的是，该窗口支持对任意 key 进行任意三种数据类型 (int, float 和 str) 的编辑。
然而对于 4D-STEM 应用中常见的实验参数，我们不建议使用该窗口进行编辑，因为我们会提供特
定的、能展示参数相关信息的页面进行修改。

作者：          胡一鸣
创建时间：      2023年3月5日

The DialogEditMeta is used to edit the metadata/attributes (attrs) of a Group 
or Dataset in an HDF5 file.

It is important to note that this window supports editing of any key for any of 
the three data types (int, float, and str). However, for experimental parameters 
common in 4D-STEM applications, we do not recommend using this window for editing. Instead, we will provide specific pages that display relevant parameter 
information for modifications.

author:        Hu Yiming
date:          Mar 5, 2024
*--------------------------- DialogEditMeta.py -------------------------------*
"""

from logging import Logger 

from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox  
from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import QObject 

from bin.MetaManager import MetaManager 
from bin.MetaManager import MetaTree 
from bin.MetaManager import MetaTreeModel 
from bin.HDFManager import HDFHandler
from bin.UIManager import ThemeHandler

from ui import uiDialogEditMeta

class DialogEditMeta(QWidget):
    """
    Dialog to edit attrs of items in the HDF5 file.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogEditMeta.Ui_Dialog()
        self.ui.setupUi(self)

        self._meta_manager = None 
        self._initEditDialog()
    
    @property 
    def meta_manager(self) -> MetaManager:
        return self._meta_manager 
    
    @property
    def meta_tree(self) -> MetaTree:
        return self._meta_manager.meta_tree
    
    @property
    def meta_tree_model(self) -> MetaTreeModel:
        return self._meta_manager.meta_tree_model
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler
    
    @property
    def item_path(self) -> str:
        return self.ui.lineEdit_item_path.text()
    
    @property
    def meta_key(self) -> str:
        return self.ui.lineEdit_meta_key.text()
    
    def _initEditDialog(self):
        """
        Initialize the edit metadata dialog.
        """
        self.ui.pushButton_ok.clicked.connect(self._slot_ok_clicked)
        self.ui.pushButton_cancel.clicked.connect(self._slot_cancel_clicked)
        self.ui.pushButton_change_dtype.clicked.connect(self._slot_change_dtype_clicked)

    def _slotOkClicked(self):
        """
        Slot of OK button clicked. Save the edited metadata to HDF5 file.
        """
        item_path = self.item_path 
        meta_key = self.meta_key

        current_page_index = self.ui.stackedWidget_set_value.currentIndex()
        if current_page_index == 0:     # Integer
            meta_value = self.ui.spinBox_edit_integer.value()
        elif current_page_index == 1:   # Float
            decimal_part = self.ui.doubleSpinBox_float_decimal.value()
            exp_part = self.ui.spinBox_float_exp.value()
            meta_value = decimal_part * (10 ** exp_part)
        else:
            meta_value = self.ui.plainTextEdit_edit_string.toPlainText()

        try:
            self.hdf_handler.file[item_path].attrs[meta_key] = meta_value 
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to save metadata: {str(e)}')
        else:
            QMessageBox.information(self, 'Success', 'Metadata saved successfully.')
            self.close()

    def _slotCancelClicked(self):
        """
        Slot for Cancel button clicked. Close the dialog without saving.
        """
        self.close()

    def _slotChangeDtypeClicked(self):
        """
        Slot for Change Data Type button clicked. Switch the stacked widget page.
        """
        current_page_index = self.ui.stackedWidget_set_value.currentIndex()
        new_page_index = (current_page_index + 1) % 3 
        # TODO 

    def setItemPath(self, item_path: str):
        """
        Set the item path (Dataset or Group) to edit metadata for.

        arguments:
            item_path: (str) The path of the Dataset or Group in the HDF5 file.
        """
        self.ui.lineEdit_item_path.setText(item_path)

    def setMetaKey(self, meta_key: str):
        """
        Set the key of the metadata to edit.

        arguments:
            meta_key: (str) The key of the metadata.
        """
        self.ui.lineEdit_meta_key.setText(meta_key)

    def readMetaFromFile(self):
        """
        Read the metadata value from the HDF5 file and display in the dialog.
        """
        item_path = self.item_path 
        meta_key = self.meta_key 

        try:
            meta_value = self.hdf_handler.file[item_path].attrs[meta_key]
        except KeyError:
            QMessageBox.warning(self, 'Warning', f'Metadata key "meta_key" not found.' )
            return 
        
        if isinstance(meta_value, int):
            self.ui.stackedWidget_set_value.setCurrentIndex(0)
            self.ui.spinBox_edit_integer.setValue(meta_value)
            self.ui.label_current_dtype.setText('Integer')
        elif isinstance(meta_value, float):
            self.ui.stackedWidget_set_value.setCurrentIndex(1)
            decimal_part, exp_part = f'{meta_value:e}'.split('e')
            self.ui.doubleSpinBox_float_decimal.setValue(float(decimal_part))
            self.ui.spinBox_float_exp.setValue(int(exp_part))
            self.ui.label_current_dtype.setText('Float')
        elif isinstance(meta_value, str):
            self.ui.stackedWidget_set_value.setCurrentIndex(2)
            self.ui.plainTextEdit_edit_string.setPlainText(meta_value)
            self.ui.label_current_dtype.setText('String')
        else:
            QMessageBox.warning(self, 'Warning', f'Unsupported data type: {type(meta_value)}')


