#-*- coding: utf-8 -*- 

"""
*-------------------------- WidgetAlignmentManual.py ----------------------------*

对 4D-STEM 衍射图样进行手动平移、合轴的部件。

提升部件：
    - 提升类名 WidgetAlignmentManual
    - 头文件 bin.Widgets.WidgetAlignmentManual

作者:           胡一鸣
创建日期:       2024年9月2日

The widget to align 4D-STEM dataset manually.

Promoted Widget:
    - name of widget class: WidgetAlignmentManual
    - header file: bin.Widgets.WidgetAlignmentManual

author:         Hu Yiming
date:           Sep 2, 2024
*-------------------------- WidgetAlignmentManual.py ----------------------------*
"""

from logging import Logger

from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QToolBar
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QTableWidgetItem 
from PySide6.QtWidgets import QSpinBox
from PySide6.QtWidgets import QInputDialog
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QDialogButtonBox
from PySide6.QtWidgets import QRadioButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtCore import QObject

import numpy as np
from matplotlib.image import AxesImage
from matplotlib.axes import Axes 
from h5py import Dataset
from scipy.optimize import curve_fit


from bin.BlitManager import BlitManager
from bin.UIManager import ThemeHandler
from bin.HDFManager import HDFHandler
from bin.HDFManager import HDFType
from bin.Widgets.DialogSaveItem import DialogSaveVectorField
# from bin.Widgets.DialogCreateItem import DialogHDFCreate
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from ui import uiWidgetAlignmentManual


def strToTuple(string: str, length: int = 2):
    """
    Convert a string in the format "(2, -4)" to a tuple. The numbers can be either int or float. The length of the tuple must be 2 in default.

    arguments:
        string: (str) The string to convert.
        
        length: (int) The length of the tuple. Default is 2.

    returns:
        tuple: The converted tuple.
    """
    try:
        # Remove the parentheses and split by comma
        stripped_string = string.strip('()')
        parts = stripped_string.split(',')
        
        # Convert each part to the appropriate type (int or float)
        tuple_values = []
        for part in parts:
            part = part.strip()
            if '.' in part:
                tuple_values.append(float(part))
            else:
                tuple_values.append(int(part))
        if length != len(tuple_values): 
            raise ValueError("Invalid tuple length")
        return tuple(tuple_values)
    except Exception as e:
        raise ValueError(f"Invalid string format for tuple conversion: {string}") from e


