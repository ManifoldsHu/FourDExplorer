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
from matplotlib.image import AxesImage 
import numpy as np
from scipy.ndimage import rotate

from Constants import APP_VERSION
from bin.BlitManager import BlitManager 
from bin.TaskManager import TaskManager 
from bin.HDFManager import HDFDataNode
from bin.UIManager import ThemeHandler
from bin.DateTimeManager import DateTimeManager
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.Widgets.DialogFindRotationAngle import DialogFindRotationAngle
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

        self._axial_bf_object = None 
        self._axial_bf_data = None 
        self._axial_bf_path = ''
        self._axial_bf_ax = None

        self._rotation_angle = 0

        self._createAxes()
        self._createQuiverAxes()
        self._createAxialBFAxes()
        self._initBaseUi()
        self._initUi()

    @property
    def rotation_angle(self) -> float:
        return self._rotation_angle 

    @property
    def task_manager(self) -> TaskManager:
        global qApp 
        return qApp.task_manager 
    
    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler

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

    @property
    def axial_bf_ax(self) -> Axes:
        return self._axial_bf_ax 
    
    @property
    def axial_bf_object(self) -> AxesImage:
        return self._axial_bf_object 
    
    @property
    def axial_bf_data(self) -> np.ndarray:
        return self._axial_bf_data
    
    @property
    def axial_bf_canvas(self) -> FigureCanvas:
        return self.ui.widget_axial_bf.canvas
    
    @property
    def axial_bf_figure(self) -> Figure:
        return self.ui.widget_axial_bf.figure
    
    @property
    def axial_bf_blit_manager(self) -> BlitManager:
        return self.ui.widget_axial_bf.blit_manager
    
    @property
    def datetime_manager(self) -> DateTimeManager:
        global qApp 
        return qApp.datetime_manager

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
        self.ui.doubleSpinBox_rotation_angle_quiver.valueChanged.connect(
            self._rotateDPAccordingToQuiver
        )
        self.ui.toolButton_refresh_quiver.clicked.connect(
            self._changeQuiverAngle 
        )
        self._updateRefreshIcon()
        self.theme_handler.theme_changed.connect(self._updateRefreshIcon)
        self.ui.doubleSpinBox_rotation_angle_quiver.setRange(-360, 720)
        
        self.ui.pushButton_browse_axial_bf.clicked.connect(self._browseAxialBF)
        self.ui.pushButton_calculate_rotation_angle_axial_bf.clicked.connect(self._calculateRotationAngleAxialBF)
        self.ui.doubleSpinBox_rotation_angle_axial_bf.valueChanged.connect(
            self._rotateDPAccordingToAxialBF
        )   # the spin box of rotation angle in axial bf tab 
        self.ui.doubleSpinBox_rotation_angle_axial_bf.setRange(-360, 720)
        self.ui.toolButton_refresh_axial_bf.clicked.connect(
            self._updateDP 
        )

        self.ui.pushButton_start.clicked.connect(self.startCalculation)
        self.ui.pushButton_start.setProperty('class', 'danger')

    def _updateRefreshIcon(self):
        _refresh_quiver_icon_path = ':/HDFEdit/resources/icons/refresh'
        refresh_icon=self.theme_handler.iconProvider(_refresh_quiver_icon_path)
        self.ui.toolButton_refresh_quiver.setIcon(refresh_icon)
        self.ui.toolButton_refresh_axial_bf.setIcon(refresh_icon)

    def setVectorField(self, vec_path: str = '', read_attr: bool = False):
        """
        Set the vector fields path.

        arguments:
            vec_path: (str) the path of the vector field. If None, a new 
                vector field will be created.

            read_attr: (bool) whether display effects are from Dataset.attrs.
        """
        if vec_path == '':
            self._vec_data = None 
            return 
            
        if not isinstance(vec_path, str):
            raise TypeError('vec_path must be a str, not '
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
            # _index = self.quiver_ax.collections.index(self.quiver_object)
            # self.quiver_ax.collections.pop(_index)
            self.quiver_object.remove()

        if self.vec_data is None:
            if 'quiver' in self.quiver_blit_manager:
                del self.quiver_blit_manager['quiver']
            return 

        _, height, width = self.vec_data.shape 
        array_i = np.linspace(0, height - 1, height)
        array_j = np.linspace(0, width - 1, width)
        coord_i, coord_j = np.meshgrid(array_i, array_j, indexing = 'ij')
        vec_i, vec_j = self.vec_data 

        X, Y = coord_j, coord_i 
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

        dp_rotate = rotate(dp, self.rotation_angle, reshape = False)
        self.dp_object.set_data(dp_rotate)
        self.dp_blit_manager.update()

    def _rotateDPAccordingToQuiver(self):
        """
        Rotate the diffraction pattern according to the double spin box 
        at the quiver tab.
        """
        self._rotation_angle = self.ui.doubleSpinBox_rotation_angle_quiver.value()

        self.ui.doubleSpinBox_rotation_angle_quiver.setValue(self.rotation_angle)
        self.ui.doubleSpinBox_rotation_angle_axial_bf.setValue(self.rotation_angle)
        self._updateDP()

    def _rotateDPAccordingToAxialBF(self):
        """
        Rotate the diffraction pattern according to the double spin box 
        at the axial bf tab.
        """
        self._rotation_angle = self.ui.doubleSpinBox_rotation_angle_axial_bf.value()

        self.ui.doubleSpinBox_rotation_angle_quiver.setValue(self.rotation_angle)
        self.ui.doubleSpinBox_rotation_angle_axial_bf.setValue(self.rotation_angle)
        self._updateDP()

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
        if self.vec_path == '':
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Should set a Center of Mass vector field first.\n'
                'If there has not been any yet, you can calculate one for\n'
                'this 4D-STEM dataset.')
            msg.exec()
            return self._browseVectorField()

        rotate_dialog = DialogFindRotationAngle(self)
        rotate_dialog.setVectorField(self.vec_path)
        dialog_code = rotate_dialog.exec()
        if dialog_code == rotate_dialog.Accepted:
            self.ui.doubleSpinBox_rotation_angle.setValue(
                rotate_dialog.getRotationAngle()
            )
        else:
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
        angle_rad = self.rotation_angle * np.pi / 180
        new_vec_i = vec_i * np.cos(angle_rad) + vec_j * np.sin(angle_rad)
        new_vec_j = - vec_i * np.sin(angle_rad) + vec_j * np.cos(angle_rad)
        self.vec_data[0, :, :] = new_vec_i 
        self.vec_data[1, :, :] = new_vec_j

    def startCalculation(self):
        """
        Start to apply the rotation to all of the diffraction patterns.
        """
        dialog_save = DialogSaveFourDSTEM(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return 
        if dialog_save.getIsInplace():
            data_node = self.hdf_handler.getNode(self.data_path)
            output_name = data_node.name 
            output_parent_path = data_node.parent.path 
        else:
            output_name = dialog_save.getNewName()
            output_parent_path = dialog_save.getParentPath()

        # meta = self.data_object.attrs
        # if 'calibrated_rotation_angle' in meta:
        #     meta['calibrated_rotation_angle'] += self.rotation_angle
        # else:
        #     meta['calibrated_rotation_angle'] = self.rotation_angle 
        meta = self._generateMeta(output_name)

        self.task = TaskFourDSTEMRotate(
            self.data_path,
            output_parent_path,
            output_name,
            self.rotation_angle,
            **meta,
        )
        self.task_manager.addTask(self.task) 


    def _generateMeta(self, name: str = None) -> dict:
        """
        Generate metadata for the rotated 4D-STEM dataset.

        arguments:
            name: (str) the name of the dataset.

        returns:
            (dict) the metadata dictionary.
        """
        meta = {}
        # meta['/Calibration/RotationalOffsetCorrection/method'] = 'Rotation by Angle'
        meta['/Calibration/RotationalOffsetCorrection/scan_rotation'] = self.rotation_angle
        # meta['/Calibration/RotationalOffsetCorrection/AngleUnit'] = 'degrees'
        # meta['/Calibration/RotationalOffsetCorrection/OriginalDatasetPath'] = self.data_path
        
        # Add general and space information
        meta['/General/title'] = name if name else 'Rotated 4D-STEM Dataset'
        meta['/General/time'] = self.datetime_manager.current_time
        meta['/General/date'] = self.datetime_manager.current_date
        meta['/General/time_zone'] = self.datetime_manager.current_timezone
        meta['/General/fourd_explorer_version'] = '.'.join(APP_VERSION)
        
        # Add space calibration information
        for key, value in self.data_object.attrs.items():
            if key.startswith('/Calibration/Space/'):
                meta[key] = value
            elif key.startswith('/Acquisition/'):
                meta[key] = value
            elif key.startswith('/Quantify/'):
                meta[key] = value
        
        return meta


    def setAxialBF(self, axial_bf_path: str, read_attr: bool = False):
        """
        Set the axial BF path.

        arguments:
            axial_bf_path: (str) the path of the axial BF. If None, a new one will be created.

            read_attr: (bool) whether to read the displaying attributes from the Axial BF image.
        """
        if axial_bf_path == '':
            self._axial_bf_data = None 
            return 
        
        if not isinstance(axial_bf_path, str):
            raise TypeError('axial_bf_path should be a string, not '
                            f'{type(axial_bf_path).__name__}')
        
        axial_bf_node = self.hdf_handler.getNode(axial_bf_path)
        if not isinstance(axial_bf_node, HDFDataNode):
            raise ValueError(f'Item {axial_bf_path} must be a Dataset')
        axial_bf_obj = self.hdf_handler.file[axial_bf_path]
        if not len(axial_bf_obj.shape) == 2:
            raise ValueError(f'Data must be a 2D array')
        
        if read_attr:
            pass # TODO 

        self._axial_bf_data = axial_bf_obj[:]
        self._axial_bf_path = axial_bf_path
        self.ui.lineEdit_axial_bf_path.setText(self._axial_bf_path)
        self._createAxialBF()
        self.axial_bf_canvas.draw()
        self.axial_bf_canvas.flush_events()

    def _createAxialBFAxes(self):
        """
        Initialize the axial BF axes.
        """
        if self._axial_bf_ax is None:
            self._axial_bf_ax = self.axial_bf_figure.add_subplot()
            self._axial_bf_ax.set_aspect('equal')
            self.axial_bf_blit_manager.addArtist('axial_bf_axes', self._axial_bf_ax)

    def _createAxialBF(self):
        """
        Show the axial bf plot.
        """
        if self._axial_bf_object in self.axial_bf_ax.images:
            self.axial_bf_object.remove()

        self._axial_bf_object = self.axial_bf_ax.imshow(self._axial_bf_data)
        self.axial_bf_blit_manager.addArtist('axial_bf', self._axial_bf_object)
        self.axial_bf_blit_manager.update()

    def _browseAxialBF(self):
        """
        Open a dialog to browse which axial bright field image to set to be calibrated.
        """
        dialog = DialogHDFChoose(self)
        dialog_code = dialog.exec()
        if dialog_code == dialog.Accepted:
            current_path = dialog.getCurrentPath()
        try:
            self.setAxialBF(current_path)
        except (KeyError, ValueError, TypeError,) as e:
            self.logger.error('{0}'.format(e), exc_info=True)
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Cannot open this data: {0}'.format(e))
            msg.exec()

    def _calculateRotationAngleAxialBF(self):
        """
        TODO
        """
        pass 


