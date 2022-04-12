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

from PySide6.QtWidgets import QWidget
from matplotlib.axes import Axes
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import numpy as np

from bin.Widgets.WidgetPlotBase import WidgetPlotBase


class WidgetPlotImage(WidgetPlotBase):
    """
    使用 matplotlib 显示 2D 图像的部件。

    Widget to show 2D images by matplotlib.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)



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
        self.setToolBarVisible(False)
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
        four times of the characteristic value:
            if we suppose the data's values distribute uniformly, the height of 
            each bar is set to be the caracteristic value, i.e.
            max y-limit =  4/(hist_x[-1] - hist_x[0])

        arguments:
            data: (np.ndarray or ArrayLike) recommended to be 2D matrix.
        """
        hist_y, hist_x = np.histogram(
            data, 
            bins = 100, 
            density = True,
        )   # hist_y is a list of histogram's height (length = bins), 
            # while hist_x is a list of pick point (length = bins + 1)
        
        bar_path = self._calculatePath(hist_x, hist_y)
        self.hist_patch.set_path(bar_path)
        self.axes.set_xlim(hist_x[0], hist_x[-1])

        if hist_x[-1] - hist_x[0] > 0:
            self.axes.set_ylim(0, min(
                np.max(hist_y),
                4 / (hist_x[-1] - hist_x[0]),
            ))
        else:
            self.axes.set_ylim(0, 4 / hist_x[-1])

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


class WidgetPlotPreview(WidgetPlotBase):
    """
    使用 matplotlib 在显示 4D-STEM 衍射图样时，显示样品实空间预览的部件。

    Widget to show 4D-STEM real-space preview by matplotlib.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setToolBarVisible(False)


    
