# -*- coding: utf-8 -*-

"""
*----------------------- DialogEditParaFourDSTEM.py --------------------------*
用于帮助用户逐步确认 4D-STEM 数据集关键参数的对话框。

作者：          胡一鸣
创建时间：      2024年9月24日

Dialog to help users step-by-step confirm key parameters for 4D-STEM datasets.

author:         Hu Yiming
date:           Sep 24, 2024
*----------------------- DialogEditParaFourDSTEM.py --------------------------*
"""

from logging import Logger 

from PySide6.QtWidgets import QWidget 
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QDateEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QDate

import numpy as np
import h5py

from bin.Widgets.DialogEditMeta import DialogEditMeta
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.MetaManager import MetaManager
from bin.HDFManager import HDFHandler
from bin.UIManager import ThemeHandler
from bin.UnitManager import UnitManager
from bin.DateTimeManager import DateTimeManager

from ui.uiDialogEditParaFourDSTEM import Ui_Dialog

class DialogEditParaFourDSTEM(QDialog):
    """
    对话框包含了 4D-STEM 数据集中一些需要用户填写的参数。
    
    This dialog contains some parameters that need to be filled in for 4D-STEM 
    datasets.
    """
    
    page_names = (
        'General', 
        'Microscope', 
        'Camera', 
        'Space', 
        'Low Order Aberration',
        'High Order Aberration', 
    )
    
    
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._dataset_path = ''
        self._navigation_label = " >> ".join(self.page_names)
        self._initMainUi()
        
    @property
    def dataset_path(self) -> str:
        return self._dataset_path
    
    @property
    def dataset(self) -> h5py.Dataset:
        return self.hdf_handler.file[self.dataset_path]
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler
    
    @property 
    def meta_manager(self) -> MetaManager:
        global qApp 
        return qApp.requireMetaManager(self.dataset_path)
    
    @property
    def unit_manager(self) -> UnitManager:
        global qApp 
        return qApp.unit_manager
    
    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler
    
    @property
    def datetime_manager(self) -> DateTimeManager:
        global qApp 
        return qApp.datetime_manager
    
    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger
    
    def _initMainUi(self):
        self.ui.lineEdit_dataset_path.setReadOnly(True)
        self.ui.stackedWidget.setCurrentIndex(0)
        self._updateNavigationLabel()
        self.ui.pushButton_browse.clicked.connect(self._browse)
        self.ui.pushButton_next.clicked.connect(self._nextPage)
        self.ui.pushButton_back.clicked.connect(self._backPage)
        self.ui.pushButton_cancel.setVisible(False)
        self.ui.pushButton_ok.clicked.connect(self.accept)
        
        
    def _updateNavigationLabel(self):
        """
        Update the navigation label to reflect the current page in the stacked 
        widget. The current page will be highlighted in bold.
        """
        current_index = self.ui.stackedWidget.currentIndex()
        parts = self._navigation_label.split(" >> ")
        formatted_parts = [f"<b>{part}</b>" if i == current_index else part for i, part in enumerate(parts)]
        self.ui.label_steps.setText(" >> ".join(formatted_parts))


    def _nextPage(self):
        """
        Show the next page.
        """
        current_index = self.ui.stackedWidget.currentIndex()
        if current_index < self.ui.stackedWidget.count() - 1:
            self.ui.stackedWidget.setCurrentIndex(current_index + 1)
            self._updateNavigationLabel()
    
    def _backPage(self):
        """
        Show the last page.
        """
        current_index = self.ui.stackedWidget.currentIndex()
        if current_index > 0:
            self.ui.stackedWidget.setCurrentIndex(current_index - 1)
            self._updateNavigationLabel()
        
    
    def _browse(self):
        """
        Open the browse dialog to select a 4D-STEM dataset.
        """
        dialog = DialogHDFChoose(self, only_group=False)
        if dialog.exec() == QDialog.Accepted:
            chosen_path = dialog.getCurrentPath()
            dataset = self.hdf_handler.file[chosen_path]
            if len(dataset.shape) == 4:  # Check if the dataset is 4D
                self.setFourDSTEM(chosen_path)
            else:
                QMessageBox.warning(self, "Invalid Dataset", "The selected dataset is not a 4D-STEM dataset.")


    def setFourDSTEM(self, dataset_path: str):
        """
        Set the 4D-STEM dataset to be edited.
        """
        if dataset_path not in self.hdf_handler.file:  # Check if the dataset exists in the HDF5 file
            raise ValueError(f"Dataset does not exist in the HDF5 file: {dataset_path}.")
        
        dataset = self.hdf_handler.file[dataset_path]
        if len(dataset.shape) != 4:
            raise ValueError(f"Dataset is not 4D: {dataset_path}.")
        
        self._dataset_path = dataset_path
        self.ui.lineEdit_dataset_path.setText(dataset_path)
        
        self._initPageGeneral()
        self._initPageMicroscope()
        self._initPageCamera()
        self._initPageSpace()
        self._initPageHighOrderAberration()
        self._initPageLowOrderAberration()
        

    def _setMetaValue(self, key: str, widget: QWidget):
        """
        Set the initial value for the widget. Note that when this function is 
        called, the 4D-STEM dataset should have been assigned (because 
        meta_manager is bound with specific 4D-STEM dataset).

        arguments:
            key: (str) The key of the metadata.
            
            widget: (QWidget) The widget to set the value.
        """
        if key not in self.meta_manager.listSchemaKeys():
            raise KeyError(f"The key does not exist in the metadata schema: {key}")
        
        if key not in self.meta_manager.listKeys():
            return 
        
        meta_value = self.meta_manager.getValue(key)
        default_unit = self.meta_manager.getSchemaUnit(key)
        display_unit = self.meta_manager.getSchemaDisplayUnit(key)
        if display_unit and default_unit:
            meta_value = self.unit_manager.convert(meta_value, default_unit, display_unit)
            meta_value = f"{meta_value} {display_unit}"
        elif default_unit:
            meta_value = f"{meta_value} {default_unit}"
        else:
            meta_value = f"{meta_value}"

        if isinstance(widget, QLineEdit):
            widget.setText(str(meta_value))
        elif isinstance(widget, QPlainTextEdit):
            widget.setPlainText(str(meta_value))
        elif isinstance(widget, QLabel):
            widget.setText(str(meta_value))
        elif isinstance(widget, QDateEdit):
            widget.setDate(QDate.fromString(str(meta_value), "yyyy-MM-dd"))
        

    def _editMeta(self, key: str, display_widget: QWidget):
        """
        Open the edit metadata dialog for the given key.

        arguments:
            key: (str) The key of the metadata.
            
            display_widget: (QWidget) The widget to display the value.
        """
        dialog = DialogEditMeta(self)
        dialog.setItemPath(self._dataset_path)
        dialog.setMetaKey(key)
        if self.meta_manager.getValue(key):
            dialog.readMetaFromFile()
        else:
            dialog.readMetaFromSchema()
        
        if dialog.exec() == QDialog.Accepted:
            self._setMetaValue(key, display_widget)
            self.logger.info(f"Edited metadata {key}: {self.meta_manager.getValue(key)}")
            
    def _editMetaWrapper(self, key: str, widgets: dict):
        """
        Wrapper function to connect the edit button to the metadata editing 
        dialog.

        This function returns a lambda function that, when called, will open 
        the metadata editing dialog for the specified key and display widget.

        arguments:
            key: (str) The key of the metadata.
            
            widgets: (dict) A dictionary containing the display widget under the key 'display'.

        returns:
            (function) A lambda function that calls _editMeta with the specified 
                key and display widget.
        """
        return lambda k = key, w = widgets: self._editMeta(key, widgets['display'])


    def _initPageGeneral(self):
        self.general_metadata_map = {
            '/General/title': {
                'display': self.ui.label_general_title,
                'edit': self.ui.pushButton_edit_general_title,
            },
            '/General/authors': {
                'display': self.ui.label_general_authors,
                'edit': self.ui.pushButton_edit_general_authors,
            },
            '/General/notes': {
                'display': self.ui.label_general_notes,
                'edit': self.ui.pushButton_edit_general_notes,
            },
            '/General/data_path': {
                'display': self.ui.label_general_data_path,
                'edit': self.ui.pushButton_edit_general_data_path,
            },
            '/General/header_path': {
                'display': self.ui.label_general_header_path,
                'edit': self.ui.pushButton_edit_general_header_path,
            },
            '/General/time': {
                'display': self.ui.label_general_time,
                'edit': self.ui.pushButton_edit_general_time,
            },
            '/General/date': {
                'display': self.ui.label_general_date,
                'edit': self.ui.pushButton_edit_general_date,
            },
            '/General/time_zone': {
                'display': self.ui.label_general_time_zone,
                'edit': self.ui.pushButton_edit_general_time_zone,
            },
            '/General/doi': {
                'display': self.ui.label_general_doi,
                'edit': self.ui.pushButton_edit_general_doi,
            },
            '/General/fourd_explorer_version': {
                'display': self.ui.label_general_fourd_explorer_version,
                'edit': self.ui.pushButton_edit_general_fourd_explorer_version,
            }
        }

        for key, widgets in self.general_metadata_map.items():
            widgets['edit'].clicked.connect(self._editMetaWrapper(key, widgets))
            widgets['display'].setToolTip(self.meta_manager.getSchemaDescription(key))
            widgets['display'].setText("(None)")
            self._setMetaValue(key, widgets['display'])



    
    def _initPageMicroscope(self):
        self.microscope_metadata_map = {
            '/Acquisition/Microscope/name': {
                'display': self.ui.label_microscope_name,
                'edit': self.ui.pushButton_edit_microscope_name,
            },
            '/Acquisition/Microscope/manufacturer': {
                'display': self.ui.label_microscope_manufacturer,
                'edit': self.ui.pushButton_edit_microscope_manufacturer,
            },
            '/Acquisition/Microscope/accelerate_voltage': {
                'display': self.ui.label_accelerate_voltage,
                'edit': self.ui.pushButton_edit_accelerate_voltage,
            },
            '/Acquisition/Microscope/beam_current': {
                'display': self.ui.label_beam_current,
                'edit': self.ui.pushButton_edit_beam_current,
            },
            '/Acquisition/Microscope/camera_length': {
                'display': self.ui.label_camera_length,
                'edit': self.ui.pushButton_edit_camera_length,
            },
            '/Acquisition/Microscope/convergence_angle': {
                'display': self.ui.label_convergence_angle,
                'edit': self.ui.pushButton_edit_convergent_angle,
            },
            '/Acquisition/Microscope/magnification': {
                'display': self.ui.label_magnification,
                'edit': self.ui.pushButton_edit_magnification,
            },
            '/Acquisition/Microscope/dwell_time': {
                'display': self.ui.label_dwell_time,
                'edit': self.ui.pushButton_edit_dwell_time,
            },
            '/Acquisition/Microscope/step_size_i': {
                'display': self.ui.label_step_size_i,
                'edit': self.ui.pushButton_edit_step_size_i,
            },
            '/Acquisition/Microscope/step_size_j': {
                'display': self.ui.label_step_size_j,
                'edit': self.ui.pushButton_edit_step_size_j,
            },
            '/Acquisition/Microscope/acquisition_date': {
                'display': self.ui.label_acquisition_date,
                'edit': self.ui.pushButton_edit_acquisition_date,
            },
            '/Acquisition/Microscope/acquisition_location': {
                'display': self.ui.label_acquisition_location,
                'edit': self.ui.pushButton_edit_acquisition_location,
            },
            '/Acquisition/Microscope/acquisition_timezone': {
                'display': self.ui.label_acquisition_timezone,
                'edit': self.ui.pushButton_edit_acquisition_timezone,
            },
        }
        self.ui.label_microscope_manufacturer.setText("(None)")
        self.ui.label_microscope_name.setText("(None)")
        self.ui.label_acquisition_location.setText("(None)")
        self.ui.label_acquisition_date.setText("(None)")
        self.ui.label_acquisition_timezone.setText("(None)")
        for key, widgets in self.microscope_metadata_map.items():
            widgets['edit'].clicked.connect(self._editMetaWrapper(key, widgets))
            widgets['display'].setToolTip(self.meta_manager.getSchemaDescription(key))
            self._setMetaValue(key, widgets['display'])

        
    
        
    def _initPageCamera(self):
        self.camera_metadata_map = {
            '/Acquisition/Camera/name': {
                'display': self.ui.label_camera_name,
                'edit': self.ui.pushButton_edit_camera_name,
            },
            '/Acquisition/Camera/manufacturer': {
                'display': self.ui.label_camera_manufacturer,
                'edit': self.ui.pushButton_edit_camera_manufacturer,
            },
            '/Acquisition/Camera/pixel_number_i': {
                'display': self.ui.label_camera_pixel_number_i,
                'edit': self.ui.pushButton_pixel_number_i,
            },
            '/Acquisition/Camera/pixel_number_j': {
                'display': self.ui.label_camera_pixel_number_j,
                'edit': self.ui.pushButton_pixel_number_j,
            },
            '/Acquisition/Camera/pixel_size_i': {
                'display': self.ui.label_camera_pixel_size_i,
                'edit': self.ui.pushButton_edit_camera_pixel_size_i,
            },
            '/Acquisition/Camera/pixel_size_j': {
                'display': self.ui.label_camera_pixel_size_j,
                'edit': self.ui.pushButton_edit_camera_pixel_size_j,
            },
        }
        self.ui.label_camera_name.setText("(None)")
        self.ui.label_camera_manufacturer.setText("(None)")
        for key, widgets in self.camera_metadata_map.items():
            widgets['edit'].clicked.connect(self._editMetaWrapper(key, widgets))
            widgets['display'].setToolTip(self.meta_manager.getSchemaDescription(key))
            self._setMetaValue(key, widgets['display'])

        

    def _initPageSpace(self):
        self.space_metadata_map = {
            '/Calibration/Space/scan_dr_i': {
                'display': self.ui.label_scan_dr_i,
                'edit': self.ui.pushButton_edit_scan_dr_i,
            },
            '/Calibration/Space/scan_dr_j': {
                'display': self.ui.label_scan_dr_j,
                'edit': self.ui.pushButton_edit_scan_dr_j,
            },
            '/Calibration/Space/du_i': {
                'display': self.ui.label_du_i,
                'edit': self.ui.pushButton_edit_du_i,
            },
            '/Calibration/Space/du_j': {
                'display': self.ui.label_du_j,
                'edit': self.ui.pushButton_edit_du_j,
            },
            '/Calibration/Space/dr_i': {
                'display': self.ui.label_dr_i,
                'edit': self.ui.pushButton_edit_dr_i,
            },
            '/Calibration/Space/dr_j': {
                'display': self.ui.label_dr_j,
                'edit': self.ui.pushButton_edit_dr_j,
            },
            '/Calibration/Space/dp_i': {
                'display': self.ui.label_dp_i,
                'edit': None,
            },
            '/Calibration/Space/dp_j': {
                'display': self.ui.label_dp_j,
                'edit': None,
            },
            '/Calibration/Space/scan_i': {
                'display': self.ui.label_scan_i,
                'edit': None,
            },
            '/Calibration/Space/scan_j': {
                'display': self.ui.label_scan_j,
                'edit': None,
            },
        }
        
        for key, widgets in self.space_metadata_map.items():
            if widgets['edit'] is not None:
                widgets['edit'].clicked.connect(self._editMetaWrapper(key, widgets))
                widgets['display'].setToolTip(self.meta_manager.getSchemaDescription(key))
            self._setMetaValue(key, widgets['display'])
    
    
    def _initPageHighOrderAberration(self):
        self.low_order_aberration_metadata_map = {
            '/Aberration/C1': {
                'display': self.ui.label_C1,
                'edit': self.ui.pushButton_edit_C1,
            },
            '/Aberration/A1': {
                'display': self.ui.label_A1,
                'edit': self.ui.pushButton_edit_A1,
            },
            '/Aberration/B2': {
                'display': self.ui.label_B2,
                'edit': self.ui.pushButton_edit_B2,
            },
            '/Aberration/A2': {
                'display': self.ui.label_A2,
                'edit': self.ui.pushButton_edit_A2,
            },
            '/Aberration/C3': {
                'display': self.ui.label_C3,
                'edit': self.ui.pushButton_edit_C3,
            },
            '/Aberration/S3': {
                'display': self.ui.label_S3,
                'edit': self.ui.pushButton_edit_S3,
            },
            '/Aberration/A3': {
                'display': self.ui.label_A3,
                'edit': self.ui.pushButton_edit_A3,
            },
        }
        for key, widgets in self.low_order_aberration_metadata_map.items():
            widgets['edit'].clicked.connect(self._editMetaWrapper(key, widgets))
            widgets['display'].setToolTip(self.meta_manager.getSchemaDescription(key))
            self._setMetaValue(key, widgets['display'])
            
        self.low_order_aberration_angle_metadata_map = {
            '/AberrationAngle/C1': {
                'display': self.ui.label_C1_angle,
                'edit': self.ui.pushButton_edit_C1_angle,
            },
            '/AberrationAngle/A1': {
                'display': self.ui.label_A1_angle,
                'edit': self.ui.pushButton_edit_A1_angle,
            },
            '/AberrationAngle/B2': {
                'display': self.ui.label_B2_angle,
                'edit': self.ui.pushButton_edit_B2_angle,
            },
            '/AberrationAngle/A2': {
                'display': self.ui.label_A2_angle,
                'edit': self.ui.pushButton_edit_A2_angle,
            },
            '/AberrationAngle/C3': {
                'display': self.ui.label_C3_angle,
                'edit': self.ui.pushButton_edit_C3_angle,
            },
            '/AberrationAngle/S3': {
                'display': self.ui.label_S3_angle,
                'edit': self.ui.pushButton_edit_S3_angle,
            },
            '/AberrationAngle/A3': {
                'display': self.ui.label_A3_angle,
                'edit': self.ui.pushButton_edit_A3_angle,
            },
        }
        for key, widgets in self.low_order_aberration_angle_metadata_map.items():
            widgets['edit'].clicked.connect(self._editMetaWrapper(key, widgets))
            widgets['display'].setToolTip(self.meta_manager.getSchemaDescription(key))
            self._setMetaValue(key, widgets['display'])
        
    
    
    def _initPageLowOrderAberration(self):
        self.high_order_aberration_metadata_map = {
            '/Aberration/B4': {
                'display': self.ui.label_B4,
                'edit': self.ui.pushButton_edit_B4,
            },
            '/Aberration/D4': {
                'display': self.ui.label_D4,
                'edit': self.ui.pushButton_edit_D4,
            },
            '/Aberration/A4': {
                'display': self.ui.label_A4,
                'edit': self.ui.pushButton_edit_A4,
            },
            '/Aberration/C5': {
                'display': self.ui.label_C5,
                'edit': self.ui.pushButton_edit_C5,
            },
            '/Aberration/A5': {
                'display': self.ui.label_A5,
                'edit': self.ui.pushButton_edit_A5,
            },
        }
        for key, widgets in self.high_order_aberration_metadata_map.items():
            widgets['edit'].clicked.connect(self._editMetaWrapper(key, widgets))
            widgets['display'].setToolTip(self.meta_manager.getSchemaDescription(key))
            self._setMetaValue(key, widgets['display'])
        self.high_order_aberration_angle_metadata_map = {
            '/AberrationAngle/B4': {
                'display': self.ui.label_B4_angle,
                'edit': self.ui.pushButton_edit_B4_angle,
            },
            '/AberrationAngle/D4': {
                'display': self.ui.label_D4_angle,
                'edit': self.ui.pushButton_edit_D4_angle,
            },
            '/AberrationAngle/A4': {
                'display': self.ui.label_A4_angle,
                'edit': self.ui.pushButton_edit_A4_angle,
            },
            '/AberrationAngle/C5': {
                'display': self.ui.label_C5_angle,
                'edit': self.ui.pushButton_edit_C5_angle,
            },
            '/AberrationAngle/A5': {
                'display': self.ui.label_A5_angle,
                'edit': self.ui.pushButton_edit_A5_angle,
            },
        }
        for key, widgets in self.high_order_aberration_angle_metadata_map.items():
            widgets['edit'].clicked.connect(self._editMetaWrapper(key, widgets))
            widgets['display'].setToolTip(self.meta_manager.getSchemaDescription(key))
            self._setMetaValue(key, widgets['display'])
    



