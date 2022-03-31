# -*- coding: utf-8 -*-

"""
*-------------------------- PageViewFourDSTEM.py -----------------------------*
显示 4D-STEM 数据的页面。

部件内容：
    - WidgetPlotDP 用于使用 matplotlib 显示衍射图样
    - WidgetPlotPreview 用于使用 matplotlib 显示实空间预览图

提升部件：
    - 提升类名 PageViewFourDSTEM
    - 头文件 bin.Widgets.PageViewFourDSTEM

作者:           胡一鸣
创建日期:       2022年3月30日

The GUI page to view 4D-STEM dataset.

Contents:
    - WidgetPlotDP, to view the diffraction patterns
    - WidgetPlotPreview, to view the real-space preview image

Promoted Widget:
    - name of widget class: PageViewFourDSTEM
    - header file: bin.Widget.PageViewFourDSTEM

author:         Hu Yiming
date:           Mar 30, 2022
*-------------------------- PageViewFourDSTEM.py -----------------------------*
"""

from logging import Logger
from typing import List, Tuple

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer
from matplotlib.backend_bases import MouseEvent
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.colorbar import Colorbar, make_axes
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.image import AxesImage
from matplotlib.axis import Axis
from matplotlib.lines import Line2D
# from matplotlib.patches import Circle
import numpy as np
import h5py

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFDataNode, HDFGroupNode, HDFHandler
from ui import uiPageViewFourDSTEM

