# -*- coding: utf-8 -*- 

"""
*----------------------------- PagePlotCTF.py --------------------------------*
通过解析式计算 CTF 的页面。

部件内容：
    - WidgetPlotImage 用于使用 matplotlib 显示图像
    - WidgetPlotLine 用于使用 matplotlib 画线

提升部件
    - 提升类名 PagePlotCTF 
    - 头文件 bin.Widgets.PagePlotCTF

作者:           胡一鸣
创建日期:       2023年6月11日

The GUI page to plot calculated contrast transfer functions (CTF).

Contents:
    - WidgetPlotImage, to view the images by matplotlib
    - WidgetPlotLine, to view the lines by matplotlib

Promoted Widget:
    - name of widget class: PagePlotCTF
    - header file: bin.Widgets.PagePlotCTF

author:         Hu Yiming 
date:           Jun 11, 2023
*----------------------------- PagePlotCTF.py --------------------------------*
"""

from logging import Logger 
from PySide6.QtWidgets import QWidget 
from PySide6.QtWidgets import QMessageBox 
from PySide6.QtWidgets import QInputDialog 
from PySide6.QtWidgets import QDialog 

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure 
from matplotlib.axes import Axes 
from matplotlib.image import AxesImage 
from matplotlib.patches import Circle 
from matplotlib.patches import Annulus
from matplotlib.colorbar import Colorbar, make_axes 

import h5py 
import numpy as np 
from bin.BlitManager import BlitManager 
from bin.HDFManager import HDFDataNode, HDFHandler 
from bin.TaskManager import TaskManager
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from ui import uiPagePlotCTF