class WidgetAlignmentManual(QWidget):
    """
    Align the 4D-STEM diffraction patterns manually.
    """
    def __init__(self, parent: QWidget=None):
        """
        Initialize the widget. The parent widget should have scan_ii and scan_jj attributes, which indicates the current scan position.
        """
        super().__init__(parent)
        self.ui = uiWidgetAlignmentManual.Ui_Form()
        self.ui.setupUi(self)
        self._shift_i_dict = {}
        self._shift_j_dict = {}
        self._initUi()
        self._initTableWidget()
        
    
    @property
    def current_dp_location(self):
        return (self.scan_ii, self.scan_jj)
    
    @property
    def current_shift_i(self):  # Current measured shift 
        return - self.ui.doubleSpinBox_manual_shift_i.value()

    @property
    def current_shift_j(self):  # Current measured shift
        return - self.ui.doubleSpinBox_manual_shift_j.value()

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
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler

    def _initTableWidget(self):
        """
        初始化 Table widget, 添加 Action Button 以及相应的 toolbar，里面包含有增加、删除、修改按钮。其中，增加按钮可将页面当前展示的衍射图像的位置以及衍射图像对应的平移量给保存下来；删除按钮可将列表中当前选定的项给删除掉；修改按钮可修改列表中当前选定的项。

        Initialize the table widget, and add the action button and the corresponding toolbar, which contains the add, delete, and modify buttons. The add button can save the position of the current diffraction image and the shift amount of the diffraction image; the delete button can delete the current item in the list; the modify button can modify the current item in the list.
        """
        self.ui.tableWidget_manual_sample.setColumnCount(2)
        self.ui.tableWidget_manual_sample.setHorizontalHeaderLabels(['location', 'shift'])
        self.ui.tableWidget_manual_sample.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_manual_sample.setRowCount(0)
        self.ui.tableWidget_manual_sample.setEditTriggers(QTableWidget.NoEditTriggers)

        self._table_widget_toolbar = QToolBar()

        self._action_add = ActionAddAnchor(self)
        self._action_add.setWidgetAlignmentManual(self)
        self._action_delete = ActionDeleteAnchor(self)
        self._action_delete.setWidgetAlignmentManual(self)
        self._action_modify = ActionModifyAnchor(self)
        self._action_modify.setWidgetAlignmentManual(self)
        self._action_import = ActionImportAnchor(self)
        self._action_import.setWidgetAlignmentManual(self)
        self._action_export = ActionExportAnchor(self)
        self._action_export.setWidgetAlignmentManual(self)
        self._table_widget_toolbar.addAction(self._action_add)
        self._table_widget_toolbar.addAction(self._action_delete)
        self._table_widget_toolbar.addAction(self._action_modify)
        self._table_widget_toolbar.addAction(self._action_import)
        self._table_widget_toolbar.addAction(self._action_export)
        self.ui.groupBox_sample_records.layout().insertWidget(0, self._table_widget_toolbar)  


    def _initUi(self):
        """
        Initialize Ui and their signal-slot connections.
        """
        self.ui.checkBox_show_shifted_dp.setChecked(True)
        self.ui.doubleSpinBox_manual_shift_i.setValue(0)
        self.ui.doubleSpinBox_manual_shift_j.setValue(0)
        self.ui.doubleSpinBox_manual_shift_i.setRange(-16384, 16384)
        self.ui.doubleSpinBox_manual_shift_j.setRange(-16384, 16384)

        self.ui.checkBox_show_shifted_dp.stateChanged.connect(self._onShowShiftedDPChanged)
        self.ui.doubleSpinBox_manual_shift_i.valueChanged.connect(self._onShiftIChanged)
        self.ui.doubleSpinBox_manual_shift_j.valueChanged.connect(self._onShiftJChanged)
        self.ui.pushButton_down.clicked.connect(self._onDownButtonClicked)
        self.ui.pushButton_up.clicked.connect(self._onUpButtonClicked)
        self.ui.pushButton_left.clicked.connect(self._onLeftButtonClicked)
        self.ui.pushButton_right.clicked.connect(self._onRightButtonClicked)
        self.ui.pushButton_generate_shift_vec.clicked.connect(self.generateShiftMapping)
        
        self.ui.label_measured_shift.setText('(0, 0)')
        
        
    def setParentAlignPage(self, align_page: QWidget):
        """
        Set the parent alignment page.

        arguments:
            align_page: (PageAlignFourDSTEM) The parent alignment page containing the 4D-STEM data and UI elements.
        """
        self._align_page = align_page 
        
        
    def getCurrentDPShiftVec(self):
        """
        Get the current measured shift vector of the current diffraction pattern.
        """
        return (self.current_shift_i, self.current_shift_j)
    
    
    def getCurrentShowShiftedDP(self):
        """
        Get the current state of the 'Show Shifted DP' checkbox.
        """
        return self.ui.checkBox_show_shifted_dp.isChecked()


    def _onShowShiftedDPChanged(self):
        """
        Handle the state change of the 'Show Shifted DP' checkbox.
        """
        self.ui.label_measured_shift.setText(f'({self.current_shift_i}, {self.current_shift_j})')
        self._align_page._updateDP()
            

    def _onShiftIChanged(self):
        """
        Handle the change of the shift i value.

        arguments:
            value: (int) The new value of the shift i.
        """
        self._onShowShiftedDPChanged()
    
    
    def _onShiftJChanged(self):
        """
        Handle the change of the shift j value.

        arguments:
            value: (int) The new value of the shift j.
        """
        self._onShowShiftedDPChanged()
    
    
    def _onDownButtonClicked(self):
        """
        Handle the click of the down button.
        """
        self.ui.doubleSpinBox_manual_shift_i.setValue(self.ui.doubleSpinBox_manual_shift_i.value() + 1)
        
        
    def _onUpButtonClicked(self):
        """
        Handle the click of the up button.
        """
        self.ui.doubleSpinBox_manual_shift_i.setValue(self.ui.doubleSpinBox_manual_shift_i.value() - 1)
    
    
    def _onLeftButtonClicked(self):
        """
        Handle the click of the left button.
        """
        self.ui.doubleSpinBox_manual_shift_j.setValue(self.ui.doubleSpinBox_manual_shift_j.value() - 1)
    
    
    def _onRightButtonClicked(self):
        """ 
        Handle the click of the right button.
        """
        self.ui.doubleSpinBox_manual_shift_j.setValue(self.ui.doubleSpinBox_manual_shift_j.value() + 1)
    
    
    def generateShiftMapping(self):
        """
        Handle the click of the generate shift vector button.
        
        A dialog will pop up to let user to choose which method to generate the shift vector. Methods include:
            - Apply the current shift vector to all the diffraction patterns.
            - Use the current anchors to generate the shift vector fields with linear regression.
            - Use the current anchors to generate the shift vector fields with quadratic polynomial.
        """
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape
        _dialog_generate_shift_map = GenerateShiftVectorDialog()
        result = _dialog_generate_shift_map.exec()
        if result == QDialog.Accepted:
            if _dialog_generate_shift_map.radio_button_apply_current_shift_vec.isChecked():
                shift_map = self._useCurrentShiftVec()
            elif _dialog_generate_shift_map.radio_button_linear_regression.isChecked():
                shift_map = self._useLinearRegression()
            elif _dialog_generate_shift_map.radio_button_quadratic_polynomial.isChecked():
                shift_map = self._useQuadraticPolynomial()
        
        # create a new vector field to store the shift map
        save_dialog = DialogSaveVectorField(self)
        save_dialog.setParentPath(self.data_object.parent.name)
        result = save_dialog.exec()
        if result == QDialog.Accepted:
            group_path = save_dialog.getParentPath()
            item_name = save_dialog.getNewName()
            full_path = f"{group_path}/{item_name}"
            self.hdf_handler.addNewData(group_path, item_name, shape=(2, scan_i, scan_j))
            shift_map_dataset = self.hdf_handler.file[full_path]
            shift_map_dataset[:] = shift_map

            # save the method used to generate the shift map in the attributes
            if _dialog_generate_shift_map.radio_button_apply_current_shift_vec.isChecked():
                shift_map_dataset.attrs['Alignment/InterpolationMethod'] = "Shift Vector Broadcast"
            elif _dialog_generate_shift_map.radio_button_linear_regression.isChecked():
                shift_map_dataset.attrs['Alignment/InterpolationMethod'] = "Linear Regression"
                self._saveShiftAnchorsInAttrs(shift_map_dataset)
            elif _dialog_generate_shift_map.radio_button_quadratic_polynomial.isChecked():
                shift_map_dataset.attrs['Alignment/InterpolationMethod'] = "Quadratic Polynomial Regression"
                self._saveShiftAnchorsInAttrs(shift_map_dataset)
            shift_map_dataset['Alignment/Method'] = "Manual"
            shift_map_dataset['Alignment/TargetDatasetPath'] = self._align_page.data_path 
            # TODO 还需要加上一些属性，例如 General 以及 Space 的信息
            self.logger.info(f"Shift map created at {full_path}")
            
            
    def _useCurrentShiftVec(self):
        """
        Use the current shift vector to shift all the diffraction patterns.
        """
        current_shift_i = self.current_shift_i
        current_shift_j = self.current_shift_j
        shift_map = np.ones((2, self.scan_ii, self.scan_jj,)) 
        shift_map[0, :, :] *= current_shift_i
        shift_map[1, :, :] *= current_shift_j 
        return shift_map


    def _useLinearRegression(self):
        """
        Use the current anchors in the table to generate the shift vector fields 
        with linear regression.
        """
        anchor_locations, anchor_shifts = self._getAnchorLists()
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape

        # Generate the shift map
        shift_map = np.zeros((2, scan_i, scan_j))
        
        def linear_model(x, a, b, c):
            return a * x[0] + b * x[1] + c

        def fit_linear_model(locations, shifts):
            popt, _ = curve_fit(linear_model, locations.T, shifts)
            return popt

        i_params = fit_linear_model(anchor_locations, anchor_shifts[:, 0])
        j_params = fit_linear_model(anchor_locations, anchor_shifts[:, 1])

        # Generate the shift map using the fitted models
        i_grid, j_grid = np.meshgrid(np.arange(scan_i), np.arange(scan_j), indexing='ij')
        locations = np.vstack([i_grid.ravel(), j_grid.ravel()]).T
        shift_map[0] = linear_model(locations.T, *i_params).reshape(scan_i, scan_j)
        shift_map[1] = linear_model(locations.T, *j_params).reshape(scan_i, scan_j)

        return shift_map


    def _useQuadraticPolynomial(self):
        """
        Use the current anchors in the table to generate the shift vector fields 
        with quadratic polynomial.
        """
        anchor_locations, anchor_shifts = self._getAnchorLists()
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape

        # Generate the shift map
        shift_map = np.zeros((2, scan_i, scan_j))
        
        def quadratic_model(x, a, b, c, d, e, f):
            return a * x[0]**2 + b * x[1]**2 + c * x[0] * x[1] + d * x[0] + e * x[1] + f

        def fit_quadratic_model(locations, shifts):
            popt, _ = curve_fit(quadratic_model, locations.T, shifts)
            return popt

        i_params = fit_quadratic_model(anchor_locations, anchor_shifts[:, 0])
        j_params = fit_quadratic_model(anchor_locations, anchor_shifts[:, 1])

        # Generate the shift map using the fitted models
        i_grid, j_grid = np.meshgrid(np.arange(scan_i), np.arange(scan_j), indexing='ij')
        locations = np.vstack([i_grid.ravel(), j_grid.ravel()]).T
        shift_map[0] = quadratic_model(locations.T, *i_params).reshape(scan_i, scan_j)
        shift_map[1] = quadratic_model(locations.T, *j_params).reshape(scan_i, scan_j)

        return shift_map
        
            
    def _saveShiftAnchorsInAttrs(self, vec_object: Dataset):
        """
        Save the current shift anchors in the attributes of the widget.
        """
        table_widget = self.ui.tableWidget_manual_sample
        anchor_locations = []
        anchor_shifts = []
        for i in range(table_widget.rowCount()):
            try:
                anchor_location_str = table_widget.item(i, 0).text()
                anchor_shift_str = table_widget.item()
                anchor_location = strToTuple(anchor_location_str)
                anchor_shift = strToTuple(anchor_shift_str)
                anchor_locations.append(anchor_location)
                anchor_shifts.append(anchor_shift)
            except (ValueError, AttributeError):
                self.logger.warning(
                    f"Invalid entry at row {i + 1} in the table widget."
                )
            
        # Save the anchors in the attributes
        for anchor_location, anchor_shift in zip(anchor_locations, anchor_shifts):
            location_str = str(anchor_location).replace(" ", "")
            shift_str = str(anchor_shift).replace(" ", "")
            vec_object.attrs[f"/Alignment/ShiftAnchors/{location_str}"] = shift_str
        
        
    def _getAnchorLists(self) -> tuple[np.ndarray, np.ndarray]:
        """
        Retrieve the list of anchor locations and their corresponding shift values from the table widget.

        Returns:
            (tuple[np.ndarray, np.ndarray]) A tuple containing two numpy array:
            
                - anchor_locations: A numpy array containing all anchor locations, which shape is (n, 2). n is the number of anchors.
                
                - anchor_shifts: A numpy array containing all anchor shifts, which shape is (n, 2). n is the number of anchors.

        Raises:
            ValueError: If the string format of the anchor location or shift value is invalid.
            
            AttributeError: If any item in the table widget is missing.
        """
        table_widget = self.ui.tableWidget_manual_sample
        anchor_locations = []
        anchor_shifts = []
        for i in range(table_widget.rowCount()):
            try:
                anchor_location_str = table_widget.item(i, 0).text()
                anchor_shift_str = table_widget.item(i, 1).text()
                anchor_location = strToTuple(anchor_location_str)
                anchor_shift = strToTuple(anchor_shift_str)
                anchor_locations.append(anchor_location)
                anchor_shifts.append(anchor_shift)
            except ValueError:
                self.logger.warning(f"Invalid string format at row {i + 1} in the table widget.")
                QMessageBox.warning(self, "Invalid Entry", f"Invalid string format at row {i + 1}. Please check the format.")
            except AttributeError:
                self.logger.warning(f"Missing item at row {i + 1} in the table widget.")
                QMessageBox.warning(self, "Missing Entry", f"Missing item at row {i + 1}. Please ensure all cells are filled.")
        anchor_locations = np.array(anchor_locations)
        anchor_shifts = np.array(anchor_shifts)
        return anchor_locations, anchor_shifts


