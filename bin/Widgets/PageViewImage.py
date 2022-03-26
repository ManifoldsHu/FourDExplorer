# -*- coding: utf-8 -*-

"""
*---------------------------- PageViewImage.py -------------------------------*
显示二维图像(单通道)的页面。

部件内容：
    - WidgetImagePlot 用于使用 Matplotlib 来显示图像
    - WidgetImageHistPlot 用于使用 Matplotlib 来显示图像的直方图

提升部件：
    - 提升类名 PageViewImage
    - 头文件 bin.Widgets.PageViewImage

作者:           胡一鸣
创建日期:       2022年3月25日

The GUI page to view 2D images (single channel).

Contents:
    - WidgetImagePlot, to view the 2D image
    - WidgetImageHistPlot, to view the histogram of the image

Promoted Widget:
    - name of widget class: PageViewImage
    - header file: bin.Widget.PageViewImage

author:         Hu Yiming
date:           Mar 25, 2022
*---------------------------- PageViewImage.py -------------------------------*
"""

from logging import Logger
from PySide6.QtWidgets import QWidget, QMessageBox
import h5py
from bin.HDFManager import HDFDataNode, HDFHandler
from ui import uiPageViewImage

class PageViewImage(QWidget):
    """
    显示二维图像的部件类。

    Ui 文件地址：ROOT_PATH/ui/uiPageViewImage.ui

    Widget to view 2D images.

    The path of the ui file: ROOT_PATH/ui/uiPageViewImage.ui
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageViewImage.Ui_Form()
        self.ui.setupUi(self)
        self._img = None
        self._img_path = ''

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler

    @property
    def img_obj(self) -> h5py.Dataset:
        return self.hdf_handler.file[self._img_path]

    @property
    def img_path(self) -> str:
        return self._img_path

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    def setImage(self, img_path: str):
        """
        Set the image path, to show the image.

        Will set the img_path attribute. The image must be a 2D matrix. 
        RGB images (3 channels) are not supported here.

        arguments:
            img_path: (str) the path of the image or data. 
        """
        if not isinstance(img_path, str):
            raise TypeError('img_path must be a str, not '
                '{0}'.format(type(img_path).__name__))

        msg = QMessageBox(parent = self)
        msg.setWindowTitle('Warning')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)

        try:
            img_node = self.hdf_handler.getNode(img_path)
        except KeyError as e:
            self.logger.error('{0}'.format(e), exc_info = True)
            msg.setText('There is no image: {0}'.format(img_path))
            msg.exec()
            return None
        
        if not isinstance(img_node, HDFDataNode):
            self.logger.error('Item {0} must be a Dataset'.format(img_path))
            msg.setText('Item {0} must be a Dataset'.format(img_path))
            msg.exec()
            return None

        img_obj = self.hdf_handler.file[img_path]
        if not len(img_obj.shape) == 2:
            self.logger.error('Data must be a 2D matrix. '
                '(length of shape must be 2)')
            msg.setText('Data must be a 2D matrix. '
                '(length of shape must be 2)')
            msg.exec()
            return None

        self._img_path = img_path
        self._renderImage()


    def _renderImage(self):
        """
        Read the image and its attributes, and show it.
        """
        pass

    def updateImage(self):
        pass

        
        
    