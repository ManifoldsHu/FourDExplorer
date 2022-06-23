# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetMaskRing.ui'
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
        Form.resize(405, 295)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_ring_parameter = QLabel(Form)
        self.label_ring_parameter.setObjectName(u"label_ring_parameter")

        self.verticalLayout_3.addWidget(self.label_ring_parameter)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_ring_inner = QLabel(self.groupBox_2)
        self.label_ring_inner.setObjectName(u"label_ring_inner")

        self.horizontalLayout.addWidget(self.label_ring_inner)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.doubleSpinBox_ring_inner = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_ring_inner.setObjectName(u"doubleSpinBox_ring_inner")

        self.horizontalLayout.addWidget(self.doubleSpinBox_ring_inner)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_ring_outer = QLabel(self.groupBox_2)
        self.label_ring_outer.setObjectName(u"label_ring_outer")

        self.horizontalLayout_2.addWidget(self.label_ring_outer)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.doubleSpinBox_ring_outer = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_ring_outer.setObjectName(u"doubleSpinBox_ring_outer")

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_ring_outer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_ring_center_j = QLabel(self.groupBox)
        self.label_ring_center_j.setObjectName(u"label_ring_center_j")

        self.horizontalLayout_4.addWidget(self.label_ring_center_j)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.doubleSpinBox_ring_center_j = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_ring_center_j.setObjectName(u"doubleSpinBox_ring_center_j")

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_ring_center_j)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_ring_center_i = QLabel(self.groupBox)
        self.label_ring_center_i.setObjectName(u"label_ring_center_i")

        self.horizontalLayout_3.addWidget(self.label_ring_center_i)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox_ring_center_i = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_ring_center_i.setObjectName(u"doubleSpinBox_ring_center_i")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_ring_center_i)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.pushButton_adjust_effects = QPushButton(Form)
        self.pushButton_adjust_effects.setObjectName(u"pushButton_adjust_effects")

        self.verticalLayout_3.addWidget(self.pushButton_adjust_effects)

        self.verticalSpacer_3 = QSpacerItem(20, 36, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

#if QT_CONFIG(shortcut)
        self.label_ring_inner.setBuddy(self.doubleSpinBox_ring_inner)
        self.label_ring_outer.setBuddy(self.doubleSpinBox_ring_outer)
        self.label_ring_center_j.setBuddy(self.doubleSpinBox_ring_center_j)
        self.label_ring_center_i.setBuddy(self.doubleSpinBox_ring_center_i)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_ring_parameter.setText(QCoreApplication.translate("Form", u"Ring parameters", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Shape", None))
        self.label_ring_inner.setText(QCoreApplication.translate("Form", u"Inner Radius (pix)(&I)", None))
        self.label_ring_outer.setText(QCoreApplication.translate("Form", u"Outer Radius (pix)(&O)", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Location", None))
        self.label_ring_center_j.setText(QCoreApplication.translate("Form", u"Horizontal Shift(&J)", None))
        self.label_ring_center_i.setText(QCoreApplication.translate("Form", u"Vertical Shift(&I)", None))
        self.pushButton_adjust_effects.setText(QCoreApplication.translate("Form", u"Adjust Effects...", None))
    # retranslateUi

