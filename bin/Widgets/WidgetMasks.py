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
from typing import Iterable, List, Tuple

from PySide6.QtWidgets import QWidget
from matplotlib.figure import Figure
from matplotlib.patches import (
    Patch, 
    Circle, 
    CirclePolygon, 
    Ellipse, 
    Annulus, 
    Rectangle, 
    Wedge,
    RegularPolygon,
)
from matplotlib.axes import Axes
import numpy as np

from bin.BlitManager import BlitManager
from ui import uiWidgetMaskCircle
from ui import uiWidgetMaskRing
from ui import uiWidgetMaskWedge
from ui import uiWidgetMaskRectangle
from ui import uiWidgetMaskEllipse
from ui import uiWidgetMaskPolygon

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
    
    def setBlitManager(self, blit_manager: BlitManager):
        """
        Set the BlitManager to manage this patch.

        Will NOT add the patch to the blit manager's artist list. We should 
        add it by ourselves.

        arguments:
            blit_manager: (BlitManager)
        """
        if not isinstance(blit_manager, BlitManager):
            raise TypeError('blit_manager must be a BlitManager object, not '
                '{0}'.format(type(blit_manager).__name__))
        self._blit_manager = blit_manager

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
        self._resetPatchCenter()

    def _resetPatchCenter(self):
        """
        When the center is reset, reimplement this function to update.
        """
        self.logger.warning('_resetPatchCenter() should be reimplemented')

    def setMaskActivate(self, is_activated: bool):
        """
        If the mask is inactivated, the patch will be invisible.

        arguments:
            is_activate: (bool) 
        """
        # self.logger.debug('{0}: {1}'.format(type(self).__name__, self.patch))
        if not self.patch is None:
            self.patch.set_visible(is_activated)



