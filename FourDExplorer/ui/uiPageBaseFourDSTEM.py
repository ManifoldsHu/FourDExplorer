# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageBaseFourDSTEM.ui'
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
    QSpacerItem, QSpinBox, QSplitter, QVBoxLayout,
    QWidget)

from bin.Widgets.WidgetPlots import WidgetPlotDP

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(785, 503)
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

        self.verticalLayout_3.setStretch(1, 1)
        self.splitter.addWidget(self.widget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalSlider_brightness = QSlider(self.layoutWidget)
        self.horizontalSlider_brightness.setObjectName(u"horizontalSlider_brightness")
        self.horizontalSlider_brightness.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_brightness)

        self.horizontalSlider_contrast = QSlider(self.layoutWidget)
        self.horizontalSlider_contrast.setObjectName(u"horizontalSlider_contrast")
        self.horizontalSlider_contrast.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_contrast)

        self.comboBox_normalize = QComboBox(self.layoutWidget)
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.setObjectName(u"comboBox_normalize")

        self.verticalLayout_5.addWidget(self.comboBox_normalize)

        self.comboBox_colormap = QComboBox(self.layoutWidget)
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


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout_7.setStretch(0, 1)
        self.splitter.addWidget(self.layoutWidget)

        self.verticalLayout_8.addWidget(self.splitter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"4D-STEM data path", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"DPi index (rows of location)", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"DPj index (columns of location)", None))
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

    # retranslateUi

