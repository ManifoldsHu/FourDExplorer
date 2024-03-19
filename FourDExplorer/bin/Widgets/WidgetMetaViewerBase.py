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

from PySide6.QtWidgets import QWidget 
from PySide6.QtWidgets import QToolBar
from PySide6.QtWidgets import QTreeView 
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QAction 
from PySide6.QtCore import Qt
from PySide6.QtCore import QObject
from PySide6.QtCore import QModelIndex

from bin.MetaManager import MetaManager 
from bin.MetaManager import MetaTree 
from bin.MetaManager import MetaTreeModel
from bin.HDFManager import HDFHandler
from bin.UIManager import ThemeHandler
from Constants import MetaDataRoles

from ui import uiWidgetMetaViewerBase

class WidgetMetaViewerBase(QWidget):
    """
    查看元数据的基类。

    The base widget to view metadata.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetMetaViewerBase.Ui_Form()
        self.ui.setupUi(self)
        self.search_toolbar = MetaToolBar(self)
        self.ui.verticalLayout.insertWidget(0, self.search_toolbar)
        # self._initMetaManager()
        self._initSearch()
        self._initRefresh()
        
        
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
        
    def _initMetaTreeView(self):
        """
        Initialize meta tree model.
        """
        self.ui.treeView_meta.setModel(self.meta_tree_model)

    def _initMetaManager(self, item_path: str):
        """
        Initialize the meta manager according to the path of the item.

        arguments:
            item_path: (str) the path of the dataset or group.
        """
        self._meta_manager = MetaManager(self)
        self._meta_manager.setItemPath(item_path)
        hdf_type = self._meta_manager.hdf_type
        self._meta_manager.initializeSchema(hdf_type)

    def initMetaViewer(self, item_path: str):
        """
        Initialize the meta viewer according to the path of the item.

        arguments:
            item_path: (str) the path of the dataset or group.
        """
        self._initMetaManager(item_path)
        self._initMetaTreeView()

    def _initRefresh(self):
        """
        Initialize refresh action.
        """
        self._action_refresh = ActionRefreshMetaModel(self.search_toolbar)
        self._action_refresh.setLinkedTreeView(self.ui.treeView_meta)
        self.search_toolbar.addAction(self._action_refresh)

    def _initSearch(self):
        """
        Initialize search lineEdita and action.
        """
        self._lineEdit_search = QLineEdit('', parent = self)
        self._action_search = ActionSearch(self.search_toolbar)
        self._action_search.setLinkedLineEdit(self._lineEdit_search)
        self._action_search.setLinkedTreeView(self.ui.treeView_meta)
        self._lineEdit_search.addAction(
            self._action_search, 
            QLineEdit.LeadingPosition
        )
        self.search_toolbar.addWidget(self._lineEdit_search)
 
    def _updateModel(self):
        """
        Update to the newest model when it is changed.
        """
        self._initMetaTreeView()
        self.ui.treeView_meta.expandToDepth(0)
        

    
class MetaToolBar(QToolBar):
    """
    The toolbar to search items in Meta tree.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setMovable(False)
        self.setFloatable(False)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        qss = self.theme_handler

    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler 
    
    def _update_style_sheet(self):
        """
        When theme is changed, the style sheet must be updated.
        """
        qss = self.theme_handler.getToolBarStyleSheet(self)
        self.setStyleSheet(qss)


