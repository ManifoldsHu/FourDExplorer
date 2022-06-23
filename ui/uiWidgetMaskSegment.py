# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetMaskSegment.ui'
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
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(494, 409)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_segment_parameter = QLabel(Form)
        self.label_segment_parameter.setObjectName(u"label_segment_parameter")

        self.verticalLayout_3.addWidget(self.label_segment_parameter)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_segment_inner = QLabel(self.groupBox)
        self.label_segment_inner.setObjectName(u"label_segment_inner")

        self.horizontalLayout_19.addWidget(self.label_segment_inner)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer)

        self.doubleSpinBox_segment_inner = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_segment_inner.setObjectName(u"doubleSpinBox_segment_inner")

        self.horizontalLayout_19.addWidget(self.doubleSpinBox_segment_inner)


        self.verticalLayout_2.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_segment_outer = QLabel(self.groupBox)
        self.label_segment_outer.setObjectName(u"label_segment_outer")

        self.horizontalLayout_20.addWidget(self.label_segment_outer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox_segment_outer = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_segment_outer.setObjectName(u"doubleSpinBox_segment_outer")

        self.horizontalLayout_20.addWidget(self.doubleSpinBox_segment_outer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_segment_open_angle = QLabel(self.groupBox)
        self.label_segment_open_angle.setObjectName(u"label_segment_open_angle")

        self.horizontalLayout_22.addWidget(self.label_segment_open_angle)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_3)

        self.doubleSpinBox_segment_open_angle = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_segment_open_angle.setObjectName(u"doubleSpinBox_segment_open_angle")

        self.horizontalLayout_22.addWidget(self.doubleSpinBox_segment_open_angle)


        self.verticalLayout_2.addLayout(self.horizontalLayout_22)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.spinBox_num_segments = QSpinBox(self.groupBox)
        self.spinBox_num_segments.setObjectName(u"spinBox_num_segments")

        self.horizontalLayout.addWidget(self.spinBox_num_segments)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_segment_center_j = QLabel(self.groupBox_2)
        self.label_segment_center_j.setObjectName(u"label_segment_center_j")

        self.horizontalLayout_23.addWidget(self.label_segment_center_j)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_5)

        self.doubleSpinBox_segment_center_j = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_segment_center_j.setObjectName(u"doubleSpinBox_segment_center_j")

        self.horizontalLayout_23.addWidget(self.doubleSpinBox_segment_center_j)


        self.verticalLayout.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_segment_center_i = QLabel(self.groupBox_2)
        self.label_segment_center_i.setObjectName(u"label_segment_center_i")

        self.horizontalLayout_24.addWidget(self.label_segment_center_i)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_6)

        self.doubleSpinBox_segment_center_i = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_segment_center_i.setObjectName(u"doubleSpinBox_segment_center_i")

        self.horizontalLayout_24.addWidget(self.doubleSpinBox_segment_center_i)


        self.verticalLayout.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_segment_rotate_angle = QLabel(self.groupBox_2)
        self.label_segment_rotate_angle.setObjectName(u"label_segment_rotate_angle")

        self.horizontalLayout_21.addWidget(self.label_segment_rotate_angle)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_7)

        self.doubleSpinBox_segment_rotate_angle = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_segment_rotate_angle.setObjectName(u"doubleSpinBox_segment_rotate_angle")

        self.horizontalLayout_21.addWidget(self.doubleSpinBox_segment_rotate_angle)


        self.verticalLayout.addLayout(self.horizontalLayout_21)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.pushButton_adjust_effects = QPushButton(Form)
        self.pushButton_adjust_effects.setObjectName(u"pushButton_adjust_effects")

        self.verticalLayout_3.addWidget(self.pushButton_adjust_effects)

        self.verticalSpacer_4 = QSpacerItem(20, 63, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

#if QT_CONFIG(shortcut)
        self.label_segment_inner.setBuddy(self.doubleSpinBox_segment_inner)
        self.label_segment_outer.setBuddy(self.doubleSpinBox_segment_outer)
        self.label_segment_open_angle.setBuddy(self.doubleSpinBox_segment_open_angle)
        self.label_segment_center_j.setBuddy(self.doubleSpinBox_segment_center_j)
        self.label_segment_center_i.setBuddy(self.doubleSpinBox_segment_center_i)
        self.label_segment_rotate_angle.setBuddy(self.doubleSpinBox_segment_rotate_angle)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_segment_parameter.setText(QCoreApplication.translate("Form", u"Segmented ring parameters", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Shape", None))
        self.label_segment_inner.setText(QCoreApplication.translate("Form", u"inner radius (pix)(&I)", None))
        self.label_segment_outer.setText(QCoreApplication.translate("Form", u"outer radius (pix)(&O)", None))
        self.label_segment_open_angle.setText(QCoreApplication.translate("Form", u"open angle (deg)(&A)", None))
        self.label.setText(QCoreApplication.translate("Form", u"Number of Segments", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Location", None))
        self.label_segment_center_j.setText(QCoreApplication.translate("Form", u"horizontal shift(&J)", None))
        self.label_segment_center_i.setText(QCoreApplication.translate("Form", u"vertical shift(&I)", None))
        self.label_segment_rotate_angle.setText(QCoreApplication.translate("Form", u"rotation angle (deg)(&R)", None))
        self.pushButton_adjust_effects.setText(QCoreApplication.translate("Form", u"Adjust Effects...", None))
    # retranslateUi

