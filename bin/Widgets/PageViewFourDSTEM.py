# -*- coding: utf-8 -*-

"""
*-------------------------- PageViewFourDSTEM.py -----------------------------*
显示 4D-STEM 数据的页面。

部件内容：
    - WidgetPlotDP 用于使用 matplotlib 显示衍射图样
    - WidgetPlotPreview 用于使用 matplotlib 显示实空间预览图

提升部件：
    - 提升类名 PageViewFourDSTEM
    - 头文件 bin.Widgets.PageViewFourDSTEM

作者:           胡一鸣
创建日期:       2022年3月30日

The GUI page to view 4D-STEM dataset.

Contents:
    - WidgetPlotDP, to view the diffraction patterns by matplotlib
    - WidgetPlotPreview, to view the real-space preview image by matplotlib

Promoted Widget:
    - name of widget class: PageViewFourDSTEM
    - header file: bin.Widgets.PageViewFourDSTEM

author:         Hu Yiming
date:           Mar 30, 2022
*-------------------------- PageViewFourDSTEM.py -----------------------------*
"""

from PySide6.QtWidgets import QWidget, QMessageBox
from matplotlib.backend_bases import MouseEvent
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.image import AxesImage
from matplotlib.lines import Line2D

from bin.BlitManager import BlitManager
from bin.HDFManager import HDFDataNode
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.Widgets.PageBaseFourDSTEM import PageBaseFourDSTEM
from ui import uiPageViewFourDSTEM