class ActionViewMetaBase(QAction):
    """
    用于在 Meta Tree 中查看 Metadata 的 Action 的基类。

    The base action for viewing meta data in the meta tree.
    """
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self._item_path = ''
        self._icon_name = ''
        self._meta_key = ''
        self.theme_handler.theme_changed.connect(
            self._updateIcon
        )
        self.hdf_handler.file_opened.connect(
            lambda: self.setEnabled(True)
        )
        self.hdf_handler.file_closed.connect(
            lambda: self.setEnabled(False)
        )
        self._meta_manager = None 
        self._treeview = None 

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler 

    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp
        return qApp.theme_handler 

    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger

    @property
    def item_path(self) -> str:
        return self._item_path 
    
    @property
    def meta_key(self) -> str:
        return self._meta_key 
    
    @property
    def meta_manager(self) -> MetaManager:
        return self._meta_manager 
    
    @property
    def meta_tree_model(self) -> MetaTreeModel:
        return self.meta_manager.meta_tree_model
    
    @property
    def meta_index(self) -> QModelIndex:
        return self.meta_tree_model.indexFromKey()
    
    def initIconResources(self, icon_name: str):
        """
        Initialize the resouce of icons.

        argumemnts:
            icon_name: (str) the name of icon.
        """
        _path = ':/HDFEdit/resources/icons/' + icon_name 
        icon = self.theme_handler.iconProvider(_path)
        self._icon_name = icon_name 
        self.setIcon(icon)
    
    def setItemPath(self, item_path: str):
        """
        Set the item path that this meta viewer action will manage. 

        arguments:
            item_path: (str) The path of the dataset or group in the HDF5 file.
        """
        if not isinstance(item_path, str):
            raise TypeError(f'path must be a str, not {type(item_path).__name__}')
        self._item_path = item_path

    def setMetaKey(self, key: str):
        """
        Set the key of the metadata that this meta viewer action will manage.

        arguments:
            key: (str) The key of the metadata
        """
        if not isinstance(key, str):
            raise TypeError(f'path must be a str, not {type(key).__name__}')
        self._meta_key = key 

    def setMetaKeyFromIndex(self, index: QModelIndex):
        """
        Set the target key from its model index.

        arguments:
            index: (QModelIndex) The meta key of the index.
        """
        if not isinstance(index, QModelIndex):
            raise TypeError(f'index must be a QModelIndex, not {type(index).__name__}')
        _key = index.data(MetaDataRoles.KeyRole)
        if _key is not None:
            self._meta_key = _key 
        else:
            self._meta_key = ''

    def _updateIcon(self):
        """
        Will update the icon when the theme mode changes.
        """
        if self._icon_name:
            _path = ':/HDFEdit/resources/icons/' + self._icon_name
            icon = self.theme_handler.iconProvider(_path)
            self.setIcon(icon)

    def setLinkedTreeView(self, treeview: QTreeView):
        """
        Set the linked treeview, so that it can show the result.
        """
        if not isinstance(treeview, QTreeView):
            raise TypeError('treeview must be a QTreeView, not '
                '{0}'.format(type(treeview).__name__))
        elif not isinstance(treeview.model(), MetaTreeModel):
            raise TypeError(
                f'treeview must be a MetaTreeModel, not {type(treeview).__name__}')
        self._treeview = treeview 
        model: MetaTreeModel = treeview.model()
        if 'meta_manager' in model.__dir__():
            self._meta_manager = model.meta_manager


def failLogging(func):
    """
    Try to do something. If failed, log it.

    This is a decorator, used for these actions on-triggered functions.
    """
    def wrapper(self: ActionViewMetaBase, *args, **kw):
        try:
            func(*args, **kw)
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('An exception happened in '
                '{0}: {1}'.format(self.text(), e))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
    return wrapper 


class ActionRefreshMetaModel(ActionViewMetaBase):
    """
    用于刷新元数据列表的 Action

    Action to refresh metadata tree.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Refresh')
        self.initIconResources('refresh.png')
        self.triggered.connect(lambda: self.refreshModel(self))

    @failLogging
    def refreshModel(self):
        """
        Will rebuild the Meta tree and then create a new model.

        We first get the current chosen key. Then we rebuild the meta manager 
        and the meta tree model. Finally, we set the chosen index of the tree 
        view to the chosen key before.
        """
        if self._treeview is not None:
            self.setMetaKeyFromIndex(self._treeview.currentIndex())
            self._meta_manager.setItemPath(self._item_path)
            self._treeview.setModel(self._meta_manager.meta_tree_model)
            _index = self.meta_tree_model.indexFromKey(self.meta_key)
            self._treeview.setCurrentIndex(_index)

class ActionSearch(ActionViewMetaBase):
    """
    用于查找下一个匹配的 Metadata 的 Action。

    Action to search Metadata.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Search')
        self.initIconResources('search.png')
        self.triggered.connect(self.searchItem)
        self._last_kw = ''
        self._result_generator = None 

    def setLinkedTreeView(self, treeview: QTreeView):
        """
        Set the linked treeview, such that it can show the result.

        arguments:
            treeview: (QTreeView) 
        """        
        self._treeview = treeview 

    def setLinkedLineEdit(self, line_edit: QLineEdit):
        """
        Set the linked line edit, such that it can get the word to search.
        """
        self._line_edit = line_edit 

    def searchItem(self):
        """
        Find the next rearch result and show it in the treeview.
        """
        kw = self._line_edit.text()
        if kw == '':
            return False 
        if kw != self._last_kw:
            # When the user changes the key word, we need to rebuild 
            # the generator and search from the beggining of the tree.
            self._last_kw = kw 
            model: MetaTreeModel = self._treeview.model()
            self._result_generator = model.matchIndexGenerator(kw)
            # TODO
        if self._result_generator is None:
            return False 
        try:
            index = next(self._result_generator)
            self._treeview.setCurrentIndex(index)
            return True 
        except StopIteration:
            msg = QMessageBox()
            msg.setWindowTitle('Search')
            msg.setIcon(QMessageBox.Information)
            msg.setText('No more results.')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self._last_kw = ''
            return False 