class WidgetMaskCircle(WidgetMaskBase):
    """
    管理圆形的部件类。

    The Widget to manage circle patches.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetMaskCircle.Ui_Form()
        self.ui.setupUi(self)
        self._initUi()

        self._radius = 0
        self._shift_i = 0
        self._shift_j = 0


    @property
    def radius(self) -> float:
        """
        The radius of the circle.
        """
        return self._radius

    @property
    def shift_i(self) -> float:
        """
        The vertical shift of the center of the circle.
        """
        return self._shift_i

    @property
    def shift_j(self) -> float:
        """
        The horizontal shift of the center of the circle.
        """
        return self._shift_j

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

    
    def _initUi(self):
        """
        Initialize uis.
        """
        self.ui.doubleSpinBox_circle_radius.setValue(0)
        self.ui.doubleSpinBox_circle_radius.setRange(0, 65535)
        self.ui.doubleSpinBox_circle_center_i.setValue(0)
        self.ui.doubleSpinBox_circle_center_i.setRange(-32768, 32767)
        self.ui.doubleSpinBox_circle_center_j.setValue(0)
        self.ui.doubleSpinBox_circle_center_j.setRange(-32768, 32767)
        
        self.ui.doubleSpinBox_circle_radius.valueChanged.connect(
            self._updateCircleShape
        )
        self.ui.doubleSpinBox_circle_center_i.valueChanged.connect(
            self._updateCircleLocation
        )
        self.ui.doubleSpinBox_circle_center_j.valueChanged.connect(
            self._updateCircleLocation
        )
        
    def _updateCircleShape(self):
        """
        Set the shape of the circle and update.
        """
        self._radius = self.ui.doubleSpinBox_circle_radius.value()
        self.patch.set_radius(self.radius)
        self.blit_manager.update()

    def _updateCircleLocation(self):
        """
        Set the location of the circle and update.
        """
        self._shift_i = self.ui.doubleSpinBox_circle_center_i.value()
        self._shift_j = self.ui.doubleSpinBox_circle_center_j.value()

        self.patch.set_center((
            self.center[1] + self.shift_j,
            self.center[0] + self.shift_i
        ))
        self.blit_manager.update()

    def _resetPatchCenter(self):
        """
        Reset the patch's shift to the center of the image.

        This method is called whenever self.setCenter() method is called.
        """
        return self._updateCircleLocation()
        
        

class WidgetMaskRing(WidgetMaskBase):
    """
    管理环形的部件类。

    The widget to manage ring patches.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetMaskRing.Ui_Form()
        self.ui.setupUi(self)
        self._initUi()

        self._inner_radius = 0
        self._outer_radius = 1
        self._shift_i = 0
        self._shift_j = 0

    @property
    def inner_radius(self) -> float:
        return self._inner_radius

    @property
    def outer_radius(self) -> float:
        return self._outer_radius

    @property
    def shift_i(self) -> float:
        return self._shift_i

    @property
    def shift_j(self) -> float:
        return self._shift_j

    @property
    def patch(self) -> Annulus:
        return self._patch

    def _initUi(self):
        """
        Initialize Uis.
        """
        self.ui.doubleSpinBox_ring_inner.setValue(0)
        self.ui.doubleSpinBox_ring_inner.setRange(0, 65535)
        self.ui.doubleSpinBox_ring_outer.setValue(0)
        self.ui.doubleSpinBox_ring_outer.setRange(0, 65535)
        self.ui.doubleSpinBox_ring_center_i.setValue(0)
        self.ui.doubleSpinBox_ring_center_i.setRange(-32768, 32767)
        self.ui.doubleSpinBox_ring_center_j.setValue(0)
        self.ui.doubleSpinBox_ring_center_j.setRange(-32768, 32767)

        self.ui.doubleSpinBox_ring_inner.valueChanged.connect(
            self._updateRingShapeByInner
        )
        self.ui.doubleSpinBox_ring_outer.valueChanged.connect(
            self._updateRingShapeByOuter
        )
        self.ui.doubleSpinBox_ring_center_i.valueChanged.connect(
            self._updateRingLocation
        )
        self.ui.doubleSpinBox_ring_center_j.valueChanged.connect(
            self._updateRingLocation
        )

    def _updateRingShapeByInner(self):
        """
        Set the inner radius of the ring.

        The inner radius cannot be larger than the outer radius.
        """
        self._inner_radius = self.ui.doubleSpinBox_ring_inner.value()
        _inner_radius = min(self.inner_radius, self.outer_radius)

        self.patch.set_radii(self.outer_radius)
        self.patch.set_width(self.outer_radius - _inner_radius)
        self.blit_manager.update()

    def _updateRingShapeByOuter(self):
        """
        Set the outer radius of the ring.

        The outer radius cannot be larger than the inner radius.
        """
        self._outer_radius = self.ui.doubleSpinBox_ring_outer.value()
        _outer_radius = max(self.outer_radius, self.inner_radius)

        self.patch.set_radii(_outer_radius)
        self.patch.set_width(_outer_radius - self.inner_radius)
        self.blit_manager.update()

    def _updateRingLocation(self):
        """
        Set the location of the ring.
        """
        self._shift_i = self.ui.doubleSpinBox_ring_center_i.value()
        self._shift_j = self.ui.doubleSpinBox_ring_center_j.value()

        self.patch.set_center((
            self.center[1] + self.shift_j,
            self.center[0] + self.shift_i
        ))
        self.blit_manager.update()

    def _resetPatchCenter(self):
        """
        Reset the patch's shift to the center of the image.

        This method is called whenever self.setCenter() method is called.
        """
        return self._updateRingLocation()

    def setPatch(self, patch: Annulus):
        """
        Set the annulus to be managed.

        arguments:
            patch: (Annulus)
        """
        if not isinstance(patch, Annulus):
            raise TypeError('patch must be an Annulus, not '
                '{0}'.format(type(patch).__name__))
        super(WidgetMaskRing, self).setPatch(patch)

        radii = patch.get_radii()
        width = patch.get_width()
        self.ui.doubleSpinBox_ring_inner.setValue(radii[0] - width)
        self.ui.doubleSpinBox_ring_outer.setValue(radii[0])
        

