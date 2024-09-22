# -*- coding: utf-8 -*-

"""
*-------------------------- WidgetAlignmentFDDNet.py ----------------------------*
对 4D-STEM 衍射图像，利用 FDDNet 进行明场衍射盘测量的界面。

提升部件:
    - 提升类名 WidgetAlignmentFDDNet
    - 头文件 bin.Widgets.WidgetAlignmentFDDNet

作者:           胡一鸣
创建日期:       2024年9月2日

The widget to measure the diffraction disk position by FDDNet.

Promoted Widget:
    - name of widget class: WidgetAlignmentFDDNet
    - header file: bin.Widgets.WidgetAlignmentFDDNet

author:         Hu Yiming
date:           Sep 2, 2024
*-------------------------------------------------------------------------------*
"""

from logging import Logger
import importlib.resources
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QDialog 

from matplotlib.axes import Axes
from matplotlib.image import AxesImage
from matplotlib.patches import Ellipse
import onnxruntime as ort
from h5py import Dataset

from bin.BlitManager import BlitManager
from bin.TaskManager import TaskManager
from lib.FDDNetInference import loadFDDNetModel 
from lib.FDDNetInference import loadFDDNetAngleModel
from lib.FDDNetInference import inferEllipseLoc
from lib.FDDNetInference import inferEllipseAngle 
from lib.FDDNetInference import inferEllipse
from lib.TaskFDDNetInference import TaskFDDNetInference
from bin.Widgets.DialogSaveItem import DialogSaveVectorField
from ui import uiWidgetAlignmentFDDNet

