# -*- coding: utf -8 -*-

'''
*------------------- WidgetMaskCircle.py ------------------------*

头文件，用于定义调整 Maplotlib 显示窗口中 PatchCircle 的控制面板。建
议先定义好显示图像的窗口以及要显示的各种元素(尤其是 PatchCircle )，再
实例化这个控制面板。

作者：          胡一鸣
创建时间：      2021年7月25日

This is a header file, which is used to define the control panel
of PatchCircle of the Matplotlib preview widget. We recomend to
define the image (and Artists like PatchCircle) first, and then
instantiate this widget.

author:             Hu Yiming
date:               July 25, 2021

All rights reserved.

*------------------- WidgetMaskCircle.py ------------------------*
'''

from PyQt5.QtWidgets import QWidget
import numpy as np
import matplotlib as mpl
import ui.uiWidgetMaskCircle
from bin.BlitManager import BlitManager
from bin.Log import Log

class WidgetMaskCircle(QWidget):

    def __init__(
        self, 
        parent_widget,
        axes = None,
        patch_circle = None, 
        blit_manager = None,
        image_metadata = None,
        dataset_metadata = None,
        activated = True,
    ):
        '''
        arguments           type                description
        -----------------------------------------------------------------------
        parent_widget       QWidget             The window/dialog that this wi-
                                                dget belongs to

        axes                mpl.axes.Axes       The axes in which the chape of 
                                                the circle is adjusted

        patch_circle        mpl.patches.Circle  The circle patch object to be 
                                                controlled

        blit_manager        BlitManager         BlitManager contains the circle

        image_metadata      dict                including information of image 
                                                generated by this widget.
                                                NOTE: DEPRECATED, will provide 
                                                patch_metadata instead

        dataset_metadata    dict                including information of resol-
                                                ution of diffraction patterns
        -----------------------------------------------------------------------
        
        '''
        super().__init__()

        if isinstance(parent_widget, QWidget):
            self.parent_widget = parent_widget
        else:
            raise TypeError('type of parent_widget must be QWidget')


        if isinstance(axes, mpl.axes.Axes):
            self._ax = axes
        else:
            raise TypeError('type of axes must be mpl.axes.Axes')

        if isinstance(activated, bool):
            self._is_activated = activated
        else:
            raise TypeError('type of activated must be bool')
        
        if patch_circle is not None:
            if isinstance(patch_circle, mpl.patch.Circle):
                self._patch_circle = patch_circle
            else:
                raise TypeError('type of patch_circle must be mpl.patch.Circle')
        
        if blit_manager is not None:
            if isinstance(blit_manager, BlitManager):
                self._blit_manager = blit_manager
            else:
                raise TypeError('type of blit_manager must be BlitManager')

        if image_metadata is not None:
            if isinstance(image_metadata, dict):
                self.image_metadata = image_metadata
            else:
                raise TypeError('type of image_metadata must be dict')
        
        if dataset_metadata is not None:
            if isinstance(dataset_metadata, dict):
                self.dataset_metadata = dataset_metadata
            else:
                raise TypeError('type of dataset_metadata must be dict')
            

        self.ui = ui.uiWidgetMaskCircle.Ui_Form()
        self.ui.setupUi(self)


        if axes and patch_circle and blit_manager:
            # Provide the circle object to be controlled, otherwise this widget
            # will just initialize the basical uis, but cannot adjust the shape.
            self._has_axes = True
            self.lim_i = axes.get_ylim()
            self.lim_j = axes.get_xlim()
            self._initUi()
        else:
            self._has_axes = False

            # if 'dp_i' and 'dp_j' in dataset_metadata:
            #     self.dp_i = dataset_metadata['dp_i']
            #     self.dp_j = dataset_metadata['dp_j']
            #     self._initCircle()
            # else:
            #     self.dp_i = None
            #     self.dp_j = None
                
            
        self.setActivated(activated)
        self.patch_metadata = {}
        self.patch_metadata['MaskShape'] = 'Circle'
        self._radius = 0
        self._is_centered = True
        self._shift_x = 0
        self._shift_y = 0

        



    def _initUi(self):
        '''
        Initialize buttons, checkboxes and spinboxes. including:
            - doubleSpinBox_circle_radius       radius of the circle
            - checkBox_circle_is_center         whether set circle center of 
                                                the coordinate
            - doubleSpinBox_circle_center_i     center y-shift of the circle
            - doubleSpinBox_circle_center_j     center x-shift of the circle
        
        In future there will be more input widgets to control shapes of the 
        circle. 
        '''
        self.ui.doubleSpinBox_circle_radius.setValue(0)
        self.ui.doubleSpinBox_circle_radius.setRange(
            0,
            self.lim_i[1] + self.lim_j[1]
        )

        self.ui.checkBox_circle_is_center.setChecked(True)
        self.ui.checkBox_circle_is_center.stateChanged.connect(
            lambda: self.ui.doubleSpinBox_circle_center_i.setDisabled(
                self.ui.checkBox_circle_is_center.isChecked()
            )
        )
        self.ui.checkBox_circle_is_center.stateChanged.connect(
            lambda: self.ui.doubleSpinBox_circle_center_j.setDisabled(
                self.ui.checkBox_circle_is_center.isChecked()
            )
        )
        
        self.ui.doubleSpinBox_circle_center_i.setValue(0)
        self.ui.doubleSpinBox_circle_center_i.setRange(
            - self.lim_i[0] - self.lim_i[1],
            self.lim_i[0] + self.lim_i[1]
        )
        self.ui.doubleSpinBox_circle_center_j.setValue(0)
        self.ui.doubleSpinBox_circle_center_j.setRange(
            - self.lim_j[0] - self.lim_j[1],
            self.lim_j[0] + self.lim_j[1]
        )

        self.ui.doubleSpinBox_circle_radius.valueChanged.connect(self._updatePatch)
        self.ui.checkBox_circle_is_center.stateChanged.connect(self._updatePatch)
        self.ui.doubleSpinBox_circle_center_i.valueChanged.connect(self._updatePatch)
        self.ui.doubleSpinBox_circle_center_j.valueChanged.connect(self._updatePatch)


    def setActivated(self, activated):
        '''
        Set status of this widget. If there is corresponding axes and a circle 
        object, the activated buttons will affect the shape of the object inst-
        antly.

        arguments           type            description
        --------------------------------------------------------------------
        activated           bool            whether this widget is activated
        '''
        if isinstance(activated, bool):
            self._is_activated = activated
        else:
            raise TypeError('type of activated must be bool')

        self.ui.doubleSpinBox_circle_radius.setDisabled(not activated)
        self.ui.doubleSpinBox_circle_center_i.setDisabled(not activated)
        self.ui.doubleSpinBox_circle_center_j.setDisabled(not activated)
        self.ui.checkBox_circle_is_center.setDisabled(not activated)

        if self._has_axes:
            self._patch_circle.set_visible(activated)
    

    def getActivated(self):
        '''
        return:     bool
        '''
        return self._is_activated


    def setRadius(self, radius):
        '''
        Set radius of the circle.

        arguments           type
        ------------------------
        radius              float/int
        '''
        if isinstance(radius, (float, int)):
            self._radius = float(radius)
            self.ui.doubleSpinBox_circle_radius.setValue(radius)
            if self._has_axes:
                self._updatePatch()
        else:
            raise TypeError('radius must be float or int')

    def getRadius(self):
        '''
        return:         float
        '''
        return self._radius


    def setIsCentered(self, is_centered):
        '''
        Set whether the circle is centered.

        arguments           type
        ------------------------
        is_centered         bool
        '''
        if isinstance(is_centered, bool):
            self._is_centered = is_centered
            self.ui.checkBox_circle_is_center.setChecked(is_centered)
            if self._has_axes:
                self._updatePatch()
        else:
            raise TypeError('is_centered must be bool')

    def getIsCentered(self):
        '''
        return:         bool
        '''
        return self._is_centered

    
    def setShiftX(self, shift_x):
        '''
        Set the x-direction shift of the center of the circle.

        arguments           type
        ------------------------
        shift_x             float/int
        '''
        if isinstance(shift_x, (float, int)):
            self._shift_x = float(shift_x)
            self.ui.doubleSpinBox_circle_center_j.setValue(shift_x)
        else:
            raise TypeError('shift_x must be float/int')


    def getShiftX(self):
        '''
        return:         float
        '''
        return self._shift_x

    def setShiftY(self, shift_y):
        '''
        Set the y-direction shift of the center of the circle.

        arguments           type
        ------------------------
        shift_x             float/int
        '''
        if isinstance(shift_y, (float, int)):
            self._shift_y = float(shift_y)
            self.ui.doubleSpinBox_circle_center_j.setValue(shift_y)
        else:
            raise TypeError('shift_x must be float/int')


    def getShiftY(self):
        '''
        return:         float
        '''
        return self._shift_y


    def _updatePatch(self):
        if self._has_axes:
            try:
                if self._ax.figure.canvas != self._blit_manager.canvas:
                    raise RuntimeError(
                        'WidgetMaskCircle._ax.figure.canvas must be \
                         WidgetMaskCircle._blit_manager.canvas'
                    )
                if self._ax != self._patch_circle.axes:
                    raise RuntimeError(
                        'WidgetMaskCircle._patch_circle.axes must be\
                         WidgetMaskCircle._ax'
                    )
            except RuntimeError as e:
                


            



