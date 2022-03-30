# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageViewFourDSTEM.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QSpinBox, QSplitter, QVBoxLayout, QWidget)

from bin.Widgets.WidgetPlots import (WidgetPlotDP, WidgetPlotPreview)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(924, 575)
        self.verticalLayout_8 = QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_data_path = QLineEdit(self.widget)
        self.lineEdit_data_path.setObjectName(u"lineEdit_data_path")

        self.horizontalLayout.addWidget(self.lineEdit_data_path)

        self.pushButton_browse = QPushButton(self.widget)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_adjust_axis = QPushButton(self.widget)
        self.pushButton_adjust_axis.setObjectName(u"pushButton_adjust_axis")

        self.horizontalLayout_2.addWidget(self.pushButton_adjust_axis)

        self.pushButton_analyze = QPushButton(self.widget)
        self.pushButton_analyze.setObjectName(u"pushButton_analyze")

        self.horizontalLayout_2.addWidget(self.pushButton_analyze)

        self.pushButton_processing = QPushButton(self.widget)
        self.pushButton_processing.setObjectName(u"pushButton_processing")

        self.horizontalLayout_2.addWidget(self.pushButton_processing)

        self.pushButton_calibrate = QPushButton(self.widget)
        self.pushButton_calibrate.setObjectName(u"pushButton_calibrate")

        self.horizontalLayout_2.addWidget(self.pushButton_calibrate)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.widget_dp = WidgetPlotDP(self.widget)
        self.widget_dp.setObjectName(u"widget_dp")

        self.verticalLayout_3.addWidget(self.widget_dp)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.spinBox_scan_ii = QSpinBox(self.widget)
        self.spinBox_scan_ii.setObjectName(u"spinBox_scan_ii")

        self.verticalLayout_2.addWidget(self.spinBox_scan_ii)

        self.spinBox_scan_jj = QSpinBox(self.widget)
        self.spinBox_scan_jj.setObjectName(u"spinBox_scan_jj")

        self.verticalLayout_2.addWidget(self.spinBox_scan_jj)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.setStretch(2, 1)
        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_6 = QVBoxLayout(self.widget1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_preview_path = QLineEdit(self.widget1)
        self.lineEdit_preview_path.setObjectName(u"lineEdit_preview_path")

        self.horizontalLayout_4.addWidget(self.lineEdit_preview_path)

        self.pushButton_preview_reset = QPushButton(self.widget1)
        self.pushButton_preview_reset.setObjectName(u"pushButton_preview_reset")

        self.horizontalLayout_4.addWidget(self.pushButton_preview_reset)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.widget_preview = WidgetPlotPreview(self.widget1)
        self.widget_preview.setObjectName(u"widget_preview")

        self.verticalLayout_6.addWidget(self.widget_preview)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_attributes = QPushButton(self.widget1)
        self.pushButton_attributes.setObjectName(u"pushButton_attributes")

        self.verticalLayout_7.addWidget(self.pushButton_attributes)

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

        self.comboBox_norm = QComboBox(self.widget1)
        self.comboBox_norm.setObjectName(u"comboBox_norm")

        self.verticalLayout_5.addWidget(self.comboBox_norm)

        self.comboBox_colormap = QComboBox(self.widget1)
        self.comboBox_colormap.setObjectName(u"comboBox_colormap")

        self.verticalLayout_5.addWidget(self.comboBox_colormap)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_6.addLayout(self.verticalLayout_7)

        self.verticalLayout_6.setStretch(1, 1)
        self.splitter.addWidget(self.widget1)

        self.verticalLayout_8.addWidget(self.splitter)


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
        self.label_2.setText(QCoreApplication.translate("Form", u"DPi index (location in vertical direction)", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"DPj index (location in horizontal direction)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Preview Path", None))
        self.pushButton_preview_reset.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.pushButton_attributes.setText(QCoreApplication.translate("Form", u"4D-STEM attributes...", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Brightness", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Contrast", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Norm", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Colormap", None))
    # retranslateUi

