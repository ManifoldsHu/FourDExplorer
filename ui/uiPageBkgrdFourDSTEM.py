# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageBkgrdFourDSTEM.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QSplitter, QVBoxLayout, QWidget)

from bin.Widgets.WidgetPlots import (WidgetPlotDP, WidgetPlotHist)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(896, 704)
        self.verticalLayout_8 = QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter_2)
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

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_adjust_axis = QPushButton(self.layoutWidget)
        self.pushButton_adjust_axis.setObjectName(u"pushButton_adjust_axis")

        self.horizontalLayout_2.addWidget(self.pushButton_adjust_axis)

        self.pushButton_analyze = QPushButton(self.layoutWidget)
        self.pushButton_analyze.setObjectName(u"pushButton_analyze")

        self.horizontalLayout_2.addWidget(self.pushButton_analyze)

        self.pushButton_processing = QPushButton(self.layoutWidget)
        self.pushButton_processing.setObjectName(u"pushButton_processing")

        self.horizontalLayout_2.addWidget(self.pushButton_processing)

        self.pushButton_calibrate = QPushButton(self.layoutWidget)
        self.pushButton_calibrate.setObjectName(u"pushButton_calibrate")

        self.horizontalLayout_2.addWidget(self.pushButton_calibrate)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

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

        self.verticalLayout_3.setStretch(2, 1)
        self.splitter_2.addWidget(self.layoutWidget)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.widget_hist = WidgetPlotHist(self.widget)
        self.widget_hist.setObjectName(u"widget_hist")

        self.verticalLayout_7.addWidget(self.widget_hist)

        self.verticalLayout_7.setStretch(1, 1)
        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_6 = QVBoxLayout(self.widget1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.doubleSpinBox_window_min = QDoubleSpinBox(self.widget1)
        self.doubleSpinBox_window_min.setObjectName(u"doubleSpinBox_window_min")

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_window_min)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.widget1)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox_window_max = QDoubleSpinBox(self.widget1)
        self.doubleSpinBox_window_max.setObjectName(u"doubleSpinBox_window_max")

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_window_max)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.checkBox_apply_window_min = QCheckBox(self.widget1)
        self.checkBox_apply_window_min.setObjectName(u"checkBox_apply_window_min")

        self.verticalLayout_6.addWidget(self.checkBox_apply_window_min)

        self.checkBox_apply_window_max = QCheckBox(self.widget1)
        self.checkBox_apply_window_max.setObjectName(u"checkBox_apply_window_max")

        self.verticalLayout_6.addWidget(self.checkBox_apply_window_max)

        self.pushButton_attributes = QPushButton(self.widget1)
        self.pushButton_attributes.setObjectName(u"pushButton_attributes")

        self.verticalLayout_6.addWidget(self.pushButton_attributes)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget1)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalSlider_brightness = QSlider(self.widget1)
        self.horizontalSlider_brightness.setObjectName(u"horizontalSlider_brightness")
        self.horizontalSlider_brightness.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_brightness)

        self.horizontalSlider_contrast = QSlider(self.widget1)
        self.horizontalSlider_contrast.setObjectName(u"horizontalSlider_contrast")
        self.horizontalSlider_contrast.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_contrast)

        self.comboBox_normalize = QComboBox(self.widget1)
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.setObjectName(u"comboBox_normalize")

        self.verticalLayout_5.addWidget(self.comboBox_normalize)

        self.comboBox_colormap = QComboBox(self.widget1)
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.setObjectName(u"comboBox_colormap")

        self.verticalLayout_5.addWidget(self.comboBox_colormap)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.splitter.addWidget(self.widget1)
        self.splitter_2.addWidget(self.splitter)

        self.verticalLayout_8.addWidget(self.splitter_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout_7.addWidget(self.pushButton_start)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.verticalLayout_8.setStretch(0, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"4D-STEM data path", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.pushButton_adjust_axis.setText(QCoreApplication.translate("Form", u"Adjust Axis...", None))
        self.pushButton_analyze.setText(QCoreApplication.translate("Form", u"Analyze...", None))
        self.pushButton_processing.setText(QCoreApplication.translate("Form", u"Processing...", None))
        self.pushButton_calibrate.setText(QCoreApplication.translate("Form", u"Calibrate...", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"DPi index (rows of location)", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"DPj index (columns of location)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Select Window Filter", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Window Min Value", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Window Max Value", None))
        self.checkBox_apply_window_min.setText(QCoreApplication.translate("Form", u"Applying Window (Min Constrain)", None))
        self.checkBox_apply_window_max.setText(QCoreApplication.translate("Form", u"Applying Window (Max Constrain)", None))
        self.pushButton_attributes.setText(QCoreApplication.translate("Form", u"4D-STEM attributes...", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Brightness", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Contrast", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Norm", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Color map", None))
        self.comboBox_normalize.setItemText(0, QCoreApplication.translate("Form", u"Linear", None))
        self.comboBox_normalize.setItemText(1, QCoreApplication.translate("Form", u"Logarithm", None))

        self.comboBox_colormap.setItemText(0, QCoreApplication.translate("Form", u"viridis", None))
        self.comboBox_colormap.setItemText(1, QCoreApplication.translate("Form", u"plasma", None))
        self.comboBox_colormap.setItemText(2, QCoreApplication.translate("Form", u"gray", None))
        self.comboBox_colormap.setItemText(3, QCoreApplication.translate("Form", u"RdYlBu", None))
        self.comboBox_colormap.setItemText(4, QCoreApplication.translate("Form", u"twilight", None))
        self.comboBox_colormap.setItemText(5, QCoreApplication.translate("Form", u"hsv", None))
        self.comboBox_colormap.setItemText(6, QCoreApplication.translate("Form", u"jet", None))
        self.comboBox_colormap.setItemText(7, QCoreApplication.translate("Form", u"Others", None))

        self.pushButton_start.setText(QCoreApplication.translate("Form", u"Start Calculation", None))
    # retranslateUi

