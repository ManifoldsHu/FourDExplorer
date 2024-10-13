# -*- coding: utf-8 -*- 

"""
*-------------------------- WidgetImportHDF5.py ------------------------------*
用于从其他 HDF5 文件导入数据的部件。

作者:           胡一鸣
创建时间:       2024年10月13日

Widgets to import 4D-STEM dataset from other HDF5 file.

author:         Hu Yiming
date:           Oct 13, 2024
*-------------------------- WidgetImportHDF5.py ------------------------------*
"""

from logging import Logger 
import os 

from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtGui import QIcon

import h5py

from bin.UIManager import ThemeHandler
from ui import uiWidgetImportHDF5 

class WidgetImportHDF5(QWidget):
    """
    用于从其他 HDF5 文件中复制某个 Dataset 到当前 HDF5 文件的部件。
    
    包含选择 .h5 文件的对话框以及一个 tree widget 来选择群组或者数据集。
    
    Widget to copy dataset from other HDF5 file to current opened HDF5 file.
    
    This includes a dialog to choose the .h5 file and a tree widget to choose 
    dataset or group.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetImportHDF5.Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.lineEdit_file_path.setReadOnly(True)
        
        self.ui.pushButton_browse.clicked.connect(self._chooseHDF5)
        self.ui.treeWidget_other_hdf5.itemClicked.connect(self._selectDataset)
        self.ui.treeWidget_other_hdf5.setHeaderLabels(["Dataset"])

    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger
    
    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler

    def _chooseHDF5(self):
        """
        Opens a file dialog to choose an HDF5 file.
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Select HDF5 File", "", "HDF5 Files (*.h5 *.hdf5)")
        if file_path:
            self.ui.lineEdit_file_path.setText(file_path)
            self._populateTreeWidget(file_path)

    def _populateTreeWidget(self, file_path: str):
        """
        Populates the tree widget with the structure of the selected HDF5 file.

        arguments:
            file_path: (str) Path to the HDF5 file.
        """
        self.ui.treeWidget_other_hdf5.clear()
        try:
            with h5py.File(file_path, 'r') as h5file:
                self._addItemsToTree(h5file, self.ui.treeWidget_other_hdf5.invisibleRootItem())
        except Exception as e:
            self.logger.error(f"Failed to open HDF5 file: {str(e)}")
            QMessageBox.warning(self, "Error", f"Failed to open HDF5 file: {str(e)}")

    def _addItemsToTree(self, h5group: 'h5py.Group', parent_item: QTreeWidgetItem):
        """
        Recursively adds items to the tree widget from the HDF5 group.

        arguments:
            h5group: (h5py.Group) The HDF5 group to add.
            
            parent_item: (QTreeWidgetItem) The parent tree widget item.
        """
        for name, item in h5group.items():
            tree_item = QTreeWidgetItem(parent_item)
            tree_item.setText(0, name)
            if isinstance(item, h5py.Group):
                tree_item.setIcon(0, self.theme_handler.iconProvider("folder"))
                self._addItemsToTree(item, tree_item)
            elif isinstance(item, h5py.Dataset):
                tree_item.setIcon(0, self.theme_handler.iconProvider("file"))
                # Add tooltip for datasets
                tooltip = f"Size: {item.shape}, Dtype: {item.dtype}"
                tree_item.setToolTip(0, tooltip)

    def _selectDataset(self, item: QTreeWidgetItem, column: int):
        """
        Handles the selection of a dataset in the tree widget. 
        
        Currently do nothing.

        arguments:
            item: (QTreeWidgetItem) The selected tree widget item.
            
            column: (int) The column of the selected item.
        """
        pass 

    
    def getHDF5FilePath(self) -> str:
        """
        Provides an external interface to get the path of the selected HDF5 file.

        returns:
            (str) The path to the selected HDF5 file.
        """
        return self.ui.lineEdit_file_path.text()
    
    def getSelectedItemPath(self) -> str:
        """
        Provides an external interface to get the path of the selected dataset or group in the HDF5 file.

        returns:
            (str) The path to the selected dataset or group, starting with '/'.
        """
        selected_item = self.ui.treeWidget_other_hdf5.currentItem()
        if selected_item:
            path_parts = []
            item = selected_item
            while item:
                path_parts.insert(0, item.text(0))
                item = item.parent()
            path = '/' + '/'.join(path_parts)
            return path
        return '/'
    
    

class WidgetImport4DSTEMFromHDF5(WidgetImportHDF5):
    """
    在 HDF5 文件中，只显示 4D-STEM 数据集的部件。
    
    Widget that only show 4D-STEM datasets from the HDF5 files in the tree 
    widget. 
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

    @property
    def icon_group(self):
        return self.theme_handler.iconProvider("folder")
        
    @property
    def icon_dataset(self):
        return self.theme_handler.iconProvider("file")

    def _addItemsToTree(self, hdf5_group: h5py.Group, parent_item: QTreeWidgetItem):
        """
        Adds items to the tree widget, filtering to show only 4D-STEM datasets.

        arguments:
            hdf5_group: (h5py.Group) The HDF5 group to add items from.
            parent_item: (QTreeWidgetItem) The parent tree widget item.
        """
        for key, value in hdf5_group.items():
            item = QTreeWidgetItem(parent_item)
            item.setText(0, key)
            if isinstance(value, h5py.Dataset):
                if self._is4DSTEMDataset(hdf5_group.name + '/' + key):
                    item.setIcon(0, self.icon_dataset)
                else:
                    parent_item.removeChild(item)
            elif isinstance(value, h5py.Group):
                item.setIcon(0, self.icon_group)
                self._addItemsToTree(value, item)

    def _is4DSTEMDataset(self, dataset_path: str) -> bool:
        """
        Checks if the dataset is a 4D-STEM dataset.

        arguments:
            dataset_path: (str) The path to the dataset in the HDF5 file.

        returns:
            (bool) True if the dataset is a 4D-STEM dataset, False otherwise.
        """
        with h5py.File(self.getHDF5FilePath(), 'r') as hdf5_file:
            dataset = hdf5_file.get(dataset_path)
            if dataset is not None and len(dataset.shape) == 4:
                return True
        return False