class PageViewFourDSTEM(QWidget):
    """
    显示 4D-STEM 数据集的部件类。

    Ui 文件地址：ROOTPATH/ui/uiPageViewFourDSTEM

    Widget to show 4D-STEM dataset.

    The path of the ui file: ROOTPATH/ui/uiPageViewFourDSTEM

    attributes:

    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageViewFourDSTEM.Ui_Form()
        self.ui.setupUi(self)

        self._data_path = ''
        self._preview_path = ''
        self._dp_ax = None
        self._colorbar_ax = None
        self._preview_ax = None
        self._dp_object = None
        self._colorbar_object = None
        self._preview_object = None
        self._preview_hcursor_object = None
        self._preview_vcursor_object = None
        self._tracking = False
        self._scan_ii = 0
        self._scan_jj = 0
        

        self._initUI()
        

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
    def preview_path(self) -> str:
        return self._preview_path

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    @property
    def dp_canvas(self) -> FigureCanvas:
        return self.ui.widget_dp.canvas

    @property
    def preview_canvas(self) -> FigureCanvas:
        return self.ui.widget_preview.canvas

    @property
    def dp_figure(self) -> Figure:
        return self.ui.widget_dp.figure

    @property
    def preview_figure(self) -> Figure:
        return self.ui.widget_preview.figure

    @property
    def dp_ax(self) -> Axes:
        return self._dp_ax

    @property
    def preview_ax(self) -> Axes:
        return self._preview_ax

    @property
    def colorbar_ax(self) -> Axes:
        return self._colorbar_ax

    @property
    def dp_object(self) -> AxesImage:
        return self._dp_object

    @property
    def preview_object(self) -> AxesImage:
        return self._preview_object

    @property
    def colorbar_object(self) -> AxesImage:
        return self._colorbar_object

    @property
    def preview_hcursor_object(self) -> Line2D:
        return self._preview_hcursor_object

    @property
    def preview_vcursor_object(self) -> Line2D:
        return self._preview_vcursor_object

    @property
    def dp_blit_manager(self) -> BlitManager:
        return self.ui.widget_dp.blit_manager

    @property
    def preview_blit_manager(self) -> BlitManager:
        return self.ui.widget_preview.blit_manager

    @property
    def scan_ii(self) -> int:
        return self._scan_ii

    @property
    def scan_jj(self) -> int:
        return self._scan_jj

    def setFourDSTEM(self, data_path: str):
        """
        Set the data path in HDF5 file, to show the image.

        Will set the data_path attribute. The FourDSTEM must be a 4D matrix.

        arguments:
            data_path: (str) the path of the image or data.

        raises:
            TypeError, KeyError, ValueError
        """
        if not isinstance(data_path, str):
            raise TypeError('data_path must be a str, not '
                '{0}'.format(type(data_path).__name__))

        data_node = self.hdf_handler.getNode(data_path)
        # May raise KeyError is the path does not exist
        if not isinstance(data_node, HDFDataNode):
            raise ValueError('Item {0} must be a Dataset'.format(data_path))
        
        data_obj = self.hdf_handler.file[data_path]
        if not len(data_obj.shape) == 4:
            raise ValueError('Data must be a 4D matrix (4D-STEM dataset)')

        self._data_path = data_path
        self.ui.lineEdit_data_path.setText(self.data_path)
        self.setWindowTitle('{0} - 4D-STEM'.format(data_node.name))

        self._createAxes()
        self._createDP()

        self.ui.spinBox_scan_ii.setValue(0)
        self.ui.spinBox_scan_jj.setValue(0)
        self.ui.spinBox_scan_ii.setMaximum(data_obj.shape[0])
        self.ui.spinBox_scan_jj.setMaximum(data_obj.shape[1])
        
        if 'preview_path' in self.data_object.attrs:
            preview_path = self.data_object.attrs['preview_path']
            try:
                self.setPreview(preview_path)
            except (KeyError, ValueError, TypeError):
                new_preview_path = self._createNewPreview()
                self.setPreview(new_preview_path)
        else:
            new_preview_path = self._createNewPreview()
            self.setPreview(new_preview_path)

        # connect

    def _createAxes(self):
        """
        Create the axes that contains the image and the colorbar respectively.
        """
        if self._dp_ax is None:
            self._dp_ax = self.dp_figure.add_subplot()
        if self._colorbar_ax is None:
            self._colorbar_ax, _kw = make_axes(
                self.dp_ax,
                location = 'right',
                orientation = 'vertical',
            )
            self._colorbar_ax.xaxis.set_visible(False)
            self._colorbar_ax.yaxis.tick_right()

    def _createDP(self):
        """
        Read the dp and the FourDSTEM attributes, and show it.

        TODO: read and save attributes, like norm, cmap, alpha, etc.
        """
        if self.dp_object is None:
            self._dp_object = self.dp_ax.imshow(self.data_object[0,0,:,:])
            self.dp_blit_manager.addArtist(self._dp_object)
            self.dp_canvas.draw()
            self.dp_canvas.flush_events()
        else:
            self.dp_object.set_data(self.data_object[0,0,:,:])
            self.dp_blit_manager.update()
    
    def setPreview(self, preview_path: str):
        """
        Set the preview path in HDF5 file, to show the preview image.

        Will set the preview_path attribute. The preview image must be a 2D
        matrix, RGB images (3 channels) are not supported here.

        The preview image's shape must be equal to the first two dimensions of 
        the 4D-STEM dataset. For example, if the shape of 4D-STEM dataset is 
            256 x 256 x 128 x 128
        where there are 256 x 256 diffraction patterns (scanning points) and 
        every diffraction pattern has 128 x 128 pixels, the shape of preview 
        image must be 256 x 256, i.e. the scanning shape.

        arguments:
            preview_path: (str) the path of the image or data.

        raises:
            TypeError, KeyError, ValueError
        """
        if not isinstance(preview_path, str):
            raise TypeError('preview_path must be a str, not '
                '{0}'.format(type(preview_path).__name__))

        preview_node = self.hdf_handler.getNode(preview_path)
        # May raise KeyError if the path does not exist
        if not isinstance(preview_node, HDFDataNode):
            raise ValueError('Item {0} must be a Dataset'.format(preview_path))
        
        preview_data_obj = self.hdf_handler.file[preview_path]
        if not len(preview_data_obj.shape) == 2:
            raise ValueError('Data must be a 2D matrix (single channel image)')

        if self.data_path == '':
            raise ValueError('Must set 4D-STEM dataset before set previewing')
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape
        if (preview_data_obj.shape[0] != scan_i 
                or preview_data_obj.shape[1] != scan_j):
            raise ValueError('The preview image\'s shape must be equal to the'
                'first two dimensions of the 4D-STEM dataset.')
        
        self._preview_path = preview_path
        self.ui.lineEdit_preview_path.setText(self.preview_path)
        
        self._createPreviewImage()
        self._createPreviewCursor()

    def _createPreviewImage(self):
        """
        Create the axes and image of the preview images.

        TODO: read and save attributes, like norm, cmap, alpha, etc.
        """
        if self._preview_ax is None:
            self._preview_ax = self.preview_figure.add_subplot()
        if self.preview_object is None:
            self._preview_object = self.preview_ax.imshow(
                self.hdf_handler.file[self.preview_path]
            )
            self.preview_blit_manager.addArtist(self._preview_object)
            self.preview_canvas.draw()
            self.preview_canvas.flush_events()
        else:
            self.preview_object.set_data(
                self.hdf_handler.file[self.preview_path]
            )
            self.preview_blit_manager.update()

    def _createPreviewCursor(self):
        """
        Create cursors on the preview image, to show where the current DP on 
        the real space is.
        """
        if self.preview_hcursor_object is None:
            self._preview_hcursor_object = self.preview_ax.axhline(
                y = self.scan_ii,
                color = 'black',
                linewidth = 1,
            )
            self.preview_blit_manager.addArtist(self.preview_hcursor_object)
        else:
            self.preview_hcursor_object.set_ydata(
                self.scan_ii
            )
            self.preview_blit_manager.update()

        if self.preview_vcursor_object is None:
            self._preview_vcursor_object = self.preview_ax.axvline(
                x = self.scan_jj,
                color = 'black',
                linewidth = 1,
            )
            self.preview_blit_manager.addArtist(self.preview_vcursor_object)
        else:
            self.preview_hcursor_object.set_xdata(
                self.scan_jj
            )
            self.preview_blit_manager.update()

        self.preview_canvas.draw()
        self.preview_canvas.flush_events()
        
    def _initUI(self):
        """
        Initialize UIs
        """
        self.ui.lineEdit_data_path.setReadOnly(True)
        self.ui.lineEdit_preview_path.setReadOnly(True)
        self.ui.spinBox_scan_ii.setMinimum(0)
        self.ui.spinBox_scan_jj.setMinimum(0)
        self.ui.spinBox_scan_ii.valueChanged.connect(self._updateDPBySpinBoxI)
        self.ui.spinBox_scan_jj.valueChanged.connect(self._updateDPBySpinBoxJ)

        self._cid_press = self.preview_canvas.mpl_connect(
            'button_press_event',       # When button pressed in preview, 
            self._startTrackingPreview  # start tracking the mouse location
        )                               # and update DP for the location
        self._cid_move = self.preview_canvas.mpl_connect(
            'motion_notify_event',      # update DP for the location
            self._updateDPByMouseMotion # NOTE: do NOT push mouse for a 
        )                               # long time!

        self._cid_release = self.preview_canvas.mpl_connect(
            'button_release_event',     # End tracking the mouse location
            self._endTrackingPreview    # when the button is released.
        )
        self._cid_leave = self.preview_canvas.mpl_connect(
            'axes_leave_event',         # End tracking the mouse location
            self._endTrackingPreview    # when the button leaves preview.
        )
        

    def _updateDP(self):
        """
        Update the current diffraction pattern according to the location in 
        the real space (in preview or in spinBoxes).
        """
        if self.data_object is None:
            return None

        scan_i, scan_j, dp_i, dp_j = self.data_object.shape
        scan_ii = max(0, min(scan_i, self.scan_ii)) # Avoid out of boundary
        scan_jj = max(0, min(scan_j, self.scan_jj))
        
        self.dp_object.set_data(
            self.data_object[scan_ii, scan_jj, :, :]
        )
        self.dp_blit_manager.update()     

        self.preview_hcursor_object.set_ydata(scan_ii)
        self.preview_vcursor_object.set_xdata(scan_jj)
        self.preview_blit_manager.update()
    
    def _updateDPBySpinBoxI(self):
        self._scan_ii = self.ui.spinBox_scan_ii.value()
        # self._scan_jj = self.ui.spinBox_scan_jj.value()
        self._updateDP()
    
    def _updateDPBySpinBoxJ(self):
        self._scan_jj = self.ui.spinBox_scan_jj.value()
        self._updateDP()

    def _updateDPByMouseMotion(self, event: MouseEvent):
        """
        Set the DP when the mouse is clicked on the preview.

        arguments:
            event: MouseEvent
        """
        if not self._tracking:
            return None
        # scan_i, scan_j, dp_i, dp_j = self.data_object.shape
        if not event.ydata is None:
            self._scan_ii = int(event.ydata)
        if not event.xdata is None:
            self._scan_jj = int(event.xdata)

        self._updateDP()

    def _startTrackingPreview(self, event: MouseEvent):
        """
        Start the tracking preview when the mouse is clicked on the preview.

        arguments:
            event: (MouseEvent)
        """
        self._tracking = True
        self._updateDPByMouseMotion(event)
        

    def _endTrackingPreview(self, event: MouseEvent):
        """
        End the tracking preview when the mouse is released.

        arguments:
            event: (MouseEvent)
        """
        self._updateDPByMouseMotion(event)
        self._tracking = False 
        self.ui.spinBox_scan_ii.setValue(self.scan_ii)
        self.ui.spinBox_scan_jj.setValue(self.scan_jj)

    def _createNewPreview(self) -> str:
        """
        Create a new preview image.

        In default, it will be /.../[4D-STEM name]_preview . If there has been
        a preview at this path, try to use it. Otherwise, add an index and try
        again: /.../[4D-STEM name]_preview_1. The new path will be under the 
        same group as the 4D-STEM dataset.

        I cannot find a quick way to calculate a new preview image for now, so 
        the preview image is set to be a zero matrix. Users can calculate a new
        preview image and reset it themselves.

        returns:
            (str) the path of the new preview.
        """
        
        data_node = self.hdf_handler.getNode(self.data_path)
        preview_name = data_node.name + '_preview'
        _count = 0
        while preview_name in data_node.parent:
            _count += 1
            preview_name = data_node.name + '_preview_{0}'.format(_count)
        if data_node.parent.path == '/':
            preview_path = '/' + preview_name
        else:
            preview_path = data_node.parent.path + '/' + preview_name

        self.data_object.attrs['preview_path'] = preview_path
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape
        # preview_data = self.data_object[:,:,int(dp_i/2),int(dp_j/2)]
        

        _index = self.hdf_handler.model.indexFromPath(self.data_path)
        self.hdf_handler.model.insertData(
            parent = _index.parent(),
            name = preview_name,
            shape = (scan_i, scan_j),
            dtype = 'float32',
        )   
        
        return preview_path

