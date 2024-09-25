#-*- coding: utf-8 -*- 

"""
*-------------------------- WidgetAlignmentRef.py ----------------------------*

通过使用 Reference 对 4D-STEM 数据集进行平移、合轴的部件。

提升部件:
    - 提升类名 WidgetAlignmentRef 
    - 头文件 bin.Widgets.WidgetAlignmentRef

作者:           胡一鸣
创建日期:       2024年9月2日

The widget to align 4D-STEM dataset by using reference dataset.

Promoted Widget:
    - name of widget class: WidgetAlignmentRef
    - header file: bin.Widgets.WidgetAlignmentRef

author:         Hu Yiming
date:           Sep 2, 2024
*-------------------------- WidgetAlignmentRef.py ----------------------------*
"""

from logging import Logger

from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox

import numpy as np
from matplotlib.axes import Axes
from matplotlib.image import AxesImage
from h5py import Dataset

from Constants import APP_VERSION
from bin.BlitManager import BlitManager
from bin.HDFManager import HDFHandler
from bin.HDFManager import HDFDataNode 
from bin.DateTimeManager import DateTimeManager
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.Widgets.DialogSaveItem import DialogSaveVectorField
from lib.VectorFieldOperators import CenterOfMass
from lib.TaskReconstruction import TaskCenterOfMass

from ui import uiWidgetAlignmentRef


