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
from bin.Widgets.DialogCreateItem import DialogHDFCreate
from Constants import HDFType
from ui import uiPagePlotCTF

from lib.Probe import OpticalSTEM

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

        self.ui.lineEdit_config_path.setReadOnly(True)

        self._initUi()

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

    @property
    def ronchigram_data_object(self) -> h5py.Dataset:
        dummy = np.zeros((256,256))
        radius = 96
        for i in range(256):
            for j in range(256):
                if (i-128)**2 + (j-128)**2 < radius**2:
                    dummy[i,j] = 1         
        return dummy#self.hdf_handler.file[self._ronchigram_data_path]
    
    @property
    def probe_data_object(self) -> h5py.Dataset:
        optics = self._setOpticalSTEM()
        return optics.getProbe()#self.hdf_handler.file[self._probe_abs_data_path]
    
    @property
    def ctf_image_data_object(self) -> h5py.Dataset:
        return np.ones((1,1))#self.hdf_handler.file[self._ctf_image_data_path]
    
    def _updateConfigObject(self):
        """
        Update the config object based on the inputs.
        """
        config_object = self.config_object

        config_object.attrs["accelerate_voltage"] = self.ui.doubleSpinBox_voltage.value() * 1e3
        config_object.attrs["alpha"] = self.ui.doubleSpinBox_alpha.value() * 1e-3
        config_object.attrs["camera_length"] = self.ui.doubleSpinBox_camera_length.value() * 1e-3
        config_object.attrs["scan_step_size"] = self.ui.doubleSpinBox_scanning_step_size.value() * 1e-9
        config_object.attrs["detector_shape"] = [int(self.ui.comboBox_pixel_number.currentText()), int(self.ui.comboBox_pixel_number.currentText())]
        # estimate the real space pixel size from small angle approximation: dx = CL * full_detector_size / N
        config_object.attrs["detector_pixel_size"] = self.config_object.attrs["camera_length"] * self.ui.doubleSpinBox_full_detector_size.value() * 1e-3 / int(self.ui.comboBox_pixel_number.currentText())

        config_object.attrs["defocus"] = self.ui.doubleSpinBox_defocus.value() * 1e-9
        config_object.attrs["Cs"] = self.ui.doubleSpinBox_Cs.value() * 1e-3

    def _setOpticalSTEM(self):
        optics = OpticalSTEM(
            accelerate_voltage=self.config_object.attrs.get("/Acquisition/Microscope/accelerate_voltage", 200e3),
            alpha=self.config_object.attrs.get("/Acquisition/Microscope/convergence_angle", 12e-3),
            camera_length=self.config_object.attrs.get("/Acquisition/Microscope/camera_length", 8e-3),
            scan_step_size=self.config_object.attrs.get("/Calibration/Space/scan_dr_i", 5e-9),
            detector_shape=self.config_object.attrs.get("detector_shape", (256, 256)),
            detector_pixel_size=self.config_object.attrs.get("/Acquisition/Camera/pixel_size_i", 1e-10),
            defocus=self.config_object.attrs.get("/Aberration/C1", 100e-9),
            Cs=self.config_object.attrs.get("/Aberration/C3", 1e-3),
        )
        wavelength = optics.wave_length
        bright_field_disk_radius = optics.alpha * optics.dp_N * optics.dx / wavelength
        optics.setBrightFieldDiskRadius(bright_field_disk_radius)

        return optics
    
    def _initUi(self):
        """
        Initialise UI.
        """
        self.ui.pushButton_browse_probe.clicked.connect(self._browseProbe)

        self.ui.comboBox_pixel_number.setCurrentIndex(0)
        self.ui.doubleSpinBox_alpha.setValue(12.0)
        self.ui.doubleSpinBox_voltage.setValue(200.0)
        self.ui.doubleSpinBox_full_detector_size.setValue(25.0)
        self.ui.doubleSpinBox_scanning_step_size.setValue(5.0)
        self.ui.doubleSpinBox_camera_length.setValue(8.0)
        self.ui.label_dk.setText("1")
        self.ui.label_dx.setText("1")
        self.ui.label_object_size.setText("1")
        self.ui.label_reciprocal_space_size.setText("1")

        self.ui.doubleSpinBox_defocus.setValue(100.0)
        self.ui.doubleSpinBox_Cs.setValue(1.0)
        
        # Opens a new dialog to set higher order aberrations.
        self.ui.pushButton_set_aberrations

        self.ui.comboBox_image_modes.setCurrentIndex(0)
        self.ui.doubleSpinBox_abf_outer_radius.setValue(20.0)
        self.ui.doubleSpinBox_abf_inner_radius.setValue(10.0)

        self.ui.pushButton_save_config_path.clicked.connect(self._saveConfigPath)

        # self._updateConfigObject()
    
    def setFourDSTEM(self, data_path: str):
        """
        Set the config path in HDF5 file, and load the appropriate optical configurations.

        arguments:
            data_path: (str) the path of the image or data

        raise:
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
        
        self._config_path = data_path
        self.ui.lineEdit_config_path.setText(self._config_path)

        self._createAxes()
        self._createImages()
        self._createColorbar()


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

    def _createImages(self):
        """
        Read the images and its attributes, and show it.
        """
        if self._ronchigram_object in self.ronchigram_ax.images:
            self._ronchigram_object.remove()

        ronchigram_min = np.min(self.ronchigram_data_object)
        ronchigram_max = np.max(self.ronchigram_data_object)
        self._ronchigram_object = self.ronchigram_ax.imshow(
            self.ronchigram_data_object,
            vmin=ronchigram_min,
            vmax=ronchigram_max,
        )
        self.ronchigram_blit_manager['image'] = self._ronchigram_object

        if self._probe_abs_object in self.probe_abs_ax.images:
            self._probe_abs_object.remove()

        probe_abs_data_object = np.abs(self.probe_data_object)
        probe_abs_min = np.min(probe_abs_data_object)
        probe_abs_max = np.max(probe_abs_data_object)
        self._probe_abs_object = self.probe_abs_ax.imshow(
            probe_abs_data_object,
            vmin=probe_abs_min,
            vmax=probe_abs_max,
        )
        self.probe_abs_blit_manager['image'] = self._probe_abs_object

        if self._probe_angle_object in self.probe_angle_ax.images:
            self._probe_angle_object.remove()

        probe_angle_data_object = np.angle(self.probe_data_object)
        probe_angle_min = np.min(probe_angle_data_object)
        probe_angle_max = np.max(probe_angle_data_object)
        self._probe_angle_object = self.probe_angle_ax.imshow(
            probe_angle_data_object,
            vmin=probe_angle_min,
            vmax=probe_angle_max,
        )
        self.probe_angle_blit_manager['image'] = self._probe_angle_object

        if self._ctf_image_object in self.ctf_image_ax.images:
            self._ctf_image_object.remove()

        ctf_image_min = np.min(self.ctf_image_data_object)
        ctf_image_max = np.max(self.ctf_image_data_object)
        self._ctf_image_object = self.ctf_image_ax.imshow(
            self.ctf_image_data_object,
            vmin=ctf_image_min,
            vmax=ctf_image_max,
        )
        self.ctf_image_blit_manager['image'] = self._ctf_image_object

    def _createColorbar(self):
        """
        Create the colorbar according to the image.
        """
        if self._ronchigram_colorbar_object is None:
            self._ronchigram_colorbar_object = Colorbar(
                ax=self._ronchigram_colorbar_ax,
                mappable=self._ronchigram_object,
            )

        else:
            self._ronchigram_colorbar_object.update_normal(self._ronchigram_object)

        if self._probe_abs_colorbar_object is None:
            self._probe_abs_colorbar_object = Colorbar(
                ax=self._probe_abs_colorbar_ax,
                mappable=self._probe_abs_object,
            )

        else:
            self._probe_abs_colorbar_object.update_normal(self._probe_abs_object)

        if self._probe_angle_colorbar_object is None:
            self._probe_angle_colorbar_object = Colorbar(
                ax=self._probe_angle_colorbar_ax,
                mappable=self._probe_angle_object,
            )

        else:
            self._probe_angle_colorbar_object.update_normal(self._probe_angle_object)

        if self._ctf_image_colorbar_object is None:
            self._ctf_image_colorbar_object = Colorbar(
                ax=self._ctf_image_colorbar_ax,
                mappable=self._ctf_image_object,
            )

        else:
            self._ctf_image_colorbar_object.update_normal(self._ctf_image_object)

    def _browseProbe(self):
        """
        Browse the probe data.
        """
        dialog = DialogHDFChoose(self)
        dialog_code = dialog.exec()
        if dialog_code == dialog.accepted:
            current_path = dialog.getCurrentPath()
        else:
            return 

        try:
            self._config_path = current_path
        except (KeyError, ValueError, TypeError,) as e:
            self.logger.error('{0}'.format(e), exc_info=True)
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Cannot open this configuration: {0}'.format(e))
            msg.exec()

    def _saveConfigPath(self):
        """
        Save the config path in the HDF5 file.
        """
        dialog_create = DialogHDFCreate()
        dialog_create.initNames()
        dialog_code = dialog_create.exec()
        if not dialog_code == dialog_create.accepted:
            return 
        item_type = dialog_create.getItemType()
        parent_path = dialog_create.getParentPath()
        name = dialog_create.getName()
        model = self.hdf_handler.model
        parent_index = model.indexFromPath(parent_path)
        # TO DO: Need to specialise to the config storage format.
        try:
            if item_type == HDFType.Group:
                model.insertGroup(parent_index, name) 
            elif item_type == HDFType.Data:
                shape = dialog_create.getShape()
                dtype = dialog_create.getDType()
                model.insertData(
                    parent = parent_index, 
                    name = name,
                    shape = shape,
                    dtype = dtype,
                ) 
        except (ValueError, KeyError) as e:
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Fail to create: {0}'.format(e))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return False

    # def setOpticalConfig(self, config_path: str):
    #     """
    #     Set the config path in HDF5 file, to show the CTF.

    #     Will set the config_path attribute. 

    #     arguments:
    #         config_path: (str) the path of the optical config data.

    #     raises:
    #         TypeError, KeyError, ValueError
    #     """
    #     if not isinstance(config_path, str):
    #         raise TypeError("config_path must be a str, not"
    #             "{0}".format(type(config_path).__name__))
        
    #     config_node = self.hdf_handler.getNode(config_path)
    #     # May raise KeyError if the path does not exist
    #     if not isinstance(config_node, HDFDataNode):
    #         raise ValueError("Item {0} must be a Dataset".format(config_path))
        
    #     config_obj = self.hdf_handler.file[config_path]
        
    #     self._config_path = config_path 
    #     self.ui.lineEdit_config_path.setText(self.config_path)
    #     self.setWindowTitle("{0} - CTF".format(config_node.name))

        #TODO read the 4D-STEM optical configuration and render the images

    # def 
    ########################
    # 进一步的代码编写需要先完善以下工作：
    #   - 调整、完善关于 4D-STEM 的实验参数的记录
    #   - 添加对于 .ctf 类型数据的支持 (于 HDFManager 中)
    #   - 构建 Calculator 类以及 OpticalConfig 类，用于得到 CTF 数据

# import sys
# from bin.app import App
# if __name__ == '__main__':
#     app = App(sys.argv)
#     app.startBackEnds()
#     ex = PagePlotCTF()
#     ex.show()
#     sys.exit(app.exec())



