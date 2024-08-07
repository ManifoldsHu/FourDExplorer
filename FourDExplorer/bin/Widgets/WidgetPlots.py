"""
*------------------------------ WidgetPlots.py -------------------------------*
使用 matplotlib 进行绘制的部件类。

作者:           胡一鸣
创建日期:       2022年3月28日

The GUI widgets to render data by matplotlib.

author:         Hu Yiming
date:           Mar 28, 2022
*------------------------------ WidgetPlots.py -------------------------------*
"""

from PySide6.QtWidgets import QWidget, QToolButton, QMenu
from PySide6.QtGui import QAction
from matplotlib.axes import Axes
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.patches import Rectangle 
from matplotlib.text import Text 
import numpy as np

from bin.Widgets.WidgetPlotBase import WidgetPlotBase

class WidgetPlotImage(WidgetPlotBase):
    """
    使用 matplotlib 显示 2D 图像的部件。

    Widget to show 2D images by matplotlib.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self._initImageProcessingActions()
        self._initImageProcessingButton()
        self._initMeasureActions()
        self._initMeasureButton()
        
    @property
    def action_scale_bar(self):
        return self._action_scale_bar 

    def _initImageProcessingActions(self):
        """
        Initialize image processing actions (and its menu).
        """
        from bin.Actions.DataActions import ActionOpenImage
        self.menu_processing = QMenu(self)
        self._processing_actions: dict[str,QAction] = {
            'open': ActionOpenImage(self)
        }
        for action in self._processing_actions.values():
            self.menu_processing.addAction(action)
        
    def _initImageProcessingButton(self):
        """
        Will add a tool button (menu) in the toolbar.
        """
        self.toolButton_processing = QToolButton(self)
        self.toolButton_processing.setPopupMode(QToolButton.MenuButtonPopup)
        self.toolButton_processing_rc = ':/HDFItem/resources/icons/picture'
        self.toolButton_processing.setIcon(
            self.theme_handler.iconProvider(self.toolButton_processing_rc)
        )
        self.theme_handler.theme_changed.connect(
            lambda: self.toolButton_processing.setIcon(
                self.theme_handler.iconProvider(
                    self.toolButton_processing_rc
                )
            )
        )
        self.addCustomizedToolButton(self.toolButton_processing)
        self.toolButton_processing.setMenu(self.menu_processing)
        self.toolButton_processing.clicked.connect(
            lambda: self._processing_actions['open'].trigger()
        )
        self.toolButton_processing.setText(
            self._processing_actions['open'].text()
        )

    def setProcessingActionItemPath(self, item_path: str):
        """
        Will update the item path of the processing actions.

        This method should be called when the parent window change the its 
        current item path.

        arguments:
            item_path: (str) the item's path of the current 4D-STEM dataset.
        """
        for action in self._processing_actions.values():
            action.setItemPath(item_path)
            
    def _initMeasureActions(self):
        """
        Initialize the plot actions (and its menu).
        """
        from bin.Actions.PlotActions import ActionScaleBar
        self.menu_measure = QMenu(self)
        self._action_scale_bar = ActionScaleBar(self)
        self._measure_actions: dict[str, QAction] = {
            'scale_bar': self._action_scale_bar
        }
        for action in self._measure_actions.values():
            self.menu_measure.addAction(action)
        
        self._action_scale_bar.initialize(
            canvas = self.canvas,
            figure = self.figure,
            blit_manager = self.blit_manager,
        )
        
    def _initMeasureButton(self):
        """
        Will add a tool button (menu) in the toolbar that contains measuring 
        actions.
        """
        self.toolButton_measure = QToolButton(self)
        self.toolButton_measure.setPopupMode(QToolButton.MenuButtonPopup)
        self.toolButton_measur_rc = ':/Navigation/resources/icons/measure'
        self.toolButton_measure.setIcon(
            self.theme_handler.iconProvider(self.toolButton_measur_rc)
        )
        self.theme_handler.theme_changed.connect(
            lambda: self.toolButton_measure.setIcon(
                self.theme_handler.iconProvider(
                    self.toolButton_measur_rc 
                )
            )
        )
        self.addCustomizedToolButton(self.toolButton_measure)
        self.toolButton_measure.clicked.connect(
            lambda: self._measure_actions['scale_bar'].trigger()
        )
        self.toolButton_measure.setText(
            self._measure_actions['scale_bar'].text()
        )
        
    def setScaleBarActionUseMeta(
        self, 
        item_path: str,
        pixel_length_meta: str,
        unit_meta: str,
    ):
        """
        Will set the scale bar's default dataset and its metadata. It will 
        determine how long the scale bar should be.
        
        arguments:
            item_path: (str) The dataset's path, where the metadata should read 
                from
            
            pixel_length_meta: (str) The meta key that defines pixel length
            
            unit_meta: (str) The meta key that defines the unit of pixel length
        """
        from bin.Actions.PlotActions import ActionScaleBar
        action: ActionScaleBar = self._measure_actions['scale_bar']
        action.initialize(
            item_path = item_path, 
            pixel_length_meta = pixel_length_meta, 
            unit_meta = unit_meta
        )
        
    def setScaleBarRelatedArtists(
        self, 
        scale_bar: Rectangle = None, 
        scale_bar_text: Text = None
    ):
        """
        Will set the scale bar's artist for the scale bar action.
        
        arguments:
            scale_bar: (Rectangle)

            scale_bar_text: (Text)
        """
        from bin.Actions.PlotActions import ActionScaleBar
        action: ActionScaleBar = self._measure_actions['scale_bar']
        action.initialize(
            scale_bar = scale_bar,
            scale_bar_text = scale_bar_text,
        )
        
        
        
        
        

class WidgetPlotHist(WidgetPlotBase):
    """
    使用 matplotlib 显示 2D 图像的直方图的部件。

    使用 self.drawHist(data) 方法来更新直方图。

    Widget to show histograms of 2D images by matplotlib.

    Use self.drawHist(data) method to update the histogram.

    attributes:
        hist_patch: (PathPatch) the histogram path patch of the image.

        axes: (Axes) the Axes where histogram patch locates.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setToolbarVisible(False)
        self._initHist()

    @property
    def hist_patch(self) -> PathPatch:
        return self._hist_patch

    @property
    def axes(self) -> Axes:
        return self._hist_ax

    def _initHist(self):
        """
        Initialize histogram's axes and patches.
        """
        self._hist_ax = self.figure.add_subplot()
        self._hist_ax.set_axis_off()
        
        verts = [(0.,0.)]       # set a simplest path to be initialized
        codes = [Path.MOVETO]
        init_path = Path(verts, codes)
        init_patch = PathPatch(
            init_path, 
            facecolor = 'blue', 
            edgecolor = None, 
            alpha = 0.5, 
            linewidth = 0,
            animated = True,
        )
        self._hist_patch = self._hist_ax.add_patch(init_patch)
        self.blit_manager.addArtist('hist_patch', self._hist_patch)
        self.canvas.draw()
        self.canvas.flush_events()
    
    def _calculatePath(
        self, 
        hist_x: np.ndarray, 
        hist_y: np.ndarray,
    ) -> Path:
        """
        Calculate histogram's path according to data.

        code reference:
        https://matplotlib.org/stable/tutorials/advanced/path_tutorial.html

        arguments:
            hist_x: (np.ndarray) pick points of the bars on x-axis.

            hist_y: (np.ndarray) heights of the bars on y-axis. The length
                of hist_y list must be len(hist_x) + 1.

        returns:
            (Path)
        """

        left = np.array(hist_x[:-1])    # left edges of hist bars
        right = np.array(hist_x[1:])    # right edges of hist bars
        bottom = np.zeros(len(left))    # bottom edges of hist bars
        top = bottom + hist_y           # top edges of hist bars
        nrects = len(left)              # number of hist bars

        nverts = nrects*(1+3+1)         # number of points
        verts = np.zeros((nverts, 2)) 
        codes = np.ones(nverts, int) * Path.LINETO
        codes[0::5] = Path.MOVETO
        codes[4::5] = Path.CLOSEPOLY
        verts[0::5, 0] = left
        verts[0::5, 1] = bottom
        verts[1::5, 0] = left
        verts[1::5, 1] = top
        verts[2::5, 0] = right
        verts[2::5, 1] = top
        verts[3::5, 0] = right
        verts[3::5, 1] = bottom

        return Path(verts, codes)

    def drawHist(self, data: np.ndarray):
        """
        Draw a histogram of the data in this widget.

        The histogram is normalized to 1 (in numpy.histogram, density = True),
        so we should also modify the limits of the axes.

        In order to avoid some bar to be too high, we constrain y-limit to be
        ten times of the characteristic value:
            if we suppose the data's values distribute uniformly, the height of 
            each bar is set to be the caracteristic value, i.e.
            max y-limit =  10/(hist_x[-1] - hist_x[0])

        arguments:
            data: (np.ndarray or ArrayLike) recommended to be 2D matrix.
        """
        hist_y, hist_x = np.histogram(
            data, 
            bins = 500, 
            density = True,
        )   # hist_y is a list of histogram's height (length = bins), 
            # while hist_x is a list of pick point (length = bins + 1)
        
        bar_path = self._calculatePath(hist_x, hist_y)
        self.hist_patch.set_path(bar_path)
        self.axes.set_xlim(hist_x[0], hist_x[-1])

        if hist_x[-1] - hist_x[0] > 0:
            self.axes.set_ylim(0, min(
                np.max(hist_y),
                10 / (hist_x[-1] - hist_x[0]),
            ))
        else:
            self.axes.set_ylim(0, 10 / hist_x[-1])

        self.blit_manager.update()
        self.canvas.flush_events()

        
