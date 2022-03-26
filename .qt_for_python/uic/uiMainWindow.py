# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

from bin.Widgets.WidgetFile import WidgetFile
from bin.Widgets.WidgetLog import WidgetLog
from bin.Widgets.WidgetTask import WidgetTask

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1207, 849)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionImport_Data = QAction(MainWindow)
        self.actionImport_Data.setObjectName(u"actionImport_Data")
        self.actionExport_Data = QAction(MainWindow)
        self.actionExport_Data.setObjectName(u"actionExport_Data")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_2.setChildrenCollapsible(False)
        self.tabWidget_control = QTabWidget(self.splitter_2)
        self.tabWidget_control.setObjectName(u"tabWidget_control")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_control.sizePolicy().hasHeightForWidth())
        self.tabWidget_control.setSizePolicy(sizePolicy)
        self.tabWidget_control.setMinimumSize(QSize(384, 0))
        self.tabWidget_control.setAutoFillBackground(False)
        self.tabWidget_control.setTabPosition(QTabWidget.West)
        self.tabWidget_control.setElideMode(Qt.ElideLeft)
        self.tabWidget_control.setDocumentMode(False)
        self.tabWidget_control.setTabsClosable(False)
        self.tabWidget_control.setMovable(False)
        self.tabWidget_control.setTabBarAutoHide(False)
        self.tab_File = WidgetFile()
        self.tab_File.setObjectName(u"tab_File")
        self.tabWidget_control.addTab(self.tab_File, "")
        self.tab_Task = WidgetTask()
        self.tab_Task.setObjectName(u"tab_Task")
        self.tabWidget_control.addTab(self.tab_Task, "")
        self.tab_Calibration = QWidget()
        self.tab_Calibration.setObjectName(u"tab_Calibration")
        self.verticalLayout_29 = QVBoxLayout(self.tab_Calibration)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.scrollArea_3 = QScrollArea(self.tab_Calibration)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 319, 948))
        self.verticalLayout_28 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.tableView_parameters = QTableView(self.groupBox_4)
        self.tableView_parameters.setObjectName(u"tableView_parameters")
        self.tableView_parameters.setMinimumSize(QSize(0, 400))

        self.verticalLayout_22.addWidget(self.tableView_parameters)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_change_meta_manually = QPushButton(self.groupBox_4)
        self.pushButton_change_meta_manually.setObjectName(u"pushButton_change_meta_manually")

        self.horizontalLayout_9.addWidget(self.pushButton_change_meta_manually)

        self.pushButton_flush_meta = QPushButton(self.groupBox_4)
        self.pushButton_flush_meta.setObjectName(u"pushButton_flush_meta")

        self.horizontalLayout_9.addWidget(self.pushButton_flush_meta)


        self.verticalLayout_22.addLayout(self.horizontalLayout_9)


        self.verticalLayout_28.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_26.addWidget(self.label_12)

        self.lineEdit_background_in_hdf5 = QLineEdit(self.groupBox_6)
        self.lineEdit_background_in_hdf5.setObjectName(u"lineEdit_background_in_hdf5")

        self.verticalLayout_26.addWidget(self.lineEdit_background_in_hdf5)

        self.pushButton_4 = QPushButton(self.groupBox_6)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_26.addWidget(self.pushButton_4)


        self.verticalLayout_28.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_25.addWidget(self.label_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_24.addWidget(self.label_10)

        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_24.addWidget(self.label_11)


        self.horizontalLayout_8.addLayout(self.verticalLayout_24)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.lineEdit = QLineEdit(self.groupBox_5)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout_23.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_23.addWidget(self.lineEdit_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_23)


        self.verticalLayout_25.addLayout(self.horizontalLayout_8)

        self.pushButton_align_change_manually = QPushButton(self.groupBox_5)
        self.pushButton_align_change_manually.setObjectName(u"pushButton_align_change_manually")

        self.verticalLayout_25.addWidget(self.pushButton_align_change_manually)

        self.pushButton_align_visual = QPushButton(self.groupBox_5)
        self.pushButton_align_visual.setObjectName(u"pushButton_align_visual")

        self.verticalLayout_25.addWidget(self.pushButton_align_visual)


        self.verticalLayout_28.addWidget(self.groupBox_5)

        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_27.addWidget(self.label_13)

        self.lineEdit_rotation_angle = QLineEdit(self.groupBox_7)
        self.lineEdit_rotation_angle.setObjectName(u"lineEdit_rotation_angle")

        self.verticalLayout_27.addWidget(self.lineEdit_rotation_angle)

        self.pushButton_change_angle_manually = QPushButton(self.groupBox_7)
        self.pushButton_change_angle_manually.setObjectName(u"pushButton_change_angle_manually")

        self.verticalLayout_27.addWidget(self.pushButton_change_angle_manually)

        self.pushButton_angle_defocused = QPushButton(self.groupBox_7)
        self.pushButton_angle_defocused.setObjectName(u"pushButton_angle_defocused")

        self.verticalLayout_27.addWidget(self.pushButton_angle_defocused)

        self.pushButton_angle_DPC = QPushButton(self.groupBox_7)
        self.pushButton_angle_DPC.setObjectName(u"pushButton_angle_DPC")

        self.verticalLayout_27.addWidget(self.pushButton_angle_DPC)


        self.verticalLayout_28.addWidget(self.groupBox_7)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_29.addWidget(self.scrollArea_3)

        self.tabWidget_control.addTab(self.tab_Calibration, "")
        self.tab_Image = QWidget()
        self.tab_Image.setObjectName(u"tab_Image")
        self.tabWidget_control.addTab(self.tab_Image, "")
        self.splitter_2.addWidget(self.tabWidget_control)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setChildrenCollapsible(True)
        self.tabWidget_view = QTabWidget(self.splitter)
        self.tabWidget_view.setObjectName(u"tabWidget_view")
        self.tabWidget_view.setMinimumSize(QSize(800, 600))
        self.tabWidget_view.setTabPosition(QTabWidget.North)
        self.tabWidget_view.setTabShape(QTabWidget.Rounded)
        self.tabWidget_view.setElideMode(Qt.ElideLeft)
        self.tabWidget_view.setDocumentMode(False)
        self.tabWidget_view.setTabsClosable(True)
        self.tabWidget_view.setMovable(True)
        self.tabWidget_view.setTabBarAutoHide(False)
        self.splitter.addWidget(self.tabWidget_view)
        self.widget_log = WidgetLog(self.splitter)
        self.widget_log.setObjectName(u"widget_log")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_log.sizePolicy().hasHeightForWidth())
        self.widget_log.setSizePolicy(sizePolicy2)
        self.splitter.addWidget(self.widget_log)
        self.splitter_2.addWidget(self.splitter)

        self.verticalLayout.addWidget(self.splitter_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1207, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuTask = QMenu(self.menubar)
        self.menuTask.setObjectName(u"menuTask")
        self.menuCalibrate = QMenu(self.menubar)
        self.menuCalibrate.setObjectName(u"menuCalibrate")
        self.menuImage = QMenu(self.menubar)
        self.menuImage.setObjectName(u"menuImage")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTask.menuAction())
        self.menubar.addAction(self.menuCalibrate.menuAction())
        self.menubar.addAction(self.menuImage.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_Data)
        self.menuFile.addAction(self.actionExport_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        self.tabWidget_control.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionImport_Data.setText(QCoreApplication.translate("MainWindow", u"Import Data", None))
        self.actionExport_Data.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.tabWidget_control.setTabText(self.tabWidget_control.indexOf(self.tab_File), QCoreApplication.translate("MainWindow", u"File", None))
        self.tabWidget_control.setTabText(self.tabWidget_control.indexOf(self.tab_Task), QCoreApplication.translate("MainWindow", u"Task", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Experimental Parameters", None))
        self.pushButton_change_meta_manually.setText(QCoreApplication.translate("MainWindow", u"Change Value", None))
        self.pushButton_flush_meta.setText(QCoreApplication.translate("MainWindow", u"Flush", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Background Subtraction", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Background Pattern in HDF5 File", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Choose a Background Matrix...", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Diffraction Disk Alignment", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Moving Patterns to...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Right (in pixels):", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Down (in pixels):", None))
        self.pushButton_align_change_manually.setText(QCoreApplication.translate("MainWindow", u"Change Manually...", None))
        self.pushButton_align_visual.setText(QCoreApplication.translate("MainWindow", u"Alignment by Visual Method...", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Angular Offset Correction", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Rotation Angle (in degrees):", None))
        self.pushButton_change_angle_manually.setText(QCoreApplication.translate("MainWindow", u"Change Manually...", None))
        self.pushButton_angle_defocused.setText(QCoreApplication.translate("MainWindow", u"Correct by Defocused Reference...", None))
        self.pushButton_angle_DPC.setText(QCoreApplication.translate("MainWindow", u"Correct by DPC...", None))
        self.tabWidget_control.setTabText(self.tabWidget_control.indexOf(self.tab_Calibration), QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.tabWidget_control.setTabText(self.tabWidget_control.indexOf(self.tab_Image), QCoreApplication.translate("MainWindow", u"Image", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTask.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.menuCalibrate.setTitle(QCoreApplication.translate("MainWindow", u"Calibrate", None))
        self.menuImage.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

