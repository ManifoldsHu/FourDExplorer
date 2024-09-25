# -*- coding: utf-8 -*-

"""
*------------------------- WidgetBaseHDFViewer.py ----------------------------*
对 HDF5 文件内部的层次结构进行显示的模块。

4D-Explorer 软件默认使用 HDF5 进行四维数据及其元数据的管理。其数据的组织方式类似于
Unix 目录。为此，我们使用 Qt 的 QTreeView 对这些四维数据进行管理。

这个 Widget 是用在主界面的，具有增删查改的功能。

作者：          胡一鸣
创建时间：      2022年2月18日

The Module to show HDF5 file structure.

4D-Explorer software use HDF5 to manage 4D-STEM data and its metadata. It looks
like Unix file system, so we use QTreeView to show the structures.

This widget is used in the main window, and hence have CRUD methods.

author:         Hu Yiming
date:           Feb 18, 2022
*------------------------- WidgetBaseHDFViewer.py ----------------------------*
"""

from logging import Logger

from PySide6.QtCore import Qt
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QMenu
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QActionGroup

from bin.Actions.DataActions import ActionOpenData
from bin.Actions.DataActions import ActionOpenDataAs
from bin.Actions.EditActions import ActionAttributes
from bin.Actions.EditActions import ActionImportFourDSTEM
from bin.Actions.EditActions import ActionImportImage
from bin.Actions.EditActions import ActionChangeHDFType
from bin.Actions.EditActions import ActionCopy
from bin.Actions.EditActions import ActionDelete
from bin.Actions.EditActions import ActionMove
from bin.Actions.EditActions import ActionNew
from bin.Actions.EditActions import ActionRename

from bin.Actions.FileActions import ActionCloseFile
from bin.Actions.FileActions import ActionNewFile
from bin.Actions.FileActions import ActionOpenFile

from bin.Actions.FourDSTEMActions import ActionAlign
from bin.Actions.FourDSTEMActions import ActionBackground
from bin.Actions.FourDSTEMActions import ActionCenterOfMass
from bin.Actions.FourDSTEMActions import ActionRotate
from bin.Actions.FourDSTEMActions import ActionVirtualImage
from bin.Actions.FourDSTEMActions import ActionPlotCTF
from bin.Actions.FourDSTEMActions import ActionEditParam

from bin.Actions.VectorFieldActions import ActionSubtractMeanVector
from bin.Actions.VectorFieldActions import ActionSubtractReferenceVector
from bin.Actions.VectorFieldActions import ActionRotateVector
from bin.Actions.VectorFieldActions import ActionFlipComponents
from bin.Actions.VectorFieldActions import ActionPotential
from bin.Actions.VectorFieldActions import ActionDivergence
from bin.Actions.VectorFieldActions import ActionCurl
from bin.Actions.VectorFieldActions import ActionSliceI
from bin.Actions.VectorFieldActions import ActionSliceJ

from bin.UIManager import ThemeHandler
from bin.Widgets.WidgetBaseHDFViewer import HDFToolBar
from bin.TabViewManager import TabViewManager
from bin.Widgets.WidgetBaseHDFViewer import WidgetBaseHDFViewer
from Constants import HDFType
from Constants import ItemDataRoles

