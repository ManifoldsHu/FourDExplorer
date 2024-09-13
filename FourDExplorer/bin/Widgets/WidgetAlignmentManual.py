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


from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QToolBar
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QTableWidgetItem 
from PySide6.QtCore import Qt

import numpy as np
from matplotlib.image import AxesImage
from matplotlib.axes import Axes 

from bin.BlitManager import BlitManager
from ui import uiWidgetAlignmentManual




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
        self._initTableWidget()
        self._initConnections()
    
    @property
    def current_dp_location(self):
        return (self.parent().scan_ii, self.parent().scan_jj)
    
    @property
    def current_shift_i(self):
        return self.ui.spinBox_manual_shift_i.value()

    @property
    def current_shift_j(self):
        return self.ui.spinBox_manual_shift_j.value()

    def setAxes(self, ax: Axes):
        """
        Set the axes object.

        arguments:
            ax: (Axes) The axes object containing the diffraction pattern.
        """
        self._ax = ax

    def setBlitManager(self, blit_manager: BlitManager):
        """
        Set the blit manager.

        arguments:
            blit_manager: (BlitManager) The blit manager for updating the display.
        """
        self._blit_manager = blit_manager

    def setDataObject(self, data_object: np.ndarray):
        """
        Set the 4D-STEM data object.

        arguments:
            data_object: (np.ndarray) The 4D-STEM dataset.
        """
        self._data_object = data_object

    def setDPObject(self, dp_object: AxesImage):
        """
        Set the diffraction pattern image object.

        arguments:
            dp_object: (AxesImage) The image object of the diffraction pattern.
        """
        self._dp_object = dp_object

    @property
    def dp_object(self) -> AxesImage:
        return self._dp_object
    
    @property
    def ax(self) -> Axes:
        return self._ax 
    
    @property
    def blit_manager(self) -> BlitManager:
        return self._blit_manager

    def _initTableWidget(self):
        """
        初始化 Table widget, 添加 Action Button 以及相应的 toolbar，里面包含有增加、删除、修改按钮。其中，增加按钮可将页面当前展示的衍射图像的位置以及衍射图像对应的平移量给保存下来；删除按钮可将列表中当前选定的项给删除掉；修改按钮可修改列表中当前选定的项。

        Initialize the table widget, and add the action button and the corresponding toolbar, which contains the add, delete, and modify buttons. The add button can save the position of the current diffraction image and the shift amount of the diffraction image; the delete button can delete the current item in the list; the modify button can modify the current item in the list.
        """
        self.ui.tableWidget_manual_sample.setColumnCount(3)
        self.ui.tableWidget_manual_sample.setHorizontalHeaderLabels(['location', 'shift i', 'shift j'])
        self.ui.tableWidget_manual_sample.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_manual_sample.setRowCount(0)
        self.ui.tableWidget_manual_sample.setEditTriggers(QTableWidget.NoEditTriggers)

        self._table_widget_toolbar = QToolBar()
        self._action_add = self._table_widget_toolbar.addAction("Add")
        self._action_delete = self._table_widget_toolbar.addAction("Delete")
        self._action_modify = self._table_widget_toolbar.addAction("Modify")
        self.ui.verticalLayout_3.addWidget(self._table_widget_toolbar)

        self._action_add.triggered.connect(self._addItem)
        self._action_delete.triggered.connect(self._deleteItem)
        self._action_modify.triggered.connect(self._modifyItem)

    def _addItem(self):
        """
        Add the current displaying item that include the diffraction pattern's location and shift.
        """
        current_location = self.current_dp_location  
        current_shift_i = self.ui.spinBox_manual_shift_i.value()
        current_shift_j = self.ui.spinBox_manual_shift_j.value()

        # Check if the location already exists in the table
        for row in range(self.ui.tableWidget_manual_sample.rowCount()):
            location_item = self.ui.tableWidget_manual_sample.item(row, 0)
            if location_item and location_item.text() == str(current_location):
                # Update the existing row
                self.ui.tableWidget_manual_sample.setItem(row, 1, QTableWidgetItem(str(current_shift_i)))
                self.ui.tableWidget_manual_sample.setItem(row, 2, QTableWidgetItem(str(current_shift_j)))
                self._shift_i_dict[str(current_location)] = current_shift_i
                self._shift_j_dict[str(current_location)] = current_shift_j
                return

        # Add a new row if the location does not exist
        row_position = self.ui.tableWidget_manual_sample.rowCount()
        self.ui.tableWidget_manual_sample.insertRow(row_position)
        self.ui.tableWidget_manual_sample.setItem(row_position, 0, QTableWidgetItem(str(current_location)))
        self.ui.tableWidget_manual_sample.setItem(row_position, 1, QTableWidgetItem(str(current_shift_i)))
        self.ui.tableWidget_manual_sample.setItem(row_position, 2, QTableWidgetItem(str(current_shift_j)))

        # Update the dictionaries
        self._shift_i_dict[str(current_location)] = current_shift_i
        self._shift_j_dict[str(current_location)] = current_shift_j


    def _deleteItem(self):
        """
        Delete the current item.
        """
        current_row = self.ui.tableWidget_manual_sample.currentRow()
        if current_row == -1:
            return

        # Create a confirmation dialog
        confirm_dialog = QMessageBox(self)
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Confirm Deletion")
        confirm_dialog.setText("Are you sure you want to delete the selected item?")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setDefaultButton(QMessageBox.No)

        # Show the dialog and get the result
        result = confirm_dialog.exec_()

        if result == QMessageBox.Yes:
            # Remove the item from the table widget
            self.ui.tableWidget_manual_sample.removeRow(current_row)

            # Remove the item from the dictionaries
            location = self.ui.tableWidget_manual_sample.item(current_row, 0).text()
            del self._shift_i_dict[location]
            del self._shift_j_dict[location]


    def _modifyItem(self):
        """
        Modify the current item.
        """
        selected_items = self.ui.tableWidget_manual_sample.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select an item to modify.")
            return

        selected_row = selected_items[0].row()
        current_location = self.current_dp_location
        current_shift_i = self.ui.spinBox_manual_shift_i.value()
        current_shift_j = self.ui.spinBox_manual_shift_j.value()

        self.ui.tableWidget_manual_sample.setItem(selected_row, 0, QTableWidgetItem(str(current_location)))
        self.ui.tableWidget_manual_sample.setItem(selected_row, 1, QTableWidgetItem(str(current_shift_i)))
        self.ui.tableWidget_manual_sample.setItem(selected_row, 2, QTableWidgetItem(str(current_shift_j)))

    def _initConnections(self):
        """
        Initialize signal-slot connections.
        """
        self.ui.checkBox_show_shifted_dp.stateChanged.connect(self._onShowShiftedDPChanged)


    def _onShowShiftedDPChanged(self, state: int):
        """
        Handle the state change of the 'Show Shifted DP' checkbox.

        arguments:
            state: (int) The state of the checkbox (Qt.Checked or Qt.Unchecked).
        """
        if self._dp_object is None or self._data_object is None:
            return

        current_location = self.current_dp_location
        scan_ii, scan_jj = current_location
        
        if state == Qt.Checked:
            shift_i = self._shift_i_dict.get(str(current_location), 0)
            shift_j = self._shift_j_dict.get(str(current_location), 0)
            shifted_dp = np.roll(self._data_object[scan_ii, scan_jj], (shift_i, shift_j), axis=(0, 1))
            self._dp_object.set_data(shifted_dp)
        else:
            original_dp = self._data_object[scan_ii, scan_jj]
            self._dp_object.set_data(original_dp)

        self._blit_manager.update()

    def updateDP(self):
        """
        Update the diffraction pattern display based on the current state.
        """
        if self.ui.checkBox_show_shifted_dp.isChecked():
            self._onShowShiftedDPChanged(Qt.Checked)
        else:
            self._onShowShiftedDPChanged(Qt.Unchecked)


