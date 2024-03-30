# -*- coding: utf-8 -*- 

"""
*---------------------------- DialogScaleBar.py ------------------------------*
用于调整比例尺的对话框。

作者：          胡一鸣 
创建时间：      2024年3月27日

Dialog to adjust scale bars.

author:         Hu Yiming
date:           Mar 27, 2024
*---------------------------- DialogScaleBar.py ------------------------------*
"""

from logging import Logger 
import math

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QWidget 
from PySide6.QtWidgets import QMessageBox

import numpy as np
from matplotlib.figure import Figure 
from matplotlib.axes import Axes 
from matplotlib.image import AxesImage 
from matplotlib.axis import Axis 
from matplotlib.patches import Rectangle 
from matplotlib.text import Text 
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
# import matplotlib as mpl

from bin.HDFManager import HDFHandler
from bin.BlitManager import BlitManager
from bin.MetaManager import MetaManager
from bin.UIManager import ThemeHandler 
from bin.UnitManager import UnitManager

from ui import uiDialogScaleBar

class DialogScaleBar(QDialog):
    """
    调整比例尺的对话框，一般来说与 matplotlib 绘制窗口挂钩。

    Dialog to adjust scale bar. In general, it is linked to a matplotlib image.
    """

    _tab_colors = {
        'blue': 'tab:blue', 
        'brown': 'tab:brown', 
        'cyan': 'tab:cyan', 
        'gray': 'tab:gray', 
        'green': 'tab:green', 
        'orange': 'tab:orange', 
        'pink': 'tab:pink', 
        'red': 'tab:red', 
        'olive': 'tab:olive', 
        'purple': 'tab:purple',
    }
    
    _default_dict = {
        'bar_visible': True,
        'customize_scale': False,
        'bar_length': 20,
        'length_per_pixel': 1,
        'custom_unit': 'pix',
        'bar_width': 2,
        'bar_location': 'bottom left',
        'bar_location_i': 0,
        'bar_location_j': 0,
        'bar_rotation': 0,
        'bar_color': 'white',
        'text_visible': True,
        'text_follow_bar': True,
        'text_location_i': 0,
        'text_location_j': 0,
        'text_va': 'bottom',
        'text_ha': 'left',
        'text_rotation': 0,
        'text_font_family': 'sans-serif',
        'text_font_size': 12,
        'text_font_style': 'normal',
        'text_color': 'white',
        'text_alpha': 1,
        'text_bg_fill_visible': True,
        'text_bg_fill_alpha': 0.1,
        'text_bg_edge_width': 0,
        'text_bg_fill_color': 'black',
        'text_bg_edge_color': 'black'
    }

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.ui = uiDialogScaleBar.Ui_Dialog()
        self.ui.setupUi(self)
        self._axes = None 
        self._figure = None 
        self._image = None 
        self._scale_bar = None 
        self._scale_bar_text = None 
        self._item_path = '' 
        self._canvas = None 
        self._blit_manager = None 
        self._pixel_length_meta = ''
        self._unit_meta = ''
        self._scale_bar_meta_dir = '/ScaleBar'
        self._initUi()
        
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler 
    
    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    @property
    def axes(self) -> Axes:
        return self._scale_bar.axes
    
    @property
    def figure(self) -> Figure:
        return self._scale_bar.figure 
    
    @property
    def scale_bar(self) -> Rectangle:
        return self._scale_bar 
    
    @property
    def scale_bar_text(self) -> Text:
        return self._scale_bar_text
    
    @property
    def item_path(self) -> str:
        return self._item_path 
    
    @property
    def meta_manager(self) -> MetaManager:
        global qApp 
        return qApp.requireMetaManager(self.item_path)
    
    @property
    def unit_manager(self) -> UnitManager:
        global qApp 
        return qApp.unit_manager 
    
    @property
    def blit_manager(self) -> BlitManager:
        return self._blit_manager 
    
    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler 
    
    @property
    def pixel_length(self) -> float:
        """
        The length of a pixel in given unit.
        """
        if not self.ui.checkBox_customize_scale.isChecked():
            meta = self.hdf_handler.file[self.item_path].attrs 
            pixel_length = meta.get(self._pixel_length_meta)
            if pixel_length is None:
                # If no pixel length is available, unit is set to pixel number
                return 1
            return pixel_length 
        else:
            return self.ui.doubleSpinBox_length_per_pixel.value()        
    
    @property
    def pixel_length_unit(self) -> str:
        """
        The length unit of the pixel. Usually it can be read from metadata.
        """
        if not self.ui.checkBox_customize_scale.isChecked():
            if self._unit_meta in self.meta_manager.listSchemaKeys():
                # If unit_meta is defined in the schema and it is a float/int 
                # field that has its own unit, we will use its unit. This 
                # convention works when unit_meta is set the same as the 
                # pixel_length_meta. 
                unit = self.meta_manager.getSchemaUnit(self._unit_meta)
                if unit is not None:
                    return unit 
            meta = self.hdf_handler.file[self.item_path].attrs 
            pixel_length_unit = meta.get(self._unit_meta)
            if pixel_length_unit is None:
                # If no pixel length is available, unit is set to pixel number
                return 'pix'
            return pixel_length_unit
        unit_text = self.ui.lineEdit_custom_unit.text()
        if not unit_text:
            return 'pix'
        else:
            return unit_text
    
    def setBlitManager(self, blit_manager: BlitManager):
        """
        Set the BlitManager to manage the patch and text.

        Will NOT add the patch to the blit manager's artist list. It should be 
        done manually.

        arguments:
            blit_manager: (BlitManager)
        """
        if not isinstance(blit_manager, BlitManager):
            raise TypeError(
                f"blit_manager must be a BlitManager object,"
                " not {type(blit_manager).__name__}"
            )
        self._blit_manager = blit_manager 

    def setScaleBar(self, rectangle: Rectangle, text: Text):
        """
        Set the rectangle and text for this dialog to manage.

        arguments:
            rectangle: (Rectangle) The scale bar itself

            text: (Text) The text annotation of the scale bar
        """
        if not rectangle.axes is text.axes:
            raise RuntimeError("The rectangle and text must be in the same axes.")
        self._scale_bar = rectangle 
        self._scale_bar_text = text 
        self._scale_bar_text.set_rotation_mode('anchor')
        
    # def initScaleBarObjects(self, axes: Axes) -> tuple:
    #     """
    #     Initialize scale bar and text for this dialog to manage. 

    #     arguments:
    #         axes: (Axes) The axes where the scale bar will be drawn

    #     returns:
    #         (Rectangle, Text) A tuple that includes a Rectangle object and 
    #             a Text object. They are the scale bar and its text annotation
    #             respectively.
    #     """
    #     self._scale_bar = Rectangle(xy = (10, 10), width = 10, height = 3,)
    #     axes.add_patch(self._scale_bar)
    #     self._scale_bar_text = axes.text(
    #         x = 10, 
    #         y = 10, 
    #         text = '', 
    #         color='k', 
    #         verticalalignment='bottom', 
    #         horizontalalignment='left', 
    #     )
    #     return self._scale_bar, self._scale_bar_text
        
    def setItemPath(self, item_path: str):
        """
        Set the item_path where the meta should read from

        arguments:
            item_path: (str) The dataset's path
        """
        self._item_path = item_path 

    def setPixelLengthMeta(self, pixel_length_meta: str):
        """
        Set the meta key that defines pixel length.

        arguments:
            pixel_length_meta: (str)
        """
        self._pixel_length_meta = pixel_length_meta

    def setUnitMeta(self, unit_meta: str):
        """
        Set the meta key that defines the unit of pixel length.
        
        Note that if the unit_meta is defined in the schema and has predefined 
        unit, the unit will be read from the schema. 

        arguments:
            unit_meta: (str)
        """
        self._unit_meta = unit_meta 
        
    def setCanvas(self, canvas: FigureCanvas):
        self._canvas = canvas 
        
    def setFigure(self, figure: Figure):
        self._figure = figure 
        
    def setAxes(self, axes: Axes):
        self._axes = axes 

    def _initUi(self):
        """
        Initialize UIs.
        """
        self.ui.tabWidget.setCurrentIndex(0)                # basic
        self.ui.checkBox_customize_scale.stateChanged.connect(
            self._setCustomizeScaleAvailable
        )

        self._useDefaultMeta()
        
        self._setLocationUIs()
        
        self.ui.tabWidget_2.setCurrentIndex(0)              # text location
        
        self.ui.checkBox_bar_visible.stateChanged.connect(self.updateScaleBar)
        self.ui.checkBox_customize_scale.stateChanged.connect(self.updateScaleBar)
        self.ui.checkBox_text_bg_fill_visible.stateChanged.connect(self.updateScaleBar)
        self.ui.checkBox_text_follow_bar.stateChanged.connect(self.updateScaleBar)
        self.ui.checkBox_text_visible.stateChanged.connect(self.updateScaleBar)
        self.ui.comboBox_bar_color.currentIndexChanged.connect(self.updateScaleBar)
        self.ui.comboBox_bar_location.currentIndexChanged.connect(self.updateScaleBar)
        self.ui.comboBox_real_length_unit.currentIndexChanged.connect(self.updateScaleBar)
        self.ui.comboBox_reciprocal_unit.currentIndexChanged.connect(self.updateScaleBar)
        self.ui.comboBox_text_bg_edge_color.currentIndexChanged.connect(self.updateScaleBar)
        self.ui.comboBox_text_bg_fill_color.currentIndexChanged.connect(self.updateScaleBar)
        self.ui.comboBox_text_color.currentIndexChanged.connect(self.updateScaleBar)
        self.ui.comboBox_text_font_family.currentIndexChanged.connect(self.updateScaleBar)
        self.ui.comboBox_text_font_style.currentIndexChanged.connect(self.updateScaleBar)
        self.ui.comboBox_text_ha.currentIndexChanged.connect(self.updateScaleBar)
        self.ui.comboBox_text_va.currentIndexChanged.connect(self.updateScaleBar)
        self.ui.doubleSpinBox_bar_alpha.valueChanged.connect(self.updateScaleBar)
        self.ui.doubleSpinBox_bar_length.valueChanged.connect(self.updateScaleBar)
        self.ui.doubleSpinBox_bar_location_i.valueChanged.connect(self.updateScaleBar)
        self.ui.doubleSpinBox_bar_location_j.valueChanged.connect(self.updateScaleBar)
        self.ui.doubleSpinBox_bar_width.valueChanged.connect(self.updateScaleBar)
        self.ui.doubleSpinBox_length_per_pixel.valueChanged.connect(self.updateScaleBar)
        self.ui.doubleSpinBox_text_alpha.valueChanged.connect(self.updateScaleBar)
        self.ui.doubleSpinBox_text_bg_edge_width.valueChanged.connect(self.updateScaleBar)
        self.ui.doubleSpinBox_text_bg_fill_alpha.valueChanged.connect(self.updateScaleBar)
        self.ui.doubleSpinBox_text_location_i.valueChanged.connect(self.updateScaleBar)
        self.ui.doubleSpinBox_text_location_j.valueChanged.connect(self.updateScaleBar)
        self.ui.lineEdit_custom_unit.editingFinished.connect(self.updateScaleBar)
        self.ui.spinBox_bar_rotation.valueChanged.connect(self.updateScaleBar)
        self.ui.spinBox_text_font_size.valueChanged.connect(self.updateScaleBar)
        self.ui.spinBox_text_rotation.valueChanged.connect(self.updateScaleBar)
        
        self.ui.comboBox_bar_location.currentIndexChanged.connect(self._setLocationUIs)
        self.ui.checkBox_text_follow_bar.stateChanged.connect(self._setLocationUIs)
        
        self.ui.pushButton_cancel.clicked.connect(self._onCancel)
        self.ui.pushButton_ok.clicked.connect(self._onOk)

    def _setLocationUIs(self):
        """
        Set the location adjusting UIs of scale bar and its text annotation.
        """
        if self.ui.comboBox_bar_location.currentText() == 'custom location':
            self.ui.doubleSpinBox_bar_location_i.setEnabled(True)
            self.ui.doubleSpinBox_bar_location_j.setEnabled(True)
        else:
            self.ui.doubleSpinBox_bar_location_i.setEnabled(False)
            self.ui.doubleSpinBox_bar_location_j.setEnabled(False)
        if self.ui.checkBox_text_follow_bar.isChecked():
            self.ui.doubleSpinBox_text_location_i.setEnabled(False)
            self.ui.doubleSpinBox_text_location_j.setEnabled(False)
            self.ui.spinBox_text_rotation.setEnabled(False)
        else:
            self.ui.doubleSpinBox_text_location_i.setEnabled(True)
            self.ui.doubleSpinBox_text_location_j.setEnabled(True)
            self.ui.spinBox_text_rotation.setEnabled(True)
        

    def _setCustomizeScaleAvailable(self): 
        """
        Set the customize scale available according to the relivant checkBox.
        """
        _use_customize_scale = self.ui.checkBox_customize_scale.isChecked()
        self.ui.lineEdit_custom_unit.setEnabled(_use_customize_scale)
        self.ui.doubleSpinBox_length_per_pixel.setEnabled(_use_customize_scale)

    def _useDefaultMeta(self):
        """
        Use the default metadata to initialize UIs.
        """
        self.ui.checkBox_bar_visible.setChecked(True)
        self.ui.checkBox_customize_scale.setChecked(False)
        
        self.ui.doubleSpinBox_bar_length.setValue(20)
        self.ui.checkBox_customize_scale.setChecked(False)
        self.ui.doubleSpinBox_length_per_pixel.setValue(1)
        self.ui.lineEdit_custom_unit.setText('pix')
        self._setCustomizeScaleAvailable()
        self.ui.doubleSpinBox_bar_width.setValue(2)
        self.ui.comboBox_bar_location.setCurrentText('bottom left')
        self.ui.doubleSpinBox_bar_location_i.setValue(0)
        self.ui.doubleSpinBox_bar_location_j.setValue(0)
        self.ui.spinBox_bar_rotation.setValue(0)
        self.ui.comboBox_bar_color.setCurrentText('white')
        
        self.ui.checkBox_text_visible.setChecked(True)
        self.ui.checkBox_text_follow_bar.setChecked(True)
        self.ui.checkBox_text_follow_bar.setChecked(True)
        self.ui.doubleSpinBox_text_location_i.setValue(0)
        self.ui.doubleSpinBox_text_location_j.setValue(0)
        self.ui.comboBox_text_va.setCurrentText('bottom')
        self.ui.comboBox_text_ha.setCurrentText('left')
        self.ui.spinBox_text_rotation.setValue(0)
        self.ui.comboBox_text_font_family.setCurrentText('sans-serif')
        self.ui.spinBox_text_font_size.setValue(12)
        self.ui.comboBox_text_font_style.setCurrentText('normal')
        self.ui.comboBox_text_color.setCurrentText('white') 
        self.ui.doubleSpinBox_text_alpha.setValue(1)
        self.ui.checkBox_text_bg_fill_visible.setChecked(True)
        self.ui.doubleSpinBox_text_bg_fill_alpha.setValue(0.1)
        self.ui.doubleSpinBox_text_bg_edge_width.setValue(0)
        self.ui.comboBox_text_bg_fill_color.setCurrentText('black')
        self.ui.comboBox_text_bg_edge_color.setCurrentText('black')
        self.ui.checkBox_text_visible.setChecked(True)

    def _onCancel(self):
        self._useDefaultMeta()
        self.readScaleBarMeta()
        self.reject()
        
    def _onOk(self):
        # msg = QMessageBox(
        #     QMessageBox.Question, 
        #     'Save the scale bar',
        #     'Are you sure to save/overwrite the scale bar for this dataset?',
        #     QMessageBox.Ok | QMessageBox.Cancel,
        # )
        # ret = msg.exec()
        # if ret == msg.Accepted:
        #     self.saveScaleBarMeta()
        #     self.accept()
        # elif ret == msg.Rejected:
        #     self._useDefaultMeta()
        #     self.readScaleBarMeta()
        #     self.reject()
        self.saveScaleBarMeta()
        self.accept()
            
        # else:
        #     self._useDefaultMeta()
        #     self.readScaleBarMeta()
        #     self.reject()


    # def setDefaultSpaceType(self, default_space_type: str):
    #     """
    #     Set the default space type. This should be consistent with metadata of 
    #     the image.

    #     arguments:
    #         defualt_space_type: (str) Must be either 'real' or 'reciprocal'.
    #     """
    #     if default_space_type not in ('real', 'reciprocal'):
    #         raise ValueError('default_space_type must be one of "real" or "reciprocal"')
    #     if default_space_type == 'real':
    #         self.ui.stackedWidget.setCurrentIndex(0)
    #     elif default_space_type == 'reciprocal':
    #         self.ui.stackedWidget.setCurrentIndex(1)

    # def updateSpaceTypeFromMeta(self):
    #     """
    #     Update the default space type from metadata of the dataset.
    #     """
    #     meta = self.hdf_handler.file[self.item_path].attrs 
    #     pixel_length = meta.get(self._pixel_length_meta)
    #     pixel_length_unit = meta.get(self._unit_meta)
    #     if pixel_length and pixel_length_unit:
    #         if self.unit_manager.isUnitLength(pixel_length_unit):
    #             self.ui.stackedWidget.setCurrentIndex(0)
    #         elif self.unit_manager.isUnitSpaceFrequency(pixel_length_unit):
    #             self.ui.stackedWidget.setCurrentIndex(1)
    #         else:
    #             self.ui.stackedWidget.setCurrentIndex(2)
    #     else:
    #         self.ui.stackedWidget.setCurrentIndex(2)

    def initializeBarLength(self):
        """
        Initialize the bar length UI.
        
        This function should be called after the axes is assigned. Otherwise, 
        default bar length is used.
        """
        try:
            bar_length_pixels, display_unit = self.calcProperLength()
            bar_length = bar_length_pixels * self.pixel_length # in self.pixel_length_unit 
            bar_length = self.unit_manager.convert(
                bar_length_pixels * self.pixel_length,
                self.pixel_length_unit,
                display_unit 
            )
            self.ui.doubleSpinBox_bar_length.setValue(bar_length)
            self.ui.label_bar_unit.setText(
                self.unit_manager.formatUnit(display_unit, context = 'unicode')
            )
        except ValueError as e:
            bar_length = 20
            self.ui.label_bar_unit.setText(display_unit)

    def updateScaleBar(self):
        """
        Update the status of scale bar and companion text.
        """
        self._scale_bar.set_visible(self.ui.checkBox_bar_visible.isChecked())
        self._scale_bar.set_visible(self.ui.checkBox_text_visible.isChecked())

        self._updateScaleBarLocation()
        self._updateScaleBarLength()
        self._updateScaleBarStyle()
        self._updateScaleBarTextStyle()

        self.blit_manager.update()
        self._canvas.draw()
        self._canvas.flush_events()
        


    def _updateScaleBarLength(self):
        """
        Update the scale bar length accordindg to its length setting and units.
        """
        bar_length = self.ui.doubleSpinBox_bar_length.value()
        bar_length_pix = bar_length 
        if not self.ui.checkBox_customize_scale.isChecked():
            try:
                scale_bar_length_pixel, display_unit = self.calcProperLength()
                bar_length_text = self.unit_manager.formatUnit(
                    display_unit, bar_length, 'unicode'
                )
                self.ui.label_bar_unit.setText(
                    self.unit_manager.formatUnit(display_unit, context = 'unicode')
                )
                bar_length_pix = self.unit_manager.convert(bar_length, display_unit, self.pixel_length_unit) / self.pixel_length 
            except ValueError as e:
                bar_length_pix = bar_length 
                self.ui.label_bar_unit.setText('pix')
                bar_length_text = f"{bar_length} pix"

        else:
            bar_length = self.ui.doubleSpinBox_bar_length.value()
            bar_length_pix = bar_length / self.ui.doubleSpinBox_length_per_pixel.value()
            bar_length_unit = self.ui.lineEdit_custom_unit.text()
            bar_length_text = f"{bar_length} {bar_length_unit}"
        self._scale_bar.set_width(bar_length_pix)
        self._scale_bar_text.set_text(bar_length_text)


    def _getMatplotlibColor(self, color: str):
        """
        Get the matplotlib color name from color str.

        arguments:
            color: (str) 
        """
        if color in ('white', 'black', 'k', 'w'):
            return color 
        elif color in self._tab_colors:
            return self._tab_colors[color]
        else:
            return color 


    def _updateScaleBarStyle(self):
        """
        Update the style of the scale bar.
        """
        self._scale_bar.set_height(self.ui.doubleSpinBox_bar_width.value())
        self._scale_bar.set_angle(self.ui.spinBox_bar_rotation.value())
        bar_color = self.ui.comboBox_bar_color.currentText()
        self._scale_bar.set_color(self._getMatplotlibColor(bar_color))
        self._scale_bar.set_alpha(self.ui.doubleSpinBox_bar_alpha.value())


    def _updateScaleBarTextStyle(self):
        """
        Update the style of the text annotation of the scale bar.
        """
        self._scale_bar_text.set_horizontalalignment(
            self.ui.comboBox_text_ha.currentText()
        )
        self._scale_bar_text.set_verticalalignment(
            self.ui.comboBox_text_va.currentText()
        )

        text_color = self.ui.comboBox_text_color.currentText()
        self._scale_bar_text.set_color(
            self._getMatplotlibColor(text_color)
        )
        self._scale_bar_text.set_alpha(self.ui.doubleSpinBox_text_alpha.value())
        self._scale_bar_text.set_fontfamily(
            self.ui.comboBox_text_font_family.currentText()
        )
        self._scale_bar_text.set_fontsize(
            self.ui.spinBox_text_font_size.value()
        )
        self._scale_bar_text.set_fontstyle(
            self.ui.comboBox_text_font_style.currentText()
        )

        self._scale_bar_text.set_bbox(dict(
            facecolor = self._getMatplotlibColor(
                self.ui.comboBox_text_bg_fill_color.currentText()
            ),
            alpha = self.ui.doubleSpinBox_text_bg_fill_alpha.value(),
            edgecolor = self._getMatplotlibColor(
                self.ui.comboBox_text_bg_edge_color.currentText()
            ),
            linewidth = self.ui.doubleSpinBox_text_bg_edge_width.value(),
            visible = self.ui.checkBox_text_bg_fill_visible.isChecked(),
        ))


    def _updateScaleBarLocation(self):
        """
        Update scale bar and text location
        """
        if self.ui.comboBox_bar_location.currentText() == "custom location":
            self._scale_bar.set_x(self.ui.doubleSpinBox_bar_location_j.value())
            self._scale_bar.set_y(self.ui.doubleSpinBox_bar_location_i.value())
        else:
            x_start, x_end = self.axes.get_xlim()
            y_start, y_end = self.axes.get_ylim()
            # pos_dict = {
            #     'upper left': (0.1, 0.1),
            #     'upper': (0.5, 0.1),
            #     'upper right': (0.9, 0.1),
            #     'left': (0.1, 0.5),
            #     'middle': (0.5, 0.5),
            #     'right': (0.9, 0.5),
            #     'bottom left': (0.1, 0.9),
            #     'bottom': (0.5, 0.9),
            #     'bottom right': (0.9, 0.9),
            # }
            pos_dict = {
                'upper left': (0.1, 0.9),
                'upper': (0.4, 0.9),
                'upper right': (0.7, 0.9),
                'left': (0.1, 0.5),
                'middle': (0.4, 0.5),
                'right': (0.7, 0.5),
                'bottom left': (0.1, 0.1),
                'bottom': (0.4, 0.1),
                'bottom right': (0.7, 0.1),
            }
            x_pos, y_pos = pos_dict[self.ui.comboBox_bar_location.currentText()]
            self._scale_bar.set_x((1-x_pos) * x_start + x_pos * x_end)
            self._scale_bar.set_y((1-y_pos) * y_start + y_pos * y_end)
        if self.ui.checkBox_text_follow_bar.isChecked():
            self._scale_bar_text.set_x(self._scale_bar.get_x())
            self._scale_bar_text.set_y(self._scale_bar.get_y())
            self._scale_bar_text.set_rotation(
                - self.ui.spinBox_bar_rotation.value()  # Clock wise as positive
            )
        else:
            self._scale_bar_text.set_x(
                self.ui.doubleSpinBox_bar_location_j.value()
            )
            self._scale_bar_text.set_y(
                self.ui.doubleSpinBox_bar_location_i.value()
            )
            self._scale_bar_text.set_rotation(
                - self.ui.spinBox_text_rotation.value() # Clock wise as positive
            )
            


    # def _updateText(self):
    #     """
    #     Update text. It should look like: "20 nm"
    #     """
    #     if self.ui.checkBox_customize_scale.isChecked():
    #         if self.ui.lineEdit_custom_unit.text():
    #             unit_str = self.ui.lineEdit_custom_unit.text()
    #         else:
    #             unit_str = 'pix'
    #     else:
    #         meta = self.hdf_handler.file[self.item_path].attrs 
    #         pixel_length = meta.get(self._pixel_length_meta)
    #         pixel_length_unit = meta.get(self._unit_meta)
    #         if pixel_length and pixel_length_unit:
    #             if self.unit_manager.isUnitLength(pixel_length_unit):
    #                 unit_str = self.ui.comboBox_real_length_unit.currentText()
    #             elif self.unit_manager.isUnitSpaceFrequency(pixel_length_unit):
    #                 space_freq_unit = self.ui.comboBox_reciprocal_unit.currentText()
    #                 unit_str = space_freq_unit.replace('⁻¹', '**-1')
    #             else:
    #                 unit_str = 'pix'
        
        
    def setScaleBarMetaDirectoryPath(self, scale_bar_meta_dir: str):
        """
        Set the scale bar metadata directory path. The metadata about the scale 
        bar will be stored there, and will be read whenver the scale bar need 
        initialize.
        
        arguments:
            scale_bar_meta_dir: (str) Must be a valid meta path, start with '/' 
                and not end with '/'.
        """
        if not self.meta_manager.meta_tree.isValidPath(scale_bar_meta_dir):
            raise ValueError(
                f"scale_bar_meta_dir must be a valid meta path: {scale_bar_meta_dir}"
            )
        self._scale_bar_meta_dir = scale_bar_meta_dir


    def calcProperLength(self) -> tuple[float, str]:
        """
        Determine a user-friendly length and unit for the scale bar.
        
        This function calculates the scale bar length to be between 1/20 and 
        1/3 of the images' width, with a unit that makes the number user-
        friendly (e.g., convering 0.005 um to 5 nm). If a custom scale is 
        specified through the UI, it uses the user-defined length and unit.
        If the axes object is not set, defaults to a length between 10 and
        30 pixels.
        
        returns:
            (tuple[float, str]) A tuple containing the scale bar length and 
                its unit. The length is in pixels, and the unit is a string.
                
        raises:
            ValueError: If the specified unit is not recognized.
        """
        if self.ui.checkBox_customize_scale.isChecked():
            display_unit = self.ui.lineEdit_custom_unit.text()
            length = self.ui.doubleSpinBox_bar_length.value()
            return length, display_unit 
        
        min_pixels, max_pixels = 5, 100 
        if self.axes is not None:
            x_left, x_right = self.axes.get_xlim()
            x_width = x_right - x_left 
            if x_width >= 16:
                min_pixels, max_pixels = x_width / 20, x_width / 3 

        suitable_length_pixel = self._chooseRoundLength(
            self.pixel_length, 
            max_pixels, 
            min_pixels,
        )
        
        if suitable_length_pixel == -1:
            return (max_pixels + min_pixels) / 2, 'pix'
        
        original_unit = self.pixel_length_unit 
        if self.unit_manager.isUnitLength(original_unit):
            # Determine a user-friendly unit and scale factor 
            length_in_original_unit = suitable_length_pixel * self.pixel_length 
            for target_unit in ['nm', 'μm', 'mm', 'm', 'Å',]:
                try:
                    converted_length = self.unit_manager.convert(
                        length_in_original_unit, original_unit, target_unit 
                    )
                    if 1 <= converted_length < 1000:
                        return suitable_length_pixel, target_unit 
                    elif converted_length < 1 and target_unit == 'Å':
                        return suitable_length_pixel, target_unit 
                    elif converted_length >= 1000 and target_unit == 'm':
                        return suitable_length_pixel, target_unit 
                except ValueError:
                    continue 
        elif self.unit_manager.isUnitSpaceFrequency(original_unit):
            length_in_original_unit = suitable_length_pixel * self.pixel_length 
            for target_unit in ['nm**-1', 'μm**-1', 'mm**-1', 'm**-1', 'Å**-1',]:
                try:
                    converted_length = self.unit_manager.convert(
                        length_in_original_unit, original_unit, target_unit
                    )
                    if 1 <= converted_length < 1000:
                        return suitable_length_pixel, target_unit 
                    elif converted_length < 1 and target_unit == 'm**-1':
                        return suitable_length_pixel, target_unit 
                    elif converted_length >= 1000 and target_unit == 'Å**-1':
                        return suitable_length_pixel, target_unit 
                except ValueError:
                    continue 
                
        # Default case if no suitable conversion is found
        return suitable_length_pixel, original_unit

        
    def _chooseRoundLength(self, pixel_length: float, max_pixels: float, min_pixels: float) -> float:
        """
        Finds a suitable scale bar length in pixels that corresponds to a 'nice'
        physical length (like 1, 2, 5, 10, 20, etc.), ensuring the scale bar is 
        neither too long nor too short.
        
        arguments:
            pixel_length: (float) The physical length represented by one pixel, 
                e.g. 0.15 nm per pixel.
            
            max_pixels: (float) The maximum length for the scale bar in pixels.
                
            min_pixels: (float) The minimum length for the scale bar in pixels.
            
        returns:
            (float) The length of the scale bar in pixels that meets the 
                criteria, or -1 if no suitable length is found.
            
        raises:
            ValueError: If any of the inpus are non-positive, or max_pixels not 
                greater than min_pixels.
        """
        if pixel_length <= 0 or max_pixels <= 0 or min_pixels <= 0:
            raise ValueError("Arguments should be positive.")
        elif max_pixels <= min_pixels:
            raise ValueError("max_pixels must be greater than min_pixels")
        
        max_length = pixel_length * max_pixels 
        min_length = pixel_length * min_pixels 
        
        suitable_lengths = []
        base_numbers = [1, 2, 3, 5, 8]
        
        # Find the appropriate round number for the scale 
        for factor in range(-10, 10):
            for base in base_numbers:
                round_length = base * (10 ** factor)
                if min_length <= round_length <= max_length:
                    scale_bar_pixels = round_length / pixel_length
                    if min_pixels <= scale_bar_pixels <= max_pixels:
                        suitable_lengths.append(scale_bar_pixels)
        
        # If suitable lengths are found, return the one closest to the middle of
        # the min and max range.
        if len(suitable_lengths) > 0:
            suitable_lengths.sort(key = lambda x: abs(x - (min_pixels + max_pixels)/2))
            return suitable_lengths[0]
        return -1 


    def saveScaleBarMeta(self):
        """
        Save the scale bar metadata in the dataset.
        """
        # Scale bar properties
        self._setMeta('bar_visible', self.ui.checkBox_bar_visible.isChecked())
        self._setMeta('customize_scale', self.ui.checkBox_customize_scale.isChecked())
        self._setMeta('bar_length', self.ui.doubleSpinBox_bar_length.value())
        self._setMeta('custom_unit', self.ui.lineEdit_custom_unit.text())
        self._setMeta('length_per_pixel', self.ui.doubleSpinBox_length_per_pixel.value())
        self._setMeta('bar_width', self.ui.doubleSpinBox_bar_width.value())
        self._setMeta('bar_location', self.ui.comboBox_bar_location.currentText())
        self._setMeta('bar_location_i', self.ui.doubleSpinBox_bar_location_i.value())
        self._setMeta('bar_location_j', self.ui.doubleSpinBox_bar_location_j.value())
        self._setMeta('bar_rotation', self.ui.spinBox_bar_rotation.value())
        self._setMeta('bar_color', self.ui.comboBox_bar_color.currentText())

        # Text properties
        self._setMeta('text_visible', self.ui.checkBox_text_visible.isChecked())
        self._setMeta('text_follow_bar', self.ui.checkBox_text_follow_bar.isChecked())
        self._setMeta('text_location_i', self.ui.doubleSpinBox_text_location_i.value())
        self._setMeta('text_location_j', self.ui.doubleSpinBox_text_location_j.value())
        self._setMeta('text_va', self.ui.comboBox_text_va.currentText())  # Vertical alignment
        self._setMeta('text_ha', self.ui.comboBox_text_ha.currentText())  # Horizontal alignment
        self._setMeta('text_rotation', self.ui.spinBox_text_rotation.value())
        self._setMeta('text_font_family', self.ui.comboBox_text_font_family.currentText())
        self._setMeta('text_font_size', self.ui.spinBox_text_font_size.value())
        self._setMeta('text_font_style', self.ui.comboBox_text_font_style.currentText())
        self._setMeta('text_color', self.ui.comboBox_text_color.currentText())
        self._setMeta('text_alpha', self.ui.doubleSpinBox_text_alpha.value())

        # Text background properties
        self._setMeta('text_bg_fill_visible', self.ui.checkBox_text_bg_fill_visible.isChecked())
        self._setMeta('text_bg_fill_alpha', self.ui.doubleSpinBox_text_bg_fill_alpha.value())
        self._setMeta('text_bg_edge_width', self.ui.doubleSpinBox_text_bg_edge_width.value())
        self._setMeta('text_bg_fill_color', self.ui.comboBox_text_bg_fill_color.currentText())
        self._setMeta('text_bg_edge_color', self.ui.comboBox_text_bg_edge_color.currentText())
        
        
    def readScaleBarMeta(self):
        """
        Read the scale bar metadata from the dataset, and initialize GUIs.
        """

        def safe_set_ui(control, value, value_type=None):
            """
            Safely set the value of a UI control, with optional type conversion.

            arguments:
                control: The UI control to set.
                
                value: The value to set, which will be fetched from metadata.
                
                value_type: The type to which the value should be converted, if necessary.
            """
            try:
                if value is None:
                    return  # If the value is None, do nothing

                if value_type:
                    value = value_type(value)  # Convert the value if a type is specified

                if hasattr(control, 'setChecked') and isinstance(value, bool):
                    control.setChecked(value)
                elif hasattr(control, 'setValue') and isinstance(value, (int, float)):
                    control.setValue(value)
                elif hasattr(control, 'setText') and isinstance(value, str):
                    control.setText(value)
                elif hasattr(control, 'setCurrentText') and isinstance(value, str):
                    control.setCurrentText(value)
            except Exception as e:
                print(f"Error setting UI control: {e}")

        # List of UI elements and their corresponding metadata keys
        ui_elements = [
            (self.ui.checkBox_bar_visible, 'bar_visible', bool),
            (self.ui.checkBox_customize_scale, 'customize_scale', bool),
            (self.ui.doubleSpinBox_bar_length, 'bar_length', float),
            (self.ui.lineEdit_custom_unit, 'custom_unit', str),
            (self.ui.doubleSpinBox_length_per_pixel, 'length_per_pixel', float),
            (self.ui.doubleSpinBox_bar_width, 'bar_width', float),
            (self.ui.comboBox_bar_location, 'bar_location', str),
            (self.ui.doubleSpinBox_bar_location_i, 'bar_location_i', float),
            (self.ui.doubleSpinBox_bar_location_j, 'bar_location_j', float),
            (self.ui.spinBox_bar_rotation, 'bar_rotation', int),
            (self.ui.comboBox_bar_color, 'bar_color', str),
            (self.ui.checkBox_text_visible, 'text_visible', bool),
            (self.ui.checkBox_text_follow_bar, 'text_follow_bar', bool),
            (self.ui.doubleSpinBox_text_location_i, 'text_location_i', float),
            (self.ui.doubleSpinBox_text_location_j, 'text_location_j', float),
            (self.ui.comboBox_text_va, 'text_va', str),
            (self.ui.comboBox_text_ha, 'text_ha', str),
            (self.ui.spinBox_text_rotation, 'text_rotation', int),
            (self.ui.comboBox_text_font_family, 'text_font_family', str),
            (self.ui.spinBox_text_font_size, 'text_font_size', int),
            (self.ui.comboBox_text_font_style, 'text_font_style', str),
            (self.ui.comboBox_text_color, 'text_color', str),
            (self.ui.doubleSpinBox_text_alpha, 'text_alpha', float),
            (self.ui.checkBox_text_bg_fill_visible, 'text_bg_fill_visible', bool),
            (self.ui.doubleSpinBox_text_bg_fill_alpha, 'text_bg_fill_alpha', float),
            (self.ui.doubleSpinBox_text_bg_edge_width, 'text_bg_edge_width', float),
            (self.ui.comboBox_text_bg_fill_color, 'text_bg_fill_color', str),
            (self.ui.comboBox_text_bg_edge_color, 'text_bg_edge_color', str)
        ]

        # Iterate over the UI elements and set their values from metadata
        for control, key, value_type in ui_elements:
            value = self._getMeta(key)
            safe_set_ui(control, value, value_type)
        
        
    def _setMeta(self, key, value):
        meta = self.hdf_handler.file[self.item_path].attrs
        meta[self._scale_bar_meta_dir + '/' + key] = value 
        
    def _getMeta(self, key):
        meta = self.hdf_handler.file[self.item_path].attrs 
        value = meta.get(self._scale_bar_meta_dir + '/' + key)
        return value 
