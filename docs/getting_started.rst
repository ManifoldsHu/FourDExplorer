Getting Started
===============

Installation
------------

From Executable
^^^^^^^^^^^^^^^

From releases, we download packages according to the operating system. Currently, only Windows is available. For Linux, see Installation FourDExplorer from Source instead.

Next, unzip the downloaded packages, and execute 4D-Explorer.exe to open the software.

From PyPI
^^^^^^^^^

It is recommended to use Anaconda to set up the programming environment:

.. code-block:: bash

   conda update conda
   conda create -n FourDExplorer python==3.10
   conda activate FourDExplorer
   pip install --upgrade FourDExplorer

Then, run python

.. code-block:: bash

   python

Now, we import the FourDExplorer module and run the GUI:

.. code-block:: python

   >>> from FourDExplorer import FourDExplorer
   >>> FourDExplorer.run()

Test Data
---------

Test 4D-STEM data will be available soon. You can use 4D-Explorer to open any HDF5 file directly.