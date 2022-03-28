# -*- coding: utf-8 -*-

"""
*---------------------------- PageViewImage.py -------------------------------*
显示二维图像(单通道)的页面。

部件内容：
    - WidgetPlotImage 用于使用 Matplotlib 来显示图像
    - WidgetPlotHist 用于使用 Matplotlib 来显示图像的直方图

提升部件：
    - 提升类名 PageViewImage
    - 头文件 bin.Widgets.PageViewImage

作者:           胡一鸣
创建日期:       2022年3月25日

The GUI page to view 2D images (single channel).

Contents:
    - WidgetPlotImage, to view the 2D image
    - WidgetPlotHist, to view the histogram of the image

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
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import numpy as np
import h5py

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFDataNode, HDFHandler
from ui import uiPageViewImage

class PageViewImage(QWidget):
    """
    显示二维图像的部件类。

    Ui 文件地址：ROOT_PATH/ui/uiPageViewImage.ui

    Widget to view 2D images.

    The path of the ui file: ROOT_PATH/ui/uiPageViewImage.ui

    attributes:
        hdf_handler: (HDFHandler) Manager to handle the HDF file. This is a 
            global singleton.

        data_object: (h5py.Dataset) The Dataset object to be drawn. Can also
            be np.ndarray or other ArrayLike objects.

        data_path: (str) The path of the Dataset object in the HDF5 file.

        logger: (Logger) Use logger to log exceptions. This is a singleton.

        image_canvas: (FigureCanvas) The canvas to draw image.

        hist_canvas: (FigureCanvas) The canvas to draw histogram of the image.

        image_figure: (Figure) The figure where image locates.

        hist_figure: (Figure) The figure where histogram locates.

        image_ax: (Axes) The Axes where image locates.

        hist_ax: (Axes) The Axes where histogram locates.

        colorbar_ax: (Axes) The Axes where colobar locates.

        image_object: (AxesImage) The image object. Can use its set-get methods
            to handle how to render the data.

        colorbar_object: (Colorbar) The Colorbar object.

        image_blit_manager: (BlitManager) Use BlitManager.update() to refresh 
            artists quickly or make animation effects. example: 
                self.image_object.set_data(new_data)
                self.image_blit_manager.update()

        
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageViewImage.Ui_Form()
        self.ui.setupUi(self)
        
        self._data_path = ''
        self._image_ax = None
        self._colorbar_ax = None
        self._image_object = None
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
        return self.ui.widget_hist_view.axes

    @property
    def colorbar_ax(self) -> Axes:
        return self._colorbar_ax

    @property
    def image_object(self) -> AxesImage:
        return self._image_object

    @property
    def colorbar_object(self) -> Colorbar:
        return self._colorbar_object

    @property
    def image_blit_manager(self) -> BlitManager:
        return self.ui.widget_image.blit_manager

    def setImage(self, data_path: str):
        """
        Set the data path in HDF5 file, to show the image.

        Will set the data_path attribute. The image must be a 2D matrix. 
        RGB images (3 channels) are not supported here.

        arguments:
            data_path: (str) the path of the image or data. 

        raises:
            TypeError, KeyError, ValueError
        """
        if not isinstance(data_path, str):
            raise TypeError('data_path must be a str, not '
                '{0}'.format(type(data_path).__name__))

        img_node = self.hdf_handler.getNode(data_path)  
        # May raise KeyError if the path is not exist
        if not isinstance(img_node, HDFDataNode):
            raise ValueError('Item {0} must be a Dataset'.format(data_path))
            
        data_obj = self.hdf_handler.file[data_path]
        if not len(data_obj.shape) == 2:
            raise ValueError('Data must be a 2D matrix (single channel image)')

        self._data_path = data_path
        self.ui.lineEdit_image_path.setText(self.data_path)
        self.setWindowTitle('{0} - Image'.format(img_node.name))

        self._createAxes()
        self._createImage()


    def _createAxes(self):
        """
        Create the axes that contains the image and the colorbar respectively.
        """
        if self._image_ax is None:
            self._image_ax = self.image_figure.add_subplot()
        if self._colorbar_ax is None:
            self._colorbar_ax, _kw = make_axes(
                self.image_ax,
                location = 'right',
                orientation = 'vertical',
            )
            self._colorbar_ax.xaxis.set_visible(False)
            self._colorbar_ax.yaxis.tick_right()
        
    def _createImage(self):
        """
        Read the image and its attributes, and show it.

        TODO: read and save attributes, like norm, cmap, alpha, etc.
        """
        # attrs = self.data_object.attrs
        if self.image_object is None:
            self._image_object = self.image_ax.imshow(self.data_object)
            self.image_blit_manager.addArtist(self._image_object)
            self.image_canvas.draw()
            self.image_canvas.flush_events()
        else:
            self.image_object.set_data(self.data_object)
            self.image_blit_manager.update()
        
        self.ui.widget_hist_view.drawHist(self.data_object)
        
        
    # def updateImage(self):
    #     pass

        
        
    