class PagePlotCTF(QWidget):
    """
    计算 CTF 的页面。

    Ui 文件地址：ROOT_PATH/ui/uiPagePlotCTF.ui

    Widget to view CTF.

    The path of the ui file: ROOT_PATH/ui/uiPagePlotCTF.ui
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPagePlotCTF.Ui_Form()
        self.ui.setupUi(self)

        self._config_path = ''
        self._ronchigram_ax = None 
        self._ronchigram_colorbar_ax = None 
        self._ronchigram_object = None 
        self._ronchigram_colorbar_object = None 
        self._probe_abs_ax = None
        self._probe_abs_colorbar_ax = None
        self._probe_abs_object = None  
        self._probe_abs_colorbar_object = None 
        self._probe_angle_ax = None  
        self._probe_angle_colorbar_ax = None 
        self._probe_angle_object = None 
        self._probe_angle_colorbar_object = None 
        self._ctf_image_ax = None 
        self._ctf_image_colorbar_ax = None 
        self._ctf_image_object = None 
        self._ctf_image_colorbar_object = None 

        self._ctf_line_ax = None 
        self._ctf_line_object = None 

        self.ui.lineEdit_config_path.setReadOnly()

        self._initUi()
        self._createAxes()

    @property 
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler 
    
    @property
    def config_object(self) -> h5py.Dataset:
        return self.hdf_handler.file[self._config_path]
    
    @property
    def config_path(self) -> str:
        return self._config_path 
    
    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger 
    
    @property
    def ronchigram_canvas(self) -> FigureCanvas:
        return self.ui.widget_plot_ronchigram.canvas 
    
    @property
    def ronchigram_figure(self) -> Figure:
        return self.ui.widget_plot_ronchigram.figure 
    
    @property
    def ronchigram_ax(self) -> Axes:
        return self._ronchigram_ax
    
    @property
    def ronchigram_object(self) -> AxesImage:
        return self._ronchigram_object
    
    @property
    def ronchigram_colorbar_ax(self) -> Axes:
        return self._ronchigram_colorbar_ax 
    
    @property
    def ronchigram_colorbar_object(self) -> Colorbar:
        return self._ronchigram_colorbar_object
    
    @property
    def ronchigram_blit_manager(self) -> BlitManager:
        return self.ui.widget_plot_ronchigram.blit_manager

    @property
    def probe_abs_canvas(self) -> FigureCanvas:
        return self.ui.widget_plot_probe_abs.canvas 
    
    @property
    def probe_abs_figure(self) -> Figure:
        return self.ui.widget_plot_probe_abs.figure 
    
    @property
    def probe_abs_ax(self) -> Axes:
        return self._probe_abs_ax
    
    @property
    def probe_abs_object(self) -> AxesImage:
        return self._probe_abs_object

    @property
    def probe_abs_colorbar_ax(self) -> Axes:
        return self._probe_abs_colorbar_ax 
    
    @property
    def probe_abs_colorbar_object(self) -> Colorbar:
        return self._probe_abs_colorbar_object
    
    @property
    def probe_abs_blit_manager(self) -> BlitManager:
        return self.ui.widget_plot_probe_abs.blit_manager

    @property
    def probe_angle_canvas(self) -> FigureCanvas:
        return self.ui.widget_plot_probe_angle.canvas 
    
    @property
    def probe_angle_figure(self) -> Figure:
        return self.ui.widget_plot_probe_angle.figure 
    
    @property
    def probe_angle_ax(self) -> Axes:
        return self._probe_angle_ax
    
    @property
    def probe_angle_object(self) -> AxesImage:
        return self._probe_angle_object
    
    @property
    def probe_angle_colorbar_ax(self) -> Axes:
        return self._probe_angle_colorbar_ax
    
    @property
    def probe_angle_colorbar_object(self) -> Colorbar:
        return self._probe_angle_colorbar_object
    
    @property
    def probe_angle_blit_manager(self) -> BlitManager:
        return self.ui.widget_plot_probe_angle.blit_manager

    @property
    def ctf_image_canvas(self) -> FigureCanvas:
        return self.ui.widget_plot_ctf_image.canvas 
    
    @property
    def ctf_image_figure(self) -> Figure:
        return self.ui.widget_plot_ctf_image.figure 
    
    @property
    def ctf_image_ax(self) -> Axes:
        return self._ctf_image_ax
    
    @property
    def ctf_image_object(self) -> AxesImage:
        return self._ctf_image_object 

    @property 
    def ctf_image_colorbar_ax(self) -> Axes:
        return self._ctf_image_colorbar_ax 
    
    @property
    def ctf_image_colorbar_object(self) -> Colorbar:
        return self._ctf_image_colorbar_object
    
    @property
    def ctf_image_blit_manager(self) -> BlitManager:
        return self.ui.widget_plot_ctf_image.blit_manager

    @property
    def ctf_line_canvas(self) -> FigureCanvas:
        return self.ui.widget_plot_ctf_curve.canvas 
    
    @property
    def ctf_line_figure(self) -> Figure:
        return self.ui.widget_plot_ctf_curve.figure 
    
    @property
    def ctf_line_ax(self) -> Axes:
        return self._ctf_line_ax
    
    @property
    def ctf_line_blit_manager(self) -> BlitManager:
        return self.ui.widget_plot_ctf_curve.blit_manager
    
    @property
    def task_manager(self) -> TaskManager:
        global qApp 
        return qApp.task_manager 
    
    def _createAxes(self):
        """
        Create the axes that contains images, colorbars, lines respectively.
        """

        if self._ronchigram_ax == None:
            self._ronchigram_ax = self.ronchigram_figure.add_subplot()
            self.ronchigram_blit_manager.addArtist('image_axes', self._ronchigram_ax)
        if self._ronchigram_colorbar_ax == None:
            self._ronchigram_colorbar_ax, _kw = make_axes(
                self.ronchigram_ax,
                location='right',
                orientation='vertical',
            )
            self._ronchigram_colorbar_ax.xaxis.set_visible(False)
            self._ronchigram_colorbar_ax.yaxis.tick_right()
            self.ronchigram_blit_manager['colorbar_axes'] = self._ronchigram_colorbar_ax
            

        if self._probe_abs_ax == None:
            self._probe_abs_ax = self.probe_abs_figure.add_subplot()
            self.probe_abs_blit_manager.addArtist('image_axes', self._probe_abs_ax)
        if self._probe_abs_colorbar_ax == None:
            self._probe_abs_colorbar_ax, _kw = make_axes(
                self.probe_abs_ax,
                location='right',
                orientation='vertical',
            )
            self._probe_abs_colorbar_ax.xaxis.set_visible(False)
            self._probe_abs_colorbar_ax.yaxis.tick_right()
            self.probe_abs_blit_manager['colorbar_axes'] = self._probe_abs_colorbar_ax

        if self._probe_angle_ax == None:
            self._probe_angle_ax = self.probe_angle_figure.add_subplot()
            self.probe_angle_blit_manager.addArtist('image_axes', self._probe_angle_ax)
        if self._probe_angle_colorbar_ax == None:
            self._probe_angle_colorbar_ax, _kw = make_axes(
                self.probe_angle_ax,
                location = 'right',
                orientation='vertical',
            )
            self._probe_angle_colorbar_ax.xaxis.set_visible(False)
            self._probe_angle_colorbar_ax.yaxis.tick_right()
            self.probe_angle_blit_manager['colorbar_axes'] = self._probe_angle_colorbar_ax

        if self._ctf_image_ax == None:
            self._ctf_image_ax = self.ctf_image_figure.add_subplot()
            self.ctf_image_blit_manager.addArtist('image_axes', self._ctf_image_ax) 
        if self._ctf_image_colorbar_ax == None:
            self._ctf_image_colorbar_ax, _kw = make_axes(
                self.ctf_image_ax,
                location = 'right',
                orientation = 'vertical',
            )
            self._ctf_image_colorbar_ax.xaxis.set_visible(False)
            self._ctf_image_colorbar_ax.yaxis.tick_right()
            self.ctf_image_blit_manager['colorbar_axes'] = self._ctf_image_colorbar_ax

        if self._ctf_line_ax == None:
            self._ctf_line_ax = self.ctf_line_figure.add_subplot()
            self.ctf_line_blit_manager.addArtist('line_axes', self._ctf_line_ax) 

    def setOpticalConfig(self, config_path: str):
        """
        Set the config path in HDF5 file, to show the CTF.

        Will set the config_path attribute. 

        arguments:
            config_path: (str) the path of the optical config data.

        raises:
            TypeError, KeyError, ValueError
        """
        if not isinstance(config_path, str):
            raise TypeError("config_path must be a str, not"
                "{0}".format(type(config_path).__name__))
        
        config_node = self.hdf_handler.getNode(config_path)
        # May raise KeyError if the path does not exist
        if not isinstance(config_node, HDFDataNode):
            raise ValueError("Item {0} must be a Dataset".format(config_path))
        
        config_obj = self.hdf_handler.file[config_path]
        
        self._config_path = config_path 
        self.ui.lineEdit_config_path.setText(self.config_path)
        self.setWindowTitle("{0} - CTF".format(config_node.name))

        #TODO read the 4D-STEM optical configuration and render the images

    # def 
    ########################
    # 进一步的代码编写需要先完善以下工作：
    #   - 调整、完善关于 4D-STEM 的实验参数的记录
    #   - 添加对于 .ctf 类型数据的支持 (于 HDFManager 中)
    #   - 构建 Calculator 类以及 OpticalConfig 类，用于得到 CTF 数据

    






