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

from configparser import ConfigParser
from logging import Logger
import os

from PySide6.QtCore import QObject, QSize
from PySide6.QtGui import QIcon 
from qt_material import apply_stylesheet

# from bin.Log import LogUtil
from Constants import CONFIG_PATH, ROOT_PATH, UIThemeColor, UIThemeMode
from ui.resources import icon_rc



# def UIThemeToFileName(theme: UITheme) -> str:
#     """
#     将 UITheme 枚举类转化为对应的皮肤的文件名。

#     Converse UITheme type to file_name. file_name is a string like 
#         'light_blue.xml'

#     arguments:
#         theme: (UITheme) The current theme applied to 4D-Explorer

#     returns:
#         (str) 
#     """
#     if not isinstance(theme, UITheme):
#         raise TypeError('Argument theme must be of UITheme')
#     file_name = theme.name + '.xml'
#     return file_name


# def NameToUITheme(name: str):
#     '''
#     将对应皮肤的文件名或者名字转化为 UITheme 枚举类。

#     Converse file_name to a UITheme.

#     arguments:
#         name: (str) This is a string like 'light_blue.xml' or 'light_blue'

#     returns:
#         (UITheme)
#     '''
#     name = name.split('.')[0]
#     return UITheme[name]




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

    def __init__(self, parent: QObject = None):
        """
        Initialize object.
        """
        super().__init__(parent)
        global qApp 
        self._app = qApp 
        self._theme_color = UIThemeColor.default

    @property
    def light_theme_path(self) -> str:
        return os.path.join(ROOT_PATH, 'ui', 'resources', 'themes', 'light')

    @property
    def dark_theme_path(self) -> str:
        return os.path.join(ROOT_PATH, 'ui', 'resources', 'themes', 'dark')

    @property
    def config(self) -> ConfigParser:
        _config = ConfigParser()
        _config.read(CONFIG_PATH, encoding = 'utf-8')
        return _config

    @property
    def theme_color(self) -> UIThemeColor:
        try:
            color = self.config['UI']['ThemeColor']
            return UIThemeColor[color]
        except Exception:
            return UIThemeColor['default']

    @property
    def theme_mode(self) -> UIThemeMode:
        try:
            mode = self.config['UI']['ThemeMode']
            return UIThemeMode[mode]
        except Exception:
            return UIThemeMode['default']
    
    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    def applyThemeColor(self, theme_color: str|UIThemeColor = None):
        """
        Applying the theme color.

        Will write the theme_color into the configure file.

        arguments:
            theme_color: (UIThemeColor or str) The available theme can be 
                found in Constants.py
        """
        if theme_color is None:
            theme_color = UIThemeColor.default
        elif isinstance(theme_color, str):
            theme_color = UIThemeColor[theme_color]

        self._applyTheme(self.theme_mode, theme_color)

        with open(CONFIG_PATH, 'w', encoding = 'UTF-8') as f:
            self.config['UI']['ThemeColor'] = theme_color.name 
            self.config.write(f)

    def applyThemeMode(self, theme_mode: str|UIThemeMode = None):
        """
        Applying theme mode.

        Will write the theme_mode into the configure file.

        arguments:
            theme_mode: (str | UIThemeMode) The available mode can be found
                in Constants.py
        """
        if theme_mode is None:
            theme_mode = UIThemeMode.default
        elif isinstance(theme_mode, str):
            theme_mode = UIThemeMode[theme_mode]
        
        self._applyTheme(theme_mode, self.theme_color)

        with open(CONFIG_PATH, 'w', encoding = 'UTF-8') as f:
            self.config['UI']['ThemeMode'] = theme_mode.name 
            self.config.write(f)
    
    def _applyTheme(self, theme_mode: UIThemeMode, theme_color: UIThemeColor):
        """
        Applying theme mode and color.

        arguments:
            theme_mode: (UIThemeMode)

            theme_color: (UIThemeColor)
        """
        xml_file = theme_color.name + '.xml'
        if theme_mode == UIThemeMode.Light:
            path = os.path.join(self.light_theme_path, xml_file)
            apply_stylesheet(self._app, path, invert_secondary = True)
        elif theme_mode == UIThemeMode.Dark:
            path = os.path.join(self.dark_theme_path, xml_file)
            apply_stylesheet(self._app, path, invert_secondary = False)
        elif theme_mode == UIThemeMode.Classical:
            self._app.setStyleSheet('')     # Not recommended
        

    def initTheme(self):
        """
        Initialize theme from the configure file.
        """
        try:
            self._applyTheme(self.theme_mode, self.theme_color)
        except Exception:
            self._applyTheme(UIThemeMode.default, UIThemeColor.default)
        

        

        
        
    # def _applyThemeColor(self, theme_color: UIThemeColor) -> bool:
    #     """
    #     arguments:
    #         theme: (UIThemeColor)
    #     """

    #     try:
    #         if theme.name.split('_')[0] == 'light':
    #             apply_stylesheet(
    #                 self._app, 
    #                 theme = UIThemeToFileName(theme),
    #                 invert_secondary = True,    # It is recommended to use inv-
    #                                             # ert secondary color in light
    #                                             # theme.
    #             )
            
    #         else:
    #             apply_stylesheet(
    #                 self._app,
    #                 theme = UIThemeToFileName(theme),
    #                 invert_secondary = False,
    #             )
    #         self.theme = theme
    #         return True
    #     except BaseException as e:
    #         # self._logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
    #         self.logger.error('{0}'.format(e), exc_info = True)
    #         return False


    # def _applyCurrentTheme(self):
    #     # self._applyTheme(self.theme)
    #     apply_stylesheet(self._app, os.path.join(ROOT_PATH, 'ui', 'resources', 'themes', 'indigo_light_400.xml'), invert_secondary=True)


    # def initializeTheme(self):
    #     """
    #     Read theme from the configure file and then set it as the current theme.
    #     """
    #     self.theme = self._readTheme()
    #     self._applyCurrentTheme()


    # def changeTheme(self, theme: UITheme):
    #     """
    #     Change, apply and save the current theme.

    #     arguments:
    #         theme: (UITheme) the theme to be applied.
    #     """
    #     self._saveTheme(theme)
    #     self._applyCurrentTheme(self)


    # def _saveTheme(self, theme = UITheme):
    #     """
    #     arguments:
    #         theme: (UITheme) the theme to be saved.
    #     """
    #     with open(CONFIG_PATH, 'w', encoding = 'UTF-8') as f:
    #         self._config['UI']['Theme'] = theme.name
    #         self._config.write(f)
    #         self.theme = theme


    # def _readTheme(self) -> UITheme:
    #     """
    #     Read the theme from configuration file.

    #     returns:
    #         (UITheme)
    #     """
    #     try:
    #         theme_str = self._config['UI']['Theme']
    #     except BaseException as e:
    #         # self._logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
    #         self.logger.error('{0}'.format(e), exc_info = True)
    #     else:
    #         theme = NameToUITheme(theme_str)
    #         return theme


    # @property
    # def theme(self) -> UITheme:
    #     return self._theme


    # @theme.setter
    # def theme(self, theme: UITheme|str):
    #     """
    #     arguments:
    #         theme: (UITheme or str)
    #     """
    #     if isinstance(theme, UITheme):
    #         self._theme = theme
    #     elif isinstance(theme, str):
    #         self._theme = NameToUITheme(theme)
    #     else:
    #         raise TypeError('Argument theme must be of UITheme or a string')

    def iconProvider(self, icon_rc: str):
        """
        Get icons from resources.
        """
        if not isinstance(icon_rc, str):
            raise TypeError('icon_rc must be a str, not '
                '{0}'.format(type(icon_rc).__name__))

        icon = QIcon()
        icon.addFile(icon_rc, QSize(), QIcon.Normal, QIcon.On)
        return icon 