class WidgetHDFViewer(WidgetBaseHDFViewer):
    """
    用于显示 HDF5 文件结构的基础组件，包含一个 QTreeView。 

    Widget to show HDF file structure, which includes a QTreeView.
    """
    def __init__(self, parent: QWidget = None):
        """
        arguments:
            parent: (QWidget) The parent widget e.g. a dialog.
        """
        super().__init__(parent)

        self.ui.treeView_HDF.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeView_HDF.customContextMenuRequested.connect(
            self.showContextMenu
        )

        
        self._initDataActions()
        self._initEditActions()
        self._initFileActions()
        self._initCalibrationActions()
        self._initReconstructionActions()
        self._initAnalysisActions()
        self._initVectorFieldActions()

        self.hdf_handler.file_closed.connect(
            self.refreshTreeView
        )
        
    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    @property
    def tabview_manager(self) -> TabViewManager:
        global qApp
        return qApp.tabview_manager

    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler

    @property
    def action_group_edit(self) -> QActionGroup:
        return self._action_group_edit 

    @property
    def action_group_open(self) -> QActionGroup:
        return self._action_group_open 

    @property
    def action_group_attr(self) -> QActionGroup:
        return self._action_group_attr 

    @property 
    def action_group_reconstruction(self) -> QActionGroup:
        return self._action_group_reconstruction

    @property
    def action_group_calibration(self) -> QActionGroup:
        return self._action_group_calibration

    @property
    def action_group_analysis(self) -> QActionGroup:
        return self._action_group_analysis

    @property
    def action_group_new(self) -> QActionGroup:
        return self._action_group_new

    @property
    def action_group_file(self) -> QActionGroup:
        return self._action_group_file

    @property
    def action_group_vector(self) -> QActionGroup:
        return self._action_group_vector

    def _initEditActions(self):
        """
        Initialize actions for editing items in HDF Tree.
        """
        self.edit_toolbar = HDFToolBar(self)
        self.ui.verticalLayout.addWidget(self.edit_toolbar)

        self._action_new = ActionNew(self)
        self._action_import_fourdstem = ActionImportFourDSTEM(self)
        self._action_import_image = ActionImportImage(self)
        self._action_group_new = QActionGroup(self)
        self._action_group_new.addAction(self._action_new)
        self._action_group_new.addAction(self._action_import_fourdstem)
        self._action_group_new.addAction(self._action_import_image)
        for action in self._action_group_new.actions():
            action.setLinkedTreeView(self.ui.treeView_HDF)
            
        self._action_move = ActionMove(self)
        self._action_copy = ActionCopy(self)
        self._action_delete = ActionDelete(self)
        self._action_rename = ActionRename(self)
        self._action_attributes = ActionAttributes(self)
        self._action_group_edit = QActionGroup(self)
        self._action_group_edit.addAction(self._action_move)
        self._action_group_edit.addAction(self._action_copy)
        self._action_group_edit.addAction(self._action_delete)
        self._action_group_edit.addAction(self._action_rename)
        for action in self._action_group_edit.actions():
            action.setLinkedTreeView(self.ui.treeView_HDF)
            self.edit_toolbar.addAction(action)
        
        self._action_group_attr = QActionGroup(self)
        self._action_group_attr.addAction(self._action_attributes)
        self._action_attributes.setLinkedTreeView(self.ui.treeView_HDF)
        
        

    def _initDataActions(self):
        """
        Initialize the open data actions.
        """
        self._action_change = ActionChangeHDFType(self)
        self._action_open_data = ActionOpenData(self)
        self._action_open_data_as = ActionOpenDataAs(self)

        self._action_group_open = QActionGroup(self)
        self._action_group_open.addAction(self._action_open_data)
        self._action_group_open.addAction(self._action_open_data_as)
        self._action_group_open.addAction(self._action_change)

        for action in self._action_group_open.actions():
            action.setLinkedTreeView(self.ui.treeView_HDF)
        
    def _initReconstructionActions(self):
        """
        Initialize 4D-STEM reconstruction actions.
        """
        self._action_virtual_image = ActionVirtualImage(self)
        self._action_center_of_mass = ActionCenterOfMass(self)

        self._action_group_reconstruction = QActionGroup(self)
        self._action_group_reconstruction.addAction(
            self._action_virtual_image
        )
        self._action_group_reconstruction.addAction(
            self._action_center_of_mass
        )

        for action in self._action_group_reconstruction.actions():
            action.setLinkedTreeView(self.ui.treeView_HDF)

    def _initCalibrationActions(self):
        """
        Initialize 4D-STEM calibration actions.
        """
        self._action_edit_param = ActionEditParam(self)
        self._action_background = ActionBackground(self)
        self._action_alignment = ActionAlign(self)
        self._action_rotate = ActionRotate(self)
        
        self._action_group_calibration = QActionGroup(self)
        self._action_group_calibration.addAction(
            self._action_edit_param
        )
        self._action_group_calibration.addAction(
            self._action_background
        )
        self._action_group_calibration.addAction(
            self._action_alignment 
        )
        self._action_group_calibration.addAction(
            self._action_rotate
        )

        for action in self._action_group_calibration.actions():
            action.setLinkedTreeView(self.ui.treeView_HDF)

    def _initAnalysisActions(self):
        """
        Initialize 4D-STEM Analysis actions.
        """
        self._action_plot_ctf = ActionPlotCTF(self)
        self._action_group_analysis = QActionGroup(self)
        self._action_group_analysis.addAction(self._action_plot_ctf)
        
        for action in self._action_group_analysis.actions():
            action.setLinkedTreeView(self.ui.treeView_HDF)

    def _initFileActions(self):
        """
        Initialize File actions.
        """
        self._action_new_file = ActionNewFile(self)
        self._action_new_file.setText('New HDF5 File...')
        self._action_open_file = ActionOpenFile(self)
        self._action_open_file.setText('Open HDF5 File...')
        self._action_close_file = ActionCloseFile(self)
        self._action_close_file.setText('Close HDF5 File')
        
        self._action_group_file = QActionGroup(self)
        self._action_group_file.addAction(self._action_new_file)
        self._action_group_file.addAction(self._action_open_file)
        self._action_group_file.addAction(self._action_close_file)

    def _initVectorFieldActions(self):
        """
        Initialize Vector Field Processing Actions.
        """
        self._action_subtract_mean_vector = ActionSubtractMeanVector(self)
        self._action_rotate_vector = ActionRotateVector(self)
        self._action_flip_vector = ActionFlipComponents(self)
        self._action_subtract_reference_vector = ActionSubtractReferenceVector(self)
        self._action_potential = ActionPotential(self)
        self._action_divergence = ActionDivergence(self)
        self._action_curl = ActionCurl(self)
        self._action_slice_i = ActionSliceI(self)
        self._action_slice_j = ActionSliceJ(self)

        self._action_group_vector = QActionGroup(self)
        self._action_group_vector.addAction(
            self._action_subtract_mean_vector
        )
        self._action_group_vector.addAction(
            self._action_subtract_reference_vector
        )
        self._action_group_vector.addAction(
            self._action_rotate_vector
        )
        self._action_group_vector.addAction(
            self._action_flip_vector
        )
        self._action_group_vector.addAction(
            self._action_potential
        )
        self._action_group_vector.addAction(
            self._action_divergence
        )
        self._action_group_vector.addAction(
            self._action_curl
        )
        self._action_group_vector.addAction(
            self._action_slice_i
        )
        self._action_group_vector.addAction(
            self._action_slice_j
        )

        for action in self._action_group_vector.actions():
            action.setLinkedTreeView(self.ui.treeView_HDF)

    def refreshTreeView(self):
        """
        Refresh the treeview of HDF file.
        """
        self.hdf_handler.buildHDFTree()
        self.ui.treeView_HDF.setModel(self.hdf_handler.model)

    def showContextMenu(self, pos: QPoint):
        """
        在 HDF5 树中显示鼠标右键菜单。

        Show Context Menu in the treeview of HDF5.

        attributes:
            pos: (QPoint) the position where the mouse is clicked.
        """
        if self.hdf_handler.isFileOpened():
            index = self.ui.treeView_HDF.currentIndex()
            chosen_type = index.data(
                role = ItemDataRoles.HDFTypeRole
            )
            _type_to_menu = {
                HDFType.Root: HDFRootMenu, 
                HDFType.Group: HDFGroupMenu,
                HDFType.FourDSTEM: HDFFourDSTEMMenu,
                HDFType.Image: HDFImageMenu,
                HDFType.VectorField: HDFVectorFieldMenu,
                HDFType.Line: HDFLineMenu,
                HDFType.Data: HDFDataMenu,
            }
            if chosen_type in _type_to_menu:
                menu = _type_to_menu[chosen_type](self)
            else:
                menu = HDFItemMenu(self)
        else:
            menu = HDFViewerFileMenu(self)
        menu.exec(self.ui.treeView_HDF.mapToGlobal(pos))


