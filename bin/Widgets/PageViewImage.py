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
from matplotlib.colors import Normalize, SymLogNorm
import numpy as np
import h5py

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFDataNode, HDFHandler
from bin.Widgets.DialogChooseItem import DialogHDFChoose
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
        self._image_max = 0
        self._image_min = 0

        self.ui.lineEdit_image_path.setReadOnly(True)

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
        # May raise KeyError if the path does not exist
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
        self._createColorbar()

        self._image_max = np.max(data_obj)
        self._image_min = np.min(data_obj)

        self.image_canvas.draw()
        self.image_canvas.flush_events()


    def _createAxes(self):
        """
        Create the axes that contains the image and the colorbar respectively.
        """
        if self._image_ax is None:
            self._image_ax = self.image_figure.add_subplot()
            self.image_blit_manager.addArtist('image_axes', self._image_ax)
        if self._colorbar_ax is None:
            self._colorbar_ax, _kw = make_axes(
                self.image_ax,
                location = 'right',
                orientation = 'vertical',
            )
            self._colorbar_ax.xaxis.set_visible(False)
            self._colorbar_ax.yaxis.tick_right()

            # Here, we must add the colorbar axes to the blit manager, so 
            # that when the colorbar update mappables, the colorbar shown
            # on the screen will also be updated.
            self.image_blit_manager['colorbar_axes'] = self._colorbar_ax
        
    def _createImage(self):
        """
        Read the image and its attributes, and show it.

        TODO: read and save attributes, like norm, cmap, alpha, etc.
        """
        if self._image_object in self.image_ax.images:
            _index = self.image_ax.images.index(self._image_object)
            self.image_ax.images.pop(_index)
        
        self._image_object = self.image_ax.imshow(
            self.data_object
        )
        self.image_blit_manager['image'] = self._image_object
        
        self.ui.widget_hist_view.drawHist(self.data_object)
        
    def _createColorbar(self):
        """
        Create the colorbar according to the image.
        """
        if self._colorbar_object is None:
            self._colorbar_object = Colorbar(
                ax = self.colorbar_ax,
                mappable = self.image_object,
            )

        else:
            self.colorbar_object.update_normal(self.image_object)


    def _initUI(self):
        """
        Initialize UI
        """
        self.ui.horizontalSlider_brightness.setRange(0,99)
        self.ui.horizontalSlider_contrast.setRange(0,99)
        self.ui.horizontalSlider_brightness.setValue(50)
        self.ui.horizontalSlider_contrast.setValue(50)
        self.ui.horizontalSlider_brightness.valueChanged.connect(
            self._updateBrightness
        )
        self.ui.horizontalSlider_contrast.valueChanged.connect(
            self._updateContrast
        )
        
        self.ui.comboBox_normalize.setCurrentIndex(0)
        self.ui.comboBox_normalize.currentIndexChanged.connect(
            self._changeNorm
        )

        self.ui.comboBox_colormap.setCurrentIndex(0)
        self.ui.comboBox_colormap.currentIndexChanged.connect(
            self._changeColormap
        )

        self.ui.pushButton_browse.clicked.connect(
            self._browse
        )

    def _updateBrightness(self, brightness: int):
        """
        Set the brightness of the image.

        arguments:
            brightness: (int) the changed brightness value. (0-99)
        """
        contrast = self.ui.horizontalSlider_contrast.value()
        norm_type = self.ui.comboBox_normalize.currentIndex()
        if norm_type == 0:      # Linear
            new_norm = self._calcLinearNorm(brightness, contrast)
        elif norm_type == 1:    # Logarithm
            new_norm = self._calcLogarithmNorm(brightness, contrast)

        self.image_object.set_norm(new_norm)
        self.image_blit_manager.update()

        self.colorbar_object.update_normal(self.image_object)  
        self.image_blit_manager.update()

    def _updateContrast(self, contrast: int):
        """
        Set the contrast of the image.

        arguments:
            contrast: (int) the changed contrast value. (0-99)
        """
        brightness = self.ui.horizontalSlider_brightness.value()
        norm_type = self.ui.comboBox_normalize.currentIndex()
        if norm_type == 0:      # Linear
            new_norm = self._calcLinearNorm(brightness, contrast)
        elif norm_type == 1:    # Logarithm
            new_norm = self._calcLogarithmNorm(brightness, contrast)
        
        self.image_object.set_norm(new_norm)
        self.colorbar_object.update_normal(self.image_object)   
        self.image_blit_manager.update()
        
    def _calcLinearNorm(self, brightness: int, contrast: int) -> Normalize:
        """
        Calculate the linear normalization according to brightness and 
        contrast value.

        This linear normalization has following properties:
            - if brightness == 0: 
                vmax is set to the mimimum of the image, so the image looks 
                like a whole black canvas.
            - if brightness == 99:
                vmin is set to the maximum of the image, so the image looks
                like a whole white canvas.
            - if contrast == 0:
                vmin is set to (about) -infinite and vmax is set to (about) 
                +infinite, so the image looks like a whole gray canvas.
            - if contrast == 99:
                vmax and vmin is set to (minimum + maximum)/2 of the image,
                so the image looks like to be binarized (black and white).

        arguments:
            brightness: (int) must between 0 to 99

            contrast: (int) must between 0 to 99
        """
        brightness = max(0, min(99, brightness))
        contrast = max(0, min(99, contrast))

        slope = np.tan((1/2 - (contrast + 1)/100)*(np.pi/2) + np.pi/4)
        hmin = self._image_min
        hmax = self._image_max
        vmin_tmp = brightness/50*(hmin - hmax) + hmax
        vmax_tmp = brightness/50*(hmin - hmax) - hmin + 2*hmax
        vmin = (vmin_tmp + vmax_tmp)/2 + slope*(vmin_tmp - vmax_tmp)/2
        vmax = (vmax_tmp + vmin_tmp)/2 + slope*(vmax_tmp - vmin_tmp)/2
        return Normalize(vmin = vmin, vmax = vmax)
        
    def _calcLogarithmNorm(self, brightness: int, contrast: int):
        """
        Calculate the logarithm normalization according to the brightness
        and contrast.

        TODO: For now brightness and contrast do not work.

        arguments:  
            brightness: (int) must between 0 to 99

            contrast: (int) must between 0 to 99
        """
        brightness = max(0, min(99, brightness))
        contrast = max(0, min(99, contrast))
        hmin = self._image_min
        hmax = self._image_max

        return SymLogNorm(1, base = 2, vmin = hmin, vmax = hmax)

    def _changeNorm(self, index: int):
        """
        Slots when current normalization is changed.

        arguments:
            index: (int)    0       Linear
                            1       Logarithm
        """
        brightness = self.ui.horizontalSlider_brightness.value()
        contrast = self.ui.horizontalSlider_contrast.value()
        if index == 0:      # Linear
            new_norm = self._calcLinearNorm(brightness, contrast)
            
        elif index == 1:    # Logarithm
            new_norm = self._calcLogarithmNorm(brightness, contrast)
            
        self.image_object.set_norm(new_norm)
        self.colorbar_object.update_normal(self.image_object)
        self.image_blit_manager.update()
        

    def _changeColormap(self, index: int):
        """
        Slots when current colormap is changed.

        arguments:
            index: (int)    0       'viridis'
                            1       'plasma'
                            2       'gray'
                            3       'RdYlBu'
                            4       'twilight'
                            5       'hsv'
                            6       'jet'
                            7       'Others'
        """
        if index > 6:
            return None
        else:
            cmap = self.ui.comboBox_colormap.currentText()
            self.image_object.set_cmap(cmap)
            self.colorbar_object.update_normal(self.image_object)
            self.image_blit_manager.update()


    
    def _browse(self):
        """
        Open a dialog to browse which image to be opened.
        """
        dialog = DialogHDFChoose(self)
        dialog_code = dialog.exec()
        if dialog_code == dialog.Accepted:
            current_path = dialog.getCurrentPath()
        try:
            self.setImage(current_path)
        except (KeyError, ValueError, TypeError,) as e:
            self.logger.error('{0}'.format(e), exc_info=True)
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Cannot open this data: {0}'.format(e))
            msg.exec()



