# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageVirtualImage.ui'
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
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from bin.Widgets.WidgetMasks import (
    WidgetMaskCircle,
    WidgetMaskEllipse,
    WidgetMaskPolygon,
    WidgetMaskRectangle,
    WidgetMaskRing,
    WidgetMaskSegment,
    WidgetMaskWedge,
)
from bin.Widgets.WidgetPlots import WidgetPlotDP


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(939, 673)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
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
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.comboBox_mode = QComboBox(self.widget1)
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.setObjectName("comboBox_mode")

        self.horizontalLayout_4.addWidget(self.comboBox_mode)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.stackedWidget_masks = QStackedWidget(self.widget1)
        self.stackedWidget_masks.setObjectName("stackedWidget_masks")
        self.stackedWidget_masks.setLineWidth(0)
        self.page_circle = WidgetMaskCircle()
        self.page_circle.setObjectName("page_circle")
        self.stackedWidget_masks.addWidget(self.page_circle)
        self.page_ring = WidgetMaskRing()
        self.page_ring.setObjectName("page_ring")
        self.stackedWidget_masks.addWidget(self.page_ring)
        self.page_wedge = WidgetMaskWedge()
        self.page_wedge.setObjectName("page_wedge")
        self.stackedWidget_masks.addWidget(self.page_wedge)
        self.page_rectangle = WidgetMaskRectangle()
        self.page_rectangle.setObjectName("page_rectangle")
        self.stackedWidget_masks.addWidget(self.page_rectangle)
        self.page_ellipse = WidgetMaskEllipse()
        self.page_ellipse.setObjectName("page_ellipse")
        self.stackedWidget_masks.addWidget(self.page_ellipse)
        self.page_polygon = WidgetMaskPolygon()
        self.page_polygon.setObjectName("page_polygon")
        self.stackedWidget_masks.addWidget(self.page_polygon)
        self.page_segment_ring = WidgetMaskSegment()
        self.page_segment_ring.setObjectName("page_segment_ring")
        self.stackedWidget_masks.addWidget(self.page_segment_ring)

        self.verticalLayout_4.addWidget(self.stackedWidget_masks)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName("label_9")

        self.verticalLayout_6.addWidget(self.label_9)

        self.label_10 = QLabel(self.widget1)
        self.label_10.setObjectName("label_10")

        self.verticalLayout_6.addWidget(self.label_10)

        self.label_11 = QLabel(self.widget1)
        self.label_11.setObjectName("label_11")

        self.verticalLayout_6.addWidget(self.label_11)

        self.label_12 = QLabel(self.widget1)
        self.label_12.setObjectName("label_12")

        self.verticalLayout_6.addWidget(self.label_12)

        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalSlider_brightness = QSlider(self.widget1)
        self.horizontalSlider_brightness.setObjectName("horizontalSlider_brightness")
        self.horizontalSlider_brightness.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.horizontalSlider_brightness)

        self.horizontalSlider_contrast = QSlider(self.widget1)
        self.horizontalSlider_contrast.setObjectName("horizontalSlider_contrast")
        self.horizontalSlider_contrast.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.horizontalSlider_contrast)

        self.comboBox_normalize = QComboBox(self.widget1)
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.setObjectName("comboBox_normalize")

        self.verticalLayout_7.addWidget(self.comboBox_normalize)

        self.comboBox_colormap = QComboBox(self.widget1)
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.addItem("")
        self.comboBox_colormap.setObjectName("comboBox_colormap")

        self.verticalLayout_7.addWidget(self.comboBox_colormap)

        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalLayout_4.setStretch(1, 1)
        self.splitter.addWidget(self.widget1)

        self.verticalLayout_5.addWidget(self.splitter)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(
            598, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName("pushButton_start")

        self.horizontalLayout_6.addWidget(self.pushButton_start)

        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalLayout_5.setStretch(0, 1)

        self.retranslateUi(Form)

        self.stackedWidget_masks.setCurrentIndex(0)

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
        self.label_4.setText(QCoreApplication.translate("Form", "Domain Shape", None))
        self.comboBox_mode.setItemText(
            0, QCoreApplication.translate("Form", "Circle (Bright Field)", None)
        )
        self.comboBox_mode.setItemText(
            1, QCoreApplication.translate("Form", "Ring (Annular Dark Field)", None)
        )
        self.comboBox_mode.setItemText(
            2, QCoreApplication.translate("Form", "Wedge", None)
        )
        self.comboBox_mode.setItemText(
            3, QCoreApplication.translate("Form", "Rectangle", None)
        )
        self.comboBox_mode.setItemText(
            4, QCoreApplication.translate("Form", "Ellipse", None)
        )
        self.comboBox_mode.setItemText(
            5, QCoreApplication.translate("Form", "Polygon", None)
        )
        self.comboBox_mode.setItemText(
            6, QCoreApplication.translate("Form", "Segmented Ring", None)
        )

        self.label_9.setText(QCoreApplication.translate("Form", "Brightness", None))
        self.label_10.setText(QCoreApplication.translate("Form", "Contrast", None))
        self.label_11.setText(QCoreApplication.translate("Form", "Norm", None))
        self.label_12.setText(QCoreApplication.translate("Form", "Color map", None))
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

        self.pushButton_start.setText(
            QCoreApplication.translate("Form", "Start Calculation", None)
        )

    # retranslateUi
