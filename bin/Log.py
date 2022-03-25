# -*- coding: utf-8 -*-

'''
*---------------------------------- Log.py -----------------------------------*

具有可以打印日志的LogUtil类。

作者：          胡一鸣
创建时间：      2021年7月25日

Use LogUtil to print Log.

author:             Hu Yiming
date:               July 25, 2021

All rights reserved.


代码示例
Coding Example

global qApp             # get the global QApplication object
logger = qApp.logger

logger.info('Write a log')
try:
    do something
    do something
    do something
except BaseException as e:      # Or any other exception
    logger.error('{0}'.format(e), exc_info = True)


*---------------------------------- Log.py -----------------------------------*
'''

import logging
import os.path
import time

from configparser import ConfigParser
from PySide6.QtCore import QObject, Signal
from Constants import ROOT_PATH, CONFIG_PATH, LogLevel

class LogUtil(QObject):
    """
    单例模式，对Logger进行封装。

    这个类里有三个 handler，分别是
        - file_handler      向文件输出
        - console_handler   向控制台(stdout)输出
        - widget_handler    向主界面中的Log窗口输出
    其中，widget_handler 在打印错误信息的时候禁用了 traceback。

    This is a logging manager to encapsulate loggers.

    There are three handlers:
        - file_handler      output to files
        - console_handler   output to stdio
        - widget_handler    output to the log widget in the MainWindow.
    Among them, widget_handler will not print traceback if an exception 
    occured.

    attributes:
        logger: (logging.Logger) use logger's functions to print logs.

        log_dir_path: (str) the directory of the log path

        path: (str) the log file path

        cLevel: (LogLevel) the log level of the console handler

        fLevel: (LogLevel) the log level of the file handler

        wLevel: (LogLevel) the log level of the widget handler

        stream: (LogStream) the log stream corresponding to the widget handler
    """

    def __init__(self, parent = None):
        """
        arguments:
            parent: (QObject)
        """
        super().__init__(parent)
        self._logger = logging.getLogger('4D-Explorer')
        self._logger.setLevel(logging.DEBUG)
        self._name = '4D-Explorer'

        self._formatter = logging.Formatter(
            '%(asctime)s - %(filename)s -> %(funcName)s[line:%(lineno)d] - '
            '%(levelname)s: %(message)s'
        )   # whole format, used in stdio and the file

        self._widget_formatter = WidgetFormatter(
            '%(asctime)s - %(levelname)s: %(message)s'
        )   # simplyfied format, used in the MainWindow

        self._config = ConfigParser()
        self._config_modified = True    # whether to read the config file

        self._initFileHandler()
        self._initConsoleHandler()
        self._initWidgetHandler()

    @property
    def log_dir_path(self) -> str:
        """
        The log directory path
        """
        if self._config_modified:
            self._config.read(CONFIG_PATH, encoding = 'utf-8')
            self._config_modified = False
        try:
            _path = self._config['Log']['path']
        except KeyError:
            self._useDefaultPath()
            self._config.read(CONFIG_PATH, encoding = 'utf-8')
            _path = self._config['Log']['path']
        finally:
            return _path


    @log_dir_path.setter
    def log_dir_path(self, _path: str):
        """
        Set the log directory path.

        Will also modify the path in the configuration file.

        arguments:
            _path: (str) must be a path of a directory.
        """
        if not isinstance(_path, str):
            raise TypeError('path must be a str, not '
                '{0}'.format(type(_path).__name__))

        self._config.read(CONFIG_PATH, encoding = 'utf-8')
        if not 'Log' in self._config:
            self._config.add_section('Log')
        self._config['Log']['path'] = _path
        with open(CONFIG_PATH, 'w', encoding = 'utf-8') as f:
            self._config.write(f)
        self._config_modified = True

    @property
    def path(self) -> str:
        """
        The log file path.

        The file name is the date of today.
        """
        date = time.strftime('%Y%m%d', time.localtime(time.time()))
        return os.path.join(self.log_dir_path, date + '.log')

    @property
    def cLevel(self) -> LogLevel:
        """
        The console level of logging.
        """
        return self._getLevel('cLevel')


    @cLevel.setter
    def cLevel(self, _cLevel: LogLevel):
        """
        Set the console logging level.

        Will also modify the cLevel in the configuration file.
        """
        self._setLevel('cLevel', _cLevel)
        self._console_handler.setLevel(_cLevel)

    @property
    def fLevel(self) -> LogLevel:
        """
        The file level of logging.
        """
        return self._getLevel('fLevel')

    @fLevel.setter
    def fLevel(self, _fLevel: LogLevel):
        """
        Set the file logging level.

        Will also modify the fLevel in the configuration file.
        """
        self._setLevel('fLevel', _fLevel)
        self._file_handler.setLevel(_fLevel)

    @property
    def wLevel(self) -> LogLevel:
        """
        The widget level of logging, shown in the MainWindow.
        """
        return self._getLevel('wLevel')

    @wLevel.setter
    def wLevel(self, _wLevel: LogLevel):
        """
        set the widget logging level.

        Will also modify the wLevel in the configuration file.
        """
        self._setLevel('wLevel', _wLevel)
        self._widget_handler.setLevel(_wLevel)

    def _getLevel(self, handler_level_name: str) -> LogLevel:
        """
        Get log level correspond to the handler.

        Will read from the configuration file.

        arguments:
            handler_level_name: (str) must be one of these
                'fLevel', 'cLevel' or 'wLevel'
        
        returns:
            (LogLevel)
        """
        if not isinstance(handler_level_name, str):
            raise TypeError('handler_level_name must be a str, not '
                '{0}'.format(type(handler_level_name).__name__))

        if not handler_level_name in ('fLevel', 'cLevel', 'wLevel'):
            raise ValueError('handler_level_name must be one of these: '
                'fLevel, cLevel or wLevel')
        
        if self._config_modified:
            self._config.read(CONFIG_PATH, encoding = 'utf-8')
            self._config_modified = False

        try:
            _level = self._config['Log'][handler_level_name]
        except KeyError:
            self._useDefaultLevel(handler_level_name)
            self._config.read(CONFIG_PATH, encoding = 'utf-8')
            _level = self._config['Log'][handler_level_name]
        finally:
            return LogLevel[_level]

    def _setLevel(self, handler_level_name: str, level: LogLevel):
        """
        Set the logging level.

        Will also modify the configuration file.

        arguments:
            handler_level_name: (str) must be one of these
                'fLevel'
                'cLevel'
                'wLevel'
            
            level: (LogLevel)
        """
        if not isinstance(handler_level_name, str):
            raise TypeError('handler_level_name must be a str, not '
                '{0}'.format(type(handler_level_name).__name__))

        if not handler_level_name in ('fLevel', 'cLevel', 'wLevel'):
            raise ValueError('handler_level_name must be one of these: '
                'fLevel, cLevel or wLevel')
        
        if not isinstance(level, int):
            raise TypeError('level must be LogLevel, or int. Not '
                '{0}'.format(type(level).__name__))
        
        self._config.read(CONFIG_PATH, encoding = 'utf-8')
        if not 'Log' in self._config:
            self._config.add_section('Log')
        if isinstance(level, LogLevel):
            self._config['Log'][handler_level_name] = level.name
        else:
            self._config['Log'][handler_level_name] = LogLevel(level).name
        
        with open(CONFIG_PATH, 'w', encoding = 'utf-8') as f:
            self._config.write(f)
        self._config_modified = True
    
    @property
    def logger(self) -> logging.Logger:
        return self._logger


    def _initFileHandler(self):
        """
        Initialize the file handler.

        The file handler will read the file path from the config file. If the
        path is invalid, it will use the default path (ROOTPATH/logs).

        Logs in the file have a whole format including:
            - datetime
            - filename (of the source)
            - funcName (of the function calling logging)
            - lineno (the line number of the calling logging)
            - levelname
            - message (exception value if there is an exception)
            - traceback (if there is an exception)
        """
        try:
            self._file_handler = logging.FileHandler(
                self.path,
                'a+',
                encoding = 'utf-8',
            )
        except FileNotFoundError:
            self._useDefaultPath()
            self._file_handler = logging.FileHandler(
                self.path,
                'a+',
                encoding = 'utf-8',
            )
        
        self._file_handler.setLevel(self.fLevel)
        self._file_handler.setFormatter(self._formatter)
        self._logger.addHandler(self._file_handler)

    def _initConsoleHandler(self):
        """
        Initialize the console handler.

        The console handler will output the logging into stdio. This is only
        used for debugging, because in releases there will be no consoles.

        Logs in the console have the whole format including:
            - datetime
            - filename (of the source)
            - funcName (of the function calling logging)
            - lineno (the line number of the calling logging)
            - levelname
            - message (exception value if there is an exception)
            - traceback (if there is an exception)
        """
        self._console_handler = logging.StreamHandler()
        self._console_handler.setLevel(self.cLevel)
        self._console_handler.setFormatter(self._formatter)
        self._logger.addHandler(self._console_handler)

    def _initWidgetHandler(self):
        """
        Initialize the widget handler.

        The widget handler will output the logging into the textBrowser in the 
        MainWindow. So the information will show to users.

        Logs in the widget have the simplified information including:
            - datetime
            - levelname
            - message (exception value if there is an exception)
        """
        self._widget_stream = LogStream(self)
        self._widget_handler = logging.StreamHandler(self._widget_stream)
        self._widget_handler.setLevel(self.wLevel)
        self._widget_handler.setFormatter(self._widget_formatter)
        self._logger.addHandler(self._widget_handler)

    def _useDefaultPath(self):
        """
        Use the default log path if no path availabe.
        """
        default_path = os.path.join(ROOT_PATH, 'logs')
        self.log_dir_path = default_path

    def _useDefaultLevel(self, handler_level_name: str):
        """
        Use the default log level if no level available.
        """
        if handler_level_name == 'cLevel':
            level = LogLevel.DEBUG
        elif handler_level_name == 'fLevel':
            level = LogLevel.DEBUG
        elif handler_level_name == 'wLevel':
            level = LogLevel.INFO
        else:
            level = LogLevel.INFO
        self._setLevel(handler_level_name, level)

    @property
    def stream(self) -> 'LogStream':
        return self._widget_handler.stream



class LogStream(QObject):
    """
    一个Logging流。用于主界面上显示Log。

    A stream of logging. Used to print logs in the MainWindow.

    signals:
        print_signal: emits whenever the logger need to log a message to the 
            widget handler.
    """
    print_signal = Signal(str)
    def __init__(self, parent: QObject = None):
        """
        arguments:
            parent: (QObject)
        """
        super().__init__(parent)
        
    
    def write(self, strings: str):
        self.print_signal.emit(strings)


class WidgetFormatter(logging.Formatter):
    """
    用于主界面的Log的格式。

    与文件以及标准输出中的格式相同，但在出现异常时，只打印异常类、异常值，而不打印traceback。

    Log formatter for the MainWindow Log Widget.

    It is the same as the file and stderr, but ignores traceback.
    """

    def format(self, record):
        record.exc_text = ''
        return super().format(record)

    def formatException(self, exc_info):
        return ''
