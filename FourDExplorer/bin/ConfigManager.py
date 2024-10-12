# -*- coding: utf-8 -*- 

"""
*---------------------------- ConfigManager.py -------------------------------*
管理配置文件。当配置文件不存在时创建。

作者：          胡一鸣
创建日期：      2024年10月13日

Manage Configuration Files. Create one if not exists.

author:         Hu Yiming
date:           Oct 13, 2024
*---------------------------- ConfigManager.py -------------------------------*
"""

import os 
from configparser import ConfigParser

from PySide6.QtCore import QObject

from Constants import CONFIG_PATH, ROOT_PATH, LogLevel 


class ConfigManager(QObject):
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._config = ConfigParser()
        self._config.read(CONFIG_PATH, encoding = 'UTF-8')
        self.initConfig()
            
    def initConfig(self):
        """
        Create config file if not exist, fix config file if needed.
        """
        if not os.path.exists(CONFIG_PATH):
            self._config['UI'] = {
                'themecolor': 'DeepPurple',
                'thememode': 'Light',
                'themedensity': 'Normal'
            }
            self._config['Log'] = {
                'path': os.path.join(ROOT_PATH, 'logs'),
                'flevel': 'DEBUG',
                'clevel': 'DEBUG',
                'wlevel': 'INFO'
            }
            with open(CONFIG_PATH, 'w', encoding='UTF-8') as f:
                self._config.write(f)
        else:
            if not self._config.has_section('UI'):
                self._config.add_section('UI')
                self._config['UI'] = {
                    'themecolor': 'DeepPurple',
                    'thememode': 'Light',
                    'themedensity': 'Normal'
                }
            if not self._config.has_section('Log'):
                self._config.add_section('Log')
                self._config['Log'] = {
                    'path': os.path.join(ROOT_PATH, 'logs'),
                    'flevel': 'DEBUG',
                    'clevel': 'DEBUG',
                    'wlevel': 'INFO'
                }
            with open(CONFIG_PATH, 'w', encoding='UTF-8') as f:
                self._config.write(f)
        
    @property
    def config(self):
        return self._config