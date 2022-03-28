"""
*----------------------------- PageViewLine.py -------------------------------*
显示一维曲线的页面。

部件内容：
    - WidgetPlotLine 用于使用 matplotlib 来显示曲线

提升部件：
    - 提升类名 PageViewLine
    - 头文件 bin.Widgets.PageViewLine

作者:           胡一鸣
创建日期:       2022年3月28日

The GUI page to view 2D lines.

Contents:
    - WidgetPlotLine, to view the 2D line

Promoted Widget:
    - name of widget class: PageViewLine
    - header file: bin.Widget.PageViewLine

author:         Hu Yiming
date:           Mar 25, 2022
*----------------------------- PageViewLine.py -------------------------------*
"""

from logging import Logger
from typing import List 

from PySide6.QtWidgets import QWidget, QListView
from PySide6.QtCore import QAbstractListModel, QObject
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
# from matplotlib.rcsetup import cycler
# from matplotlib import rcParams
import numpy as np
import h5py

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFDataNode, HDFHandler
from ui import uiPageViewLine


class PageViewLine(QWidget):
    """
    显示一维曲线的部件类。

    Ui 文件地址：ROOTPATH/ui/uiPageViewLine.ui

    Widget to view 1D/2D lines.

    The path of the ui file: ROOT_PATH/ui/uiPageViewLine.ui

    attributes:
        hdf_handler: (HDFHandler) Manager to handle the HDF file. This is a 
            global singleton.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageViewLine.Ui_Form()
        self.ui.setupUi()

        self._data_paths = []
        self._line_ax = None
        self._line_objects = []
        self._model = None
        # self._cycler = cycler(
        #     color=['#1f77b4', 'green', 'blue', 'black'],
        #     linestyle = ['']
        # )

        self.ui.lineEdit_line_path.setReadOnly(True)

    @property
    def data_paths(self) -> List[str]:
        return self._data_paths

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler

    @property
    def line_ax(self) -> Axes:
        return self._line_ax

    @property
    def line_canvas(self) -> FigureCanvas:
        return self.ui.widget_plot_line.canvas

    @property
    def line_figure(self) -> Figure:
        return self.ui.widget_plot_line.figure

    @property
    def line_model(self) -> QAbstractListModel:
        return self._model

    @property
    def line_objects(self) -> List[Line2D]:
        return self.line_objects

    @property
    def line_blit_manager(self) -> BlitManager:
        return self.ui.widget_plot_line.blit_manager

    def addLine(self, data_path: str, update_title: bool = False):
        """
        Set the data_path of the line, to show the curve.

        Will set the data_path attribute. The line must be a 2D array with 
        shape (2, n).

        NOTE: This function is to add a new line. So other lines saved in the 
        self._data_paths and self._line_objects will not be cleared. If it is
        the first time this function is called, axes will be initialized.

        arguments:
            data_path: (str) the data's path in the HDF5 file.

            update_title: (bool) whether to update the window title and the 
                path lineEdit. If this is the first line, it is recommended to
                be True.

        raises:
            TypeError, KeyError, ValueError
        """
        if not isinstance(data_path, str):
            raise TypeError('data_path must be a str, not '
                '{0}'.format(type(data_path).__name__))

        line_node = self.hdf_handler.getNode(data_path)  
        # May raise KeyError if the path is not exist
        if not isinstance(line_node, HDFDataNode):
            raise ValueError('Item {0} must be a Dataset'.format(data_path))

        data_object = self.hdf_handler.file[data_path]
        if not (len(data_object.shape) == 1 or len(data_object.shape) == 2):
            raise ValueError('Data must be an 1D array or 2D matrix')
        elif not (len(data_object.shape) == 2 and data_object.shape[0] == 2):
            raise ValueError('Data must be with shape (n,) or (2, n)')
        
        self._data_paths.append(data_path)

        if update_title:
            self.ui.lineEdit_line_path.setText(data_path)
            self.setWindowTitle('{0} - Line'.format(line_node.name))

        self._createAxes()
        self._createLine(data_object)

    def _createAxes(self):
        """
        Create the axes that contains the lines.
        """
        if self._line_ax is None:
            self._line_ax = self.line_figure.add_subplot()
    
    def _createLine(self, data_object: h5py.Dataset):
        """
        Read the line and its attributes, and show it.

        TODO: read and save attributes.

        attributes:
            data_object: (h5py.Dataset) or other Array like.
        """
        if len(data_object.shape) == 1:
            X_data = np.arange(len(data_object))
            Y_data = data_object
        elif len(data_object.shape) == 2:
            X_data = data_object[0, :]
            Y_data = data_object[1, :]
        else:
            raise ValueError('Invalid data shape to draw line.')
        
        line = self._line_ax.plot(X_data, Y_data)
        self._line_objects.append(line)
        self.line_blit_manager.addArtist(line)
        self.line_canvas.draw()
        self.line_canvas.flush_events()

        # line = self._line_ax.plot()
        # self._line_objects.append()

class LinesModel(QAbstractListModel):
    """
    用来查看多条 Lines 的 model。

    这是 Qt 中 Model/View 架构的一部分。要显示这些曲线，可以通过实例化 QListView，
    然后调用其 setModel() 方法，将这个类的实例传递进去。

    为了实现只读的、显示与数据分离的架构，这个 Model 类必须实现如下方法：
        - rowCount(self, parent: QModelIndex) -> int
            返回有多少列

        - data(self, index: QModelIndex, role: int)
            根据 role 的不同，返回数据结构中内部存储的数据

    This is a model for viewing lines.

    This is a part of Model/View architecture of Qt. If we want to display 
    these lines, we can instantiate QListView, and call its setModel() method.

    In order to realize a read-only and data-display decoupled architecture, we
    need to reimplement the following methods:
        - rowCount(self, parent: QModelIndex) -> int
            Get number of rows (number of lines)

        - data(self, index: QModelIndex, role: int)
            Return the internal data according to the role
    """
    def __init__(self, parent: QObject):
        """
        arguments:
            parent: (QObject)
        """
        super().__init__(parent)
        