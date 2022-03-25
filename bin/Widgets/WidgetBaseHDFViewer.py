# -*- coding: utf-8 -*-

"""
*--------------------------- WidgetHDFViewer.py ------------------------------*
对 HDF5 文件内部的层次结构进行显示的模块。

4D-Explorer 软件默认使用 HDF5 进行四维数据及其元数据的管理。其数据的组织方式类似于
Unix 目录。为此，我们使用 Qt 的 QTreeView 对这些四维数据进行管理。

这个 Widget 是用在小窗口的，只具有查找功能。

作者：          胡一鸣
创建时间：      2022年3月2日

The Module to show HDF5 file structure.

4D-Explorer software use HDF5 to manage 4D-STEM data and its metadata. It looks
like Unix file system, so we use QTreeView to show the structures.

This widget is used in the dialogs, and hence has only search method.

author:         Hu Yiming
date:           Mar 2, 2022
*--------------------------- WidgetHDFViewer.py ------------------------------*
"""

from PySide6.QtWidgets import QWidget, QMessageBox
from bin.HDFManager import HDFHandler
from ui import uiWidgetBaseHDFViewer

class WidgetBaseHDFViewer(QWidget):
    """
    查看 HDF5 文件内部结构的基类。
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetBaseHDFViewer.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_search.setEnabled(
            self.hdf_handler.isFileOpened()
        )
        self.ui.pushButton_refresh.setEnabled(
            self.hdf_handler.isFileOpened()
        )

        self.ui.pushButton_refresh.clicked.connect(self.refresh)

        self.hdf_handler.file_state_changed.connect(
            self.changeStateByFileState)

        self.ui.treeView_HDF.setModel(self.hdf_handler.model)

        self._last_kw = ''  # last key word of the user, for searching
        self.ui.pushButton_search.clicked.connect(self.search)
        self._result_generator = None 
    
    def changeStateByFileState(self):
        """
        Reactions (Slot) of file widgets if the file state is changed 
        (opened or close).
        """
        self.ui.pushButton_refresh.setEnabled(
            self.hdf_handler.isFileOpened()
        )
        self.ui.pushButton_search.setEnabled(
            self.hdf_handler.isFileOpened()
        )
        self.refresh()

    @property 
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler

    
    def refresh(self):
        """
        Will rebuild the HDFTree and then create a new model.
        """
        self.hdf_handler.buildHDFTree()
        self.hdf_handler._createModel()
        self.ui.treeView_HDF.setModel(self.hdf_handler.model)

    def search(self) -> bool:
        """
        When the pushbutton 'search' is clicked, this function will be called.

        This function will build a generator, which generates matched nodes. 
        Then everytime this function is called, the generator returns the next 
        matched node. This function will at last show the corresponding index 
        in the treeview of the HDF5 file.

        returns:
            (bool) whether there is a matched item.
        """
        kw = self.ui.lineEdit_search.text()
        if kw == '':
            return False
        else:
            if kw != self._last_kw:
                # The user changes the key word, so we need rebuild the genera-
                # tor and search from the beginning of the tree.
                self._last_kw = kw
                model = self.ui.treeView_HDF.model()
                self._result_generator = model.matchIndexGenerator(kw)
            if self._result_generator is None:
                return False
            try:
                index = next(self._result_generator)
                self.ui.treeView_HDF.setCurrentIndex(index)
                return True
            except StopIteration:
                msg = QMessageBox(parent = self)
                msg.setWindowTitle('Search Next')
                msg.setIcon(QMessageBox.Information)
                msg.setText('No more results.')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                self._last_kw = '' # reset the search widget
                return False

    
