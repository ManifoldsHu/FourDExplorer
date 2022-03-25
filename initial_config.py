# -*- coding: utf-8 -*-

"""
This script is used to create a default configuration file.
"""

from configparser import ConfigParser
from Constants import CONFIG_PATH, ROOT_PATH, UITheme, LogLevel
import os
from bin.UIManager import ThemeHandler


if __name__ == '__main__':
    config = ConfigParser()

    config.read(CONFIG_PATH, encoding = 'UTF-8')

    if not 'UI' in config:
        config.add_section('UI')
    config['UI']['Theme'] = 'light_blue.xml'

    if not 'Log' in config:
        config.add_section('Log')
    config['Log']['path'] = os.path.join(ROOT_PATH, 'logs')
    config['Log']['cLevel'] = LogLevel.DEBUG.name
    config['Log']['fLevel'] = LogLevel.DEBUG.name
    config['Log']['wLevel'] = LogLevel.INFO.name

    


    with open(CONFIG_PATH, 'w', encoding = 'UTF-8') as f:
        config.write(f)