class WidgetPlotLine(WidgetPlotBase):
    """
    使用 matplotlib 显示 1D 曲线的部件。

    Widget to show 1D lines by matplotlib.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)


class WidgetPlotDP(WidgetPlotBase):
    """
    使用 matplotlib 显示 4D-STEM 衍射图样的部件。

    Widget to show 4D-STEM diffraction pattern by matplotlib.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self._initFourDSTEMProcessingActions()
        self._initFourDSTEMProcessingButton()
        self._initMeasureActions()
        self._initMeasureButton()
        
    @property
    def action_scale_bar(self):
        return self._action_scale_bar 

    def _initFourDSTEMProcessingButton(self):
        """
        Will add a tool button (menu) in the toolbar.
        """
        self.toolButton_processing = QToolButton(self)
        self.toolButton_processing.setPopupMode(QToolButton.MenuButtonPopup)
        self.toolButton_processing_rc = ':/HDFItem/resources/icons/cube'
        self.toolButton_processing.setIcon(
            self.theme_handler.iconProvider(self.toolButton_processing_rc)
        )
        self.theme_handler.theme_changed.connect(
            lambda: self.toolButton_processing.setIcon(
                self.theme_handler.iconProvider(
                    self.toolButton_processing_rc
                )
            )
        )
        self.addCustomizedToolButton(self.toolButton_processing)
        self.toolButton_processing.setMenu(self.menu_processing)
        self.toolButton_processing.clicked.connect(
            lambda: self._processing_actions['open'].trigger()
        )
        self.toolButton_processing.setText(
            self._processing_actions['open'].text()
        )

    def _initFourDSTEMProcessingActions(self):
        """
        Initialize the actions (menu) for 4D-STEM processing.
        """
        from bin.Actions.DataActions import ActionOpenFourDSTEM
        from bin.Actions.FourDSTEMActions import ActionAlign
        from bin.Actions.FourDSTEMActions import ActionBackground
        from bin.Actions.FourDSTEMActions import ActionCenterOfMass
        from bin.Actions.FourDSTEMActions import ActionRotate
        from bin.Actions.FourDSTEMActions import ActionVirtualImage
        from bin.Actions.FourDSTEMActions import ActionPlotCTF
        self.menu_processing = QMenu(self)
        self._processing_actions: dict[str,QAction] = {
            'open': ActionOpenFourDSTEM(self),
            'virtual_image': ActionVirtualImage(self),
            'center_of_mass': ActionCenterOfMass(self),
            'align': ActionAlign(self),
            'background': ActionBackground(self),
            'rotate': ActionRotate(self),
            'plot_ctf': ActionPlotCTF(self),
        }
        for action in self._processing_actions.values():
            self.menu_processing.addAction(action)
        self.menu_processing.insertSeparator(
            self._processing_actions['virtual_image']
        )
        self.menu_processing.insertSeparator(
            self._processing_actions['align']
        )
        self.menu_processing.insertSeparator(
            self._processing_actions['plot_ctf']
        )

    def setProcessingActionItemPath(self, item_path: str):
        """
        Will update the item path of the processing actions.

        This method should be called when the parent window change the its 
        current item path.

        arguments:
            item_path: (str) the item's path of the current 4D-STEM dataset.
        """
        for action in self._processing_actions.values():
            action.setItemPath(item_path)

            
    def _initMeasureActions(self):
        """
        Initialize the plot actions (and its menu).
        """
        from bin.Actions.PlotActions import ActionScaleBar
        self.menu_measure = QMenu(self)
        self._action_scale_bar = ActionScaleBar(self)
        self._measure_actions: dict[str, QAction] = {
            'scale_bar': self._action_scale_bar
        }
        for action in self._measure_actions.values():
            self.menu_measure.addAction(action)
        
        self._action_scale_bar.initialize(
            canvas = self.canvas,
            figure = self.figure,
            blit_manager = self.blit_manager,
        )
        
    def _initMeasureButton(self):
        """
        Will add a tool button (menu) in the toolbar that contains measuring 
        actions.
        """
        self.toolButton_measure = QToolButton(self)
        self.toolButton_measure.setPopupMode(QToolButton.MenuButtonPopup)
        self.toolButton_measur_rc = ':/Navigation/resources/icons/measure'
        self.toolButton_measure.setIcon(
            self.theme_handler.iconProvider(self.toolButton_measur_rc)
        )
        self.theme_handler.theme_changed.connect(
            lambda: self.toolButton_measure.setIcon(
                self.theme_handler.iconProvider(
                    self.toolButton_measur_rc 
                )
            )
        )
        self.addCustomizedToolButton(self.toolButton_measure)
        self.toolButton_measure.clicked.connect(
            lambda: self._measure_actions['scale_bar'].trigger()
        )
        self.toolButton_measure.setText(
            self._measure_actions['scale_bar'].text()
        )
        
    def setScaleBarActionUseMeta(
        self, 
        item_path: str = None,
        pixel_length_meta: str = None,
        unit_meta: str = None,
    ):
        """
        Will set the scale bar's default dataset and its metadata. It will 
        determine how long the scale bar should be.
        
        arguments:
            item_path: (str) The dataset's path, where the metadata should read 
                from
            
            pixel_length_meta: (str) The meta key that defines pixel length
            
            unit_meta: (str) The meta key that defines the unit of pixel length
        """
        from bin.Actions.PlotActions import ActionScaleBar
        action: ActionScaleBar = self._measure_actions['scale_bar']
        action.initialize(
            item_path = item_path, 
            pixel_length_meta = pixel_length_meta, 
            unit_meta = unit_meta
        )
        
    def setScaleBarRelatedArtists(
        self, 
        scale_bar: Rectangle = None, 
        scale_bar_text: Text = None
    ):
        """
        Will set the scale bar's artist for the scale bar action.
        
        arguments:
            scale_bar: (Rectangle)

            scale_bar_text: (Text)
        """
        from bin.Actions.PlotActions import ActionScaleBar
        action: ActionScaleBar = self._measure_actions['scale_bar']
        action.initialize(
            scale_bar = scale_bar,
            scale_bar_text = scale_bar_text,
        )
        