class HDFViewerMenuBase(QMenu):
    """
    当点到 HDFTreeView 时的鼠标右键菜单。

    允许对 Item 进行修改操作。在使用时请根据取到的 QModelIndex 选择其合适的子类。

    The context menu of HDF tree view.

    Allowing modification operations of items. Use its subclass according to
    the current QModelIndex.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self._action_groups = []
        self._hdf_viewer = None 

    @property
    def hdf_viewer(self) -> WidgetHDFViewer:
        return self._hdf_viewer
        
    def addActionGroup(self, group: QActionGroup, separator: bool = True):
        """
        Add all of the actions in the group to the menu.

        If separator is True, it will also add a separator automatically 
        between two groups.

        arguments:
            group: (QActionGroup) 

            separator: (bool)
        """
        if len(self._action_groups) > 0 and separator:
            self.addSeparator() 
        self._action_groups.append(group)
        self.addActions(group.actions())

    def addActionGroupAsSubMenu(self, group: QActionGroup, name: str) -> QMenu:
        """
        Add all of the actions to a submenu.

        arguments:
            group: (QActionGroup)

            name: (str) the name of the submenu.

        returns:
            (QMenu) the added submenu.
        """
        submenu = self.addMenu(name)
        submenu.addActions(group.actions())
        return submenu

    def setLinkedHDFViewer(self, viewer: WidgetHDFViewer):
        """
        Set the HDFViewer of the menu.

        arguments:
            viewer: (WidgetHDFViewer)
        """
        self._hdf_viewer = viewer 

    
class HDFViewerFileMenu(HDFViewerMenuBase):
    """
    没有打开文件的时候对应的 Menu。

    When there is no file opened, the viewer will show this menu.
    """
    def __init__(self, parent: WidgetBaseHDFViewer):
        super().__init__(parent)
        self.setLinkedHDFViewer(parent)
        self.addActionGroup(self.hdf_viewer.action_group_file)

class HDFItemMenu(HDFViewerMenuBase):
    """
    一般的 Item 对应的 Menu。

    Menu for general items in HDF file.
    """
    def __init__(self, parent: WidgetHDFViewer):
        super().__init__(parent)
        self.setLinkedHDFViewer(parent)
        self.addActionGroup(self.hdf_viewer.action_group_edit)
        self.addActionGroup(self.hdf_viewer.action_group_attr)


class HDFRootMenu(HDFViewerMenuBase):
    """
    根目录的 Item 对应的 Menu。

    Menu for root.
    """
    def __init__(self, parent: WidgetHDFViewer):
        super().__init__(parent)
        self.setLinkedHDFViewer(parent)
        self.addActionGroup(self.hdf_viewer.action_group_file)
        self.addActionGroup(self.hdf_viewer.action_group_new)
        self.addActionGroup(self.hdf_viewer.action_group_attr)
        
    
class HDFGroupMenu(HDFViewerMenuBase):
    """
    一般的 Group 对应的 Menu。

    Menu for groups in HDF file.
    """
    def __init__(self, parent: WidgetHDFViewer):
        super().__init__(parent)
        self.setLinkedHDFViewer(parent)
        self.addActionGroup(self.hdf_viewer.action_group_new)
        self.addActionGroup(self.hdf_viewer.action_group_edit)
        self.addActionGroup(self.hdf_viewer.action_group_attr)


class HDFDataMenu(HDFViewerMenuBase):
    """
    一般的 Data 对应的 Menu。

    Menu for general Dataset in HDF file.
    """
    def __init__(self, parent: WidgetHDFViewer):
        super().__init__(parent)
        self.setLinkedHDFViewer(parent)
        self.addActionGroup(self.hdf_viewer.action_group_open)
        self.addActionGroup(self.hdf_viewer.action_group_edit)
        self.addActionGroup(self.hdf_viewer.action_group_attr)


class HDFLineMenu(HDFDataMenu):
    def __init__(self, parent: WidgetHDFViewer):
        super().__init__(parent)


class HDFImageMenu(HDFDataMenu):
    def __init__(self, parent: WidgetHDFViewer):
        super().__init__(parent)


class HDFVectorFieldMenu(HDFViewerMenuBase):
    def __init__(self, parent: WidgetHDFViewer):
        super().__init__(parent)
        self.setLinkedHDFViewer(parent)
        self.addActionGroup(self.hdf_viewer.action_group_open)
        self.addSeparator()
        menu = self.addActionGroupAsSubMenu(
            self.hdf_viewer.action_group_vector,
            name = 'Vector Field Processing',
        )
        menu.insertSeparator(self.hdf_viewer._action_potential)
        self.addActionGroup(self.hdf_viewer.action_group_edit)
        self.addActionGroup(self.hdf_viewer.action_group_attr)


class HDFFourDSTEMMenu(HDFViewerMenuBase):
    """
    4D-STEM 数据集所对应的 Menu。

    Menu for 4D-STEM dataset.
    """
    def __init__(self, parent: WidgetHDFViewer):
        super().__init__(parent)
        self.setLinkedHDFViewer(parent)
        self.addActionGroup(self.hdf_viewer.action_group_open)
        self.addSeparator()
        self.addActionGroupAsSubMenu(
            self.hdf_viewer.action_group_calibration, 
            name = 'Calibration',
        )
        self.addActionGroupAsSubMenu(
            self.hdf_viewer.action_group_reconstruction, 
            name = 'Reconstruction',
        )
        self.addActionGroupAsSubMenu(
            self.hdf_viewer.action_group_analysis, 
            name = 'Analysis',
        )
        self.addActionGroup(self.hdf_viewer.action_group_edit)
        self.addActionGroup(self.hdf_viewer.action_group_attr)
        

    


# class HDFBaseItemMenu(QMenu):
#     """
#     当点到 HDFTreeView 时的鼠标右键菜单。

