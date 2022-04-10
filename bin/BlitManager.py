# -*- coding: utf-8 -*-
"""
*------------------------------ BlitManager.py -------------------------------*
用于 Matplotlib 的位图传送，可以显著改善图像更新性能。

源代码参考:
https://matpolotlib.org/stable/tutorials/advanced/blitting.html

作者：          胡一鸣
创建时间：      2021年7月26日

Blitting is a standard technique in raster graphics that, in
the context of Matplotlib, can be used to drastically improve
performance of interactive figures.

Source ref:
https://matpolotlib.org/stable/tutorials/advanced/blitting.html

author:         Hu Yiming
date:           July 26, 2021

All rights reserved

*------------------------------ BlitManager.py -------------------------------*
"""


from PySide6.QtCore import QObject
from matplotlib.artist import Artist
from matplotlib.backend_bases import Event
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
)
from matplotlib.figure import Figure

class BlitManager(QObject):
    """
    Matplotlib 位图传送管理器。

    使用位图传送管理器可以高效刷新图像。在 4D-Explorer 中，各个画布都具有自己的 
    BlitManager，以此实现动态效果。

    Block transfer (Blit) manager of matplotlib.

    We can refresh the canvas by the blit manager. in 4D-Explorer, each canvas
    has its own BlitManager, and to realize dynamic effects.

    attributes:
        canvas: (FigureCanvas) the canvas managed by this object.

        figure: (Figure) the figure associated with the canvas managed by this
            BlitManager object.
    """
    def __init__(self, canvas: FigureCanvas, parent: QObject = None):
        """
        arguments:
            canvas: (FigureCanvas)

            parent: (QObject)
        """
        super().__init__(parent)
        self._background = None
        self._canvas = canvas
        self._artists = []
        
        # grab the background on every draw
        self._cid = self._canvas.mpl_connect('draw_event', self._onDraw)

    @property
    def canvas(self) -> FigureCanvas:
        return self._canvas 

    @property
    def figure(self) -> Figure:
        return self._canvas.figure

    def __contains__(self, artist: Artist) -> bool:
        """
        Test whether the artist is managed by this manager.

        arguments:
            artist: (Artist)
        """
        return artist in self._artists

    def _onDraw(self, event: Event):
        """
        The callback function to register with draw_event.

        arguments:
            event: (Event)
        """
        if not event is None:
            if not event.canvas is self.canvas:
                raise RuntimeError('The event must be of the same canvas '
                    'as the BlitManager.')
        self._background = self.canvas.copy_from_bbox(
            self.figure.bbox
        )
        self._drawAnimated()

    def addArtist(self, artist: Artist):
        """
        Add an artist to be managed.

        arguments:
            artist: (Artist) The artist to be added. It will be set to 
                animated to be safe. The artist must be in the figure
                associated with the canvas that this class is managing.
        """
        if not artist.figure is self.figure:
            raise RuntimeError('The artist must be in the figure associated '
                'with the canvas that this BlitManager is managing')

        artist.set_animated(True)
        self._artists.append(artist)

    def _drawAnimated(self):
        """
        Draw all of the animted artists.
        """
        for artist in self._artists:
            self.figure.draw_artist(artist)

    def update(self):
        """
        Update the screen with animated artists.
        """
        # paranoia in case we missed the draw event
        if self._background is None:
            self._onDraw(None)
        else:
            # restore the background
            self.canvas.restore_region(self._background)
            # draw all of the animated artists
            self._drawAnimated()
            self.canvas.blit(self.figure.bbox)
        # let the GUI event loop process anything it has to do.
        self.canvas.flush_events()

    

# class BlitManager(object):
#     '''
        

#     '''
#     def __init__(self, canvas, animated_artists = (), animated_collections = ()):
#         '''
#         Parameters:
#         ---------------
#         canvas : FigureCanvasAgg


#         animated_artists : Iterable[Artist]
#         List of the artists to manage
#         '''
#         self.canvas = canvas
#         self._bg = None
#         self._artists = []
#         self._collections = []


#         for artist in animated_artists:
#             self.add_artist(artist)

#         for collection in animated_collections:
#             self.add_collection(collection)

#         #为每次画图抓取背景
#         self.cid = canvas.mpl_connect('draw_event', self.on_draw)


#     def on_draw(self, event):
#         '''
#         回调，用于向 'draw_event' 登记
#         '''
#         cv = self.canvas
#         if event is not None:
#             if event.canvas != cv:
#                 raise RuntimeError
#         self._bg = cv.copy_from_bbox(cv.figure.bbox)
#         self._draw_animated()


#     def add_artist(self, art):
#         '''
#         添加一个需要处理的artist

#         Parameters
#         --------------
#         art : Artist

#         添加Artist，设置其为'animated'
#         *art*必须在与此画布关联的图中

#         '''
#         if art.figure != self.canvas.figure:
#             raise RuntimeError

#         art.set_animated(True)
#         self._artists.append(art)

#     def add_collection(self, collection):
#         '''
#         添加一个需要处理的collection

#         Parameters
#         ---------------
#         collection : instance of subclass of collections.Collection

#         添加collection，设置其为'animated'
#         其必须在与此画布关联的图中
#         '''

#         if collection.axes.figure != self.canvas.figure:
#             raise RuntimeError

#         collection.set_animated(True)
#         self._collections.append(collection)


#     def _draw_animated(self):
#         '''
#         画出所有可变的artists
#         '''
#         fig = self.canvas.figure
#         for a in self._artists:
#             fig.draw_artist(a)
        
#         for c in self._collections:
#             fig.draw_artist(c)

#     def update(self):
#         '''
#         更新屏幕
#         '''
#         cv = self.canvas
#         fig = cv.figure
#         if self._bg is None:
#             self.on_draw(None)
#         else:
#             #储存background
#             cv.restore_region(self._bg)
#             #画出所有动态artist
#             self._draw_animated()
#             #更新GUI状态
#             cv.blit(fig.bbox)

#         #继续GUI事件循环
#         cv.flush_events()

        