class WidgetMaskWedge(WidgetMaskBase):
    """
    管理扇形的部件类。

    The widget to manage wedge patches.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetMaskWedge.Ui_Form()
        self.ui.setupUi(self)
        self._initUi()

        self._inner_radius = 0
        self._outer_radius = 0
        self._open_angle = 0
        self._shift_i = 0
        self._shift_j = 0
        self._rotation_angle = 0

    @property
    def inner_radius(self) -> float:
        return self._inner_radius

    @property
    def outer_radius(self) -> float:
        return self._outer_radius

    @property
    def open_angle(self) -> float:
        return self._open_angle

    @property
    def rotation_angle(self) -> float:
        return self._rotation_angle

    @property
    def shift_i(self) -> float:
        return self._shift_i

    @property
    def shift_j(self) -> float:
        return self._shift_j

    def _initUi(self):
        """
        Initialize Uis
        """
        self.ui.doubleSpinBox_wedge_inner.setValue(0)
        self.ui.doubleSpinBox_wedge_inner.setRange(0, 65535)
        self.ui.doubleSpinBox_wedge_outer.setValue(0)
        self.ui.doubleSpinBox_wedge_outer.setRange(0, 65535)
        self.ui.doubleSpinBox_wedge_open_angle.setValue(0)
        self.ui.doubleSpinBox_wedge_open_angle.setRange(0, 360)
        self.ui.doubleSpinBox_wedge_rotate_angle.setValue(0)
        self.ui.doubleSpinBox_wedge_rotate_angle.setRange(-32768, 32767)

        self.ui.doubleSpinBox_wedge_inner.valueChanged.connect(
            self._updateWedgeShapeByInner
        )
        self.ui.doubleSpinBox_wedge_outer.valueChanged.connect(
            self._updateWedgeShapeByOuter
        )
        self.ui.doubleSpinBox_wedge_open_angle.valueChanged.connect(
            self._updateWedgeShapeByOpenAngle
        )
        self.ui.doubleSpinBox_wedge_rotate_angle.valueChanged.connect(
            self._updateWedgeShapeByRotationAngle
        )
        self.ui.doubleSpinBox_wedge_center_i.valueChanged.connect(
            self._updateWedgeLocation
        )
        self.ui.doubleSpinBox_wedge_center_j.valueChanged.connect(
            self._updateWedgeLocation
        )

    def _updateWedgeShapeByInner(self):
        """
        Set the inner radius of the ring.

        The inner radius cannot be larger than the outer radius.
        """
        self._inner_radius = self.ui.doubleSpinBox_wedge_inner.value()
        _inner_radius = min(self.inner_radius, self.outer_radius)

        self.patch.set_radius(self.outer_radius)
        self.patch.set_width(self.outer_radius - _inner_radius)
        self.blit_manager.update()
        
    def _updateWedgeShapeByOuter(self):
        """
        Set the outer radius of the ring.

        The inner radius connot be larger than the outer radius.
        """
        self._outer_radius = self.ui.doubleSpinBox_wedge_outer.value()
        _outer_radius = max(self.outer_radius, self.inner_radius)

        self.patch.set_radius(_outer_radius)
        self.patch.set_width(_outer_radius - self.inner_radius)
        self.blit_manager.update()

    def _updateWedgeShapeByOpenAngle(self):
        """
        Set the open angle of the wedge.

        The open angle cannot be larger than 360 or less than 0.
        """
        self._open_angle = self.ui.doubleSpinBox_wedge_open_angle.value()
        _open_angle = min(360, max(0, self._open_angle))
        theta_1 = self.rotation_angle
        theta_2 = self.rotation_angle + _open_angle
        
        self.patch.set_theta1(theta_1)
        self.patch.set_theta2(theta_2)
        self.blit_manager.update()

    def _updateWedgeShapeByRotationAngle(self):
        """
        Set the rotation angle of the wedge.

        The rotation angle can be less than 0 or larger than 360.
        """
        self._rotation_angle = self.ui.doubleSpinBox_wedge_rotate_angle.value()
        _open_angle = min(360, max(0, self._open_angle))
        theta_1 = self.rotation_angle
        theta_2 = self.rotation_angle + _open_angle

        self.patch.set_theta1(theta_1)
        self.patch.set_theta2(theta_2)
        self.blit_manager.update()

    def _updateWedgeLocation(self):
        """
        Set the location of the wedge.
        """
        self._rotation_angle = self.ui.doubleSpinBox_wedge_rotate_angle.value()
        self._shift_i = self.ui.doubleSpinBox_wedge_center_i.value()
        self._shift_j = self.ui.doubleSpinBox_wedge_center_j.value()
        
        self.patch.set_center((
            self.center[1] + self.shift_j,
            self.center[0] + self.shift_i
        ))
        
        self.blit_manager.update()

    def _resetPatchCenter(self):
        """
        Reset the patch's shift to the center of the image.

        This method is called whenever self.setCenter() method is called.
        """
        return self._updateWedgeLocation()

    def setPatch(self, patch: Wedge):
        """
        Set the wedge to be managed.

        arguments:
            patch: (Wedge)
        """
        if not isinstance(patch, Wedge):
            raise TypeError('patch must be a Wedge, not '
                '{0}'.format(patch))
        super().setPatch(patch)

        theta_1 = patch.theta1
        theta_2 = patch.theta2
        radius = patch.r
        width = patch.width

        self.ui.doubleSpinBox_wedge_outer.setValue(radius)
        self.ui.doubleSpinBox_wedge_inner.setValue(radius - width)
        self.ui.doubleSpinBox_wedge_rotate_angle.setValue(theta_1)
        self.ui.doubleSpinBox_wedge_open_angle.setValue(theta_2 - theta_1)
        
    

class WidgetMaskRectangle(WidgetMaskBase):
    """
    管理矩形的部件类。

    The widget to manage rectangle patches.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetMaskRectangle.Ui_Form()
        self.ui.setupUi(self)
        self._initUi()

        self._width = 0
        self._height = 0
        self._shift_i = 0
        self._shift_j = 0
        self._rotation_angle = 0

    @property
    def width(self) -> float:
        return self._width

    @property
    def height(self) -> float:
        return self._height

    @property
    def shift_i(self) -> float:
        return self._shift_i

    @property
    def shift_j(self) -> float:
        return self._shift_j

    @property
    def rotation_angle(self) -> float:
        return self._rotation_angle

    def _initUi(self):
        """
        Initialize Uis.
        """
        self.ui.doubleSpinBox_rectangle_width.setValue(0)
        self.ui.doubleSpinBox_rectangle_width.setRange(0, 65535)
        self.ui.doubleSpinBox_rectangle_height.setValue(0)
        self.ui.doubleSpinBox_rectangle_height.setRange(0, 65535)
        self.ui.doubleSpinBox_rectangle_rotation_angle.setValue(0)
        self.ui.doubleSpinBox_rectangle_rotation_angle.setRange(-32768, 32767)
        self.ui.doubleSpinBox_rectangle_center_i.setValue(0)
        self.ui.doubleSpinBox_rectangle_center_i.setRange(-32768, 32767)
        self.ui.doubleSpinBox_rectangle_center_j.setValue(0)
        self.ui.doubleSpinBox_rectangle_center_j.setRange(-32768, 32767)

        self.ui.doubleSpinBox_rectangle_width.valueChanged.connect(
            self._updateRectangleShapeByWidth
        )
        self.ui.doubleSpinBox_rectangle_height.valueChanged.connect(
            self._updateRectangleShapeByHeight
        )
        self.ui.doubleSpinBox_rectangle_rotation_angle.valueChanged.connect(
            self._updateRectangleShapeByRotationAngle
        )
        self.ui.doubleSpinBox_rectangle_center_i.valueChanged.connect(
            self._updateRectangleLocation
        )
        self.ui.doubleSpinBox_rectangle_center_j.valueChanged.connect(
            self._updateRectangleLocation
        )

    def _updateRectangleShapeByWidth(self):
        """
        Set the width of the rectangle.

        The center of the rectangle will be unchanged.
        """
        self._width = self.ui.doubleSpinBox_rectangle_width.value()
        _xy = self._calculateAnchor()
        self.patch.set_width(self._width)
        self.patch.set_xy(_xy)
        self.blit_manager.update()

    def _updateRectangleShapeByHeight(self):
        """
        Set the height of the rectangle.

        The center of the rectangle will be unchanged.
        """
        self._height = self.ui.doubleSpinBox_rectangle_height.value()
        _xy = self._calculateAnchor()
        self.patch.set_height(self._height)
        self.patch.set_xy(_xy)
        self.blit_manager.update()

    def _updateRectangleShapeByRotationAngle(self):
        """
        Set the rotation angle of the rectangle.

        The rotation angle can be less than 0 or larger than 360. The center of
        the rectangle will be unchanged.
        """
        self._rotation_angle = (        # Here is NOT a tuple.
            self.ui.doubleSpinBox_rectangle_rotation_angle.value())
        _xy = self._calculateAnchor()
        self.patch.set_angle(self._rotation_angle)
        self.patch.set_xy(_xy)
        self.blit_manager.update()

    def _updateRectangleLocation(self):
        """
        Set the rectangle location.
        """
        self._shift_i = self.ui.doubleSpinBox_rectangle_center_i.value()
        self._shift_j = self.ui.doubleSpinBox_rectangle_center_j.value()
        _xy = self._calculateAnchor()
        self.patch.set_xy(_xy)
        self.blit_manager.update()

    def _resetPatchCenter(self):
        """
        Reset the patch's shift to the center of the image.

        This method is called whenever self.setCenter() method is called.
        """
        return self._updateRectangleLocation()

    def _calculateAnchor(self) -> Tuple[float, float]:
        """
        Returns the current anchor point of the rectangle.

        The anchor point is the xy as the bottom left corner of the rectangle.
        However, which corner xy is actually depends on the direction of the 
        axis and the sign of width and height. Here, xy would be the top-left
        corner, because the y-axis is inverted.

        We assign the center and rotation angle to the rectangle, and use this
        function to know where xy is.

        NOTE the coordinate in 4D-Explorer is i-j. Here we set x=j, y=i.

        returns:
            (x, y) the anchor point.
        """
        x_0 = self.center[1] + self.shift_j
        y_0 = self.center[0] + self.shift_i
        angle = self.rotation_angle*np.pi/180
        h = self.height
        w = self.width
        x = x_0 + h/2*np.sin(angle) - w/2*np.cos(angle)
        y = y_0 - h/2*np.cos(angle) - w/2*np.sin(angle)
        return (x, y)

    def setPatch(self, patch: Rectangle):
        """
        Set the rectangle to be managed.

        arguments:
            patch: (Rectangle)
        """
        if not isinstance(patch, Rectangle):
            raise TypeError('patch must be a Rectangle, not '
                '{0}'.format(type(patch).__name__))
        super().setPatch(patch)

        width = patch.get_width()
        height = patch.get_height()
        angle = patch.get_angle()
        self.ui.doubleSpinBox_rectangle_width.setValue(width)
        self.ui.doubleSpinBox_rectangle_height.setValue(height)
        self.ui.doubleSpinBox_rectangle_rotation_angle.setValue(angle)