#     允许对 Item 进行修改操作。在使用时请根据取到的 QModelIndex 选择其合适的子类。

#     The context menu of HDF tree view.

#     Allowing modification operations of items. Use its subclass according to
#     the current QModelIndex.
#     """
#     def __init__(
#         self, 
#         parent: QWidget = None, 
#         index: QModelIndex = QModelIndex(),
#     ):
#         if not isinstance(index, QModelIndex):
#             raise TypeError('index must be QModelIndex, not '
#                 '{0}'.format(type(index).__name__))
#         super().__init__(parent)
#         self._model_index = index

#         # self._action_create = ActionCreate(self, index)
#         # self._action_copy = ActionCopy(self, index)
#         # self._action_move = ActionMove(self, index)
#         # self._action_rename = ActionRename(self, index)
#         # self._action_delete = ActionDelete(self, index)
#         # self._action_attributes = ActionAttributes(self, index)
#         # self._action_change_data_type = ActionChangeDataType(self, index)
#         # self._action_show_data = ActionShowData(self, index)
#         # self._action_show_line = ActionShowLine(self, index)
#         # self._action_show_image = ActionShowImage(self, index)
#         # self._action_show_vector_field = ActionShowVectorField(self, index)
#         # self._action_show_fourdstem = ActionShowFourDSTEM(self, index)
#         # self._action_virtual_image = ActionVirtualImage(self, index)
#         # self._action_center_of_mass = ActionCenterOfMass(self, index)
#         # self._action_align = ActionAlign(self, index)
#         # self._action_bkgrd = ActionBkgrd(self, index)
#         # self._action_rotate = ActionRotate(self, index)
    
