# -*- coding: utf-8 -*-

"""
*------------------------- PageViewVectorField.py ----------------------------*
显示矢量场数据的页面。

部件内容：
    - WidgetPlotVector 用于使用 matplotlib 显示矢量场及背景
    - WidgetPlotBackground 用于使用 matplotlib 显示全域背景

提升部件
    - 提升类名 PageViewVectorField
    - 头文件 bin.Widgets.PageViewVectorField

作者:           胡一鸣
创建日期:       2022年5月18日

The GUI page to view Vector Field dataset.

Contents:
    - WidgetPlotVector, to view the vector fields and backgroud by matplotlib
    - WidgetPlotBackground, to view the full-scale background by matplotlib

Promoted Widget:
    - name of widget class: PageViewVectorField
    - header file: bin.Widgets.PageViewVectorField

author:         Hu Yiming
date:           Mar 30, 2022
*------------------------- PageViewVectorField.py ----------------------------*
"""

from logging import Logger
import os
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QInputDialog
from PySide6.QtWidgets import QDialog
# from PySide6.QtWidgets import QMenu
# from PySide6.QtCore import QPoint
from matplotlib.backend_bases import MouseEvent 
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure
from matplotlib.axes import Axes 
from matplotlib.image import AxesImage 
from matplotlib.quiver import Quiver
from matplotlib.patches import Rectangle
from matplotlib.colorbar import Colorbar, make_axes
import h5py 
import numpy as np

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFDataNode, HDFHandler
from bin.TaskManager import TaskManager 
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.Widgets.DialogSaveItem import DialogSaveImage
from bin.Widgets.DialogSaveItem import DialogSaveVectorField
from lib.TaskVectorFieldProcess import TaskCurl, TaskFlipVectorField
from lib.TaskVectorFieldProcess import TaskDivergence
from lib.TaskVectorFieldProcess import TaskPotential
from lib.TaskVectorFieldProcess import TaskRotateVectorAngle
from lib.TaskVectorFieldProcess import TaskSliceI
from lib.TaskVectorFieldProcess import TaskSliceJ
from lib.TaskVectorFieldProcess import TaskSubtractVectorOffset
from ui import uiDialogCreateImage
from ui import uiPageViewVectorField
from ui import uiDialogAdjustQuiverEffect
from ui import uiDialogVectorProcessing

