# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageAlignFourDSTEM.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QSplitter, QStackedWidget, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

from bin.Widgets.WidgetMasks import WidgetMaskCircle
from bin.Widgets.WidgetPlots import WidgetPlotDP

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(905, 604)
        self.verticalLayout_10 = QVBoxLayout(Form)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
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

        self.verticalLayout_3.setStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_alignment = QWidget()
        self.tab_alignment.setObjectName(u"tab_alignment")
        self.verticalLayout_4 = QVBoxLayout(self.tab_alignment)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 9, 0, 0)
        self.comboBox_fine_tuning_mode = QComboBox(self.tab_alignment)
        self.comboBox_fine_tuning_mode.addItem("")
        self.comboBox_fine_tuning_mode.addItem("")
        self.comboBox_fine_tuning_mode.addItem("")
        self.comboBox_fine_tuning_mode.setObjectName(u"comboBox_fine_tuning_mode")

        self.verticalLayout_4.addWidget(self.comboBox_fine_tuning_mode)

        self.stackedWidget = QStackedWidget(self.tab_alignment)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_simple = QWidget()
        self.page_simple.setObjectName(u"page_simple")
        self.verticalLayout_6 = QVBoxLayout(self.page_simple)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.label_4 = QLabel(self.page_simple)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.page_simple)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.spinBox_simple_shift_i = QSpinBox(self.page_simple)
        self.spinBox_simple_shift_i.setObjectName(u"spinBox_simple_shift_i")

        self.horizontalLayout_5.addWidget(self.spinBox_simple_shift_i)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.page_simple)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.spinBox_simple_shift_j = QSpinBox(self.page_simple)
        self.spinBox_simple_shift_j.setObjectName(u"spinBox_simple_shift_j")

        self.horizontalLayout_6.addWidget(self.spinBox_simple_shift_j)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.checkBox_apply_coarse = QCheckBox(self.page_simple)
        self.checkBox_apply_coarse.setObjectName(u"checkBox_apply_coarse")

        self.verticalLayout_6.addWidget(self.checkBox_apply_coarse)

        self.verticalSpacer_3 = QSpacerItem(20, 81, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_up = QPushButton(self.page_simple)
        self.pushButton_up.setObjectName(u"pushButton_up")
        self.pushButton_up.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_up, 0, 1, 1, 1)

        self.pushButton_left = QPushButton(self.page_simple)
        self.pushButton_left.setObjectName(u"pushButton_left")
        self.pushButton_left.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_left, 1, 0, 1, 1)

        self.pushButton_down = QPushButton(self.page_simple)
        self.pushButton_down.setObjectName(u"pushButton_down")
        self.pushButton_down.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_down, 1, 1, 1, 1)

        self.pushButton_right = QPushButton(self.page_simple)
        self.pushButton_right.setObjectName(u"pushButton_right")
        self.pushButton_right.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_right, 1, 2, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.page_simple)
        self.page_reference = QWidget()
        self.page_reference.setObjectName(u"page_reference")
        self.verticalLayout_7 = QVBoxLayout(self.page_reference)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_5 = QSpacerItem(20, 63, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.label_9 = QLabel(self.page_reference)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_reference_com = QLineEdit(self.page_reference)
        self.lineEdit_reference_com.setObjectName(u"lineEdit_reference_com")

        self.horizontalLayout_2.addWidget(self.lineEdit_reference_com)

        self.pushButton_browse_reference_com = QPushButton(self.page_reference)
        self.pushButton_browse_reference_com.setObjectName(u"pushButton_browse_reference_com")

        self.horizontalLayout_2.addWidget(self.pushButton_browse_reference_com)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_6 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)

        self.checkBox_apply_reference = QCheckBox(self.page_reference)
        self.checkBox_apply_reference.setObjectName(u"checkBox_apply_reference")

        self.verticalLayout_7.addWidget(self.checkBox_apply_reference)

        self.verticalSpacer_4 = QSpacerItem(20, 63, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.page_reference)
        self.page_anchors = QWidget()
        self.page_anchors.setObjectName(u"page_anchors")
        self.verticalLayout_8 = QVBoxLayout(self.page_anchors)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.page_anchors)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_8.addWidget(self.label_13)

        self.tableView_anchors = QTableView(self.page_anchors)
        self.tableView_anchors.setObjectName(u"tableView_anchors")

        self.verticalLayout_8.addWidget(self.tableView_anchors)

        self.stackedWidget.addWidget(self.page_anchors)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.tabWidget.addTab(self.tab_alignment, "")
        self.tab_display_effect = QWidget()
        self.tab_display_effect.setObjectName(u"tab_display_effect")
        self.verticalLayout_5 = QVBoxLayout(self.tab_display_effect)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_circle = WidgetMaskCircle(self.tab_display_effect)
        self.widget_circle.setObjectName(u"widget_circle")

        self.verticalLayout_5.addWidget(self.widget_circle)

        self.tabWidget.addTab(self.tab_display_effect, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.horizontalSlider_brightness = QSlider(self.widget)
        self.horizontalSlider_brightness.setObjectName(u"horizontalSlider_brightness")
        self.horizontalSlider_brightness.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_brightness, 0, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.horizontalSlider_contrast = QSlider(self.widget)
        self.horizontalSlider_contrast.setObjectName(u"horizontalSlider_contrast")
        self.horizontalSlider_contrast.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_contrast, 1, 1, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.comboBox_normalize = QComboBox(self.widget)
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.addItem("")
        self.comboBox_normalize.setObjectName(u"comboBox_normalize")

        self.gridLayout_2.addWidget(self.comboBox_normalize, 2, 1, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

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

        self.gridLayout_2.addWidget(self.comboBox_colormap, 3, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_2)

        self.splitter.addWidget(self.widget)

        self.verticalLayout_10.addWidget(self.splitter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout_4.addWidget(self.pushButton_start)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.verticalLayout_10.setStretch(0, 1)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_right.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"4D-STEM data path", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"DPi index (rows of location)", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"DPj index (columns of location)", None))
        self.comboBox_fine_tuning_mode.setItemText(0, QCoreApplication.translate("Form", u"Coarse Alignment", None))
        self.comboBox_fine_tuning_mode.setItemText(1, QCoreApplication.translate("Form", u"Using Reference (CoM)", None))
        self.comboBox_fine_tuning_mode.setItemText(2, QCoreApplication.translate("Form", u"Using Translation Anchors", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"Beam spot translation", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Shift i-direct", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Shift j-direct", None))
        self.checkBox_apply_coarse.setText(QCoreApplication.translate("Form", u"Apply Alignment", None))
        self.pushButton_up.setText(QCoreApplication.translate("Form", u"\u2191", None))
        self.pushButton_left.setText(QCoreApplication.translate("Form", u"\u2190", None))
        self.pushButton_down.setText(QCoreApplication.translate("Form", u"\u2193", None))
        self.pushButton_right.setText(QCoreApplication.translate("Form", u"\u2192", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Reference Center of Mass", None))
        self.pushButton_browse_reference_com.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.checkBox_apply_reference.setText(QCoreApplication.translate("Form", u"Apply Alignment", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Translation Anchors", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_alignment), QCoreApplication.translate("Form", u"Alignment", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_display_effect), QCoreApplication.translate("Form", u"Displaying Effect", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Brightness", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Contrast", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Norm", None))
        self.comboBox_normalize.setItemText(0, QCoreApplication.translate("Form", u"Linear", None))
        self.comboBox_normalize.setItemText(1, QCoreApplication.translate("Form", u"Logarithm", None))

        self.label_8.setText(QCoreApplication.translate("Form", u"Color map", None))
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

