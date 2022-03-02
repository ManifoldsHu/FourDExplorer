# -*- coding: utf-8 -*-

"""
*--------------------------- WidgetHDFViewer.py ------------------------------*
对 HDF5 文件内部的层次结构进行显示的模块。

4D-Explorer 软件默认使用 HDF5 进行四维数据及其元数据的管理。其数据的组织方式类似于
Unix 目录。为此，我们使用 Qt 的 QTreeView 对这些四维数据进行管理。

作者：          胡一鸣
创建时间：      2022年3月2日
*--------------------------- WidgetHDFViewer.py ------------------------------*
"""

from PySide6.QtWidgets import QWidget 
from ui import uiWidgetBaseHDFViewer

class WidgetBaseHDFViewer(QWidget):
    """
    查看 HDF5 文件内部结构的基类。
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetBaseHDFViewer.Ui_Form()
        self.ui.setupUi(self)

        global qApp 
        self._hdf_handler = qApp.hdf_handler

        self.ui.pushButton_search.setEnabled(
            self._hdf_handler.isFileOpened()
        )
        self.ui.pushButton_refresh.setEnabled(
            self._hdf_handler.isFileOpened()
        )

        self._hdf_handler.file_state_changed.connect(
            self.changeStateByFileState)

        self.ui.treeView_HDF.setModel(self._hdf_handler.model)
    
    def changeStateByFileState(self):
        """
        Reactions (Slot) of file widgets if the file state is changed 
        (opened or close).
        """
        self.ui.pushButton_refresh.setEnabled(
            self._hdf_handler.isFileOpened()
        )
        self.ui.pushButton_search.setEnabled(
            self._hdf_handler.isFileOpened()
        )
        self.refresh()

    @property 
    def hdf_handler(self):
        return self._hdf_handler

    
    def refresh(self):
        """
        Will rebuild the HDFTree and then create a new model.
        """
        self._hdf_handler.buildHDFTree()
        self._hdf_handler._createModel()
        self.ui.treeView_HDF.setModel(self._hdf_handler.model)

    def search(self):
        pass