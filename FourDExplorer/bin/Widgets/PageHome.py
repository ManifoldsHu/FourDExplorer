# -*- coding: utf-8 -*-

"""
*------------------------------- PageHome.py ---------------------------------*
主页。

作者:           胡一鸣
创建日期:       2022年3月25日

The home page.

author:         Hu Yiming
date:           Mar 25, 2022
*------------------------------- PageHome.py ---------------------------------*
"""

from PySide6.QtWidgets import QWidget
from bin.TaskManager import TaskManager
from bin.HDFManager import HDFHandler

from bin.Actions.EditActions import ActionImportFourDSTEM 
from bin.Actions.EditActions import ActionImportImage
from bin.Actions.FileActions import ActionNewFile 
from bin.Actions.FileActions import ActionOpenFile 
from bin.Actions.DataActions import ActionOpenFourDSTEM
from bin.Actions.FourDSTEMActions import ActionAlign
from bin.Actions.FourDSTEMActions import ActionRotate 
from bin.Actions.FourDSTEMActions import ActionBackground

from ui import uiPageHome


class PageHome(QWidget):
    """
    主页。

    Ui 文件地址：ROOT_PATH/ui/uiPageHome.ui

    The home page.

    The path of the ui file: ROOT_PATH/ui.uiPageHome.ui
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageHome.Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle('Home')

        self.ui.pushButton_import_fourDSTEM.clicked.connect(
            self._importFourDSTEM
        )
        self.ui.pushButton_new_file.clicked.connect(
            self._newFile
        )
        self.ui.pushButton_open_file.clicked.connect(
            self._openFile
        )
        self.ui.pushButton_import_image.clicked.connect(
            self._importImage
        )
        self.ui.pushButton_diffraction_alignment.clicked.connect(
            self._diffractionAlignment
        )
        self.ui.pushButton_rotational_correction.clicked.connect(
            self._rotationalCorrection
        )
        self.ui.pushButton_open_fourDSTEM.clicked.connect(
            self._openFourDSTEM
        )
        
        self.ui.pushButton_import_image.setVisible(False)
        self.ui.pushButton_background_subtraction.setVisible(False)

        # Connect signals to update button states
        self.hdf_handler.file_opened.connect(self._onFileOpened)
        self.hdf_handler.file_closed.connect(self._onFileClosed)

        # Initialize button states
        self._updateButtonStates()

    @property
    def task_manager(self) -> TaskManager:
        global qApp
        return qApp.task_manager

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler

    def _updateButtonStates(self):
        is_file_opened = self.hdf_handler.isFileOpened()
        self.ui.pushButton_import_fourDSTEM.setEnabled(is_file_opened)
        self.ui.pushButton_import_image.setEnabled(is_file_opened)
        self.ui.pushButton_new_file.setEnabled(True)
        self.ui.pushButton_open_file.setEnabled(True)
        self.ui.pushButton_background_subtraction.setEnabled(is_file_opened)
        self.ui.pushButton_diffraction_alignment.setEnabled(is_file_opened)
        self.ui.pushButton_open_fourDSTEM.setEnabled(is_file_opened)
        self.ui.pushButton_rotational_correction.setEnabled(is_file_opened)

    def _onFileOpened(self):
        self._updateButtonStates()

    def _onFileClosed(self):
        self._updateButtonStates()

    def _newFile(self):
        self.new_file_action = ActionNewFile(self)
        self.new_file_action.trigger()

    def _openFile(self):
        self.open_file_action = ActionOpenFile(self)
        self.open_file_action.trigger()

    def _importImage(self):
        self.import_image_action = ActionImportImage(self)
        self.import_image_action.trigger()

    def _importFourDSTEM(self):
        self.import_action = ActionImportFourDSTEM(self)
        self.import_action.trigger()
        
    def _backgroundSubtraction(self):
        self.background_subtraction_action = ActionBackground(self)
        self.background_subtraction_action.trigger()

    def _diffractionAlignment(self):
        self.diffraction_alignment_action = ActionAlign(self)
        self.diffraction_alignment_action.trigger()

    def _openFourDSTEM(self):
        self.open_fourDSTEM_action = ActionOpenFourDSTEM(self)
        self.open_fourDSTEM_action.trigger()

    def _rotationalCorrection(self):
        self.rotational_correction_action = ActionRotate(self)
        self.rotational_correction_action.trigger()


