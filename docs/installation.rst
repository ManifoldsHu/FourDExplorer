Installation Guide
==================

Executable File Installation
----------------------------

On the repository's **Release** page, download the compressed file containing the executable based on your operating system. Currently, only Windows and macOS are supported. If you are using Linux, please use the PyPI installation method. After downloading the compressed file, extract it and locate the ``4D-Explorer.exe`` file to run the application.

PyPI Installation
-----------------

It is recommended to use Anaconda to set up a Python virtual environment, with Python version 3.10 as required:

.. code-block:: bash

    conda update conda
    conda create -n FourDExplorerVenv python==3.10

After creating the virtual environment named ``FourDExplorerVenv``, activate the environment, and then install 4D-Explorer using pip:

.. code-block:: bash

    conda activate FourDExplorerVenv
    (FourDExplorerVenv) pip install --upgrade FourDExplorer

Once the installation is complete, launch Python, enter the interactive environment, and run the following commands to start the software:

.. code-block:: python

    (FourDExplorerVenv) python
    >>> from FourDExplorer import FourDExplorer
    >>> FourDExplorer.run()







