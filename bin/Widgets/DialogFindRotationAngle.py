# -*- coding: utf-8 -*-

"""
*------------------------ DialogFindRotationAngle.py -------------------------*
寻找矢量场旋转角度(来把它转成保守场)的对话框。

部件内容：
    - WidgetPlotLine

作者:           胡一鸣
创建日期:       2022年6月2日

Dialog to find the rotation angle of the vector field (to correct it to be a 
conservative field).

Contents:
    - WidgetPlotLine

author:         Hu Yiming
date:           Jun 2, 2022
*------------------------ DialogFindRotationAngle.py -------------------------*
"""

from logging import Logger 

from PySide6.QtWidgets import QDialog, QWidget, QMessageBox
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas
)
from matplotlib.figure import Figure 
from matplotlib.axes import Axes 
from matplotlib.lines import Line2D
import numpy as np
import h5py 

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFDataNode, HDFHandler
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from lib.VectorFieldOperators import Divergence2D
from lib.VectorFieldOperators import Curl2D
from ui import uiDialogFindRotationAngle



class DialogFindRotationAngle(QDialog):
    """
    寻找矢量场旋转角度的部件类。

    Ui 文件地址: ROOTPATH/ui/uiDialogFindRotationAngle.ui

    Dialog to find the rotation angle of vector field.

    The path of the ui file: ROOTPATH/ui/uiDialogFindRotationAngle.ui

    attributes:

    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogFindRotationAngle.Ui_Dialog()
        self.ui.setupUi(self)
        
        self._vec_path = ''
        self._curve_angle = np.linspace(0, 359, 360)
        self._curve_curl = np.zeros_like(self._curve_angle)
        self._curve_div = np.zeros_like(self._curve_angle)
        self._curve_ax = None
        self._line_curl = None 
        self._line_div = None 
        self._legend = None 
        

        self._createAxes()
        self._createLines()
        self.curve_canvas.draw()
        self.curve_canvas.flush_events()

        self._initUi()

    @property
    def curve_canvas(self) -> FigureCanvas:
        return self.ui.widget_curve.canvas 

    @property
    def curve_figure(self) -> Figure:
        return self.ui.widget_curve.figure 

    @property
    def curve_ax(self) -> Axes:
        return self._curve_ax 

    @property
    def curve_angle(self) -> np.ndarray:
        return self._curve_angle 

    @property
    def curve_div(self) -> np.ndarray:
        return self._curve_div

    @property
    def curve_curl(self) -> np.ndarray:
        return self._curve_curl 

    @property 
    def line_div(self) -> Line2D:
        return self._line_div

    @property
    def line_curl(self) -> Line2D:
        return self._line_curl

    @property
    def curve_blit_manager(self) -> BlitManager:
        return self.ui.widget_curve.blit_manager

    @property
    def vec_path(self) -> str:
        return self._vec_path

    @property
    def vec_object(self) -> h5py.Dataset:
        return self.hdf_handler.file[self.vec_path]

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler

    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger

    

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

    def _createAxes(self):
        """
        Create the axes that contains the curve.
        """
        if self._curve_ax is None:
            self._curve_ax = self.curve_figure.add_subplot()
            self.curve_blit_manager.addArtist('curve_axes', self._curve_ax)
            self.curve_ax.set_xlabel('rotation angle (deg)')
            self.curve_ax.set_ylabel('relative value to maximum')
            self.curve_ax.set_title('Sum of point-wise squared distribution'
                ' - angle curve')
            self.curve_ax.set_xlim(0, 360)
            self.curve_ax.set_ylim(0, 1.2)


    def _createLines(self):
        """
        Create the Line2D objects.
        """
        self._line_curl, = self.curve_ax.plot(
            self.curve_angle, 
            self.curve_curl,
            color = 'black',
            linestyle = 'solid',
            linewidth = 2,
            label = 'curl',
        )
        self._line_div, = self.curve_ax.plot(
            self.curve_angle,
            self.curve_div,
            color = 'blue',
            linestyle = 'dashed',
            linewidth = 2,
            label = 'divergence',
        )
        
        self.curve_blit_manager.addArtist('line_curl', self._line_curl)
        self.curve_blit_manager.addArtist('line_div', self._line_div)
        self._legend = self.curve_ax.legend(loc = 'upper right')

    def setVectorField(self, vec_path: str):
        """
        Set the data path in HDF5 file, to calculate the dcom-theta and curl
        com-theta curve.

        arguments:
            vec_path: (str) the path of the vector field.

        raises:
            TypeError, KeyError, ValueError
        """
        if not isinstance(vec_path, str):
            raise TypeError('vec_path must be a str, not '
                '{0}'.format(type(vec_path).__name__))
        
        img_node = self.hdf_handler.getNode(vec_path)
        # May raise KeyError if the path does not exist
        if not isinstance(img_node, HDFDataNode):
            raise ValueError('Item {0} must be a Dataset'.format(vec_path))

        data_obj = self.hdf_handler.file[vec_path]
        if not len(data_obj.shape) == 3:
            raise ValueError('Data must be a 3D matrix (2, i, j)')

        self._vec_path = vec_path 
        self.ui.lineEdit_vector_field_path.setText(self._vec_path)
        
        self._calculateLines()
        self._updateCurve()
        min_angle = self._findMinCurl()
        self.ui.doubleSpinBox_rotation_angle.setValue(min_angle)
        
    def getRotationAngle(self) -> float:
        """
        returns the calculated rotation angle.

        returns:
            (float) unit: degree.
        """
        return self.ui.doubleSpinBox_rotation_angle.value()

    def _calculateLines(self):
        """
        Calculate the square divergence and curl of the vector field, to 
        rotation angle curve.
        """
        
        for ii, angle_deg in enumerate(self._curve_angle):
            vec = self.vec_object[:]
            vec_rotated = self._rotateVec(vec, angle_deg)
            self._curve_div[ii] = np.sum(np.square(Divergence2D(
                vec_rotated[0,:,:], 
                vec_rotated[1,:,:]
            )))

            self._curve_curl[ii] = np.sum(np.square(Curl2D(
                vec_rotated[0,:,:], 
                vec_rotated[1,:,:]
            )))

    def _findMinCurl(self):
        """
        Find the rotation angle which produces the minimum sum of the 
        point-wise square curl distribution of the vector field.
        """
        _angle = 0
        _curl = self._curve_curl[0]
        for angle, curl_sq in zip(self._curve_angle, self._curve_curl):
            if curl_sq < _curl:
                _angle = angle 
                _curl = curl_sq 
        return _angle 

    def _initUi(self):
        """
        Initialize Uis.
        """
        self.ui.doubleSpinBox_rotation_angle.setRange(0, 360)
        self.ui.pushButton_browse.clicked.connect(self._browse)
        self.ui.pushButton_ok.clicked.connect(self.accept)
        self.ui.pushButton_cancel.clicked.connect(self.reject)

    def _rotateVec(self, vec: np.ndarray, angle_deg: float) -> np.ndarray:
        """
        Calculate the rotated vector field.

        arguments:
            vec: (np.ndarray) with shape (2, i, j)

            angle: (float) unit: degree.
        """
        vec_i = vec[0, :, :]
        vec_j = vec[1, :, :]
        angle = angle_deg * np.pi / 180 
        new_vec = np.zeros_like(vec)
        new_vec[0, : ,:] = vec_i * np.cos(angle) - vec_j * np.sin(angle)
        new_vec[1, :, :] = vec_i * np.sin(angle) + vec_j * np.cos(angle)
        return new_vec 

    def _updateCurve(self):
        """
        Update the curves to the current data.
        """
        self.line_div.set_ydata(self.curve_div/np.max(self.curve_div))
        self.line_curl.set_ydata(self.curve_curl/np.max(self.curve_curl))
        
        self.curve_blit_manager.update()
