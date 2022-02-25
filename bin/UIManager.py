# -*- coding: utf-8 -*-

"""
*----------------------------- UIManager.py ----------------------------------*
管理 4D-Explorer 的主题、夜间模式、以及色彩表现。在这里采用了开源库 qt_material.

作者:           胡一鸣
创建日期:       2022年2月19日

Manage the theme of 4D-Explorer. Here we use an open source module qt_material.

author:         Hu Yiming
date:           Feb 19, 2022
*----------------------------- UIManager.py ----------------------------------*
"""

import traceback
from configparser import ConfigParser

from PySide6.QtCore import QObject

from qt_material import apply_stylesheet

from bin.Log import LogUtil
from Constants import CONFIG_PATH, UITheme



def UIThemeToFileName(theme: UITheme) -> str:
    """
    将 UITheme 枚举类转化为对应的皮肤的文件名。

    Converse UITheme type to file_name. file_name is a string like 
        'light_blue.xml'

    arguments:
        theme: (UITheme) The current theme applied to 4D-Explorer

    returns:
        (str) 
    """
    if not isinstance(theme, UITheme):
        raise TypeError('Argument theme must be of UITheme')
    file_name = theme.name + '.xml'
    return file_name


def NameToUITheme(name: str):
    '''
    将对应皮肤的文件名或者名字转化为 UITheme 枚举类。

    Converse file_name to a UITheme.

    arguments:
        name: (str) This is a string like 'light_blue.xml' or 'light_blue'

    returns:
        (UITheme)
    '''
    name = name.split('.')[0]
    return UITheme[name]




class ThemeHandler(QObject):
    """
    使用 ThemeHandler 管理 4D-Explorer 的皮肤。

    注意，这个类使用单例模式。在程序的任何地方要想取到这个实例，要先取到全局变量 qApp, 
    然后得到 qApp.hdf_handler 即可。

    调用 theme_handler.initializeTheme() 和 theme_handler.changeTheme() 来初始化
    或改变皮肤。


    Use ThemeHandler to manage the theme of 4D-Explorer. 
    
    NOTE: there is only SINGLE instance. Anywhere we need to get the pointer of
    this instance, use the global pointer qApp, and get qApp.hdf_handler. 

    We recommend to call theme_handler.innitializeTheme() and 
    theme_handler.changeTheme() to initialize or change themes.

    attributes:
        theme: (UITheme) The current theme applied to 4D-Explorer
    """

    def __init__(self):
        """
        Initialize object.
        """
        global qApp 
        self._app = qApp 
        self._config = ConfigParser()
        self._config.read(CONFIG_PATH, encoding = 'utf-8')
        self._logger = LogUtil(__name__)
        self._theme = UITheme.default


    def _applyTheme(self, theme: UITheme) -> bool:
        """
        arguments:
            theme: (UITheme)
        """
        try:
            if theme.name.split('_')[0] == 'light':
                apply_stylesheet(
                    self._app, 
                    theme = UIThemeToFileName(theme),
                    invert_secondary = True,    # It is recommended to use inv-
                                                # ert secondary color in light
                                                # theme.
                )
            
            else:
                apply_stylesheet(
                    self._app,
                    theme = UIThemeToFileName(theme),
                    invert_secondary = False,
                )
            self.theme = theme
            return True
        except BaseException as e:
            self._logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
            return False


    def _applyCurrentTheme(self):
        self._applyTheme(self.theme)


    def initializeTheme(self):
        """
        Read theme from the configure file and then set it as the current theme.
        """
        self.theme = self._readTheme()
        self._applyCurrentTheme()


    def changeTheme(self, theme: UITheme):
        """
        Change, apply and save the current theme.

        arguments:
            theme: (UITheme) the theme to be applied.
        """
        self._saveTheme(theme)
        self._applyCurrentTheme(self)


    def _saveTheme(self, theme = UITheme):
        """
        arguments:
            theme: (UITheme) the theme to be saved.
        """
        with open(CONFIG_PATH, 'w', encoding = 'UTF-8') as f:
            self._config['UI']['Theme'] = theme.name
            self._config.write(f)
            self.theme = theme


    def _readTheme(self) -> UITheme:
        """
        Read the theme from configuration file.

        returns:
            (UITheme)
        """
        try:
            theme_str = self._config['UI']['Theme']
        except BaseException as e:
            self._logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
        else:
            theme = NameToUITheme(theme_str)
            return theme


    @property
    def theme(self) -> UITheme:
        return self._theme


    @theme.setter
    def theme(self, theme: UITheme|str):
        """
        arguments:
            theme: (UITheme or str)
        """
        if isinstance(theme, UITheme):
            self._theme = theme
        elif isinstance(theme, str):
            self._theme = NameToUITheme(theme)
        else:
            raise TypeError('Argument theme must be of UITheme or a string')
