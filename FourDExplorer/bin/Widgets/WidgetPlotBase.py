# -*- coding: utf-8 -*-
"""
*---------------------------- WidgetPlotBase.py ------------------------------*
使用 matplotlib 进行绘制的部件基类。

作者:           胡一鸣
创建日期:       2022年3月26日

The GUI base widget to render data by matplotlib.

author:         Hu Yiming
date:           Mar 26, 2022
*---------------------------- WidgetPlotBase.py ------------------------------*
"""

# from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget, QVBoxLayout, QToolBar, QToolButton
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize, Qt
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT,
)
from matplotlib.figure import Figure
import numpy as np
from Constants import UIThemeMode


from bin.BlitManager import BlitManager
from bin.UIManager import ThemeHandler

class WidgetPlotBase(QWidget):
    """
    使用 matplotlib 进行绘制的部件基类。

    Base widget to plot items by matplotlib.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self._figure = Figure()
        self._canvas = FigureCanvas(self._figure)
        self._blit_manager = BlitManager(self._canvas)
        self._blit_manager.addArtist('_figure_patch', self._figure.patch)
        
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setContentsMargins(0,0,0,0,)
        self._navigation_actions = {}
        self._initActions()
        self._navigation_toolbar = self._buildNavigationToolBar()
        self.vertical_layout.addWidget(self._navigation_toolbar)
        self.vertical_layout.addWidget(self._canvas)
        self.setLayout(self.vertical_layout)

        self.theme_handler.theme_changed.connect(self._updateFigurePatch)

    @property
    def figure(self) -> Figure:
        return self._figure

    @property
    def canvas(self) -> FigureCanvas:
        return self._canvas

    @property
    def blit_manager(self) -> BlitManager:
        return self._blit_manager

    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp
        return qApp.theme_handler

    @property
    def navigation_actions(self) -> dict:
        return self._navigation_actions 

    def setToolbarVisible(self, visible: bool = True):
        """
        Set whether the navigation tool bar of matplotlib to hide.

        If this method is never called, the default state of the tool bar will
        be visible. 

        arguments:
            visible: (bool)
        """
        self._navigation_toolbar.setVisible(visible)

    _mpl_action_icons = {
        'home': 'home',
        'back': 'backward',
        'forward': 'forward',
        'pan': 'move',
        'zoom': 'search',
        'configure_subplots': 'layout',
        'edit_parameters': 'adjust',
        'save_figure': 'save',
    }

    def _initActions(self):
        """
        Initialize actions in the navigation toolbar.
        """
        self._mpl_toolbar = NavigationToolbar2QT(self.canvas, self)
        self._mpl_toolbar.setVisible(False)
        self._navigation_actions = self._mpl_toolbar._actions
        for key, action in self.navigation_actions.items():
            self._initActionIcon(action, self._mpl_action_icons[key])

    _action_icon_rc = ':/Navigation/resources/icons/'

    def _initActionIcon(self, action: QAction, rc_name: str):
        """
        Initialize icons for actions.
        """
        _path = self._action_icon_rc + rc_name 
        icon = self.theme_handler.iconProvider(_path)
        action.setIcon(icon)
        self.theme_handler.theme_changed.connect(
            lambda: action.setIcon(
                self.theme_handler.iconProvider(_path)
            )
        )

    def _buildNavigationToolBar(self) -> 'NavigationToolBar':
        """
        Build the navigation toolbar according to the actions.
        """
        tool_bar = NavigationToolBar(self)
        for action in self.navigation_actions.values():
            tool_bar.addAction(action)
        self.loc_label = self._mpl_toolbar.locLabel
        self._action_loc_label = tool_bar.addWidget(self.loc_label)
        self._action_loc_label.setVisible(True)
        return tool_bar 

    def addCustomizedAction(self, action: QAction, key: str = None):
        """
        Add the cutomized action.

        The widget must take the responsibility for update the action's icon
        whenever the theme is changed.

        arguments:
            action: (QAction) the customized action to be added.

            key: (str) in default it will be the text of the action.
        """
        if key is not None:
            self.navigation_actions[key] = action 
        else:
            self.navigation_actions[action.text()]
        self._navigation_toolbar.insertAction(self._action_loc_label, action)

    def addCustomizedToolButton(self, button: QToolButton):
        """
        Add the customized tool button.

        The tool button must take the responsibility for update the button's 
        icon whenever the theme is changed.

        arguments:
            button: (QToolButton) the customized toolbutton to be added.
        """
        self._navigation_toolbar.insertWidget(self._action_loc_label, button)


    _theme_mode_to_color = {
        UIThemeMode.Classical: 'white',
        UIThemeMode.Dark: 'black',
        UIThemeMode.Light: 'white',
    }

    def _updateFigurePatch(self):
        """
        Update the figure patch's color when the current theme changed.

        NOTE: I connot find a simple way to update all of the artists with current 
        rcParams in the figure. So this function is deprecated.
        """
        # self.figure.patch.set_color(
        #     self._theme_mode_to_color[
        #         self.theme_handler.theme_mode
        #     ]
        # )
        # self.blit_manager.update()
        pass 


class NavigationToolBar(QToolBar):
    """
    Customize navigation tool bar, based on matplotlib.
    """
    def __init__(self, parent: QWidget):
        """
        arguments:
            parent: (QWidget)

            canvas: (FigureCanvas) Must be the canvas which binds the actions.
        """
        super().__init__(parent)
        qss = self.theme_handler.getToolBarStyleSheet(self)
        self.setStyleSheet(qss)
        self.theme_handler.theme_changed.connect(self._update_style_sheet)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)

    def _update_style_sheet(self):
        """
        When theme is changed, the style sheet must be updated.
        """
        qss = self.theme_handler.getToolBarStyleSheet(self)
        self.setStyleSheet(qss)

    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler

