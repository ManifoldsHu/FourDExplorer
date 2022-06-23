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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QSplitter, QVBoxLayout, QWidget)

from bin.Widgets.WidgetPlots import (WidgetPlotHist, WidgetPlotImage)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(859, 636)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_image_path = QLineEdit(self.layoutWidget)
        self.lineEdit_image_path.setObjectName(u"lineEdit_image_path")

        self.horizontalLayout_3.addWidget(self.lineEdit_image_path)

        self.pushButton_browse = QPushButton(self.layoutWidget)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout_3.addWidget(self.pushButton_browse)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.widget_image = WidgetPlotImage(self.layoutWidget)
        self.widget_image.setObjectName(u"widget_image")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_image.sizePolicy().hasHeightForWidth())
        self.widget_image.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.widget_image)

        self.verticalLayout_5.setStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.label_4)

        self.widget_hist_view = WidgetPlotHist(self.widget)
        self.widget_hist_view.setObjectName(u"widget_hist_view")
        sizePolicy.setHeightForWidth(self.widget_hist_view.sizePolicy().hasHeightForWidth())
        self.widget_hist_view.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.widget_hist_view)

        self.verticalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSlider_brightness = QSlider(self.widget)
        self.horizontalSlider_brightness.setObjectName(u"horizontalSlider_brightness")
        self.horizontalSlider_brightness.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_brightness, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalSlider_contrast = QSlider(self.widget)
        self.horizontalSlider_contrast.setObjectName(u"horizontalSlider_contrast")
        self.horizontalSlider_contrast.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_contrast, 1, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.comboBox_normalize = QComboBox(self.widget)
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.setObjectName(u"comboBox_normalize")

        self.gridLayout.addWidget(self.comboBox_normalize, 2, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.comboBox_colormap = QComboBox(self.widget)
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.setObjectName(u"comboBox_colormap")

        self.gridLayout.addWidget(self.comboBox_colormap, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.splitter.addWidget(self.widget)

        self.verticalLayout_2.addWidget(self.splitter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Image Path", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Histogram", None))
        self.label.setText(QCoreApplication.translate("Form", u"Brightness", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Contrast", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Norm", None))
        self.comboBox_normalize.setItemText(0, QCoreApplication.translate("Form", u"Linear", None))
        self.comboBox_normalize.setItemText(1, QCoreApplication.translate("Form", u"Logrithm", None))

        self.label_6.setText(QCoreApplication.translate("Form", u"Colormap", None))
        self.comboBox_colormap.setItemText(0, QCoreApplication.translate("Form", u"viridis", None))
        self.comboBox_colormap.setItemText(1, QCoreApplication.translate("Form", u"plasma", None))
        self.comboBox_colormap.setItemText(2, QCoreApplication.translate("Form", u"gray", None))
        self.comboBox_colormap.setItemText(3, QCoreApplication.translate("Form", u"RdYlBu", None))
        self.comboBox_colormap.setItemText(4, QCoreApplication.translate("Form", u"twilight", None))
        self.comboBox_colormap.setItemText(5, QCoreApplication.translate("Form", u"hsv", None))
        self.comboBox_colormap.setItemText(6, QCoreApplication.translate("Form", u"jet", None))
        self.comboBox_colormap.setItemText(7, QCoreApplication.translate("Form", u"Others", None))

    # retranslateUi