class WidgetMaskEllipse(WidgetMaskBase):
    """
    管理椭圆形的部件类。

    The widget to manage ellipse patches.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetMaskEllipse.Ui_Form()
        self.ui.setupUi(self)
        self._initUi()

        self._width = 0
        self._height = 0
        self._shift_i = 0
        self._shift_j = 0
        self._rotation_angle = 0
        
    @property
    def width(self) -> float:
        return self._width

    @property
    def height(self) -> float:
        return self._height

    @property
    def shift_i(self) -> float:
        return self._shift_i

    @property
    def shift_j(self) -> float:
        return self._shift_j

    @property
    def rotation_angle(self) -> float:
        return self._rotation_angle

    def _initUi(self):
        """
        Initialize Uis.
        """
        self.ui.doubleSpinBox_ellipse_width.setValue(0)
        self.ui.doubleSpinBox_ellipse_width.setRange(0, 65535)
        self.ui.doubleSpinBox_ellipse_height.setValue(0)
        self.ui.doubleSpinBox_ellipse_height.setRange(0, 65535)
        self.ui.doubleSpinBox_ellipse_rotation_angle.setValue(0)
        self.ui.doubleSpinBox_ellipse_rotation_angle.setRange(-32768, 32767)
        self.ui.doubleSpinBox_ellipse_center_i.setValue(0)
        self.ui.doubleSpinBox_ellipse_center_i.setRange(-32768, 32767)
        self.ui.doubleSpinBox_ellipse_center_j.setValue(0)
        self.ui.doubleSpinBox_ellipse_center_j.setRange(-32768, 32767)

        self.ui.doubleSpinBox_ellipse_width.valueChanged.connect(
            self._updateEllipseShapeByWidth
        )
        self.ui.doubleSpinBox_ellipse_height.valueChanged.connect(
            self._updateEllipseShapeByHeight
        )
        self.ui.doubleSpinBox_ellipse_rotation_angle.valueChanged.connect(
            self._updateEllipseShapeByRotationAngle
        )
        self.ui.doubleSpinBox_ellipse_center_i.valueChanged.connect(
            self._updateEllipseLocation
        )
        self.ui.doubleSpinBox_ellipse_center_j.valueChanged.connect(
            self._updateEllipseLocation
        )

    def _updateEllipseShapeByWidth(self):
        """
        Set the width of the ellipse.

        The center of the rectangle will be unchanged.
        """
        self._width = self.ui.doubleSpinBox_ellipse_width.value()
        self.patch.set_width(self.width)
        self.blit_manager.update()

    def _updateEllipseShapeByHeight(self):
        """
        Set the height of the ellipse.
        """
        self._height = self.ui.doubleSpinBox_ellipse_height.value()
        self.patch.set_height(self.height)
        self.blit_manager.update()

    def _updateEllipseShapeByRotationAngle(self):
        """
        Set the rotation angle of the ellipse.
        """
        self._rotation_angle = (    # Here is NOT a tuple.
            self.ui.doubleSpinBox_ellipse_rotation_angle.value())
        self.patch.set_angle(self.rotation_angle)
        self.blit_manager.update()

    def _updateEllipseLocation(self):
        """
        Set the location of the ellipse.
        """
        self._shift_i = self.ui.doubleSpinBox_ellipse_center_i.value()
        self._shift_j = self.ui.doubleSpinBox_ellipse_center_j.value()
        self.patch.set_center(self._calculateAnchor())
        self.blit_manager.update()

    
    def _calculateAnchor(self) -> Tuple[float, float]:
        """
        Returns the center of the ellipse.

        returns:
            (x, y) the anchor (center) point.
        """
        x = self.center[1] + self.shift_j
        y = self.center[0] + self.shift_i
        return (x, y)

    def setPatch(self, patch: Ellipse):
        """
        Set the ellipse to be managed.

        arguments:
            patch: (Ellipse)
        """
        if not isinstance(patch, Ellipse):
            raise TypeError('patch must be a Ellipse, not '
                '{0}'.format(type(patch).__name__))
        super(WidgetMaskEllipse, self).setPatch(patch)

        width = patch.get_width()
        height = patch.get_height()
        angle = patch.get_angle()
        self.ui.doubleSpinBox_ellipse_width.setValue(width)
        self.ui.doubleSpinBox_ellipse_height.setValue(height)
        self.ui.doubleSpinBox_ellipse_rotation_angle.setValue(angle)

    def _resetPatchCenter(self):
        """
        Reset the patch's shift to the center of the image.

        This method is called whenever self.setCenter() method is called.
        """
        return self._updateEllipseLocation()

class WidgetMaskPolygon(WidgetMaskBase):
    """
    管理正多边形的部件类。

    The widget to manage regular polygon patches.

    The regular polygons have at least 3 vertices.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiWidgetMaskPolygon.Ui_Form()
        self.ui.setupUi(self)
        

        self._num_vertices = 3
        self._radius = 0
        self._shift_i = 0
        self._shift_j = 0
        self._rotation_angle = 0
        self.max_vertices = 20      # Max vertices available.

        self._initUi()

    @property
    def num_vertices(self) -> int:
        return self._num_vertices

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def shift_i(self) -> float:
        return self._shift_i

    @property
    def shift_j(self) -> float:
        return self._shift_j

    @property
    def rotation_angle(self) -> float:
        return self._rotation_angle

    @property
    def patch(self) -> List[RegularPolygon]:
        return self._patch

    def _initUi(self):
        """
        Initialize Uis.
        """
        self.ui.spinBox_vertices_number.setValue(3)
        self.ui.spinBox_vertices_number.setRange(3, self.max_vertices)
        self.ui.doubleSpinBox_polygon_radius.setValue(0)
        self.ui.doubleSpinBox_polygon_radius.setRange(0, 65535)
        self.ui.doubleSpinBox_polygon_center_i.setValue(0)
        self.ui.doubleSpinBox_polygon_center_i.setRange(-32768, 32767)
        self.ui.doubleSpinBox_polygon_center_j.setValue(0)
        self.ui.doubleSpinBox_polygon_center_j.setRange(-32768, 32767)
        self.ui.doubleSpinBox_polygon_rotate_angle.setValue(0)
        self.ui.doubleSpinBox_polygon_rotate_angle.setRange(-32768, 32767)

        self.ui.spinBox_vertices_number.valueChanged.connect(
            self._updatePolygonShapeByVertices
        )
        self.ui.doubleSpinBox_polygon_radius.valueChanged.connect(
            self._updatePolygonShapeByRadius
        )
        self.ui.doubleSpinBox_polygon_center_i.valueChanged.connect(
            self._updatePolygonLocation
        )
        self.ui.doubleSpinBox_polygon_center_j.valueChanged.connect(
            self._updatePolygonLocation
        )
        self.ui.doubleSpinBox_polygon_rotate_angle.valueChanged.connect(
            self._updatePolygonShapeByRotationAngle
        )

    def _updatePolygonShapeByVertices(self):
        """
        Set the number of the vertices of the regular polygon.

        Will find the corresponding polygon to show.
        """
        self._num_vertices = self.ui.spinBox_vertices_number.value()
        for ii, polygon in enumerate(self.patch):
            polygon.set_visible(ii + 3 == self._num_vertices)
        self.blit_manager.update()

    def _updatePolygonShapeByRadius(self):
        """
        Set the radius of the regular polygon.
        """
        self._radius = self.ui.doubleSpinBox_polygon_radius.value()
        for polygon in self.patch:
            polygon.radius = self._radius
        self.blit_manager.update()

    def _updatePolygonShapeByRotationAngle(self):
        """
        Set the rotation angle of the regular polygon.
        """
        self._rotation_angle = (   # This is NOT a tuple.
            self.ui.doubleSpinBox_polygon_rotate_angle.value())
        for polygon in self.patch:
            polygon.orientation = self._rotation_angle * np.pi/180
        self.blit_manager.update()

    def _updatePolygonLocation(self):
        """
        Update the location of the regular polygon.
        """
        self._shift_i = self.ui.doubleSpinBox_polygon_center_i.value()
        self._shift_j = self.ui.doubleSpinBox_polygon_center_j.value()
        x = self.center[1] + self.shift_j
        y = self.center[0] + self.shift_i
        for polygon in self.patch:
            polygon.xy = (x, y)
        self.blit_manager.update()

    def setPatch(self, patch: List[RegularPolygon]):
        """
        Set the regular polygons to be managed.

        arguments:
            patch: (list) a list that contains regular polygon patches.
        """
        if not isinstance(patch, Iterable):
            raise TypeError('patch must be an Iterable with '
                'regular polygons, not {0}'.format(type(patch).__name__))
        for p in patch:
            if not isinstance(p, RegularPolygon):
                raise TypeError('patch must be an Iterable with '
                    'regular polygons, but {0}'.format(type(p).__name__))
        self._patch = patch

        radius = self._patch[0].radius
        angle = self._patch[0].orientation / np.pi * 180
        self.ui.doubleSpinBox_polygon_radius.setValue(radius)
        self.ui.doubleSpinBox_polygon_rotate_angle.setValue(angle)
        self.ui.spinBox_vertices_number.setValue(3)

    def _resetPatchCenter(self):
        """
        Reset the patch's shift to the center of the image.

        This method is called whenever self.setCenter() method is called.
        """
        self.logger.debug('Polygon _resetPatchCenter is called')
        self._updatePolygonLocation()

    def setMaskActivate(self, is_activated: bool):
        """
        If the mask is inactivated, the patch will be invisible. Otherwise,
        only the polygon with corresponding vertices will be visible.

        arguments:
            is_activate: (bool) 
        """
        if is_activated:
            for ii, polygon in enumerate(self.patch):
                polygon.set_visible(ii + 3 == self._num_vertices)
            self.blit_manager.update()
        
        

    

class WidgetMaskSegment(WidgetMaskBase):
    """
    管理分段环形的部件类。

    The widget to manage segmented ring patches.
    """
    
    def setPatch(self, patches: List[Patch]):
        self._patch = patches

