# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageRotateFourDSTEM.ui'
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
    QToolButton,
    QVBoxLayout,
    QWidget,
)

from bin.Widgets.WidgetPlots import WidgetPlotDP, WidgetPlotImage, WidgetPlotQuiver


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(913, 744)
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
        self.tab_UseCoM = QWidget()
        self.tab_UseCoM.setObjectName("tab_UseCoM")
        self.verticalLayout_5 = QVBoxLayout(self.tab_UseCoM)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QLabel(self.tab_UseCoM)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEdit_vector_field_path = QLineEdit(self.tab_UseCoM)
        self.lineEdit_vector_field_path.setObjectName("lineEdit_vector_field_path")

        self.horizontalLayout_6.addWidget(self.lineEdit_vector_field_path)

        self.pushButton_browse_vector_field = QPushButton(self.tab_UseCoM)
        self.pushButton_browse_vector_field.setObjectName(
            "pushButton_browse_vector_field"
        )

        self.horizontalLayout_6.addWidget(self.pushButton_browse_vector_field)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.widget_vector_field = WidgetPlotQuiver(self.tab_UseCoM)
        self.widget_vector_field.setObjectName("widget_vector_field")
        self.widget_vector_field.setMinimumSize(QSize(0, 400))

        self.verticalLayout_4.addWidget(self.widget_vector_field)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QLabel(self.tab_UseCoM)
        self.label_9.setObjectName("label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.doubleSpinBox_rotation_angle_quiver = QDoubleSpinBox(self.tab_UseCoM)
        self.doubleSpinBox_rotation_angle_quiver.setObjectName(
            "doubleSpinBox_rotation_angle_quiver"
        )

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_rotation_angle_quiver)

        self.toolButton_refresh_quiver = QToolButton(self.tab_UseCoM)
        self.toolButton_refresh_quiver.setObjectName("toolButton_refresh_quiver")

        self.horizontalLayout_4.addWidget(self.toolButton_refresh_quiver)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.pushButton_calculate_rotation_angle = QPushButton(self.tab_UseCoM)
        self.pushButton_calculate_rotation_angle.setObjectName(
            "pushButton_calculate_rotation_angle"
        )

        self.verticalLayout_4.addWidget(self.pushButton_calculate_rotation_angle)

        self.pushButton_adjust_quiver_effects = QPushButton(self.tab_UseCoM)
        self.pushButton_adjust_quiver_effects.setObjectName(
            "pushButton_adjust_quiver_effects"
        )

        self.verticalLayout_4.addWidget(self.pushButton_adjust_quiver_effects)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab_UseCoM, "")
        self.tab_UseAxialBF = QWidget()
        self.tab_UseAxialBF.setObjectName("tab_UseAxialBF")
        self.verticalLayout_6 = QVBoxLayout(self.tab_UseAxialBF)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QLabel(self.tab_UseAxialBF)
        self.label_10.setObjectName("label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.lineEdit_axial_bf_path = QLineEdit(self.tab_UseAxialBF)
        self.lineEdit_axial_bf_path.setObjectName("lineEdit_axial_bf_path")

        self.horizontalLayout_2.addWidget(self.lineEdit_axial_bf_path)

        self.pushButton_browse_axial_bf = QPushButton(self.tab_UseAxialBF)
        self.pushButton_browse_axial_bf.setObjectName("pushButton_browse_axial_bf")

        self.horizontalLayout_2.addWidget(self.pushButton_browse_axial_bf)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.widget_axial_bf = WidgetPlotImage(self.tab_UseAxialBF)
        self.widget_axial_bf.setObjectName("widget_axial_bf")

        self.verticalLayout_6.addWidget(self.widget_axial_bf)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QLabel(self.tab_UseAxialBF)
        self.label_11.setObjectName("label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.doubleSpinBox_rotation_angle_axial_bf = QDoubleSpinBox(self.tab_UseAxialBF)
        self.doubleSpinBox_rotation_angle_axial_bf.setObjectName(
            "doubleSpinBox_rotation_angle_axial_bf"
        )

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_rotation_angle_axial_bf)

        self.toolButton_refresh_axial_bf = QToolButton(self.tab_UseAxialBF)
        self.toolButton_refresh_axial_bf.setObjectName("toolButton_refresh_axial_bf")

        self.horizontalLayout_5.addWidget(self.toolButton_refresh_axial_bf)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.pushButton_calculate_rotation_angle_axial_bf = QPushButton(
            self.tab_UseAxialBF
        )
        self.pushButton_calculate_rotation_angle_axial_bf.setObjectName(
            "pushButton_calculate_rotation_angle_axial_bf"
        )

        self.verticalLayout_6.addWidget(
            self.pushButton_calculate_rotation_angle_axial_bf
        )

        self.verticalLayout_6.setStretch(1, 1)
        self.tabWidget.addTab(self.tab_UseAxialBF, "")

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
        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

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
            QCoreApplication.translate("Form", "Vector Field Path", None)
        )
        self.pushButton_browse_vector_field.setText(
            QCoreApplication.translate("Form", "Browse", None)
        )
        self.label_9.setText(QCoreApplication.translate("Form", "Rotation Angle", None))
        self.toolButton_refresh_quiver.setText("")
        self.pushButton_calculate_rotation_angle.setText(
            QCoreApplication.translate("Form", "Calculate Rotation Angle", None)
        )
        self.pushButton_adjust_quiver_effects.setText(
            QCoreApplication.translate("Form", "Adjust Quiver Effects", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_UseCoM),
            QCoreApplication.translate("Form", "CoM Method", None),
        )
        self.label_10.setText(QCoreApplication.translate("Form", "Axial BF Path", None))
        self.pushButton_browse_axial_bf.setText(
            QCoreApplication.translate("Form", "Browse", None)
        )
        self.label_11.setText(
            QCoreApplication.translate("Form", "Rotation Angle", None)
        )
        self.toolButton_refresh_axial_bf.setText("")
        self.pushButton_calculate_rotation_angle_axial_bf.setText(
            QCoreApplication.translate("Form", "Calculate Rotation Angle", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_UseAxialBF),
            QCoreApplication.translate("Form", "Axial BF Method", None),
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
            QCoreApplication.translate(
                "Form", "Apply Rotation and Start Calculation ", None
            )
        )

    # retranslateUi
