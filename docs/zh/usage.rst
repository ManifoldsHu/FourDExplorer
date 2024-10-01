使用指南
========

数据操作
--------

4D-Explorer 基于 [HDF5](https://www.hdfgroup.org/solutions/hdf5)。要创建一个新的 HDF5 文件，找到 '文件' 菜单，并点击 '新建 HDF5 文件' 选项。然后，点击 '打开 HDF5 文件' 以打开之前创建的文件。

.. image:: ../images/create_new_file.png
   :alt: 创建新文件

初始化有三个组：

- 校准
- 重建
- 临时

这些组显示在左侧控制面板的 '文件' 页面上。在 HDF5 文件中，组类似于文件夹或目录，数据集类似于文件，它们可以像我们在操作系统中那样进行编辑。HDF5 文件中的所有组和数据集都将显示在这里。

.. image:: ../images/open_h5.png
   :alt: 打开 H5

右键点击其中一个组并打开上下文菜单。有以下选项可用：

- '新建' 创建子组或数据集
- '导入 4D-STEM 数据集' 将 4D-STEM 数据集导入该组。
- '移动/复制/重命名/删除' 编辑该组。
- '属性' 查看该组的属性。

.. image:: ../images/create_new_group_1.png
   :alt: 创建新组 1

.. image:: ../images/create_new_group_2.png
   :alt: 创建新组 2

您也可以根据需要创建、移动、复制、重命名或删除这些组，但请注意，可能无法撤销操作。

> 删除内容时要小心。