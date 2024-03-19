# -*- coding: utf-8 -*-

"""
*--------------------------- DialogAttrViewer.py -----------------------------*
用于查看属性值的对话框。

作者：          胡一鸣
创建时间：      2022年3月11日

Dialog to view the attrs of items in the h5 file.

author:             Hu Yiming
date:               Mar 11, 2022
*--------------------------- DialogAttrViewer.py -----------------------------*
"""

from PySide6.QtWidgets import QDialog, QWidget, QHeaderView
from ui import uiDialogAttrViewer
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.HDFManager import HDFAttrModel
# from bin.MetaManager import MetaManager, ValueTree, ValueTreeModel
from bin.MetaManager import MetaManager
from bin.MetaManager import MetaTree 
from bin.MetaManager import MetaTreeModel

class DialogAttrViewer(QDialog):
    """
    用于查看属性值的对话框。

    Dialog to view the attributions (keys and values).
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogAttrViewer.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Attributions')

        # self._item_path = '/'
        # self.ui.lineEdit_item_path.setText('/')
        self.ui.lineEdit_item_path.setReadOnly(True)

        # self.ui.tableView_attr.setModel(HDFAttrModel(self))


        # horizontal_header.setEnabled(True)
        # horizontal_header.setHidden(False)
        
        
        
    @property
    def item_path(self) -> str:
        return self._item_path

    @property
    def model(self) -> HDFAttrModel:
        return self.ui.tableView_attr.model()

    @item_path.setter
    def item_path(self, path):
        if not isinstance(path, str):
            raise TypeError('path must be a str, not'
                '{0}'.format(type(path)))
        self._item_path = path
        

    def setItemPath(self, path: str):
        """
        Set the item path (of the attributions).
        """
        self.item_path = path
        self.ui.lineEdit_item_path.setText(path)
        model = HDFAttrModel(self)
        model.initialize(path)
        self.ui.tableView_attr.setModel(model)
        vertical_header = self.ui.tableView_attr.verticalHeader()
        vertical_header.setVisible(False)
        horizontal_header = self.ui.tableView_attr.horizontalHeader()
        horizontal_header.setSectionResizeMode(QHeaderView.Stretch)
        horizontal_header.setAlternatingRowColors(True)

        self.setMetaTree()
        self.setupWidgetMetaViewer()


    def setMetaTree(self):
        # Experimental
        self._meta_manager = MetaManager(self)
        self._meta_manager.setItemPath(self.item_path)
        hdf_type = self._meta_manager.hdf_type 
        self._meta_manager.initializeSchema(hdf_type)
        self.ui.treeView.setModel(self._meta_manager.meta_tree_model)

    def setupWidgetMetaViewer(self):
        # Experimental 
        self._meta_manager_2 = MetaManager(self)
        self.widget_meta_viewer = self.ui.widget 
        self.widget_meta_viewer.initMetaViewer(self.item_path)
        
        