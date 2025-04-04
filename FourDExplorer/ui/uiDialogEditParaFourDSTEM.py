# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogEditParaFourDSTEM.ui'
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
    QDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(536, 734)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(18, -1, 18, -1)
        self.label_71 = QLabel(Dialog)
        self.label_71.setObjectName("label_71")

        self.horizontalLayout_56.addWidget(self.label_71)

        self.lineEdit_dataset_path = QLineEdit(Dialog)
        self.lineEdit_dataset_path.setObjectName("lineEdit_dataset_path")

        self.horizontalLayout_56.addWidget(self.lineEdit_dataset_path)

        self.pushButton_browse = QPushButton(Dialog)
        self.pushButton_browse.setObjectName("pushButton_browse")

        self.horizontalLayout_56.addWidget(self.pushButton_browse)

        self.verticalLayout_4.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(18, -1, 18, -1)
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")

        self.horizontalLayout_3.addWidget(self.label)

        self.label_steps = QLabel(Dialog)
        self.label_steps.setObjectName("label_steps")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_steps.sizePolicy().hasHeightForWidth())
        self.label_steps.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_steps)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 516, 626))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_back = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_back.setObjectName("pushButton_back")

        self.horizontalLayout_2.addWidget(self.pushButton_back)

        self.pushButton_next = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_next.setObjectName("pushButton_next")

        self.horizontalLayout_2.addWidget(self.pushButton_next)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_general = QWidget()
        self.page_general.setObjectName("page_general")
        self.verticalLayout_3 = QVBoxLayout(self.page_general)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.groupBox_2 = QGroupBox(self.page_general)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_58 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_58)

        self.label_general_title = QLabel(self.groupBox_2)
        self.label_general_title.setObjectName("label_general_title")

        self.horizontalLayout.addWidget(self.label_general_title)

        self.pushButton_edit_general_title = QPushButton(self.groupBox_2)
        self.pushButton_edit_general_title.setObjectName(
            "pushButton_edit_general_title"
        )

        self.horizontalLayout.addWidget(self.pushButton_edit_general_title)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_48 = QLabel(self.groupBox_2)
        self.label_48.setObjectName("label_48")

        self.horizontalLayout_5.addWidget(self.label_48)

        self.horizontalSpacer_59 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_59)

        self.label_general_data_path = QLabel(self.groupBox_2)
        self.label_general_data_path.setObjectName("label_general_data_path")

        self.horizontalLayout_5.addWidget(self.label_general_data_path)

        self.pushButton_edit_general_data_path = QPushButton(self.groupBox_2)
        self.pushButton_edit_general_data_path.setObjectName(
            "pushButton_edit_general_data_path"
        )

        self.horizontalLayout_5.addWidget(self.pushButton_edit_general_data_path)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_49 = QLabel(self.groupBox_2)
        self.label_49.setObjectName("label_49")

        self.horizontalLayout_6.addWidget(self.label_49)

        self.horizontalSpacer_60 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_60)

        self.label_general_header_path = QLabel(self.groupBox_2)
        self.label_general_header_path.setObjectName("label_general_header_path")

        self.horizontalLayout_6.addWidget(self.label_general_header_path)

        self.pushButton_edit_general_header_path = QPushButton(self.groupBox_2)
        self.pushButton_edit_general_header_path.setObjectName(
            "pushButton_edit_general_header_path"
        )

        self.horizontalLayout_6.addWidget(self.pushButton_edit_general_header_path)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.label_50 = QLabel(self.groupBox_2)
        self.label_50.setObjectName("label_50")

        self.horizontalLayout_61.addWidget(self.label_50)

        self.horizontalSpacer_61 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_61.addItem(self.horizontalSpacer_61)

        self.label_general_time = QLabel(self.groupBox_2)
        self.label_general_time.setObjectName("label_general_time")

        self.horizontalLayout_61.addWidget(self.label_general_time)

        self.pushButton_edit_general_time = QPushButton(self.groupBox_2)
        self.pushButton_edit_general_time.setObjectName("pushButton_edit_general_time")

        self.horizontalLayout_61.addWidget(self.pushButton_edit_general_time)

        self.verticalLayout_2.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.label_51 = QLabel(self.groupBox_2)
        self.label_51.setObjectName("label_51")

        self.horizontalLayout_62.addWidget(self.label_51)

        self.horizontalSpacer_62 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_62.addItem(self.horizontalSpacer_62)

        self.label_general_date = QLabel(self.groupBox_2)
        self.label_general_date.setObjectName("label_general_date")

        self.horizontalLayout_62.addWidget(self.label_general_date)

        self.pushButton_edit_general_date = QPushButton(self.groupBox_2)
        self.pushButton_edit_general_date.setObjectName("pushButton_edit_general_date")

        self.horizontalLayout_62.addWidget(self.pushButton_edit_general_date)

        self.verticalLayout_2.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.label_52 = QLabel(self.groupBox_2)
        self.label_52.setObjectName("label_52")

        self.horizontalLayout_63.addWidget(self.label_52)

        self.horizontalSpacer_63 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_63.addItem(self.horizontalSpacer_63)

        self.label_general_time_zone = QLabel(self.groupBox_2)
        self.label_general_time_zone.setObjectName("label_general_time_zone")

        self.horizontalLayout_63.addWidget(self.label_general_time_zone)

        self.pushButton_edit_general_time_zone = QPushButton(self.groupBox_2)
        self.pushButton_edit_general_time_zone.setObjectName(
            "pushButton_edit_general_time_zone"
        )

        self.horizontalLayout_63.addWidget(self.pushButton_edit_general_time_zone)

        self.verticalLayout_2.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.label_53 = QLabel(self.groupBox_2)
        self.label_53.setObjectName("label_53")

        self.horizontalLayout_64.addWidget(self.label_53)

        self.horizontalSpacer_64 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_64.addItem(self.horizontalSpacer_64)

        self.label_general_doi = QLabel(self.groupBox_2)
        self.label_general_doi.setObjectName("label_general_doi")

        self.horizontalLayout_64.addWidget(self.label_general_doi)

        self.pushButton_edit_general_doi = QPushButton(self.groupBox_2)
        self.pushButton_edit_general_doi.setObjectName("pushButton_edit_general_doi")

        self.horizontalLayout_64.addWidget(self.pushButton_edit_general_doi)

        self.verticalLayout_2.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_65.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_65.addItem(self.horizontalSpacer_3)

        self.label_general_authors = QLabel(self.groupBox_2)
        self.label_general_authors.setObjectName("label_general_authors")

        self.horizontalLayout_65.addWidget(self.label_general_authors)

        self.pushButton_edit_general_authors = QPushButton(self.groupBox_2)
        self.pushButton_edit_general_authors.setObjectName(
            "pushButton_edit_general_authors"
        )

        self.horizontalLayout_65.addWidget(self.pushButton_edit_general_authors)

        self.verticalLayout_2.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_66.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_66.addItem(self.horizontalSpacer_4)

        self.label_general_notes = QLabel(self.groupBox_2)
        self.label_general_notes.setObjectName("label_general_notes")

        self.horizontalLayout_66.addWidget(self.label_general_notes)

        self.pushButton_edit_general_notes = QPushButton(self.groupBox_2)
        self.pushButton_edit_general_notes.setObjectName(
            "pushButton_edit_general_notes"
        )

        self.horizontalLayout_66.addWidget(self.pushButton_edit_general_notes)

        self.verticalLayout_2.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        self.label_55 = QLabel(self.groupBox_2)
        self.label_55.setObjectName("label_55")

        self.horizontalLayout_67.addWidget(self.label_55)

        self.horizontalSpacer_65 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_67.addItem(self.horizontalSpacer_65)

        self.label_general_fourd_explorer_version = QLabel(self.groupBox_2)
        self.label_general_fourd_explorer_version.setObjectName(
            "label_general_fourd_explorer_version"
        )

        self.horizontalLayout_67.addWidget(self.label_general_fourd_explorer_version)

        self.pushButton_edit_general_fourd_explorer_version = QPushButton(
            self.groupBox_2
        )
        self.pushButton_edit_general_fourd_explorer_version.setObjectName(
            "pushButton_edit_general_fourd_explorer_version"
        )

        self.horizontalLayout_67.addWidget(
            self.pushButton_edit_general_fourd_explorer_version
        )

        self.verticalLayout_2.addLayout(self.horizontalLayout_67)

        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_general)
        self.page_microscope = QWidget()
        self.page_microscope.setObjectName("page_microscope")
        self.verticalLayout_9 = QVBoxLayout(self.page_microscope)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.groupBox = QGroupBox(self.page_microscope)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_59.addWidget(self.label_5)

        self.horizontalSpacer_15 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_59.addItem(self.horizontalSpacer_15)

        self.label_microscope_name = QLabel(self.groupBox)
        self.label_microscope_name.setObjectName("label_microscope_name")

        self.horizontalLayout_59.addWidget(self.label_microscope_name)

        self.pushButton_edit_microscope_name = QPushButton(self.groupBox)
        self.pushButton_edit_microscope_name.setObjectName(
            "pushButton_edit_microscope_name"
        )

        self.horizontalLayout_59.addWidget(self.pushButton_edit_microscope_name)

        self.verticalLayout_5.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_58.addWidget(self.label_6)

        self.horizontalSpacer_54 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_58.addItem(self.horizontalSpacer_54)

        self.label_microscope_manufacturer = QLabel(self.groupBox)
        self.label_microscope_manufacturer.setObjectName(
            "label_microscope_manufacturer"
        )

        self.horizontalLayout_58.addWidget(self.label_microscope_manufacturer)

        self.pushButton_edit_microscope_manufacturer = QPushButton(self.groupBox)
        self.pushButton_edit_microscope_manufacturer.setObjectName(
            "pushButton_edit_microscope_manufacturer"
        )

        self.horizontalLayout_58.addWidget(self.pushButton_edit_microscope_manufacturer)

        self.verticalLayout_5.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")

        self.horizontalLayout_57.addWidget(self.label_16)

        self.horizontalSpacer_55 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_57.addItem(self.horizontalSpacer_55)

        self.label_acquisition_location = QLabel(self.groupBox)
        self.label_acquisition_location.setObjectName("label_acquisition_location")

        self.horizontalLayout_57.addWidget(self.label_acquisition_location)

        self.pushButton_edit_acquisition_location = QPushButton(self.groupBox)
        self.pushButton_edit_acquisition_location.setObjectName(
            "pushButton_edit_acquisition_location"
        )

        self.horizontalLayout_57.addWidget(self.pushButton_edit_acquisition_location)

        self.verticalLayout_5.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")

        self.horizontalLayout_15.addWidget(self.label_17)

        self.horizontalSpacer_56 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_15.addItem(self.horizontalSpacer_56)

        self.label_acquisition_timezone = QLabel(self.groupBox)
        self.label_acquisition_timezone.setObjectName("label_acquisition_timezone")

        self.horizontalLayout_15.addWidget(self.label_acquisition_timezone)

        self.pushButton_edit_acquisition_timezone = QPushButton(self.groupBox)
        self.pushButton_edit_acquisition_timezone.setObjectName(
            "pushButton_edit_acquisition_timezone"
        )

        self.horizontalLayout_15.addWidget(self.pushButton_edit_acquisition_timezone)

        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")

        self.horizontalLayout_16.addWidget(self.label_15)

        self.horizontalSpacer_13 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_16.addItem(self.horizontalSpacer_13)

        self.label_acquisition_date = QLabel(self.groupBox)
        self.label_acquisition_date.setObjectName("label_acquisition_date")

        self.horizontalLayout_16.addWidget(self.label_acquisition_date)

        self.pushButton_edit_acquisition_date = QPushButton(self.groupBox)
        self.pushButton_edit_acquisition_date.setObjectName(
            "pushButton_edit_acquisition_date"
        )

        self.horizontalLayout_16.addWidget(self.pushButton_edit_acquisition_date)

        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(
            18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.label_beam_current = QLabel(self.groupBox)
        self.label_beam_current.setObjectName("label_beam_current")

        self.horizontalLayout_7.addWidget(self.label_beam_current)

        self.pushButton_edit_beam_current = QPushButton(self.groupBox)
        self.pushButton_edit_beam_current.setObjectName("pushButton_edit_beam_current")

        self.horizontalLayout_7.addWidget(self.pushButton_edit_beam_current)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.label_accelerate_voltage = QLabel(self.groupBox)
        self.label_accelerate_voltage.setObjectName("label_accelerate_voltage")

        self.horizontalLayout_8.addWidget(self.label_accelerate_voltage)

        self.pushButton_edit_accelerate_voltage = QPushButton(self.groupBox)
        self.pushButton_edit_accelerate_voltage.setObjectName(
            "pushButton_edit_accelerate_voltage"
        )

        self.horizontalLayout_8.addWidget(self.pushButton_edit_accelerate_voltage)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.label_camera_length = QLabel(self.groupBox)
        self.label_camera_length.setObjectName("label_camera_length")

        self.horizontalLayout_9.addWidget(self.label_camera_length)

        self.pushButton_edit_camera_length = QPushButton(self.groupBox)
        self.pushButton_edit_camera_length.setObjectName(
            "pushButton_edit_camera_length"
        )

        self.horizontalLayout_9.addWidget(self.pushButton_edit_camera_length)

        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.label_convergence_angle = QLabel(self.groupBox)
        self.label_convergence_angle.setObjectName("label_convergence_angle")

        self.horizontalLayout_10.addWidget(self.label_convergence_angle)

        self.pushButton_edit_convergent_angle = QPushButton(self.groupBox)
        self.pushButton_edit_convergent_angle.setObjectName(
            "pushButton_edit_convergent_angle"
        )

        self.horizontalLayout_10.addWidget(self.pushButton_edit_convergent_angle)

        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.label_magnification = QLabel(self.groupBox)
        self.label_magnification.setObjectName("label_magnification")

        self.horizontalLayout_11.addWidget(self.label_magnification)

        self.pushButton_edit_magnification = QPushButton(self.groupBox)
        self.pushButton_edit_magnification.setObjectName(
            "pushButton_edit_magnification"
        )

        self.horizontalLayout_11.addWidget(self.pushButton_edit_magnification)

        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.horizontalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)

        self.label_dwell_time = QLabel(self.groupBox)
        self.label_dwell_time.setObjectName("label_dwell_time")

        self.horizontalLayout_12.addWidget(self.label_dwell_time)

        self.pushButton_edit_dwell_time = QPushButton(self.groupBox)
        self.pushButton_edit_dwell_time.setObjectName("pushButton_edit_dwell_time")

        self.horizontalLayout_12.addWidget(self.pushButton_edit_dwell_time)

        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")

        self.horizontalLayout_13.addWidget(self.label_14)

        self.horizontalSpacer_11 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.label_step_size_i = QLabel(self.groupBox)
        self.label_step_size_i.setObjectName("label_step_size_i")

        self.horizontalLayout_13.addWidget(self.label_step_size_i)

        self.pushButton_edit_step_size_i = QPushButton(self.groupBox)
        self.pushButton_edit_step_size_i.setObjectName("pushButton_edit_step_size_i")

        self.horizontalLayout_13.addWidget(self.pushButton_edit_step_size_i)

        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.horizontalSpacer_12 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_14.addItem(self.horizontalSpacer_12)

        self.label_step_size_j = QLabel(self.groupBox)
        self.label_step_size_j.setObjectName("label_step_size_j")

        self.horizontalLayout_14.addWidget(self.label_step_size_j)

        self.pushButton_edit_step_size_j = QPushButton(self.groupBox)
        self.pushButton_edit_step_size_j.setObjectName("pushButton_edit_step_size_j")

        self.horizontalLayout_14.addWidget(self.pushButton_edit_step_size_j)

        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.verticalLayout_9.addWidget(self.groupBox)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page_microscope)
        self.page_camera = QWidget()
        self.page_camera.setObjectName("page_camera")
        self.verticalLayout_7 = QVBoxLayout(self.page_camera)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_3 = QGroupBox(self.page_camera)
        self.groupBox_3.setObjectName("groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName("label_18")

        self.horizontalLayout_21.addWidget(self.label_18)

        self.horizontalSpacer_57 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_21.addItem(self.horizontalSpacer_57)

        self.label_camera_name = QLabel(self.groupBox_3)
        self.label_camera_name.setObjectName("label_camera_name")

        self.horizontalLayout_21.addWidget(self.label_camera_name)

        self.pushButton_edit_camera_name = QPushButton(self.groupBox_3)
        self.pushButton_edit_camera_name.setObjectName("pushButton_edit_camera_name")

        self.horizontalLayout_21.addWidget(self.pushButton_edit_camera_name)

        self.verticalLayout_6.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName("label_19")

        self.horizontalLayout_60.addWidget(self.label_19)

        self.horizontalSpacer_19 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_60.addItem(self.horizontalSpacer_19)

        self.label_camera_manufacturer = QLabel(self.groupBox_3)
        self.label_camera_manufacturer.setObjectName("label_camera_manufacturer")

        self.horizontalLayout_60.addWidget(self.label_camera_manufacturer)

        self.pushButton_edit_camera_manufacturer = QPushButton(self.groupBox_3)
        self.pushButton_edit_camera_manufacturer.setObjectName(
            "pushButton_edit_camera_manufacturer"
        )

        self.horizontalLayout_60.addWidget(self.pushButton_edit_camera_manufacturer)

        self.verticalLayout_6.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName("label_20")

        self.horizontalLayout_17.addWidget(self.label_20)

        self.horizontalSpacer_14 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_17.addItem(self.horizontalSpacer_14)

        self.label_camera_pixel_number_i = QLabel(self.groupBox_3)
        self.label_camera_pixel_number_i.setObjectName("label_camera_pixel_number_i")

        self.horizontalLayout_17.addWidget(self.label_camera_pixel_number_i)

        self.pushButton_pixel_number_i = QPushButton(self.groupBox_3)
        self.pushButton_pixel_number_i.setObjectName("pushButton_pixel_number_i")

        self.horizontalLayout_17.addWidget(self.pushButton_pixel_number_i)

        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName("label_21")

        self.horizontalLayout_18.addWidget(self.label_21)

        self.horizontalSpacer_16 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_18.addItem(self.horizontalSpacer_16)

        self.label_camera_pixel_number_j = QLabel(self.groupBox_3)
        self.label_camera_pixel_number_j.setObjectName("label_camera_pixel_number_j")

        self.horizontalLayout_18.addWidget(self.label_camera_pixel_number_j)

        self.pushButton_pixel_number_j = QPushButton(self.groupBox_3)
        self.pushButton_pixel_number_j.setObjectName("pushButton_pixel_number_j")

        self.horizontalLayout_18.addWidget(self.pushButton_pixel_number_j)

        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName("label_22")

        self.horizontalLayout_19.addWidget(self.label_22)

        self.horizontalSpacer_17 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_19.addItem(self.horizontalSpacer_17)

        self.label_camera_pixel_size_i = QLabel(self.groupBox_3)
        self.label_camera_pixel_size_i.setObjectName("label_camera_pixel_size_i")

        self.horizontalLayout_19.addWidget(self.label_camera_pixel_size_i)

        self.pushButton_edit_camera_pixel_size_i = QPushButton(self.groupBox_3)
        self.pushButton_edit_camera_pixel_size_i.setObjectName(
            "pushButton_edit_camera_pixel_size_i"
        )

        self.horizontalLayout_19.addWidget(self.pushButton_edit_camera_pixel_size_i)

        self.verticalLayout_6.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName("label_23")

        self.horizontalLayout_20.addWidget(self.label_23)

        self.horizontalSpacer_18 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_20.addItem(self.horizontalSpacer_18)

        self.label_camera_pixel_size_j = QLabel(self.groupBox_3)
        self.label_camera_pixel_size_j.setObjectName("label_camera_pixel_size_j")

        self.horizontalLayout_20.addWidget(self.label_camera_pixel_size_j)

        self.pushButton_edit_camera_pixel_size_j = QPushButton(self.groupBox_3)
        self.pushButton_edit_camera_pixel_size_j.setObjectName(
            "pushButton_edit_camera_pixel_size_j"
        )

        self.horizontalLayout_20.addWidget(self.pushButton_edit_camera_pixel_size_j)

        self.verticalLayout_6.addLayout(self.horizontalLayout_20)

        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_camera)
        self.page_space = QWidget()
        self.page_space.setObjectName("page_space")
        self.verticalLayout_17 = QVBoxLayout(self.page_space)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, 0, -1)
        self.groupBox_4 = QGroupBox(self.page_space)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_24 = QLabel(self.groupBox_4)
        self.label_24.setObjectName("label_24")

        self.horizontalLayout_27.addWidget(self.label_24)

        self.horizontalSpacer_20 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_27.addItem(self.horizontalSpacer_20)

        self.label_du_i = QLabel(self.groupBox_4)
        self.label_du_i.setObjectName("label_du_i")

        self.horizontalLayout_27.addWidget(self.label_du_i)

        self.pushButton_edit_du_i = QPushButton(self.groupBox_4)
        self.pushButton_edit_du_i.setObjectName("pushButton_edit_du_i")

        self.horizontalLayout_27.addWidget(self.pushButton_edit_du_i)

        self.verticalLayout_16.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_25 = QLabel(self.groupBox_4)
        self.label_25.setObjectName("label_25")

        self.horizontalLayout_26.addWidget(self.label_25)

        self.horizontalSpacer_21 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_26.addItem(self.horizontalSpacer_21)

        self.label_du_j = QLabel(self.groupBox_4)
        self.label_du_j.setObjectName("label_du_j")

        self.horizontalLayout_26.addWidget(self.label_du_j)

        self.pushButton_edit_du_j = QPushButton(self.groupBox_4)
        self.pushButton_edit_du_j.setObjectName("pushButton_edit_du_j")

        self.horizontalLayout_26.addWidget(self.pushButton_edit_du_j)

        self.verticalLayout_16.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_28 = QLabel(self.groupBox_4)
        self.label_28.setObjectName("label_28")

        self.horizontalLayout_25.addWidget(self.label_28)

        self.horizontalSpacer_22 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_25.addItem(self.horizontalSpacer_22)

        self.label_dr_i = QLabel(self.groupBox_4)
        self.label_dr_i.setObjectName("label_dr_i")

        self.horizontalLayout_25.addWidget(self.label_dr_i)

        self.pushButton_edit_dr_i = QPushButton(self.groupBox_4)
        self.pushButton_edit_dr_i.setObjectName("pushButton_edit_dr_i")

        self.horizontalLayout_25.addWidget(self.pushButton_edit_dr_i)

        self.verticalLayout_16.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_29 = QLabel(self.groupBox_4)
        self.label_29.setObjectName("label_29")

        self.horizontalLayout_24.addWidget(self.label_29)

        self.horizontalSpacer_23 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_24.addItem(self.horizontalSpacer_23)

        self.label_dr_j = QLabel(self.groupBox_4)
        self.label_dr_j.setObjectName("label_dr_j")

        self.horizontalLayout_24.addWidget(self.label_dr_j)

        self.pushButton_edit_dr_j = QPushButton(self.groupBox_4)
        self.pushButton_edit_dr_j.setObjectName("pushButton_edit_dr_j")

        self.horizontalLayout_24.addWidget(self.pushButton_edit_dr_j)

        self.verticalLayout_16.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_26 = QLabel(self.groupBox_4)
        self.label_26.setObjectName("label_26")

        self.horizontalLayout_23.addWidget(self.label_26)

        self.horizontalSpacer_24 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_23.addItem(self.horizontalSpacer_24)

        self.label_scan_dr_i = QLabel(self.groupBox_4)
        self.label_scan_dr_i.setObjectName("label_scan_dr_i")

        self.horizontalLayout_23.addWidget(self.label_scan_dr_i)

        self.pushButton_edit_scan_dr_i = QPushButton(self.groupBox_4)
        self.pushButton_edit_scan_dr_i.setObjectName("pushButton_edit_scan_dr_i")

        self.horizontalLayout_23.addWidget(self.pushButton_edit_scan_dr_i)

        self.verticalLayout_16.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_27 = QLabel(self.groupBox_4)
        self.label_27.setObjectName("label_27")

        self.horizontalLayout_22.addWidget(self.label_27)

        self.horizontalSpacer_25 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_22.addItem(self.horizontalSpacer_25)

        self.label_scan_dr_j = QLabel(self.groupBox_4)
        self.label_scan_dr_j.setObjectName("label_scan_dr_j")

        self.horizontalLayout_22.addWidget(self.label_scan_dr_j)

        self.pushButton_edit_scan_dr_j = QPushButton(self.groupBox_4)
        self.pushButton_edit_scan_dr_j.setObjectName("pushButton_edit_scan_dr_j")

        self.horizontalLayout_22.addWidget(self.pushButton_edit_scan_dr_j)

        self.verticalLayout_16.addLayout(self.horizontalLayout_22)

        self.verticalLayout_17.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.page_space)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_30 = QLabel(self.groupBox_5)
        self.label_30.setObjectName("label_30")

        self.horizontalLayout_28.addWidget(self.label_30)

        self.horizontalSpacer_26 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_28.addItem(self.horizontalSpacer_26)

        self.label_scan_i = QLabel(self.groupBox_5)
        self.label_scan_i.setObjectName("label_scan_i")

        self.horizontalLayout_28.addWidget(self.label_scan_i)

        self.verticalLayout_15.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_31 = QLabel(self.groupBox_5)
        self.label_31.setObjectName("label_31")

        self.horizontalLayout_29.addWidget(self.label_31)

        self.horizontalSpacer_27 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_29.addItem(self.horizontalSpacer_27)

        self.label_scan_j = QLabel(self.groupBox_5)
        self.label_scan_j.setObjectName("label_scan_j")

        self.horizontalLayout_29.addWidget(self.label_scan_j)

        self.verticalLayout_15.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_32 = QLabel(self.groupBox_5)
        self.label_32.setObjectName("label_32")

        self.horizontalLayout_30.addWidget(self.label_32)

        self.horizontalSpacer_28 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_30.addItem(self.horizontalSpacer_28)

        self.label_dp_i = QLabel(self.groupBox_5)
        self.label_dp_i.setObjectName("label_dp_i")

        self.horizontalLayout_30.addWidget(self.label_dp_i)

        self.verticalLayout_15.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_33 = QLabel(self.groupBox_5)
        self.label_33.setObjectName("label_33")

        self.horizontalLayout_31.addWidget(self.label_33)

        self.horizontalSpacer_29 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_31.addItem(self.horizontalSpacer_29)

        self.label_dp_j = QLabel(self.groupBox_5)
        self.label_dp_j.setObjectName("label_dp_j")

        self.horizontalLayout_31.addWidget(self.label_dp_j)

        self.verticalLayout_15.addLayout(self.horizontalLayout_31)

        self.verticalLayout_17.addWidget(self.groupBox_5)

        self.verticalSpacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_17.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.page_space)
        self.page_low_order_aberration = QWidget()
        self.page_low_order_aberration.setObjectName("page_low_order_aberration")
        self.verticalLayout_20 = QVBoxLayout(self.page_low_order_aberration)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, -1, 0, -1)
        self.groupBox_6 = QGroupBox(self.page_low_order_aberration)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_34 = QLabel(self.groupBox_6)
        self.label_34.setObjectName("label_34")

        self.horizontalLayout_32.addWidget(self.label_34)

        self.horizontalSpacer_30 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_32.addItem(self.horizontalSpacer_30)

        self.label_C1 = QLabel(self.groupBox_6)
        self.label_C1.setObjectName("label_C1")

        self.horizontalLayout_32.addWidget(self.label_C1)

        self.pushButton_edit_C1 = QPushButton(self.groupBox_6)
        self.pushButton_edit_C1.setObjectName("pushButton_edit_C1")

        self.horizontalLayout_32.addWidget(self.pushButton_edit_C1)

        self.verticalLayout_18.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_35 = QLabel(self.groupBox_6)
        self.label_35.setObjectName("label_35")

        self.horizontalLayout_33.addWidget(self.label_35)

        self.horizontalSpacer_31 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_33.addItem(self.horizontalSpacer_31)

        self.label_A1 = QLabel(self.groupBox_6)
        self.label_A1.setObjectName("label_A1")

        self.horizontalLayout_33.addWidget(self.label_A1)

        self.pushButton_edit_A1 = QPushButton(self.groupBox_6)
        self.pushButton_edit_A1.setObjectName("pushButton_edit_A1")

        self.horizontalLayout_33.addWidget(self.pushButton_edit_A1)

        self.verticalLayout_18.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_37 = QLabel(self.groupBox_6)
        self.label_37.setObjectName("label_37")

        self.horizontalLayout_34.addWidget(self.label_37)

        self.horizontalSpacer_32 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_34.addItem(self.horizontalSpacer_32)

        self.label_B2 = QLabel(self.groupBox_6)
        self.label_B2.setObjectName("label_B2")

        self.horizontalLayout_34.addWidget(self.label_B2)

        self.pushButton_edit_B2 = QPushButton(self.groupBox_6)
        self.pushButton_edit_B2.setObjectName("pushButton_edit_B2")

        self.horizontalLayout_34.addWidget(self.pushButton_edit_B2)

        self.verticalLayout_18.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_39 = QLabel(self.groupBox_6)
        self.label_39.setObjectName("label_39")

        self.horizontalLayout_35.addWidget(self.label_39)

        self.horizontalSpacer_33 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_35.addItem(self.horizontalSpacer_33)

        self.label_A2 = QLabel(self.groupBox_6)
        self.label_A2.setObjectName("label_A2")

        self.horizontalLayout_35.addWidget(self.label_A2)

        self.pushButton_edit_A2 = QPushButton(self.groupBox_6)
        self.pushButton_edit_A2.setObjectName("pushButton_edit_A2")

        self.horizontalLayout_35.addWidget(self.pushButton_edit_A2)

        self.verticalLayout_18.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_41 = QLabel(self.groupBox_6)
        self.label_41.setObjectName("label_41")

        self.horizontalLayout_36.addWidget(self.label_41)

        self.horizontalSpacer_34 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_36.addItem(self.horizontalSpacer_34)

        self.label_C3 = QLabel(self.groupBox_6)
        self.label_C3.setObjectName("label_C3")

        self.horizontalLayout_36.addWidget(self.label_C3)

        self.pushButton_edit_C3 = QPushButton(self.groupBox_6)
        self.pushButton_edit_C3.setObjectName("pushButton_edit_C3")

        self.horizontalLayout_36.addWidget(self.pushButton_edit_C3)

        self.verticalLayout_18.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_43 = QLabel(self.groupBox_6)
        self.label_43.setObjectName("label_43")

        self.horizontalLayout_37.addWidget(self.label_43)

        self.horizontalSpacer_35 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_37.addItem(self.horizontalSpacer_35)

        self.label_S3 = QLabel(self.groupBox_6)
        self.label_S3.setObjectName("label_S3")

        self.horizontalLayout_37.addWidget(self.label_S3)

        self.pushButton_edit_S3 = QPushButton(self.groupBox_6)
        self.pushButton_edit_S3.setObjectName("pushButton_edit_S3")

        self.horizontalLayout_37.addWidget(self.pushButton_edit_S3)

        self.verticalLayout_18.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_45 = QLabel(self.groupBox_6)
        self.label_45.setObjectName("label_45")

        self.horizontalLayout_38.addWidget(self.label_45)

        self.horizontalSpacer_36 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_38.addItem(self.horizontalSpacer_36)

        self.label_A3 = QLabel(self.groupBox_6)
        self.label_A3.setObjectName("label_A3")

        self.horizontalLayout_38.addWidget(self.label_A3)

        self.pushButton_edit_A3 = QPushButton(self.groupBox_6)
        self.pushButton_edit_A3.setObjectName("pushButton_edit_A3")

        self.horizontalLayout_38.addWidget(self.pushButton_edit_A3)

        self.verticalLayout_18.addLayout(self.horizontalLayout_38)

        self.verticalLayout_20.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.page_low_order_aberration)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_47 = QLabel(self.groupBox_7)
        self.label_47.setObjectName("label_47")

        self.verticalLayout_19.addWidget(self.label_47)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_54 = QLabel(self.groupBox_7)
        self.label_54.setObjectName("label_54")

        self.horizontalLayout_39.addWidget(self.label_54)

        self.horizontalSpacer_37 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_39.addItem(self.horizontalSpacer_37)

        self.label_C1_angle = QLabel(self.groupBox_7)
        self.label_C1_angle.setObjectName("label_C1_angle")

        self.horizontalLayout_39.addWidget(self.label_C1_angle)

        self.pushButton_edit_C1_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_C1_angle.setObjectName("pushButton_edit_C1_angle")

        self.horizontalLayout_39.addWidget(self.pushButton_edit_C1_angle)

        self.verticalLayout_19.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_36 = QLabel(self.groupBox_7)
        self.label_36.setObjectName("label_36")

        self.horizontalLayout_40.addWidget(self.label_36)

        self.horizontalSpacer_38 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_40.addItem(self.horizontalSpacer_38)

        self.label_A1_angle = QLabel(self.groupBox_7)
        self.label_A1_angle.setObjectName("label_A1_angle")

        self.horizontalLayout_40.addWidget(self.label_A1_angle)

        self.pushButton_edit_A1_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_A1_angle.setObjectName("pushButton_edit_A1_angle")

        self.horizontalLayout_40.addWidget(self.pushButton_edit_A1_angle)

        self.verticalLayout_19.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_38 = QLabel(self.groupBox_7)
        self.label_38.setObjectName("label_38")

        self.horizontalLayout_41.addWidget(self.label_38)

        self.horizontalSpacer_39 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_41.addItem(self.horizontalSpacer_39)

        self.label_B2_angle = QLabel(self.groupBox_7)
        self.label_B2_angle.setObjectName("label_B2_angle")

        self.horizontalLayout_41.addWidget(self.label_B2_angle)

        self.pushButton_edit_B2_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_B2_angle.setObjectName("pushButton_edit_B2_angle")

        self.horizontalLayout_41.addWidget(self.pushButton_edit_B2_angle)

        self.verticalLayout_19.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.label_40 = QLabel(self.groupBox_7)
        self.label_40.setObjectName("label_40")

        self.horizontalLayout_42.addWidget(self.label_40)

        self.horizontalSpacer_40 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_42.addItem(self.horizontalSpacer_40)

        self.label_A2_angle = QLabel(self.groupBox_7)
        self.label_A2_angle.setObjectName("label_A2_angle")

        self.horizontalLayout_42.addWidget(self.label_A2_angle)

        self.pushButton_edit_A2_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_A2_angle.setObjectName("pushButton_edit_A2_angle")

        self.horizontalLayout_42.addWidget(self.pushButton_edit_A2_angle)

        self.verticalLayout_19.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.label_42 = QLabel(self.groupBox_7)
        self.label_42.setObjectName("label_42")

        self.horizontalLayout_43.addWidget(self.label_42)

        self.horizontalSpacer_41 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_43.addItem(self.horizontalSpacer_41)

        self.label_C3_angle = QLabel(self.groupBox_7)
        self.label_C3_angle.setObjectName("label_C3_angle")

        self.horizontalLayout_43.addWidget(self.label_C3_angle)

        self.pushButton_edit_C3_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_C3_angle.setObjectName("pushButton_edit_C3_angle")

        self.horizontalLayout_43.addWidget(self.pushButton_edit_C3_angle)

        self.verticalLayout_19.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.label_44 = QLabel(self.groupBox_7)
        self.label_44.setObjectName("label_44")

        self.horizontalLayout_44.addWidget(self.label_44)

        self.horizontalSpacer_42 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_44.addItem(self.horizontalSpacer_42)

        self.label_S3_angle = QLabel(self.groupBox_7)
        self.label_S3_angle.setObjectName("label_S3_angle")

        self.horizontalLayout_44.addWidget(self.label_S3_angle)

        self.pushButton_edit_S3_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_S3_angle.setObjectName("pushButton_edit_S3_angle")

        self.horizontalLayout_44.addWidget(self.pushButton_edit_S3_angle)

        self.verticalLayout_19.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.label_46 = QLabel(self.groupBox_7)
        self.label_46.setObjectName("label_46")

        self.horizontalLayout_45.addWidget(self.label_46)

        self.horizontalSpacer_43 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_45.addItem(self.horizontalSpacer_43)

        self.label_A3_angle = QLabel(self.groupBox_7)
        self.label_A3_angle.setObjectName("label_A3_angle")

        self.horizontalLayout_45.addWidget(self.label_A3_angle)

        self.pushButton_edit_A3_angle = QPushButton(self.groupBox_7)
        self.pushButton_edit_A3_angle.setObjectName("pushButton_edit_A3_angle")

        self.horizontalLayout_45.addWidget(self.pushButton_edit_A3_angle)

        self.verticalLayout_19.addLayout(self.horizontalLayout_45)

        self.verticalLayout_20.addWidget(self.groupBox_7)

        self.verticalSpacer_5 = QSpacerItem(
            20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_20.addItem(self.verticalSpacer_5)

        self.stackedWidget.addWidget(self.page_low_order_aberration)
        self.page_high_order_aberration = QWidget()
        self.page_high_order_aberration.setObjectName("page_high_order_aberration")
        self.verticalLayout_23 = QVBoxLayout(self.page_high_order_aberration)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, -1, 0, -1)
        self.groupBox_8 = QGroupBox(self.page_high_order_aberration)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.label_56 = QLabel(self.groupBox_8)
        self.label_56.setObjectName("label_56")

        self.horizontalLayout_51.addWidget(self.label_56)

        self.horizontalSpacer_49 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_51.addItem(self.horizontalSpacer_49)

        self.label_B4 = QLabel(self.groupBox_8)
        self.label_B4.setObjectName("label_B4")

        self.horizontalLayout_51.addWidget(self.label_B4)

        self.pushButton_edit_B4 = QPushButton(self.groupBox_8)
        self.pushButton_edit_B4.setObjectName("pushButton_edit_B4")

        self.horizontalLayout_51.addWidget(self.pushButton_edit_B4)

        self.verticalLayout_21.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.label_57 = QLabel(self.groupBox_8)
        self.label_57.setObjectName("label_57")

        self.horizontalLayout_52.addWidget(self.label_57)

        self.horizontalSpacer_50 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_52.addItem(self.horizontalSpacer_50)

        self.label_D4 = QLabel(self.groupBox_8)
        self.label_D4.setObjectName("label_D4")

        self.horizontalLayout_52.addWidget(self.label_D4)

        self.pushButton_edit_D4 = QPushButton(self.groupBox_8)
        self.pushButton_edit_D4.setObjectName("pushButton_edit_D4")

        self.horizontalLayout_52.addWidget(self.pushButton_edit_D4)

        self.verticalLayout_21.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.label_58 = QLabel(self.groupBox_8)
        self.label_58.setObjectName("label_58")

        self.horizontalLayout_53.addWidget(self.label_58)

        self.horizontalSpacer_51 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_53.addItem(self.horizontalSpacer_51)

        self.label_A4 = QLabel(self.groupBox_8)
        self.label_A4.setObjectName("label_A4")

        self.horizontalLayout_53.addWidget(self.label_A4)

        self.pushButton_edit_A4 = QPushButton(self.groupBox_8)
        self.pushButton_edit_A4.setObjectName("pushButton_edit_A4")

        self.horizontalLayout_53.addWidget(self.pushButton_edit_A4)

        self.verticalLayout_21.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.label_59 = QLabel(self.groupBox_8)
        self.label_59.setObjectName("label_59")

        self.horizontalLayout_54.addWidget(self.label_59)

        self.horizontalSpacer_52 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_54.addItem(self.horizontalSpacer_52)

        self.label_C5 = QLabel(self.groupBox_8)
        self.label_C5.setObjectName("label_C5")

        self.horizontalLayout_54.addWidget(self.label_C5)

        self.pushButton_edit_C5 = QPushButton(self.groupBox_8)
        self.pushButton_edit_C5.setObjectName("pushButton_edit_C5")

        self.horizontalLayout_54.addWidget(self.pushButton_edit_C5)

        self.verticalLayout_21.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.label_60 = QLabel(self.groupBox_8)
        self.label_60.setObjectName("label_60")

        self.horizontalLayout_55.addWidget(self.label_60)

        self.horizontalSpacer_53 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_55.addItem(self.horizontalSpacer_53)

        self.label_A5 = QLabel(self.groupBox_8)
        self.label_A5.setObjectName("label_A5")

        self.horizontalLayout_55.addWidget(self.label_A5)

        self.pushButton_edit_A5 = QPushButton(self.groupBox_8)
        self.pushButton_edit_A5.setObjectName("pushButton_edit_A5")

        self.horizontalLayout_55.addWidget(self.pushButton_edit_A5)

        self.verticalLayout_21.addLayout(self.horizontalLayout_55)

        self.verticalLayout_23.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.page_high_order_aberration)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.label_61 = QLabel(self.groupBox_9)
        self.label_61.setObjectName("label_61")

        self.horizontalLayout_46.addWidget(self.label_61)

        self.horizontalSpacer_44 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_46.addItem(self.horizontalSpacer_44)

        self.label_B4_angle = QLabel(self.groupBox_9)
        self.label_B4_angle.setObjectName("label_B4_angle")

        self.horizontalLayout_46.addWidget(self.label_B4_angle)

        self.pushButton_edit_B4_angle = QPushButton(self.groupBox_9)
        self.pushButton_edit_B4_angle.setObjectName("pushButton_edit_B4_angle")

        self.horizontalLayout_46.addWidget(self.pushButton_edit_B4_angle)

        self.verticalLayout_22.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.label_62 = QLabel(self.groupBox_9)
        self.label_62.setObjectName("label_62")

        self.horizontalLayout_47.addWidget(self.label_62)

        self.horizontalSpacer_45 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_47.addItem(self.horizontalSpacer_45)

        self.label_D4_angle = QLabel(self.groupBox_9)
        self.label_D4_angle.setObjectName("label_D4_angle")

        self.horizontalLayout_47.addWidget(self.label_D4_angle)

        self.pushButton_edit_D4_angle = QPushButton(self.groupBox_9)
        self.pushButton_edit_D4_angle.setObjectName("pushButton_edit_D4_angle")

        self.horizontalLayout_47.addWidget(self.pushButton_edit_D4_angle)

        self.verticalLayout_22.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.label_63 = QLabel(self.groupBox_9)
        self.label_63.setObjectName("label_63")

        self.horizontalLayout_48.addWidget(self.label_63)

        self.horizontalSpacer_46 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_48.addItem(self.horizontalSpacer_46)

        self.label_A4_angle = QLabel(self.groupBox_9)
        self.label_A4_angle.setObjectName("label_A4_angle")

        self.horizontalLayout_48.addWidget(self.label_A4_angle)

        self.pushButton_edit_A4_angle = QPushButton(self.groupBox_9)
        self.pushButton_edit_A4_angle.setObjectName("pushButton_edit_A4_angle")

        self.horizontalLayout_48.addWidget(self.pushButton_edit_A4_angle)

        self.verticalLayout_22.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.label_64 = QLabel(self.groupBox_9)
        self.label_64.setObjectName("label_64")

        self.horizontalLayout_49.addWidget(self.label_64)

        self.horizontalSpacer_48 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_49.addItem(self.horizontalSpacer_48)

        self.label_C5_angle = QLabel(self.groupBox_9)
        self.label_C5_angle.setObjectName("label_C5_angle")

        self.horizontalLayout_49.addWidget(self.label_C5_angle)

        self.pushButton_edit_C5_angle = QPushButton(self.groupBox_9)
        self.pushButton_edit_C5_angle.setObjectName("pushButton_edit_C5_angle")

        self.horizontalLayout_49.addWidget(self.pushButton_edit_C5_angle)

        self.verticalLayout_22.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.label_65 = QLabel(self.groupBox_9)
        self.label_65.setObjectName("label_65")

        self.horizontalLayout_50.addWidget(self.label_65)

        self.horizontalSpacer_47 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_50.addItem(self.horizontalSpacer_47)

        self.label_A5_angle = QLabel(self.groupBox_9)
        self.label_A5_angle.setObjectName("label_A5_angle")

        self.horizontalLayout_50.addWidget(self.label_A5_angle)

        self.pushButton_edit_A5_angle = QPushButton(self.groupBox_9)
        self.pushButton_edit_A5_angle.setObjectName("pushButton_edit_A5_angle")

        self.horizontalLayout_50.addWidget(self.pushButton_edit_A5_angle)

        self.verticalLayout_22.addLayout(self.horizontalLayout_50)

        self.verticalLayout_23.addWidget(self.groupBox_9)

        self.verticalSpacer_6 = QSpacerItem(
            20, 165, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_23.addItem(self.verticalSpacer_6)

        self.stackedWidget.addWidget(self.page_high_order_aberration)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName("pushButton_ok")

        self.horizontalLayout_4.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.horizontalLayout_4.addWidget(self.pushButton_cancel)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.label_71.setText(
            QCoreApplication.translate("Dialog", "4D-STEM path", None)
        )
        self.pushButton_browse.setText(
            QCoreApplication.translate("Dialog", "Browse", None)
        )
        self.label.setText(QCoreApplication.translate("Dialog", "Steps:", None))
        self.label_steps.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_back.setText(
            QCoreApplication.translate("Dialog", "\u2190 Back", None)
        )
        self.pushButton_next.setText(
            QCoreApplication.translate("Dialog", "Next \u2192", None)
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("Dialog", "Basic Information", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("Dialog", "Dataset Title", None)
        )
        self.label_general_title.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_general_title.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_48.setText(
            QCoreApplication.translate("Dialog", "Original Dataset Path", None)
        )
        self.label_general_data_path.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_general_data_path.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_49.setText(
            QCoreApplication.translate("Dialog", "Original Header Path", None)
        )
        self.label_general_header_path.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_general_header_path.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_50.setText(
            QCoreApplication.translate("Dialog", "Created Time", None)
        )
        self.label_general_time.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_general_time.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_51.setText(
            QCoreApplication.translate("Dialog", "Created Date", None)
        )
        self.label_general_date.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_general_date.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_52.setText(
            QCoreApplication.translate("Dialog", "Created Time Zone", None)
        )
        self.label_general_time_zone.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_general_time_zone.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_53.setText(QCoreApplication.translate("Dialog", "DOI", None))
        self.label_general_doi.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_general_doi.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_3.setText(QCoreApplication.translate("Dialog", "Authors", None))
        self.label_general_authors.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_general_authors.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_4.setText(QCoreApplication.translate("Dialog", "Notes", None))
        self.label_general_notes.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_general_notes.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_55.setText(
            QCoreApplication.translate("Dialog", "4D-Explorer Version", None)
        )
        self.label_general_fourd_explorer_version.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_general_fourd_explorer_version.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", "Microscope", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", "Name", None))
        self.label_microscope_name.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_microscope_name.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_6.setText(QCoreApplication.translate("Dialog", "Manufacturer", None))
        self.label_microscope_manufacturer.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_microscope_manufacturer.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_16.setText(
            QCoreApplication.translate("Dialog", "Acquisition Location", None)
        )
        self.label_acquisition_location.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_acquisition_location.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_17.setText(
            QCoreApplication.translate("Dialog", "Acquisition Timezone", None)
        )
        self.label_acquisition_timezone.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_acquisition_timezone.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_15.setText(
            QCoreApplication.translate("Dialog", "Acquisition Date", None)
        )
        self.label_acquisition_date.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_acquisition_date.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_7.setText(QCoreApplication.translate("Dialog", "Beam Current", None))
        self.label_beam_current.setText(
            QCoreApplication.translate("Dialog", "0 nA", None)
        )
        self.pushButton_edit_beam_current.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("Dialog", "Accelerate Voltage", None)
        )
        self.label_accelerate_voltage.setText(
            QCoreApplication.translate("Dialog", "0 kV", None)
        )
        self.pushButton_edit_accelerate_voltage.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_10.setText(
            QCoreApplication.translate("Dialog", "Camera Length", None)
        )
        self.label_camera_length.setText(
            QCoreApplication.translate("Dialog", "0 m", None)
        )
        self.pushButton_edit_camera_length.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("Dialog", "Convergence Angle", None)
        )
        self.label_convergence_angle.setText(
            QCoreApplication.translate("Dialog", "0 mrad", None)
        )
        self.pushButton_edit_convergent_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_11.setText(
            QCoreApplication.translate("Dialog", "Magnification", None)
        )
        self.label_magnification.setText(
            QCoreApplication.translate("Dialog", "0x", None)
        )
        self.pushButton_edit_magnification.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_12.setText(QCoreApplication.translate("Dialog", "Dwell Time", None))
        self.label_dwell_time.setText(
            QCoreApplication.translate("Dialog", "0 us", None)
        )
        self.pushButton_edit_dwell_time.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_14.setText(
            QCoreApplication.translate("Dialog", "Step Size (I Direction)", None)
        )
        self.label_step_size_i.setText(
            QCoreApplication.translate("Dialog", "0 nm", None)
        )
        self.pushButton_edit_step_size_i.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_13.setText(
            QCoreApplication.translate("Dialog", "Step Size (J Direction)", None)
        )
        self.label_step_size_j.setText(
            QCoreApplication.translate("Dialog", "0 nm", None)
        )
        self.pushButton_edit_step_size_j.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", "Camera", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", "Name", None))
        self.label_camera_name.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_camera_name.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_19.setText(
            QCoreApplication.translate("Dialog", "Manufacturer", None)
        )
        self.label_camera_manufacturer.setText(
            QCoreApplication.translate("Dialog", "TextLabel", None)
        )
        self.pushButton_edit_camera_manufacturer.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_20.setText(
            QCoreApplication.translate("Dialog", "Pixel Number (Height)", None)
        )
        self.label_camera_pixel_number_i.setText(
            QCoreApplication.translate("Dialog", "0", None)
        )
        self.pushButton_pixel_number_i.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_21.setText(
            QCoreApplication.translate("Dialog", "Pixel Number (Width)", None)
        )
        self.label_camera_pixel_number_j.setText(
            QCoreApplication.translate("Dialog", "0", None)
        )
        self.pushButton_pixel_number_j.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_22.setText(
            QCoreApplication.translate("Dialog", "Sensor Pixel Size (Height)", None)
        )
        self.label_camera_pixel_size_i.setText(
            QCoreApplication.translate("Dialog", "0 \u03bcm", None)
        )
        self.pushButton_edit_camera_pixel_size_i.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_23.setText(
            QCoreApplication.translate("Dialog", "Sensor Pixel Size (Width)", None)
        )
        self.label_camera_pixel_size_j.setText(
            QCoreApplication.translate("Dialog", "0 \u03bcm", None)
        )
        self.pushButton_edit_camera_pixel_size_j.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.groupBox_4.setTitle(
            QCoreApplication.translate("Dialog", "Calibrated Space Parameters", None)
        )
        self.label_24.setText(
            QCoreApplication.translate("Dialog", "\u0394u (I Direction)", None)
        )
        self.label_du_i.setText(QCoreApplication.translate("Dialog", "1 1/nm", None))
        self.pushButton_edit_du_i.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_25.setText(
            QCoreApplication.translate("Dialog", "\u0394u (J Direction)", None)
        )
        self.label_du_j.setText(QCoreApplication.translate("Dialog", "1 1/nm", None))
        self.pushButton_edit_du_j.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_28.setText(
            QCoreApplication.translate("Dialog", "\u0394r (I Direction)", None)
        )
        self.label_dr_i.setText(QCoreApplication.translate("Dialog", "1 nm", None))
        self.pushButton_edit_dr_i.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_29.setText(
            QCoreApplication.translate("Dialog", "\u0394r (J Direction)", None)
        )
        self.label_dr_j.setText(QCoreApplication.translate("Dialog", "1 nm", None))
        self.pushButton_edit_dr_j.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_26.setText(
            QCoreApplication.translate("Dialog", "Scanning \u0394r (I Direction)", None)
        )
        self.label_scan_dr_i.setText(QCoreApplication.translate("Dialog", "1 nm", None))
        self.pushButton_edit_scan_dr_i.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_27.setText(
            QCoreApplication.translate("Dialog", "Scanning \u0394r (J Direction)", None)
        )
        self.label_scan_dr_j.setText(QCoreApplication.translate("Dialog", "1 nm", None))
        self.pushButton_edit_scan_dr_j.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.groupBox_5.setTitle(
            QCoreApplication.translate("Dialog", "4D-STEM Dataset Shape", None)
        )
        self.label_30.setText(
            QCoreApplication.translate("Dialog", "Scanning Steps (I Direction)", None)
        )
        self.label_scan_i.setText(QCoreApplication.translate("Dialog", "1", None))
        self.label_31.setText(
            QCoreApplication.translate("Dialog", "Scanning Steps (J Direction)", None)
        )
        self.label_scan_j.setText(QCoreApplication.translate("Dialog", "1", None))
        self.label_32.setText(
            QCoreApplication.translate("Dialog", "Diffraction Pattern Height", None)
        )
        self.label_dp_i.setText(QCoreApplication.translate("Dialog", "1", None))
        self.label_33.setText(
            QCoreApplication.translate("Dialog", "Diffraction Pattern Width", None)
        )
        self.label_dp_j.setText(QCoreApplication.translate("Dialog", "1", None))
        self.groupBox_6.setTitle(
            QCoreApplication.translate(
                "Dialog", "Low Order Aberration Coefficients (Length)", None
            )
        )
        self.label_34.setText(QCoreApplication.translate("Dialog", "C1", None))
        self.label_C1.setText(QCoreApplication.translate("Dialog", "0 nm", None))
        self.pushButton_edit_C1.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_35.setText(QCoreApplication.translate("Dialog", "A1", None))
        self.label_A1.setText(QCoreApplication.translate("Dialog", "0 nm", None))
        self.pushButton_edit_A1.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_37.setText(QCoreApplication.translate("Dialog", "B2", None))
        self.label_B2.setText(QCoreApplication.translate("Dialog", "0 nm", None))
        self.pushButton_edit_B2.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_39.setText(QCoreApplication.translate("Dialog", "A2", None))
        self.label_A2.setText(QCoreApplication.translate("Dialog", "0 nm", None))
        self.pushButton_edit_A2.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_41.setText(QCoreApplication.translate("Dialog", "C3", None))
        self.label_C3.setText(QCoreApplication.translate("Dialog", "0 \u03bcm", None))
        self.pushButton_edit_C3.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_43.setText(QCoreApplication.translate("Dialog", "S3", None))
        self.label_S3.setText(QCoreApplication.translate("Dialog", "0 \u03bcm", None))
        self.pushButton_edit_S3.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_45.setText(QCoreApplication.translate("Dialog", "A3", None))
        self.label_A3.setText(QCoreApplication.translate("Dialog", "0 \u03bcm", None))
        self.pushButton_edit_A3.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.groupBox_7.setTitle(
            QCoreApplication.translate(
                "Dialog", "Low Order Aberration Coefficients (Angle)", None
            )
        )
        self.label_47.setText(
            QCoreApplication.translate("Dialog", "Defocus (C1) Angle", None)
        )
        self.label_54.setText(QCoreApplication.translate("Dialog", "C1", None))
        self.label_C1_angle.setText(QCoreApplication.translate("Dialog", "0 deg", None))
        self.pushButton_edit_C1_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_36.setText(QCoreApplication.translate("Dialog", "A1", None))
        self.label_A1_angle.setText(QCoreApplication.translate("Dialog", "0 deg", None))
        self.pushButton_edit_A1_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_38.setText(QCoreApplication.translate("Dialog", "B2", None))
        self.label_B2_angle.setText(QCoreApplication.translate("Dialog", "0 deg", None))
        self.pushButton_edit_B2_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_40.setText(QCoreApplication.translate("Dialog", "A2", None))
        self.label_A2_angle.setText(QCoreApplication.translate("Dialog", "0 deg", None))
        self.pushButton_edit_A2_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_42.setText(QCoreApplication.translate("Dialog", "C3", None))
        self.label_C3_angle.setText(QCoreApplication.translate("Dialog", "0 deg", None))
        self.pushButton_edit_C3_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_44.setText(QCoreApplication.translate("Dialog", "S3", None))
        self.label_S3_angle.setText(QCoreApplication.translate("Dialog", "0 deg", None))
        self.pushButton_edit_S3_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_46.setText(QCoreApplication.translate("Dialog", "A3", None))
        self.label_A3_angle.setText(QCoreApplication.translate("Dialog", "0 deg", None))
        self.pushButton_edit_A3_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.groupBox_8.setTitle(
            QCoreApplication.translate(
                "Dialog", "High Order Aberration Coefficients (Length)", None
            )
        )
        self.label_56.setText(QCoreApplication.translate("Dialog", "B4", None))
        self.label_B4.setText(QCoreApplication.translate("Dialog", "0 \u03bcm", None))
        self.pushButton_edit_B4.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_57.setText(QCoreApplication.translate("Dialog", "D4", None))
        self.label_D4.setText(QCoreApplication.translate("Dialog", "0 \u03bcm", None))
        self.pushButton_edit_D4.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_58.setText(QCoreApplication.translate("Dialog", "A4", None))
        self.label_A4.setText(QCoreApplication.translate("Dialog", "0 \u03bcm", None))
        self.pushButton_edit_A4.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_59.setText(QCoreApplication.translate("Dialog", "C5", None))
        self.label_C5.setText(QCoreApplication.translate("Dialog", "0 mm", None))
        self.pushButton_edit_C5.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_60.setText(QCoreApplication.translate("Dialog", "A5", None))
        self.label_A5.setText(QCoreApplication.translate("Dialog", "0 mm", None))
        self.pushButton_edit_A5.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.groupBox_9.setTitle(
            QCoreApplication.translate(
                "Dialog", "High Order Aberration Coefficients (Angle)", None
            )
        )
        self.label_61.setText(QCoreApplication.translate("Dialog", "B4", None))
        self.label_B4_angle.setText(QCoreApplication.translate("Dialog", "0 deg", None))
        self.pushButton_edit_B4_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_62.setText(QCoreApplication.translate("Dialog", "D4", None))
        self.label_D4_angle.setText(QCoreApplication.translate("Dialog", "0 deg", None))
        self.pushButton_edit_D4_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_63.setText(QCoreApplication.translate("Dialog", "A4", None))
        self.label_A4_angle.setText(QCoreApplication.translate("Dialog", "0 deg", None))
        self.pushButton_edit_A4_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_64.setText(QCoreApplication.translate("Dialog", "C5", None))
        self.label_C5_angle.setText(QCoreApplication.translate("Dialog", "0 deg", None))
        self.pushButton_edit_C5_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.label_65.setText(QCoreApplication.translate("Dialog", "A5", None))
        self.label_A5_angle.setText(QCoreApplication.translate("Dialog", "0 deg", None))
        self.pushButton_edit_A5_angle.setText(
            QCoreApplication.translate("Dialog", "Edit", None)
        )
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", "OK", None))
        self.pushButton_cancel.setText(
            QCoreApplication.translate("Dialog", "Cancel", None)
        )

    # retranslateUi
