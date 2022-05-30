# -*- coding: utf-8 -*-

"""
*-------------------------- PageBaseFourDSTEM.py -----------------------------*
显示 4D-STEM 数据页面的基类。

部件内容：
    - WidgetPlotDP 用于使用 matplotlib 显示衍射图样

提升部件：
    None

作者:           胡一鸣
创建日期:       2022年4月8日

The base class to view 4D-STEM dataset.

Contents:
    - WidgetPlotDP, to view the diffraction patterns by matplotlib.

Promoted Widget:
    None

author:         Hu Yiming
date:           Apr 8, 2022
*-------------------------- PageBaseFourDSTEM.py -----------------------------*
"""

from logging import Logger

from PySide6.QtWidgets import QWidget, QMessageBox

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.colorbar import Colorbar, make_axes
from matplotlib.colors import Normalize, SymLogNorm
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.image import AxesImage
from matplotlib.axis import Axis

import numpy as np
import h5py

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFDataNode, HDFGroupNode, HDFHandler
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from ui import uiPageBaseFourDSTEM

class PageBaseFourDSTEM(QWidget):
    """
    显示 4D-STEM 数据集的部件的基类。包含以下功能：
        - 根据行、列显示对应的衍射图样
        - 绘制颜色条
        - 调整亮度、衬度、标尺类型、颜色图类型

    Ui 文件地址：ROOTPATH/ui/uiPageBaseFourDSTEM

    注意，这个类只是抽象地提供预览 4D-STEM 的功能。要使用此类，应当自己构建独立的 
    .ui 文件及对应的 .py 文件，并确保子类与父类相同的控件的名字一致。这个类不提供
    实际的渲染，只提供控件之间的逻辑链接。

    The base class of the widgets to show 4D-STEM dataset, including:
        - show diffraction patterns according to i,j index
        - draw colorbars
        - adjust brightness, contrast, norm and colormap.

    The path of the ui file: ROOTPATH/ui/uiPageBaseFourDSTEM

    NOTE: This class provides methods to preview 4D-STEM abstractly. To use
    this class, we should construct .ui file and .py file ourselves, and ensure
    widgets' names are the same as the parent class. This class cannot be used
    to show 4D-STEM directly, but only provides logic connects between widgets.

    attributes:
        hdf_handler: (HDFHandler) The handler to manage the hdf file and the 
            objects inside it.

        data_object: (h5py.Dataset) The data object of 4D-STEM data.

        data_path: (str) The path of the data object.

        logger: (Logger) Use logger to record information.

        dp_canvas: (FigureCanvas) The canvas (widget) object to show 
            Diffraction patterns.

        dp_figure: (Figure) The Figure object of the diffraction patterns.

        dp_ax: (Axes) The Axes object of the diffraction patterns.

        colorbar_ax: (Axes) The Axes object of the colorbar.

        dp_object: (AxesImage) The image object of the diffraction patterns.

        colorbar_object: (Colorbar) The Colorbar object. This colorbar is atta-
            ched to the diffraction patterns.

        dp_blit_manager: (BlitManager) The blit manager of the diffraction 
            patterns. When the data, norm, colormap or other attributes of the 
            diffraction pattern change, use its update() method to plot the 
            updated images.

        scan_ii: (int) The i-coordinate of the current diffraction pattern in 
            the real space. This is also regarded as the row index in a matrix.

        scan_jj: (int) The j-coordinate of the current diffraction pattern in
            the real space. This is also regarded as the column index in a 
            matrix.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageBaseFourDSTEM.Ui_Form()

        self._data_path = ''
        self._dp_ax = None
        self._colorbar_ax = None
        self._dp_object = None
        self._colorbar_object = None
        self._scan_ii = 0
        self._scan_jj = 0

        # self._initBaseUi()
        

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
    def dp_canvas(self) -> FigureCanvas:
        return self.ui.widget_dp.canvas

    @property
    def dp_figure(self) -> Figure:
        return self.ui.widget_dp.figure

    @property
    def dp_ax(self) -> Axes:
        return self._dp_ax

    @property
    def colorbar_ax(self) -> Axes:
        return self._colorbar_ax

    @property
    def dp_object(self) -> AxesImage:
        return self._dp_object

    @property
    def colorbar_object(self) -> Colorbar:
        return self._colorbar_object

    @property
    def dp_blit_manager(self) -> BlitManager:
        return self.ui.widget_dp.blit_manager

    @property
    def scan_ii(self) -> int:
        return self._scan_ii

    @property
    def scan_jj(self) -> int:
        return self._scan_jj

    def _initBaseUi(self):
        """
        Initialize Uis.
        """
        self.ui.lineEdit_data_path.setReadOnly(True)
        self.ui.spinBox_scan_ii.setMinimum(0)
        self.ui.spinBox_scan_jj.setMinimum(0)
        self.ui.spinBox_scan_ii.valueChanged.connect(self._updateDPBySpinBoxI)
        self.ui.spinBox_scan_jj.valueChanged.connect(self._updateDPBySpinBoxJ)

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
        
        self.ui.comboBox_colormap.setCurrentIndex(0)
        self.ui.comboBox_colormap.currentIndexChanged.connect(
            self._changeColormap
        )
        self.ui.comboBox_normalize.setCurrentIndex(0)
        self.ui.comboBox_normalize.currentIndexChanged.connect(
            self._changeNorm
        )
        
        self.ui.pushButton_browse.clicked.connect(self._browse)


    def setFourDSTEM(self, data_path: str):
        """
        Set the data path in HDF5 file, to show the 4D-STEM dataset.

        Will set the data_set attribute. the FourDSTEM must be a 4D matrix.

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
        
        # self._createAxes()
        self._createDP()
        self._createColorbar()

        self.ui.spinBox_scan_ii.setValue(0)
        self.ui.spinBox_scan_jj.setValue(0)
        self.ui.spinBox_scan_ii.setMaximum(data_obj.shape[0] - 1)
        self.ui.spinBox_scan_jj.setMaximum(data_obj.shape[1] - 1)

        self.dp_canvas.draw()
        self.dp_canvas.flush_events()


    def _createAxes(self):
        """
        Create the axes that contains the image and the colorbar respectively.
        """
        if self._dp_ax is None:
            self._dp_ax = self.dp_figure.add_subplot()
            self.dp_blit_manager.addArtist('dp_axes', self._dp_ax)
        if self._colorbar_ax is None:
            self._colorbar_ax, _kw = make_axes(
                self.dp_ax,
                location = 'right',
                orientation = 'vertical',
            )
            self._colorbar_ax.xaxis.set_visible(False)
            self._colorbar_ax.yaxis.tick_right()
            self.dp_blit_manager.addArtist('colorbar_axes', self._colorbar_ax)

    def _createDP(self):
        """
        Read the dp and the FourDSTEM attributes, and show it.

        TODO: read and save attributes, like norm, cmap, alpha, etc.
        """
        if self._dp_object in self.dp_ax.images:
            # clear dp objects in the axes.
            _index = self.dp_ax.images.index(self._dp_object)
            self.dp_ax.images.pop(_index)

        self._dp_object = self.dp_ax.imshow(
            self.data_object[0, 0, :, :]
        )
        self.dp_blit_manager['dp_image'] = self._dp_object
        

    def _createColorbar(self):
        """
        Create the colorbar according to the dp.
        """
        if self._colorbar_object is None:
            self._colorbar_object = Colorbar(
                ax = self.colorbar_ax,
                mappable = self.dp_object,
            )
        else:
            self.colorbar_object.update_normal(self.dp_object)

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
        self.colorbar_object.update_normal(self.dp_object)
        self.dp_blit_manager.update()     

    def _updateDPBySpinBoxI(self):
        self._scan_ii = self.ui.spinBox_scan_ii.value()
        # self._scan_jj = self.ui.spinBox_scan_jj.value()
        self._updateDP()
    
    def _updateDPBySpinBoxJ(self):
        self._scan_jj = self.ui.spinBox_scan_jj.value()
        self._updateDP()
    
    def _browse(self):
        """
        Open a dialog to browse which 4D-STEM to be opened.
        """
        dialog = DialogHDFChoose(self)
        dialog_code = dialog.exec()
        if dialog_code == dialog.Accepted:
            current_path = dialog.getCurrentPath()
        try:
            self.setFourDSTEM(current_path)
        except (KeyError, ValueError, TypeError,) as e:
            self.logger.error('{0}'.format(e), exc_info = True)
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Cannot open this data: {0}'.format(e))
            msg.exec()
        
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

        self.dp_object.set_norm(new_norm)
        self.dp_blit_manager.update()

        self.colorbar_object.update_normal(self.dp_object)  
        self.dp_blit_manager.update()

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
        
        self.dp_object.set_norm(new_norm)
        self.colorbar_object.update_normal(self.dp_object)   
        self.dp_blit_manager.update()

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

        # Do not use self.data_object[self.scan_ii, self.scan_jj, :, :], to
        # avoid calculate maximum and minimum of the data from the disk. 
        # Rather, the array here is saved in the dp_object in memory.
        hmin = float(np.min(self.dp_object.get_array()))   
        hmax = float(np.max(self.dp_object.get_array()))
        
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
        hmin = np.min(self.dp_object.get_array())   
        hmax = np.max(self.dp_object.get_array())
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
            
        self.dp_object.set_norm(new_norm)
        self.colorbar_object.update_normal(self.dp_object)
        self.dp_blit_manager.update()

    def _changeColormap(self, index: int):
        """
        Slots when current colormap is changed.

        Will change the diffraction pattern's AND the preview's colormaps.

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
            self.dp_object.set_cmap(cmap)
            self.colorbar_object.update_normal(self.dp_object)
            self.dp_blit_manager.update()
    

