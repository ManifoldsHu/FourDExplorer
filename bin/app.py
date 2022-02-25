# -*- coding: utf-8 -*-

"""

"""

from PySide6.QtWidgets import QApplication

from bin.HDFManager import HDFHandler
from bin.UIManager import ThemeHandler
from bin.Log import LogUtil

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
            HDF files.

        theme_handler: (ThemeHandler) read only property. Use theme_handler to 
            manage themes, colors of interfaces.
    """
    def __init__(self, argv):
        """
        arguments:
            argv: (list) usually be sys.argv
        """
        super().__init__(argv)
        self._hdf_handler = HDFHandler()
        self._theme_handler = ThemeHandler()

    @property
    def hdf_handler(self):
        return self._hdf_handler

    @property
    def theme_handler(self):
        return self._theme_handler
