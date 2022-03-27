# -*- coding: utf-8 -*-

"""
*---------------------------- PageViewImage.py -------------------------------*
显示二维图像(单通道)的页面。

部件内容：
    - WidgetImagePlot 用于使用 Matplotlib 来显示图像
    - WidgetImageHistPlot 用于使用 Matplotlib 来显示图像的直方图

提升部件：
    - 提升类名 PageViewImage
    - 头文件 bin.Widgets.PageViewImage

作者:           胡一鸣
创建日期:       2022年3月25日

The GUI page to view 2D images (single channel).

Contents:
    - WidgetImagePlot, to view the 2D image
    - WidgetImageHistPlot, to view the histogram of the image

Promoted Widget:
    - name of widget class: PageViewImage
    - header file: bin.Widget.PageViewImage

author:         Hu Yiming
date:           Mar 25, 2022
*---------------------------- PageViewImage.py -------------------------------*
"""

from logging import Logger

from PySide6.QtWidgets import QWidget, QMessageBox
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.colorbar import Colorbar, make_axes
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.image import AxesImage
from matplotlib.axis import Axis
 

import h5py

from bin.HDFManager import HDFDataNode, HDFHandler
from ui import uiPageViewImage

class PageViewImage(QWidget):
    """
    显示二维图像的部件类。

    Ui 文件地址：ROOT_PATH/ui/uiPageViewImage.ui

    Widget to view 2D images.

    The path of the ui file: ROOT_PATH/ui/uiPageViewImage.ui
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageViewImage.Ui_Form()
        self.ui.setupUi(self)
        
        self._data_path = ''
        self._image_ax = None
        self._hist_ax = None
        self._colorbar_ax = None
        self._image_object = None
        self._hist_object = None
        self._colorbar_object = None

        self.ui.lineEdit_image_path.setReadOnly(True)


    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler

    @property
    def data_object(self) -> h5py.Dataset:
        return self.hdf_handler.file[self._data_path]

    @property
    def data_path(self) -> str:
        return self._data_path

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    @property
    def image_canvas(self) -> FigureCanvas:
        return self.ui.widget_image.canvas

    @property
    def hist_canvas(self) -> FigureCanvas:
        return self.ui.widget_hist_view.canvas

    @property
    def image_figure(self) -> Figure:
        return self.ui.widget_image.figure

    @property
    def hist_figure(self) -> Figure:
        return self.ui.widget_image.figure

    @property
    def image_ax(self) -> Axes:
        return self._image_ax

    @property
    def hist_ax(self) -> Axes:
        return self._hist_ax

    @property
    def colorbar_ax(self) -> Axes:
        return self._colorbar_ax

    @property
    def image_object(self) -> AxesImage:
        return self._image_object

    @property
    def hist_object(self) -> AxesImage:
        return self._hist_object

    @property
    def colorbar_object(self) -> Colorbar:
        return self._colorbar_object

    def setImage(self, data_path: str):
        """
        Set the data path, to show the image.

        Will set the data_path attribute. The image must be a 2D matrix. 
        RGB images (3 channels) are not supported here.

        arguments:
            data_path: (str) the path of the image or data. 
        """
        if not isinstance(data_path, str):
            raise TypeError('img_path must be a str, not '
                '{0}'.format(type(data_path).__name__))

        msg = QMessageBox(parent = self)
        msg.setWindowTitle('Warning')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)

        try:
            img_node = self.hdf_handler.getNode(data_path)
        except KeyError as e:
            self.logger.error('{0}'.format(e), exc_info = True)
            msg.setText('There is no image: {0}'.format(data_path))
            msg.exec()
            return None
        
        if not isinstance(img_node, HDFDataNode):
            self.logger.error('Item {0} must be a Dataset'.format(data_path))
            msg.setText('Item {0} must be a Dataset'.format(data_path))
            msg.exec()
            return None

        data_obj = self.hdf_handler.file[data_path]
        if not len(data_obj.shape) == 2:
            self.logger.error('Data must be a 2D matrix. '
                '(length of shape must be 2)')
            msg.setText('Data must be a 2D matrix. '
                '(length of shape must be 2)')
            msg.exec()
            return None

        self._data_path = data_path
        self.ui.lineEdit_image_path.setText(self.data_path)
        
        self._createAxes()



    def _createAxes(self):
        """
        Create the axes that contains the image, histogram and the colorbar.
        """
        self._image_ax = self.image_figure.add_subplot()
        self._hist_ax = self.hist_figure.add_subplot()
        self._colorbar_ax, _kw = make_axes(
            self.image_ax,
            location = 'right',
            orientation = 'vertical',
        )
        
    def _createImages(self):
        """
        Read the image and its attributes, and show it.
        """
        self._image_object = self.image_ax.imshow(self.data_object)
        

    def updateImage(self):
        pass

        
        
    