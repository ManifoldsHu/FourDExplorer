# -*- coding: utf-8 -*-

"""
*------------------------------ WidgetMasks.py -------------------------------*
用于使用 matplotlib 绘制各种几何形状的 Mask 的模组。

使用这些类以调整各种形状的位置和大小。

作者：          胡一鸣
创建时间：      2022年4月10日

This module is used to plot geometric masks using matplotlib.

Use these classes to manage masks' locations and shapes.

author:         Hu Yiming
date:           Apr 10, 2021
*------------------------------ WidgetMasks.py -------------------------------*
"""

from logging import Logger
from typing import Tuple

from PySide6.QtWidgets import QWidget
from matplotlib.figure import Figure
from matplotlib.patches import Patch, Circle, CirclePolygon, Ellipse
from matplotlib.axes import Axes
import numpy as np

from bin.BlitManager import BlitManager
from ui import uiWidgetMaskCircle

class WidgetMaskBase(QWidget):
    """
    管理各种几何形状的面板控制类的基类。

    The base class of widgets to manage geometric patches.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self._patch = None
        self._blit_manager = None
        self._center = (0, 0)

    @property
    def patch(self) -> Patch:
        return self._patch

    @property
    def axes(self) -> Axes:
        return self.patch.axes

    @property
    def figure(self) -> Figure:
        return self.patch.figure

    @property
    def blit_manager(self) -> BlitManager:
        return self._blit_manager

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    @property
    def center(self) -> Tuple[float, float]:
        return self._center

    def setPatch(self, patch: Patch):
        """
        Set the patch to be managed.

        arguments:
            patch: (Patch) the patch artist in matplotlib to be managed.
        """
        if not isinstance(patch, Patch):
            raise TypeError('patch must be Patch object, not '
                '{0}'.format(type(patch).__name__))
        self._patch = patch

        # reset blit manager to None when the patch is reset.
        if not self.blit_manager is None:
            if not patch in self.blit_manager:
                self._blit_manager = None
    
    def setBlitManager(self, blit_manager: BlitManager):
        """
        Set the BlitManager to manage this patch.

        Will add the patch to the blit manager's artist list.

        arguments:
            blit_manager: (BlitManager)
        """
        if not isinstance(blit_manager, BlitManager):
            raise TypeError('blit_manager must be a BlitManager object, not '
                '{0}'.format(type(blit_manager).__name__))
        self._blit_manager = blit_manager
        if not self.patch in blit_manager:
            blit_manager.addArtist(self.patch)

    def isContained(self, loc: Tuple) -> bool:
        """
        Test whether loc is contained in the patch.

        arguments:
            loc: (Tuple) must be (i, j) coordinates in the axes.
        """
        if not isinstance(loc, Tuple):
            raise TypeError('loc must be a tuple with 2 numbers, not '
                '{0}'.format(type(loc).__name__))

        elif len(loc) != 2:
            raise ValueError('loc must be a tuple with 2 numbers, but '
                '{0} is given'.format(len(loc)))
        
        coordinate = self.axes.transData.transform((loc[1], loc[0]))
        return self.patch.contains_point(coordinate)
        
    def setCenter(self, loc: Tuple):
        """
        Set the center of the original patch locates.

        The locations of patches are decided by the center and the shift_x,
        shift_y attributes.

        In default, the center is at this location:
            (image_data.shape[0] - 1)/2,
            (image_data.shape[1] - 1)/2.
        For example, for an image with shape (128, 128), the center will be 
        (63.5, 63.5). This is because in matplotlib the axes starts at -0.5 
        while ends at 127.5 .

        arguments:
            loc: (Tuple) must be (i, j) coordinates in the axes.
        """
        if not isinstance(loc, Tuple):
            raise TypeError('loc must be a tuple with 2 numbers, not '
                '{0}'.format(type(loc).__name__))

        elif len(loc) != 2:
            raise ValueError('loc must be a tuple with 2 numbers, but '
                '{0} is given'.format(len(loc)))

        self._center = loc

    def setMaskActivate(self, is_activated: bool):
        return self.patch.set_visible(is_activated)



class WidgetMaskCircle(WidgetMaskBase):
    """
    管理圆形的部件类。

    The Widget to manage circle patches.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetMaskCircle.Ui_Form()
        self.ui.setupUi(self)

    @property
    def radius(self) -> float:
        """
        The radius of the circle.
        """
        return self.ui.doubleSpinBox_circle_radius.value()

    @property
    def shift_i(self) -> float:
        """
        The vertical shift of the center of the circle.
        """
        return self.ui.doubleSpinBox_circle_center_i.value()

    @property
    def shift_j(self) -> float:
        """
        The horizontal shift of the center of the circle.
        """
        return self.ui.doubleSpinBox_circle_center_j.value()

    @property
    def patch(self) -> Circle:
        return self._patch

    def setPatch(self, patch: Patch):
        """
        Set the circle to be managed.

        arguments:
            patch: (Patch) the patch artist in matplotlib to be managed.
        """
        super(WidgetMaskCircle, self).setPatch(patch)
        if not isinstance(patch, (Circle, CirclePolygon)):
            self.logger.warning(
                'patch set to WidgetMaskCircle should be a Circle '
                'or CirclePolygon patch, but given '
                '{0}'.format(type(patch).__name__)
            )
        self.ui.doubleSpinBox_circle_radius.setValue(patch.radius)
        center_j, center_i = patch.center
        self.ui.doubleSpinBox_circle_center_i.setValue(
            center_i - self.center[0]
        )
        self.ui.doubleSpinBox_circle_center_j.setValue(
            center_j - self.center[1]
        )
    
    def _initUi(self):
        """
        Initialize uis.
        """
        self.ui.doubleSpinBox_circle_radius.setValue(5)
        self.ui.doubleSpinBox_circle_center_i.setValue(0)
        self.ui.doubleSpinBox_circle_center_j.setValue(0)
        self.ui.doubleSpinBox_circle_radius.setMinimum(0)
        
        self.ui.doubleSpinBox_circle_radius.valueChanged.connect(
            self._updateCircleShape
        )
        self.ui.doubleSpinBox_circle_center_i.valueChagned.connect(
            self._updateCircleLocation
        )
        self.ui.doubleSpinBox_circle_center_j.valueChanged.connect(
            self._updateCircleLocation
        )
        
    def _updateCircleShape(self):
        """
        Set the shape of the circle and update.
        """
        self.ui.patch.set_radius(self.radius)
        self.blit_manager.update()

    def _updateCircleLocation(self):
        """
        Set the location of the circle and update
        """
        self.ui.patch.set_center(
            self.center[1] + self.shift_j,
            self.center[0] + self.shift_i
        )
        self.blit_manager.update()


class WidgetMaskRing(WidgetMaskBase):
    """
    管理环形的部件类。

    The widget to manage ring patches.
    """
    pass


class WidgetMaskWedge(WidgetMaskBase):
    """
    管理扇形的部件类。

    The widget to manage wedge patches.
    """
    pass

class WidgetMaskRectangle(WidgetMaskBase):
    """
    管理矩形的部件类。

    The widget to manage rectangle patches.
    """
    pass


class WidgetMaskSegment(WidgetMaskBase):
    """
    管理分段环形的部件类。

    The widget to manage segmented ring patches.
    """
    pass

