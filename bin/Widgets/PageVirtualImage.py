# -*- coding: utf-8 -*-

"""
*--------------------------- PageVirtualImage.py -----------------------------*
用于计算 4D-STEM 虚拟成像的页面。

部件内容：
    - WidgetPlotDP 用于使用 matplotlib 来显示衍射图样
    - WidgetMaskCircle 用于绘制圆形区域
    - WidgetMaskRing 用于绘制环形区域
    - WidgetMaskWedge 用于绘制扇形区域
    - WidgetMaskRectangle 用于绘制矩形区域
    - WidgetMaskSegment2 用于绘制2分段环形区域
    - WidgetMaskSegment4 用于绘制4分段环形区域
    - WidgetMaskSegment6 用于绘制6分段环形区域
    - WidgetMaskSegment8 用于绘制8分段环形区域

提升部件：
    - 提升类名 PageVirtualImage
    - 头文件 bin.Widgets.PageVirtualImage

作者:           胡一鸣
创建日期:       2022年4月8日

The GUI page to calculate virtual images from 4D-STEM.

Contents:
    - WidgetPlotDP, to view the diffraction patterns
    - WidgetMaskCircle, to draw circular region
    - WidgetMaskRing, to draw annular region
    - WidgetMaskWedge, to draw fan-shaped region
    - WidgetMaskRectangle, to draw rectangular region
    - WidgetMaskSegment2, to draw 2-segmented annular regions
    - WidgetMaskSegment4, to draw 4-segmented annular regions
    - WidgetMaskSegment6, to draw 6-segmented annular regions
    - WidgetMaskSegment8, to draw 8-segmented annular regions

Promoted Widget:
    - name of widget class: PageVirtualImage
    - header file: bin.Widget.PageVirtualImage

author:         Hu Yiming
date:           Apr 8, 2022
*--------------------------- PageVirtualImage.py -----------------------------*
"""

from logging import Logger
# from typing import List, Tuple

from PySide6.QtWidgets import QWidget, QMessageBox, QDialog
from PySide6.QtGui import QRegularExpressionValidator

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.colorbar import Colorbar, make_axes
from matplotlib.colors import Normalize, SymLogNorm
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.image import AxesImage
from matplotlib.axis import Axis
from matplotlib.lines import Line2D
from matplotlib.patches import (
    Circle, 
    Rectangle, 
    Wedge, 
    Annulus, 
    Ellipse,
    RegularPolygon,
)

import numpy as np
import h5py

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFHandler, reValidHDFName, HDFGroupNode
from bin.TaskManager import TaskManager
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.Widgets.PageBaseFourDSTEM import PageBaseFourDSTEM
from lib.TaskReconstruction import TaskVirtualImage
from ui import uiPageVirtualImage
from ui import uiDialogTestPlot
from ui import uiDialogCreateImage

