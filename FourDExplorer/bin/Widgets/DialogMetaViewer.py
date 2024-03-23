# -*- coding: utf-8 -*- 

"""
*--------------------------- DialogMetaViewer.py -----------------------------*
用于查看属性值的对话框。

该文件替代 DialogAttrViewer.py

作者：          胡一鸣
创建时间：      2024年3月24日

Dialog to view the attrs of items in the h5 file.

This file replaces DialogAttrViewer.py

author:             Hu Yiming
date:               Mar 24, 2024
*--------------------------- DialogMetaViewer.py -----------------------------*
"""

from PySide6.QtWidgets import QDialog 
from PySide6.QtWidgets import QWidget 

from bin.MetaManager import MetaManager

from ui import uiDialogMetaViewer

class DialogMetaViewer(QDialog):
    """
    用于查看属性值的对话框。

    Dialog to view the metadata (keys and values).
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogMetaViewer.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Metadata")
        self.ui.lineEdit_item_path.setReadOnly(True)
        self.ui.pushButton_browse_item_path.setVisible(False)
        self._item_path = ''

    @property
    def item_path(self) -> str:
        return self._item_path
    
    @property
    def meta_manager(self) -> MetaManager:
        global qApp 
        return qApp.requireMetaManager(self.item_path)

    def setItemPath(self, item_path: str):
        """
        Set the item path (of the meta data).

        arguments:
            item_path: (str) The path of the item (Dataset or Group)
        """
        if not isinstance(item_path, str):
            raise TypeError(f'path must be a str, not {type(item_path).__name__}')
        self._item_path = item_path 
        self.ui.lineEdit_item_path.setText(item_path)
        self.ui.widget.setItemPath(item_path)
        # self.ui.widget.ui.widget_meta_viewer.setItemPath(item_path)
        # self.ui.widget.ui.widget_meta_viewer_not_pathlike.setItemPath(item_path)

    
