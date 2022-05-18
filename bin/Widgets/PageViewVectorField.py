# -*- coding: utf-8 -*-

"""
*------------------------- PageViewVectorField.py ----------------------------*
显示矢量场数据的页面。

部件内容：
    - WidgetPlotVector 用于使用 matplotlib 显示矢量场及背景
    - WidgetPlotBackground 用于使用 matplotlib 显示全域背景

提升部件
    - 提升类名 PageViewVectorField
    - 头文件 bin.Widgets.PageViewVectorField

作者:           胡一鸣
创建日期:       2022年5月18日

The GUI page to view Vector Field dataset.

Contents:
    - WidgetPlotVector, to view the vector fields and backgroud by matplotlib
    - WidgetPlotBackground, to view the full-scale background by matplotlib

Promoted Widget:
    - name of widget class: PageViewVectorField
    - header file: bin.Widgets.PageViewVectorField

author:         Hu Yiming
date:           Mar 30, 2022
*------------------------- PageViewVectorField.py ----------------------------*
"""

from logging import Logger
import os
from PySide6.QtWidgets import QWidget, QMessageBox 
from matplotlib.backend_bases import MouseEvent 
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure
from matplotlib.axes import Axes 
from matplotlib.image import AxesImage 
from matplotlib.quiver import Quiver
from matplotlib.patches import Rectangle
from matplotlib.colorbar import Colorbar, make_axes
import h5py 
import numpy as np

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFDataNode, HDFHandler 
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from ui import uiPageViewVectorField

