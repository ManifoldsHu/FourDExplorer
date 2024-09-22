# -*- coding: utf-8 -*-

"""
*-------------------------- PageAlignFourDSTEM.py ----------------------------*
对 4D-STEM 衍射图样进行平移、合轴的界面。其中包含三种方法，分别是手动法、
参考数据集法以及使用 FDDNet 来自动判断衍射盘位置。

部件内容：
    - WidgetPlotDP 用于使用 matplotlib 显示衍射图样
    - WidgetMaskCircle 用于控制 Cursor 的大小

提升部件：
    - 提升类名 PageAlignFourDSTEM
    - 头文件 bin.Widgets.PageAlignFourDSTEM

作者:           胡一鸣
创建日期:       2022年5月26日


The GUI page to align 4D-STEM dataset. There are three methods to align the 
diffraction patterns. The methods are manual, reference data set and FDDNet.

Contents:
    - WidgetPlotDP, to view the diffraction patterns by matplotlib
    - WidgetMaskCircle, control the shape of the cursor.

Promoted Widget:
    - name of widget class: PageAlignFourDSTEM
    - header file: bin.Widgets.PageAlignFourDSTEM

author:         Hu Yiming
date:           May 26, 2022
*-------------------------- PageAlignFourDSTEM.py ----------------------------*
"""

from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
# from matplotlib.text import Annotation
from matplotlib.patches import FancyArrowPatch
from h5py import Dataset
import numpy as np
from skimage.transform import warp
from skimage.transform import SimilarityTransform

from bin.TaskManager import TaskManager
from bin.Widgets.PageBaseFourDSTEM import PageBaseFourDSTEM
from bin.Widgets.DialogSaveFourDSTEM import DialogSaveFourDSTEM
from bin.Widgets.WidgetAlignmentManual import WidgetAlignmentManual
from bin.Widgets.WidgetAlignmentRef import WidgetAlignmentRef
from bin.Widgets.WidgetAlignmentFDDNet import WidgetAlignmentFDDNet
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from lib.TaskCalibration import TaskFourDSTEMAlign
from ui import uiPageAlignFourDSTEM

