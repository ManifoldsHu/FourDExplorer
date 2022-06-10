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

from PySide6.QtCore import QObject, QSize, Qt
from PySide6.QtGui import QIcon, QPixmap
from qt_material import apply_stylesheet

# from bin.Log import LogUtil
from Constants import CONFIG_PATH
from Constants import ROOT_PATH
from Constants import UIThemeColor
from Constants import UIThemeMode
from Constants import UIThemeDensity
from ui.resources import icon_rc

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
        self.initTheme()

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
    def theme_density(self) -> UIThemeDensity:
        try:
            density = self.config['UI']['ThemeDensity']
            return UIThemeDensity[density]
        except Exception:
            return UIThemeDensity['default']
    
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

        self._applyTheme(self.theme_mode, theme_color, self.theme_density)

        config = self.config
        with open(CONFIG_PATH, 'w', encoding = 'UTF-8') as f:
            config['UI']['ThemeColor'] = theme_color.name 
            config.write(f)

    def applyThemeMode(self, theme_mode: str|UIThemeMode = None):
        """
        Applying theme mode.

        Will write the theme_mode into the configure file.

        arguments:
            theme_mode: (str or UIThemeMode) The available mode can be found
                in Constants.py
        """
        if theme_mode is None:
            theme_mode = UIThemeMode.default
        elif isinstance(theme_mode, str):
            theme_mode = UIThemeMode[theme_mode]
        
        self._applyTheme(theme_mode, self.theme_color, self.theme_density)

        config = self.config
        with open(CONFIG_PATH, 'w', encoding = 'UTF-8') as f:
            config['UI']['ThemeMode'] = theme_mode.name 
            config.write(f)

    def applyThemeDensity(self, theme_density: str|UIThemeDensity = None):
        """
        Applying theme density.

        Will write the theme_mode into the configure file.

        Density subsystem provides adaptive layout to components. Material 
        Design uses low-density space by default but offers high-density space 
        when it improves the user experience. Components with high density 
        enable users to process and take action against large amounts of 
        information in a more manageable way. List, tables, and long forms 
        are components that benefit from increased density.

        See also: https://material.io/develop/web/supporting/density

        arguments:
            theme_density: (str or UIThemeDensity) the available density can 
                be found in Constants.py
        """
        if theme_density is None:
            theme_density = UIThemeDensity.default 
        elif isinstance(theme_density, str):
            theme_density = UIThemeDensity[theme_density]
        
        self._applyTheme(self.theme_mode, self.theme_color, theme_density)

        config = self.config 
        with open(CONFIG_PATH, 'w', encoding = 'UTF-8') as f:
            config['UI']['ThemeDensity'] = theme_density.name 
            config.write(f)
    
    def _applyTheme(self, 
        theme_mode: UIThemeMode, 
        theme_color: UIThemeColor,
        theme_density: UIThemeDensity,
    ):
        """
        Applying theme mode and color.

        arguments:
            theme_mode: (UIThemeMode)

            theme_color: (UIThemeColor)

            theme_density: (UIThemeDensity)
        """
        extra = {'density_scale': str(theme_density.value)}
        xml_file = theme_color.name + '.xml'
        if theme_mode == UIThemeMode.Light:
            path = os.path.join(self.light_theme_path, xml_file)
            apply_stylesheet(
                self._app, 
                path, 
                invert_secondary = True, 
                extra=extra,
            )
        elif theme_mode == UIThemeMode.Dark:
            path = os.path.join(self.dark_theme_path, xml_file)
            apply_stylesheet(
                self._app, 
                path, 
                invert_secondary = False, 
                extra=extra,
            )
        elif theme_mode == UIThemeMode.Classical:
            self._app.setStyleSheet('')     # Not recommended
        

    def initTheme(self):
        """
        Initialize theme from the configure file.
        """
        # Check whether config file is valid.
        config = self.config
        if not 'UI' in self.config:
            config.add_section('UI')
        
        if not 'ThemeColor' in config['UI']:
            config['UI']['ThemeColor'] = UIThemeColor.default.name 

        if not 'ThemeMode' in config['UI']:
            config['UI']['ThemeMode'] = UIThemeMode.default.name 

        if not 'ThemeDensity' in config['UI']:
            config['UI']['ThemeDensity'] = UIThemeDensity.default.name 

        with open(CONFIG_PATH, 'w', encoding = 'UTF-8') as f:
            config.write(f)

        try:
            self._applyTheme(
                self.theme_mode, 
                self.theme_color,
                self.theme_density,
            )
        except Exception:
            self._applyTheme(
                UIThemeMode.default, 
                UIThemeColor.default,
                UIThemeDensity.default,
            )

        

    def iconProvider(self, icon_rc: str):
        """
        Get icons from resources.

        arguments:
            icon_rc: (str) like ':/HDFItem/icons/cube.png'

        returns:
            (QIcon)
        """
        if not isinstance(icon_rc, str):
            raise TypeError('icon_rc must be a str, not '
                '{0}'.format(type(icon_rc).__name__))

        icon_light_rc = icon_rc.rstrip('.png') + '_light.png'
        icon = QIcon()
        if self.theme_mode == UIThemeMode.Dark :
            icon.addFile(icon_rc, mode = QIcon.Selected)
            icon.addFile(icon_light_rc, mode = QIcon.Normal)
        else:
            icon.addFile(icon_rc, mode = QIcon.Normal)
            if self.getIconDarkness():
                icon.addFile(icon_light_rc, mode = QIcon.Selected)
            else:
                icon.addFile(icon_rc, mode = QIcon.Selected)
        return icon 

    def getIconDarkness(self) -> bool:
        """
        Get the color of icons should be displayed.

        Sometimes when an item is selected, the text need to be displayed as 
        white rather than black, in order to make itself visible. Icons, which 
        shows beside the text, should also change their darkness. 

        returns:
            (bool) whether icon should be white.
        """
        light = {
            UIThemeColor.Red: True,
            UIThemeColor.Pink: True,
            UIThemeColor.Purple: True,
            UIThemeColor.DeepPurple: True,
            UIThemeColor.Indigo: True,
            UIThemeColor.Blue: True,
            UIThemeColor.LightBlue: True,
            UIThemeColor.Cyan: True,
            UIThemeColor.Teal: True,
            UIThemeColor.Green: True,
            UIThemeColor.LightGreen: False,
            UIThemeColor.Lime: False,
            UIThemeColor.Yellow: False,
            UIThemeColor.Amber: False,
            UIThemeColor.Orange: False,
            UIThemeColor.DeepOrange: False,
            UIThemeColor.Brown: True,
            UIThemeColor.Gray: True,
            UIThemeColor.BlueGray: True,
        }
        if self.theme_mode == UIThemeMode.Classical:
            return False 
        elif self.theme_mode == UIThemeMode.Light:
            return light[self.theme_color]
        elif self.theme_mode == UIThemeMode.Dark:
            return False

