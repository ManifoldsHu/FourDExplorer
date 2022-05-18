# -*- coding: utf-8 -*-

"""
*--------------------------- PageCenterOfMass.py -----------------------------*
用于计算 4D-STEM 质心成像的页面。

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
    - 提升类名 PageCenterOfMass
    - 头文件 bin.Widgets.PageCenterOfMass

作者:           胡一鸣
创建日期:       2022年5月18日

The GUI page to calculate Center Of Mass images from 4D-STEM.

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
    - name of widget class: PageCenterOfMass
    - header file: bin.Widget.PageCenterOfMass

author:         Hu Yiming
date:           May 18, 2022
*--------------------------- PageCenterOfMass.py -----------------------------*
"""

from PySide6.QtWidgets import QWidget

from bin.Widgets.PageVirtualImage import PageVirtualImage
from bin.Widgets.PageVirtualImage import DialogSaveImage
from lib.TaskReconstruction import TaskCenterOfMass

class PageCenterOfMass(PageVirtualImage):
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

        self.setWindowTitle('Center Of Image')

    def startCalculation(self):
        """
        Start calculate Center Of Mass of 4D-STEM.

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
        meta['image_mode'] = 'Center Of Mass'
        attrs = self.data_object.attrs
        if 'dp_pixel_size' in attrs:
            meta['vector_length_i'] = attrs['dp_pixel_size']
            meta['vector_length_j'] = attrs['dp_pixel_size']
        else:
            if 'dp_pixel_size_i' in attrs:
                meta['vector_length_i'] = attrs['dp_pixel_size_i']
            if 'dp_pixel_size_j' in attrs:
                meta['vector_length_j'] = attrs['dp_pixel_size_j']

        mask = self._generateMask()
        self.task = TaskCenterOfMass(
            self.data_path,
            image_parent_path,
            image_name,
            mask,
            **meta,
        )
        self.task_manager.addTask(self.task)

    