class PageViewVectorField(QWidget):
    """
    显示二维矢量场的部件类。使用 Quiver。

    Ui 文件地址：ROOT_PATH/ui/uiPageVieweVectorField.ui

    Widget to view vector fields by quiver plot.

    The path of the ui file: ROOT_PATH/ui/uiPageViewVectorField.ui
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageViewVectorField.Ui_Form()
        self.ui.setupUi(self)

        self._data_path = ''
        self._background_path = ''
        self._image_ax = None 
        self._colorbar_ax = None 
        self._background_ax = None 
        self._quiver_object = None 
        self._colorbar_object = None 
        self._background_object = None
        self._image_object = None 
        self._scale_bar = None 
        self._scale_bar_text = None 
        self._image_max = 0
        self._image_min = 0

        self.ui.lineEdit_vector_path.setReadOnly(True)
        self.ui.lineEdit_background_path.setReadOnly(True)

        self._initUi()
        self._createAxes()

    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler 

    @property
    def data_object(self) -> h5py.Dataset:
        return self.hdf_handler.file[self._data_path]

    @property
    def data_path(self) -> str:
        return self._data_path

    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger

    @property
    def image_canvas(self) -> FigureCanvas:
        return self.ui.widget_quiver.canvas 

    @property
    def background_canvas(self) -> FigureCanvas:
        return self.ui.widget_background.canvas

    @property
    def image_figure(self) -> Figure:
        return self.ui.widget_quiver.figure 

    @property
    def background_figure(self) -> Figure:
        return self.ui.widget_background.figure 

    @property
    def image_ax(self) -> Axes:
        return self._image_ax 

    @property
    def background_ax(self) -> Axes:
        return self._background_ax

    @property
    def colorbar_ax(self) -> Axes:
        return self._colorbar_ax 

    @property
    def image_object(self) -> AxesImage:
        return self._image_object

    @property
    def quiver_object(self) -> Quiver:
        return self._quiver_object

    @property
    def colorbar_object(self) -> Colorbar:
        return self._colorbar_object

    @property
    def background_object(self) -> AxesImage:
        return self._background_object

    @property
    def background_path(self) -> str:
        return self._background_path

    @property
    def image_blit_manager(self) -> BlitManager:
        return self.ui.widget_quiver.blit_manager

    @property
    def background_blit_manager(self) -> BlitManager:
        return self.ui.widget_background.blit_manager

    @property
    def background_visible(self) -> bool:
        return self.ui.checkBox_background_visible.isChecked()

    @property
    def task_manager(self) -> TaskManager:
        global qApp 
        return qApp.task_manager

    def setVectorField(self, data_path: str):
        """
        Set the data path in HDF5 file, to show the vector field.

        Will set the data_path attribute. The vector field must be a 3D matrix.

        arguments:
            data_path: (str) the path of the vector field data.

        raises:
            TypeError, KeyError, ValueError
        """
        if not isinstance(data_path, str):
            raise TypeError('data_path must be a str, not '
                '{0}'.format(type(data_path).__name__))

        img_node = self.hdf_handler.getNode(data_path)  
        # May raise KeyError if the path does not exist
        if not isinstance(img_node, HDFDataNode):
            raise ValueError('Item {0} must be a Dataset'.format(data_path))

        data_obj = self.hdf_handler.file[data_path]
        if not len(data_obj.shape) == 3:
            raise ValueError('Data must be a 3D matrix (2, i, j)')

        self._data_path = data_path
        self.ui.lineEdit_vector_path.setText(self.data_path)
        self.setWindowTitle('{0} - Vector'.format(img_node.name))

        # We must first render the background image, in order not to 
        # cover the vector field.
        if 'background_path' in self.data_object.attrs:
            background_path = self.data_object.attrs['background_path']
            try:
                self.setBackground(background_path)
            except (KeyError, ValueError, TypeError):
                new_background_path = self._createNewBackground()
                self.setBackground(new_background_path)
        else:
            new_background_path = self._createNewBackground()
            self.setBackground(new_background_path)

        self._createQuiver()
        self._createScaleBar()
        
        self.image_canvas.draw()
        self.image_canvas.flush_events()
        
        self.ui.widget_quiver.setProcessingActionItemPath(self.data_path)
        self.ui.widget_quiver.action_scale_bar.dialog_scale_bar.initializeBarLength()
        self.ui.widget_quiver.action_scale_bar.dialog_scale_bar.readScaleBarMeta()
        self.ui.widget_quiver.action_scale_bar.dialog_scale_bar.updateScaleBar()


    def _createAxes(self):
        """
        Create the axes that contains the quiver, colorbar and the background
        respectively.
        """
        if self._image_ax is None:
            self._image_ax = self.image_figure.add_subplot()
            self.image_blit_manager.addArtist('image_axes', self._image_ax)
        
        if self._background_ax is None:
            self._background_ax = self.background_figure.add_subplot()
            self.background_blit_manager.addArtist(
                'background_axes', 
                self._background_ax,
            )

        if self._colorbar_ax is None:
            self._colorbar_ax, _kw = make_axes(
                self.background_ax,
                location = 'right',
                orientation = 'vertical',
            )
            self._colorbar_ax.xaxis.set_visible(False)
            self._colorbar_ax.yaxis.tick_right()

            self.background_blit_manager['colorbar_axes'] = self._colorbar_ax

    def _createQuiver(self):
        """
        Read the vector field and its attributes, and show it.

        TODO: read and save attributes, like length unit.
        """
        if self._quiver_object in self.image_ax.collections:
            # _index = self.image_ax.collections.index(self._quiver_object)
            # self.image_ax.collections.pop(_index)
            self._quiver_object.remove()

        _, height, width = self.data_object.shape 
        array_i = np.linspace(0, height - 1, height)
        array_j = np.linspace(0, width - 1, width)
        coord_i, coord_j = np.meshgrid(array_i, array_j, indexing = 'ij')
        vec_i, vec_j = self.data_object

        if 'quiver_scale' in self.data_object.attrs:
            quiver_scale = self.data_object.attrs['quiver_scale']
        else:
            self.data_object.attrs['quiver_scale'] = 1
            quiver_scale = 1
        
        if 'quiver_width' in self.data_object.attrs:
            quiver_width = self.data_object.attrs['quiver_width']
        else:
            self.data_object.attrs['quiver_width'] = 0.15
            quiver_width = 0.15
        
        if 'quiver_color' in self.data_object.attrs:
            quiver_color = self.data_object.attrs['quiver_color']
        else:
            self.data_object.attrs['quiver_color'] = 'black'
            quiver_color = 'black'

        X, Y = coord_j, coord_i 
        U, V = vec_j, vec_i 

        self._quiver_object = self.image_ax.quiver(
            X, Y, U, V,
            units = 'xy',
            scale = quiver_scale,
            width = quiver_width,
            angles = 'xy',
            pivot = 'mid',
            color = quiver_color,
        )

        self.image_blit_manager['quiver'] = self._quiver_object
        
    def _createScaleBar(self):
        """
        Create the scale bar and its text artist.
        """
        if self._scale_bar is None:
            self._scale_bar = Rectangle((1, 1), 1, 1)
            self.image_ax.add_patch(self._scale_bar)
        if self._scale_bar_text is None:
            self._scale_bar_text = self.image_ax.text(1, 1, '1')
        self.ui.widget_quiver.setScaleBarRelatedArtists(
            self._scale_bar, 
            self._scale_bar_text,
        )
        self.image_blit_manager['scale_bar'] = self._scale_bar 
        self.image_blit_manager['scale_bar_text'] = self._scale_bar_text 
        self.ui.widget_quiver.setScaleBarActionUseMeta(
            item_path = self.data_path,
            pixel_length_meta = '/Calibration/Space/pixel_size_i',
            unit_meta = '/Calibration/Space/pixel_size_unit',
        )

    def setBackground(self, background_path: str):
        """
        Set the background path in HDF5 file, to show the background image.

        Will set the background_path attribute. The background image must be
        a 2D matrix, RGB images (3 channels) are not supported here.

        The background image's shape must be equal to one of the channel of
        the vector field. For example, if the shape of the vector field is 
            2 x 256 x 256
        the shape of the background image must be 256 x 256 then.

        arguments:
            background_path: (str) the path of the image or data.

        raises:
            TypeError, KeyError, ValueError
        """
        if not isinstance(background_path, str):
            raise TypeError('background_path must be a str, not '
                '{0}'.format(type(background_path).__name__))

        background_node = self.hdf_handler.getNode(background_path)
        # May raise KeyError if the path does not exist
        if not isinstance(background_node, HDFDataNode):
            raise ValueError('Item {0} must be a '
                'Dataset'.format(background_path))
        
        background_data_obj = self.hdf_handler.file[background_path]
        if not len(background_data_obj.shape) == 2:
            raise ValueError('Data must be a 2D matrix (single channel image)')

        if self.data_path == '':
            raise ValueError('Must set vector field before set background')
        _, height, width = self.data_object.shape 
        if (background_data_obj.shape[0] != height 
                or background_data_obj.shape[1] != width):
            raise ValueError('The background image\'s shape must be equal to'
                ' one of the channel of the vector field.')
        
        self._background_path = background_path
        self.ui.lineEdit_background_path.setText(self.background_path)
        self.data_object.attrs['background_path'] = background_path

        self._createBackgroundImage()
        self._createColorbar()
        
        self.background_canvas.draw()
        self.background_canvas.flush_events()
        self.image_canvas.draw()
        self.image_canvas.flush_events()

    def _createBackgroundImage(self):
        """
        Create the axes and images of the background images.

        TODO: read and save attributes, like norm, cmap, alpha, etc.
        """
        # if self._background_object in self.background_ax.images:
        #     # clear current objects in the axes
        #     _index = self.background_ax.images.index(self._background_object)
        #     self.background_ax.images.pop(_index)
        # if self._background_object in self.background_ax.images:
        #     # Remove the current _background_object from the background axes
        #     _index = self.background_ax.images.index(self._background_object)
        #     del self.background_ax.images[_index]
        
        if self._background_object in self.background_ax.images:
            self._background_object.remove()

        self._background_object = self.background_ax.imshow(
            self.hdf_handler.file[self.background_path]
        )
        self.background_blit_manager['background_image'] = self._background_object

        if self._image_object in self.image_ax.images:
            # clear current objects in the axes
            # _index = self.image_ax.images.index(self._image_object)
            # self.image_ax.images.pop(_index)
            self._image_object.remove()
        
        self._image_object = self.image_ax.imshow(
            self.hdf_handler.file[self.background_path],
            interpolation = 'hermite',
        )
        self._image_object.set_visible(self.background_visible)
        self.image_blit_manager['image'] = self._image_object 


    def _createColorbar(self):
        """
        Create the colorbar according to the background image.
        """
        if self._colorbar_object is None:
            self._colorbar_object = Colorbar(
                ax = self.colorbar_ax,
                mappable = self.background_object
            )
        else:
            self.colorbar_object.update_normal(self.background_object)

    def _initUi(self):
        """
        Initialize UI.
        """
        self.ui.checkBox_background_visible.setChecked(False)
        self.ui.checkBox_background_visible.stateChanged.connect(
            self._setImageVisible
        )
    
        self.ui.pushButton_browse.clicked.connect(
            self._browse
        )
        self.ui.pushButton_browse_background.clicked.connect(
            self._browseBackground
        )
        # self.ui.pushButton_vector_processing.clicked.connect(
        #     self._vectorProcessing
        # )
        self.ui.pushButton_adjust_effects.clicked.connect(
            self._adjustEffects
        )

        self.ui.pushButton_show_color_wheel.setVisible(False)   # TODO
        self.ui.pushButton_show_color_wheel.setVisible(False)   # TODO

    def _adjustEffects(self):
        """
        Open a dialog to adjust quiver display effects.
        """
        dialog = DialogAdjustQuiverEffect(self)
        dialog.setVectorField(self.data_path)
        dialog_code = dialog.exec()
        if dialog_code == DialogAdjustQuiverEffect.Rejected:
            return 

        self.data_object.attrs['quiver_scale'] = dialog.getScale()
        self.data_object.attrs['quiver_width'] = dialog.getWidth()
        self.data_object.attrs['quiver_color'] = dialog.getColor()
        
        self.setVectorField(self.data_path)


    def _browse(self):
        """
        Open a dialog to browse which vector field to be opened.
        """
        dialog = DialogHDFChoose(self)
        dialog_code = dialog.exec()
        if dialog_code == dialog.Accepted:
            current_path = dialog.getCurrentPath()
        else:
            return 

        try:
            self.setVectorField(current_path)
        except (KeyError, ValueError, TypeError,) as e:
            self.logger.error('{0}'.format(e), exc_info = True)
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Cannot open this data: {0}'.format(e))
            msg.exec()

    def _browseBackground(self):
        """
        Open a dialog to browse which image to be opened as the background.
        """
        dialog = DialogHDFChoose(self)
        dialog_code = dialog.exec()
        if dialog_code == dialog.Accepted:
            current_path = dialog.getCurrentPath()
        else:
            return 

        try:
            self.setBackground(current_path)
        except (KeyError, ValueError, TypeError,) as e:
            self.logger.error('{0}'.format(e), exc_info = True)
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Cannot open this data: {0}'.format(e))
            msg.exec()

    def _setImageVisible(self):
        """
        Set whether the background image to be visible or not. 
        """
        self.image_object.set_visible(self.background_visible)
        self.image_blit_manager.update()

    def _createNewBackground(self):
        """
        Create a new background image.

        In default, it will be /.../[vector name]_bkgrd.img . If there has been
        a background at this path, try to use it. Otherwise, add an index and 
        try again: /.../[vector name]_bkgrd_1.img . The new path will be under
        the same group as the vector field.

        Users can calculate a new background and reset it themselves. 

        returns:
            (str) the path of the new background image.
        """
        
        # Get a valid new name of the new background image
        data_node = self.hdf_handler.getNode(self.data_path)
        if '.' in data_node.name:
            name_array = data_node.name.split('.')
            name_array.pop()
            original_name = '.'.join(name_array)
        else:
            original_name = data_node.name 

        bkgrd_name = original_name + '_bkgrd.img'
        _count = 0
        while bkgrd_name in data_node.parent:
            _count += 1
            bkgrd_name = original_name + '_bkgrd_{0}.img'.format(_count)
        
        # Get the shape of the new background image
        _, height, width = self.data_object.shape 
        
        self.hdf_handler.addNewData( 
            parent_path = data_node.parent.path, 
            name = bkgrd_name, 
            shape = (height, width), 
            dtype = 'float64',
        )

        # Get the path of the new background image
        if data_node.parent.path == '/':
            bkgrd_path = '/' + bkgrd_name 
        else:
            bkgrd_path = data_node.parent.path + '/' + bkgrd_name

        self.data_object.attrs['background_path'] = bkgrd_path

        return bkgrd_path
        

    def _vectorProcessing(self):
        """
        Open a dialog to show vector processing methods.

        Including change angles, subtracting mean vector, and calculate curl, 
        divergence, potential, ...
        """
        dialog = DialogVectorProcessing(self)
        dialog_code = dialog.exec()
        if not dialog_code == dialog.Accepted:
            return 
        result = dialog.getResult()
        if result == 'rotate':
            self._vectorRotateAngle()
        if result == 'subtract':
            self._vectorSubtract()
        if result == 'flip':
            self._vectorFlip()
        if result == 'potential':
            self._vectorPotential()
        if result == 'divergence':
            self._vectorDivergence()
        if result == 'curl':
            self._vectorCurl()
        if result == 'vec_i':
            self._vectorSliceI()
        if result == 'vec_j':
            self._vectorSliceJ()


    def _vectorRotateAngle(self):
        """
        Rotate every vector an angle.

        In practical experiment, there may exist some angular shift between 
        the scanning array and the pixelized camera, but we usually cannot 
        be aware of this by pure 4D-STEM dataset. Fortunately, we know that
        some vector fields (like Electric field) keeps non-curl, so we use 
        this property to get correct vector fields.
        """
        angle, is_accepted = QInputDialog.getDouble(
            self,
            'Input rotation angle',
            'Here input a rotation angle of every vector. Unit: degree',
            0,
            minValue = -360,
            maxValue = 360,
            decimals = 1,
            step = 1,
        )

        if not is_accepted:
            return 
        
        dialog_save = DialogSaveVectorField(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return 
        image_name = dialog_save.getNewName()
        image_parent_path = dialog_save.getParentPath()
        meta = self.data_object.attrs 
        
        self.task = TaskRotateVectorAngle(
            self.data_path,
            image_parent_path,
            image_name,
            angle = angle,
            parent = self,
            **meta,
        )
        
        self.task_manager.addTask(self.task)

    def _vectorSubtract(self):
        """
        Subtract every vector by their mean vector.

        In practical experiment, there may exist some shift between the center
        of the diffraction pattern and the origin of the diffraction plane. In 
        this case, the calculated center of mass will have an global offset. 
        Here this function will be able to recover the fine architecture of the
        vector field, by set the vector offset to be zero.
        """
        dialog_save = DialogSaveVectorField(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return 
        image_name = dialog_save.getNewName()
        image_parent_path = dialog_save.getParentPath()
        meta = self.data_object.attrs 

        self.task = TaskSubtractVectorOffset(
            self.data_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)

    def _vectorFlip(self):
        """
        Exchange every vector's i, j components.

        In practical experiment, the coordinate of the diffraction plane may 
        differ from the convention of 4D-Explorer. For example, both typical 
        i-j indexing and x-y coordinates are right-handed system:

            ┌------------> j        ^y
            |                       |
            |                       |
            |                       |
            |                       |
            v                       |
            i                       └----------------> x


        However, in some conventions, the coordinate is left-handed:

            ┌------------> x       
            |                       
            |                      
            |                       
            |                       
            v                       
            y

        In this case, the calculated vector field's components should be 
        exchanged in order to reveal correct electromagnetic field.   
        """
        dialog_save = DialogSaveVectorField(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return 
        image_name = dialog_save.getNewName()
        image_parent_path = dialog_save.getParentPath()
        meta = self.data_object.attrs 

        self.task = TaskFlipVectorField(
            self.data_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)


    def _vectorPotential(self):
        """
        Calculate potential for the vector field.

        The vector field should be a non-curl field, otherwise the result is 
        invalid in physics.
        """
        dialog_save = DialogSaveImage(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return 
        image_name = dialog_save.getNewName()
        image_parent_path = dialog_save.getParentPath()
        meta = self.data_object.attrs 

        self.task = TaskPotential(
            self.data_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)

    def _vectorDivergence(self):
        """
        Calculate divergence for the vector field.
        """
        dialog_save = DialogSaveImage(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return 
        image_name = dialog_save.getNewName()
        image_parent_path = dialog_save.getParentPath()
        meta = self.data_object.attrs 

        self.task = TaskDivergence(
            self.data_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)

    def _vectorCurl(self):
        """
        Calculate curl for the vector field.
        """
        dialog_save = DialogSaveImage(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return 
        image_name = dialog_save.getNewName()
        image_parent_path = dialog_save.getParentPath()
        meta = self.data_object.attrs 

        self.task = TaskCurl(
            self.data_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)

    def _vectorSliceI(self):
        """
        Slice i-component for the vector field.
        """
        dialog_save = DialogSaveImage(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return 
        image_name = dialog_save.getNewName()
        image_parent_path = dialog_save.getParentPath()
        meta = self.data_object.attrs 

        self.task = TaskSliceI(
            self.data_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)

    def _vectorSliceJ(self):
        """
        Slice j-component for the vector field.
        """
        dialog_save = DialogSaveImage(self)
        dialog_save.setParentPath(self.data_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return 
        image_name = dialog_save.getNewName()
        image_parent_path = dialog_save.getParentPath()
        meta = self.data_object.attrs 

        self.task = TaskSliceJ(
            self.data_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)




class DialogAdjustQuiverEffect(QDialog):
    """
    用于调整矢量场箭头图的效果的对话框。

    Dialog to adjust quiver display effect.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogAdjustQuiverEffect.Ui_Dialog()
        self.ui.setupUi(self)
        self._item_path = None 
        self._colors = {
            'blue': 0,
            'cyan': 1,
            'green': 2,
            'black': 3,
            'magenta': 4,
            'red': 5,
            'white': 6,
            'yellow': 7,
        }
        self.ui.doubleSpinBox_scale.setMaximum(1e9)
        self.ui.doubleSpinBox_scale.setMinimum(0.01)
        self.ui.doubleSpinBox_scale.setValue(1)
        self.ui.doubleSpinBox_width.setMinimum(0.01)
        self.ui.doubleSpinBox_width.setValue(0.15)
        self.ui.comboBox_color.setCurrentIndex(3)

        self.ui.pushButton_cancel.clicked.connect(self.reject)
        self.ui.pushButton_ok.clicked.connect(self.accept)
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler

    @property 
    def data_object(self) -> h5py.Dataset:
        return self.hdf_handler.file[self._item_path]

    @property
    def data_scale(self) -> float:
        return self.data_object.attrs['quiver_scale']

    @property
    def data_width(self) -> float:
        return self.data_object.attrs['quiver_width']

    @property 
    def data_color(self) -> str:
        return self.data_object.attrs['quiver_color']

    def setVectorField(self, item_path: str):
        """
        arguments:
            item_path: (str) the vector field's path in hdf5 file.
        """
        self._item_path = item_path
         
        self.ui.doubleSpinBox_scale.setValue(self.data_scale)
        self.ui.doubleSpinBox_width.setValue(self.data_width)
        self.ui.comboBox_color.setCurrentIndex(
            self._colors[self.data_color]
        )

    def getScale(self) -> float:
        return self.ui.doubleSpinBox_scale.value()

    def getWidth(self) -> float:
        return self.ui.doubleSpinBox_width.value()

    def getColor(self) -> str:
        return self.ui.comboBox_color.currentText()

    
