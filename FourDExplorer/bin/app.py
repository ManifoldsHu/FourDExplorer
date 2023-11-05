# -*- coding: utf-8 -*-

"""
*--------------------------------- app.py ------------------------------------*

App 对象。在整个 4D-Explorer 生命周期中，只能有一个 App 对象。

它是全局变量，其他单例都可以通过 App 对象取到，如
    - theme_handler
    - hdf_handler
    - task_manager

App 对象应当在程序开始时实例化。

作者:           胡一鸣
创建日期:       2022年2月26日

This module includes App class. In the whole life-time of 4D-Explorer, there
only exists ONE App object.

App object is a global variable, and other singleton can be gotten by App, e.g.
    - theme_handler
    - hdf_handler
    - task_manager

App object need to be instantiated when the program is started.

author:         Hu Yiming
date:           Feb 26, 2022

*--------------------------------- app.py ------------------------------------*
"""

from logging import Logger
from PySide6.QtWidgets import QApplication

class App(QApplication):
    """
    包含各种后台工作的对象，作为 QApplication 的子类。

    整个程序中只能有一个 App 对象，使用
    global qApp 
    来得到这个全局变量。

    Backend Instance, as subclass of QApplication.

    This is a singleton instance. Use 
    global qApp 
    to get its global pointer.

    attributes:
        hdf_handler: (HDFHandler) read only property. Use hdf_handler to manage
            HDF files. This is a singleton.

        theme_handler: (ThemeHandler) read only property. Use theme_handler to 
            manage themes, colors of interfaces. This is a singleton.

        task_manager: (TaskManager) read only property. Use task_manager to 
            submit tasks. This is a singleton.

        logger: (logging.Logger) read only property. Use logger to print logs.
            In 4D-Explorer I recommend to use this logger as a singleton.

        log_util: (LogUtil) read only property. Use log_util to manage loggers.

        main_window: (MainWindow) read only property. Get the instance of the 
            MainWindow object.

        tabWidget_view: (QTabWidget) read only property. Get the instance of 
            the tabWidget_view, to add new pages (for viewing images).

    signals:
        aboutToQuit: emits when the application is about to quit. Will call 
            cleanResources() method.
    """
    def __init__(self, argv):
        """
        arguments:
            argv: (list) usually be sys.argv
        """
        super().__init__(argv)
        self._main_window = None

    def startBackEnds(self):
        """
        This function must be called after QApplication is initialized.
        """
        from bin.HDFManager import HDFHandler
        from bin.UIManager import ThemeHandler
        from bin.TaskManager import TaskManager
        from bin.Log import LogUtil
        from bin.MetaManagers.UnitManager import UnitManager

        self._hdf_handler = HDFHandler(self)
        self._theme_handler = ThemeHandler(self)
        self._task_manager = TaskManager(self)
        self._log_util = LogUtil(self)
        self._unit_manager = UnitManager(self)

    @property
    def hdf_handler(self):
        return self._hdf_handler

    @property
    def theme_handler(self):
        return self._theme_handler

    @property
    def task_manager(self):
        return self._task_manager

    @property
    def logger(self) -> Logger:
        return self._log_util.logger

    @property
    def log_util(self):
        return self._log_util

    @property
    def main_window(self):
        return self._main_window
    
    @property
    def unit_manager(self):
        return self._unit_manager

    @main_window.setter
    def main_window(self, _main_window):
        if self._main_window is None:
            self._main_window = _main_window
        else:
            raise ValueError('There have been one main window!')

    # @property
    # def tabWidget_view(self) -> QTabWidget:
    #     return self._main_window.ui.tabWidget_view

    @property
    def tabview_manager(self):
        return self._main_window.tabview_manager

    def cleanResources(self):
        """
        To Clean up resources when the program exits.
        """
        self.hdf_handler.closeFile()
        self.task_manager.shutDown()

