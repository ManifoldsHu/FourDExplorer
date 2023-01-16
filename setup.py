#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command
from FourDExplorer.Constants import APP_VERSION

# Package meta-data.
NAME = 'FourDExplorer'
DESCRIPTION = 'Use 4D-Explorer to process and analyze 4D-STEM data.'
URL = 'https://github.com/ManifoldsHu/FourDExplorer'
EMAIL = 'FourDExplorer@gmail.com'
AUTHOR = 'Hu Yiming'
REQUIRES_PYTHON = '>=3.9.0'
VERSION = '.'.join([str(v) for v in APP_VERSION])

# What packages are required for this module to be executed?
REQUIRED = [
    'numpy >= 1.20, <= 1.23',
    'h5py >= 3.7, <= 3.8',
    'matplotlib >= 3.5, <= 3.6',
    'pyinstaller >= 5.4, <= 5.5',
    'psutil == 5.9',
    'pyside6 >= 6.2, <= 6.3',
    'qt-material == 2.12',
    'scikit-image >= 0.18, <= 0.19',
    'scipy >= 1.8, <= 1.9',
]

# What packages are optional?
EXTRAS = {
    # 'GPU enabling': ['cupy'],
}

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


# The setup function do the actual work.
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(
        exclude=[
        "test",
        "test*",
        "logs", 
        "*.log",
    ]),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='GPLv3',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Chemistry',
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)