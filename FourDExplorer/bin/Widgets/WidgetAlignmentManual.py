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

from bin.BlitManager import BlitManager
from bin.UIManager import ThemeHandler
from bin.Log import Logger
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
        return (self.scan_ii, self.scan_jj)
    
    @property
    def current_shift_i(self):
        return self.ui.spinBox_manual_shift_i.value()

    @property
    def current_shift_j(self):
        return self.ui.spinBox_manual_shift_j.value()

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
        self._action_delete = ActionDeleteAnchor(self)
        self._action_modify = ActionModifyAnchor(self)
        self._action_import = ActionImportAnchor(self)
        self._action_export = ActionExportAnchor(self)
        self._table_widget_toolbar.addAction(self._action_add)
        self._table_widget_toolbar.addAction(self._action_delete)
        self._table_widget_toolbar.addAction(self._action_modify)
        self._table_widget_toolbar.addAction(self._action_import)
        self._table_widget_toolbar.addAction(self._action_export)
        self.ui.groupBox_sample_records.layout().insertWidget(0, self._table_widget_toolbar)  


    def _initConnections(self):
        """
        Initialize signal-slot connections.
        """
        self.ui.checkBox_show_shifted_dp.stateChanged.connect(self._onShowShiftedDPChanged)
        self.ui.spinBox_manual_shift_i.valueChanged.connect(self._onShiftIChanged)
        self.ui.spinBox_manual_shift_j.valueChanged.connect(self._onShiftJChanged)
        self.ui.pushButton_down.clicked.connect(self._onDownButtonClicked)
        self.ui.pushButton_up.clicked.connect(self._onUpButtonClicked)
        self.ui.pushButton_left.clicked.connect(self._onLeftButtonClicked)
        self.ui.pushButton_right.clicked.connect(self._onRightButtonClicked)
        self.ui.pushButton_generate_shift_vec.clicked.connect(self._onGenerateShiftVecClicked)
        


    def _onShowShiftedDPChanged(self):
        """
        Handle the state change of the 'Show Shifted DP' checkbox.

        arguments:
            state: (int) The state of the checkbox (Qt.Checked or Qt.Unchecked).
        """
        if self.ui.checkBox_show_shifted_dp.isChecked():
            original_data = self.data_object[self.scan_ii, self.scan_jj, :, :]
            shifted_data = np.roll(original_data, self.current_shift_i, axis=0)
            shifted_data = np.roll(shifted_data, self.current_shift_j, axis=1)
            self.dp_object.set_data(shifted_data)
            self.blit_manager.update()
        else:
            self.dp_object.set_data(self.data_object[self.scan_ii, self.scan_jj, :, :])
            self.blit_manager.update()

    
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
        self.ui.spinBox_manual_shift_i.setValue(self.ui.spinBox_manual_shift_i.value() + 1)
        
    def _onUpButtonClicked(self):
        """
        Handle the click of the up button.
        """
        self.ui.spinBox_manual_shift_i.setValue(self.ui.spinBox_manual_shift_i.value() - 1)
    
    def _onLeftButtonClicked(self):
        """
        Handle the click of the left button.
        """
        self.ui.spinBox_manual_shift_j.setValue(self.ui.spinBox_manual_shift_j.value() - 1)
    
    def _onRightButtonClicked(self):
        """ 
        Handle the click of the right button.
        """
        self.ui.spinBox_manual_shift_j.setValue(self.ui.spinBox_manual_shift_j.value() + 1)
    
    def _onGenerateShiftVecClicked(self):
        """
        Handle the click of the generate shift vector button.
        
        A dialog will pop up to let user to choose which method to generate the shift vector. Methods include:
            - Apply the current shift vector to all the diffraction patterns.
            - Use the current anchors to generate the shift vector fields with linear regression.
            - Use the current anchors to generate the shift vector fields with quadratic polynomial.
        """
        _dialog = GenerateShiftVectorDialog(self)
        result = _dialog.exec()
        if result == QDialog.Accepted:
            if _dialog.radio_button_apply_current_shift_vec.isChecked():
                shift_map = self._useCurrentShiftVec()
            elif _dialog.radio_button_linear_regression.isChecked():
                shift_map = self._useLinearRegression()
            elif _dialog.radio_button_quadratic_polynomial.isChecked():
                shift_map = self._useQuadraticPolynomial()

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
        Use the current anchors to generate the shift vector fields with linear regression.
        """
        table_widget = self.ui.tableWidget_manual_sample
        anchor_locations = [eval(table_widget.item(i, 0).text()) for i in range(table_widget.rowCount())]
        anchor_shifts = [eval(table_widget.item(i, 1).text()) for i in range(table_widget.rowCount())]
        shift_vec = np.zeros((2, self.scan_ii, self.scan_jj,))
        for anchor_location, anchor_shift in zip(anchor_locations, anchor_shifts):
            shift_vec[0, anchor_location[0], anchor_location[1]] = anchor_shift[0]
            shift_vec[1, anchor_location[0], anchor_location[1]] = anchor_shift[1]
        return shift_vec

    def _useQuadraticPolynomial(self):
        """
        Use the current anchors to generate the shift vector fields with quadratic polynomial.
        """
        pass # TODO
            

        
        


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
        Add the current displaying item that include the diffraction pattern's location and shift.
        """
        current_location = self.widget_alignment_manual.current_dp_location
        current_shift_i = self.widget_alignment_manual.current_shift_i
        current_shift_j = self.widget_alignment_manual.current_shift_j
        self.table_widget.insertRow(self.table_widget.rowCount())
        self.table_widget.setItem(self.table_widget.rowCount() - 1, 0, QTableWidgetItem(str(current_location)))
        self.table_widget.setItem(self.table_widget.rowCount() - 1, 1, QTableWidgetItem(str((current_shift_i, current_shift_j))))
        


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
        modify_dialog = ModifyDialog(self, self.table_widget, current_index)
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
        Export the current selected item.
        """
        pass # TODO

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
        Import the current selected item.
        """
        pass # TODO


class ModifyDialog(QDialog):
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
        self.initUi()
        self._current_index = current_index
        self._table_widget = table_widget


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
        shift_i_input.setValue(int(self._table_widget.item(self._current_index, 1).text()))
        layout.addWidget(shift_i_label)
        layout.addWidget(shift_i_input)
        
        shift_j_label = QLabel('Shift j:')
        shift_j_input = QSpinBox()
        shift_j_input.setValue(int(self._table_widget.item(self._current_index, 2).text()))
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
