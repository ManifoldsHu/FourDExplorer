# -*- coding: utf-8 -*- 

"""
DEPRECATED
"""

from logging import Logger 

from PySide6.QtWidgets import QDialog 
from PySide6.QtCore import QObject

from bin.MetaManager import MetaManager 
from bin.MetaManager import MetaTree 
from bin.MetaManager import MetaTreeModel 
from bin.HDFManager import HDFHandler
from bin.UIManager import ThemeHandler

from ui import uiDialogDeleteMeta 

class DialogDeleteMeta(QDialog):
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.ui = uiDialogDeleteMeta.Ui_Dialog()
        self.ui.setupUi(self)
        self.initUi()

    def initUi(self):
        self.ui.lineEdit_item_path.setEnabled(False)
        self.ui.lineEdit_meta_key.setEnabled(False)
        self.ui.plainTextEdit_note.setEnabled(False)
        self.ui.plainTextEdit_value.setEnabled(False)


    @property 
    def meta_manager(self) -> MetaManager:
        # return self._meta_manager 
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
