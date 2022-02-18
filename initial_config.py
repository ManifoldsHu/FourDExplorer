# -*- coding: utf-8 -*-

from configparser import ConfigParser
import os

if __name__ == '__main__':
    config = ConfigParser()
    ROOTPATH = os.path.dirname(os.path.abspath(__file__))
    cfg_path = os.path.join(ROOTPATH, '.config')
    config.read(cfg_path, encoding = 'UTF-8')

    config.add_section('UI')
    config.add_section('Log')

    config['UI']['mode'] = 'light'

    config['Log']['path_mode'] = 'Default'
    config['Log']['path'] = '.'

    # config.write(open(cfg_path, 'w'))
    with open(cfg_path, 'w', encoding = 'UTF-8') as f:
        config.write(f)
    

# config.add_section('')

