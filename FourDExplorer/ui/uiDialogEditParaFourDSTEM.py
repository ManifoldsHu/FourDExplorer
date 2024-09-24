# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogEditParaFourDSTEM.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(536, 734)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(18, -1, 18, -1)
        self.label_71 = QLabel(Dialog)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_56.addWidget(self.label_71)

        self.lineEdit_dataset_path = QLineEdit(Dialog)
        self.lineEdit_dataset_path.setObjectName(u"lineEdit_dataset_path")

        self.horizontalLayout_56.addWidget(self.lineEdit_dataset_path)

        self.pushButton_browse = QPushButton(Dialog)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout_56.addWidget(self.pushButton_browse)


        self.verticalLayout_4.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(18, -1, 18, -1)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.label_steps = QLabel(Dialog)
        self.label_steps.setObjectName(u"label_steps")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_steps.sizePolicy().hasHeightForWidth())
        self.label_steps.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_steps)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 516, 626))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_back = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.horizontalLayout_2.addWidget(self.pushButton_back)

        self.pushButton_next = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_next.setObjectName(u"pushButton_next")

        self.horizontalLayout_2.addWidget(self.pushButton_next)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_general = QWidget()
        self.page_general.setObjectName(u"page_general")
        self.verticalLayout_3 = QVBoxLayout(self.page_general)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.groupBox_2 = QGroupBox(self.page_general)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_dataset_title = QLineEdit(self.groupBox_2)
        self.lineEdit_dataset_title.setObjectName(u"lineEdit_dataset_title")

        self.horizontalLayout.addWidget(self.lineEdit_dataset_title)

        self.pushButton_edit_dataset_title = QPushButton(self.groupBox_2)
        self.pushButton_edit_dataset_title.setObjectName(u"pushButton_edit_dataset_title")

        self.horizontalLayout.addWidget(self.pushButton_edit_dataset_title)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.pushButton_edit_authors = QPushButton(self.groupBox_2)
        self.pushButton_edit_authors.setObjectName(u"pushButton_edit_authors")

        self.horizontalLayout_5.addWidget(self.pushButton_edit_authors)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.plainTextEdit_authors = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_authors.setObjectName(u"plainTextEdit_authors")

        self.verticalLayout_2.addWidget(self.plainTextEdit_authors)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.pushButton_edit_notes = QPushButton(self.groupBox_2)
        self.pushButton_edit_notes.setObjectName(u"pushButton_edit_notes")

        self.horizontalLayout_6.addWidget(self.pushButton_edit_notes)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.plainTextEdit_notes = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_notes.setObjectName(u"plainTextEdit_notes")

        self.verticalLayout_2.addWidget(self.plainTextEdit_notes)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_general)
        self.page_microscope = QWidget()
        self.page_microscope.setObjectName(u"page_microscope")
        self.verticalLayout_9 = QVBoxLayout(self.page_microscope)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.groupBox = QGroupBox(self.page_microscope)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_59.addWidget(self.label_5)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_15)

        self.label_microscope_name = QLabel(self.groupBox)
        self.label_microscope_name.setObjectName(u"label_microscope_name")

        self.horizontalLayout_59.addWidget(self.label_microscope_name)

        self.pushButton_edit_microscope_name = QPushButton(self.groupBox)
        self.pushButton_edit_microscope_name.setObjectName(u"pushButton_edit_microscope_name")

        self.horizontalLayout_59.addWidget(self.pushButton_edit_microscope_name)


        self.verticalLayout_5.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_58.addWidget(self.label_6)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_54)

        self.label_microscope_manufacturer = QLabel(self.groupBox)
        self.label_microscope_manufacturer.setObjectName(u"label_microscope_manufacturer")

        self.horizontalLayout_58.addWidget(self.label_microscope_manufacturer)

        self.pushButton_edit_microscope_manufacturer = QPushButton(self.groupBox)
        self.pushButton_edit_microscope_manufacturer.setObjectName(u"pushButton_edit_microscope_manufacturer")

        self.horizontalLayout_58.addWidget(self.pushButton_edit_microscope_manufacturer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_57.addWidget(self.label_16)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_55)

        self.label_acquisition_location = QLabel(self.groupBox)
        self.label_acquisition_location.setObjectName(u"label_acquisition_location")

        self.horizontalLayout_57.addWidget(self.label_acquisition_location)

        self.pushButton_edit_acquisition_location = QPushButton(self.groupBox)
        self.pushButton_edit_acquisition_location.setObjectName(u"pushButton_edit_acquisition_location")

        self.horizontalLayout_57.addWidget(self.pushButton_edit_acquisition_location)


        self.verticalLayout_5.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_15.addWidget(self.label_17)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_56)

        self.label_acquisition_timezone = QLabel(self.groupBox)
        self.label_acquisition_timezone.setObjectName(u"label_acquisition_timezone")

        self.horizontalLayout_15.addWidget(self.label_acquisition_timezone)

        self.pushButton_edit_acquisition_timezone = QPushButton(self.groupBox)
        self.pushButton_edit_acquisition_timezone.setObjectName(u"pushButton_edit_acquisition_timezone")

        self.horizontalLayout_15.addWidget(self.pushButton_edit_acquisition_timezone)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_16.addWidget(self.label_15)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_13)

        self.label_acquisition_date = QLabel(self.groupBox)
        self.label_acquisition_date.setObjectName(u"label_acquisition_date")

        self.horizontalLayout_16.addWidget(self.label_acquisition_date)

        self.pushButton_edit_acquisition_date = QPushButton(self.groupBox)
        self.pushButton_edit_acquisition_date.setObjectName(u"pushButton_edit_acquisition_date")

        self.horizontalLayout_16.addWidget(self.pushButton_edit_acquisition_date)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.label_beam_current = QLabel(self.groupBox)
        self.label_beam_current.setObjectName(u"label_beam_current")

        self.horizontalLayout_7.addWidget(self.label_beam_current)

        self.pushButton_edit_beam_current = QPushButton(self.groupBox)
        self.pushButton_edit_beam_current.setObjectName(u"pushButton_edit_beam_current")

        self.horizontalLayout_7.addWidget(self.pushButton_edit_beam_current)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.label_accelerate_voltage = QLabel(self.groupBox)
        self.label_accelerate_voltage.setObjectName(u"label_accelerate_voltage")

        self.horizontalLayout_8.addWidget(self.label_accelerate_voltage)

        self.pushButton_edit_accelerate_voltage = QPushButton(self.groupBox)
        self.pushButton_edit_accelerate_voltage.setObjectName(u"pushButton_edit_accelerate_voltage")

        self.horizontalLayout_8.addWidget(self.pushButton_edit_accelerate_voltage)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.label_camera_length = QLabel(self.groupBox)
        self.label_camera_length.setObjectName(u"label_camera_length")

        self.horizontalLayout_9.addWidget(self.label_camera_length)

        self.pushButton_edit_camera_length = QPushButton(self.groupBox)
        self.pushButton_edit_camera_length.setObjectName(u"pushButton_edit_camera_length")

        self.horizontalLayout_9.addWidget(self.pushButton_edit_camera_length)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.label_convergence_angle = QLabel(self.groupBox)
        self.label_convergence_angle.setObjectName(u"label_convergence_angle")

        self.horizontalLayout_10.addWidget(self.label_convergence_angle)

        self.pushButton_edit_convergent_angle = QPushButton(self.groupBox)
        self.pushButton_edit_convergent_angle.setObjectName(u"pushButton_edit_convergent_angle")

        self.horizontalLayout_10.addWidget(self.pushButton_edit_convergent_angle)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.label_magnification = QLabel(self.groupBox)
        self.label_magnification.setObjectName(u"label_magnification")

        self.horizontalLayout_11.addWidget(self.label_magnification)

        self.pushButton_edit_magnification = QPushButton(self.groupBox)
        self.pushButton_edit_magnification.setObjectName(u"pushButton_edit_magnification")

        self.horizontalLayout_11.addWidget(self.pushButton_edit_magnification)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)

        self.label_dwell_time = QLabel(self.groupBox)
        self.label_dwell_time.setObjectName(u"label_dwell_time")

        self.horizontalLayout_12.addWidget(self.label_dwell_time)

        self.pushButton_edit_dwell_time = QPushButton(self.groupBox)
        self.pushButton_edit_dwell_time.setObjectName(u"pushButton_edit_dwell_time")

        self.horizontalLayout_12.addWidget(self.pushButton_edit_dwell_time)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_13.addWidget(self.label_14)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.label_step_size_i = QLabel(self.groupBox)
        self.label_step_size_i.setObjectName(u"label_step_size_i")

        self.horizontalLayout_13.addWidget(self.label_step_size_i)

        self.pushButton_edit_step_size_i = QPushButton(self.groupBox)
        self.pushButton_edit_step_size_i.setObjectName(u"pushButton_edit_step_size_i")

        self.horizontalLayout_13.addWidget(self.pushButton_edit_step_size_i)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_12)

        self.label_step_size_j = QLabel(self.groupBox)
        self.label_step_size_j.setObjectName(u"label_step_size_j")

        self.horizontalLayout_14.addWidget(self.label_step_size_j)

        self.pushButton_edit_step_size_j = QPushButton(self.groupBox)
        self.pushButton_edit_step_size_j.setObjectName(u"pushButton_edit_step_size_j")

        self.horizontalLayout_14.addWidget(self.pushButton_edit_step_size_j)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)


        self.verticalLayout_9.addWidget(self.groupBox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page_microscope)
        self.page_camera = QWidget()
        self.page_camera.setObjectName(u"page_camera")
        self.verticalLayout_7 = QVBoxLayout(self.page_camera)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_3 = QGroupBox(self.page_camera)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_21.addWidget(self.label_18)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_57)

        self.label_camera_name = QLabel(self.groupBox_3)
        self.label_camera_name.setObjectName(u"label_camera_name")

        self.horizontalLayout_21.addWidget(self.label_camera_name)

        self.pushButton_edit_camera_name = QPushButton(self.groupBox_3)
        self.pushButton_edit_camera_name.setObjectName(u"pushButton_edit_camera_name")

        self.horizontalLayout_21.addWidget(self.pushButton_edit_camera_name)


        self.verticalLayout_6.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_60.addWidget(self.label_19)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_19)

        self.label_camera_manufacturer = QLabel(self.groupBox_3)
        self.label_camera_manufacturer.setObjectName(u"label_camera_manufacturer")

        self.horizontalLayout_60.addWidget(self.label_camera_manufacturer)

        self.pushButton_edit_camera_manufacturer = QPushButton(self.groupBox_3)
        self.pushButton_edit_camera_manufacturer.setObjectName(u"pushButton_edit_camera_manufacturer")

        self.horizontalLayout_60.addWidget(self.pushButton_edit_camera_manufacturer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_17.addWidget(self.label_20)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_14)

        self.label_camera_pixel_number_i = QLabel(self.groupBox_3)
        self.label_camera_pixel_number_i.setObjectName(u"label_camera_pixel_number_i")

        self.horizontalLayout_17.addWidget(self.label_camera_pixel_number_i)

        self.pushButton_pixel_number_i = QPushButton(self.groupBox_3)
        self.pushButton_pixel_number_i.setObjectName(u"pushButton_pixel_number_i")

        self.horizontalLayout_17.addWidget(self.pushButton_pixel_number_i)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_18.addWidget(self.label_21)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_16)

        self.label_camera_pixel_number_j = QLabel(self.groupBox_3)
        self.label_camera_pixel_number_j.setObjectName(u"label_camera_pixel_number_j")

        self.horizontalLayout_18.addWidget(self.label_camera_pixel_number_j)

        self.pushButton_pixel_number_j = QPushButton(self.groupBox_3)
        self.pushButton_pixel_number_j.setObjectName(u"pushButton_pixel_number_j")

        self.horizontalLayout_18.addWidget(self.pushButton_pixel_number_j)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_19.addWidget(self.label_22)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_17)

        self.label_camera_pixel_size_i = QLabel(self.groupBox_3)
        self.label_camera_pixel_size_i.setObjectName(u"label_camera_pixel_size_i")

        self.horizontalLayout_19.addWidget(self.label_camera_pixel_size_i)

        self.pushButton_edit_camera_pixel_size_i = QPushButton(self.groupBox_3)
        self.pushButton_edit_camera_pixel_size_i.setObjectName(u"pushButton_edit_camera_pixel_size_i")

        self.horizontalLayout_19.addWidget(self.pushButton_edit_camera_pixel_size_i)


        self.verticalLayout_6.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_20.addWidget(self.label_23)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_18)

        self.label_camera_pixel_size_j = QLabel(self.groupBox_3)
        self.label_camera_pixel_size_j.setObjectName(u"label_camera_pixel_size_j")

        self.horizontalLayout_20.addWidget(self.label_camera_pixel_size_j)

        self.pushButton_edit_camera_pixel_size_j = QPushButton(self.groupBox_3)
        self.pushButton_edit_camera_pixel_size_j.setObjectName(u"pushButton_edit_camera_pixel_size_j")

        self.horizontalLayout_20.addWidget(self.pushButton_edit_camera_pixel_size_j)


        self.verticalLayout_6.addLayout(self.horizontalLayout_20)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_camera)
        self.page_space = QWidget()
        self.page_space.setObjectName(u"page_space")
        self.verticalLayout_17 = QVBoxLayout(self.page_space)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, 0, -1)
        self.groupBox_4 = QGroupBox(self.page_space)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_24 = QLabel(self.groupBox_4)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_27.addWidget(self.label_24)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_20)

        self.label_du_i = QLabel(self.groupBox_4)
        self.label_du_i.setObjectName(u"label_du_i")

        self.horizontalLayout_27.addWidget(self.label_du_i)

        self.pushButton_edit_du_i = QPushButton(self.groupBox_4)
        self.pushButton_edit_du_i.setObjectName(u"pushButton_edit_du_i")

        self.horizontalLayout_27.addWidget(self.pushButton_edit_du_i)


        self.verticalLayout_16.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_25 = QLabel(self.groupBox_4)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_26.addWidget(self.label_25)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_21)

        self.label_du_j = QLabel(self.groupBox_4)
        self.label_du_j.setObjectName(u"label_du_j")

        self.horizontalLayout_26.addWidget(self.label_du_j)

        self.pushButton_edit_du_j = QPushButton(self.groupBox_4)
        self.pushButton_edit_du_j.setObjectName(u"pushButton_edit_du_j")

        self.horizontalLayout_26.addWidget(self.pushButton_edit_du_j)


        self.verticalLayout_16.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_28 = QLabel(self.groupBox_4)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_25.addWidget(self.label_28)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_22)

        self.label_dr_i = QLabel(self.groupBox_4)
        self.label_dr_i.setObjectName(u"label_dr_i")

        self.horizontalLayout_25.addWidget(self.label_dr_i)

        self.pushButton_edit_dr_i = QPushButton(self.groupBox_4)
        self.pushButton_edit_dr_i.setObjectName(u"pushButton_edit_dr_i")

        self.horizontalLayout_25.addWidget(self.pushButton_edit_dr_i)


        self.verticalLayout_16.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_29 = QLabel(self.groupBox_4)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_24.addWidget(self.label_29)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_23)

        self.label_dr_j = QLabel(self.groupBox_4)
        self.label_dr_j.setObjectName(u"label_dr_j")

        self.horizontalLayout_24.addWidget(self.label_dr_j)

        self.pushButton_edit_dr_j = QPushButton(self.groupBox_4)
        self.pushButton_edit_dr_j.setObjectName(u"pushButton_edit_dr_j")

        self.horizontalLayout_24.addWidget(self.pushButton_edit_dr_j)


        self.verticalLayout_16.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_26 = QLabel(self.groupBox_4)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_23.addWidget(self.label_26)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_24)

        self.label_scan_dr_i = QLabel(self.groupBox_4)
        self.label_scan_dr_i.setObjectName(u"label_scan_dr_i")

        self.horizontalLayout_23.addWidget(self.label_scan_dr_i)

        self.pushButton_edit_scan_dr_i = QPushButton(self.groupBox_4)
        self.pushButton_edit_scan_dr_i.setObjectName(u"pushButton_edit_scan_dr_i")

        self.horizontalLayout_23.addWidget(self.pushButton_edit_scan_dr_i)


        self.verticalLayout_16.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_27 = QLabel(self.groupBox_4)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_22.addWidget(self.label_27)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_25)

        self.label_scan_dr_j = QLabel(self.groupBox_4)
        self.label_scan_dr_j.setObjectName(u"label_scan_dr_j")

        self.horizontalLayout_22.addWidget(self.label_scan_dr_j)

        self.pushButton_edit_scan_dr_j = QPushButton(self.groupBox_4)
        self.pushButton_edit_scan_dr_j.setObjectName(u"pushButton_edit_scan_dr_j")

        self.horizontalLayout_22.addWidget(self.pushButton_edit_scan_dr_j)


        self.verticalLayout_16.addLayout(self.horizontalLayout_22)


        self.verticalLayout_17.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.page_space)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_30 = QLabel(self.groupBox_5)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_28.addWidget(self.label_30)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_26)

        self.label_scan_i = QLabel(self.groupBox_5)
        self.label_scan_i.setObjectName(u"label_scan_i")

        self.horizontalLayout_28.addWidget(self.label_scan_i)


        self.verticalLayout_15.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_31 = QLabel(self.groupBox_5)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_29.addWidget(self.label_31)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_27)

        self.label_scan_j = QLabel(self.groupBox_5)
        self.label_scan_j.setObjectName(u"label_scan_j")

        self.horizontalLayout_29.addWidget(self.label_scan_j)


        self.verticalLayout_15.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_32 = QLabel(self.groupBox_5)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_30.addWidget(self.label_32)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_28)

        self.label_dp_i = QLabel(self.groupBox_5)
        self.label_dp_i.setObjectName(u"label_dp_i")

        self.horizontalLayout_30.addWidget(self.label_dp_i)


        self.verticalLayout_15.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_33 = QLabel(self.groupBox_5)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_31.addWidget(self.label_33)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_29)

        self.label_dp_j = QLabel(self.groupBox_5)
        self.label_dp_j.setObjectName(u"label_dp_j")

        self.horizontalLayout_31.addWidget(self.label_dp_j)


        self.verticalLayout_15.addLayout(self.horizontalLayout_31)


        self.verticalLayout_17.addWidget(self.groupBox_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.page_space)
        self.page_low_order_aberration = QWidget()
        self.page_low_order_aberration.setObjectName(u"page_low_order_aberration")
        self.verticalLayout_20 = QVBoxLayout(self.page_low_order_aberration)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, -1, 0, -1)
        self.groupBox_6 = QGroupBox(self.page_low_order_aberration)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_34 = QLabel(self.groupBox_6)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_32.addWidget(self.label_34)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_30)

        self.label_C1 = QLabel(self.groupBox_6)
        self.label_C1.setObjectName(u"label_C1")

        self.horizontalLayout_32.addWidget(self.label_C1)

        self.pushButton_edit_C1 = QPushButton(self.groupBox_6)
        self.pushButton_edit_C1.setObjectName(u"pushButton_edit_C1")

        self.horizontalLayout_32.addWidget(self.pushButton_edit_C1)


        self.verticalLayout_18.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_35 = QLabel(self.groupBox_6)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_33.addWidget(self.label_35)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_31)

        self.label_A1 = QLabel(self.groupBox_6)
        self.label_A1.setObjectName(u"label_A1")

        self.horizontalLayout_33.addWidget(self.label_A1)

        self.pushButton_edit_A1 = QPushButton(self.groupBox_6)
        self.pushButton_edit_A1.setObjectName(u"pushButton_edit_A1")

        self.horizontalLayout_33.addWidget(self.pushButton_edit_A1)


        self.verticalLayout_18.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_37 = QLabel(self.groupBox_6)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_34.addWidget(self.label_37)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_32)

        self.label_B2 = QLabel(self.groupBox_6)
        self.label_B2.setObjectName(u"label_B2")

        self.horizontalLayout_34.addWidget(self.label_B2)

        self.pushButton_edit_B2 = QPushButton(self.groupBox_6)
        self.pushButton_edit_B2.setObjectName(u"pushButton_edit_B2")

        self.horizontalLayout_34.addWidget(self.pushButton_edit_B2)


        self.verticalLayout_18.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_39 = QLabel(self.groupBox_6)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_35.addWidget(self.label_39)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_33)

        self.label_A2 = QLabel(self.groupBox_6)
        self.label_A2.setObjectName(u"label_A2")

        self.horizontalLayout_35.addWidget(self.label_A2)

        self.pushButton_edit_A2 = QPushButton(self.groupBox_6)
        self.pushButton_edit_A2.setObjectName(u"pushButton_edit_A2")

        self.horizontalLayout_35.addWidget(self.pushButton_edit_A2)


        self.verticalLayout_18.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_41 = QLabel(self.groupBox_6)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_36.addWidget(self.label_41)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_34)

        self.label_C3 = QLabel(self.groupBox_6)
        self.label_C3.setObjectName(u"label_C3")

        self.horizontalLayout_36.addWidget(self.label_C3)

        self.pushButton_edit_C3 = QPushButton(self.groupBox_6)
        self.pushButton_edit_C3.setObjectName(u"pushButton_edit_C3")

        self.horizontalLayout_36.addWidget(self.pushButton_edit_C3)


        self.verticalLayout_18.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_43 = QLabel(self.groupBox_6)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_37.addWidget(self.label_43)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_35)

        self.label_S3 = QLabel(self.groupBox_6)
        self.label_S3.setObjectName(u"label_S3")

        self.horizontalLayout_37.addWidget(self.label_S3)

        self.pushButton_edit_S3 = QPushButton(self.groupBox_6)
        self.pushButton_edit_S3.setObjectName(u"pushButton_edit_S3")

        self.horizontalLayout_37.addWidget(self.pushButton_edit_S3)


        self.verticalLayout_18.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_45 = QLabel(self.groupBox_6)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_38.addWidget(self.label_45)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_36)

        self.label_A3 = QLabel(self.groupBox_6)
        self.label_A3.setObjectName(u"label_A3")

        self.horizontalLayout_38.addWidget(self.label_A3)

        self.pushButton_edit_A3 = QPushButton(self.groupBox_6)
        self.pushButton_edit_A3.setObjectName(u"pushButton_edit_A3")

        self.horizontalLayout_38.addWidget(self.pushButton_edit_A3)


        self.verticalLayout_18.addLayout(self.horizontalLayout_38)


        self.verticalLayout_20.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.page_low_order_aberration)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_47 = QLabel(self.groupBox_7)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_19.addWidget(self.label_47)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_54 = QLabel(self.groupBox_7)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_39.addWidget(self.label_54)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_37)

        self.label_C1_angle = QLabel(self.groupBox_7)
        self.label_C1_angle.setObjectName(u"label_C1_angle")

        self.horizontalLayout_39.addWidget(self.label_C1_angle)

        self.pushButton_edit_C1_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_C1_angle.setObjectName(u"pushButton_edit_C1_angle")

        self.horizontalLayout_39.addWidget(self.pushButton_edit_C1_angle)


        self.verticalLayout_19.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_36 = QLabel(self.groupBox_7)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_40.addWidget(self.label_36)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_38)

        self.label_A1_angle = QLabel(self.groupBox_7)
        self.label_A1_angle.setObjectName(u"label_A1_angle")

        self.horizontalLayout_40.addWidget(self.label_A1_angle)

        self.pushButton_edit_A1_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_A1_angle.setObjectName(u"pushButton_edit_A1_angle")

        self.horizontalLayout_40.addWidget(self.pushButton_edit_A1_angle)


        self.verticalLayout_19.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_38 = QLabel(self.groupBox_7)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_41.addWidget(self.label_38)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_39)

        self.label_B2_angle = QLabel(self.groupBox_7)
        self.label_B2_angle.setObjectName(u"label_B2_angle")

        self.horizontalLayout_41.addWidget(self.label_B2_angle)

        self.pushButton_edit_B2_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_B2_angle.setObjectName(u"pushButton_edit_B2_angle")

        self.horizontalLayout_41.addWidget(self.pushButton_edit_B2_angle)


        self.verticalLayout_19.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_40 = QLabel(self.groupBox_7)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_42.addWidget(self.label_40)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_40)

        self.label_A2_angle = QLabel(self.groupBox_7)
        self.label_A2_angle.setObjectName(u"label_A2_angle")

        self.horizontalLayout_42.addWidget(self.label_A2_angle)

        self.pushButton_edit_A2_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_A2_angle.setObjectName(u"pushButton_edit_A2_angle")

        self.horizontalLayout_42.addWidget(self.pushButton_edit_A2_angle)


        self.verticalLayout_19.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_42 = QLabel(self.groupBox_7)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_43.addWidget(self.label_42)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_41)

        self.label_C3_angle = QLabel(self.groupBox_7)
        self.label_C3_angle.setObjectName(u"label_C3_angle")

        self.horizontalLayout_43.addWidget(self.label_C3_angle)

        self.pushButton_edit_C3_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_C3_angle.setObjectName(u"pushButton_edit_C3_angle")

        self.horizontalLayout_43.addWidget(self.pushButton_edit_C3_angle)


        self.verticalLayout_19.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_44 = QLabel(self.groupBox_7)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_44.addWidget(self.label_44)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_42)

        self.label_S3_angle = QLabel(self.groupBox_7)
        self.label_S3_angle.setObjectName(u"label_S3_angle")

        self.horizontalLayout_44.addWidget(self.label_S3_angle)

        self.pushButton_edit_S3_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_S3_angle.setObjectName(u"pushButton_edit_S3_angle")

        self.horizontalLayout_44.addWidget(self.pushButton_edit_S3_angle)


        self.verticalLayout_19.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_46 = QLabel(self.groupBox_7)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_45.addWidget(self.label_46)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_43)

        self.label_A3_angle = QLabel(self.groupBox_7)
        self.label_A3_angle.setObjectName(u"label_A3_angle")

        self.horizontalLayout_45.addWidget(self.label_A3_angle)

        self.pushButton_edit_A3_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_A3_angle.setObjectName(u"pushButton_edit_A3_angle")

        self.horizontalLayout_45.addWidget(self.pushButton_edit_A3_angle)


        self.verticalLayout_19.addLayout(self.horizontalLayout_45)


        self.verticalLayout_20.addWidget(self.groupBox_7)

        self.verticalSpacer_5 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_5)

        self.stackedWidget.addWidget(self.page_low_order_aberration)
        self.page_high_order_aberration = QWidget()
        self.page_high_order_aberration.setObjectName(u"page_high_order_aberration")
        self.verticalLayout_23 = QVBoxLayout(self.page_high_order_aberration)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, -1, 0, -1)
        self.groupBox_8 = QGroupBox(self.page_high_order_aberration)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_56 = QLabel(self.groupBox_8)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_51.addWidget(self.label_56)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_49)

        self.label_B4 = QLabel(self.groupBox_8)
        self.label_B4.setObjectName(u"label_B4")

        self.horizontalLayout_51.addWidget(self.label_B4)

        self.pushButton_edit_B4 = QPushButton(self.groupBox_8)
        self.pushButton_edit_B4.setObjectName(u"pushButton_edit_B4")

        self.horizontalLayout_51.addWidget(self.pushButton_edit_B4)


        self.verticalLayout_21.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_57 = QLabel(self.groupBox_8)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_52.addWidget(self.label_57)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_50)

        self.label_D4 = QLabel(self.groupBox_8)
        self.label_D4.setObjectName(u"label_D4")

        self.horizontalLayout_52.addWidget(self.label_D4)

        self.pushButton_edit_D4 = QPushButton(self.groupBox_8)
        self.pushButton_edit_D4.setObjectName(u"pushButton_edit_D4")

        self.horizontalLayout_52.addWidget(self.pushButton_edit_D4)


        self.verticalLayout_21.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_58 = QLabel(self.groupBox_8)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_53.addWidget(self.label_58)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_51)

        self.label_A4 = QLabel(self.groupBox_8)
        self.label_A4.setObjectName(u"label_A4")

        self.horizontalLayout_53.addWidget(self.label_A4)

        self.pushButton_edit_A4 = QPushButton(self.groupBox_8)
        self.pushButton_edit_A4.setObjectName(u"pushButton_edit_A4")

        self.horizontalLayout_53.addWidget(self.pushButton_edit_A4)


        self.verticalLayout_21.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_59 = QLabel(self.groupBox_8)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_54.addWidget(self.label_59)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_52)

        self.label_C5 = QLabel(self.groupBox_8)
        self.label_C5.setObjectName(u"label_C5")

        self.horizontalLayout_54.addWidget(self.label_C5)

        self.pushButton_edit_C5 = QPushButton(self.groupBox_8)
        self.pushButton_edit_C5.setObjectName(u"pushButton_edit_C5")

        self.horizontalLayout_54.addWidget(self.pushButton_edit_C5)


        self.verticalLayout_21.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_60 = QLabel(self.groupBox_8)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_55.addWidget(self.label_60)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_53)

        self.label_A5 = QLabel(self.groupBox_8)
        self.label_A5.setObjectName(u"label_A5")

        self.horizontalLayout_55.addWidget(self.label_A5)

        self.pushButton_edit_A5 = QPushButton(self.groupBox_8)
        self.pushButton_edit_A5.setObjectName(u"pushButton_edit_A5")

        self.horizontalLayout_55.addWidget(self.pushButton_edit_A5)


        self.verticalLayout_21.addLayout(self.horizontalLayout_55)


        self.verticalLayout_23.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.page_high_order_aberration)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_61 = QLabel(self.groupBox_9)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_46.addWidget(self.label_61)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_44)

        self.label_B4_angle = QLabel(self.groupBox_9)
        self.label_B4_angle.setObjectName(u"label_B4_angle")

        self.horizontalLayout_46.addWidget(self.label_B4_angle)

        self.pushButton_edit_B4_angle = QPushButton(self.groupBox_9)
        self.pushButton_edit_B4_angle.setObjectName(u"pushButton_edit_B4_angle")

        self.horizontalLayout_46.addWidget(self.pushButton_edit_B4_angle)


        self.verticalLayout_22.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_62 = QLabel(self.groupBox_9)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_47.addWidget(self.label_62)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_45)

        self.label_D4_angle = QLabel(self.groupBox_9)
        self.label_D4_angle.setObjectName(u"label_D4_angle")

        self.horizontalLayout_47.addWidget(self.label_D4_angle)

        self.pushButton_edit_D4_angle = QPushButton(self.groupBox_9)
        self.pushButton_edit_D4_angle.setObjectName(u"pushButton_edit_D4_angle")

        self.horizontalLayout_47.addWidget(self.pushButton_edit_D4_angle)


        self.verticalLayout_22.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_63 = QLabel(self.groupBox_9)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_48.addWidget(self.label_63)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_46)

        self.label_A4_angle = QLabel(self.groupBox_9)
        self.label_A4_angle.setObjectName(u"label_A4_angle")

        self.horizontalLayout_48.addWidget(self.label_A4_angle)

        self.pushButton_edit_A4_angle = QPushButton(self.groupBox_9)
        self.pushButton_edit_A4_angle.setObjectName(u"pushButton_edit_A4_angle")

        self.horizontalLayout_48.addWidget(self.pushButton_edit_A4_angle)


        self.verticalLayout_22.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_64 = QLabel(self.groupBox_9)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_49.addWidget(self.label_64)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_48)

        self.label_C5_angle = QLabel(self.groupBox_9)
        self.label_C5_angle.setObjectName(u"label_C5_angle")

        self.horizontalLayout_49.addWidget(self.label_C5_angle)

        self.pushButton_edit_C5_angle = QPushButton(self.groupBox_9)
        self.pushButton_edit_C5_angle.setObjectName(u"pushButton_edit_C5_angle")

        self.horizontalLayout_49.addWidget(self.pushButton_edit_C5_angle)


        self.verticalLayout_22.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_65 = QLabel(self.groupBox_9)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_50.addWidget(self.label_65)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_47)

        self.label_A5_angle = QLabel(self.groupBox_9)
        self.label_A5_angle.setObjectName(u"label_A5_angle")

        self.horizontalLayout_50.addWidget(self.label_A5_angle)

        self.pushButton_edit_A5_angle = QPushButton(self.groupBox_9)
        self.pushButton_edit_A5_angle.setObjectName(u"pushButton_edit_A5_angle")

        self.horizontalLayout_50.addWidget(self.pushButton_edit_A5_angle)


        self.verticalLayout_22.addLayout(self.horizontalLayout_50)


        self.verticalLayout_23.addWidget(self.groupBox_9)

        self.verticalSpacer_6 = QSpacerItem(20, 165, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_6)

        self.stackedWidget.addWidget(self.page_high_order_aberration)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_4.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_4.addWidget(self.pushButton_cancel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_71.setText(QCoreApplication.translate("Dialog", u"4D-STEM path", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Steps:", None))
        self.label_steps.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton_back.setText(QCoreApplication.translate("Dialog", u"\u2190 Back", None))
        self.pushButton_next.setText(QCoreApplication.translate("Dialog", u"Next \u2192", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Basic Information", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Dataset Title", None))
        self.pushButton_edit_dataset_title.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Authors", None))
        self.pushButton_edit_authors.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Notes", None))
        self.pushButton_edit_notes.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Microscope", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_microscope_name.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton_edit_microscope_name.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Manufacturer", None))
        self.label_microscope_manufacturer.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton_edit_microscope_manufacturer.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Acquisition Location", None))
        self.label_acquisition_location.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton_edit_acquisition_location.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Acquisition Timezone", None))
        self.label_acquisition_timezone.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton_edit_acquisition_timezone.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Acquisition Date", None))
        self.label_acquisition_date.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton_edit_acquisition_date.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Beam Current", None))
        self.label_beam_current.setText(QCoreApplication.translate("Dialog", u"0 nA", None))
        self.pushButton_edit_beam_current.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Accelerate Voltage", None))
        self.label_accelerate_voltage.setText(QCoreApplication.translate("Dialog", u"0 kV", None))
        self.pushButton_edit_accelerate_voltage.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Camera Length", None))
        self.label_camera_length.setText(QCoreApplication.translate("Dialog", u"0 m", None))
        self.pushButton_edit_camera_length.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Convergence Angle", None))
        self.label_convergence_angle.setText(QCoreApplication.translate("Dialog", u"0 mrad", None))
        self.pushButton_edit_convergent_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Magnification", None))
        self.label_magnification.setText(QCoreApplication.translate("Dialog", u"0x", None))
        self.pushButton_edit_magnification.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Dwell Time", None))
        self.label_dwell_time.setText(QCoreApplication.translate("Dialog", u"0 us", None))
        self.pushButton_edit_dwell_time.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Step Size (I Direction)", None))
        self.label_step_size_i.setText(QCoreApplication.translate("Dialog", u"0 nm", None))
        self.pushButton_edit_step_size_i.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Step Size (J Direction)", None))
        self.label_step_size_j.setText(QCoreApplication.translate("Dialog", u"0 nm", None))
        self.pushButton_edit_step_size_j.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Camera", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_camera_name.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton_edit_camera_name.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Manufacturer", None))
        self.label_camera_manufacturer.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton_edit_camera_manufacturer.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Pixel Number (Height)", None))
        self.label_camera_pixel_number_i.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.pushButton_pixel_number_i.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Pixel Number (Width)", None))
        self.label_camera_pixel_number_j.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.pushButton_pixel_number_j.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Sensor Pixel Size (Height)", None))
        self.label_camera_pixel_size_i.setText(QCoreApplication.translate("Dialog", u"0 \u03bcm", None))
        self.pushButton_edit_camera_pixel_size_i.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Sensor Pixel Size (Width)", None))
        self.label_camera_pixel_size_j.setText(QCoreApplication.translate("Dialog", u"0 \u03bcm", None))
        self.pushButton_edit_camera_pixel_size_j.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Calibrated Space Parameters", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"\u0394u (I Direction)", None))
        self.label_du_i.setText(QCoreApplication.translate("Dialog", u"1 1/nm", None))
        self.pushButton_edit_du_i.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"\u0394u (J Direction)", None))
        self.label_du_j.setText(QCoreApplication.translate("Dialog", u"1 1/nm", None))
        self.pushButton_edit_du_j.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"\u0394r (I Direction)", None))
        self.label_dr_i.setText(QCoreApplication.translate("Dialog", u"1 nm", None))
        self.pushButton_edit_dr_i.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"\u0394r (J Direction)", None))
        self.label_dr_j.setText(QCoreApplication.translate("Dialog", u"1 nm", None))
        self.pushButton_edit_dr_j.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Scanning \u0394r (I Direction)", None))
        self.label_scan_dr_i.setText(QCoreApplication.translate("Dialog", u"1 nm", None))
        self.pushButton_edit_scan_dr_i.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Scanning \u0394r (J Direction)", None))
        self.label_scan_dr_j.setText(QCoreApplication.translate("Dialog", u"1 nm", None))
        self.pushButton_edit_scan_dr_j.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"4D-STEM Dataset Shape", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"Scanning Steps (I Direction)", None))
        self.label_scan_i.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"Scanning Steps (J Direction)", None))
        self.label_scan_j.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"Diffraction Pattern Height", None))
        self.label_dp_i.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label_33.setText(QCoreApplication.translate("Dialog", u"Diffraction Pattern Width", None))
        self.label_dp_j.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"Low Order Aberration Coefficients (Length)", None))
        self.label_34.setText(QCoreApplication.translate("Dialog", u"C1", None))
        self.label_C1.setText(QCoreApplication.translate("Dialog", u"0 nm", None))
        self.pushButton_edit_C1.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_35.setText(QCoreApplication.translate("Dialog", u"A1", None))
        self.label_A1.setText(QCoreApplication.translate("Dialog", u"0 nm", None))
        self.pushButton_edit_A1.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_37.setText(QCoreApplication.translate("Dialog", u"B2", None))
        self.label_B2.setText(QCoreApplication.translate("Dialog", u"0 nm", None))
        self.pushButton_edit_B2.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_39.setText(QCoreApplication.translate("Dialog", u"A2", None))
        self.label_A2.setText(QCoreApplication.translate("Dialog", u"0 nm", None))
        self.pushButton_edit_A2.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_41.setText(QCoreApplication.translate("Dialog", u"C3", None))
        self.label_C3.setText(QCoreApplication.translate("Dialog", u"0 \u03bcm", None))
        self.pushButton_edit_C3.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_43.setText(QCoreApplication.translate("Dialog", u"S3", None))
        self.label_S3.setText(QCoreApplication.translate("Dialog", u"0 \u03bcm", None))
        self.pushButton_edit_S3.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_45.setText(QCoreApplication.translate("Dialog", u"A3", None))
        self.label_A3.setText(QCoreApplication.translate("Dialog", u"0 \u03bcm", None))
        self.pushButton_edit_A3.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog", u"Low Order Aberration Coefficients (Angle)", None))
        self.label_47.setText(QCoreApplication.translate("Dialog", u"Defocus (C1) Angle", None))
        self.label_54.setText(QCoreApplication.translate("Dialog", u"C1", None))
        self.label_C1_angle.setText(QCoreApplication.translate("Dialog", u"0 deg", None))
        self.pushButton_edit_C1_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_36.setText(QCoreApplication.translate("Dialog", u"A1", None))
        self.label_A1_angle.setText(QCoreApplication.translate("Dialog", u"0 deg", None))
        self.pushButton_edit_A1_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_38.setText(QCoreApplication.translate("Dialog", u"B2", None))
        self.label_B2_angle.setText(QCoreApplication.translate("Dialog", u"0 deg", None))
        self.pushButton_edit_B2_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_40.setText(QCoreApplication.translate("Dialog", u"A2", None))
        self.label_A2_angle.setText(QCoreApplication.translate("Dialog", u"0 deg", None))
        self.pushButton_edit_A2_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_42.setText(QCoreApplication.translate("Dialog", u"C3", None))
        self.label_C3_angle.setText(QCoreApplication.translate("Dialog", u"0 deg", None))
        self.pushButton_edit_C3_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_44.setText(QCoreApplication.translate("Dialog", u"S3", None))
        self.label_S3_angle.setText(QCoreApplication.translate("Dialog", u"0 deg", None))
        self.pushButton_edit_S3_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_46.setText(QCoreApplication.translate("Dialog", u"A3", None))
        self.label_A3_angle.setText(QCoreApplication.translate("Dialog", u"0 deg", None))
        self.pushButton_edit_A3_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Dialog", u"High Order Aberration Coefficients (Length)", None))
        self.label_56.setText(QCoreApplication.translate("Dialog", u"B4", None))
        self.label_B4.setText(QCoreApplication.translate("Dialog", u"0 \u03bcm", None))
        self.pushButton_edit_B4.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_57.setText(QCoreApplication.translate("Dialog", u"D4", None))
        self.label_D4.setText(QCoreApplication.translate("Dialog", u"0 \u03bcm", None))
        self.pushButton_edit_D4.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_58.setText(QCoreApplication.translate("Dialog", u"A4", None))
        self.label_A4.setText(QCoreApplication.translate("Dialog", u"0 \u03bcm", None))
        self.pushButton_edit_A4.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_59.setText(QCoreApplication.translate("Dialog", u"C5", None))
        self.label_C5.setText(QCoreApplication.translate("Dialog", u"0 mm", None))
        self.pushButton_edit_C5.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_60.setText(QCoreApplication.translate("Dialog", u"A5", None))
        self.label_A5.setText(QCoreApplication.translate("Dialog", u"0 mm", None))
        self.pushButton_edit_A5.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Dialog", u"High Order Aberration Coefficients (Angle)", None))
        self.label_61.setText(QCoreApplication.translate("Dialog", u"B4", None))
        self.label_B4_angle.setText(QCoreApplication.translate("Dialog", u"0 deg", None))
        self.pushButton_edit_B4_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_62.setText(QCoreApplication.translate("Dialog", u"D4", None))
        self.label_D4_angle.setText(QCoreApplication.translate("Dialog", u"0 deg", None))
        self.pushButton_edit_D4_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_63.setText(QCoreApplication.translate("Dialog", u"A4", None))
        self.label_A4_angle.setText(QCoreApplication.translate("Dialog", u"0 deg", None))
        self.pushButton_edit_A4_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_64.setText(QCoreApplication.translate("Dialog", u"C5", None))
        self.label_C5_angle.setText(QCoreApplication.translate("Dialog", u"0 deg", None))
        self.pushButton_edit_C5_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.label_65.setText(QCoreApplication.translate("Dialog", u"A5", None))
        self.label_A5_angle.setText(QCoreApplication.translate("Dialog", u"0 deg", None))
        self.pushButton_edit_A5_angle.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