class ActionShiftAnchorBase(QAction):
    """
    操作表格中的平移锚点的基础类。
    
    The base class for operating the shift anchor in the table.
    """
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.theme_handler.theme_changed.connect(
            self._updateIcon
        )
        
    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler

    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger
    
    @property
    def widget_alignment_manual(self) -> WidgetAlignmentManual:
        return self._widget_alignment_manual
    
    @property
    def table_widget(self) -> QTableWidget:
        return self.widget_alignment_manual.ui.tableWidget_manual_sample
    
    def setWidgetAlignmentManual(self, widget_alignment_manual: WidgetAlignmentManual):
        """
        Set the linked widget alignment manual.

        arguments:
            widget_alignment_manual: (WidgetAlignmentManual) The widget alignment manual to be linked.
        """
        self._widget_alignment_manual = widget_alignment_manual
        
    def _updateIcon(self):
        """
        Will update the icon when the theme mode changes.
        """
        if self._icon_name:
            _path = ':/HDFEdit/resources/icons/' + self._icon_name
            icon = self.theme_handler.iconProvider(_path)
            self.setIcon(icon)
            
    def initIconResources(self, icon_name: str):
        """
        Initialize the resource of icons.

        arguments:
            icon_name: (str) the name of icon.
        """
        _path = ':/HDFEdit/resources/icons/' + icon_name
        icon = self.theme_handler.iconProvider(_path)
        self._icon_name = icon_name 
        self.setIcon(icon)
    

