# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QWidget

from bin.Widgets.WidgetPlotBase import WidgetPlotBase


class WidgetPlotHist(WidgetPlotBase):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setToolBarVisible(False)