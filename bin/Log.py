# -*- coding: utf-8 -*-

'''
*------------------- Log.py ------------------------*

具有可以打印日志的函数。

作者：          胡一鸣
创建时间：      2021年7月25日

Print Log.

author:             Hu Yiming
date:               July 25, 2021

All rights reserved.

*------------------- Log.py ------------------------*
'''

import logging
import os.path
import time
# logging.basicConfig(
#     level = logging.WARNING,
#     format = '{0:s} - {1:s}[line:{2:d}] - {3:s}: {4:s}'.format(
#         asctime,
#         filename,
#         lineno,
#         levelname,
#         message,
#     )
# )


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




# logging.basicConfig(
#     level = logging.WARNING,
#     format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
# )


# def LogToFile():
#     '''
    
#     '''
#     logger = logging.getLogger()
#     logger.setLevel(logging.WARNING)
#     rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
#     log_path = os.path.dirname(os.getcwd()) + '/logs/'
#     log_name = log_path + rq + '.log'
#     logfile = log_name
#     fh = logging.FileHandler(logfile, mode = 'w')
#     fh.setLevel(logging.DEBUG)
#     formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# def test():
#     return os.getcwd()

# if __name__ == '__main__':
#     logging.warning('this is a logging warning message')
    