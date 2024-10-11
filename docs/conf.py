# -*- coding: utf-8 -*- 

"""
*-------------------------------- conf.py ------------------------------------*
Sphinx 文档构建的配置文件。

内置的配置项，请查阅：
https://www.sphinx-doc.org/en/master/usage/configuration.html

作者：          胡一鸣
创建时间：      2024年10月1日

Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see:
https://www.sphinx-doc.org/en/master/usage/configuration.html

author:         Hu Yiming
date:           Oct 1, 2024
*-------------------------------- conf.py ------------------------------------*
"""

import os 
import sys 
sys.path.insert(0, os.path.abspath('..'))

from FourDExplorer.Constants import APP_VERSION

# Project Information 
project = '4D-Explorer'
copyright = '2024, Hu Yiming'
author = 'Hu Yiming'

# The full version, including alpha/beta/rc tags
release = '.'.join(str(v) for v in (APP_VERSION))

# General consifgurations
extensions = [
    'sphinx.ext.autodoc', # automatically add documentation according to docstrings
    'sphinx.ext.viewcode', # add links to highlighted source code
    'sphinx.ext.todo', # manage todo items
    'sphinx.ext.imgmath', # render math as images
    'sphinx.ext.ifconfig', # conditionally include content based on config values
    'sphinx.ext.intersphinx', # link to other Sphinx documentation
    'sphinx.ext.napoleon', # support for NumPy and Google style docstrings
    'sphinx.ext.githubpages', # publish documentation to GitHub Pages
    'sphinx.ext.mathjax',   # mathjax
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static', 'fig']
html_favicon = 'fig/4D.png'
# html_logo = 'fig/4D.png'  # The color of icon is near to the background, looks odd

# Locale settings for internationalization
locale_dirs = ['locale/']  # Directory where translation files are stored
gettext_compact = False # Do not merge multiple .po files into one
gettext_uuid = True  # Enable UUID generation for better tracking of changes

