# -*- coding: utf-8 -*- 

"""

"""

from PySide6.QtWidgets import QDialog 
from PySide6.QtCore import QObject

from ui import uiDialogDeleteMeta 

class DialogDeleteMeta(QDialog):
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.ui = uiDialogDeleteMeta.Ui_Dialog()
        self.ui.setupUi(self)