class PageVirtualImage(PageBaseFourDSTEM):
    """
    进行虚拟成像的部件类。

    Ui 文件地址：ROOTPATH/ui/uiPageVirtualImage

    Widget to calculate Virtual Image.

    The path of the ui file: ROOTPATH/ui/uiPageVirtualImage

    attributes:
        hdf_handler: (HDFHandler) The handler to manage the hdf file and the
            objects inside it.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageVirtualImage.Ui_Form()
        self.ui.setupUi(self)

        self._initBaseUi()
        self._initUi()
        
        self._max_segment_num = 10      # The maximum number of segmented ring.
        self._mask_widgets = []         # Must be the same order as the mode.

        self._patch_circle = None
        self._patch_ring = None
        self._patch_wedge = None
        self._patch_rectangle = None
        self._patch_ellipse = None
        self._patch_polygons = []
        self._patch_segments = []

        self._createAxes()
        
    @property
    def mask_index(self) -> int:
        """
        Indicates which mask is used:
            0       Circle
            1       Ring
            2       Wedge
            3       Rectangle
            4       Ellipse
            5       Polygon
            6       Segmented Ring
        """
        return self.ui.comboBox_mode.currentIndex()

    @property
    def task_manager(self) -> TaskManager:
        global qApp
        return qApp.task_manager

    def _initUi(self):
        """
        Initialize Uis.
        """
        self.setWindowTitle('Virtual Image')

        self.ui.comboBox_mode.setCurrentIndex(0)
        self.ui.stackedWidget_masks.setCurrentIndex(self.mask_index)
        self.ui.comboBox_mode.currentIndexChanged.connect(self._changeMode)

        self.ui.pushButton_start.setProperty('class', 'danger')
        # self.ui.pushButton_start.clicked.connect(self.startCalculationTest)
        self.ui.pushButton_start.clicked.connect(self.startCalculation)

    def _createMasks(self):
        """
        Initialize all of the mask patches, and add them to the axes.
        """

        self._createCircle()
        self._createRing()
        self._createWedge()
        self._createRectangle()
        self._createEllipse()
        self._createPolygon()
        self._createSegments()

        self.dp_canvas.draw()
        self.dp_canvas.flush_events()
        

    def _createCircle(self):
        """
        Initialize the circle patch and its managers.
        """
        if self._patch_circle in self.dp_ax.patches:
            _index = self.dp_ax.patches.index(self._patch_circle)
            self.dp_ax.patches.pop(_index)

        self._patch_circle = Circle(
            (0, 0),
            radius = 25,
            edgecolor = 'white',
            facecolor = 'black',
            alpha = 0.4,
            fill = True,
            visible = True,
        )
        
        self.dp_ax.add_patch(self._patch_circle)
        self.dp_blit_manager['circle_patch'] = self._patch_circle
        self.ui.page_circle.setBlitManager(self.dp_blit_manager)
        self.ui.page_circle.setPatch(self._patch_circle)
        self._mask_widgets.append(self.ui.page_circle)

    def _createRing(self):
        """
        Initialize the ring patch and its managers.
        """
        if self._patch_ring in self.dp_ax.patches:
            _index = self.dp_ax.patches.index(self._patch_ring)
            self.dp_ax.patches.pop(_index)

        self._patch_ring = Annulus(
            (0, 0),
            r = 25,
            width = 15,
            edgecolor = 'white',
            facecolor = 'black',
            alpha = 0.4,
            fill = True,
            visible = False,
        )

        self.dp_ax.add_patch(self._patch_ring)
        self.dp_blit_manager['ring_patch'] = self._patch_ring
        self.ui.page_ring.setBlitManager(self.dp_blit_manager)
        self.ui.page_ring.setPatch(self._patch_ring)
        self._mask_widgets.append(self.ui.page_ring)

    def _createWedge(self):
        """
        Initialize the wedge patch and its managers.
        """
        if self._patch_wedge in self.dp_ax.patches:
            _index = self.dp_ax.patches.index(self._patch_wedge)
            self.dp_ax.patches.pop(_index)

        self._patch_wedge = Wedge(
            (0, 0),
            r = 25,
            theta1 = 0,
            theta2 = 120,
            width = 15,
            edgecolor = 'white',
            facecolor = 'black',
            alpha = 0.4,
            fill = True,
            visible = False,
        )

        self.dp_ax.add_patch(self._patch_wedge)
        self.dp_blit_manager['wedge_patch'] = self._patch_wedge
        self.ui.page_wedge.setBlitManager(self.dp_blit_manager)
        self.ui.page_wedge.setPatch(self._patch_wedge)
        self._mask_widgets.append(self.ui.page_wedge)

    def _createRectangle(self):
        """
        Initialize the rectangle patch and its managers.
        """
        if self._patch_rectangle in self.dp_ax.patches:
            _index = self.dp_ax.patches.index(self._patch_rectangle)
            self.dp_ax.patches.pop(_index)

        self._patch_rectangle = Rectangle(
            (0, 0),
            width = 25,
            height = 15,
            angle = 0,
            edgecolor = 'white',
            facecolor = 'black',
            alpha = 0.4,
            fill = True,
            visible = False,
        )

        self.dp_ax.add_patch(self._patch_rectangle)
        self.dp_blit_manager['rectangle_patch'] = self._patch_rectangle
        self.ui.page_rectangle.setBlitManager(self.dp_blit_manager)
        self.ui.page_rectangle.setPatch(self._patch_rectangle)
        self._mask_widgets.append(self.ui.page_rectangle)

    def _createEllipse(self):
        """
        Initialize the ellipse patch and its managers.
        """
        if self._patch_ellipse in self.dp_ax.patches:
            _index = self.dp_ax.patches.index(self._patch_ellipse)
            self.dp_ax.patches.pop(_index)

        self._patch_ellipse = Ellipse(
            (0, 0),
            width = 25,
            height = 15,
            angle = 0,
            edgecolor = 'white',
            facecolor = 'black',
            alpha = 0.4,
            fill = True,
            visible = False,
        )

        self.dp_ax.add_patch(self._patch_ellipse)
        self.dp_blit_manager['ellipse_patch'] = self._patch_ellipse
        self.ui.page_ellipse.setBlitManager(self.dp_blit_manager)
        self.ui.page_ellipse.setPatch(self._patch_ellipse)
        self._mask_widgets.append(self.ui.page_ellipse)

    def _createPolygon(self):
        """
        Initialize the regular polygon patch and its managers.

        The number of polygon patches is decided by _max_vertices. A polygon 
        has at least 3 vertices.
        """
        for _polygon in self._patch_polygons:
            if _polygon in self.dp_ax.patches:
                _index = self.dp_ax.patches.index(_polygon)
                self.dp_ax.patches.pop(_index)

        self._patch_polygons = []
        _max_vertices = self.ui.page_polygon.max_vertices
        for ii in range(3, _max_vertices + 1):
            _polygon = RegularPolygon(
                (0, 0),
                numVertices = ii,
                radius = 25,
                orientation = 0,
                edgecolor = 'white',
                facecolor = 'black',
                alpha = 0.4,
                fill = True,
                visible = False,
            )
            self._patch_polygons.append(_polygon)
            self.dp_ax.add_patch(_polygon)
            self.dp_blit_manager['polygon_patch_{0}'.format(ii)] = _polygon
        
        self.ui.page_polygon.setBlitManager(self.dp_blit_manager)
        self.ui.page_polygon.setPatch(self._patch_polygons)
        self._mask_widgets.append(self.ui.page_polygon)
        

    def _createSegments(self):
        """
        Initialize the segmented patches and their managers.

        There are at most _max_segments (number) segments. 
        """
        for _wedge in self._patch_segments:
            if _wedge in self.dp_ax.patches:
                _index = self.dp_ax.patches.index(_wedge)
                self.dp_ax.patches.pop(_index)

        self._patch_segments = []
        _max_segments = self.ui.page_segment_ring.max_segments
        for ii in range(_max_segments):
            _wedge = Wedge(
                (0, 0),
                r = 25,
                theta1 = 0,
                theta2 = 120,
                width = 15,
                edgecolor = 'white',
                facecolor = 'black',
                alpha = 0.4,
                fill = True,
                visible = False,
            )
            self._patch_segments.append(_wedge)
            self.dp_ax.add_patch(_wedge)
            self.dp_blit_manager['segment_patch_{0}'.format(ii)] = _wedge

        self.ui.page_segment_ring.setBlitManager(self.dp_blit_manager)
        self.ui.page_segment_ring.setPatch(self._patch_segments)
        self._mask_widgets.append(self.ui.page_segment_ring)


    def setFourDSTEM(self, data_path: str):
        """
        Set the data path in HDF5 file, to show the diffraction patterns.

        Will set the data_path attribute. The FourDSTEM must be a 4D matrix.

        arguments:
            data_path: (str) the path of the 4D-STEM data.

        raises:
            TypeError, KeyError, ValueError
        """
        super(PageVirtualImage, self).setFourDSTEM(data_path)
        self._createMasks()

        scan_i, scan_j, dp_i, dp_j = self.hdf_handler.file[data_path].shape
        for widget in self._mask_widgets:
            widget.setCenter(
                ((dp_i - 1)/2, (dp_j - 1)/2)
            )
        

    def _changeMode(self):
        """
        Change mask patch's mode according to mask index.

        The activated patch is set to be visible, while others are set to be 
        invisible.
        """
        self.ui.stackedWidget_masks.setCurrentIndex(self.mask_index)

        # Set the patch visible according to the index
        for ii, widget in enumerate(self._mask_widgets):
            widget.setMaskActivate(ii == self.mask_index)
        self.dp_blit_manager.update()

    def calcMask(self) -> np.ndarray:
        """
        Calculate integration region of the virtual image.

        This function returns a matrix whose shape is the same as the diffract-
        ion patterns' size of the 4D-STEM dataset. Elements within the region 
        will be 1, while otherwise will be 0.

        returns:
            (np.ndarray) 
        """
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape
        mask = np.zeros((dp_i, dp_j), dtype = self.data_object.dtype)
        widget = self._mask_widgets[self.mask_index]
        for ii in range(dp_i):
            for jj in range(dp_j):
                mask[ii, jj] = widget.isContained((ii, jj))
        return mask

    def startCalculation(self):
        """
        Start calculate virtual image of 4D-STEM.

        When the button 'Start Calculation' is clicked, this function will be 
        called. 
        """
        dialog_save = DialogSaveImage(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return 
        image_name = dialog_save.getNewName()
        image_parent_path = dialog_save.getParentPath()

        meta = self._generateImageMeta()
        mask = self._generateMask()
        self.task = TaskVirtualImage(
            self.data_path,
            image_parent_path,
            image_name,
            mask,
            **meta,
        )
        self.task_manager.addTask(self.task)

    def _generateImageMeta(self) -> dict:
        """
        Generate the meta data saved in the reconstructed image.
        """
        meta = {
            'image_mode': 'Virtual Image',
            'image_width': self.data_object.shape[1],
            'image_height': self.data_object.shape[0],
            'stem_path': self.data_path,
        }
        for key in self.data_object.attrs:
            new_key = 'stem_' + key
            meta[new_key] = self.data_object.attrs[key]
            # meta.update(new_key = self.data_object.attrs[key])
        
        meta['pixel_unit'] = 'm'

        if 'scan_step_size' in self.data_object.attrs:
            meta['pixel_size_i'] = self.data_object.attrs['scan_step_size']
            meta['pixel_size_j'] = self.data_object.attrs['scan_step_size']
        if 'scan_step_size_i' in self.data_object.attrs:
            meta['pixel_size_i'] = self.data_object.attrs['scan_step_size_i']
        if 'scan_step_size_j' in self.data_object.attrs:
            meta['pixel_size_j'] = self.data_object.attrs['scan_step_size_j'] 

        widget = self._mask_widgets[self.mask_index]
        mask_meta = widget.generateMeta()
        meta.update(**mask_meta)

        return meta 

    def _generateMask(self) -> np.ndarray:
        """
        Generate the integrate region.
        """
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape 
        mask = np.zeros((dp_i, dp_j), dtype = self.data_object.dtype)
        for ii in range(dp_i):
            for jj in range(dp_j):
                widget = self._mask_widgets[self.mask_index]
                mask[ii, jj] = widget.isContained((ii, jj))
        return mask
        

    def startCalculationTest(self):
        """
        Only for test.
        """
        mask = self._generateMask()
        dialog = DialogTestPlot(mask, self)
        dialog.exec()


class DialogTestPlot(QDialog):
    def __init__(self, image, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogTestPlot.Ui_Dialog()
        self.ui.setupUi(self)
        self.ax = self.ui.widget.figure.add_subplot(111)
        self.ax.imshow(image)
        
    
class DialogSaveImage(QDialog):
    """
    选择在 HDF 文件中保存重构图像路径的对话框。

    Dialog to choose where to save the reconstructed image in the HDF file.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogCreateImage.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_ok.clicked.connect(self.accept)
        self.ui.pushButton_cancel.clicked.connect(self.reject)
        self.ui.pushButton_browse.clicked.connect(self.browseParent)

        self.ui.lineEdit_name.setText('Untitled')
        self._validateNewName()

        
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler
        
    def browseParent(self) -> bool:
        """
        Open a dialog to browse a group to be parent.

        returns:
            (bool) whether a new path is set.
        """
        dialog_browse = DialogHDFChoose(self, only_group = True)
        dialog_code = dialog_browse.exec()
        if dialog_code == dialog_browse.Accepted:
            current_path = dialog_browse.getCurrentPath()
            if current_path:
                self.ui.lineEdit_parent_path.setText(current_path)
            return True 
        else:
            return False 

    def setParentPath(self, item_path: str):
        """
        Set the parent group's path where created images will locate.

        arguments:
            item_path: (str) 
        """
        if not isinstance(item_path, str):
            raise TypeError('item_path must be a str, not '
                '{0}'.format(type(item_path).__name__))
        
        node = self.hdf_handler.getNode(item_path)
        if not isinstance(node, HDFGroupNode):
            self.ui.lineEdit_parent_path.setText(node.parent.path)
        else:
            self.ui.lineEdit_parent_path.setText(item_path)

    def getParentPath(self) -> str:
        """
        Return the parent group's path where imported dataset will locate.

        returns:
            (str)
        """
        return self.ui.lineEdit_parent_path.text()

    def getNewName(self) -> str:
        """
        returns the new name of the imported dataset.

        Will add '.img' automatically as the extension.
        """
        name = self.ui.lineEdit_name.text()
        if '.' in name:
            if name.split('.')[-1] == 'img':
                return name 
        return name + '.img'

    def _validateNewName(self):
        """
        Set validator by regular expressioin for the name.
        """
        self.re_validator = QRegularExpressionValidator()
        self.re_validator.setRegularExpression(reValidHDFName.pattern)
        self.ui.lineEdit_name.setValidator(self.re_validator)
    

        
        




