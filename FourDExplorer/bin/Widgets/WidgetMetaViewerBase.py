# -*- coding: utf-8 -*-

"""
*------------------------ WidgetMetaViewerBase.py ----------------------------*
WidgetMetaViewerBase 用于展示 HDF5 文件中数据集的元数据。该 Widget 以树状结构和标签
页形式组织元数据，方便用户查看和理解数据集结构。

层次结构展示：元数据按照路径名类似的键组织成树状结构。根节点下的一级节点对应不同的标签
页 (Tab)，每个标签页展示该分支下的子节点信息。

二级及以下节点展示：从二级节点开始，所有子节点都在对应标签页中的 QTreeView 中展示。每个元数据节点预定义了类型、名称、描述和单位，这些信息存储在 schema 目录中。

未预定义的属性处理：对于不在预定义属性中的项，即使是一级节点，也将在一个单独的“未定义”标签页中以 QTreeView 形式展示。这些属性可能由用户添加或由于版本不兼容等原因出现。

基本信息展示：预定义的视图不包括基础数据类型和尺寸信息。因此，第一个标签页（一般为 "General"）除了展示其下的属性外，还会显示数据集的数据类型、尺寸和对应扩展名的说明。

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
图。MetaManagers 可以列出所有预定义的属性项，从而方便我们构造预定义的属性树。如上所述，
不在预定义的属性树内的属性，会被归类到 Undefined 中。

对于各个属性，我们根据其类型，在 QTreeView 列的右边加入按钮以提供修改方式。此外，和 
HDFViewer 类似，我们提供刷新按钮以及搜索功能。

作者：          胡一鸣
创建时间：      2023年11月17日


WidgetMetaViewerBase is designed for displaying metadata from HDF5 file datase-
ts. This Widget organizes metadata in a hierarchical structure and tabbed layo-
ut, facilitating easy viewing and understanding of the dataset structure.

Hierarchical Structure Display: Metadata are organized into a tree-like struct-
ure based on path-like keys. Root-level nodes correspond to different tabs (Ta-
bs), with each tab displaying information about the children of that branch.

Display of Secondary and Lower-Level Nodes: Starting from the second level, all 
child nodes are displayed in a QTreeView within the corresponding tab. Each me-
tadata node is predefined with type, name, description, and unit, stored in the 
schema directory.

Handling of Undefined Attributes: Items not in the predefined properties, even 
if they are first-level nodes, are displayed in a separate “Undefined” tab usi-
ng QTreeView. These attributes might be added by users or arise due to version incompatibilities.

Basic Information Display: The predefined view doesn't include basic data type 
and size information. Thus, the first tab (usually "General") displays these a-
ttributes along with the dataset's data type, size, and an explanation corresp-
onding to the extension name.

For example, consider a .4dstem dataset with the following attributes:
- /General/title
- /General/original_name
- /AcquisitionInstrument/manufacturer
- /AcquisitionInstrument/accelerate_voltage
- /AcquisitionInstrument/Camera/manufacturer
- /AcquisitionInstrument/Camera/pixel_size_i
- /Calibration/Space/du_i
- ...
- sample_name               # an attribute added by user, undefined in software
- /Sample/classification    # another user-added, undefined attribute

The display would be organized as follows:

- Tab0: General, displaying `title` and `original_name` in TreeView, along with `dataset_size` and `dataset_dtype`.

- Tab1: AcquisitionInstrument, displaying `manufacturer` and `accelerate_voltage` 
  in TreeView; adding a Camera branch node with `manufacturer` and `pixel_size_i`.

- Tab2: Calibration, displaying a Space branch node with `du_i` in TreeView.

- Tab3: Undefined, displaying `sample_name`; adding a Sample branch node with 
`classification`. As the software cannot identify their meaning, only values are 
displayed.

The specific predefined views are loaded from MetaManagers, with different file 
extensions/dataset types corresponding to different predefined views. MetaMana-
gers can list all predefined attributes, facilitating the construction of the 
predefined attribute tree. Attributes not in the predefined tree are categorized 
into Undefined.

For each attribute, based on its type, buttons are added next to the QTreeView 
column to provide a method of modification. Additionally, similar to HDFViewer, 
refresh buttons and search functionality are provided.

author:         Hu Yiming
date:           Nov 17, 2023
*------------------------ WidgetMetaViewerBase.py ----------------------------*
"""

from logging import Logger 

from PySide6.QtWidgets import QWidget, QMessageBox, QToolBar, QLineEdit, QTreeView
from PySide6.QtGui import QAction 
from PySide6.QtCore import QObject, QModelIndex, Qt 

# from bin.MetaManager import MetaManagerFourDSTEM, MetaManagerImg, MetaManagerVec, MetaManagerBase
from bin.MetaManager import MetaManager, MetadataFieldBase, MetaRootNode, MetaTreeNode, IntField, FloatField, StringField, MetaTree, MetaTreeModel 
# from bin.MetaManagers.MetadataFields import IntField, FloatField, StringField
# from bin.MetaManagers.UnitManager import UnitManager
from bin.HDFManager import HDFHandler, ItemDataRoles
from bin.UIManager import ThemeHandler
from bin.Actions.MetaActions import ActionEditMeta

from ui import uiWidgetMetaViewerBase

class WidgetMetaViewerBase(QWidget):
    """
    查看元数据的基类。
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetMetaViewerBase.Ui_Form()
        self.ui.setupUi(self)
        
        # self._tabs = []
        self._meta_manager = None 
        
    @property
    def meta_manager(self) -> MetaManager:
        return self._meta_manager  
    
    @property
    def meta_tree(self) -> MetaTree:
        return self._meta_manager.meta_tree
    
    @property
    def meta_tree_model(self) -> MetaTreeModel:
        return self._meta_manager.meta_tree_model
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler
        
    def _initValueTreeView(self):
        # self._value_tree_view = QTreeView(self)
        # self._value_tree_view.setModel(self.value_tree_model)
        self.ui.treeView.setModel(self.meta_tree_model)

    def _initMetaManager(self, item_path: str):
        self._meta_manager = MetaManager(self)
        self._meta_manager.setItemPath(item_path)
        hdf_type = self._meta_manager.hdf_type
        self._meta_manager.initializeSchema(hdf_type)

    def initMetaViewer(self, item_path: str):
        self._initMetaManager(item_path)
        self._initValueTreeView()

 