class ActionAddAnchor(ActionShiftAnchorBase):
    """
    添加锚点。
    
    Add anchor.
    """
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.setText('Add')
        self.initIconResources('file_add')
        self.triggered.connect(self.addItem)
        
    def addItem(self):
        """
        Add the current displaying item that include the diffraction pattern's location and shift. If the location already exists, it will ask whether to update it.
        """
        current_location = self.widget_alignment_manual.current_dp_location
        current_shift_i = self.widget_alignment_manual.current_shift_i
        current_shift_j = self.widget_alignment_manual.current_shift_j
        
        current_location_str = str(current_location)
        current_shift_str = str((current_shift_i, current_shift_j))
        
        for row in range(self.table_widget.rowCount()):
            location_item = self.table_widget.item(row, 0)
            shift_item = self.table_widget.item(row, 1)
            
            if location_item and location_item.text() == current_location_str:
                if shift_item and shift_item.text() != current_shift_str:
                    msgbox = QMessageBox()
                    msgbox.setIcon(QMessageBox.Question)
                    msgbox.setText(f'The location {current_location_str} already exists with a different shift. Do you want to update it?')
                    msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    msgbox.setDefaultButton(QMessageBox.No)
                    result = msgbox.exec()
                    if result == QMessageBox.Yes:
                        self.table_widget.setItem(row, 1, QTableWidgetItem(current_shift_str))
                return
        
        self.table_widget.insertRow(self.table_widget.rowCount())
        self.table_widget.setItem(self.table_widget.rowCount() - 1, 0, QTableWidgetItem(current_location_str))
        self.table_widget.setItem(self.table_widget.rowCount() - 1, 1, QTableWidgetItem(current_shift_str))
        