class WidgetPlotPreview(WidgetPlotBase):
    """
    使用 matplotlib 在显示 4D-STEM 衍射图样时，显示样品实空间预览的部件。

    Widget to show 4D-STEM real-space preview by matplotlib.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setToolbarVisible(False)

class WidgetPlotBackground(WidgetPlotBase):
    """
    使用 matplotlib 在显示矢量场时，显示背景图的部件。

    Widget to show the background image when opening a vector field.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setToolbarVisible(False)

class WidgetPlotQuiver(WidgetPlotBase):
    """
    使用 matplotlib 显示矢量场 (Quiver) 的部件。

    Widget to show the vector fields by matplotlib.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self._initVectorFieldProcessingActions()
        self._initVectorFieldProcessingButton()
        self._initMeasureActions()
        self._initMeasureButton()

        
    @property
    def action_scale_bar(self):
        return self._action_scale_bar 

    def _initVectorFieldProcessingButton(self):
        """
        Will add a tool button (menu) in the toolbar.
        """
        self.toolButton_processing = QToolButton(self)
        self.toolButton_processing.setPopupMode(QToolButton.MenuButtonPopup)
        self.toolButton_processing_rc = (
            ':/HDFItem/resources/icons/particle_tracking')
        self.toolButton_processing.setIcon(
            self.theme_handler.iconProvider(self.toolButton_processing_rc)
        )
        self.theme_handler.theme_changed.connect(
            lambda: self.toolButton_processing.setIcon(
                self.theme_handler.iconProvider(
                    self.toolButton_processing_rc
                )
            )
        )
        self.addCustomizedToolButton(self.toolButton_processing)
        self.toolButton_processing.setMenu(self.menu_processing)
        self.toolButton_processing.clicked.connect(
            lambda: self._processing_actions['open'].trigger()
        )
        self.toolButton_processing.setText(
            self._processing_actions['open'].text()
        )

    def _initVectorFieldProcessingActions(self):
        """
        Initialize the actions (menu) for vector field processing.
        """
        from bin.Actions.DataActions import ActionOpenVectorField
        from bin.Actions.VectorFieldActions import ActionSubtractMeanVector
        from bin.Actions.VectorFieldActions import ActionSubtractReferenceVector
        from bin.Actions.VectorFieldActions import ActionRotateVector
        from bin.Actions.VectorFieldActions import ActionFlipComponents
        from bin.Actions.VectorFieldActions import ActionPotential
        from bin.Actions.VectorFieldActions import ActionDivergence
        from bin.Actions.VectorFieldActions import ActionCurl
        from bin.Actions.VectorFieldActions import ActionSliceI
        from bin.Actions.VectorFieldActions import ActionSliceJ
        self.menu_processing = QMenu(self)
        self._processing_actions: dict[str,QAction] = {
            'open': ActionOpenVectorField(self),
            'subtract_offset': ActionSubtractMeanVector(self),
            'subtract_reference': ActionSubtractReferenceVector(self),
            'rotate': ActionRotateVector(self),
            'flip': ActionFlipComponents(self),
            'potential': ActionPotential(self),
            'divergence': ActionDivergence(self),
            'curl': ActionCurl(self),
            'slice_i': ActionSliceI(self),
            'slice_j': ActionSliceJ(self),
        }
        for action in self._processing_actions.values():
            self.menu_processing.addAction(action)
        self.menu_processing.insertSeparator(
            self._processing_actions['subtract_offset']
        )
        self.menu_processing.insertSeparator(
            self._processing_actions['potential']
        )

    def setProcessingActionItemPath(self, item_path: str):
        """
        Will update the item path of the processing actions.

        This method should be called when the parent window change the its 
        current item path.

        arguments:
            item_path: (str) the item's path of the current 4D-STEM dataset.
        """
        for action in self._processing_actions.values():
            action.setItemPath(item_path)
            
            
    def _initMeasureActions(self):
        """
        Initialize the plot actions (and its menu).
        """
        from bin.Actions.PlotActions import ActionScaleBar
        self.menu_measure = QMenu(self)
        self._action_scale_bar = ActionScaleBar(self)
        self._measure_actions: dict[str, QAction] = {
            'scale_bar': self._action_scale_bar
        }
        for action in self._measure_actions.values():
            self.menu_measure.addAction(action)
        
        self._action_scale_bar.initialize(
            canvas = self.canvas,
            figure = self.figure,
            blit_manager = self.blit_manager,
        )
        
    def _initMeasureButton(self):
        """
        Will add a tool button (menu) in the toolbar that contains measuring 
        actions.
        """
        self.toolButton_measure = QToolButton(self)
        self.toolButton_measure.setPopupMode(QToolButton.MenuButtonPopup)
        self.toolButton_measur_rc = ':/Navigation/resources/icons/measure'
        self.toolButton_measure.setIcon(
            self.theme_handler.iconProvider(self.toolButton_measur_rc)
        )
        self.theme_handler.theme_changed.connect(
            lambda: self.toolButton_measure.setIcon(
                self.theme_handler.iconProvider(
                    self.toolButton_measur_rc 
                )
            )
        )
        self.addCustomizedToolButton(self.toolButton_measure)
        self.toolButton_measure.clicked.connect(
            lambda: self._measure_actions['scale_bar'].trigger()
        )
        self.toolButton_measure.setText(
            self._measure_actions['scale_bar'].text()
        )
        
    def setScaleBarActionUseMeta(
        self, 
        item_path: str = None,
        pixel_length_meta: str = None,
        unit_meta: str = None,
    ):
        """
        Will set the scale bar's default dataset and its metadata. It will 
        determine how long the scale bar should be.
        
        arguments:
            item_path: (str) The dataset's path, where the metadata should read 
                from
            
            pixel_length_meta: (str) The meta key that defines pixel length
            
            unit_meta: (str) The meta key that defines the unit of pixel length
        """
        from bin.Actions.PlotActions import ActionScaleBar
        action: ActionScaleBar = self._measure_actions['scale_bar']
        action.initialize(
            item_path = item_path, 
            pixel_length_meta = pixel_length_meta, 
            unit_meta = unit_meta
        )
        
    def setScaleBarRelatedArtists(
        self, 
        scale_bar: Rectangle = None, 
        scale_bar_text: Text = None
    ):
        """
        Will set the scale bar's artist for the scale bar action.
        
        arguments:
            scale_bar: (Rectangle)

            scale_bar_text: (Text)
        """
        from bin.Actions.PlotActions import ActionScaleBar
        action: ActionScaleBar = self._measure_actions['scale_bar']
        action.initialize(
            scale_bar = scale_bar,
            scale_bar_text = scale_bar_text,
        )
        