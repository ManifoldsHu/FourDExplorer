# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageViewImage.ui'
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
    QSplitter, QVBoxLayout, QWidget)

from bin.Widgets.WidgetPlots import (WidgetPlotHist, WidgetPlotImage)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(859, 636)
        self.verticalLayout_8 = QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_image_path = QLineEdit(Form)
        self.lineEdit_image_path.setObjectName(u"lineEdit_image_path")

        self.horizontalLayout_3.addWidget(self.lineEdit_image_path)

        self.pushButton_browse = QPushButton(Form)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout_3.addWidget(self.pushButton_browse)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_adjust_axis = QPushButton(self.widget)
        self.pushButton_adjust_axis.setObjectName(u"pushButton_adjust_axis")

        self.horizontalLayout.addWidget(self.pushButton_adjust_axis)

        self.pushButton_analysis = QPushButton(self.widget)
        self.pushButton_analysis.setObjectName(u"pushButton_analysis")

        self.horizontalLayout.addWidget(self.pushButton_analysis)

        self.pushButton_image_processing = QPushButton(self.widget)
        self.pushButton_image_processing.setObjectName(u"pushButton_image_processing")

        self.horizontalLayout.addWidget(self.pushButton_image_processing)

        self.pushButton_calibrate = QPushButton(self.widget)
        self.pushButton_calibrate.setObjectName(u"pushButton_calibrate")

        self.horizontalLayout.addWidget(self.pushButton_calibrate)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.widget_image = WidgetPlotImage(self.widget)
        self.widget_image.setObjectName(u"widget_image")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_image.sizePolicy().hasHeightForWidth())
        self.widget_image.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.widget_image)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_7 = QVBoxLayout(self.widget1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.label_4)

        self.widget_hist_view = WidgetPlotHist(self.widget1)
        self.widget_hist_view.setObjectName(u"widget_hist_view")
        sizePolicy.setHeightForWidth(self.widget_hist_view.sizePolicy().hasHeightForWidth())
        self.widget_hist_view.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.widget_hist_view)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_4 = QPushButton(self.widget1)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalSlider_brightness = QSlider(self.widget1)
        self.horizontalSlider_brightness.setObjectName(u"horizontalSlider_brightness")
        self.horizontalSlider_brightness.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider_brightness)

        self.horizontalSlider_contrast = QSlider(self.widget1)
        self.horizontalSlider_contrast.setObjectName(u"horizontalSlider_contrast")
        self.horizontalSlider_contrast.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider_contrast)

        self.comboBox_normalize = QComboBox(self.widget1)
        self.comboBox_normalize.setObjectName(u"comboBox_normalize")

        self.verticalLayout_2.addWidget(self.comboBox_normalize)

        self.comboBox_colormap = QComboBox(self.widget1)
        self.comboBox_colormap.setObjectName(u"comboBox_colormap")

        self.verticalLayout_2.addWidget(self.comboBox_colormap)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.splitter.addWidget(self.widget1)

        self.verticalLayout_8.addWidget(self.splitter)

        self.verticalLayout_8.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Image Path", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.pushButton_adjust_axis.setText(QCoreApplication.translate("Form", u"Adjust Axis...", None))
        self.pushButton_analysis.setText(QCoreApplication.translate("Form", u"Analyze...", None))
        self.pushButton_image_processing.setText(QCoreApplication.translate("Form", u"Image Processing...", None))
        self.pushButton_calibrate.setText(QCoreApplication.translate("Form", u"Calibrate...", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Histogram", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Image Attributes...", None))
        self.label.setText(QCoreApplication.translate("Form", u"Brightness", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Contrast", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Norm", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Colormap", None))
    # retranslateUi