class PageViewVectorField(QWidget):
    """
    显示二维矢量场的部件类。使用 Quiver。

    Ui 文件地址：ROOT_PATH/ui/uiPageVieweVectorField.ui

    Widget to view vector fields by quiver plot.

    The path of the ui file: ROOT_PATH/ui/uiPageViewVectorField.ui
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageViewVectorField.Ui_Form()
        self.ui.setupUi(self)

        self._data_path = ''
        self._background_path = ''
        self._image_ax = None 
        self._colorbar_ax = None 
        self._background_ax = None 
        self._quiver_object = None 
        self._colorbar_object = None 
        self._background_object = None
        self._image_object = None 
        self._image_max = 0
        self._image_min = 0

        self.ui.lineEdit_vector_path.setReadOnly(True)
        self.ui.lineEdit_background_path.setReadOnly(True)

        self._initUi()
        self._createAxes()

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
        return self.ui.widget_quiver.canvas 

    @property
    def background_canvas(self) -> FigureCanvas:
        return self.ui.widget_background.canvas

    @property
    def image_figure(self) -> Figure:
        return self.ui.widget_quiver.figure 

    @property
    def background_figure(self) -> Figure:
        return self.ui.widget_background.figure 

    @property
    def image_ax(self) -> Axes:
        return self._image_ax 

    @property
    def background_ax(self) -> Axes:
        return self._background_ax

    @property
    def colorbar_ax(self) -> Axes:
        return self._colorbar_ax 

    @property
    def image_object(self) -> AxesImage:
        return self._image_object

    @property
    def quiver_object(self) -> Quiver:
        return self._quiver_object

    @property
    def colorbar_object(self) -> Colorbar:
        return self._colorbar_object

    @property
    def background_object(self) -> AxesImage:
        return self._background_object

    @property
    def background_path(self) -> str:
        return self._background_path

    @property
    def image_blit_manager(self) -> BlitManager:
        return self.ui.widget_quiver.blit_manager

    @property
    def background_blit_manager(self) -> BlitManager:
        return self.ui.widget_background.blit_manager

    @property
    def background_visible(self) -> bool:
        return self.ui.checkBox_background_visible.isChecked()

    def setVectorField(self, data_path: str):
        """
        Set the data path in HDF5 file, to show the vector field.

        Will set the data_path attribute. The vector field must be a 3D matrix.

        arguments:
            data_path: (str) the path of the vector field data.

        raises:
            TypeError, KeyError, ValueError
        """
        if not isinstance(data_path, str):
            raise TypeError('data_path must be a str, not '
                '{0}'.format(type(data_path).__name__))

        img_node = self.hdf_handler.getNode(data_path)  
        # May raise KeyError if the path does not exist
        if not isinstance(img_node, HDFDataNode):
            raise ValueError('Item {0} must be a Dataset'.format(data_path))

        data_obj = self.hdf_handler.file[data_path]
        if not len(data_obj.shape) == 3:
            raise ValueError('Data must be a 3D matrix (2, i, j)')

        self._data_path = data_path
        self.ui.lineEdit_vector_path.setText(self.data_path)
        self.setWindowTitle('{0} - Vector'.format(img_node.name))

        self._createQuiver()
        
        if 'background_path' in self.data_object.attrs:
            background_path = self.data_object.attrs['background_path']
            try:
                self.setBackground(background_path)
            except (KeyError, ValueError, TypeError):
                new_background_path = self._createNewBackground()
                self.setBackground(new_background_path)
        else:
            new_background_path = self._createNewBackground()
            self.setBackground(new_background_path)

        self.image_canvas.draw()
        self.image_canvas.flush_events()
        # self._createBackground()


    def _createAxes(self):
        """
        Create the axes that contains the quiver, colorbar and the background
        respectively.
        """
        if self._image_ax is None:
            self._image_ax = self.image_figure.add_subplot()
            self.image_blit_manager.addArtist('image_axes', self._image_ax)
        
        if self._background_ax is None:
            self._background_ax = self.background_figure.add_subplot()
            self.background_blit_manager.addArtist(
                'background_axes', 
                self._background_ax,
            )

        if self._colorbar_ax is None:
            self._colorbar_ax, _kw = make_axes(
                self.background_ax,
                location = 'right',
                orientation = 'vertical',
            )
            self._colorbar_ax.xaxis.set_visible(False)
            self._colorbar_ax.yaxis.tick_right()

            self.background_blit_manager['colorbar_axes'] = self._colorbar_ax

    def _createQuiver(self):
        """
        Read the vector field and its attributes, and show it.

        TODO: read and save attributes, like length unit.
        """
        if self._quiver_object in self.image_ax.collections:
            _index = self.image_ax.collections.index(self._quiver_object)
            self.image_ax.collections.pop(_index)

        _, height, width = self.data_object.shape 
        array_i = np.linspace(0, height - 1, height)
        array_j = np.linspace(0, width - 1, width)
        coord_i, coord_j = np.meshgrid(array_i, array_j, indexing = 'ij')
        vec_i, vec_j = self.data_object[0, :, :], self.data_object[1, :, :]

        if 'quiver_scale' in self.data_object.attrs:
            quiver_scale = self.data_object.attrs['quiver_scale']
        else:
            quiver_scale = None
        
        if 'quiver_width' in self.data_object.attrs:
            quiver_width = self.data_object.attrs['quiver_width']
        else:
            quiver_width = 0.15
        
        if 'quiver_color' in self.data_object.attrs:
            quiver_color = self.data_object.attrs['quiver_color']
        else:
            quiver_color = 'white'

        self._quiver_object = self.image_ax.quiver(
            coord_i,
            coord_j,
            vec_i,
            vec_j,
            units = 'xy',
            scale = quiver_scale,
            width = quiver_width,
            angles = 'xy',
            pivot = 'mid',
            color = quiver_color,
        )

        self.image_blit_manager['quiver'] = self._quiver_object
        

    def setBackground(self, background_path: str):
        """
        Set the background path in HDF5 file, to show the background image.

        Will set the background_path attribute. The background image must be
        a 2D matrix, RGB images (3 channels) are not supported here.

        The background image's shape must be equal to one of the channel of
        the vector field. For example, if the shape of the vector field is 
            2 x 256 x 256
        the shape of the background image must be 256 x 256 then.

        arguments:
            background_path: (str) the path of the image or data.

        raises:
            TypeError, KeyError, ValueError
        """
        if not isinstance(background_path, str):
            raise TypeError('background_path must be a str, not '
                '{0}'.format(type(background_path).__name__))

        background_node = self.hdf_handler.getNode(background_path)
        # May raise KeyError if the path does not exist
        if not isinstance(background_node, HDFDataNode):
            raise ValueError('Item {0} must be a '
                'Dataset'.format(background_path))
        
        background_data_obj = self.hdf_handler.file[background_path]
        if not len(background_data_obj.shape) == 2:
            raise ValueError('Data must be a 2D matrix (single channel image)')

        if self.data_path == '':
            raise ValueError('Must set vector field before set background')
        _, height, width = self.data_object.shape 
        if (background_data_obj.shape[0] != height 
                or background_data_obj.shape[1] != width):
            raise ValueError('The background image\'s shape must be equal to'
                ' one of the channel of the vector field.')
        
        self._background_path = background_path
        self.ui.lineEdit_background_path.setText(self.background_path)

        self._createBackgroundImage()
        self._createColorbar()
        
        self.background_canvas.draw()
        self.background_canvas.flush_events()
        self.image_canvas.draw()
        self.image_canvas.flush_events()

    def _createBackgroundImage(self):
        """
        Create the axes and images of the background images.

        TODO: read and save attributes, like norm, cmap, alpha, etc.
        """
        if self._background_object in self.background_ax.images:
            # clear current objects in the axes
            _index = self.background_ax.images.index(self._background_object)
            self.background_ax.images.pop(_index)

        self._background_object = self.background_ax.imshow(
            self.hdf_handler.file[self.background_path]
        )
        self.background_blit_manager['background_image'] = self._background_object

        if self._image_object in self.image_ax.images:
            # clear current objects in the axes
            _index = self.image_ax.images.index(self._image_object)
            self.image_ax.images.pop(_index)
        
        self._image_object = self.image_ax.imshow(
            self.hdf_handler.file[self.background_path]
        )
        self._image_object.set_visible(self.background_visible)
        self.image_blit_manager['image'] = self._image_object 


    def _createColorbar(self):
        """
        Create the colorbar according to the background image.
        """
        if self._colorbar_object is None:
            self._colorbar_object = Colorbar(
                ax = self.colorbar_ax,
                mappable = self.background_object
            )
        else:
            self.colorbar_object.update_normal(self.background_object)

    def _initUi(self):
        """
        Initialize UI.
        """
        self.ui.checkBox_background_visible.setChecked(False)
        self.ui.checkBox_background_visible.stateChanged.connect(
            self._setImageVisible
        )
    
        self.ui.pushButton_browse.clicked.connect(
            self._browse
        )
        self.ui.pushButton_browse_background.clicked.connect(
            self._browseBackground
        )

    def _browse(self):
        """
        Open a dialog to browse which vector field to be opened.
        """
        dialog = DialogHDFChoose(self)
        dialog_code = dialog.exec()
        if dialog_code == dialog.Accepted:
            current_path = dialog.getCurrentPath()
        else:
            return 

        try:
            self.setVectorField(current_path)
        except (KeyError, ValueError, TypeError,) as e:
            self.logger.error('{0}'.format(e), exc_info = True)
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Cannot open this data: {0}'.format(e))
            msg.exec()

    def _browseBackground(self):
        """
        Open a dialog to browse which image to be opened as the background.
        """
        dialog = DialogHDFChoose(self)
        dialog_code = dialog.exec()
        if dialog_code == dialog.Accepted:
            current_path = dialog.getCurrentPath()
        else:
            return 

        try:
            self.setBackground(current_path)
        except (KeyError, ValueError, TypeError,) as e:
            self.logger.error('{0}'.format(e), exc_info = True)
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Cannot open this data: {0}'.format(e))
            msg.exec()

    def _setImageVisible(self):
        """
        Set whether the background image to be visible or not. 
        """
        self.image_object.set_visible(self.background_visible)
        self.image_blit_manager.update()

    def _createNewBackground(self):
        """
        Create a new background image.

        In default, it will be /.../[vector name]_bkgrd.img . If there has been
        a background at this path, try to use it. Otherwise, add an index and 
        try again: /.../[vector name]_bkgrd_1.img . The new path will be under
        the same group as the vector field.

        Users can calculate a new background and reset it themselves. 

        returns:
            (str) the path of the new background image.
        """
        
        # Get a valid new name of the new background image
        data_node = self.hdf_handler.getNode(self.data_path)
        if '.' in data_node.name:
            name_array = data_node.name.split('.').pop()
            original_name = '.'.join(name_array)
        else:
            original_name = data_node.name 

        bkgrd_name = original_name + '_bkgrd.img'
        _count = 0
        while bkgrd_name in data_node.parent:
            _count += 1
            bkgrd_name = original_name + '_bkgrd_{0}.img'.format(_count)
        
        # Get the shape of the new background image
        _, height, width = self.data_object.shape 
        
        self.hdf_handler.addNewData( 
            parent_path = data_node.parent.path, 
            name = bkgrd_name, 
            shape = (height, width), 
            dtype = 'float64',
        )

        # Get the path of the new background image
        if data_node.parent.path == '/':
            bkgrd_path = '/' + bkgrd_name 
        else:
            bkgrd_path = data_node.parent.path + '/' + bkgrd_name

        self.data_object.attrs['background_path'] = bkgrd_path

        return bkgrd_path
        