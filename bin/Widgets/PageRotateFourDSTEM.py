# -*- coding: utf-8 -*-

"""
*-------------------------- PageRotateFourDSTEM.py ---------------------------*
对 4D-STEM 衍射图样进行旋转的界面。

部件内容：
    - WidgetPlotDP 用于使用 matplotlib 显示衍射图样
    - WidgetPlotQuiver 用于使用 matplotlib 显示预览矢量场图

提升部件：
    - 提升类名 PageRotateFourDSTEM.py
    - 头文件 bin.Widgets.PageRotateFourDSTEM

作者:           胡一鸣
创建日期:       2022年5月31日

The GUI page to rotate diffraction patterns.

Contents:
    - WidgetPlotDP, to view the diffraction patterns by matplotlib
    - WidgetPlotQuiver, to view the quiver plot of the vector field.

Promoted Widget:
    - name of widget class: PageRotateFourDSTEM
    - header file: bin.Widgets.PageRotateFourDSTEM

author:         Hu Yiming
date:           May 31, 2022
*-------------------------- PageRotateFourDSTEM.py ---------------------------*
"""

from PySide6.QtWidgets import QWidget, QDialog, QMessageBox 
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas
)
from matplotlib.figure import Figure 
from matplotlib.axes import Axes 
from matplotlib.lines import Line2D
from matplotlib.quiver import Quiver 
from matplotlib.transforms import Affine2D
import numpy as np
from scipy.ndimage import rotate

from bin.BlitManager import BlitManager 
from bin.TaskManager import TaskManager 
from bin.HDFManager import HDFDataNode
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.Widgets.DialogSaveFourDSTEM import DialogSaveFourDSTEM
from bin.Widgets.PageBaseFourDSTEM import PageBaseFourDSTEM
from bin.Widgets.PageViewVectorField import DialogAdjustQuiverEffect
from lib.TaskCalibration import TaskFourDSTEMRotate
from ui import uiPageRotateFourDSTEM