#     @property
#     def model_index(self) -> QModelIndex:
#         return self._model_index

# class HDFItemMenu(HDFBaseItemMenu):
#     """
#     一般的 HDF5 文件对象都有的操作，包括：
#         - 移动
#         - 复制
#         - 删除
#         - 重命名
#         - 属性
        

#     All of the items in HDF5 files have these actions:
#         - move
#         - copy
#         - delete
#         - rename
#         - attributes
#     """
#     def __init__(
#         self, 
#         parent: QWidget = None,
#         index: QModelIndex = QModelIndex(),
#     ):
#         super().__init__(parent, index)

#         # self.addActions([
#         #     self._action_move,
#         #     self._action_copy,
#         #     self._action_delete,
#         #     self._action_rename,
#         # ])
#         # self.addSeparator()
#         # self.addActions([
#         #     self._action_attributes,
#         # ])

# class HDFRootMenu(HDFBaseItemMenu):
#     """
#     根目录所具有的操作。包括:
#         - 创建
#         - 属性

#     The root of the HDF5 file has these actions:
#         - create
#         - attributes
#     """
#     def __init__(
#         self, 
#         parent: QWidget = None,
#         index: QModelIndex = QModelIndex(),
#     ):
#         super().__init__(parent, index)

#         self.addActions([
#             self._action_create,
#         ])
#         self.addSeparator()
#         self.addActions([
#             self._action_attributes,
#         ])

