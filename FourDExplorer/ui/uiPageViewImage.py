# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageViewImage.ui'
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
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSplitter,
    QVBoxLayout,
    QWidget,
)

from bin.Widgets.WidgetPlots import WidgetPlotHist, WidgetPlotImage


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(859, 636)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_image_path = QLineEdit(self.layoutWidget)
        self.lineEdit_image_path.setObjectName("lineEdit_image_path")

        self.horizontalLayout_3.addWidget(self.lineEdit_image_path)

        self.pushButton_browse = QPushButton(self.layoutWidget)
        self.pushButton_browse.setObjectName("pushButton_browse")

        self.horizontalLayout_3.addWidget(self.pushButton_browse)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.widget_image = WidgetPlotImage(self.layoutWidget)
        self.widget_image.setObjectName("widget_image")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_image.sizePolicy().hasHeightForWidth())
        self.widget_image.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.widget_image)

        self.verticalLayout_5.setStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.label_4)

        self.widget_hist_view = WidgetPlotHist(self.widget)
        self.widget_hist_view.setObjectName("widget_hist_view")
        sizePolicy.setHeightForWidth(
            self.widget_hist_view.sizePolicy().hasHeightForWidth()
        )
        self.widget_hist_view.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.widget_hist_view)

        self.verticalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSlider_brightness = QSlider(self.widget)
        self.horizontalSlider_brightness.setObjectName("horizontalSlider_brightness")
        self.horizontalSlider_brightness.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_brightness, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalSlider_contrast = QSlider(self.widget)
        self.horizontalSlider_contrast.setObjectName("horizontalSlider_contrast")
        self.horizontalSlider_contrast.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_contrast, 1, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName("label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.comboBox_normalize = QComboBox(self.widget)
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.setObjectName("comboBox_normalize")

        self.gridLayout.addWidget(self.comboBox_normalize, 2, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName("label_6")

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
        self.comboBox_colormap.setObjectName("comboBox_colormap")

        self.gridLayout.addWidget(self.comboBox_colormap, 3, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.splitter.addWidget(self.widget)

        self.verticalLayout_2.addWidget(self.splitter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", "Image Path", None))
        self.pushButton_browse.setText(
            QCoreApplication.translate("Form", "Browse", None)
        )
        self.label_4.setText(QCoreApplication.translate("Form", "Histogram", None))
        self.label.setText(QCoreApplication.translate("Form", "Brightness", None))
        self.label_2.setText(QCoreApplication.translate("Form", "Contrast", None))
        self.label_5.setText(QCoreApplication.translate("Form", "Norm", None))
        self.comboBox_normalize.setItemText(
            0, QCoreApplication.translate("Form", "Linear", None)
        )
        self.comboBox_normalize.setItemText(
            1, QCoreApplication.translate("Form", "Logrithm", None)
        )

        self.label_6.setText(QCoreApplication.translate("Form", "Colormap", None))
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