class PageViewFourDSTEM(PageBaseFourDSTEM):
    """
    显示 4D-STEM 数据集的部件类。

    Ui 文件地址：ROOTPATH/ui/uiPageViewFourDSTEM

    Widget to show 4D-STEM dataset.

    The path of the ui file: ROOTPATH/ui/uiPageViewFourDSTEM

    attributes:
        hdf_handler: (HDFHandler) The handler to manage the hdf file and the 
            objects inside it.

        data_object: (h5py.Dataset) The data object of 4D-STEM data.

        data_path: (str) The path of the data object.

        preview_path: (str) The path of the previewing image in real space.

        logger: (Logger) Use logger to record information.

        dp_canvas: (FigureCanvas) The canvas (widget) object to show 
            Diffraction patterns.

        preview_canvas: (FigureCanvas) The canvas (widget) object to show
            preview images in the real space.

        dp_figure: (Figure) The Figure object of the diffraction patterns.

        preview_figure: (Figure) The Figure object of the preview images.

        dp_ax: (Axes) The Axes object of the diffraction patterns.

        preview_ax: (Axes) The Axes object of the preview images.

        colorbar_ax: (Axes) The Axes object of the colorbar.

        dp_object: (AxesImage) The image object of the diffraction patterns.

        preview_object: (AxesImage) The image object of the preview images.

        colorbar_object: (Colorbar) The Colorbar object. This colorbar is atta-
            ched to the diffraction patterns.

        preview_hcursor_object: (Line2D) The line object. This is a horizontal
            line in the preview image, indicating coordinates in the real space
            of the shown diffraction pattern.

        preview_vcursor_object: (Line2D) The line object. This is a vertical 
            line in the preview image, indicating coordinates in the real space
            of the shown diffraction pattern.

        dp_blit_manager: (BlitManager) The blit manager of the diffraction 
            patterns. When the data, norm, colormap or other attributes of the 
            diffraction pattern change, use its update() method to plot the 
            updated images.

        preview_blit_manager: (BlitManager) The blit manager of the preview 
            images. When the data, norm, colormap or other attributes of the
            preview images change, use its update() method to plot the updated
            images.

        scan_ii: (int) The i-coordinate of the current diffraction pattern in 
            the real space. This is also regarded as the row index in a matrix.

        scan_jj: (int) The j-coordinate of the current diffraction pattern in
            the real space. This is also regarded as the column index in a 
            matrix.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiPageViewFourDSTEM.Ui_Form()
        self.ui.setupUi(self)

        self._preview_path = ''
        self._preview_ax = None
        self._preview_object = None
        self._preview_hcursor_object = None
        self._preview_vcursor_object = None
        self._tracking = False

        self._initBaseUi()
        self._initUi()
        self._createAxes()
        self._createPreviewAxes()
        self._initTracking()

    @property
    def preview_path(self) -> str:
        return self._preview_path

    @property
    def preview_canvas(self) -> FigureCanvas:
        return self.ui.widget_preview.canvas

    @property
    def preview_figure(self) -> Figure:
        return self.ui.widget_preview.figure

    @property
    def preview_ax(self) -> Axes:
        return self._preview_ax

    @property
    def preview_object(self) -> AxesImage:
        return self._preview_object

    @property
    def preview_hcursor_object(self) -> Line2D:
        return self._preview_hcursor_object

    @property
    def preview_vcursor_object(self) -> Line2D:
        return self._preview_vcursor_object

    @property
    def preview_blit_manager(self) -> BlitManager:
        return self.ui.widget_preview.blit_manager

    def _initUi(self):
        """
        Initialize ui.
        """
        self.ui.pushButton_browse_preview.clicked.connect(
            self._browsePreview
        )

    def _initTracking(self):
        """
        Initialize tracking mouse location in the preview image.
        """
        self._cid_press = self.preview_canvas.mpl_connect(
            'button_press_event',       # When button pressed in preview, 
            self._startTrackingPreview  # start tracking the mouse location
        )                               # and update DP for the location
        self._cid_move = self.preview_canvas.mpl_connect(
            'motion_notify_event',      # update DP for the location
            self._updateDPByMouseMotion # NOTE: do NOT push mouse for a 
        )                               # long time!

        self._cid_release = self.preview_canvas.mpl_connect(
            'button_release_event',     # End tracking the mouse location
            self._endTrackingPreview    # when the button is released.
        )
        self._cid_leave = self.preview_canvas.mpl_connect(
            'axes_leave_event',         # End tracking the mouse location
            self._endTrackingPreview    # when the button leaves preview.
        )

    def setFourDSTEM(self, data_path: str):
        """
        Set the data path in HDF5 file, to show the diffraction patterns.

        Will set the data_path attribute. The FourDSTEM must be a 4D matrix.

        arguments:
            data_path: (str) the path of the 4D-STEM data.

        raises:
            TypeError, KeyError, ValueError
        """

        super(PageViewFourDSTEM, self).setFourDSTEM(data_path)
        
        if 'preview_path' in self.data_object.attrs:
            preview_path = self.data_object.attrs['preview_path']
            try:
                self.setPreview(preview_path)
            except (KeyError, ValueError, TypeError):
                new_preview_path = self._createNewPreview()
                self.setPreview(new_preview_path)
        else:
            new_preview_path = self._createNewPreview()
            self.setPreview(new_preview_path)
        data_node = self.hdf_handler.getNode(data_path)
        self.setWindowTitle('{0} - 4D-STEM'.format(data_node.name))

    def setPreview(self, preview_path: str):
        """
        Set the preview path in HDF5 file, to show the preview image.

        Will set the preview_path attribute. The preview image must be a 2D
        matrix, RGB images (3 channels) are not supported here.

        The preview image's shape must be equal to the first two dimensions of 
        the 4D-STEM dataset. For example, if the shape of 4D-STEM dataset is 
            256 x 256 x 128 x 128
        where there are 256 x 256 diffraction patterns (scanning points) and 
        every diffraction pattern has 128 x 128 pixels, the shape of preview 
        image must be 256 x 256, i.e. the scanning shape.

        arguments:
            preview_path: (str) the path of the image or data.

        raises:
            TypeError, KeyError, ValueError
        """
        if not isinstance(preview_path, str):
            raise TypeError('preview_path must be a str, not '
                '{0}'.format(type(preview_path).__name__))

        preview_node = self.hdf_handler.getNode(preview_path)
        # May raise KeyError if the path does not exist
        if not isinstance(preview_node, HDFDataNode):
            raise ValueError('Item {0} must be a Dataset'.format(preview_path))
        
        preview_data_obj = self.hdf_handler.file[preview_path]
        if not len(preview_data_obj.shape) == 2:
            raise ValueError('Data must be a 2D matrix (single channel image)')

        if self.data_path == '':
            raise ValueError('Must set 4D-STEM dataset before set previewing')
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape
        if (preview_data_obj.shape[0] != scan_i 
                or preview_data_obj.shape[1] != scan_j):
            raise ValueError('The preview image\'s shape must be equal to the'
                ' first two dimensions of the 4D-STEM dataset.')
        
        self._preview_path = preview_path
        self.ui.lineEdit_preview_path.setText(self.preview_path)
        self.data_object.attrs['preview_path'] = preview_path

        self._createPreviewImage()
        self._createPreviewCursor()

        self.preview_canvas.draw()
        self.preview_canvas.flush_events()
    
    def _createPreviewAxes(self):
        """
        Create the axes that contains previewing image.
        """
        if self._preview_ax is None:
            self._preview_ax = self.preview_figure.add_subplot()
            self.preview_blit_manager['preview_axes'] = self._preview_ax

    def _createPreviewImage(self):
        """
        Create the axes and image of the preview images.

        TODO: read and save attributes, like norm, cmap, alpha, etc.
        """
        if self._preview_object in self.dp_ax.images:
            # clear preview objects in the axes
            _index = self.dp_ax.images.index(self._preview_object)
            self.preview_ax.images.pop(_index)
        
        self._preview_object = self.preview_ax.imshow(
                self.hdf_handler.file[self.preview_path]
        )
        self.preview_blit_manager['preview_image'] = self._preview_object
        
        

    def _createPreviewCursor(self):
        """
        Create cursors on the preview image, to show where the current DP on 
        the real space is.
        """
        if self.preview_hcursor_object is None:
            self._preview_hcursor_object = self.preview_ax.axhline(
                y = self.scan_ii,
                color = 'black',
                linewidth = 1,
            )
            self.preview_blit_manager['preview_hcursor'] = (
                self.preview_hcursor_object)    # Here is not a tuple
        else:
            self.preview_hcursor_object.set_ydata(
                self.scan_ii
            )
            self.preview_blit_manager.update()

        if self.preview_vcursor_object is None:
            self._preview_vcursor_object = self.preview_ax.axvline(
                x = self.scan_jj,
                color = 'black',
                linewidth = 1,
            )
            self.preview_blit_manager['preview_vcursor'] = (
                self.preview_vcursor_object)    # Here is not a tuple
            
        else:
            self.preview_vcursor_object.set_xdata(
                self.scan_jj
            )
            self.preview_blit_manager.update()

        

    def _updateDP(self):
        """
        Update the current diffraction pattern according to the location in 
        the real space (in preview or in spinBoxes).
        """
        super(PageViewFourDSTEM, self)._updateDP()
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape
        scan_ii = max(0, min(scan_i, self.scan_ii)) # Avoid out of boundary
        scan_jj = max(0, min(scan_j, self.scan_jj))
        self.preview_hcursor_object.set_ydata(scan_ii)
        self.preview_vcursor_object.set_xdata(scan_jj)
        self.preview_blit_manager.update()

    def _updateDPByMouseMotion(self, event: MouseEvent):
        """
        Set the DP when the mouse is clicked on the preview.

        arguments:
            event: MouseEvent
        """
        if not self._tracking:
            return None
        if not event.ydata is None:
            self._scan_ii = int(event.ydata)
        if not event.xdata is None:
            self._scan_jj = int(event.xdata)

        self._updateDP()

    def _startTrackingPreview(self, event: MouseEvent):
        """
        Start the tracking preview when the mouse is clicked on the preview.

        arguments:
            event: (MouseEvent)
        """
        self._tracking = True
        self._updateDPByMouseMotion(event)

    def _endTrackingPreview(self, event: MouseEvent):
        """
        End the tracking preview when the mouse is released.

        arguments:
            event: (MouseEvent)
        """
        self._updateDPByMouseMotion(event)
        self._tracking = False 
        self.ui.spinBox_scan_ii.setValue(self.scan_ii)
        self.ui.spinBox_scan_jj.setValue(self.scan_jj)

    def _createNewPreview(self) -> str:
        """
        Create a new preview image.

        In default, it will be /.../[4D-STEM name]_preview.img . If there has
        been a preview at this path, try to use it. Otherwise, add an index and 
        try again: /.../[4D-STEM name]_preview_1.img . The new path will be 
        under the same group as the 4D-STEM dataset.

        I cannot find a quick way to calculate a new preview image for now, so 
        the preview image is set to be a zero matrix. Users can calculate a new
        preview image and reset it themselves.

        returns:
            (str) the path of the new preview.
        """
        
        data_node = self.hdf_handler.getNode(self.data_path)
        if '.' in data_node.name:
            name_array = data_node.name.split('.')
            name_array.pop()
            original_name = '.'.join(name_array)
        else:
            original_name = data_node.name

        preview_name = original_name + '_preview.img'
        _count = 0
        while preview_name in data_node.parent:
            _count += 1
            preview_name = original_name + '_preview_{0}.img'.format(_count)
        if data_node.parent.path == '/':
            preview_path = '/' + preview_name
        else:
            preview_path = data_node.parent.path + '/' + preview_name

        self.data_object.attrs['preview_path'] = preview_path
        scan_i, scan_j, dp_i, dp_j = self.data_object.shape

        _index = self.hdf_handler.model.indexFromPath(self.data_path)
        self.hdf_handler.model.insertData(
            parent = _index.parent(),
            name = preview_name,
            shape = (scan_i, scan_j),
            dtype = 'float32',
        )   
        
        return preview_path

    def _browsePreview(self):
        """
        Open a dialog to browse which preview to set to the current 4D-STEM.

        Will modify the attribute 'preview_path' of 4D-STEM data object to the
        chosen preview path.
        """
        dialog = DialogHDFChoose(self)
        dialog_code = dialog.exec()
        if dialog_code == dialog.Accepted:
            current_path = dialog.getCurrentPath()
        try:
            self.setPreview(current_path)
        except (KeyError, ValueError, TypeError,) as e:
            self.logger.error('{0}'.format(e), exc_info=True)
            msg = QMessageBox(parent = self)
            msg.setWindowTitle('Warning')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Cannot open this data: {0}'.format(e))
            msg.exec()
        # else:
        #     self.data_object.attrs['preview_path'] = current_path

    def _changeColormap(self, index: int):
        """
        Slots when current colormap is changed.

        Will change the diffraction pattern's AND the preview's colormaps.

        arguments:
            index: (int)    0       'viridis'
                            1       'plasma'
                            2       'gray'
                            3       'RdYlBu'
                            4       'twilight'
                            5       'hsv'
                            6       'jet'
                            7       'Others'
        """
        if index > 6:
            return None
        else:
            cmap = self.ui.comboBox_colormap.currentText()
            self.dp_object.set_cmap(cmap)
            self.colorbar_object.update_normal(self.dp_object)
            self.dp_blit_manager.update()
            
            self.preview_object.set_cmap(cmap)
            self.preview_blit_manager.update()