class ActionDeleteAnchor(ActionShiftAnchorBase):
    """
    删除锚点。
    
    Delete anchor.
    """
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.setText('Delete')
        self.initIconResources('file_delete')
        self.triggered.connect(self.deleteItem)

    def deleteItem(self):
        """
        Delete the current selected item.
        """
        current_index = self.table_widget.currentRow()
        if current_index < 0:
            return
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Question)
        msgbox.setText('Are you sure to delete the current selected item?')
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgbox.setDefaultButton(QMessageBox.No)
        result = msgbox.exec()
        if result == QMessageBox.Yes:
            self.table_widget.removeRow(current_index)

class ActionModifyAnchor(ActionShiftAnchorBase):
    """
    修改锚点。
    
    Modify anchor.
    """
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.setText('Modify')
        self.initIconResources('edit')
        self.triggered.connect(self.modifyItem)

    def modifyItem(self):
        """
        Modify the current selected item.
        """
        current_index = self.table_widget.currentRow()
        if current_index < 0:
            return
        modify_dialog = ModifyAnchorDialog(parent = None, table_widget = self.table_widget, current_index = current_index)
        result = modify_dialog.exec()
        if result == QDialog.Accepted:
            shift_i = modify_dialog.shift_i_input.value()
            shift_j = modify_dialog.shift_j_input.value()
            self.table_widget.setItem(current_index, 1, QTableWidgetItem(str((shift_i, shift_j))))
        

        
class ActionExportAnchor(ActionShiftAnchorBase):
    """
    导出锚点。
    
    Export anchor.
    """
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.setText('Export')
        self.initIconResources('export')
        self.triggered.connect(self.exportItem)

    def exportItem(self):
        """
        Export the anchors in the table.
        """
        return self.widget_alignment_manual.generateShiftMapping()



class ActionImportAnchor(ActionShiftAnchorBase):
    """
    导入锚点。
    
    Import anchor.
    """
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.setText('Import')
        self.initIconResources('import')
        self.triggered.connect(self.importItem)

    def importItem(self):
        """
        Import anchors into the table.
        """
        dialog = DialogHDFChoose(self)
        if dialog.exec() != QDialog.Accepted:
            return
        
        dataset_path = dialog.getCurrentPath()
        try:
            dataset = self.hdf_handler.file[dataset_path]
            self._validateDataset(dataset)
            anchor_locations, anchor_shifts = self._parseAnchors(dataset)
            self._handleExistingRecords(anchor_locations, anchor_shifts)
        except (KeyError, ValueError, TypeError) as e:
            self._handleError(e)

    def _validateDataset(self, dataset: Dataset):
        """
        Validate if the dataset contains the required attributes.
        
        arguments:
            dataset: (Dataset) The dataset to validate.
        
        raises:
            ValueError: If the dataset does not contain the required attributes.
        """
        if 'Alignment/ManualMethod' not in dataset.attrs:
            raise ValueError("The selected dataset does not contain the required attributes.")

    def _parseAnchors(self, dataset: Dataset) -> tuple[list, list]:
        """
        Parse the anchor locations and shifts from the dataset.
        
        arguments:
            dataset: (Dataset) The dataset to parse.
        
        returns:
            tuple[list, list]: A tuple containing lists of anchor locations and shifts.
        """
        anchor_locations = [strToTuple(loc) for loc in dataset.attrs['Alignment/ManualMethod']]
        anchor_shifts = [strToTuple(shift) for shift in dataset.attrs['Alignment/ManualMethod']]
        return anchor_locations, anchor_shifts

    def _handleExistingRecords(self, anchor_locations: list, anchor_shifts: list):
        """
        Handle existing records in the table.
        
        arguments:
            anchor_locations: (list) List of anchor locations.
            
            anchor_shifts: (list) List of anchor shifts.
        """
        if self.table_widget.rowCount() > 0:
            result = self._showConfirmationDialog()
            if result == 3:  # Cancel
                return
            self._processImport(anchor_locations, anchor_shifts, result)
        else:
            self._processImport(anchor_locations, anchor_shifts, 0)  # Replace existing records

    def _showConfirmationDialog(self) -> int:
        """
        Show a confirmation dialog to handle existing records.
        
        returns:
            int: The user's choice from the dialog.
        """
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirm Import")
        msg_box.setText("The table already contains some records. How would you like to proceed?")
        msg_box.addButton("Replace existing records", QMessageBox.YesRole)
        msg_box.addButton("Append and replace duplicates", QMessageBox.NoRole)
        msg_box.addButton("Append and keep duplicates", QMessageBox.ActionRole)
        msg_box.addButton("Cancel", QMessageBox.RejectRole)
        return msg_box.exec()

    def _processImport(self, anchor_locations: list, anchor_shifts: list, result: int):
        """
        Process the imported anchors based on the user's choice.
        
        arguments:
            anchor_locations: (list) List of anchor locations.
            
            anchor_shifts: (list) List of anchor shifts.
            
            result: (int) The user's choice from the confirmation dialog.
        """
        if result == 0:  # Replace existing records
            self.table_widget.setRowCount(0)
        for loc, shift in zip(anchor_locations, anchor_shifts):
            if result == 1:  # Append and replace duplicates
                self._appendAndReplaceDuplicates(loc, shift)
            elif result == 2:  # Append and keep duplicates
                self._appendAndKeepDuplicates(loc, shift)
            else:  # Replace existing records
                self._appendNewRecord(loc, shift)

    def _appendAndReplaceDuplicates(self, loc: tuple, shift: tuple):
        """
        Append new records and replace duplicate records.
        
        arguments:
            loc: (tuple) The anchor location.
            
            shift: (tuple) The anchor shift.
        """
        for row in range(self.table_widget.rowCount()):
            if self.table_widget.item(row, 0).text() == str(loc):
                self.table_widget.setItem(row, 1, QTableWidgetItem(str(shift)))
                break
        else:
            self._appendNewRecord(loc, shift)

    def _appendAndKeepDuplicates(self, loc: tuple, shift: tuple):
        """
        Append new records and keep duplicate records.
        
        arguments:
            loc: (tuple) The anchor location.
            
            shift: (tuple) The anchor shift.
        """
        if str(loc) not in [self.table_widget.item(row, 0).text() for row in range(self.table_widget.rowCount())]:
            self._appendNewRecord(loc, shift)

    def _appendNewRecord(self, loc: tuple, shift: tuple):
        """
        Append a new record.
        
        arguments:
            loc: (tuple) The anchor location.
            
            shift: (tuple) The anchor shift.
        """
        self.table_widget.insertRow(self.table_widget.rowCount())
        self.table_widget.setItem(self.table_widget.rowCount() - 1, 0, QTableWidgetItem(str(loc)))
        self.table_widget.setItem(self.table_widget.rowCount() - 1, 1, QTableWidgetItem(str(shift)))

    def _handleError(self, e: Exception):
        """
        Handle errors during anchor import.
        
        arguments:
            e: (Exception) The exception to handle.
        """
        self.logger.error(f'Error importing anchors: {e}', exc_info=True)
        msg = QMessageBox(parent=self)
        msg.setWindowTitle('Warning')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setText(f'Cannot import anchors: {e}')
        msg.exec()



