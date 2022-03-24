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
from Constants import ROOT_PATH, CONFIG_PATH

class LogUtil(object):
    '''
        对Logger进行封装。

        这个类里有三个 handler，分别是
            - file_handler      向文件输出
            - console_handler   向控制台(stdout)输出
            - widget_handler    向主界面中的Log窗口输出
    '''
    def __init__(self, name, cLevel = logging.INFO, fLevel = logging.INFO):
        '''
        arguments       type            description
        ----------------------------------------------------------------------
        name            str             Filename of the object creater, i.e. 
                                        __name__
            
        cLevel          int             Level of logging printed towards the
                                        console

        fLevel          int             Level of logging written towards the
                                        .log files
        -----------------------------------------------------------------------
        '''

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.name = name
        
        try:
            self.file_handler = logging.FileHandler(
                self.getLogPath(), 
                'a+', 
                encoding='utf-8',
            )
        except FileNotFoundError as e:
            self.initializeLogPath()
            self.file_handler = logging.FileHandler(
                self.getLogPath(),
                'a+',
                encoding = 'utf-8',
            )

        self.file_handler.setLevel(fLevel)

        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(cLevel)

        self.widget_handler = logging.StreamHandler(stream = LogStream())
        self.widget_handler.setLevel(cLevel)

        formatter = logging.Formatter(
            '%(asctime)s - %(filename)s -> %(funcName)s[line:%(lineno)d] - '
            '%(levelname)s: %(message)s'
        )
        
        widget_formatter = WidgetFormatter(
            '%(asctime)s - %(filename)s -> %(funcName)s[line:%(lineno)d] - '
            '%(levelname)s: %(message)s'
        )   # This formatter is used for the log widget in the main window.


        self.file_handler.setFormatter(formatter)
        self.console_handler.setFormatter(formatter)
        self.widget_handler.setFormatter(widget_formatter)

        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.widget_handler)


    def setCLevel(self, cLevel):
        '''
        Set the logging level of the console handler

        arguments           type            description
        ------------------------------------------------------------
        cLevel              int             level of console handler
        ------------------------------------------------------------
        '''
        if cLevel not in (
            logging.DEBUG,
            logging.INFO,
            logging.WARNING,
            logging.ERROR,
            logging.CRITICAL,
        ):
            raise RuntimeError('cLevel must be one of logging.DEBUG, \
            logging.INFO, logging.WARNING, logging.ERROR and logging.CRITICAL')
        else:
            self.console_handler.setLevel(cLevel)
            self.widget_handler.setLevel(cLevel)

    def setFLevel(self, fLevel):
        '''
        Set the logging level of the file handler

        arguments           type            description
        ------------------------------------------------------------
        fLevel              int             level of file handler
        ------------------------------------------------------------
        '''
        if fLevel not in (
            logging.DEBUG,
            logging.INFO,
            logging.WARNING,
            logging.ERROR,
            logging.CRITICAL,
        ):
            raise RuntimeError('fLevel must be one of logging.DEBUG, \
            logging.INFO, logging.WARNING, logging.ERROR and logging.CRITICAL')
        else:
            self.file_handler.setLevel(fLevel)

    def getLogPath(self) -> str:
        '''
        Returns the path of logging file.
        '''
        config = ConfigParser()
        try:
            config.read(CONFIG_PATH, encoding = 'UTF-8')
            log_path = config['Log']['path']
        except KeyError:
            self.initializeLogPath()
            config.read(CONFIG_PATH, encoding = 'UTF-8')
            log_path = config['Log']['path']
        finally:  
            date = time.strftime('%Y%m%d', time.localtime(time.time()))
            log_file_path = os.path.join(log_path, date + '.log')
            return log_file_path

    def setLogPath(self, path: str):
        '''
        Set the log path in the configuration file.
        '''
        config = ConfigParser()
        config.read(CONFIG_PATH, encoding = 'UTF-8')
        if not 'Log' in config:
            config.add_section('Log')
        config['Log']['path'] = path
        with open(CONFIG_PATH, 'w', encoding = 'UTF-8') as f:
            config.write(f)

    def initializeLogPath(self):
        '''
        If there is no valid log path, use default path instead.
        '''
        default_path = os.path.join(ROOT_PATH, 'logs')
        self.setLogPath(default_path)


class LogStream(QObject):
    """
    一个Logging流。用于主界面上显示Log。

    A stream of logging. Used to print logs in the MainWindow.
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
