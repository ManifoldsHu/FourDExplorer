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
    QLabel, QLineEdit, QListView, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

from bin.Widgets.WidgetFile import WidgetFile

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1009, 849)
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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(384, 0))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_File = WidgetFile()
        self.tab_File.setObjectName(u"tab_File")
        self.tabWidget.addTab(self.tab_File, "")
        self.tab_Task = QWidget()
        self.tab_Task.setObjectName(u"tab_Task")
        self.verticalLayout_13 = QVBoxLayout(self.tab_Task)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea_2 = QScrollArea(self.tab_Task)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 341, 767))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox_current_task = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_current_task.setObjectName(u"groupBox_current_task")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_current_task)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_current_task)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.label_task_name = QLabel(self.groupBox_current_task)
        self.label_task_name.setObjectName(u"label_task_name")

        self.horizontalLayout_2.addWidget(self.label_task_name)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_task_executing = QLabel(self.groupBox_current_task)
        self.label_task_executing.setObjectName(u"label_task_executing")

        self.verticalLayout_2.addWidget(self.label_task_executing)

        self.progressBar = QProgressBar(self.groupBox_current_task)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.listView_task_queue = QListView(self.groupBox_current_task)
        self.listView_task_queue.setObjectName(u"listView_task_queue")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listView_task_queue.sizePolicy().hasHeightForWidth())
        self.listView_task_queue.setSizePolicy(sizePolicy1)
        self.listView_task_queue.setMinimumSize(QSize(0, 0))

        self.verticalLayout_2.addWidget(self.listView_task_queue)

        self.pushButton_next_task = QPushButton(self.groupBox_current_task)
        self.pushButton_next_task.setObjectName(u"pushButton_next_task")

        self.verticalLayout_2.addWidget(self.pushButton_next_task)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_14.addWidget(self.groupBox_current_task)

        self.groupBox_system_info = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_system_info.setObjectName(u"groupBox_system_info")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_system_info)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.groupBox_system_info)
        self.label.setObjectName(u"label")

        self.verticalLayout_8.addWidget(self.label)

        self.label_3 = QLabel(self.groupBox_system_info)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_8.addWidget(self.label_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_cpu_count = QLabel(self.groupBox_system_info)
        self.label_cpu_count.setObjectName(u"label_cpu_count")

        self.verticalLayout_5.addWidget(self.label_cpu_count)

        self.label_cpu_percent = QLabel(self.groupBox_system_info)
        self.label_cpu_percent.setObjectName(u"label_cpu_percent")

        self.verticalLayout_5.addWidget(self.label_cpu_percent)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)

        self.progressBar_cpu_percent = QProgressBar(self.groupBox_system_info)
        self.progressBar_cpu_percent.setObjectName(u"progressBar_cpu_percent")
        self.progressBar_cpu_percent.setValue(24)

        self.verticalLayout_11.addWidget(self.progressBar_cpu_percent)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.groupBox_system_info)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_9.addWidget(self.label_4)

        self.label_5 = QLabel(self.groupBox_system_info)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_memory_total = QLabel(self.groupBox_system_info)
        self.label_memory_total.setObjectName(u"label_memory_total")

        self.verticalLayout_6.addWidget(self.label_memory_total)

        self.label_memory_available = QLabel(self.groupBox_system_info)
        self.label_memory_available.setObjectName(u"label_memory_available")

        self.verticalLayout_6.addWidget(self.label_memory_available)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.progressBar_memory_percent = QProgressBar(self.groupBox_system_info)
        self.progressBar_memory_percent.setObjectName(u"progressBar_memory_percent")
        self.progressBar_memory_percent.setValue(24)

        self.verticalLayout_11.addWidget(self.progressBar_memory_percent)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_14 = QLabel(self.groupBox_system_info)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_10.addWidget(self.label_14)

        self.label_6 = QLabel(self.groupBox_system_info)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.label_7 = QLabel(self.groupBox_system_info)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_10.addWidget(self.label_7)


        self.horizontalLayout_5.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_disk_partition = QLabel(self.groupBox_system_info)
        self.label_disk_partition.setObjectName(u"label_disk_partition")

        self.verticalLayout_7.addWidget(self.label_disk_partition)

        self.label_disk_total = QLabel(self.groupBox_system_info)
        self.label_disk_total.setObjectName(u"label_disk_total")

        self.verticalLayout_7.addWidget(self.label_disk_total)

        self.label_disk_available = QLabel(self.groupBox_system_info)
        self.label_disk_available.setObjectName(u"label_disk_available")

        self.verticalLayout_7.addWidget(self.label_disk_available)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.progressBar_disk_percent = QProgressBar(self.groupBox_system_info)
        self.progressBar_disk_percent.setObjectName(u"progressBar_disk_percent")
        self.progressBar_disk_percent.setValue(24)

        self.verticalLayout_11.addWidget(self.progressBar_disk_percent)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.groupBox_system_info)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_process_io = QLabel(self.groupBox_system_info)
        self.label_process_io.setObjectName(u"label_process_io")

        self.horizontalLayout_6.addWidget(self.label_process_io)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.verticalLayout_11.setStretch(0, 2)
        self.verticalLayout_11.setStretch(1, 1)
        self.verticalLayout_11.setStretch(2, 1)
        self.verticalLayout_11.setStretch(3, 2)
        self.verticalLayout_11.setStretch(4, 1)
        self.verticalLayout_11.setStretch(5, 1)
        self.verticalLayout_11.setStretch(6, 3)
        self.verticalLayout_11.setStretch(7, 1)
        self.verticalLayout_11.setStretch(8, 1)

        self.verticalLayout_12.addLayout(self.verticalLayout_11)


        self.verticalLayout_14.addWidget(self.groupBox_system_info)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_13.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab_Task, "")
        self.tab_Calibration = QWidget()
        self.tab_Calibration.setObjectName(u"tab_Calibration")
        self.verticalLayout_29 = QVBoxLayout(self.tab_Calibration)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.scrollArea_3 = QScrollArea(self.tab_Calibration)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 324, 944))
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)

        self.verticalLayout_23.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)

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

        self.tabWidget.addTab(self.tab_Calibration, "")
        self.tab_Image = QWidget()
        self.tab_Image.setObjectName(u"tab_Image")
        self.tabWidget.addTab(self.tab_Image, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1009, 22))
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

        self.tabWidget.setCurrentIndex(0)


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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_File), QCoreApplication.translate("MainWindow", u"File", None))
        self.groupBox_current_task.setTitle(QCoreApplication.translate("MainWindow", u"Current Task", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Task Name", None))
        self.label_task_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_task_executing.setText(QCoreApplication.translate("MainWindow", u"A task is executing", None))
        self.pushButton_next_task.setText(QCoreApplication.translate("MainWindow", u"Execute Task", None))
        self.groupBox_system_info.setTitle(QCoreApplication.translate("MainWindow", u"System Info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CPU count", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPU percent", None))
        self.label_cpu_count.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_cpu_percent.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Memory Total", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Memory Available", None))
        self.label_memory_total.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_memory_available.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Disk Partition", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Disk Total", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Disk Available", None))
        self.label_disk_partition.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_disk_total.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_disk_available.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Process IO", None))
        self.label_process_io.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Task), QCoreApplication.translate("MainWindow", u"Task", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Calibration), QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Image), QCoreApplication.translate("MainWindow", u"Image", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTask.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.menuCalibrate.setTitle(QCoreApplication.translate("MainWindow", u"Calibrate", None))
        self.menuImage.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

