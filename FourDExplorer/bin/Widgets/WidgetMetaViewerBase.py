# -*- coding: utf-8 -*-

"""
*------------------------ WidgetMetaViewerBase.py ----------------------------*
显示 Metadata 的模块。Metadata 由 HDF5 文件内数据集的属性决定。

对于 4D-Explorer 软件内置的各种数据集类型而言，其属性以类似于路径名的形式存储，而以树
状形式，分层进行展示：
- 其根节点下的一级树枝节点，每个树枝都存在一个 Tab，用以展示该树枝节点中子节点的数据
- 从二级节点开始，下级的节点都将以 TreeView 的形式，展示在相应的 Tab 中。

每个节点，具有相应预定义的类型、名称、说明、单位。它们作为视图，存储在 schema 目录中。

对于那些不存在于预定义的属性，但又以树状形式组织的，我们在最后一个 Tab 中放置它们。换
句话说，对于未知的属性，即使是一级树枝节点，只要不是预定义的，都在最后一个 Tab 中单独
以 TreeView 的形式放置，并且无法提供类型、名称、说明、单位 (毕竟，它们只能由软件内部
提供)。出现这种异常情况的原因，一般有几种：
    - 用户进行了预料之外的转换，例如把 4D-STEM 数据集的扩展名从 .4dstem 改为 .img，
      从而 4D-Explorer 无法正确识别该数据集，也无法正确展示其属性
    - 用户通过代码向某个数据集中插入了额外的属性项
    - 前版本不兼容的属性

在预定义的视图中，我们没有给出最基础的数据类型和尺寸信息。因此，第一个 Tab 中，原本用
于展示根节点直属属性项的地方，我们在这里添加一些其他信息，包括：
    - 数据集的数据类型 (如 float, int 等)
    - 数据集的尺寸 
    - 该数据集扩展名所对应的说明

作为例子，我们考虑某个 .4dstem 数据集，其属性包括：
    /General/title
    /General/original_name
    /AcquisitionInstrument/manufacturer
    /AcquisitionInstrument/accelerate_voltage   
    /AcquisitionInstrument/Camera/manufacturer
    /AcquisitionInstrument/Camera/pixel_size_i
    /Calibration/Space/du_i
    ...
    sample_name    # an attribute added by user, which is undefined in software
    /Sample/classification   # another attribute added by user, undefined

那么它应当以这样的形式展示。首先，它应当是一个 QTabView，然后其各个 Tab 分别为

    Tab0: General, 在 TreeView 中，分别给出 title 和 original_name 叶子节点，并添加
          dataset_size 和 dataset_dtype 的展示

    Tab1: AcquisitionInstrument, 在 TreeView 中，添加 manufacturer 和 
          accelerate_voltage 的叶子节点；添加 Camera 树枝节点，并在其下添加 
          manufacturer 以及 pixel_size_i 的叶子节点。

    Tab2: Calibration, 在 TreeView 中，添加 Space 树枝节点，并在其下添加 du_i 叶子节
          点

    Tab3: Undefined, 添加 sample_name 叶子节点；添加 Sample 树枝节点，并在其下添加 
          classification 叶子节点。由于软件不知道它表示的是什么，所以只展示值。

具体预定义的视图由 MetaManagers 中读取，其中不同的扩展名/数据集类型对应不同的预定义视
图。MetaManagers 可以列出所有的属性项，从而方便我们构造属性树。

作者：          胡一鸣
创建时间：      2023年11月17日





*------------------------ WidgetMetaViewerBase.py ----------------------------*
"""