class DialogVectorProcessing(QDialog):
    """
    用于计算 Vector Field 相关操作的对话框。

    Dialog to calculate some processings for vector fields.
    """
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.ui = uiDialogVectorProcessing.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_rotate_vector_angle.clicked.connect(
            self._rotate_vector_angle
        )
        self.ui.pushButton_subtract_mean_vector.clicked.connect(
            self._subtract_mean_vector
        )
        self.ui.pushButton_flip.clicked.connect(
            self._flip
        )
        self.ui.pushButton_calculate_curl.clicked.connect(
            self._calculate_curl
        )
        self.ui.pushButton_calculate_divergence.clicked.connect(
            self._calculate_divergence
        )
        self.ui.pushButton_calculate_potential.clicked.connect(
            self._calculate_potential
        )
        self.ui.pushButton_vec_i.clicked.connect(
            self._slice_vec_i
        )
        self.ui.pushButton_vec_j.clicked.connect(
            self._slice_vec_j
        )

    def getResult(self):
        return self._result

    def _rotate_vector_angle(self):
        self._result = 'rotate'
        self.accept()

    def _subtract_mean_vector(self):
        self._result = 'subtract'
        self.accept()

    def _calculate_curl(self):
        self._result = 'curl'
        self.accept()

    def _calculate_divergence(self):
        self._result = 'divergence'
        self.accept()

    def _calculate_potential(self):
        self._result = 'potential'
        self.accept()

    def _slice_vec_i(self):
        self._result = 'vec_i'
        self.accept()

    def _slice_vec_j(self):
        self._result = 'vec_j'
        self.accept()

    def _flip(self):
        self._result = 'flip'
        self.accept()

# if 'quiver_scale' in self.data_object.attrs:
#             quiver_scale = self.data_object.attrs['quiver_scale']
#         else:
#             self.data_object.attrs['quiver_scale'] = 1
#             quiver_scale = 1
        
#         if 'quiver_width' in self.data_object.attrs:
#             quiver_width = self.data_object.attrs['quiver_width']
#         else:
#             self.data_object.attrs['quiver_width'] = 0.15
#             quiver_width = 0.15
        
#         if 'quiver_color' in self.data_object.attrs: