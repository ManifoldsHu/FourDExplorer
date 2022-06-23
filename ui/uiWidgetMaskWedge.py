# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetMaskWedge.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(522, 385)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_wedge_parameter = QLabel(Form)
        self.label_wedge_parameter.setObjectName(u"label_wedge_parameter")

        self.verticalLayout_3.addWidget(self.label_wedge_parameter)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_wedge_inner = QLabel(self.groupBox)
        self.label_wedge_inner.setObjectName(u"label_wedge_inner")

        self.horizontalLayout.addWidget(self.label_wedge_inner)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.doubleSpinBox_wedge_inner = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_wedge_inner.setObjectName(u"doubleSpinBox_wedge_inner")

        self.horizontalLayout.addWidget(self.doubleSpinBox_wedge_inner)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_wedge_outer = QLabel(self.groupBox)
        self.label_wedge_outer.setObjectName(u"label_wedge_outer")

        self.horizontalLayout_2.addWidget(self.label_wedge_outer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox_wedge_outer = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_wedge_outer.setObjectName(u"doubleSpinBox_wedge_outer")

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_wedge_outer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_wedge_open_angle = QLabel(self.groupBox)
        self.label_wedge_open_angle.setObjectName(u"label_wedge_open_angle")

        self.horizontalLayout_4.addWidget(self.label_wedge_open_angle)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.doubleSpinBox_wedge_open_angle = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_wedge_open_angle.setObjectName(u"doubleSpinBox_wedge_open_angle")

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_wedge_open_angle)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_wedge_center_j = QLabel(self.groupBox_2)
        self.label_wedge_center_j.setObjectName(u"label_wedge_center_j")

        self.horizontalLayout_6.addWidget(self.label_wedge_center_j)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.doubleSpinBox_wedge_center_j = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_wedge_center_j.setObjectName(u"doubleSpinBox_wedge_center_j")

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_wedge_center_j)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_wedge_center_i = QLabel(self.groupBox_2)
        self.label_wedge_center_i.setObjectName(u"label_wedge_center_i")

        self.horizontalLayout_5.addWidget(self.label_wedge_center_i)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.doubleSpinBox_wedge_center_i = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_wedge_center_i.setObjectName(u"doubleSpinBox_wedge_center_i")

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_wedge_center_i)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_wedge_rotate_angle = QLabel(self.groupBox_2)
        self.label_wedge_rotate_angle.setObjectName(u"label_wedge_rotate_angle")

        self.horizontalLayout_3.addWidget(self.label_wedge_rotate_angle)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.doubleSpinBox_wedge_rotate_angle = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_wedge_rotate_angle.setObjectName(u"doubleSpinBox_wedge_rotate_angle")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_wedge_rotate_angle)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.pushButton_adjust_effects = QPushButton(Form)
        self.pushButton_adjust_effects.setObjectName(u"pushButton_adjust_effects")

        self.verticalLayout_3.addWidget(self.pushButton_adjust_effects)

        self.verticalSpacer = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

#if QT_CONFIG(shortcut)
        self.label_wedge_inner.setBuddy(self.doubleSpinBox_wedge_inner)
        self.label_wedge_outer.setBuddy(self.doubleSpinBox_wedge_outer)
        self.label_wedge_open_angle.setBuddy(self.doubleSpinBox_wedge_open_angle)
        self.label_wedge_center_j.setBuddy(self.doubleSpinBox_wedge_center_j)
        self.label_wedge_center_i.setBuddy(self.doubleSpinBox_wedge_center_i)
        self.label_wedge_rotate_angle.setBuddy(self.doubleSpinBox_wedge_rotate_angle)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_wedge_parameter.setText(QCoreApplication.translate("Form", u"Wedge parameters", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Shape", None))
        self.label_wedge_inner.setText(QCoreApplication.translate("Form", u"Inner Radius (pix)(&I)", None))
        self.label_wedge_outer.setText(QCoreApplication.translate("Form", u"Outer Radius (pix)(&O)", None))
        self.label_wedge_open_angle.setText(QCoreApplication.translate("Form", u"Open Angle (deg)(&A)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Location", None))
        self.label_wedge_center_j.setText(QCoreApplication.translate("Form", u"Horizontal Shift(&J)", None))
        self.label_wedge_center_i.setText(QCoreApplication.translate("Form", u"Vertical Shift(&I)", None))
        self.label_wedge_rotate_angle.setText(QCoreApplication.translate("Form", u"Rotation Angle (deg)(&R)", None))
        self.pushButton_adjust_effects.setText(QCoreApplication.translate("Form", u"Adjust Effects...", None))
    # retranslateUi

