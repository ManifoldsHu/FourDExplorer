# -*- coding: utf-8 -*-

'''
*------------------------ Log.py ------------------------*

具有可以打印日志的LogUtil类。

作者：          胡一鸣
创建时间：      2021年7月25日

Use LogUtil to print Log.

author:             Hu Yiming
date:               July 25, 2021

All rights reserved.


代码示例
Coding Example

from bin.Log import LogUtil
import traceback

logger = LogUtil(__name__)
logger.info('Write a log')
try:
    do something
    do something
    do something
except BaseException as e:      # Or any other exception
    logger.error('{0}\n{1}'.format(e, traceback.format_exc()))


*------------------------ Log.py ------------------------*
'''

import logging
import os.path
import time



class LogUtil(object):
    '''
        对Logger进行封装。
    '''
    def __init__(self, name, cLevel = logging.INFO, fLevel = logging.INFO):
        '''
            arguments       type            description
            ------------------------------------------------------------------
            name            str             Filename of the object creater, 
                                            i.e. __name__
            
            cLevel          int             Level of logging printed towards 
                                            the console

            fLevel          int             Level of logging written towards
                                            the .log files
            -------------------------------------------------------------------
            
        '''

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.name = name
        
        log_path = os.path.join(os.path.abspath('.'), 'logs')
        date = time.strftime('%Y%m%d', time.localtime(time.time()))
        log_file_name = os.path.join(log_path, date + '.log')
        self.file_handler = logging.FileHandler(log_file_name, 'a+', encoding='utf-8')
        self.file_handler.setLevel(fLevel)

        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(cLevel)

        formatter = logging.Formatter(
            '%(asctime)s - %(filename)s->%(funcName)s[line:%(lineno)d] - \
            %(levelname)s: %(message)s'
        )
        self.file_handler.setFormatter(formatter)
        self.console_handler.setFormatter(formatter)

        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)

    def debug(self, message):
        '''
        arguments           type            description
        -----------------------------------------------------
        message             str             log message
        -----------------------------------------------------
        '''
        self.logger.debug(message)

    def info(self, message):
        '''
        arguments           type            description
        -----------------------------------------------------
        message             str             log message
        -----------------------------------------------------
        '''
        self.logger.info(message)

    def warning(self, message):
        '''
        arguments           type            description
        -----------------------------------------------------
        message             str             log message
        -----------------------------------------------------
        '''
        self.logger.warning(message)

    def error(self, message):
        '''
        arguments           type            description
        -----------------------------------------------------
        message             str             log message
        -----------------------------------------------------
        '''
        self.logger.error(message)
    
    def critical(self, message):
        '''
        arguments           type            description
        -----------------------------------------------------
        message             str             log message
        -----------------------------------------------------
        '''
        self.logger.critical(message)

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
