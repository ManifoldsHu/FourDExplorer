# -*- coding: utf-8 -*-

"""
*---------------------------- TabViewManager.py ------------------------------*
用于管理主窗口中标签页的模组。

标签页可以用来代替各种对话框，也可以用来作为子窗口显示各种自定义界面。目前预定义的标签
页功能有：
    - 欢迎 (主页)
    - 绘制图像
    - 各种 Calibrate 操作
    - 设置

作者：          胡一鸣
创建时间：      2022年3月27日

This module is used to manage tabviews in the MainWindow.

Tabs can be regarded as subwindows or dialogs. For now, we can use the tabs to
    - introduce (home page)
    - draw figures
    - do some calibrations
    - and modify settings.

author:         Hu Yiming
date:           Mar 27, 2021
*---------------------------- TabViewManager.py ------------------------------*
"""

from logging import Logger
from typing import List

from PySide6.QtWidgets import (
    QTabWidget, 
    QWidget, 
    QScrollArea,
    QVBoxLayout,
)
from PySide6.QtCore import QObject, Qt, Signal

from bin.Widgets.PageHome import PageHome

class TabViewManager(QObject):
    """
    标签页的管理器。

    Managers of tabs.
    """
    signal_tab_opened = Signal(str)
    signal_tab_closed = Signal(str)

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._tabWidget_view = None
        self._page_home = PageHome(self.parent())   # parent is MainWindow
        
        # DEPRECATED: keep tab widget objects in list will cause memory leak
        self._tab_history = []      
        self._tab_history_max = 0
        self.hdf_handler.file_about_to_close.connect(
            self.pageWaitForFileClose
        )


    @property
    def tabWidget_view(self) -> QTabWidget:
        return self._tabWidget_view

    @tabWidget_view.setter
    def tabWidget_view(self, tabview: QTabWidget):
        if not isinstance(tabview, QTabWidget):
            raise TypeError('tabview must be QTabWidget, not '
                '{0}'.format(type(tabview).__name__))
        self._tabWidget_view = tabview

    @property
    def page_home(self) -> PageHome:
        return self._page_home

    @property
    def tab_history(self) -> List[QWidget]: # DEPRECATED
        return self._tab_history

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    @property 
    def hdf_handler(self):
        global qApp 
        return qApp.hdf_handler

    def setTabWidget(self, tabview: QTabWidget):
        """
        Set the tabwidget that this manager to handle.

        arguments:
            tabview: (QTabWidget) should be MainWindow.ui.tabWidget_view
        """
        self.tabWidget_view = tabview

    def initializeTabView(self):
        """
        To initialize TabViews.
        """
        self.openTab(self.page_home)
        self.tabWidget_view.setTabsClosable(True)
        self.tabWidget_view.tabCloseRequested.connect(self.closeTab)
        
    def closeTab(self, tab_index: int):
        """
        Slots when the user requests to close a tab.

        Will automatically open the home page if there is no tabs remain.
        """
        tab = self.tabWidget_view.widget(tab_index)
        self.tabWidget_view.removeTab(tab_index)
        tab.close()
        self.signal_tab_closed.emit(tab.windowTitle())
        
        if tab is not self._page_home:
            tab.deleteLater()
            
        # If there is no tab opened, open home page automatically
        if self.tabWidget_view.count() == 0:
            self.openTab(self.page_home)
        

    def getTab(self, index: int):
        """
        Returns the tab page according to the index.

        NOTE: tabWidget.widget() will return a QScrollArea, rather than 
        the page itself, which is what we want.

        arguments:
            index: (int) the index of the page.

        returns:
            (QWidget)
        """
        scroll_area = self.tabWidget_view.widget(index)
        return scroll_area.page
        

    def openTab(self, page: QWidget):
        """
        Open a tab.

        Usually the tab should be a Page, but other widgets are not forbidden.

        Will automatically add put the page in a scroll area.
        
        arguments:
            page: (QWidget) the tab to be opened.
        """
        for ii in range(self.tabWidget_view.count()):
            if page is self.getTab(ii):
                raise RuntimeError('Tab has been opened.')
        
        # if not page is self._page_home:
        #     if len(self._tab_history) > self._tab_history_max:
        #         self._tab_history.pop(0)
        #     self._tab_history.append(page)

        scroll_area = self._encapsulatePageToScrollArea(page)
        scroll_area.setAttribute(Qt.WA_DeleteOnClose)
        new_tab_index = self.tabWidget_view.addTab(
            scroll_area,
            page.windowIcon(),
            page.windowTitle(),
        )
        
        self.tabWidget_view.setCurrentIndex(new_tab_index)
        self.signal_tab_opened.emit(page.windowTitle())
        self.logger.debug('Open a new page: {0}'.format(page.windowTitle()))


    def _encapsulatePageToScrollArea(self, page: QWidget) -> QScrollArea:
        """
        Encapsulate a page to a QScrollArea.

        Then if the page is too large, it can still full display.

        arguments:
            page: (QWidget)

        returns:
            (QScrollArea)
        """
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.scrollAreaWidgetContents = QWidget(scroll_area)
        scroll_area.setWidget(scroll_area.scrollAreaWidgetContents)
        scroll_area.verticalLayout = QVBoxLayout(
            scroll_area.scrollAreaWidgetContents
        )
        scroll_area.verticalLayout.addWidget(page)
        scroll_area.page = page 
        page.setParent(scroll_area.scrollAreaWidgetContents)
        return scroll_area

    def pageWaitForFileClose(self):
        """
        Ask user to close the pages before closing the file.
        """
        pass 
        


    