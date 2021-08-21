# -*- coding: utf-8 -*-
'''
*------------------- BlitManager.py --------------------------*
用于Matplotlib的位图传送，可以显著改善图像更新性能。

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

*------------------- BlitManager.py --------------------------*
'''

class BlitManager(object):
    '''
        

    '''
    def __init__(self, canvas, animated_artists = (), animated_collections = ()):
        '''
        Parameters:
        ---------------
        canvas : FigureCanvasAgg


        animated_artists : Iterable[Artist]
        List of the artists to manage
        '''
        self.canvas = canvas
        self._bg = None
        self._artists = []
        self._collections = []


        for artist in animated_artists:
            self.add_artist(artist)

        for collection in animated_collections:
            self.add_collection(collection)

        #为每次画图抓取背景
        self.cid = canvas.mpl_connect('draw_event', self.on_draw)


    def on_draw(self, event):
        '''
        回调，用于向 'draw_event' 登记
        '''
        cv = self.canvas
        if event is not None:
            if event.canvas != cv:
                raise RuntimeError
        self._bg = cv.copy_from_bbox(cv.figure.bbox)
        self._draw_animated()


    def add_artist(self, art):
        '''
        添加一个需要处理的artist

        Parameters
        --------------
        art : Artist

        添加Artist，设置其为'animated'
        *art*必须在与此画布关联的图中

        '''
        if art.figure != self.canvas.figure:
            raise RuntimeError

        art.set_animated(True)
        self._artists.append(art)

    def add_collection(self, collection):
        '''
        添加一个需要处理的collection

        Parameters
        ---------------
        collection : instance of subclass of collections.Collection

        添加collection，设置其为'animated'
        其必须在与此画布关联的图中
        '''

        if collection.axes.figure != self.canvas.figure:
            raise RuntimeError

        collection.set_animated(True)
        self._collections.append(collection)


    def _draw_animated(self):
        '''
        画出所有可变的artists
        '''
        fig = self.canvas.figure
        for a in self._artists:
            fig.draw_artist(a)
        
        for c in self._collections:
            fig.draw_artist(c)

    def update(self):
        '''
        更新屏幕
        '''
        cv = self.canvas
        fig = cv.figure
        if self._bg is None:
            self.on_draw(None)
        else:
            #储存background
            cv.restore_region(self._bg)
            #画出所有动态artist
            self._draw_animated()
            #更新GUI状态
            cv.blit(fig.bbox)

        #继续GUI事件循环
        cv.flush_events()

        