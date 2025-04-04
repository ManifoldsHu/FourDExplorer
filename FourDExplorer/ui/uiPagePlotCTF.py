# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPagePlotCTF.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
    QComboBox,
    QDoubleSpinBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSplitter,
    QStackedWidget,
    QTabWidget,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from bin.Widgets.WidgetPlots import WidgetPlotImage, WidgetPlotLine


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1216, 1043)
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QLabel(Form)
        self.label.setObjectName("label")

        self.horizontalLayout_6.addWidget(self.label)

        self.lineEdit_config_path = QLineEdit(Form)
        self.lineEdit_config_path.setObjectName("lineEdit_config_path")

        self.horizontalLayout_6.addWidget(self.lineEdit_config_path)

        self.pushButton_browse_config = QPushButton(Form)
        self.pushButton_browse_config.setObjectName("pushButton_browse_config")

        self.horizontalLayout_6.addWidget(self.pushButton_browse_config)

        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.tabWidget_2 = QTabWidget(self.splitter)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_11 = QVBoxLayout(self.tab_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.widget_plot_ronchigram = WidgetPlotImage(self.tab_3)
        self.widget_plot_ronchigram.setObjectName("widget_plot_ronchigram")

        self.verticalLayout_11.addWidget(self.widget_plot_ronchigram)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_9 = QVBoxLayout(self.tab_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_plot_probe_abs = WidgetPlotImage(self.tab_4)
        self.widget_plot_probe_abs.setObjectName("widget_plot_probe_abs")

        self.verticalLayout_9.addWidget(self.widget_plot_probe_abs)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_12 = QVBoxLayout(self.tab_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget_plot_probe_angle = WidgetPlotImage(self.tab_5)
        self.widget_plot_probe_angle.setObjectName("widget_plot_probe_angle")

        self.verticalLayout_12.addWidget(self.widget_plot_probe_angle)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.splitter.addWidget(self.tabWidget_2)
        self.tabWidget_3 = QTabWidget(self.splitter)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName("tab_9")
        self.verticalLayout_28 = QVBoxLayout(self.tab_9)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.widget_plot_ctf_image = WidgetPlotImage(self.tab_9)
        self.widget_plot_ctf_image.setObjectName("widget_plot_ctf_image")

        self.verticalLayout_28.addWidget(self.widget_plot_ctf_image)

        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName("tab_10")
        self.verticalLayout_7 = QVBoxLayout(self.tab_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_plot_ctf_curve = WidgetPlotLine(self.tab_10)
        self.widget_plot_ctf_curve.setObjectName("widget_plot_ctf_curve")

        self.verticalLayout_7.addWidget(self.widget_plot_ctf_curve)

        self.tabWidget_3.addTab(self.tab_10, "")
        self.splitter.addWidget(self.tabWidget_3)
        self.splitter_2.addWidget(self.splitter)
        self.tabWidget = QTabWidget(self.splitter_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_27 = QVBoxLayout(self.tab)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_18 = QLabel(self.tab)
        self.label_18.setObjectName("label_18")

        self.verticalLayout_19.addWidget(self.label_18)

        self.label_19 = QLabel(self.tab)
        self.label_19.setObjectName("label_19")

        self.verticalLayout_19.addWidget(self.label_19)

        self.label_20 = QLabel(self.tab)
        self.label_20.setObjectName("label_20")

        self.verticalLayout_19.addWidget(self.label_20)

        self.label_21 = QLabel(self.tab)
        self.label_21.setObjectName("label_21")

        self.verticalLayout_19.addWidget(self.label_21)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName("label_7")

        self.verticalLayout_19.addWidget(self.label_7)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName("label_8")

        self.verticalLayout_19.addWidget(self.label_8)

        self.horizontalLayout_8.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.comboBox_pixel_number = QComboBox(self.tab)
        self.comboBox_pixel_number.addItem("")
        self.comboBox_pixel_number.addItem("")
        self.comboBox_pixel_number.addItem("")
        self.comboBox_pixel_number.addItem("")
        self.comboBox_pixel_number.addItem("")
        self.comboBox_pixel_number.addItem("")
        self.comboBox_pixel_number.setObjectName("comboBox_pixel_number")

        self.verticalLayout_20.addWidget(self.comboBox_pixel_number)

        self.doubleSpinBox_alpha = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_alpha.setObjectName("doubleSpinBox_alpha")
        self.doubleSpinBox_alpha.setMaximum(9999.989999999999782)

        self.verticalLayout_20.addWidget(self.doubleSpinBox_alpha)

        self.doubleSpinBox_voltage = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_voltage.setObjectName("doubleSpinBox_voltage")
        self.doubleSpinBox_voltage.setMaximum(9999.989999999999782)

        self.verticalLayout_20.addWidget(self.doubleSpinBox_voltage)

        self.doubleSpinBox_bright_field_disk_radius = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_bright_field_disk_radius.setObjectName(
            "doubleSpinBox_bright_field_disk_radius"
        )
        self.doubleSpinBox_bright_field_disk_radius.setMaximum(9999.989999999999782)

        self.verticalLayout_20.addWidget(self.doubleSpinBox_bright_field_disk_radius)

        self.doubleSpinBox_scanning_step_size = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_scanning_step_size.setObjectName(
            "doubleSpinBox_scanning_step_size"
        )
        self.doubleSpinBox_scanning_step_size.setDecimals(6)
        self.doubleSpinBox_scanning_step_size.setMaximum(999999.999998999992386)

        self.verticalLayout_20.addWidget(self.doubleSpinBox_scanning_step_size)

        self.doubleSpinBox_camera_length = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_camera_length.setObjectName("doubleSpinBox_camera_length")
        self.doubleSpinBox_camera_length.setDecimals(6)
        self.doubleSpinBox_camera_length.setMaximum(999999.999998999992386)

        self.verticalLayout_20.addWidget(self.doubleSpinBox_camera_length)

        self.horizontalLayout_8.addLayout(self.verticalLayout_20)

        self.verticalLayout_18.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_22 = QLabel(self.tab)
        self.label_22.setObjectName("label_22")

        self.verticalLayout_21.addWidget(self.label_22)

        self.label_23 = QLabel(self.tab)
        self.label_23.setObjectName("label_23")

        self.verticalLayout_21.addWidget(self.label_23)

        self.label_25 = QLabel(self.tab)
        self.label_25.setObjectName("label_25")

        self.verticalLayout_21.addWidget(self.label_25)

        self.label_26 = QLabel(self.tab)
        self.label_26.setObjectName("label_26")

        self.verticalLayout_21.addWidget(self.label_26)

        self.horizontalLayout_9.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_dk = QLabel(self.tab)
        self.label_dk.setObjectName("label_dk")

        self.verticalLayout_22.addWidget(self.label_dk)

        self.label_dx = QLabel(self.tab)
        self.label_dx.setObjectName("label_dx")

        self.verticalLayout_22.addWidget(self.label_dx)

        self.label_object_size = QLabel(self.tab)
        self.label_object_size.setObjectName("label_object_size")

        self.verticalLayout_22.addWidget(self.label_object_size)

        self.label_reciprocal_space_size = QLabel(self.tab)
        self.label_reciprocal_space_size.setObjectName("label_reciprocal_space_size")

        self.verticalLayout_22.addWidget(self.label_reciprocal_space_size)

        self.horizontalLayout_9.addLayout(self.verticalLayout_22)

        self.verticalLayout_18.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_18.addItem(self.verticalSpacer_4)

        self.verticalLayout_27.addLayout(self.verticalLayout_18)

        self.tabWidget.addTab(self.tab, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout_26 = QVBoxLayout(self.tab_8)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_27 = QLabel(self.tab_8)
        self.label_27.setObjectName("label_27")

        self.verticalLayout_23.addWidget(self.label_27)

        self.label_28 = QLabel(self.tab_8)
        self.label_28.setObjectName("label_28")

        self.verticalLayout_23.addWidget(self.label_28)

        self.horizontalLayout_10.addLayout(self.verticalLayout_23)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.doubleSpinBox_defocus = QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_defocus.setObjectName("doubleSpinBox_defocus")
        self.doubleSpinBox_defocus.setDecimals(6)
        self.doubleSpinBox_defocus.setMinimum(-999999.999998999992386)
        self.doubleSpinBox_defocus.setMaximum(999999.999998999992386)

        self.verticalLayout_24.addWidget(self.doubleSpinBox_defocus)

        self.doubleSpinBox_Cs = QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_Cs.setObjectName("doubleSpinBox_Cs")
        self.doubleSpinBox_Cs.setDecimals(6)
        self.doubleSpinBox_Cs.setMaximum(9999.999998999999661)

        self.verticalLayout_24.addWidget(self.doubleSpinBox_Cs)

        self.horizontalLayout_10.addLayout(self.verticalLayout_24)

        self.verticalLayout_25.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.pushButton_set_aberrations = QPushButton(self.tab_8)
        self.pushButton_set_aberrations.setObjectName("pushButton_set_aberrations")

        self.horizontalLayout_11.addWidget(self.pushButton_set_aberrations)

        self.verticalLayout_25.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_5 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_25.addItem(self.verticalSpacer_5)

        self.verticalLayout_26.addLayout(self.verticalLayout_25)

        self.tabWidget.addTab(self.tab_8, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.textBrowser_image_mode_descriptions = QTextBrowser(self.tab_2)
        self.textBrowser_image_mode_descriptions.setObjectName(
            "textBrowser_image_mode_descriptions"
        )

        self.verticalLayout_3.addWidget(self.textBrowser_image_mode_descriptions)

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.comboBox_image_modes = QComboBox(self.tab_2)
        self.comboBox_image_modes.addItem("")
        self.comboBox_image_modes.addItem("")
        self.comboBox_image_modes.addItem("")
        self.comboBox_image_modes.addItem("")
        self.comboBox_image_modes.addItem("")
        self.comboBox_image_modes.addItem("")
        self.comboBox_image_modes.setObjectName("comboBox_image_modes")

        self.horizontalLayout_3.addWidget(self.comboBox_image_modes)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.stackedWidget = QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_virtual_detector = QWidget()
        self.page_virtual_detector.setObjectName("page_virtual_detector")
        self.verticalLayout_2 = QVBoxLayout(self.page_virtual_detector)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QLabel(self.page_virtual_detector)
        self.label_5.setObjectName("label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QLabel(self.page_virtual_detector)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(
            18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.doubleSpinBox_abf_outer_radius = QDoubleSpinBox(self.page_virtual_detector)
        self.doubleSpinBox_abf_outer_radius.setObjectName(
            "doubleSpinBox_abf_outer_radius"
        )
        self.doubleSpinBox_abf_outer_radius.setDecimals(4)
        self.doubleSpinBox_abf_outer_radius.setMaximum(9999.999900000000707)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_abf_outer_radius)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QLabel(self.page_virtual_detector)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(
            18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox_abf_inner_radius = QDoubleSpinBox(self.page_virtual_detector)
        self.doubleSpinBox_abf_inner_radius.setObjectName(
            "doubleSpinBox_abf_inner_radius"
        )
        self.doubleSpinBox_abf_inner_radius.setDecimals(4)
        self.doubleSpinBox_abf_inner_radius.setMaximum(9999.999900000000707)

        self.horizontalLayout.addWidget(self.doubleSpinBox_abf_inner_radius)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 132, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_virtual_detector)
        self.page_nothing = QWidget()
        self.page_nothing.setObjectName("page_nothing")
        self.stackedWidget.addWidget(self.page_nothing)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_2, "")
        self.splitter_2.addWidget(self.tabWidget)

        self.verticalLayout_6.addWidget(self.splitter_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pushButton_start_calculation = QPushButton(Form)
        self.pushButton_start_calculation.setObjectName("pushButton_start_calculation")

        self.horizontalLayout_5.addWidget(self.pushButton_start_calculation)

        self.pushButton_save_config_path = QPushButton(Form)
        self.pushButton_save_config_path.setObjectName("pushButton_save_config_path")

        self.horizontalLayout_5.addWidget(self.pushButton_save_config_path)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Form)

        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText(
            QCoreApplication.translate("Form", "Optical Configuration (CTF) Path", None)
        )
        self.pushButton_browse_config.setText(
            QCoreApplication.translate("Form", "Browse", None)
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_3),
            QCoreApplication.translate("Form", "Ronchigram (Random Sample)", None),
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_4),
            QCoreApplication.translate("Form", "Probe (Amplitude)", None),
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_5),
            QCoreApplication.translate("Form", "Probe (Phase)", None),
        )
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.tab_9),
            QCoreApplication.translate("Form", "CTF Image", None),
        )
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.tab_10),
            QCoreApplication.translate("Form", "CTF Curve", None),
        )
        self.label_18.setText(
            QCoreApplication.translate("Form", "Detector Pixel Number (N)", None)
        )
        self.label_19.setText(
            QCoreApplication.translate(
                "Form", "Convergent Semi-angle \u03b1 (in mrad)", None
            )
        )
        self.label_20.setText(
            QCoreApplication.translate("Form", "Accelerate Voltage (in kV)", None)
        )
        self.label_21.setText(
            QCoreApplication.translate(
                "Form", "Bright Field Disk Radius (in pix)", None
            )
        )
        self.label_7.setText(
            QCoreApplication.translate("Form", "Scanning Step Size (in nm)", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("Form", "Camera Length (in mm)", None)
        )
        self.comboBox_pixel_number.setItemText(
            0, QCoreApplication.translate("Form", "128", None)
        )
        self.comboBox_pixel_number.setItemText(
            1, QCoreApplication.translate("Form", "256", None)
        )
        self.comboBox_pixel_number.setItemText(
            2, QCoreApplication.translate("Form", "512", None)
        )
        self.comboBox_pixel_number.setItemText(
            3, QCoreApplication.translate("Form", "1024", None)
        )
        self.comboBox_pixel_number.setItemText(
            4, QCoreApplication.translate("Form", "2048", None)
        )
        self.comboBox_pixel_number.setItemText(
            5, QCoreApplication.translate("Form", "4096", None)
        )

        self.label_22.setText(
            QCoreApplication.translate("Form", "Reciprocal Pixel Size (dk)", None)
        )
        self.label_23.setText(
            QCoreApplication.translate("Form", "Real Pixel Size (dx)", None)
        )
        self.label_25.setText(QCoreApplication.translate("Form", "Object Size", None))
        self.label_26.setText(
            QCoreApplication.translate("Form", "Reciprocal Space Size", None)
        )
        self.label_dk.setText(QCoreApplication.translate("Form", "TextLabel", None))
        self.label_dx.setText(QCoreApplication.translate("Form", "TextLabel", None))
        self.label_object_size.setText(
            QCoreApplication.translate("Form", "TextLabel", None)
        )
        self.label_reciprocal_space_size.setText(
            QCoreApplication.translate("Form", "TextLabel", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("Form", "Optical Parameters", None),
        )
        self.label_27.setText(
            QCoreApplication.translate(
                "Form", "<html><head/><body><p>Defocus (in nm)</p></body></html>", None
            )
        )
        self.label_28.setText(
            QCoreApplication.translate(
                "Form", "Spherical Aberration Cs (in \u03bcm)", None
            )
        )
        self.pushButton_set_aberrations.setText(
            QCoreApplication.translate("Form", "Set High Order Aberrations...", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_8),
            QCoreApplication.translate("Form", "Aberration Coefficients", None),
        )
        self.label_6.setText(QCoreApplication.translate("Form", "Descriptions", None))
        self.label_2.setText(QCoreApplication.translate("Form", "Image Modes", None))
        self.comboBox_image_modes.setItemText(
            0, QCoreApplication.translate("Form", "(Annular) Bright Fields", None)
        )
        self.comboBox_image_modes.setItemText(
            1, QCoreApplication.translate("Form", "Annular Dark Fields", None)
        )
        self.comboBox_image_modes.setItemText(
            2, QCoreApplication.translate("Form", "Full Bright Fields", None)
        )
        self.comboBox_image_modes.setItemText(
            3, QCoreApplication.translate("Form", "Axial Bright Fields", None)
        )
        self.comboBox_image_modes.setItemText(
            4, QCoreApplication.translate("Form", "Differentiated Center of Mass", None)
        )
        self.comboBox_image_modes.setItemText(
            5, QCoreApplication.translate("Form", "Integrated Center of Mass", None)
        )

        self.label_5.setText(
            QCoreApplication.translate("Form", "Virtual Detector Regions", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("Form", "Outer Radius (in mrad)", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("Form", "Inner Radius (in mrad)", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("Form", "CTF Image Modes", None),
        )
        self.pushButton_start_calculation.setText(
            QCoreApplication.translate("Form", "Start Calculation", None)
        )
        self.pushButton_save_config_path.setText(
            QCoreApplication.translate(
                "Form", "Save Optical Configuration (CTF Curve)", None
            )
        )

    # retranslateUi
