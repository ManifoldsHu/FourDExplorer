# -*- coding: utf-8 -*- 

"""
*---------------------------- PlotActions.py ---------------------------------*
针对各种画图操作的 Action。

作者:           胡一鸣
创建日期:       2024年3月29日

This module includes actions towards matplotlib widgets.

author:         Hu Yiming
date:           Mar 29, 2024
*---------------------------- PlotActions.py ---------------------------------*
"""

from logging import Logger 


from PySide6.QtCore import QObject
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMessageBox

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.patches import Rectangle 
from matplotlib.text import Text 
import numpy as np

from bin.HDFManager import HDFHandler 
from bin.UIManager import ThemeHandler
from bin.BlitManager import BlitManager
from bin.Widgets.DialogScaleBar import DialogScaleBar 

class ActionPlotBase(QAction):
    """
    The base class of actions for editing matplotlib widgets.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._canvas = None 
        self._figure = None 
        self._axes = None 
        self._blit_manager = None 
        self._icon_name = ''
        
    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.logger 
    
    @property 
    def canvas(self) -> FigureCanvas:
        return self._canvas 
    
    @property
    def figure(self) -> Figure:
        return self._figure
    
    @property
    def axes(self) -> Axes:
        return self._axes
    
    @property
    def blit_manager(self) -> BlitManager:
        return self._blit_manager

    def setCanvas(self, canvas: FigureCanvas):
        """
        Set the canvas that the action should manage.

        arguments:
            canvas: (FigureCanvas)
        """
        self._canvas = canvas 

    def setFigure(self, figure: Figure):
        """
        Set the figure that the action should manage.

        In general, the canvas of the figure should be the same as self.canvas

        arguments:
            figure: (Figure)
        """
        self._figure = figure 

    def setAxes(self, axes: Axes):
        """
        Set the axes that the action should manage.

        Although an action may not rely on one certain axes, this function is 
        provided for convenience.

        arguments:
            axes: (Axes)
        """
        self._axes = axes 

    def setBlitManager(self, blit_manager: BlitManager):
        """
        Set the blit manager that the action should manage.

        arguments:
            blit_manager: (BlitManager) 
        """
        self._blit_manager = blit_manager

    def _updateIcon(self):
        """
        Will update the icon when the theme mode changes.
        """
        if self._icon_name:
            _path = ':/Navigation/resources/icons/' + self._icon_name
            icon = self.theme_handler.iconProvider(_path)
            self.setIcon(icon)

    def initIconResources(self, icon_name: str):
        """
        Initialize the resource of icons.

        arguments:
            icon_name: (str) the name of icon.
        """
        _path = ':/Navigation/resources/icons/' + icon_name 
        icon = self.theme_handler.iconProvider(_path)
        self._icon_name = icon_name 
        self.setIcon(icon)

def failLogging(func):
    """
    Try to do something. If failed, log it.

    This is a decorator, used for these actions on-triggered functions.
    """
    def wrapper(self: ActionPlotBase, *args, **kw):
        try:
            func(*args, **kw)
        except Exception as e:
            self.logger.error('{0}'.format(e), exc_info = True)
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('An exception happened in '
                '{0}: {1}'.format(self.text(), e))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
    return wrapper 
        

class ActionScaleBar(ActionPlotBase):
    """
    The Action to manage the scale bar dialog.
    """
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.setText('Scale bar')
        self._item_path = ''
        self._icon_name = ''
        self._dialog = None 
        self._scale_bar = None
        self._scale_bar_text = None  
        global qApp 
        self._dialog = DialogScaleBar(qApp.main_window)
        self.triggered.connect(self.manageScaleBar)

    @property
    def dialog_scale_bar(self) -> DialogScaleBar:
        return self._dialog
    
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
    def pixel_length_meta(self) -> str:
        return self._pixel_length_meta 

    @property
    def unit_meta(self) -> str:
        return self._unit_meta 

    def setArtists(self, scale_bar: Rectangle, scale_bar_text: Text):
        """
        Set the artist that this action should manage.
        """
        self._scale_bar = scale_bar 
        self._scale_bar_text = scale_bar_text 
        
    # def setScaleBarDialog(self, dialog: DialogScaleBar):
    #     """
    #     Set the scale bar dialog that this action should manage.
    #     """
    #     self._dialog = dialog 

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

        arguments:
            unit_meta: (str)
        """
        self._unit_meta = unit_meta 

    def initialize(
        self,
        canvas: FigureCanvas = None,
        figure: Figure = None,
        axes: Axes = None,
        blit_manager: BlitManager = None,
        scale_bar: Rectangle = None,
        scale_bar_text: Text = None,
        item_path: str = '',
        pixel_length_meta: str = '',
        unit_meta: str = '',
    ):
        """
        Initialize the action with necessary objects.

        arguments:
            canvas: (FigureCanvase) Optional

            figure: (Figure) Optional 

            axes: (Axes) Optional 

            blit_manager: (BlitManager) Required, but can be set by 
                setBlitManager method.

            scale_bar: (Rectangle) Required, but can be set by setArtist 
                method.

            scale_bar_text: (Text) Required, but can be set by setArtist 
                method.

            item_path: (str) Optional, the path of the dataset

            pixel_length_meta: (str) Optional, the metadata key that stores 
                pixel length information.

            unit_meta: (str) Optional, the metadata key that stores the unit 
                of the pixel length.
        """
        dialog = self._dialog
        if canvas is not None:
            self.setCanvas(canvas)
            dialog.setCanvas(self.canvas)
        if figure is not None:
            self.setFigure(figure)
            dialog.setFigure(self.figure)
        if axes is not None:
            self.setAxes(axes)
            dialog.setAxes(self.axes)
        if blit_manager is not None:
            self.setBlitManager(blit_manager)
            dialog.setBlitManager(self.blit_manager)
        if scale_bar is not None and scale_bar_text is not None:
            self.setArtists(scale_bar, scale_bar_text)
            dialog.setScaleBar(self.scale_bar, self.scale_bar_text)
        if item_path:
            self.setItemPath(item_path)
            dialog.setItemPath(self.item_path)
        if pixel_length_meta:
            self.setPixelLengthMeta(pixel_length_meta)
            dialog.setPixelLengthMeta(self.pixel_length_meta)
        if unit_meta:
            self.setUnitMeta(unit_meta)
            dialog.setUnitMeta(self.unit_meta)

    def manageScaleBar(self):
        """
        Show the dialog to manage the scale bar.
        """
        pass
        # dialog = DialogScaleBar()
        dialog = self._dialog
        dialog.updateScaleBar()
        dialog.show()
        
    