# class HDFGroupMenu(HDFBaseItemMenu):
#     """
#     Group 具有的操作。包括：
#         - 创建
#         - 移动
#         - 复制
#         - 删除
#         - 重命名
#         - 属性

#     Groups in HDF5 files have these actions:
#         - create
#         - move
#         - copy
#         - delete
#         - rename
#         - attributes
#     """
#     def __init__(
#         self, 
#         parent: QWidget = None,
#         index: QModelIndex = QModelIndex(),
#     ):
#         super().__init__(parent, index)

#         self.addActions([
#             self._action_create,
#         ])
#         self.addSeparator()
#         self.addActions([
#             self._action_move,
#             self._action_copy,
#             self._action_delete,
#             self._action_rename,
#         ])
#         self.addSeparator()
#         self.addActions([
#             self._action_attributes,
#         ])

# class HDFDataMenu(HDFBaseItemMenu):
#     """
#     HDF 数据具有的操作，包括：
#         - 显示
#         - 更改数据类型
#         - 移动
#         - 复制
#         - 删除
#         - 重命名
#         - 属性

#     Datasets in HDF5 files have these actions:
#         - show
#         - change data type
#         - move
#         - copy
#         - delete
#         - rename
#         - attributes
#     """
#     def __init__(
#         self, 
#         parent: QWidget = None,
#         index: QModelIndex = QModelIndex(),
#     ):
#         super().__init__(parent, index)

#         self.addActions([
#             self._action_show_data,
#             self._action_change_data_type,
#         ])

#         self.addSeparator()

#         self.addActions([
#             self._action_move,
#             self._action_copy,
#             self._action_delete,
#             self._action_rename,
#         ])

#         self.addSeparator()

#         self.addActions([
#             self._action_attributes
#         ])

# class HDFLineMenu(HDFBaseItemMenu):
#     """
#     线性数据所具有的操作。包括：
#         - 显示
#         - 更改数据类型
#         - 移动
#         - 复制
#         - 删除
#         - 重命名
#         - 属性

#     Line data in HDF5 files have these actions:
#         - show
#         - change data type
#         - move
#         - copy
#         - delete
#         - rename
#         - attributes
#     """
#     def __init__(
#         self, 
#         parent: QWidget = None,
#         index: QModelIndex = QModelIndex(),
#     ):
#         super().__init__(parent, index)