class PageRotateFourDSTEM(PageBaseFourDSTEM):
    """
    对 4D-STEM 衍射图样进行旋转操作的部件类。

    Ui 文件地址：ROOTPATH/ui/uiPageRotateFourDSTEM.ui

    Widget to rotate diffraction patterns of 4D-STEM dataset.

    The path of the ui file: ROOTPATH/ui/uiPageRotateFourDSTEM.ui

    attributes:
        
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageRotateFourDSTEM.Ui_Form()
        self.ui.setupUi(self)

        
        self._quiver_object = None 
        self._vec_data = None 
        self._vec_path = ''
        self._quiver_ax = None
        self._quiver_scale = 1
        self._quiver_width = 0.15
        self._quiver_color = 'black'
        self._createAxes()
        self._createQuiverAxes()
        self._initBaseUi()
        self._initUi()

    @property
    def rotate_angle(self) -> float:
        return self.ui.doubleSpinBox_rotation_angle.value()

    @property
    def task_manager(self) -> TaskManager:
        global qApp 
        return qApp.task_manager 
    
    @property
    def quiver_canvas(self) -> FigureCanvas:
        return self.ui.widget_vector_field.canvas 

    @property
    def quiver_figure(self) -> Figure:
        return self.ui.widget_vector_field.figure 

    @property
    def quiver_ax(self) -> Axes:
        return self.ui.widget_vector_field.figure.ax

    @property 
    def quiver_blit_manager(self) -> BlitManager:
        return self.ui.widget_vector_field.blit_manager

    @property
    def quiver_object(self) -> Quiver:
        return self._quiver_object 

    @property
    def vec_data(self) -> np.ndarray:
        return self._vec_data

    @property
    def vec_path(self) -> str:
        return self._vec_path

    @property
    def quiver_ax(self) -> Axes:
        return self._quiver_ax 

    @property
    def quiver_scale(self) -> float:
        return self._quiver_scale 

    @property
    def quiver_width(self) -> float:
        return self._quiver_width

    @property 
    def quiver_color(self) -> str:
        return self._quiver_color

    def setFourDSTEM(self, data_path: str):
        """
        Set the data path in HDF5 file, to show the diffraction patterns.

        Will set the data_path attribute. The FourDSTEM must be a 4D matrix.

        arguments:
            data_path: (str) the path of the 4D-STEM data.

        raises:
            TypeError, KeyError, ValueError
        """
        super(PageRotateFourDSTEM, self).setFourDSTEM(data_path)
        self.setVectorField()
    
    def _initUi(self):
        """
        Initialize Ui.
        """

        self.setWindowTitle('Rotation Calibration')
        self.ui.pushButton_browse_vector_field.clicked.connect(
            self._browseVectorField
        )
        self.ui.pushButton_adjust_quiver_effects.clicked.connect(
            self._adjustQuiverEffects
        )
        self.ui.pushButton_calculate_rotation_angle.clicked.connect(
            self._calculateRotationAngle
        )
        self.ui.doubleSpinBox_rotation_angle.valueChanged.connect(
            self._updateDP 
        )
        self.ui.pushButton_refresh_quiver.clicked.connect(
            self._changeQuiverAngle 
        )
        self.ui.doubleSpinBox_rotation_angle.setRange(-360, 720)
        
        

    def setVectorField(self, vec_path: str = '', read_attr: bool = False):
        """
        Set the vector fields path.

        arguments:
            data_path: (str) the path of the vector field. If None, a new 
                vector field will be created.

            read_attr: (bool) whether display effects are from Dataset.attrs.
        """
        if vec_path == '':
            self._vec_data = None 
            return 
            
        if not isinstance(vec_path, str):
            raise TypeError('data_path must be a str, not '
                '{0}'.format(type(vec_path).__name__))

        img_node = self.hdf_handler.getNode(vec_path)  
        # May raise KeyError if the path does not exist
        if not isinstance(img_node, HDFDataNode):
            raise ValueError(
                'Item {0} must be a Dataset'.format(vec_path)
            )
        vec_obj = self.hdf_handler.file[vec_path]
        if not len(vec_obj.shape) == 3:
            raise ValueError('Data must be a 3D matrix '
                'with shape (2, i, j)')

        if read_attr:
            quiver_hdf_obj = self.hdf_handler.file[self.vec_path]
            if 'quiver_scale' in quiver_hdf_obj.attrs:
                self._quiver_scale = quiver_hdf_obj.attrs['quiver_scale']
            if 'quiver_width' in quiver_hdf_obj.attrs:
                self._quiver_width = quiver_hdf_obj.attrs['quiver_width']
            if 'quiver_color' in quiver_hdf_obj.attrs:
                self._quiver_color = quiver_hdf_obj.attrs['quiver_color']

        self._vec_data = vec_obj[:]
        self._vec_path = vec_path 
        self.ui.lineEdit_vector_field_path.setText(self.vec_path)
        self._createQuiver()

        self.quiver_canvas.draw()
        self.quiver_canvas.flush_events()

    def _createQuiverAxes(self):
        """
        Initialize the quiver axes.
        """
        if self._quiver_ax is None:
            self._quiver_ax = self.quiver_figure.add_subplot()
            self._quiver_ax.set_aspect('equal')
            self.quiver_blit_manager.addArtist('quiver_axes', self.quiver_ax)

    def _createQuiver(self):
        """
        Show the quiver plot.
        """
        if self.quiver_object in self.quiver_ax.collections:
            _index = self.quiver_ax.collections.index(self.quiver_object)
            self.quiver_ax.collections.pop(_index)

        if self.vec_data is None:
            if 'quiver' in self.quiver_blit_manager:
                del self.quiver_blit_manager['quiver']
            return 

        _, height, width = self.vec_data.shape 
        array_i = np.linspace(0, height - 1, height)
        array_j = np.linspace(0, width - 1, width)
        coord_i, coord_j = np.meshgrid(array_i, array_j, indexing = 'ij')
        vec_i, vec_j = self.vec_data 

        X, Y = coord_i, coord_j 
        U, V = vec_j, vec_i 

        self._quiver_object = self.quiver_ax.quiver(
            X, Y, U, V,
            units = 'xy',
            scale = self.quiver_scale,
            width = self.quiver_width,
            angles = 'xy',
            pivot = 'mid',
            color = self.quiver_color,
        )

        self.quiver_blit_manager['quiver'] = self._quiver_object

    def _updateDP(self):
        """
        Update the current diffraction pattern according to the location in 
        the real space. Will automatically rotate according to the rotate 
        angle.
        """
        if self.data_object is None:
            return None 
        
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape 
        scan_ii = max(0, min(scan_i, self.scan_ii)) # Avoid out of boundary
        scan_jj = max(0, min(scan_j, self.scan_jj))
        dp = self.data_object[scan_ii, scan_jj, :, :]

        dp_rotate = rotate(dp, - self.rotate_angle, reshape = False)
        self.dp_object.set_data(dp_rotate)
        self.dp_blit_manager.update()

    def _browseVectorField(self):
        """
        Open a dialog to browse which vector field to set to be calibrated.
        """
        dialog = DialogHDFChoose(self)
        dialog_code = dialog.exec()
        if dialog_code == dialog.Accepted:
            current_path = dialog.getCurrentPath()
        try:
            self.setVectorField(current_path)
        except (KeyError, ValueError, TypeError,) as e:
            self.logger.error('{0}'.format(e), exc_info=True)
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Cannot open this data: {0}'.format(e))
            msg.exec()

    def _adjustQuiverEffects(self):
        """
        Open a dialog to adjust quiver display effects.

        This function will NOT modify the attributes in the Dataset.attrs.
        """
        dialog = DialogAdjustQuiverEffect(self)
        # dialog.setVectorField(self.data_path)
        dialog_code = dialog.exec()
        if dialog_code == DialogAdjustQuiverEffect.Rejected:
            return 

        self._quiver_scale = dialog.getScale()
        self._quiver_width = dialog.getWidth()
        self._quiver_color = dialog.getColor()
        self.setVectorField(self.vec_path)

    def _calculateRotationAngle(self):
        """
        Open a dialog to calculate rotational angle.
        """
        # rotate_dialog = 
        pass

    def _changeQuiverAngle(self):
        """
        This function will change the quiver display effects by change every
        vector's angle.
        """
        if self.vec_path == '':
            return 
        if self.vec_data is None:
            return 
        self._calculateRotatedQuiver()
        self._createQuiver()
        self.quiver_canvas.draw()
        self.quiver_blit_manager.update()

    def _calculateRotatedQuiver(self):
        """
        Calculate the rotated vector field.
        """
        original_data = self.hdf_handler.file[self.vec_path]
        vec_i = original_data[0, :, :]
        vec_j = original_data[1, :, :]
        angle_rad = self.rotate_angle * np.pi / 180
        new_vec_i = vec_i * np.cos(angle_rad) - vec_j * np.sin(angle_rad)
        new_vec_j = vec_i * np.sin(angle_rad) + vec_j * np.cos(angle_rad)
        self.vec_data[0, :, :] = new_vec_i 
        self.vec_data[1, :, :] = new_vec_j


# class DialogAdjustQuiverEffect(QDialog):
#     """
#     用于调整矢量场箭头图的效果的对话框。

#     注意，这个类和 PageViewVectorField 中的类在 API 上具有不同。这个对话框
#     不会试图读取

#     Dialog to adjust quiver display effect.
#     """

