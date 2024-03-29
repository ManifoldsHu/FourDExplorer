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

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QWidget 

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
            # if self._unit_meta == self._pixel_length_meta:
            if self._unit_meta in self.meta_manager.listSchemaKeys():
                unit = self.meta_manager.getSchemaUnit(self._pixel_length_meta)
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
        # self.ui.doubleSpinBox_bar_length.setValue(1)
        # if self.hdf_handler.file[self.item_path].attrs[]

        self.ui.pushButton_ok.setVisible(False)
        self.ui.pushButton_cancel.setVisible(False)

        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.checkBox_customize_scale.stateChanged.connect(
            self._setCustomizeScaleAvailable
        )
        self.ui.checkBox_bar_visible.setChecked(True)
        self.ui.checkBox_customize_scale.setChecked(False)
        self.ui.checkBox_text_follow_bar.setChecked(True)
        self.ui.checkBox_text_visible.setChecked(True)

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
            self.ui.doubleSpinBox_text_location_i.setEnabled(True)
            self.ui.doubleSpinBox_text_location_j.setEnabled(True)
        else:
            self.ui.doubleSpinBox_text_location_i.setEnabled(False)
            self.ui.doubleSpinBox_text_location_j.setEnabled(False)
        

    def _setCustomizeScaleAvailalbe(self): 
        """
        Set the customize scale available according to the relivant checkBox.
        """
        _use_customize_scale = self.ui.checkBox_customize_scale.isChecked()
        self.ui.lineEdit_custom_unit.setEnabled(_use_customize_scale)
        self.ui.doubleSpinBox_length_per_pixel.setEnabled(_use_customize_scale)

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
            if self.unit_manager.isUnitLength(self.pixel_length_unit):
                bar_length_unit = self.ui.comboBox_real_length_unit.currentText()
                bar_length_pix = self.unit_manager.convert(
                    bar_length, 
                    bar_length_unit, 
                    self.pixel_length_unit,
                ) / self.pixel_length
                bar_length_text = self.unit_manager.formatUnit(
                    bar_length_unit, 
                    bar_length, 
                    'unicode'
                )
            elif self.unit_manager.isUnitSpaceFrequency(self.pixel_length_unit):
                space_freq_unit = self.ui.comboBox_reciprocal_unit.currentText()
                bar_length_unit = space_freq_unit.replace('⁻¹', '**-1')
                bar_length_pix = self.unit_manager.convert(
                    bar_length, 
                    bar_length_unit,
                    self.pixel_length_unit,
                ) / self.pixel_length 
                bar_length_text = self.unit_manager.formatUnit(
                    bar_length_unit, 
                    bar_length, 
                    'unicode'
                )
            else:
                bar_length_unit = 'pix'
                bar_length_pix = bar_length 
                bar_length_text = f"{bar_length} {bar_length_unit}"
        else:
            bar_length = self.ui.doubleSpinBox_bar_length.value()
            bar_length_pix = bar_length / self.ui.doubleSpinBox_length_per_pixel.value()
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
        self._scale_bar.set_angle(self.ui.spinBox_text_rotation.value())
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
        self._scale_bar_text.set_rotation(
            self.ui.spinBox_text_rotation.value()
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
            line_width = self.ui.doubleSpinBox_text_bg_edge_width.value(),
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
            pos_dict = {
                'upper left': (0.1, 0.1),
                'upper': (0.5, 0.1),
                'upper right': (0.9, 0.1),
                'left': (0.1, 0.5),
                'middle': (0.5, 0.5),
                'right': (0.9, 0.5),
                'bottom left': (0.1, 0.9),
                'bottom': (0.5, 0.9),
                'bottom right': (0.9, 0.9),
            }
            x_pos, y_pos = pos_dict[self.ui.comboBox_bar_location.currentText()]
            self._scale_bar.set_x((1-x_pos) * x_start + x_pos * x_end)
            self._scale_bar.set_y((1-y_pos) * y_start + y_pos * y_end)
        if self.ui.checkBox_text_follow_bar.isChecked():
            self._scale_bar_text.set_x(self._scale_bar.get_x())
            self._scale_bar_text.set_y(self._scale_bar.get_y())
        else:
            self._scale_bar_text.set_x(
                self.ui.doubleSpinBox_bar_location_j.value()
            )
            self._scale_bar_text.set_y(
                self.ui.doubleSpinBox_bar_location_i.value()
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
        Set the scale bar metadata directory path.
        
        In which there will stores 
        
        arguments:
            scale_bar_meta_dir: (str)
        """
