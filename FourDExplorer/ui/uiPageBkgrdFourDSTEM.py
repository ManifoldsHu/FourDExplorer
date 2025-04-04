# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageBkgrdFourDSTEM.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QSpinBox,
    QSplitter,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from bin.Widgets.WidgetPlots import WidgetPlotDP, WidgetPlotHist


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(896, 704)
        self.verticalLayout_8 = QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_data_path = QLineEdit(self.layoutWidget)
        self.lineEdit_data_path.setObjectName("lineEdit_data_path")

        self.horizontalLayout.addWidget(self.lineEdit_data_path)

        self.pushButton_browse = QPushButton(self.layoutWidget)
        self.pushButton_browse.setObjectName("pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.widget_dp = WidgetPlotDP(self.layoutWidget)
        self.widget_dp.setObjectName("widget_dp")

        self.verticalLayout_3.addWidget(self.widget_dp)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spinBox_scan_ii = QSpinBox(self.layoutWidget)
        self.spinBox_scan_ii.setObjectName("spinBox_scan_ii")

        self.verticalLayout_2.addWidget(self.spinBox_scan_ii)

        self.spinBox_scan_jj = QSpinBox(self.layoutWidget)
        self.spinBox_scan_jj.setObjectName("spinBox_scan_jj")

        self.verticalLayout_2.addWidget(self.spinBox_scan_jj)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.setStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_background_path = QLineEdit(self.tab)
        self.lineEdit_background_path.setObjectName("lineEdit_background_path")

        self.horizontalLayout_2.addWidget(self.lineEdit_background_path)

        self.pushButton_browse_background = QPushButton(self.tab)
        self.pushButton_browse_background.setObjectName("pushButton_browse_background")

        self.horizontalLayout_2.addWidget(self.pushButton_browse_background)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.checkBox_apply_subtraction = QCheckBox(self.tab)
        self.checkBox_apply_subtraction.setObjectName("checkBox_apply_subtraction")

        self.verticalLayout_6.addWidget(self.checkBox_apply_subtraction)

        self.verticalSpacer = QSpacerItem(
            20, 447, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab, "")
        self.tab_window_filter = QWidget()
        self.tab_window_filter.setObjectName("tab_window_filter")
        self.verticalLayout_5 = QVBoxLayout(self.tab_window_filter)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_hist = WidgetPlotHist(self.tab_window_filter)
        self.widget_hist.setObjectName("widget_hist")

        self.verticalLayout_4.addWidget(self.widget_hist)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QLabel(self.tab_window_filter)
        self.label_9.setObjectName("label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.doubleSpinBox_window_min = QDoubleSpinBox(self.tab_window_filter)
        self.doubleSpinBox_window_min.setObjectName("doubleSpinBox_window_min")

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_window_min)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QLabel(self.tab_window_filter)
        self.label_10.setObjectName("label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox_window_max = QDoubleSpinBox(self.tab_window_filter)
        self.doubleSpinBox_window_max.setObjectName("doubleSpinBox_window_max")

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_window_max)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.checkBox_apply_window_min = QCheckBox(self.tab_window_filter)
        self.checkBox_apply_window_min.setObjectName("checkBox_apply_window_min")

        self.verticalLayout_4.addWidget(self.checkBox_apply_window_min)

        self.checkBox_apply_window_max = QCheckBox(self.tab_window_filter)
        self.checkBox_apply_window_max.setObjectName("checkBox_apply_window_max")

        self.verticalLayout_4.addWidget(self.checkBox_apply_window_max)

        self.verticalLayout_4.setStretch(0, 1)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab_window_filter, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName("label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.horizontalSlider_brightness = QSlider(self.widget)
        self.horizontalSlider_brightness.setObjectName("horizontalSlider_brightness")
        self.horizontalSlider_brightness.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_brightness, 0, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName("label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.horizontalSlider_contrast = QSlider(self.widget)
        self.horizontalSlider_contrast.setObjectName("horizontalSlider_contrast")
        self.horizontalSlider_contrast.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_contrast, 1, 1, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName("label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.comboBox_normalize = QComboBox(self.widget)
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.setObjectName("comboBox_normalize")

        self.gridLayout.addWidget(self.comboBox_normalize, 2, 1, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName("label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

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

        self.verticalLayout_7.addLayout(self.gridLayout)

        self.splitter.addWidget(self.widget)

        self.verticalLayout_8.addWidget(self.splitter)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName("pushButton_start")

        self.horizontalLayout_7.addWidget(self.pushButton_start)

        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)

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
        self.label_4.setText(
            QCoreApplication.translate("Form", "Background Path", None)
        )
        self.pushButton_browse_background.setText(
            QCoreApplication.translate("Form", "Browse", None)
        )
        self.checkBox_apply_subtraction.setText(
            QCoreApplication.translate("Form", "Apply Background Subtraction", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("Form", "Subtract Reference", None),
        )
        self.label_9.setText(
            QCoreApplication.translate("Form", "Window Min Value", None)
        )
        self.label_10.setText(
            QCoreApplication.translate("Form", "Window Max Value", None)
        )
        self.checkBox_apply_window_min.setText(
            QCoreApplication.translate("Form", "Applying Window (Min Constrain)", None)
        )
        self.checkBox_apply_window_max.setText(
            QCoreApplication.translate("Form", "Applying Window (Max Constrain)", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_window_filter),
            QCoreApplication.translate("Form", "Select Window Filter", None),
        )
        self.label_5.setText(QCoreApplication.translate("Form", "Brightness", None))
        self.label_6.setText(QCoreApplication.translate("Form", "Contrast", None))
        self.label_7.setText(QCoreApplication.translate("Form", "Norm", None))
        self.comboBox_normalize.setItemText(
            0, QCoreApplication.translate("Form", "Linear", None)
        )
        self.comboBox_normalize.setItemText(
            1, QCoreApplication.translate("Form", "Logarithm", None)
        )

        self.label_8.setText(QCoreApplication.translate("Form", "Color map", None))
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