#         self.addActions([
#             self._action_show_line,
#             self._action_change_data_type,
#         ])

#         self.addSeparator()
        
#         self.addActions([
#             self._action_move,
#             self._action_copy,
#             self._action_delete,
#             self._action_rename,
#         ])

#         self.addSeparator()

#         self.addActions([
#             self._action_attributes
#         ])

# class HDFImageMenu(HDFBaseItemMenu):
#     """
#     图像数据所具有的操作。包括：
#         - 显示
#         - 更改数据类型
#         - 移动
#         - 复制
#         - 删除
#         - 重命名
#         - 属性

#     Image data in HDF5 files have these actions:
#         - show
#         - change data type
#         - move
#         - copy
#         - delete
#         - rename
#         - attributes
#     """
#     def __init__(
#         self, 
#         parent: QWidget = None,
#         index: QModelIndex = QModelIndex(),
#     ):
#         super().__init__(parent, index)

#         self.addActions([
#             self._action_show_image,
#             self._action_change_data_type,
#         ])

#         self.addSeparator()
        
#         self.addActions([
#             self._action_move,
#             self._action_copy,
#             self._action_delete,
#             self._action_rename,
#         ])

#         self.addSeparator()

#         self.addActions([
#             self._action_attributes
#         ])
    
# class HDFVectorFieldMenu(HDFBaseItemMenu):
#     """
#     矢量场数据所具有的操作。包括：
#         - 显示
#         - 更改数据类型
#         - 移动
#         - 复制
#         - 删除
#         - 重命名
#         - 属性

#     Vector field data in HDF5 files have these actions:
#         - show
#         - change data type
#         - move
#         - copy
#         - delete
#         - rename
#         - attributes
#     """
#     def __init__(
#         self, 
#         parent: QWidget = None,
#         index: QModelIndex = QModelIndex(),
#     ):
#         super().__init__(parent, index)

#         self.addActions([
#             self._action_show_vector_field,
#             self._action_change_data_type,
#         ])

#         self.addSeparator()
        
#         self.addActions([
#             self._action_move,
#             self._action_copy,
#             self._action_delete,
#             self._action_rename,
#         ])

#         self.addSeparator()

#         self.addActions([
#             self._action_attributes
#         ])

# class HDFFourDSTEMMenu(HDFBaseItemMenu):
#     """
#     4D-STEM 数据具有的操作。包括：
#         - 显示
#         - 更改数据类型
#         - 校准
#             |- 查看实验参数
#             |- 合轴
#             |- 背景校正
#             |- 角度校正
#         - 重构
#             |- 虚拟成像
#             |- 差分相位衬度 (DPC)
#             |- 质心成像 (CoM)
#             |- 叠层电子衍射重构 (Ptychography)
#         - 移动
#         - 复制
#         - 删除
#         - 重命名
#         - 属性
#     """
#     def __init__(
#         self, 
#         parent: QWidget = None,
#         index: QModelIndex = QModelIndex(),
#     ):
#         super().__init__(parent, index)

#         self.addActions([
#             self._action_show_fourdstem,
#             self._action_change_data_type,
#         ])

#         self.addSeparator()
    
#         menu_calibrate = self.addMenu('Calibrate')
#         menu_calibrate.addActions([
#             self._action_align,
#             self._action_bkgrd,
#             self._action_rotate,
#         ])
#         menu_reconstruct = self.addMenu('Reconstruct')
#         menu_reconstruct.addActions([
#             self._action_virtual_image,
#             self._action_center_of_mass,
#         ])
        
#         self.addSeparator()

#         self.addActions([
#             self._action_move,
#             self._action_copy,
#             self._action_delete,
#             self._action_rename,
#         ])

#         self.addSeparator()

#         self.addActions([
#             self._action_attributes,
#         ])

        