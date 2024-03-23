# -*- coding: utf-8 -*- 

"""
*--------------------------- DialogAddMeta.py -------------------------------*
DialogAddMeta 用于添加 HDF5 文件中 Group 或者 Dataset 的元数据/属性 attrs。

需要注意的是，该窗口支持对任意 key 进行任意三种数据类型 (int, float 和 str) 的添加。

作者：          胡一鸣
创建时间：      2023年3月24日

The DialogEditMeta is used to add the metadata/attributes (attrs) of a Group 
or Dataset in an HDF5 file.

It is important to note that this window supports adding of any key for any of 
the three data types (int, float, and str). 

author:        Hu Yiming
date:          Mar 24, 2024
*--------------------------- DialogAddMeta.py -------------------------------*
"""

from logging import Logger 

from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QMessageBox  
from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtCore import QObject 
import numpy as np

from bin.MetaManager import MetaManager 
from bin.MetaManager import MetaTree 
from bin.MetaManager import MetaTreeModel 
from bin.HDFManager import HDFHandler
from bin.UIManager import ThemeHandler
from bin.Widgets.DialogEditMeta import DialogTypeSelection

from ui import uiDialogEditMeta

class DialogAddMeta(QDialog):
    """
    Dialog to edit attrs of items in the HDF5 file.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogEditMeta.Ui_Dialog()
        self.ui.setupUi(self)
        
        # self._meta_manager = None 
        self._initAddDialog()

    @property 
    def meta_manager(self) -> MetaManager:
        global qApp 
        return qApp.requireMetaManager(self.item_path)
    
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
    
    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger
    
    def _initAddDialog(self):
        """
        Initialize the edit metadata dialog.
        """
        self.setWindowTitle("Add Metadata")
        self.ui.lineEdit_item_path.setReadOnly(True)
        self.ui.lineEdit_meta_key.textChanged.connect(self._onMetaKeyChanged)
        self.ui.lineEdit_meta_key.editingFinished.connect(self.readMetaFromFile)
        self.ui.pushButton_browse_item_path.setVisible(False)
        self.ui.pushButton_browse_item_path.setEnabled(False)
        self.ui.pushButton_browse_meta_key.setVisible(False)
        self.ui.pushButton_browse_meta_key.setEnabled(False)
        self.ui.pushButton_ok.clicked.connect(self._slotOkClicked)
        self.ui.pushButton_cancel.clicked.connect(self._slotCancelClicked)
        self.ui.pushButton_change_dtype.clicked.connect(self._slotChangeDtypeClicked)
        self.ui.stackedWidget_set_value.setCurrentIndex(0)
        self.ui.plainTextEdit_note.setReadOnly(True)
        self.ui.label_unit_float.setVisible(False)
        self.ui.label_unit_float_hint.setVisible(False)
        self.ui.label_unit_int.setVisible(False)
        self.ui.label_unit_int_hint.setVisible(False)
        

    def _onMetaKeyChanged(self):
        """
        If the user is editing meta key, this function will be called.
        """
        pass 

    def _slotOkClicked(self):
        """
        Slot of OK button clicked. Save the edited metadata to HDF5 file.
        """
        item_path = self.item_path 
        meta_key = self.meta_key
        # if self.meta_manager is not None:
        if meta_key in self.meta_manager.listSchemaKeys():
            msg_box_ask = QMessageBox(self)
            msg_box_ask.setWindowTitle("Metadata Modification Warning")
            msg_box_ask.setIcon(QMessageBox.Warning)
            msg_box_ask.setText(f"Modifying this metadata may affect how the software works.")
            msg_box_ask.setInformativeText(
                f"<code>{meta_key}</code> is a predefined metadata item that may have actual physical meaning or be involved in the computation. Please double check before making any changes."
            )
            msg_box_ask.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            msg_box_ask.setDefaultButton(QMessageBox.Cancel)
            ret = msg_box_ask.exec()
            if ret == QMessageBox.Cancel:
                return 

        current_page_index = self.ui.stackedWidget_set_value.currentIndex()
        if current_page_index == 0:     # Integer
            meta_value = self.ui.spinBox_edit_integer.value()
        elif current_page_index == 1:   # Float
            decimal_part = self.ui.doubleSpinBox_float_decimal.value()
            exp_part = self.ui.spinBox_float_exp.value()
            meta_value = decimal_part * (10 ** exp_part)
        else:                           # String
            meta_value = self.ui.plainTextEdit_edit_string.toPlainText()

        if meta_key in self.hdf_handler.file[item_path].attrs:
            ret = QMessageBox.information(self, 'Info', f'There has been an existing metadata: <code>{meta_key}</code>. Do you want to overwrite it?', buttons = QMessageBox.Ok|QMessageBox.Cancel)
            if ret == QMessageBox.Cancel:
                return 
            

        try:
            self.hdf_handler.file[item_path].attrs[meta_key] = meta_value 
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to save metadata: {str(e)}')
        else:
            QMessageBox.information(self, 'Success', 'Metadata saved successfully.')
            self.meta_manager.refreshModel()
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
        pages = {
            'Integer': 0,
            'Float': 1,
            'String': 2,
        }
        dialog = DialogTypeSelection(self)
        ret = dialog.exec()
        if ret == dialog.Accepted:
            self.ui.stackedWidget_set_value.setCurrentIndex(pages[dialog.chosen_type])
            self.ui.label_current_dtype.setText(dialog.chosen_type)
        return 
    
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
        if not meta_key:
            return 
        if meta_key in self.hdf_handler.file[item_path].attrs:
            self.logger.warning(
                f'Metadata key {meta_key} exists in {item_path}'
            )
            QMessageBox.warning(
                self,
                'Warning',
                f'Metadata key <code>{meta_key}</code> exists in <code>{item_path}</code>',
            )
            self._setExistMeta()
        else:
            self.ui.label_unit_int_hint.setVisible(False)
            self.ui.label_unit_int.setVisible(False)
            self.ui.label_unit_float_hint.setVisible(False)
            self.ui.label_unit_float.setVisible(False)
        

        
    def _setExistMeta(self):
        """
        If there exists metadata, use the same logic as DialogEditMeta.
        """
        item_path = self.item_path 
        meta_key = self.meta_key 
        meta_value = self.hdf_handler.file[item_path].attrs[meta_key]
        if isinstance(meta_value, (int, np.integer)):
            self.ui.stackedWidget_set_value.setCurrentIndex(0)
            self.ui.spinBox_edit_integer.setValue(meta_value)
            self.ui.label_current_dtype.setText('Integer')
            if meta_key in self.meta_manager.listSchemaKeys():
                if self.meta_manager.getSchemaUnit(meta_key) is not None:
                    self.ui.label_unit_int_hint.setVisible(True)
                    self.ui.label_unit_int.setVisible(True)
                    self.ui.label_unit_float_hint.setVisible(False)
                    self.ui.label_unit_float.setVisible(False)
                    self.ui.label_unit_int.setText(
                        self.meta_manager.getSchemaUnit(meta_key)
                    )
                else:
                    self.ui.label_unit_int_hint.setVisible(False)
                    self.ui.label_unit_int.setVisible(False)
                    self.ui.label_unit_float_hint.setVisible(False)
                    self.ui.label_unit_float.setVisible(False)


        elif isinstance(meta_value, (float, np.floating)):
            self.ui.stackedWidget_set_value.setCurrentIndex(1)
            decimal_part, exp_part = f'{meta_value:e}'.split('e')
            self.ui.doubleSpinBox_float_decimal.setValue(float(decimal_part))
            self.ui.spinBox_float_exp.setValue(int(exp_part))
            self.ui.label_current_dtype.setText('Float')
            if meta_key in self.meta_manager.listSchemaKeys():
                if self.meta_manager.getSchemaUnit(meta_key) is not None:
                    self.ui.label_unit_int_hint.setVisible(False)
                    self.ui.label_unit_int.setVisible(False)
                    self.ui.label_unit_float_hint.setVisible(True)
                    self.ui.label_unit_float.setVisible(True)
                    self.ui.label_unit_float.setText(
                        self.meta_manager.getSchemaUnit(meta_key)
                    )
                else:
                    self.ui.label_unit_int_hint.setVisible(False)
                    self.ui.label_unit_int.setVisible(False)
                    self.ui.label_unit_float_hint.setVisible(False)
                    self.ui.label_unit_float.setVisible(False)

        elif isinstance(meta_value, str):
            self.ui.stackedWidget_set_value.setCurrentIndex(2)
            self.ui.plainTextEdit_edit_string.setPlainText(meta_value)
            self.ui.label_current_dtype.setText('String')

            self.ui.label_unit_int_hint.setVisible(False)
            self.ui.label_unit_int.setVisible(False)
            self.ui.label_unit_float_hint.setVisible(False)
            self.ui.label_unit_float.setVisible(False)
        else:
            QMessageBox.warning(self, 'Warning', f'Unsupported data type: {type(meta_value)}')

        if meta_key in self.meta_manager.listSchemaKeys():
            self.ui.plainTextEdit_note.setPlainText(
                'This is a parameter whose physical meaning and default units have been predefined.\n\n'+self.meta_manager.getSchemaDescription(meta_key)
            )

    