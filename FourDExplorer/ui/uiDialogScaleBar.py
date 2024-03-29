# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogScaleBar.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QDoubleSpinBox, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(370, 348)
        self.verticalLayout_11 = QVBoxLayout(Dialog)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_basic = QWidget()
        self.tab_basic.setObjectName(u"tab_basic")
        self.verticalLayout_5 = QVBoxLayout(self.tab_basic)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.tab_basic)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.doubleSpinBox_bar_length = QDoubleSpinBox(self.tab_basic)
        self.doubleSpinBox_bar_length.setObjectName(u"doubleSpinBox_bar_length")
        self.doubleSpinBox_bar_length.setMinimum(0.010000000000000)
        self.doubleSpinBox_bar_length.setMaximum(9999.989999999999782)
        self.doubleSpinBox_bar_length.setValue(1.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_bar_length)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.stackedWidget = QStackedWidget(self.tab_basic)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page_basic_reciprocal_space = QWidget()
        self.page_basic_reciprocal_space.setObjectName(u"page_basic_reciprocal_space")
        self.verticalLayout = QVBoxLayout(self.page_basic_reciprocal_space)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_25 = QLabel(self.page_basic_reciprocal_space)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_2.addWidget(self.label_25)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.comboBox_reciprocal_unit = QComboBox(self.page_basic_reciprocal_space)
        self.comboBox_reciprocal_unit.addItem("")
        self.comboBox_reciprocal_unit.addItem("")
        self.comboBox_reciprocal_unit.addItem("")
        self.comboBox_reciprocal_unit.addItem("")
        self.comboBox_reciprocal_unit.addItem("")
        self.comboBox_reciprocal_unit.setObjectName(u"comboBox_reciprocal_unit")

        self.horizontalLayout_2.addWidget(self.comboBox_reciprocal_unit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 163, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_basic_reciprocal_space)
        self.page_basic_real_space = QWidget()
        self.page_basic_real_space.setObjectName(u"page_basic_real_space")
        self.verticalLayout_2 = QVBoxLayout(self.page_basic_real_space)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.page_basic_real_space)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.comboBox_real_length_unit = QComboBox(self.page_basic_real_space)
        self.comboBox_real_length_unit.addItem("")
        self.comboBox_real_length_unit.addItem("")
        self.comboBox_real_length_unit.addItem("")
        self.comboBox_real_length_unit.addItem("")
        self.comboBox_real_length_unit.addItem("")
        self.comboBox_real_length_unit.setObjectName(u"comboBox_real_length_unit")

        self.horizontalLayout.addWidget(self.comboBox_real_length_unit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 163, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_basic_real_space)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_24 = QVBoxLayout(self.page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_22 = QLabel(self.page)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_12.addWidget(self.label_22)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.label_28 = QLabel(self.page)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_12.addWidget(self.label_28)


        self.verticalLayout_24.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_9 = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_9)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_customize_scale = QCheckBox(self.tab_basic)
        self.checkBox_customize_scale.setObjectName(u"checkBox_customize_scale")

        self.horizontalLayout_3.addWidget(self.checkBox_customize_scale)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.tab_basic)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.label_8 = QLabel(self.tab_basic)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_7 = QSpacerItem(13, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.doubleSpinBox_length_per_pixel = QDoubleSpinBox(self.tab_basic)
        self.doubleSpinBox_length_per_pixel.setObjectName(u"doubleSpinBox_length_per_pixel")
        self.doubleSpinBox_length_per_pixel.setDecimals(6)
        self.doubleSpinBox_length_per_pixel.setMinimum(0.000001000000000)
        self.doubleSpinBox_length_per_pixel.setMaximum(99999999.000000000000000)

        self.verticalLayout_4.addWidget(self.doubleSpinBox_length_per_pixel)

        self.lineEdit_custom_unit = QLineEdit(self.tab_basic)
        self.lineEdit_custom_unit.setObjectName(u"lineEdit_custom_unit")

        self.verticalLayout_4.addWidget(self.lineEdit_custom_unit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.tab_basic, "")
        self.tab_style = QWidget()
        self.tab_style.setObjectName(u"tab_style")
        self.verticalLayout_6 = QVBoxLayout(self.tab_style)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_19 = QLabel(self.tab_style)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_7.addWidget(self.label_19)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_16)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.tab_style)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 0, 1, 1, 1)

        self.doubleSpinBox_bar_width = QDoubleSpinBox(self.tab_style)
        self.doubleSpinBox_bar_width.setObjectName(u"doubleSpinBox_bar_width")

        self.gridLayout_2.addWidget(self.doubleSpinBox_bar_width, 0, 2, 1, 1)

        self.label_4 = QLabel(self.tab_style)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 1, 1, 1, 1)

        self.comboBox_bar_location = QComboBox(self.tab_style)
        self.comboBox_bar_location.addItem("")
        self.comboBox_bar_location.addItem("")
        self.comboBox_bar_location.addItem("")
        self.comboBox_bar_location.addItem("")
        self.comboBox_bar_location.addItem("")
        self.comboBox_bar_location.addItem("")
        self.comboBox_bar_location.addItem("")
        self.comboBox_bar_location.addItem("")
        self.comboBox_bar_location.addItem("")
        self.comboBox_bar_location.addItem("")
        self.comboBox_bar_location.setObjectName(u"comboBox_bar_location")

        self.gridLayout_2.addWidget(self.comboBox_bar_location, 1, 2, 1, 1)

        self.label_14 = QLabel(self.tab_style)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 2, 1, 1, 1)

        self.doubleSpinBox_bar_location_i = QDoubleSpinBox(self.tab_style)
        self.doubleSpinBox_bar_location_i.setObjectName(u"doubleSpinBox_bar_location_i")

        self.gridLayout_2.addWidget(self.doubleSpinBox_bar_location_i, 2, 2, 1, 1)

        self.label_15 = QLabel(self.tab_style)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_12, 3, 1, 1, 1)

        self.doubleSpinBox_bar_location_j = QDoubleSpinBox(self.tab_style)
        self.doubleSpinBox_bar_location_j.setObjectName(u"doubleSpinBox_bar_location_j")

        self.gridLayout_2.addWidget(self.doubleSpinBox_bar_location_j, 3, 2, 1, 1)

        self.label_20 = QLabel(self.tab_style)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 4, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_13, 4, 1, 1, 1)

        self.spinBox_bar_rotation = QSpinBox(self.tab_style)
        self.spinBox_bar_rotation.setObjectName(u"spinBox_bar_rotation")
        self.spinBox_bar_rotation.setMinimum(-360)
        self.spinBox_bar_rotation.setMaximum(360)

        self.gridLayout_2.addWidget(self.spinBox_bar_rotation, 4, 2, 1, 1)

        self.label_3 = QLabel(self.tab_style)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_14, 5, 1, 1, 1)

        self.comboBox_bar_color = QComboBox(self.tab_style)
        self.comboBox_bar_color.addItem("")
        self.comboBox_bar_color.addItem("")
        self.comboBox_bar_color.addItem("")
        self.comboBox_bar_color.addItem("")
        self.comboBox_bar_color.addItem("")
        self.comboBox_bar_color.addItem("")
        self.comboBox_bar_color.addItem("")
        self.comboBox_bar_color.addItem("")
        self.comboBox_bar_color.addItem("")
        self.comboBox_bar_color.addItem("")
        self.comboBox_bar_color.addItem("")
        self.comboBox_bar_color.addItem("")
        self.comboBox_bar_color.setObjectName(u"comboBox_bar_color")

        self.gridLayout_2.addWidget(self.comboBox_bar_color, 5, 2, 1, 1)

        self.label_5 = QLabel(self.tab_style)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_15, 6, 1, 1, 1)

        self.doubleSpinBox_bar_alpha = QDoubleSpinBox(self.tab_style)
        self.doubleSpinBox_bar_alpha.setObjectName(u"doubleSpinBox_bar_alpha")
        self.doubleSpinBox_bar_alpha.setMaximum(1.000000000000000)
        self.doubleSpinBox_bar_alpha.setSingleStep(0.100000000000000)
        self.doubleSpinBox_bar_alpha.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_bar_alpha, 6, 2, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_2)

        self.verticalSpacer_6 = QSpacerItem(20, 9, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.checkBox_bar_visible = QCheckBox(self.tab_style)
        self.checkBox_bar_visible.setObjectName(u"checkBox_bar_visible")

        self.verticalLayout_6.addWidget(self.checkBox_bar_visible)

        self.tabWidget.addTab(self.tab_style, "")
        self.tab_text = QWidget()
        self.tab_text.setObjectName(u"tab_text")
        self.verticalLayout_23 = QVBoxLayout(self.tab_text)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.tabWidget_2 = QTabWidget(self.tab_text)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_text_location = QWidget()
        self.tab_text_location.setObjectName(u"tab_text_location")
        self.verticalLayout_14 = QVBoxLayout(self.tab_text_location)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.tab_text_location)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_18)

        self.checkBox_text_follow_bar = QCheckBox(self.tab_text_location)
        self.checkBox_text_follow_bar.setObjectName(u"checkBox_text_follow_bar")

        self.horizontalLayout_9.addWidget(self.checkBox_text_follow_bar)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_13 = QLabel(self.tab_text_location)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_7.addWidget(self.label_13)

        self.label_16 = QLabel(self.tab_text_location)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_7.addWidget(self.label_16)


        self.horizontalLayout_10.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_19)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.doubleSpinBox_text_location_i = QDoubleSpinBox(self.tab_text_location)
        self.doubleSpinBox_text_location_i.setObjectName(u"doubleSpinBox_text_location_i")
        self.doubleSpinBox_text_location_i.setMaximum(999999.989999999990687)

        self.verticalLayout_8.addWidget(self.doubleSpinBox_text_location_i)

        self.doubleSpinBox_text_location_j = QDoubleSpinBox(self.tab_text_location)
        self.doubleSpinBox_text_location_j.setObjectName(u"doubleSpinBox_text_location_j")
        self.doubleSpinBox_text_location_j.setMaximum(999999.989999999990687)

        self.verticalLayout_8.addWidget(self.doubleSpinBox_text_location_j)


        self.horizontalLayout_10.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)


        self.verticalLayout_14.addLayout(self.verticalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.tab_text_location)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_10.addWidget(self.label_11)

        self.label_12 = QLabel(self.tab_text_location)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_10.addWidget(self.label_12)

        self.label_17 = QLabel(self.tab_text_location)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_10.addWidget(self.label_17)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_21)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_22)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_23)


        self.horizontalLayout_6.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.comboBox_text_ha = QComboBox(self.tab_text_location)
        self.comboBox_text_ha.addItem("")
        self.comboBox_text_ha.addItem("")
        self.comboBox_text_ha.addItem("")
        self.comboBox_text_ha.setObjectName(u"comboBox_text_ha")

        self.verticalLayout_13.addWidget(self.comboBox_text_ha)

        self.comboBox_text_va = QComboBox(self.tab_text_location)
        self.comboBox_text_va.addItem("")
        self.comboBox_text_va.addItem("")
        self.comboBox_text_va.addItem("")
        self.comboBox_text_va.addItem("")
        self.comboBox_text_va.setObjectName(u"comboBox_text_va")

        self.verticalLayout_13.addWidget(self.comboBox_text_va)

        self.spinBox_text_rotation = QSpinBox(self.tab_text_location)
        self.spinBox_text_rotation.setObjectName(u"spinBox_text_rotation")
        self.spinBox_text_rotation.setMinimum(-360)
        self.spinBox_text_rotation.setMaximum(360)

        self.verticalLayout_13.addWidget(self.spinBox_text_rotation)


        self.horizontalLayout_6.addLayout(self.verticalLayout_13)


        self.verticalLayout_14.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_8 = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_8)

        self.tabWidget_2.addTab(self.tab_text_location, "")
        self.tab_text_font = QWidget()
        self.tab_text_font.setObjectName(u"tab_text_font")
        self.verticalLayout_17 = QVBoxLayout(self.tab_text_font)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_26 = QLabel(self.tab_text_font)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_15.addWidget(self.label_26)

        self.label_21 = QLabel(self.tab_text_font)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_15.addWidget(self.label_21)

        self.label_30 = QLabel(self.tab_text_font)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_15.addWidget(self.label_30)

        self.label_18 = QLabel(self.tab_text_font)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_15.addWidget(self.label_18)

        self.label_7 = QLabel(self.tab_text_font)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_15.addWidget(self.label_7)


        self.horizontalLayout_13.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_24)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.comboBox_text_font_family = QComboBox(self.tab_text_font)
        self.comboBox_text_font_family.addItem("")
        self.comboBox_text_font_family.addItem("")
        self.comboBox_text_font_family.addItem("")
        self.comboBox_text_font_family.addItem("")
        self.comboBox_text_font_family.addItem("")
        self.comboBox_text_font_family.setObjectName(u"comboBox_text_font_family")

        self.verticalLayout_16.addWidget(self.comboBox_text_font_family)

        self.spinBox_text_font_size = QSpinBox(self.tab_text_font)
        self.spinBox_text_font_size.setObjectName(u"spinBox_text_font_size")
        self.spinBox_text_font_size.setValue(12)

        self.verticalLayout_16.addWidget(self.spinBox_text_font_size)

        self.comboBox_text_font_style = QComboBox(self.tab_text_font)
        self.comboBox_text_font_style.addItem("")
        self.comboBox_text_font_style.addItem("")
        self.comboBox_text_font_style.addItem("")
        self.comboBox_text_font_style.setObjectName(u"comboBox_text_font_style")

        self.verticalLayout_16.addWidget(self.comboBox_text_font_style)

        self.comboBox_text_color = QComboBox(self.tab_text_font)
        self.comboBox_text_color.addItem("")
        self.comboBox_text_color.addItem("")
        self.comboBox_text_color.addItem("")
        self.comboBox_text_color.addItem("")
        self.comboBox_text_color.addItem("")
        self.comboBox_text_color.addItem("")
        self.comboBox_text_color.addItem("")
        self.comboBox_text_color.addItem("")
        self.comboBox_text_color.addItem("")
        self.comboBox_text_color.addItem("")
        self.comboBox_text_color.addItem("")
        self.comboBox_text_color.addItem("")
        self.comboBox_text_color.setObjectName(u"comboBox_text_color")

        self.verticalLayout_16.addWidget(self.comboBox_text_color)

        self.doubleSpinBox_text_alpha = QDoubleSpinBox(self.tab_text_font)
        self.doubleSpinBox_text_alpha.setObjectName(u"doubleSpinBox_text_alpha")
        self.doubleSpinBox_text_alpha.setMaximum(1.000000000000000)
        self.doubleSpinBox_text_alpha.setSingleStep(0.010000000000000)
        self.doubleSpinBox_text_alpha.setValue(1.000000000000000)

        self.verticalLayout_16.addWidget(self.doubleSpinBox_text_alpha)


        self.horizontalLayout_13.addLayout(self.verticalLayout_16)


        self.verticalLayout_17.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_5 = QSpacerItem(20, 32, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_5)

        self.tabWidget_2.addTab(self.tab_text_font, "")
        self.tab_text_bg = QWidget()
        self.tab_text_bg.setObjectName(u"tab_text_bg")
        self.verticalLayout_22 = QVBoxLayout(self.tab_text_bg)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.checkBox_text_bg_fill_visible = QCheckBox(self.tab_text_bg)
        self.checkBox_text_bg_fill_visible.setObjectName(u"checkBox_text_bg_fill_visible")

        self.horizontalLayout_15.addWidget(self.checkBox_text_bg_fill_visible)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_25)


        self.verticalLayout_22.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_23 = QLabel(self.tab_text_bg)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_18.addWidget(self.label_23)

        self.label_24 = QLabel(self.tab_text_bg)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_18.addWidget(self.label_24)


        self.horizontalLayout_16.addLayout(self.verticalLayout_18)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_27)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.comboBox_text_bg_fill_color = QComboBox(self.tab_text_bg)
        self.comboBox_text_bg_fill_color.addItem("")
        self.comboBox_text_bg_fill_color.addItem("")
        self.comboBox_text_bg_fill_color.addItem("")
        self.comboBox_text_bg_fill_color.addItem("")
        self.comboBox_text_bg_fill_color.addItem("")
        self.comboBox_text_bg_fill_color.addItem("")
        self.comboBox_text_bg_fill_color.addItem("")
        self.comboBox_text_bg_fill_color.addItem("")
        self.comboBox_text_bg_fill_color.addItem("")
        self.comboBox_text_bg_fill_color.addItem("")
        self.comboBox_text_bg_fill_color.addItem("")
        self.comboBox_text_bg_fill_color.addItem("")
        self.comboBox_text_bg_fill_color.setObjectName(u"comboBox_text_bg_fill_color")

        self.verticalLayout_19.addWidget(self.comboBox_text_bg_fill_color)

        self.doubleSpinBox_text_bg_fill_alpha = QDoubleSpinBox(self.tab_text_bg)
        self.doubleSpinBox_text_bg_fill_alpha.setObjectName(u"doubleSpinBox_text_bg_fill_alpha")
        self.doubleSpinBox_text_bg_fill_alpha.setMaximum(1.000000000000000)
        self.doubleSpinBox_text_bg_fill_alpha.setSingleStep(0.010000000000000)
        self.doubleSpinBox_text_bg_fill_alpha.setValue(1.000000000000000)

        self.verticalLayout_19.addWidget(self.doubleSpinBox_text_bg_fill_alpha)


        self.horizontalLayout_16.addLayout(self.verticalLayout_19)


        self.verticalLayout_22.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_27 = QLabel(self.tab_text_bg)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_20.addWidget(self.label_27)

        self.label_29 = QLabel(self.tab_text_bg)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_20.addWidget(self.label_29)


        self.horizontalLayout_18.addLayout(self.verticalLayout_20)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_28)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.comboBox_text_bg_edge_color = QComboBox(self.tab_text_bg)
        self.comboBox_text_bg_edge_color.addItem("")
        self.comboBox_text_bg_edge_color.addItem("")
        self.comboBox_text_bg_edge_color.addItem("")
        self.comboBox_text_bg_edge_color.addItem("")
        self.comboBox_text_bg_edge_color.addItem("")
        self.comboBox_text_bg_edge_color.addItem("")
        self.comboBox_text_bg_edge_color.addItem("")
        self.comboBox_text_bg_edge_color.addItem("")
        self.comboBox_text_bg_edge_color.addItem("")
        self.comboBox_text_bg_edge_color.addItem("")
        self.comboBox_text_bg_edge_color.addItem("")
        self.comboBox_text_bg_edge_color.addItem("")
        self.comboBox_text_bg_edge_color.setObjectName(u"comboBox_text_bg_edge_color")

        self.verticalLayout_21.addWidget(self.comboBox_text_bg_edge_color)

        self.doubleSpinBox_text_bg_edge_width = QDoubleSpinBox(self.tab_text_bg)
        self.doubleSpinBox_text_bg_edge_width.setObjectName(u"doubleSpinBox_text_bg_edge_width")

        self.verticalLayout_21.addWidget(self.doubleSpinBox_text_bg_edge_width)


        self.horizontalLayout_18.addLayout(self.verticalLayout_21)


        self.verticalLayout_22.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_4 = QSpacerItem(20, 27, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_4)

        self.tabWidget_2.addTab(self.tab_text_bg, "")

        self.verticalLayout_23.addWidget(self.tabWidget_2)

        self.verticalSpacer_7 = QSpacerItem(20, 247, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_text_visible = QCheckBox(self.tab_text)
        self.checkBox_text_visible.setObjectName(u"checkBox_text_visible")

        self.horizontalLayout_8.addWidget(self.checkBox_text_visible)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_17)


        self.verticalLayout_23.addLayout(self.horizontalLayout_8)

        self.tabWidget.addTab(self.tab_text, "")

        self.verticalLayout_11.addWidget(self.tabWidget)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_20)

        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_11.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_11.addWidget(self.pushButton_cancel)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(2)
        self.comboBox_reciprocal_unit.setCurrentIndex(0)
        self.comboBox_real_length_unit.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(1)
        self.comboBox_text_font_family.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Length", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Unit", None))
        self.comboBox_reciprocal_unit.setItemText(0, QCoreApplication.translate("Dialog", u"m\u207b\u00b9", None))
        self.comboBox_reciprocal_unit.setItemText(1, QCoreApplication.translate("Dialog", u"mm\u207b\u00b9", None))
        self.comboBox_reciprocal_unit.setItemText(2, QCoreApplication.translate("Dialog", u"\u03bcm\u207b\u00b9", None))
        self.comboBox_reciprocal_unit.setItemText(3, QCoreApplication.translate("Dialog", u"nm\u207b\u00b9", None))
        self.comboBox_reciprocal_unit.setItemText(4, QCoreApplication.translate("Dialog", u"\u00c5\u207b\u00b9", None))

        self.label_6.setText(QCoreApplication.translate("Dialog", u"Unit", None))
        self.comboBox_real_length_unit.setItemText(0, QCoreApplication.translate("Dialog", u"m", None))
        self.comboBox_real_length_unit.setItemText(1, QCoreApplication.translate("Dialog", u"mm", None))
        self.comboBox_real_length_unit.setItemText(2, QCoreApplication.translate("Dialog", u"\u03bcm", None))
        self.comboBox_real_length_unit.setItemText(3, QCoreApplication.translate("Dialog", u"nm", None))
        self.comboBox_real_length_unit.setItemText(4, QCoreApplication.translate("Dialog", u"\u00c5", None))

        self.label_22.setText(QCoreApplication.translate("Dialog", u"Unit", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"pixel", None))
        self.checkBox_customize_scale.setText(QCoreApplication.translate("Dialog", u"Customize Scale", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Length per pixel (in custom unit)", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Custom unit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_basic), QCoreApplication.translate("Dialog", u"Basic", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Bar (rectangle patch) style", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Width", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Location", None))
        self.comboBox_bar_location.setItemText(0, QCoreApplication.translate("Dialog", u"upper left", None))
        self.comboBox_bar_location.setItemText(1, QCoreApplication.translate("Dialog", u"upper", None))
        self.comboBox_bar_location.setItemText(2, QCoreApplication.translate("Dialog", u"upper right", None))
        self.comboBox_bar_location.setItemText(3, QCoreApplication.translate("Dialog", u"left", None))
        self.comboBox_bar_location.setItemText(4, QCoreApplication.translate("Dialog", u"middle", None))
        self.comboBox_bar_location.setItemText(5, QCoreApplication.translate("Dialog", u"right", None))
        self.comboBox_bar_location.setItemText(6, QCoreApplication.translate("Dialog", u"bottom left", None))
        self.comboBox_bar_location.setItemText(7, QCoreApplication.translate("Dialog", u"bottom", None))
        self.comboBox_bar_location.setItemText(8, QCoreApplication.translate("Dialog", u"bottom right", None))
        self.comboBox_bar_location.setItemText(9, QCoreApplication.translate("Dialog", u"custom location", None))

        self.label_14.setText(QCoreApplication.translate("Dialog", u"  i-index", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"  j-index", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Rotation (deg)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Color", None))
        self.comboBox_bar_color.setItemText(0, QCoreApplication.translate("Dialog", u"black", None))
        self.comboBox_bar_color.setItemText(1, QCoreApplication.translate("Dialog", u"blue", None))
        self.comboBox_bar_color.setItemText(2, QCoreApplication.translate("Dialog", u"brown", None))
        self.comboBox_bar_color.setItemText(3, QCoreApplication.translate("Dialog", u"cyan", None))
        self.comboBox_bar_color.setItemText(4, QCoreApplication.translate("Dialog", u"gray", None))
        self.comboBox_bar_color.setItemText(5, QCoreApplication.translate("Dialog", u"green", None))
        self.comboBox_bar_color.setItemText(6, QCoreApplication.translate("Dialog", u"orange", None))
        self.comboBox_bar_color.setItemText(7, QCoreApplication.translate("Dialog", u"pink", None))
        self.comboBox_bar_color.setItemText(8, QCoreApplication.translate("Dialog", u"red", None))
        self.comboBox_bar_color.setItemText(9, QCoreApplication.translate("Dialog", u"olive", None))
        self.comboBox_bar_color.setItemText(10, QCoreApplication.translate("Dialog", u"purple", None))
        self.comboBox_bar_color.setItemText(11, QCoreApplication.translate("Dialog", u"white", None))

        self.label_5.setText(QCoreApplication.translate("Dialog", u"Alpha (transparency)", None))
        self.checkBox_bar_visible.setText(QCoreApplication.translate("Dialog", u"Scale bar visible", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_style), QCoreApplication.translate("Dialog", u"Bar Style", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Location", None))
        self.checkBox_text_follow_bar.setText(QCoreApplication.translate("Dialog", u"Location following scale bar", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"  i-index", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"  j-index", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Horizontal alignment", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Vertical alignment", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Rotation", None))
        self.comboBox_text_ha.setItemText(0, QCoreApplication.translate("Dialog", u"left", None))
        self.comboBox_text_ha.setItemText(1, QCoreApplication.translate("Dialog", u"center", None))
        self.comboBox_text_ha.setItemText(2, QCoreApplication.translate("Dialog", u"right", None))

        self.comboBox_text_va.setItemText(0, QCoreApplication.translate("Dialog", u"top", None))
        self.comboBox_text_va.setItemText(1, QCoreApplication.translate("Dialog", u"center", None))
        self.comboBox_text_va.setItemText(2, QCoreApplication.translate("Dialog", u"baseline", None))
        self.comboBox_text_va.setItemText(3, QCoreApplication.translate("Dialog", u"bottom", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_text_location), QCoreApplication.translate("Dialog", u"Location", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Font family", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Font size (pt)", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"Font style", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Color", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Text alpha (transparency)", None))
        self.comboBox_text_font_family.setItemText(0, QCoreApplication.translate("Dialog", u"cursive", None))
        self.comboBox_text_font_family.setItemText(1, QCoreApplication.translate("Dialog", u"fantasy", None))
        self.comboBox_text_font_family.setItemText(2, QCoreApplication.translate("Dialog", u"monospace", None))
        self.comboBox_text_font_family.setItemText(3, QCoreApplication.translate("Dialog", u"sans-serif", None))
        self.comboBox_text_font_family.setItemText(4, QCoreApplication.translate("Dialog", u"serif", None))

        self.comboBox_text_font_style.setItemText(0, QCoreApplication.translate("Dialog", u"normal", None))
        self.comboBox_text_font_style.setItemText(1, QCoreApplication.translate("Dialog", u"italic", None))
        self.comboBox_text_font_style.setItemText(2, QCoreApplication.translate("Dialog", u"oblique", None))

        self.comboBox_text_color.setItemText(0, QCoreApplication.translate("Dialog", u"black", None))
        self.comboBox_text_color.setItemText(1, QCoreApplication.translate("Dialog", u"blue", None))
        self.comboBox_text_color.setItemText(2, QCoreApplication.translate("Dialog", u"brown", None))
        self.comboBox_text_color.setItemText(3, QCoreApplication.translate("Dialog", u"cyan", None))
        self.comboBox_text_color.setItemText(4, QCoreApplication.translate("Dialog", u"gray", None))
        self.comboBox_text_color.setItemText(5, QCoreApplication.translate("Dialog", u"green", None))
        self.comboBox_text_color.setItemText(6, QCoreApplication.translate("Dialog", u"orange", None))
        self.comboBox_text_color.setItemText(7, QCoreApplication.translate("Dialog", u"pink", None))
        self.comboBox_text_color.setItemText(8, QCoreApplication.translate("Dialog", u"red", None))
        self.comboBox_text_color.setItemText(9, QCoreApplication.translate("Dialog", u"olive", None))
        self.comboBox_text_color.setItemText(10, QCoreApplication.translate("Dialog", u"purple", None))
        self.comboBox_text_color.setItemText(11, QCoreApplication.translate("Dialog", u"white", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_text_font), QCoreApplication.translate("Dialog", u"Font", None))
        self.checkBox_text_bg_fill_visible.setText(QCoreApplication.translate("Dialog", u"Background visible", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Color", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Alpha (transparency)", None))
        self.comboBox_text_bg_fill_color.setItemText(0, QCoreApplication.translate("Dialog", u"black", None))
        self.comboBox_text_bg_fill_color.setItemText(1, QCoreApplication.translate("Dialog", u"blue", None))
        self.comboBox_text_bg_fill_color.setItemText(2, QCoreApplication.translate("Dialog", u"brown", None))
        self.comboBox_text_bg_fill_color.setItemText(3, QCoreApplication.translate("Dialog", u"cyan", None))
        self.comboBox_text_bg_fill_color.setItemText(4, QCoreApplication.translate("Dialog", u"gray", None))
        self.comboBox_text_bg_fill_color.setItemText(5, QCoreApplication.translate("Dialog", u"green", None))
        self.comboBox_text_bg_fill_color.setItemText(6, QCoreApplication.translate("Dialog", u"orange", None))
        self.comboBox_text_bg_fill_color.setItemText(7, QCoreApplication.translate("Dialog", u"pink", None))
        self.comboBox_text_bg_fill_color.setItemText(8, QCoreApplication.translate("Dialog", u"red", None))
        self.comboBox_text_bg_fill_color.setItemText(9, QCoreApplication.translate("Dialog", u"olive", None))
        self.comboBox_text_bg_fill_color.setItemText(10, QCoreApplication.translate("Dialog", u"purple", None))
        self.comboBox_text_bg_fill_color.setItemText(11, QCoreApplication.translate("Dialog", u"white", None))

        self.label_27.setText(QCoreApplication.translate("Dialog", u"Edge color", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"Edge width", None))
        self.comboBox_text_bg_edge_color.setItemText(0, QCoreApplication.translate("Dialog", u"black", None))
        self.comboBox_text_bg_edge_color.setItemText(1, QCoreApplication.translate("Dialog", u"blue", None))
        self.comboBox_text_bg_edge_color.setItemText(2, QCoreApplication.translate("Dialog", u"brown", None))
        self.comboBox_text_bg_edge_color.setItemText(3, QCoreApplication.translate("Dialog", u"cyan", None))
        self.comboBox_text_bg_edge_color.setItemText(4, QCoreApplication.translate("Dialog", u"gray", None))
        self.comboBox_text_bg_edge_color.setItemText(5, QCoreApplication.translate("Dialog", u"green", None))
        self.comboBox_text_bg_edge_color.setItemText(6, QCoreApplication.translate("Dialog", u"orange", None))
        self.comboBox_text_bg_edge_color.setItemText(7, QCoreApplication.translate("Dialog", u"pink", None))
        self.comboBox_text_bg_edge_color.setItemText(8, QCoreApplication.translate("Dialog", u"red", None))
        self.comboBox_text_bg_edge_color.setItemText(9, QCoreApplication.translate("Dialog", u"olive", None))
        self.comboBox_text_bg_edge_color.setItemText(10, QCoreApplication.translate("Dialog", u"purple", None))
        self.comboBox_text_bg_edge_color.setItemText(11, QCoreApplication.translate("Dialog", u"white", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_text_bg), QCoreApplication.translate("Dialog", u"Background", None))
        self.checkBox_text_visible.setText(QCoreApplication.translate("Dialog", u"Show text annotation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_text), QCoreApplication.translate("Dialog", u"Text Style", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

