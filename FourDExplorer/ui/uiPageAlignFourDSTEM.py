# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageAlignFourDSTEM.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QSplitter, QStackedWidget,
    QTabWidget, QVBoxLayout, QWidget)

from bin.Widgets.WidgetAlignmentFDDNet import WidgetAlignmentFDDNet
from bin.Widgets.WidgetAlignmentManual import WidgetAlignmentManual
from bin.Widgets.WidgetAlignmentRef import WidgetAlignmentRef
from bin.Widgets.WidgetMasks import WidgetMaskCircle
from bin.Widgets.WidgetPlots import WidgetPlotDP

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(905, 604)
        self.verticalLayout_7 = QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_data_path = QLineEdit(self.layoutWidget)
        self.lineEdit_data_path.setObjectName(u"lineEdit_data_path")

        self.horizontalLayout.addWidget(self.lineEdit_data_path)

        self.pushButton_browse = QPushButton(self.layoutWidget)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.widget_dp = WidgetPlotDP(self.layoutWidget)
        self.widget_dp.setObjectName(u"widget_dp")

        self.verticalLayout_3.addWidget(self.widget_dp)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.spinBox_scan_ii = QSpinBox(self.layoutWidget)
        self.spinBox_scan_ii.setObjectName(u"spinBox_scan_ii")

        self.verticalLayout_2.addWidget(self.spinBox_scan_ii)

        self.spinBox_scan_jj = QSpinBox(self.layoutWidget)
        self.spinBox_scan_jj.setObjectName(u"spinBox_scan_jj")

        self.verticalLayout_2.addWidget(self.spinBox_scan_jj)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.setStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_diffraction_shift_alignment = QWidget()
        self.tab_diffraction_shift_alignment.setObjectName(u"tab_diffraction_shift_alignment")
        self.verticalLayout_4 = QVBoxLayout(self.tab_diffraction_shift_alignment)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.tab_diffraction_shift_alignment)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.comboBox_show_alignment_method = QComboBox(self.tab_diffraction_shift_alignment)
        self.comboBox_show_alignment_method.addItem("")
        self.comboBox_show_alignment_method.addItem("")
        self.comboBox_show_alignment_method.addItem("")
        self.comboBox_show_alignment_method.setObjectName(u"comboBox_show_alignment_method")

        self.horizontalLayout_10.addWidget(self.comboBox_show_alignment_method)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.stackedWidget_align_mode = QStackedWidget(self.tab_diffraction_shift_alignment)
        self.stackedWidget_align_mode.setObjectName(u"stackedWidget_align_mode")
        self.stackedWidget_align_mode_manually = WidgetAlignmentManual()
        self.stackedWidget_align_mode_manually.setObjectName(u"stackedWidget_align_mode_manually")
        self.stackedWidget_align_mode.addWidget(self.stackedWidget_align_mode_manually)
        self.stackedWidget_align_mode_reference = WidgetAlignmentRef()
        self.stackedWidget_align_mode_reference.setObjectName(u"stackedWidget_align_mode_reference")
        self.stackedWidget_align_mode.addWidget(self.stackedWidget_align_mode_reference)
        self.stackedWidget_align_mode_fddnet = WidgetAlignmentFDDNet()
        self.stackedWidget_align_mode_fddnet.setObjectName(u"stackedWidget_align_mode_fddnet")
        self.stackedWidget_align_mode.addWidget(self.stackedWidget_align_mode_fddnet)

        self.verticalLayout_4.addWidget(self.stackedWidget_align_mode)

        self.tabWidget.addTab(self.tab_diffraction_shift_alignment, "")
        self.tab_displaying_effects = QWidget()
        self.tab_displaying_effects.setObjectName(u"tab_displaying_effects")
        self.verticalLayout_10 = QVBoxLayout(self.tab_displaying_effects)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_13 = QLabel(self.tab_displaying_effects)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_8.addWidget(self.label_13)

        self.lineEdit_shift_mapping_path = QLineEdit(self.tab_displaying_effects)
        self.lineEdit_shift_mapping_path.setObjectName(u"lineEdit_shift_mapping_path")

        self.horizontalLayout_8.addWidget(self.lineEdit_shift_mapping_path)

        self.pushButton_browse_shift_mapping = QPushButton(self.tab_displaying_effects)
        self.pushButton_browse_shift_mapping.setObjectName(u"pushButton_browse_shift_mapping")

        self.horizontalLayout_8.addWidget(self.pushButton_browse_shift_mapping)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.groupBox_2 = QGroupBox(self.tab_displaying_effects)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_draw_auxiliary_arrow = QCheckBox(self.groupBox_2)
        self.checkBox_draw_auxiliary_arrow.setObjectName(u"checkBox_draw_auxiliary_arrow")

        self.verticalLayout_9.addWidget(self.checkBox_draw_auxiliary_arrow)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_8.addWidget(self.label_14)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_8.addWidget(self.label_15)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.comboBox_auxiliary_arrow_color = QComboBox(self.groupBox_2)
        self.comboBox_auxiliary_arrow_color.addItem("")
        self.comboBox_auxiliary_arrow_color.addItem("")
        self.comboBox_auxiliary_arrow_color.addItem("")
        self.comboBox_auxiliary_arrow_color.addItem("")
        self.comboBox_auxiliary_arrow_color.addItem("")
        self.comboBox_auxiliary_arrow_color.addItem("")
        self.comboBox_auxiliary_arrow_color.addItem("")
        self.comboBox_auxiliary_arrow_color.addItem("")
        self.comboBox_auxiliary_arrow_color.addItem("")
        self.comboBox_auxiliary_arrow_color.setObjectName(u"comboBox_auxiliary_arrow_color")

        self.verticalLayout_6.addWidget(self.comboBox_auxiliary_arrow_color)

        self.doubleSpinBox_auxiliary_arrow_width = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_auxiliary_arrow_width.setObjectName(u"doubleSpinBox_auxiliary_arrow_width")

        self.verticalLayout_6.addWidget(self.doubleSpinBox_auxiliary_arrow_width)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)


        self.verticalLayout_10.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.tab_displaying_effects)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_auxiliary_circle = WidgetMaskCircle(self.groupBox)
        self.widget_auxiliary_circle.setObjectName(u"widget_auxiliary_circle")

        self.verticalLayout_5.addWidget(self.widget_auxiliary_circle)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_current_auxiliary_circle_center = QLabel(self.groupBox)
        self.label_current_auxiliary_circle_center.setObjectName(u"label_current_auxiliary_circle_center")

        self.horizontalLayout_2.addWidget(self.label_current_auxiliary_circle_center)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.checkBox_set_auxiliary_circle_center_to_shift = QCheckBox(self.groupBox)
        self.checkBox_set_auxiliary_circle_center_to_shift.setObjectName(u"checkBox_set_auxiliary_circle_center_to_shift")

        self.verticalLayout_5.addWidget(self.checkBox_set_auxiliary_circle_center_to_shift)

        self.checkBox_show_auxiliary_circle = QCheckBox(self.groupBox)
        self.checkBox_show_auxiliary_circle.setObjectName(u"checkBox_show_auxiliary_circle")

        self.verticalLayout_5.addWidget(self.checkBox_show_auxiliary_circle)


        self.verticalLayout_10.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.tab_displaying_effects)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.horizontalSlider_brightness = QSlider(self.tab_displaying_effects)
        self.horizontalSlider_brightness.setObjectName(u"horizontalSlider_brightness")
        self.horizontalSlider_brightness.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_brightness, 0, 1, 1, 1)

        self.label_6 = QLabel(self.tab_displaying_effects)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.horizontalSlider_contrast = QSlider(self.tab_displaying_effects)
        self.horizontalSlider_contrast.setObjectName(u"horizontalSlider_contrast")
        self.horizontalSlider_contrast.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_contrast, 1, 1, 1, 1)

        self.label_7 = QLabel(self.tab_displaying_effects)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.comboBox_normalize = QComboBox(self.tab_displaying_effects)
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.setObjectName(u"comboBox_normalize")

        self.gridLayout_2.addWidget(self.comboBox_normalize, 2, 1, 1, 1)

        self.label_8 = QLabel(self.tab_displaying_effects)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.comboBox_colormap = QComboBox(self.tab_displaying_effects)
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.setObjectName(u"comboBox_colormap")

        self.gridLayout_2.addWidget(self.comboBox_colormap, 3, 1, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.tab_displaying_effects, "")
        self.splitter.addWidget(self.tabWidget)

        self.verticalLayout_7.addWidget(self.splitter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout_4.addWidget(self.pushButton_start)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.verticalLayout_7.setStretch(0, 1)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget_align_mode.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"4D-STEM data path", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"DPi index (rows of location)", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"DPj index (columns of location)", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Alignment Method", None))
        self.comboBox_show_alignment_method.setItemText(0, QCoreApplication.translate("Form", u"Manually", None))
        self.comboBox_show_alignment_method.setItemText(1, QCoreApplication.translate("Form", u"Use Reference Dataset", None))
        self.comboBox_show_alignment_method.setItemText(2, QCoreApplication.translate("Form", u"Use FDDNet", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_diffraction_shift_alignment), QCoreApplication.translate("Form", u"Diffraction Shift Alignment", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Shift Mapping Path", None))
        self.pushButton_browse_shift_mapping.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Auxiliary Arrow", None))
        self.checkBox_draw_auxiliary_arrow.setText(QCoreApplication.translate("Form", u"Draw shift arrow at the center", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Arrow Color", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Arrow Width", None))
        self.comboBox_auxiliary_arrow_color.setItemText(0, QCoreApplication.translate("Form", u"black", None))
        self.comboBox_auxiliary_arrow_color.setItemText(1, QCoreApplication.translate("Form", u"blue", None))
        self.comboBox_auxiliary_arrow_color.setItemText(2, QCoreApplication.translate("Form", u"cyan", None))
        self.comboBox_auxiliary_arrow_color.setItemText(3, QCoreApplication.translate("Form", u"green", None))
        self.comboBox_auxiliary_arrow_color.setItemText(4, QCoreApplication.translate("Form", u"orange", None))
        self.comboBox_auxiliary_arrow_color.setItemText(5, QCoreApplication.translate("Form", u"purple", None))
        self.comboBox_auxiliary_arrow_color.setItemText(6, QCoreApplication.translate("Form", u"red", None))
        self.comboBox_auxiliary_arrow_color.setItemText(7, QCoreApplication.translate("Form", u"white", None))
        self.comboBox_auxiliary_arrow_color.setItemText(8, QCoreApplication.translate("Form", u"yellow", None))

        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Auxiliary Circle", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Current Circle Center", None))
        self.label_current_auxiliary_circle_center.setText(QCoreApplication.translate("Form", u"(0, 0)", None))
        self.checkBox_set_auxiliary_circle_center_to_shift.setText(QCoreApplication.translate("Form", u"Set circle center to where the shift vector point to", None))
        self.checkBox_show_auxiliary_circle.setText(QCoreApplication.translate("Form", u"Show auxiliary circle", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Brightness", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Contrast", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Norm", None))
        self.comboBox_normalize.setItemText(0, QCoreApplication.translate("Form", u"Linear", None))
        self.comboBox_normalize.setItemText(1, QCoreApplication.translate("Form", u"Logarithm", None))

        self.label_8.setText(QCoreApplication.translate("Form", u"Color map", None))
        self.comboBox_colormap.setItemText(0, QCoreApplication.translate("Form", u"viridis", None))
        self.comboBox_colormap.setItemText(1, QCoreApplication.translate("Form", u"plasma", None))
        self.comboBox_colormap.setItemText(2, QCoreApplication.translate("Form", u"gray", None))
        self.comboBox_colormap.setItemText(3, QCoreApplication.translate("Form", u"RdYlBu", None))
        self.comboBox_colormap.setItemText(4, QCoreApplication.translate("Form", u"twilight", None))
        self.comboBox_colormap.setItemText(5, QCoreApplication.translate("Form", u"hsv", None))
        self.comboBox_colormap.setItemText(6, QCoreApplication.translate("Form", u"jet", None))
        self.comboBox_colormap.setItemText(7, QCoreApplication.translate("Form", u"Others", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_displaying_effects), QCoreApplication.translate("Form", u"Displaying Effects", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"Start Calculation (Applying Shift Vector to 4D-STEM Dataset)", None))
    # retranslateUi