class PageAlignFourDSTEM(PageBaseFourDSTEM):
    """
    对 4D-STEM 衍射图样进行平移、合轴的部件类。

    Ui 文件地址：ROOTPATH/ui/uiPageAlignFourDSTEM

    Widget to align 4D-STEM dataset.

    The path of the ui file: ROOTPATH/ui/uiPageAlignFourDSTEM

    attributes:
        hdf_handler: (HDFHandler) The handler to manage the hdf file and the 
            objects inside it.

        data_object: (h5py.Dataset) The data object of 4D-STEM data.

        data_path: (str) The path of the data object.

        logger: (Logger) Use logger to record information.

        dp_canvas: (FigureCanvas) The canvas (widget) object to show 
            Diffraction patterns.

        dp_figure: (Figure) The Figure object of the diffraction patterns.

        dp_ax: (Axes) The Axes object of the diffraction patterns.

        colorbar_ax: (Axes) The Axes object of the colorbar.

        dp_object: (AxesImage) The image object of the diffraction patterns.

        colorbar_object: (Colorbar) The Colorbar object. This colorbar is atta-
            ched to the diffraction patterns.

        dp_blit_manager: (BlitManager) The blit manager of the diffraction 
            patterns. When the data, norm, colormap or other attributes of the 
            diffraction pattern change, use its update() method to plot the 
            updated images.

        scan_ii: (int) The i-coordinate of the current diffraction pattern in 
            the real space. This is also regarded as the row index in a matrix.

        scan_jj: (int) The j-coordinate of the current diffraction pattern in
            the real space. This is also regarded as the column index in a 
            matrix.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageAlignFourDSTEM.Ui_Form()
        self.ui.setupUi(self)

        self._initBaseUi()
        self._initUi()

        self._method = ['Manual', 'Reference', 'FDDNet']

        self._auxiliary_circle_object = None 
        self._hcursor_object = None 
        self._vcursor_object = None 
        self._shift_arrow_object = None 
        # self._shift_vec = None 
        self._fddnet_ellipse = None 

        self._createAxes()
        # self._translation_vector = (0, 0)

        # Initialize WidgetAlignmentManual
        # self._widget_alignment_manual = WidgetAlignmentManual(self)
        # self._widget_alignment_manual.setParentAlignPage(self)
        # self.ui.stackedWidget_align_mode.insertWidget(0, self._widget_alignment_manual)
        
        self._widget_alignment_manual = self.ui.stackedWidget_align_mode_manually
        self._widget_alignment_ref = self.ui.stackedWidget_align_mode_reference
        self._widget_alignment_fddnet = self.ui.stackedWidget_align_mode_fddnet
        self._widget_alignment_manual.setParentAlignPage(self)
        self._widget_alignment_ref.setParentAlignPage(self)
        self._widget_alignment_fddnet.setParentAlignPage(self)
        
        
        self._doubleSpinBox_circle_center_i = self.ui.widget_auxiliary_circle.ui.doubleSpinBox_circle_center_i 
        self._doubleSpinBox_circle_center_j = self.ui.widget_auxiliary_circle.ui.doubleSpinBox_circle_center_j 
        self._doubleSpinBox_circle_radius = self.ui.widget_auxiliary_circle.ui.doubleSpinBox_circle_radius

        # self._updateDP()
        self._updateAuxiliaryCircle()
        # self._updateAuxiliaryArrow()


    @property
    def hcursor_object(self) -> Line2D:
        return self._hcursor_object

    @property
    def vcursor_object(self) -> Line2D:
        return self._vcursor_object

    @property
    def auxiliary_circle_object(self) -> Circle:
        return self._auxiliary_circle_object

    @property
    def fddnet_ellipse(self) -> Ellipse:
        return self._fddnet_ellipse

    @property
    def task_manager(self) -> TaskManager:
        global qApp 
        return qApp.task_manager 

    @property
    def shift_vec(self) -> tuple[float, float]:
        if self.current_method == 'Manual':
            return self._widget_alignment_manual.getCurrentDPShiftVec()
        elif self.current_method == 'Reference':
            return self._widget_alignment_ref.getCurrentDPShiftVec()
        elif self.current_method == 'FDDNet':
            return self._widget_alignment_fddnet.getCurrentDPShiftVec()
    
    @property
    def current_show_shifted_dp(self) -> bool:
        if self.current_method == 'Manual':
            return self._widget_alignment_manual.getCurrentShowShiftedDP()
        elif self.current_method == 'Reference':
            return self._widget_alignment_ref.getCurrentShowShiftedDP()
        elif self.current_method == 'FDDNet':
            return self._widget_alignment_fddnet.getCurrentShowShiftedDP()
    
    
    @property
    def current_shift_vec_i(self) -> float:
        # 当前显示的衍射图像所对应的平移向量 (i 方向分量)
        if self._shift_vec is None: 
            return 0
        i_index = self.ui.spinBox_scan_ii.value()
        i_index = max(i_index, min(i_index, self.data_object.shape[0]), 0)
        j_index = self.ui.spinBox_scan_jj.value()
        j_index = max(j_index, min(j_index, self.data_object.shape[1]), 0)
        return self._shift_vec[0, i_index, j_index]
    
    @property
    def current_shift_vec_j(self) -> float:
        # 当前显示的衍射图像所对应的平移向量 (j 方向分量)
        if self._shift_vec is None: 
            return 0
        i_index = self.ui.spinBox_scan_ii.value()
        i_index = max(i_index, min(i_index, self.data_object.shape[0]), 0)
        j_index = self.ui.spinBox_scan_jj.value()
        j_index = max(j_index, min(j_index, self.data_object.shape[1]), 0)
        return self._shift_vec[1, i_index, j_index]
    
    @property
    def current_method(self) -> str:
        return self._method[self.ui.comboBox_show_alignment_method.currentIndex()]

    @property
    def shift_arrow_object(self) -> FancyArrowPatch:
        return self._shift_arrow_object 
    
    @property
    def shift_mapping_dataset(self) -> Dataset:
        return self.hdf_handler.file[self.ui.lineEdit_shift_mapping_path]

    def _initUi(self):
        """
        Initialize Uis
        """
        self.setWindowTitle('4D-STEM Diffraction Shift Alignment')

        self.ui.pushButton_start.setProperty('class', 'danger')
        self.ui.pushButton_start.clicked.connect(self.startCalculation)
        self.ui.pushButton_start.setText('Start to Apply Alignment')
        
        self.ui.comboBox_show_alignment_method.setCurrentIndex(0)
        self.ui.stackedWidget_align_mode.setCurrentIndex(0)

        self.ui.comboBox_show_alignment_method.currentIndexChanged.connect(self._onAlignmentMethodChanged)
        
        self.ui.checkBox_show_auxiliary_circle.stateChanged.connect(
            self._updateAuxiliaryCircle
        )
        self.ui.checkBox_set_auxiliary_circle_center_to_shift.stateChanged.connect(
            self._updateAuxiliaryCircle
        )
        
        # hide the auxiliary arrow, since it is a useless and failure design
        self.ui.groupBox_2.setVisible(False)    
        
        self.ui.checkBox_draw_auxiliary_arrow.setChecked(False)
        self.ui.checkBox_set_auxiliary_circle_center_to_shift.setChecked(False)
        self.ui.checkBox_set_auxiliary_circle_center_to_shift.setEnabled(False)
        self.ui.checkBox_show_auxiliary_circle.setChecked(True)
        
        self.ui.checkBox_set_auxiliary_circle_center_to_shift.stateChanged.connect(
            self._onAuxiliaryCircleCenterToShiftChanged
        )
        
        self.ui.pushButton_browse_shift_mapping.clicked.connect(self._browseShiftMapping)
        
        self.ui.spinBox_scan_ii.valueChanged.connect(self._changeAuxiliaryCircleWithShift)
        self.ui.spinBox_scan_jj.valueChanged.connect(self._changeAuxiliaryCircleWithShift)
        
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.stackedWidget_align_mode.setCurrentIndex(0)
        self.ui.comboBox_show_alignment_method.setCurrentIndex(0)


    def _createPatches(self):
        """
        Initialize all of the cursor patches, and add them to the axes.

        Including a circle, a horizontal line and a vertical line.
        """
        if self._auxiliary_circle_object in self.dp_ax.patches:
            # delete the current patch if there exists.
            self._auxiliary_circle_object.remove()

        self._auxiliary_circle_object = Circle(
            (0, 0),
            radius = 25,
            edgecolor = 'white',
            facecolor = 'black',
            alpha = 0.4,
            fill = True,
            visible = True,
        )

        self.dp_ax.add_patch(self._auxiliary_circle_object)
        self.dp_blit_manager['circle_patch'] = self._auxiliary_circle_object 
        self.ui.widget_auxiliary_circle.setBlitManager(self.dp_blit_manager)
        self.ui.widget_auxiliary_circle.setPatch(self._auxiliary_circle_object)
        
        if self.hcursor_object is None:
            self._hcursor_object = self.dp_ax.axhline(
                y = 0,
                color = 'black',
                linewidth = 1,
            )
            self.dp_blit_manager['hcursor'] = self.hcursor_object
        
        if self.vcursor_object is None:
            self._vcursor_object = self.dp_ax.axvline(
                x = 0,
                color = 'black', 
                linewidth = 1,
            )
            self.dp_blit_manager['vcursor'] = self.vcursor_object
            
        if self._shift_arrow_object in self.dp_ax.patches:
            self._shift_arrow_object.remove()

        self._shift_arrow_object = FancyArrowPatch(
            posA=(0, 0),
            posB=(0, 0),
            arrowstyle='->',
            color='green',
            mutation_scale=20,
            visible=False,
        )

        self.dp_ax.add_patch(self._shift_arrow_object)
        self.dp_blit_manager['shift_arrow'] = self._shift_arrow_object
            
            
        if self._fddnet_ellipse in self.dp_ax.patches:
            self._fddnet_ellipse.remove()

        self._fddnet_ellipse = Ellipse(
            xy = (0, 0),
            width = 0,
            height = 0,
            angle = 0,
            color = 'red',
            alpha = 0.5,
            fill = False,
            visible = False,
        )
        
        self.dp_ax.add_patch(self._fddnet_ellipse)
        self.dp_blit_manager['fddnet_ellipse'] = self._fddnet_ellipse
        self.ui.stackedWidget_align_mode_fddnet.setBlitManager(self.dp_blit_manager)
        self.ui.stackedWidget_align_mode_fddnet.setEllipsePatch(self._fddnet_ellipse)
       

    def setFourDSTEM(self, data_path: str):
        """
        Set the data path in HDF5 file, to show the diffraction patterns.

        Will set the data_path attribute. The FourDSTEM must be a 4D matrix.

        arguments:
            data_path: (str) the path of the 4D-STEM data.

        raises:
            TypeError, KeyError, ValueError
        """
        # if data_path != self.data_path:
        #     self._shift_vec = None 
        super(PageAlignFourDSTEM, self).setFourDSTEM(data_path)
        self._createPatches()

        scan_i, scan_j, dp_i, dp_j = self.hdf_handler.file[data_path].shape 
        self._setCursorCenter(
            ((dp_i - 1)/2, (dp_j - 1)/2)
        )

        # TODO: read/save the alignment attribute



    def _setCursorCenter(self, center: tuple):
        """
        Set the center of the cursor (i.e. the diffraction pattern).

        arguments:
            center: (tuple) must be a tuple which length is 2, like array
                shape.
        """
        # self.patch_circle.set_center(center)
        self.ui.widget_auxiliary_circle.setCenter(center)
        self.hcursor_object.set_ydata(center[0])
        self.vcursor_object.set_xdata(center[1])
        self.dp_blit_manager.update()

    def _updateDP(self):
        """
        Update the current diffraction pattern according to the location in 
        the real space and the translation vector.
        """
        if self.data_object is None:
            return None

        scan_i, scan_j, dp_i, dp_j = self.data_object.shape
        scan_ii = max(0, min(scan_i, self.scan_ii)) # Avoid out of boundary
        scan_jj = max(0, min(scan_j, self.scan_jj))

        shift_vec_xy = (self.shift_vec[1], self.shift_vec[0])
        center_xy = ((dp_j-1)/2, (dp_i-1)/2)

        if self.current_show_shifted_dp:
            # Create a translation matrix based on the shift vector
            translation_matrix = SimilarityTransform(translation=shift_vec_xy)
            
            # Apply the translation to the diffraction pattern data
            self.dp_object.set_data(
                warp(
                    self.data_object[scan_ii, scan_jj, :, :],
                    translation_matrix,
                    mode='edge',
                    cval=0,
                    preserve_range=True
                )
            )
        else:
            self.dp_object.set_data(
                self.data_object[scan_ii, scan_jj, :, :]
            )

        self.colorbar_object.update_normal(self.dp_object)
        self.dp_blit_manager.update()     
        
    def _onAlignmentMethodChanged(self, index: int):
        """
        Handle the change of alignment method.

        arguments:
            index: (int) The index of the selected alignment method.
        """
        self.ui.stackedWidget_align_mode.setCurrentIndex(index)
        self._updateDP()


    def _updateAuxiliaryCircle(self):
        """
        Update the auxiliary circle based on the current settings and shift vector.

        This method adjusts the center of the auxiliary circle according to the 
        user's choice to either set it to the shift vector or keep it at the 
        original center of the diffraction pattern. The visibility of the circle 
        is also updated based on the user's settings.
        """
        if not self.ui.lineEdit_data_path.text():
            return 
        
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape
        original_center_xy = ((dp_j-1)/2, (dp_i-1)/2)
        shift_center_xy = (
            - self._doubleSpinBox_circle_center_j.value(), 
            - self._doubleSpinBox_circle_center_i.value()
        )
        
        if self.ui.checkBox_set_auxiliary_circle_center_to_shift.isChecked():
            self.auxiliary_circle_object.set_center((
                shift_center_xy[0] + original_center_xy[0], 
                shift_center_xy[1] + original_center_xy[1]
            ))
        else:
            self.auxiliary_circle_object.set_center(original_center_xy)
        self.auxiliary_circle_object.set_visible(
            self.ui.checkBox_show_auxiliary_circle.isChecked()
        )
        self.dp_blit_manager.update()
        


    def _onAuxiliaryCircleCenterToShiftChanged(self):
        """
        Handle the state change of the 'Set Auxiliary Circle Center to Shift' checkbox.

        This function ensures that the checkbox is only enabled when a valid shift mapping is selected.
        If the checkbox is checked, the double spin boxes for circle center i and j are disabled,
        and their values are updated based on the shift mapping corresponding to the current scan position.
        If the checkbox is unchecked, the double spin boxes are enabled for manual adjustment.
        """
        shift_mapping_path = self.ui.lineEdit_shift_mapping_path.text()
        if not shift_mapping_path:
            self.ui.checkBox_set_auxiliary_circle_center_to_shift.setChecked(False)
            self.ui.checkBox_set_auxiliary_circle_center_to_shift.setEnabled(False)
            self._doubleSpinBox_circle_center_i.setEnabled(True)
            self._doubleSpinBox_circle_center_j.setEnabled(True)
            return

        self.ui.checkBox_set_auxiliary_circle_center_to_shift.setEnabled(True)
        if self.ui.checkBox_set_auxiliary_circle_center_to_shift.isChecked():
            self._doubleSpinBox_circle_center_i.setEnabled(False)
            self._doubleSpinBox_circle_center_j.setEnabled(False)
            scan_ii = self.ui.spinBox_scan_ii.value()
            scan_jj = self.ui.spinBox_scan_jj.value()
            shift_mapping = self.hdf_handler.file[shift_mapping_path]
            if shift_mapping.shape[:2] == self.data_object.shape[:2]:
                shift_i = shift_mapping[scan_ii, scan_jj, 0]
                shift_j = shift_mapping[scan_ii, scan_jj, 1]
                self._doubleSpinBox_circle_center_i.setValue(shift_i)
                self._doubleSpinBox_circle_center_j.setValue(shift_j)
            else:
                self.logger.warning("Shift mapping shape does not match data object shape.")
        else:
            self._doubleSpinBox_circle_center_i.setEnabled(True)
            self._doubleSpinBox_circle_center_j.setEnabled(True)

    
    def _browseShiftMapping(self):
        """
        Opens a dialog to browse and select a shift mapping path.
        
        Validates the selected path and updates the UI accordingly.
        
        raise::
            KeyError: If the selected path is not a valid HDF5 dataset.
        """
        dialog = DialogHDFChoose(self)
        dialog_code = dialog.exec()
        if dialog_code != dialog.Accepted:
            return

        current_path = dialog.getCurrentPath()
        try:
            shift_mapping = self.hdf_handler.file[current_path]
            if not isinstance(shift_mapping, Dataset):
                self.logger.error("Invalid Shift Mapping: The selected path is not a valid HDF5 dataset.")
                QMessageBox.warning(self, "Invalid Shift Mapping", "The selected path is not a dataset.")
                return

            scan_i, scan_j = self.data_object.shape[:2]
            if shift_mapping.shape != (2, scan_i, scan_j):
                self.logger.error(f"Invalid Shift Mapping: The selected shift mapping does not have the expected shape (2, {scan_i}, {scan_j}).")
                QMessageBox.warning(self, "Invalid Shift Mapping", "The selected shift mapping does not have the expected shape (2, scan_i, scan_j).")
                return

            self.ui.lineEdit_shift_mapping_path.setText(current_path)
            
            self.ui.checkBox_set_auxiliary_circle_center_to_shift.setEnabled(True)
        except KeyError:
            QMessageBox.warning(self, "Invalid Path", "The selected path does not exist in the HDF file.")


    def _changeAuxiliaryCircleWithShift(self):
        """
        Updates the auxiliary circle center to the shift values from the shift mapping dataset.

        This method is called when the 'Set Auxiliary Circle Center to Shift' checkbox is checked.
        It retrieves the shift values from the shift mapping dataset for the current scan indices
        and sets the auxiliary circle center to these values.
        """
        if not self.ui.checkBox_set_auxiliary_circle_center_to_shift.isChecked():
            return 
        if not self.ui.lineEdit_shift_mapping_path.text():
            return 
        self._doubleSpinBox_circle_center_i.setValue(self.shift_mapping_dataset[0, self.scan_ii, self.scan_jj])
        self._doubleSpinBox_circle_center_j.setValue(self.shift_mapping_dataset[1, self.scan_ii, self.scan_jj])
        


    def startCalculation(self):
        """
        Use the chosen shift mapping to align the 4D-STEM dataset.
        """
        if not self.ui.lineEdit_shift_mapping_path.text():
            QMessageBox.warning(self, "Invalid Path", "Please select a valid shift mapping path.")
            return 
        if not self.ui.lineEdit_data_path.text():
            QMessageBox.warning(self, "Invalid Path", "Please select a valid 4D-STEM data path.")
        
        
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
        # TODO: add meta
        
        self.task = TaskFourDSTEMAlign(
            self.data_path,
            output_parent_path,
            output_name,
            self.shift_mapping_dataset,
            # **meta,
        )
        self.task_manager.addTask(self.task)
