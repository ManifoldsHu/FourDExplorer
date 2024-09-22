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


from typing import Iterator
import time 
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
        self._artists = {}
        
        # grab the background on every draw
        self._cid = self._canvas.mpl_connect('draw_event', self._onDraw)
        
        self._last_update_time = time.time()
        self._min_interval = 0.01
        self._is_updating = False 
        

    @property
    def canvas(self) -> FigureCanvas:
        return self._canvas 

    @property
    def figure(self) -> Figure:
        return self._canvas.figure

    def __getitem__(self, key: str) -> Artist:
        return self._artists[key]

    def __iter__(self) -> Iterator:
        return iter(self._artists)

    def __len__(self) -> int:
        return len(self._artists)

    def __str__(self) -> str:
        return '<BlitManager> canvas: {0}'.format(self.canvas)

    def __repr__(self) -> str:
        return self.__str__()

    def __setitem__(self, key: str, artist: Artist):
        """
        Add or change an artist.

        It is recommended to use artists' labels as keys.
        """
        if not isinstance(key, str):
            raise TypeError('key must be a str, not '
                '{0}'.format(type(key).__name__))
        if not isinstance(artist, Artist):
            raise TypeError('artist must be an Artist, not '
                '{0}'.format(type(artist).__name__))
        if not artist.figure is self.figure:
            raise RuntimeError('The artist must be in the figure associated '
                'with the canvas that this BlitManager is managing')
        artist.set_animated(True)
        self._artists[key] = artist

    def __contains__(self, _object: str | Artist) -> bool:
        """
        Test whether the artist is managed by this manager.

        arguments:
            artist: (Artist)
        """
        if isinstance(_object, str):
            return _object in self._artists.keys()
        elif isinstance(_object, Artist):
            return _object in self._artists.values()
        else:
            raise TypeError('_object must be a str or Artist, not '
                '{0}'.format(type(_object).__name__))

    def __delitem__(self, key: str):
        del self._artists[key]

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

    def addArtist(self, key: str, artist: Artist):
        """
        Add an artist to be managed.

        arguments:
            key: (str) The key of the artist. Recommended to use label.

            artist: (Artist) The artist to be added. It will be set to 
                animated to be safe. The artist must be in the figure
                associated with the canvas that this class is managing.
        """
        if key in self._artists:
            raise ValueError('There has been an artist with key '
                '{0}'.format(key))
        self[key] = artist
    
    def resetArtist(self, key: str, artist: Artist):
        """
        Reset an artist with key to be managed.

        arguments:
            key: (str) The key of the artist. Recommended to use label.

            artist: (Artist) The artist to be reset. It will be set to
                animated to be safe. The artist must be in the figure 
                associated with the canvas that this class is managing.
        """
        if not key in self._artists:
            raise KeyError('There is no artist with key '
                '{0}'.format(key))
        self[key] = artist

    def _drawAnimated(self):
        """
        Draw all of the animted artists.
        """
        for artist in self._artists.values():
            self.figure.draw_artist(artist)

    def update(self):
        """
        Update the screen with animated artists.
        """
        
        # if self._is_updating:
        #     return 
        # self._is_updating = True 
        current_time = time.time()
        if current_time - self._last_update_time < self._min_interval:
            return 
        self._last_update_time = current_time
        
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
        # self._is_updating = False 

    def keys(self):
        return self._artists.keys()

    def artists(self):
        return self._artists.values()

    def items(self):
        return self._artists.items()

        