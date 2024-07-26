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
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
from matplotlib.text import Annotation
import numpy as np

from bin.TaskManager import TaskManager
from bin.Widgets.PageBaseFourDSTEM import PageBaseFourDSTEM
from bin.Widgets.DialogSaveFourDSTEM import DialogSaveFourDSTEM
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
        self._shift_vec = None 


        self._createAxes()
        self._translation_vector = (0, 0)

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
    def shift_vec(self) -> np.ndarray:
        return self._shift_vec  # 指的是当前整个数据集的平移向量
    
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
    def shift_arrow(self) -> Annotation:
        return self._shift_arrow_object 

    def _initUi(self):
        """
        Initialize Uis
        """
        self.setWindowTitle('4D-STEM Diffraction Shift Alignment')

        self.ui.pushButton_start.setProperty('class', 'danger')
        self.ui.pushButton_start.clicked.connect(self.startCalculation)
        self.ui.pushButton_start.setText('Start to Apply Alignment')

        # self.ui.

    def _createPatches(self):
        """
        Initialize all of the cursor patches, and add them to the axes.

        Including a circle, a horizontal line and a vertical line.
        """
        if self._auxiliary_circle_object in self.dp_ax.patches:
            # delete the current patch if there exists.
            _index = self.dp_ax.patches.index(self._auxiliary_circle_object)
            self.dp_ax.patches.pop(_index)

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
        self.ui.widget_circle.setBlitManager(self.dp_blit_manager)
        self.ui.widget_circle.setPatch(self._auxiliary_circle_object)
        
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
        self.ui.widget_circle.setCenter(center)
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
        self.dp_object.set_data(
            np.roll(
                self.data_object[scan_ii, scan_jj, :, :], 
                self._translation_vector,
                axis = (0, 1),
            )
        )
        
        self.colorbar_object.update_normal(self.dp_object)
        self.dp_blit_manager.update()     
        
    # def _translateUp(self):
    #     self._translation_vector = (
    #         self._translation_vector[0] - 1, 
    #         self._translation_vector[1]
    #     )
    #     # self._translation_vector[0] -= 1
    #     self._updateDP()
    
    # def _translateDown(self):
    #     # self._translation_vector[0] += 1
    #     self._translation_vector = (
    #         self._translation_vector[0] + 1,
    #         self._translation_vector[1],
    #     )
    #     self._updateDP()

    # def _translateLeft(self):
    #     # self._translation_vector[1] -= 1
    #     self._translation_vector = (
    #         self._translation_vector[0],
    #         self._translation_vector[1] - 1,
    #     )
    #     self._updateDP()

    # def _translateRight(self):
    #     # self._translation_vector[1] += 1
    #     self._translation_vector = (
    #         self._translation_vector[0],
    #         self._translation_vector[1] + 1,
    #     )
    #     self._updateDP()

    # def startCalculation(self):
    #     """
    #     Start to apply the translation towards all the diffraction patterns.
    #     """
    #     dialog_save = DialogSaveFourDSTEM(self)
    #     dialog_save.setParentPath(self.data_path)
    #     dialog_code = dialog_save.exec()
    #     if not dialog_code == dialog_save.Accepted:
    #         return 
    #     if dialog_save.getIsInplace():
    #         data_node = self.hdf_handler.getNode(self.data_path)
    #         output_name = data_node.name 
    #         output_parent_path = data_node.parent.path 
    #     else:
    #         output_name = dialog_save.getNewName()
    #         output_parent_path = dialog_save.getParentPath()
        
    #     meta = self.data_object.attrs 
    #     if 'translation_vector_i' in meta:
    #         meta['translation_vector_i'] += self._translation_vector[0]
    #     else:
    #         meta['translation_vector_i'] = self._translation_vector[0]
        
    #     if 'translation_vector_j' in meta:
    #         meta['translation_vector_j'] += self._translation_vector[1]
    #     else:
    #         meta['translation_vector_j'] = self._translation_vector[1]

    #     self.task = TaskFourDSTEMAlign(
    #         self.data_path,
    #         output_parent_path,
    #         output_name,
    #         self._translation_vector,
    #         **meta,
    #     )
    #     self.task_manager.addTask(self.task)
        


