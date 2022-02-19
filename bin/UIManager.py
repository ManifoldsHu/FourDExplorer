# -*- coding: utf-8 -*-

'''
*----------------------------- UIManager.py ----------------------------------*
管理 4D-Explorer 的主题、夜间模式、以及色彩表现。在这里采用了开源库 qt_material.

作者:           胡一鸣
创建日期:       2022年2月19日

Manage the theme of 4D-Explorer. Here we use an open source module qt_material.

author:         Hu Yiming
date:           Feb 19, 2022
*----------------------------- UIManager.py ----------------------------------*
'''


from PySide6.QtWidgets import QApplication

from bin.Log import LogUtil
import traceback
import threading

from configparser import ConfigParser
from Constants import CONFIG_PATH, UITheme
from qt_material import apply_stylesheet


def UIThemeToFileName(theme: UITheme) -> str:
    '''
    将 UITheme 枚举类转化为对应的皮肤的文件名。

    Converse UITheme type to file_name. file_name is a string like 
        'light_blue.xml'

    attributes              type                description
    ---------------------------------------------------------------------------
    theme                   UITheme             The current theme applied to 
                                                4D-Explorer
    ---------------------------------------------------------------------------
    '''
    if not isinstance(theme, UITheme):
        raise TypeError('Argument theme must be of UITheme')
    file_name = theme.name + '.xml'
    return file_name


def NameToUITheme(name: str):
    '''
    将对应皮肤的文件名或者名字转化为 UITheme 枚举类。

    Converse file_name to a UITheme.

    attributes              type                description
    ---------------------------------------------------------------------------
    name                    str                 This is a string like
                                                'light_blue.xml'
                                                or
                                                'light_blue'
    ---------------------------------------------------------------------------
    '''
    name = name.split('.')[0]
    return UITheme[name]




class ThemeHandler(object):
    '''
    使用 ThemeHandler 管理 4D-Explorer 的皮肤。注意，这个类使用单例模式，如果已经有一
    个这个类的实例，那么再次创建该类的实例的时候就直接返回已有的那个实例。

    Use ThemeHandler to manage the theme of 4D-Explorer. NOTE: there is only S-
    INGLE instance. If there has been one instance of this class, the existing 
    instance will be returned. (Singleton class)

    attributes              type                description
    ---------------------------------------------------------------------------
    theme                   UITheme             The current theme applied to 
                                                4D-Explorer
    ---------------------------------------------------------------------------

    一般而言，外部可以调用 theme_handler.initializeTheme() 和 
    theme_handler.changeTheme() 来初始化或改变皮肤。

    We recommend to call theme_handler.innitializeTheme() and 
    theme_handler.changeTheme() to initialize or change themes.
    '''

    _instance = None    # existing instance
    _instance_lock = threading.Lock()

    def __new__(cls, app: QApplication):
        '''
        There is only one instance allowed to exist.
        '''
        with cls._instance_lock:
            if cls._instance is None:
                cls._instance = object.__new__(cls)
                cls._instance.__init__(app)
            return cls._instance


    def __init__(self, app: QApplication):
        '''
        arguments           type                description
        -----------------------------------------------------------------------
        app                 QApplication        The main application instance.
        -----------------------------------------------------------------------
        '''
        self._app = app
        self._config = ConfigParser()
        self._config.read(CONFIG_PATH, encoding = 'utf-8')
        self._logger = LogUtil(__name__)
        self._theme = UITheme.default


    def _applyTheme(self, theme: UITheme) -> bool:
        '''
        应用主题。

        arguments           type                description
        -----------------------------------------------------------------------
        theme               UITheme             The theme applied.
        -----------------------------------------------------------------------
        '''
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
        '''
        应用当前主题。
        '''
        self._applyTheme(self.theme)


    def initializeTheme(self):
        '''
        从配置文件中读取并设置为当前主题。

        Read theme from the configure file and then set it as the current theme.
        '''
        self.theme = self._readTheme()
        self._applyCurrentTheme()


    def changeTheme(self, theme: UITheme):
        '''
        更改、应用并保存新皮肤。

        Change, apply and save the current theme.

        arguments           type                description
        -----------------------------------------------------------------------
        theme               UITheme             The theme applied.
        -----------------------------------------------------------------------
        '''
        self._saveTheme(theme)
        self._applyCurrentTheme(self)


    def _saveTheme(self, theme = UITheme):
        '''
        arguments           type                description
        -----------------------------------------------------------------------
        theme               UITheme             The theme applied.
        -----------------------------------------------------------------------
        '''
        with open(CONFIG_PATH, 'w', encoding = 'UTF-8') as f:
            self._config['UI']['Theme'] = theme.name
            self._config.write(f)
            self.theme = theme


    def _readTheme(self) -> UITheme:
        '''
        从配置文件中读取应当采用的皮肤。

        Read the theme from configuration file.
        '''
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
    def theme(self, theme):
        '''
        arguments           type                description
        -----------------------------------------------------------------------
        theme               UITheme             The theme applied.
        -----------------------------------------------------------------------
        '''
        if isinstance(theme, UITheme):
            self._theme = theme
        elif isinstance(theme, str):
            self._theme = NameToUITheme(theme)
        else:
            raise TypeError('Argument theme must be of UITheme or a string')