class ModifyAnchorDialog(QDialog):
    """
    修改锚点对话框。
    
    Modify anchor dialog.
    """
    def __init__(self, parent: QWidget = None, table_widget: QTableWidget = None, current_index: int = None):
        """
        Initialize the dialog.
        
        arguments:
            parent: (QWidget) The parent widget.
        """
        super().__init__(parent)
        
        self._current_index = current_index
        self._table_widget = table_widget
        self.initUi()


    def initUi(self):
        """
        Initialize the UI.
        """
        self.setWindowTitle('Modify Anchor')
        self.setModal(True)
        layout = QVBoxLayout()
        
        location_label = QLabel(f'Location: {self._table_widget.item(self._current_index, 0).text()}')
        layout.addWidget(location_label)
        
        shift_i_label = QLabel('Shift i:')
        shift_i_input = QSpinBox()
        shift_i_input.setValue(strToTuple(self._table_widget.item(self._current_index, 1).text())[0])
        layout.addWidget(shift_i_label)
        layout.addWidget(shift_i_input)
        
        shift_j_label = QLabel('Shift j:')
        shift_j_input = QSpinBox()
        shift_j_input.setValue(strToTuple(self._table_widget.item(self._current_index, 1).text())[1])
        layout.addWidget(shift_j_label)
        layout.addWidget(shift_j_input)
        
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        self.setLayout(layout)
        
        self.shift_i_input = shift_i_input
        self.shift_j_input = shift_j_input


class GenerateShiftVectorDialog(QDialog):
    """
    选择生成平移向量方法的对话框。
    
    Select the method to generate the shift vector.
    """
    def __init__(self, parent: QWidget = None):
        """
        Initialize the dialog.
        
        arguments:
            parent: (QWidget) The parent widget.
        """
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        """
        Initialize the UI.
        """
        self.setWindowTitle('Generate Shift Vector')
        self.setModal(True)
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Select the method to generate the shift vector:'))
        radio_button_apply_current_shift_vec = QRadioButton('Apply the current shift vector to all the diffraction patterns.')
        radio_button_linear_regression = QRadioButton('Linear Regression')
        radio_button_quadratic_polynomial = QRadioButton('Quadratic Polynomial Regression')
        layout.addWidget(radio_button_apply_current_shift_vec)
        layout.addWidget(radio_button_linear_regression)
        layout.addWidget(radio_button_quadratic_polynomial)
        
        self.setLayout(layout)
        
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        self.radio_button_apply_current_shift_vec = radio_button_apply_current_shift_vec
        self.radio_button_linear_regression = radio_button_linear_regression
        self.radio_button_quadratic_polynomial = radio_button_quadratic_polynomial
        self.setLayout(layout)
