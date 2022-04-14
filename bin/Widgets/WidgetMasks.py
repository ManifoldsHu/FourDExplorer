# -*- coding: utf-8 -*-

"""
*------------------------------ WidgetMasks.py -------------------------------*
用于使用 matplotlib 绘制各种几何形状的 Mask 的模组。

使用这些类以调整各种形状的位置和大小。其中包括：
    - 圆形
    - 环形
    - 扇形
    - 矩形
    - 椭圆形
    - 正多边形
    - 分段环形

作者：          胡一鸣
创建时间：      2022年4月10日

This module is used to plot geometric masks using matplotlib.

Use these classes to manage masks' locations and shapes. This module includes:
    - Circle
    - Ring (Annulus)
    - Wedge (Fan-like)
    - Rectangle
    - Ellipse
    - Regular Polygon
    - Segmented Ring

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
from ui import uiWidgetMaskSegment

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
            self._updateShape
        )
        self.ui.doubleSpinBox_circle_center_i.valueChanged.connect(
            self._updateLocation
        )
        self.ui.doubleSpinBox_circle_center_j.valueChanged.connect(
            self._updateLocation
        )
        
    def _updateShape(self):
        """
        Set the shape of the circle and update.
        """
        self._radius = self.ui.doubleSpinBox_circle_radius.value()
        self.patch.set_radius(self.radius)
        self.blit_manager.update()

    def _updateLocation(self):
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
        return self._updateLocation()

    def generateMeta(self) -> dict:
        """
        Generate the patch's metadata as a dict.

        returns:
            (dict)
        """
        meta = {
            'MaskShape': 'Circle',
            'MaskRadius': self.radius,
            'MaskCenterShiftI': self.shift_i,
            'MaskCenterShiftJ': self.shift_j, 
        }
        return meta
        
        

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
            self._updateByInner
        )
        self.ui.doubleSpinBox_ring_outer.valueChanged.connect(
            self._updateByOuter
        )
        self.ui.doubleSpinBox_ring_center_i.valueChanged.connect(
            self._updateLocation
        )
        self.ui.doubleSpinBox_ring_center_j.valueChanged.connect(
            self._updateLocation
        )

    def _updateInner(self):
        """
        Set the inner radius of the ring.

        The inner radius cannot be larger than the outer radius.
        """
        self._inner_radius = self.ui.doubleSpinBox_ring_inner.value()
        _inner_radius = min(self.inner_radius, self.outer_radius)

        self.patch.set_radii(self.outer_radius)
        self.patch.set_width(self.outer_radius - _inner_radius)
        self.blit_manager.update()

    def _updateOuter(self):
        """
        Set the outer radius of the ring.

        The outer radius cannot be larger than the inner radius.
        """
        self._outer_radius = self.ui.doubleSpinBox_ring_outer.value()
        _outer_radius = max(self.outer_radius, self.inner_radius)

        self.patch.set_radii(_outer_radius)
        self.patch.set_width(_outer_radius - self.inner_radius)
        self.blit_manager.update()

    def _updateLocation(self):
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
        return self._updateLocation()

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

        c_i = self.center[0] + self.shift_i
        c_j = self.center[1] + self.shift_j
        r_sq = (loc[0] - c_i)**2 + (loc[1] - c_j)**2
        return (r_sq > self.inner_radius**2) and (
                    r_sq < self.outer_radius**2)
        
    def generateMeta(self) -> dict:
        """
        Generate the patch's metadata as a dict.

        returns:
            (dict)
        """
        meta = {
            'MaskShape': 'Ring',
            'MaskOuterRadius': self.outer_radius,
            'MaskInnerRadius': self.inner_radius,
            'MaskCenterShiftI': self.shift_i,
            'MaskCenterShiftJ': self.shift_j, 
        }
        return meta


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
            self._updateInner
        )
        self.ui.doubleSpinBox_wedge_outer.valueChanged.connect(
            self._updateOuter
        )
        self.ui.doubleSpinBox_wedge_open_angle.valueChanged.connect(
            self._updateOpenAngle
        )
        self.ui.doubleSpinBox_wedge_rotate_angle.valueChanged.connect(
            self._updateRotationAngle
        )
        self.ui.doubleSpinBox_wedge_center_i.valueChanged.connect(
            self._updateLocation
        )
        self.ui.doubleSpinBox_wedge_center_j.valueChanged.connect(
            self._updateLocation
        )

    def _updateInner(self):
        """
        Set the inner radius of the ring.

        The inner radius cannot be larger than the outer radius.
        """
        self._inner_radius = self.ui.doubleSpinBox_wedge_inner.value()
        _inner_radius = min(self.inner_radius, self.outer_radius)

        self.patch.set_radius(self.outer_radius)
        self.patch.set_width(self.outer_radius - _inner_radius)
        self.blit_manager.update()
        
    def _updateOuter(self):
        """
        Set the outer radius of the ring.

        The inner radius connot be larger than the outer radius.
        """
        self._outer_radius = self.ui.doubleSpinBox_wedge_outer.value()
        _outer_radius = max(self.outer_radius, self.inner_radius)

        self.patch.set_radius(_outer_radius)
        self.patch.set_width(_outer_radius - self.inner_radius)
        self.blit_manager.update()

    def _updateOpenAngle(self):
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

    def _updateRotationAngle(self):
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

    def _updateLocation(self):
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
        return self._updateLocation()

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
        
    def generateMeta(self) -> dict:
        """
        Generate the patch's metadata as a dict.

        returns:
            (dict)
        """
        meta = {
            'MaskShape': 'Wedge',
            'MaskOuterRadius': self.outer_radius,
            'MaskInnerRadius': self.inner_radius,
            'MaskOpenAngle': self.open_angle,
            'MaskRotationAnlge': self.rotation_angle,
            'MaskCenterShiftI': self.shift_i,
            'MaskCenterShiftJ': self.shift_j, 
        }
        return meta


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
            self._updateWidth
        )
        self.ui.doubleSpinBox_rectangle_height.valueChanged.connect(
            self._updateHeight
        )
        self.ui.doubleSpinBox_rectangle_rotation_angle.valueChanged.connect(
            self._updateRotationAngle
        )
        self.ui.doubleSpinBox_rectangle_center_i.valueChanged.connect(
            self._updateLocation
        )
        self.ui.doubleSpinBox_rectangle_center_j.valueChanged.connect(
            self._updateLocation
        )

    def _updateWidth(self):
        """
        Set the width of the rectangle.

        The center of the rectangle will be unchanged.
        """
        self._width = self.ui.doubleSpinBox_rectangle_width.value()
        _xy = self._calculateAnchor()
        self.patch.set_width(self._width)
        self.patch.set_xy(_xy)
        self.blit_manager.update()

    def _updateHeight(self):
        """
        Set the height of the rectangle.

        The center of the rectangle will be unchanged.
        """
        self._height = self.ui.doubleSpinBox_rectangle_height.value()
        _xy = self._calculateAnchor()
        self.patch.set_height(self._height)
        self.patch.set_xy(_xy)
        self.blit_manager.update()

    def _updateRotationAngle(self):
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

    def _updateLocation(self):
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
        return self._updateLocation()

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

    def generateMeta(self) -> dict:
        """
        Generate the patch's metadata as a dict.

        returns:
            (dict)
        """
        meta = {
            'MaskShape': 'Rectangle',
            'MaskWidth': self.width,
            'MaskHeight': self.height,
            'MaskRotationAngle': self.rotation_angle,
            'MaskCenterShiftI': self.shift_i,
            'MaskCenterShiftJ': self.shift_j, 
        }
        return meta


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
            self._updateWidth
        )
        self.ui.doubleSpinBox_ellipse_height.valueChanged.connect(
            self._updateHeight
        )
        self.ui.doubleSpinBox_ellipse_rotation_angle.valueChanged.connect(
            self._updateRotationAngle
        )
        self.ui.doubleSpinBox_ellipse_center_i.valueChanged.connect(
            self._updateLocation
        )
        self.ui.doubleSpinBox_ellipse_center_j.valueChanged.connect(
            self._updateLocation
        )

    def _updateWidth(self):
        """
        Set the width of the ellipse.

        The center of the rectangle will be unchanged.
        """
        self._width = self.ui.doubleSpinBox_ellipse_width.value()
        self.patch.set_width(self.width)
        self.blit_manager.update()

    def _updateHeight(self):
        """
        Set the height of the ellipse.
        """
        self._height = self.ui.doubleSpinBox_ellipse_height.value()
        self.patch.set_height(self.height)
        self.blit_manager.update()

    def _updateRotationAngle(self):
        """
        Set the rotation angle of the ellipse.
        """
        self._rotation_angle = (    # Here is NOT a tuple.
            self.ui.doubleSpinBox_ellipse_rotation_angle.value())
        self.patch.set_angle(self.rotation_angle)
        self.blit_manager.update()

    def _updateLocation(self):
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
        return self._updateLocation()

    def generateMeta(self) -> dict:
        """
        Generate the patch's metadata as a dict.

        returns:
            (dict)
        """
        meta = {
            'MaskShape': 'Ellipse',
            'MaskWidth': self.width,
            'MaskHeight': self.height,
            'MaskRotationAngle': self.rotation_angle,
            'MaskCenterShiftI': self.shift_i,
            'MaskCenterShiftJ': self.shift_j, 
        }
        return meta


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
            self._updateVertices
        )
        self.ui.doubleSpinBox_polygon_radius.valueChanged.connect(
            self._updateRadius
        )
        self.ui.doubleSpinBox_polygon_center_i.valueChanged.connect(
            self._updateLocation
        )
        self.ui.doubleSpinBox_polygon_center_j.valueChanged.connect(
            self._updateLocation
        )
        self.ui.doubleSpinBox_polygon_rotate_angle.valueChanged.connect(
            self._updateRotationAngle
        )

    def _updateVertices(self):
        """
        Set the number of the vertices of the regular polygon.

        Will find the corresponding polygon to show.
        """
        self._num_vertices = self.ui.spinBox_vertices_number.value()
        for ii, polygon in enumerate(self.patch):
            polygon.set_visible(ii + 3 == self._num_vertices)
        self.blit_manager.update()

    def _updateRadius(self):
        """
        Set the radius of the regular polygon.
        """
        self._radius = self.ui.doubleSpinBox_polygon_radius.value()
        for polygon in self.patch:
            polygon.radius = self._radius
        self.blit_manager.update()

    def _updateRotationAngle(self):
        """
        Set the rotation angle of the regular polygon.
        """
        self._rotation_angle = (   # This is NOT a tuple.
            self.ui.doubleSpinBox_polygon_rotate_angle.value())
        for polygon in self.patch:
            polygon.orientation = self._rotation_angle * np.pi/180
        self.blit_manager.update()

    def _updateLocation(self):
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
        # self.logger.debug('Polygon _resetPatchCenter is called')
        self._updateLocation()

    def setMaskActivate(self, is_activated: bool):
        """
        If the mask is inactivated, the patch will be invisible. Otherwise,
        only the polygon with corresponding vertices will be visible.

        arguments:
            is_activate: (bool) 
        """
        for ii, polygon in enumerate(self.patch):
            polygon.set_visible(
                (ii + 3 == self._num_vertices) and is_activated
            )
        self.blit_manager.update()
        
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

        ax = self.patch[0].axes
        coordinate = ax.transData.transform((loc[1], loc[0]))
        _current_patch = self.patch[self._num_vertices - 3]
        return _current_patch.contains_point(coordinate)

    def generateMeta(self) -> dict:
        """
        Generate the patch's metadata as a dict.

        returns:
            (dict)
        """
        meta = {
            'MaskShape': 'RegularPolygon',
            'MaskRadius': self.radius,
            'MaskVerticeNumber': self.num_vertices,
            'MaskRotationAngle': self.rotation_angle,
            'MaskCenterShiftI': self.shift_i,
            'MaskCenterShiftJ': self.shift_j, 
        }
        return meta


class WidgetMaskSegment(WidgetMaskBase):
    """
    管理分段环形的部件类。

    The widget to manage segmented ring patches.
    """
    def __init__(self, parent: QWidget = None):
        """
        arguments:
            parent: (QWidget)
        """
        super().__init__(parent)
        self.ui = uiWidgetMaskSegment.Ui_Form()
        self.ui.setupUi(self)
        
        self._num_segments = 2
        self._inner_radius = 0
        self._outer_radius = 0
        self._open_angle = 0
        self._shift_i = 0
        self._shift_j = 0
        self._rotation_angle = 0
        self.max_segments = 10      # Max segments available.

        self._initUi()

    @property
    def num_segments(self) -> int:
        return self._num_segments

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
        self.ui.spinBox_num_segments.setValue(2)
        self.ui.spinBox_num_segments.setRange(1, self.max_segments)
        self.ui.doubleSpinBox_segment_inner.setValue(0)
        self.ui.doubleSpinBox_segment_inner.setRange(0, 65535)
        self.ui.doubleSpinBox_segment_outer.setValue(0)
        self.ui.doubleSpinBox_segment_outer.setRange(0, 65535)
        self.ui.doubleSpinBox_segment_open_angle.setValue(0)
        self.ui.doubleSpinBox_segment_open_angle.setRange(0, 360)
        self.ui.doubleSpinBox_segment_rotate_angle.setValue(0)
        self.ui.doubleSpinBox_segment_rotate_angle.setRange(-32768, 32767)
        self.ui.doubleSpinBox_segment_center_i.setValue(0)
        self.ui.doubleSpinBox_segment_center_i.setRange(-32768, 32767)
        self.ui.doubleSpinBox_segment_center_j.setValue(0)
        self.ui.doubleSpinBox_segment_center_j.setRange(-32768, 32767)
        
        self.ui.spinBox_num_segments.valueChanged.connect(
            self._updateNumSegments
        )
        self.ui.doubleSpinBox_segment_inner.valueChanged.connect(
            self._updateInnerRadius
        )
        self.ui.doubleSpinBox_segment_outer.valueChanged.connect(
            self._updateOuterRadius
        )
        self.ui.doubleSpinBox_segment_open_angle.valueChanged.connect(
            self._updateOpenAngle
        )
        self.ui.doubleSpinBox_segment_rotate_angle.valueChanged.connect(
            self._updateRotationAngle
        )
        self.ui.doubleSpinBox_segment_center_i.valueChanged.connect(
            self._updateLocation
        )
        self.ui.doubleSpinBox_segment_center_j.valueChanged.connect(
            self._updateLocation
        )

    def _updateNumSegments(self):
        """
        Change patches' shape by change the number of the segments.
        """
        self._num_segments = self.ui.spinBox_num_segments.value()
        self._resetThetas()
        for ii, segment in enumerate(self.patch):
            segment.set_visible(ii < self.num_segments)
        self.blit_manager.update()
        

    def _updateOpenAngle(self):
        """
        Change patches' shape by change the open angle of the segments.
        """
        self._open_angle = self.ui.doubleSpinBox_segment_open_angle.value()
        self._resetThetas()
        self.blit_manager.update()
        
    def _updateRotationAngle(self):
        """
        Change patches' shape by change the rotation angle of the segments.
        """
        self._rotation_angle = (    # Here is NOT a tuple
                self.ui.doubleSpinBox_segment_rotate_angle.value())
        self._resetThetas()
        self.blit_manager.update()

    def _resetThetas(self):
        """
        Reset the start angle and end angle of the segment wedges.

        Every wedge's angles will be decided by the number of wedges, the 
        open angle and the rotation angle. 
        """
        open_angle = min(360, max(0, self.open_angle))
        rotate_angle = self.rotation_angle
        num = self.num_segments
        if num < 1 or num > self.max_segments:
            return None
        for ii, segment in enumerate(self.patch):
            theta_1 = rotate_angle + 360 / num * ii
            theta_2 = theta_1 + open_angle
            segment.set_theta1(theta_1)
            segment.set_theta2(theta_2)
            # self.logger.debug('Segment {0}: theta1 {1}; '
            #     'theta2 {2}'.format(ii, theta_1, theta_2))
        return None 
    
    def _updateInnerRadius(self):
        """
        Change patches' shape by change their inner radius.
        """
        self._inner_radius = self.ui.doubleSpinBox_segment_inner.value()
        _inner_radius = min(self.inner_radius, self.outer_radius)
        for segment in self.patch:
            segment.set_radius(self.outer_radius)
            segment.set_width(self.outer_radius - _inner_radius)
        self.blit_manager.update()

    def _updateOuterRadius(self):
        """
        Change patches' shape by change their outer radius.
        """
        self._outer_radius = self.ui.doubleSpinBox_segment_outer.value()
        _outer_radius = max(self.outer_radius, self.inner_radius)
        for segment in self.patch:
            segment.set_radius(_outer_radius)
            segment.set_width(_outer_radius - self.inner_radius)
        self.blit_manager.update()

    def _updateLocation(self):
        """
        Change patches' location. 
        """
        self._shift_i = self.ui.doubleSpinBox_segment_center_i.value()
        self._shift_j = self.ui.doubleSpinBox_segment_center_j.value()
        for ii, segment in enumerate(self.patch):
            segment.set_center((
                self.center[1] + self.shift_j,
                self.center[0] + self.shift_i
            ))
        self.blit_manager.update()
    
    def _resetPatchCenter(self):
        return self._updateLocation()

    def setPatch(self, patch: List[Wedge]):
        """
        Set the patch list to be managed.

        arguments:
            patch: (List[Wedge])
        """
        if not isinstance(patch, Iterable):
            raise TypeError('patch must be an Iterable with '
                'Wedge, not {0}'.format(type(patch).__name__))
        for p in patch:
            if not isinstance(p, Wedge):
                raise TypeError('patches must be a Iterable with '
                    'Wedge in it, but given a {0}'.format(type(p).__name__))
        self._patch = patch

        theta_1 = patch[0].theta1
        theta_2 = patch[0].theta2
        radius = patch[0].r
        width = patch[0].width

        self.ui.doubleSpinBox_segment_outer.setValue(radius)
        self.ui.doubleSpinBox_segment_inner.setValue(radius - width)
        self.ui.doubleSpinBox_segment_rotate_angle.setValue(theta_1)
        self.ui.doubleSpinBox_segment_open_angle.setValue(theta_2 - theta_1)

    def setMaskActivate(self, is_activated: bool):
        """
        If the mask is inactivated, the patch will be invisible. Otherwise,
        only the polygon with corresponding vertices will be visible.

        arguments:
            is_activate: (bool) 
        """
        for ii, segment in enumerate(self.patch):
            segment.set_visible(ii < self.num_segments and is_activated)
        self.blit_manager.update()

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

        ax = self.patch[0].axes
        coordinate = ax.transData.transform((loc[1], loc[0]))
        for segment in self.patch[0:self.num_segments]:
            if segment.contains_point(coordinate):
                return True
        return False
        
    def generateMeta(self) -> dict:
        """
        Generate the patch's metadata as a dict.

        returns:
            (dict)
        """
        meta = {
            'MaskShape': 'SegmentRing',
            'MaskSegmentNumber': self.num_segments,
            'MaskInnerRadius': self.inner_radius,
            'MaskOuterRadius': self.outer_radius,
            'MaskOpenAngle': self.open_angle,
            'MaskRotationAngle': self.rotation_angle,
            'MaskCenterShiftI': self.shift_i,
            'MaskCenterShiftJ': self.shift_j, 
        }
        return meta