class WidgetAlignmentFDDNet(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uiWidgetAlignmentFDDNet.Ui_Form()
        self.ui.setupUi(self)
        self._session_fddnet = loadFDDNetModel() 
        self._session_fddnet_angle = loadFDDNetAngleModel()
        self._ellipse_patch = None 
        self._current_a = 0
        self._current_b = 0
        self._current_ci = 0
        self._current_cj = 0
        self._current_theta = 0
        
        self._current_record = {
            "data_path": '',
            "scan_ii": -1,
            "scan_jj": -1,
        }
        self._initUi()
        
    @property
    def current_dp_location(self):
        return (self.scan_ii, self.scan_jj)
    
    def setParentAlignPage(self, align_page: QWidget):
        """
        Set the parent alignment page.

        arguments:
            align_page: (PageAlignFourDSTEM) The parent alignment page containing the 4D-STEM data and UI elements.
        """
        self._align_page = align_page
        
    @property
    def dp_object(self) -> AxesImage:
        return self._align_page.dp_object
    
    @property
    def ax(self) -> Axes:
        return self._align_page.dp_ax
    
    @property
    def blit_manager(self) -> BlitManager:
        return self._blit_manager
    
    @property
    def data_object(self) -> Dataset:
        return self._align_page.data_object
    
    @property
    def scan_ii(self) -> int:
        return self._align_page.scan_ii
    
    @property
    def scan_jj(self) -> int:
        return self._align_page.scan_jj
    
    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger
    
    @property
    def ellipse_patch(self) -> Ellipse:
        return self._ellipse_patch
    
    @property
    def task_manager(self) -> TaskManager:
        global qApp 
        return qApp.task_manager
    
    @property
    def data_path(self) -> str:
        return self._align_page.data_path
    
    def _initUi(self):
        """
        Initialize Ui and their signal-slot connections.
        """
        self.ui.label_fddnet_center_shift_ci.setText('0')
        self.ui.label_fddnet_center_shift_cj.setText('0')
        self.ui.label_fddnet_elliptical_a.setText('0')
        self.ui.label_fddnet_elliptical_b.setText('0')
        self.ui.label_fddnet_elliptical_angle.setText('0')
        
        # self.ui.pushButton_fddnet_inference.clicked.connect(self.inference)
        self.ui.pushButton_generate_shift_vec.clicked.connect(self.generateShiftMapping)
        self.ui.checkBox_show_shifted_dp.clicked.connect(self._onShowShiftedDPChanged)
        self.ui.checkBox_show_measured_ellipse.stateChanged.connect(self._updateEllipsePatch)
        

    def inference(self) -> tuple[float]:
        """
        Use FDDNet to infer the center and the ellipse of the diffraction disk. 
        Note that the input data will be original diffraction pattern, rather 
        than the shifted one.
        
        returns:
            (tuple[float]) center_i, center_j, a, b and theta of the ellipse
        """
        # Get the current diffraction pattern
        dp = self.data_object[self.scan_ii, self.scan_jj, :, :]
        
        # Infer the ellipse parameters using FDDNet
        ci, cj, a, b, theta = inferEllipse(dp, self._session_fddnet, self._session_fddnet_angle)
        
        self._current_a = a
        self._current_b = b
        self._current_ci = ci
        self._current_cj = cj
        self._current_theta = theta
        
        self._current_record["data_path"] = self.data_path 
        self._current_record["scan_ii"] = self.scan_ii
        self._current_record["scan_jj"] = self.scan_jj 
        
        # Update the UI labels with the inferred values
        self.ui.label_fddnet_center_shift_ci.setText(f'{ci:.2f}')
        self.ui.label_fddnet_center_shift_cj.setText(f'{cj:.2f}')
        self.ui.label_fddnet_elliptical_a.setText(f'{a:.2f}')
        self.ui.label_fddnet_elliptical_b.setText(f'{b:.2f}')
        self.ui.label_fddnet_elliptical_angle.setText(f'{theta:.2f}')
        
        # Log the inference results
        # self.logger.info(f'Inferred ellipse parameters: ci={ci:.2f}, cj={cj:.2f}, a={a:.2f}, b={b:.2f}, theta={theta:.2f}')
        
        self._updateEllipsePatch()
        
        return ci, cj, a, b, theta 
    
    
    def setParentAlignPage(self, align_page: QWidget):
        """
        Set the parent alignment page.

        arguments:
            align_page: (PageAlignFourDSTEM) The parent alignment page containing the 4D-STEM data and UI elements.
        """
        self._align_page = align_page 
        
        
    def getCurrentDPShiftVec(self):
        """
        Get the current shift vector of the current diffraction pattern.
        
        If the data path and scan location is not changed, use cached ci and cj 
        instead.
        """
        if (self.data_path == self._current_record["data_path"] and 
            self.scan_ii == self._current_record["scan_ii"] and 
            self.scan_jj == self._current_record["scan_jj"]):
            return self._current_ci, self._current_cj 
        
        # ci, cj, a, b, angle = inferEllipse(
        #     self.data_object[self.scan_ii, self.scan_jj, :, :],
        #     self._session_fddnet,
        #     self._session_fddnet_angle,
        # )
        # self._current_record["data_path"] = self.data_path 
        # self._current_record["scan_ii"] = self.scan_ii
        # self._current_record["scan_jj"] = self.scan_jj 
        # self._current_a = a 
        # self._current_b = b
        # self._current_ci = ci 
        # self._current_cj = cj 
        # self._current_angle = angle 
        
        ci, cj, a, b, theta = self.inference()
        return (ci, cj)
    
    
    def getCurrentShowShiftedDP(self):
        """
        Get the current state of the 'Show Shifted DP' checkbox.
        """
        return self.ui.checkBox_show_shifted_dp.isChecked()
    
    
    def setBlitManager(self, blit_manager: BlitManager):
        """
        Set the blit manager that manages the ellipse indicating the results 
        of FDDNet.
        
        arguments:
            blit_manager: (BlitManager) the blit manager where the 
        """
        self._blit_manager = blit_manager
    
    def _onShowShiftedDPChanged(self):
        """
        Handle the state change of the 'Show Shifted DP' checkbox.
        """
        self._updateEllipsePatch()
        self._align_page._updateDP()
        
    
    def setEllipsePatch(self, ellipse_patch: Ellipse):
        """
        Set the ellipse patch object to show the inferred result.
        """
        self._ellipse_patch = ellipse_patch

    def setEllipsePatchVisible(self, visible: bool = True):
        """
        Set whether the ellipse patch is visible.
        
        arguments:
            visible: (bool) 
        """
        self._ellipse_patch.set_visible(visible)

    def _updateEllipsePatch(self):
        """
        Update the ellipse patch object with the current inference result.
        """
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape 
        center_i, center_j = (dp_i - 1)/2, (dp_j - 1)/2
        # center_i, center_j = dp_i/2, dp_j/2
        self._ellipse_patch.set_width(self._current_a * 2)
        self._ellipse_patch.set_height(self._current_b * 2)
        self._ellipse_patch.set_center(
            (self._current_cj + center_j, self._current_ci + center_i,)
        )
        self._ellipse_patch.set_angle(self._current_theta)
        self._ellipse_patch.set_visible(
            self.ui.checkBox_show_measured_ellipse.isChecked()
        )
        self.blit_manager.update()
        
        
    def generateShiftMapping(self):
        """
        Generate the shift map for the entire 4D-STEM dataset by applying inference ellipse loc to each diffraction pattern. It will ask users for fitting model.
        
        This function will submit a background task using the task manager.
        """

        # Use the DialogGenerateShiftVector to select the fit model
        dialog_fit_model = DialogGenerateShiftVector(self)
        result = dialog_fit_model.exec()
        if result == QDialog.Accepted:
            fit_model = dialog_fit_model.getSelectedModel()
        else:
            return
        
        # Open the dialog to get the path and name for saving the Shift Map
        dialog_save = DialogSaveVectorField(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return

        parent_path = dialog_save.getParentPath()
        shift_map_name = dialog_save.getNewName()

        calc_dict = {
            'center': True,
            'ci': False,
            'cj': False,
            'a': False,
            'b': False,
            'angle': False,
        }
        
        names_dict = {
            'center': shift_map_name,
        }
        
        centers_meta = self._generateShiftMapMeta()
        metas_dict = {
            'center': centers_meta
        }
        
        fit_models_dict = {
            'center': fit_model
        }

        # Initialize the TaskFDDNetInference with the necessary parameters
        self.task = TaskFDDNetInference(
            item_path=self.data_path,
            image_parent_path=parent_path,
            calc_dict = calc_dict,
            names_dict = names_dict,
            metas_dict = metas_dict,
            fit_models_dict = fit_models_dict,
        )

        self.task_manager.addTask(self.task)

    def _generateShiftMapMeta(self) -> dict:
        """
        Generate metadata for the shift map.
        """
        meta = {}
        meta['Alignment/Method'] = 'FDDNet Inference'
        meta['Alignment/TargetDatasetPath'] = self.data_path
        # TODO: Add more attributes as needed
        return meta


class DialogGenerateShiftVector(QDialog):
    """
    A dialog to select the fit model for generating shift vectors.

    This dialog allows the user to specify the fit model to be used for generating
    shift vectors using the FDDNet model. It includes radio buttons to select the fit model.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Fitting Model")

        # Create layout and widgets
        layout = QVBoxLayout()

        self.radio_button_apply_current_shift_vec = QRadioButton("None (Do not use fit)")
        self.radio_button_linear_regression = QRadioButton("Linear")
        self.radio_button_quadratic_polynomial = QRadioButton("Quadratic")

        self.radio_button_apply_current_shift_vec.setChecked(True)

        layout.addWidget(self.radio_button_apply_current_shift_vec)
        layout.addWidget(self.radio_button_linear_regression)
        layout.addWidget(self.radio_button_quadratic_polynomial)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)

        self.setLayout(layout)

    def getSelectedModel(self) -> str|None:
        """
        Get the selected fit model.

        returns:
            (str|None) The selected fit model.
        """
        if self.radio_button_apply_current_shift_vec.isChecked():
            return None
        elif self.radio_button_linear_regression.isChecked():
            return 'Linear'
        elif self.radio_button_quadratic_polynomial.isChecked():
            return 'Quadratic'
        return None