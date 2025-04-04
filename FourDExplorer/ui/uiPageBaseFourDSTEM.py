# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageBaseFourDSTEM.ui'
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
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QSpinBox,
    QSplitter,
    QVBoxLayout,
    QWidget,
)

from bin.Widgets.WidgetPlots import WidgetPlotDP


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(785, 503)
        self.verticalLayout_8 = QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_data_path = QLineEdit(self.widget)
        self.lineEdit_data_path.setObjectName("lineEdit_data_path")

        self.horizontalLayout.addWidget(self.lineEdit_data_path)

        self.pushButton_browse = QPushButton(self.widget)
        self.pushButton_browse.setObjectName("pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.widget_dp = WidgetPlotDP(self.widget)
        self.widget_dp.setObjectName("widget_dp")

        self.verticalLayout_3.addWidget(self.widget_dp)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spinBox_scan_ii = QSpinBox(self.widget)
        self.spinBox_scan_ii.setObjectName("spinBox_scan_ii")

        self.verticalLayout_2.addWidget(self.spinBox_scan_ii)

        self.spinBox_scan_jj = QSpinBox(self.widget)
        self.spinBox_scan_jj.setObjectName("spinBox_scan_jj")

        self.verticalLayout_2.addWidget(self.spinBox_scan_jj)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.setStretch(1, 1)
        self.splitter.addWidget(self.widget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalSlider_brightness = QSlider(self.layoutWidget)
        self.horizontalSlider_brightness.setObjectName("horizontalSlider_brightness")
        self.horizontalSlider_brightness.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_brightness)

        self.horizontalSlider_contrast = QSlider(self.layoutWidget)
        self.horizontalSlider_contrast.setObjectName("horizontalSlider_contrast")
        self.horizontalSlider_contrast.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_contrast)

        self.comboBox_normalize = QComboBox(self.layoutWidget)
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.setObjectName("comboBox_normalize")

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
        self.comboBox_colormap.setObjectName("comboBox_colormap")

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
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText(
            QCoreApplication.translate("Form", "4D-STEM data path", None)
        )
        self.pushButton_browse.setText(
            QCoreApplication.translate("Form", "Browse", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("Form", "DPi index (rows of location)", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("Form", "DPj index (columns of location)", None)
        )
        self.label_5.setText(QCoreApplication.translate("Form", "Brightness", None))
        self.label_6.setText(QCoreApplication.translate("Form", "Contrast", None))
        self.label_7.setText(QCoreApplication.translate("Form", "Norm", None))
        self.label_8.setText(QCoreApplication.translate("Form", "Color map", None))
        self.comboBox_normalize.setItemText(
            0, QCoreApplication.translate("Form", "Linear", None)
        )
        self.comboBox_normalize.setItemText(
            1, QCoreApplication.translate("Form", "Logarithm", None)
        )

        self.comboBox_colormap.setItemText(
            0, QCoreApplication.translate("Form", "viridis", None)
        )
        self.comboBox_colormap.setItemText(
            1, QCoreApplication.translate("Form", "plasma", None)
        )
        self.comboBox_colormap.setItemText(
            2, QCoreApplication.translate("Form", "gray", None)
        )
        self.comboBox_colormap.setItemText(
            3, QCoreApplication.translate("Form", "RdYlBu", None)
        )
        self.comboBox_colormap.setItemText(
            4, QCoreApplication.translate("Form", "twilight", None)
        )
        self.comboBox_colormap.setItemText(
            5, QCoreApplication.translate("Form", "hsv", None)
        )
        self.comboBox_colormap.setItemText(
            6, QCoreApplication.translate("Form", "jet", None)
        )
        self.comboBox_colormap.setItemText(
            7, QCoreApplication.translate("Form", "Others", None)
        )

    # retranslateUi