class WidgetAlignmentRef(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._reference_path = ''
        self.ui = uiWidgetAlignmentRef.Ui_Form()
        self.ui.setupUi(self)
        self._initUi()
        
    @property
    def current_dp_location(self):
        return (self.scan_ii, self.scan_jj)
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler
    
    @property
    def current_ref_com(self) -> tuple[float, float]:
        if not self.reference_path: 
            return (0, 0)
        return CenterOfMass(self.reference_dataset[self.scan_ii, self.scan_jj, :, :])
    
    @property
    def reference_path(self) -> str:
        return self._reference_path

    @property
    def reference_dataset(self) -> Dataset:
        return self.hdf_handler.file[self._reference_path]
        
    @property
    def dp_object(self) -> AxesImage:
        return self._align_page.dp_object
    
    @property
    def ax(self) -> Axes:
        return self._align_page.dp_ax
    
    @property
    def blit_manager(self) -> BlitManager:
        return self._align_page.dp_blit_manager
    
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
    def datetime_manager(self) -> DateTimeManager:
        global qApp 
        return qApp.datetime_manager
    
    
    def _initUi(self):
        """
        Initialize Ui and their signal slot connections.
        """
        self.ui.lineEdit_reference_4dstem.setReadOnly(True)
        self.ui.pushButton_browse_reference_4dstem.clicked.connect(self._onBrowseReference4DSTEMPath)
        self.ui.checkBox_show_shifted_dp.stateChanged.connect(self._onShowShiftedDPChanged)
        self.ui.pushButton_generate_shift_vec.clicked.connect(self._onGenerateShiftVecClicked)
        self.ui.label_measured_dp_shift.setText("(0, 0)")

        
        
    def _onBrowseReference4DSTEMPath(self):
        """
        Open a dialog to browse which 4D-STEM dataset to be opened as the reference.
        """
        dialog = DialogHDFChoose(self)
        dialog_code = dialog.exec()
        if dialog_code == dialog.Accepted:
            current_path = dialog.getCurrentPath()
        else:
            return 

        try:
            self.setReference4DSTEM(current_path)
        except (KeyError, ValueError, TypeError,) as e:
            self.logger.error('{0}'.format(e), exc_info = True)
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Cannot open this data: {0}'.format(e))
            msg.exec()


    def setParentAlignPage(self, align_page: QWidget):
        """
        Set the parent alignment page.

        arguments:
            align_page: (PageAlignFourDSTEM) The parent alignment page containing the 4D-STEM data and UI elements.
        """
        self._align_page = align_page
        self._align_page.ui.spinBox_scan_ii.valueChanged.connect(self._onScanChanged)
        self._align_page.ui.spinBox_scan_jj.valueChanged.connect(self._onScanChanged)


    def setReference4DSTEM(self, reference_path: str):
        """
        Set the reference 4D-STEM dataset path in HDF5 file.

        Will set the reference_path attribute. The reference dataset must be
        a 4D matrix.

        arguments:
            reference_path: (str) the 4D-STEM dataset's path in hdf5 file.
        """
        if not isinstance(reference_path, str):
            raise TypeError('reference_path must be a str, not '
                '{0}'.format(type(reference_path).__name__))

        reference_node = self.hdf_handler.getNode(reference_path)
        # May raise KeyError if the path does not exist
        if not isinstance(reference_node, HDFDataNode):
            raise ValueError('Item {0} must be a '
                'Dataset'.format(reference_path))
        
        reference_data_obj = self.hdf_handler.file[reference_path]
        if not len(reference_data_obj.shape) == 4:
            raise ValueError('Data must be a 4D matrix (4D-STEM dataset)')

        if reference_data_obj.shape[:2] != self.data_object.shape[:2]:
            raise ValueError(f'The first two dimensions of the reference dataset ({reference_data_obj.shape[:2]}) must match the first two dimensions of the data object ({self.data_object.shape[:2]}).')
        
        if reference_data_obj.shape[2:] != self.data_object.shape[2:]:
            self.logger.warning(f'The last two dimensions of the reference dataset ({reference_data_obj.shape[2:]}) do not match the last two dimensions of the data object ({self.data_object.shape[2:]}).')

        self._reference_path = reference_path
        self.ui.lineEdit_reference_4dstem.setText(self.reference_path)
        
    
    
    def _onShowShiftedDPChanged(self):
        """
        Handle the state change of the 'Show Shifted DP' checkbox.
        """
        self._align_page._updateDP()
        

    def _onGenerateShiftVecClicked(self):
        """
        Handle the click of the 'Generate Shift Vector' button.
        This function will calculate the Center of Mass (CoM) for the reference 4D-STEM dataset.
        """
        if not self._reference_path:
            QMessageBox.warning(self, 'No Reference Dataset', 'Please set a reference 4D-STEM dataset first.')
            return

        # Open the dialog to get the path and name for saving the Vector Field
        dialog_save = DialogSaveVectorField(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return

        parent_path = dialog_save.getParentPath()
        com_name = dialog_save.getNewName()

        # Initialize the TaskCenterOfMass with only CoM calculation
        calc_dict = {'CoM': True}
        names = {'CoM': com_name}
        metas = {'CoM': self._generateCoMMeta()}

        is_com_inverted = False  # Assuming no inversion for simplicity
        is_mean_set_to_zero = True  # Assuming mean set to zero for simplicity

        mask = None  # Assuming no mask for simplicity

        self.task = TaskCenterOfMass(
            item_path=self._reference_path,
            image_parent_path=parent_path,
            calc_dict=calc_dict,
            names_dict=names,
            metas_dict=metas,
            mask=mask,
            is_com_inverted=is_com_inverted,
            is_mean_set_to_zero=is_mean_set_to_zero,
        )

        self.task_manager.addTask(self.task)

    def _generateCoMMeta(self, name: str = None) -> dict:
        """
        Generate metadata for center of mass vector field.
        """
        meta = {}
        meta['Alignment/Method'] = 'Reference Center of Mass'
        meta['Alignment/ReferenceDatasetPath'] = self._reference_path
        meta['Alignment/TargetDatasetPath'] = self._align_page.data_path
        
        # Add general and space information
        meta['/General/title'] = name if name else 'Reference CoM Vector Field'
        meta['/General/time'] = self.datetime_manager.current_time
        meta['/General/date'] = self.datetime_manager.current_date
        meta['/General/time_zone'] = self.datetime_manager.current_timezone
        meta['/General/foud_explorer_version'] = '.'.join(APP_VERSION)
        
        # Add space calibration information
        if '/Calibration/Space/scan_dr_i' in self.data_object.attrs:
            meta['/Calibration/Space/pixel_size_i'] = self.data_object.attrs['/Calibration/Space/scan_dr_i']
        if '/Calibration/Space/scan_dr_j' in self.data_object.attrs:
            meta['/Calibration/Space/pixel_size_j'] = self.data_object.attrs['/Calibration/Space/scan_dr_j']
        meta['/Calibration/Space/pixel_size_unit'] = 'm'
        meta['/Calibration/Space/pixel_size_unit_display'] = 'nm'
        meta['/Calibration/Space/display_unit_magnify'] = 1e9
        meta['/Calibration/Quantify/value_unit'] = 'pix'
        meta['/Calibration/Quantify/value_unit_display'] = 'pix'
        meta['/Calibration/Quantify/display_unit_magnify'] = 1
        meta['/Calibration/Quantify/display_norm_mode'] = 'linear'
        
        return meta
    
    def getCurrentDPShiftVec(self) -> tuple[float, float]:
        """
        Get the current shift vector of the current diffraction pattern.
        """
        if not self._reference_path:
            return (0, 0)
        # ref_com = self.current_ref_com 
        # self.ui.label_measured_dp_shift.setText(f'({ref_com[0]:.2f}, {ref_com[1]:.2f})')
        return self.current_ref_com
        
    def getCurrentShowShiftedDP(self) -> bool:
        """
        Get the current state of the 'Show Shifted DP' checkbox.
        """
        return self.ui.checkBox_show_shifted_dp.isChecked()
    
    def _onScanChanged(self):
        ref_com = self.current_ref_com
        self.ui.label_measured_dp_shift.setText(f'({ref_com[0]:.2f}, {ref_com[1]:.2f})')