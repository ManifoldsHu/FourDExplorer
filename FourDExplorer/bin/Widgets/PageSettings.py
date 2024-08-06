# -*- coding: utf-8 -*-

"""
*----------------------------- PageSettings.py -------------------------------*
对软件进行设置的界面。

作者:           胡一鸣
创建日期:       2022年6月9日

The page to configure the 4D-Explorer.

author:         Hu Yiming
date:           Jun 9, 2022
*----------------------------- PageSettings.py -------------------------------*
"""

import os
from logging import Logger

from PySide6.QtWidgets import QWidget, QFileDialog

from bin.UIManager import ThemeHandler
from bin.Log import LogUtil
from Constants import ROOT_PATH, LogLevel
from ui import uiPageSettings

class PageSettings(QWidget):
    """
    对软件进行设置的界面。

    Ui 文件地址：ROOTPATH/ui/uiPageSettings.ui

    Widget to configure the software.

    The path of the ui file: ROOTPATH/ui/uiPageSettings.ui
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageSettings.Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle('Settings')

        self._initDisplay()
        self._initLog()

    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp
        return qApp.theme_handler 

    @property
    def log_util(self) -> LogUtil:
        global qApp
        return qApp.log_util

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    def _initDisplay(self):
        """
        Initialize the theme tab.
        """
        mode_index = self.ui.comboBox_theme_mode.findText(
            self.theme_handler.theme_mode.name
        )
        self.ui.comboBox_theme_mode.setCurrentIndex(mode_index)
        self.ui.comboBox_theme_mode.currentIndexChanged.connect(
            self._applyThemeMode
        )

        color_index = self.ui.comboBox_theme_color.findText(
            self.theme_handler.theme_color.name 
        )
        self.ui.comboBox_theme_color.setCurrentIndex(color_index)
        self.ui.comboBox_theme_color.currentIndexChanged.connect(
            self._applyThemeColor
        )
        
        _revers_map = {
            'VeryHuge': 'Very Huge',
            'VeryLarge': 'Very Large',
            'VerySmall': 'Very Small',
            'VeryTiny': 'Very Tiny',
        }
        _density = self.theme_handler.theme_density.name 
        if _density in _revers_map:
            _density = _revers_map[_density]
        
        density_index = self.ui.comboBox_theme_density.findText(_density)
        self.ui.comboBox_theme_density.setCurrentIndex(density_index)
        self.ui.comboBox_theme_density.currentIndexChanged.connect(
            self._applyThemeDensity
        )

    def _initLog(self):
        """
        Initialize the log tab.
        """
        flevel_index = self.ui.comboBox_level_file.findText(
            self.log_util.fLevel.name
        )
        self.ui.comboBox_level_file.setCurrentIndex(flevel_index)
        self.ui.comboBox_level_file.currentIndexChanged.connect(
            self._applyLogLevels
        )

        wlevel_index = self.ui.comboBox_level_window.findText(
            self.log_util.wLevel.name 
        )
        self.ui.comboBox_level_window.setCurrentIndex(wlevel_index)
        self.ui.comboBox_level_window.currentIndexChanged.connect(
            self._applyLogLevels
        )

        self.ui.lineEdit_log_file_folder.setText(
            self.log_util.log_dir_path
        )
        self.ui.lineEdit_log_file_folder.setReadOnly(True)
        self.ui.pushButton_browse.clicked.connect(self._browseLogPath)
        self.ui.pushButton_clear_log_file.clicked.connect(self._clearLogFile)
        self.ui.pushButton_use_default_path.clicked.connect(
            self._useDefaultLogPath
        )
        self.ui.pushButton_open_log_folder.clicked.connect(
            self._openLogFolder
        )


    def _applyThemeMode(self):
        """
        Apply the changes of the theme mode.
        """
        theme_mode = self.ui.comboBox_theme_mode.currentText()
        self.theme_handler.applyThemeMode(theme_mode)
        self.logger.info('Applying Theme Mode: {0}'.format(theme_mode))
    
    def _applyThemeColor(self):
        """
        Apply the changes of the theme color.
        """
        theme_color = self.ui.comboBox_theme_color.currentText()
        self.theme_handler.applyThemeColor(theme_color)
        self.logger.info('Applying Theme Color: {0}'.format(theme_color))

    def _applyThemeDensity(self):
        """
        Apply the changes of the theme density.
        """
        theme_density = self.ui.comboBox_theme_density.currentText()
        _map = {
            'Very Huge': 'VeryHuge',
            'Very Large': 'VeryLarge',
            'Very Small': 'VerySmall',
            'Very Tiny': 'VeryTiny',
        }
        if theme_density in _map:
            theme_density = _map[theme_density]
        self.theme_handler.applyThemeDensity(theme_density)
        self.logger.info('Applying Theme Density: {0}'.format(theme_density))

    def _applyLogLevels(self):
        """
        Apply the changes of the log levels.
        """
        wlevel = self.ui.comboBox_level_window.currentText()
        flevel = self.ui.comboBox_level_file.currentText()
        self.log_util.wLevel = LogLevel[wlevel]
        self.log_util.fLevel = LogLevel[flevel]

    def _browseLogPath(self):
        """
        Open a dialog to browse which folder to save log files.
        """
        _path = QFileDialog.getExistingDirectory(
            self, 
            'Open Directory',
            './',
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        if _path:
            self.ui.lineEdit_log_file_folder.setText(_path)
            self.log_util.log_dir_path = _path 
        
    def _clearLogFile(self):
        """
        Delete all of the logs in the log folder.
        """
        pass 

    def _openLogFolder(self):
        """
        Open the log folder in the file system.
        """
        return os.startfile(self.log_util.log_dir_path)

    def _useDefaultLogPath(self):
        """
        Use the default log path: ROOT_PATH/logs
        """
        _path = os.path.join(ROOT_PATH, 'logs')
        self.ui.lineEdit_log_file_folder.setText(_path)
        self.log_util.log_dir_path = _path 

    
