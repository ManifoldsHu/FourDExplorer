入门指南
========

安装
----

从可执行文件
^^^^^^^^^^^^

从发布页面，我们根据操作系统下载相应的包。目前仅支持 Windows。对于 Linux，请参阅从源代码安装。

接下来，解压缩下载的包，并执行 4D-Explorer.exe 以打开软件。

从 PyPI
^^^^^^^

建议使用 Anaconda 来设置编程环境：

.. code-block:: bash

   conda update conda
   conda create -n FourDExplorer python==3.10
   conda activate FourDExplorer
   pip install --upgrade FourDExplorer

然后，运行 python

.. code-block:: bash

   python

现在，我们导入 FourDExplorer 模块并运行 GUI：

.. code-block:: python

   >>> from FourDExplorer import FourDExplorer
   >>> FourDExplorer.run()

测试数据
--------

测试 4D-STEM 数据将很快可用。您可以使用 4D-Explorer 直接打开任何 HDF5 文件。