# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QSplitter,
    QStackedWidget,
    QStatusBar,
    QTabWidget,
    QWidget,
)

from bin.Widgets.WidgetEMServer import WidgetEMServer
from bin.Widgets.WidgetFile import WidgetFile
from bin.Widgets.WidgetLog import WidgetLog
from bin.Widgets.WidgetPages import WidgetPages
from bin.Widgets.WidgetSystemInfo import WidgetSystemInfo
from bin.Widgets.WidgetTaskManager import WidgetTaskManager


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.actionNew_HDF5 = QAction(MainWindow)
        self.actionNew_HDF5.setObjectName("actionNew_HDF5")
        self.actionOpen_HDF5 = QAction(MainWindow)
        self.actionOpen_HDF5.setObjectName("actionOpen_HDF5")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, 9)
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_2.setChildrenCollapsible(False)
        self.stackedWidget_control = QStackedWidget(self.splitter_2)
        self.stackedWidget_control.setObjectName("stackedWidget_control")
        self.stackedWidget_control.setLineWidth(1)
        self.tab_file = WidgetFile()
        self.tab_file.setObjectName("tab_file")
        self.stackedWidget_control.addWidget(self.tab_file)
        self.tab_pages = WidgetPages()
        self.tab_pages.setObjectName("tab_pages")
        self.stackedWidget_control.addWidget(self.tab_pages)
        self.tab_task = WidgetTaskManager()
        self.tab_task.setObjectName("tab_task")
        self.stackedWidget_control.addWidget(self.tab_task)
        self.tab_system_info = WidgetSystemInfo()
        self.tab_system_info.setObjectName("tab_system_info")
        self.stackedWidget_control.addWidget(self.tab_system_info)
        self.tab_server = WidgetEMServer()
        self.tab_server.setObjectName("tab_server")
        self.stackedWidget_control.addWidget(self.tab_server)
        self.splitter_2.addWidget(self.stackedWidget_control)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.tabWidget_view = QTabWidget(self.splitter)
        self.tabWidget_view.setObjectName("tabWidget_view")
        self.splitter.addWidget(self.tabWidget_view)
        self.widget_log = WidgetLog(self.splitter)
        self.widget_log.setObjectName("widget_log")
        self.splitter.addWidget(self.widget_log)
        self.splitter_2.addWidget(self.splitter)

        self.horizontalLayout.addWidget(self.splitter_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile_F = QMenu(self.menubar)
        self.menuFile_F.setObjectName("menuFile_F")
        self.menuEdit_E = QMenu(self.menubar)
        self.menuEdit_E.setObjectName("menuEdit_E")
        self.menuView_V = QMenu(self.menubar)
        self.menuView_V.setObjectName("menuView_V")
        self.menuDataset_D = QMenu(self.menubar)
        self.menuDataset_D.setObjectName("menuDataset_D")
        self.menuSettings_S = QMenu(self.menubar)
        self.menuSettings_S.setObjectName("menuSettings_S")
        self.menuHelp_H = QMenu(self.menubar)
        self.menuHelp_H.setObjectName("menuHelp_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile_F.menuAction())
        self.menubar.addAction(self.menuEdit_E.menuAction())
        self.menubar.addAction(self.menuView_V.menuAction())
        self.menubar.addAction(self.menuDataset_D.menuAction())
        self.menubar.addAction(self.menuSettings_S.menuAction())
        self.menubar.addAction(self.menuHelp_H.menuAction())

        self.retranslateUi(MainWindow)

        self.stackedWidget_control.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.actionNew_HDF5.setText(
            QCoreApplication.translate("MainWindow", "New HDF5...", None)
        )
        self.actionOpen_HDF5.setText(
            QCoreApplication.translate("MainWindow", "Open HDF5...", None)
        )
        self.menuFile_F.setTitle(
            QCoreApplication.translate("MainWindow", "File(&F)", None)
        )
        self.menuEdit_E.setTitle(
            QCoreApplication.translate("MainWindow", "Edit(&E)", None)
        )
        self.menuView_V.setTitle(
            QCoreApplication.translate("MainWindow", "View(&V)", None)
        )
        self.menuDataset_D.setTitle(
            QCoreApplication.translate("MainWindow", "Dataset(&D)", None)
        )
        self.menuSettings_S.setTitle(
            QCoreApplication.translate("MainWindow", "Settings(&S)", None)
        )
        self.menuHelp_H.setTitle(
            QCoreApplication.translate("MainWindow", "Help(&H)", None)
        )

    # retranslateUi
