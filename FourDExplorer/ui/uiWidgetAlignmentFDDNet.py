# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetAlignmentFDDNet.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 616)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_fddnet_inference = QPushButton(Form)
        self.pushButton_fddnet_inference.setObjectName(u"pushButton_fddnet_inference")

        self.verticalLayout_3.addWidget(self.pushButton_fddnet_inference)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_3.addWidget(self.label_16)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout.addWidget(self.label_17)

        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout.addWidget(self.label_18)

        self.label_19 = QLabel(Form)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout.addWidget(self.label_19)

        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout.addWidget(self.label_20)

        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout.addWidget(self.label_21)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_fddnet_center_shift_ci = QLabel(Form)
        self.label_fddnet_center_shift_ci.setObjectName(u"label_fddnet_center_shift_ci")

        self.verticalLayout_2.addWidget(self.label_fddnet_center_shift_ci)

        self.label_fddnet_center_shift_cj = QLabel(Form)
        self.label_fddnet_center_shift_cj.setObjectName(u"label_fddnet_center_shift_cj")

        self.verticalLayout_2.addWidget(self.label_fddnet_center_shift_cj)

        self.label_fddnet_elliptical_a = QLabel(Form)
        self.label_fddnet_elliptical_a.setObjectName(u"label_fddnet_elliptical_a")

        self.verticalLayout_2.addWidget(self.label_fddnet_elliptical_a)

        self.label_fddnet_elliptical_b = QLabel(Form)
        self.label_fddnet_elliptical_b.setObjectName(u"label_fddnet_elliptical_b")

        self.verticalLayout_2.addWidget(self.label_fddnet_elliptical_b)

        self.label_fddnet_elliptical_angle = QLabel(Form)
        self.label_fddnet_elliptical_angle.setObjectName(u"label_fddnet_elliptical_angle")

        self.verticalLayout_2.addWidget(self.label_fddnet_elliptical_angle)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.checkBox_show_shifted_dp = QCheckBox(Form)
        self.checkBox_show_shifted_dp.setObjectName(u"checkBox_show_shifted_dp")

        self.verticalLayout_3.addWidget(self.checkBox_show_shifted_dp)

        self.verticalSpacer = QSpacerItem(20, 373, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_generate_shift_vec = QPushButton(Form)
        self.pushButton_generate_shift_vec.setObjectName(u"pushButton_generate_shift_vec")

        self.verticalLayout_3.addWidget(self.pushButton_generate_shift_vec)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_fddnet_inference.setText(QCoreApplication.translate("Form", u"FDDNet Inference", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"FDDNet Prediction Result", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Disk Center Shift (i)", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Disk Center Shift (j)", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Elliptical Semi-major Axis", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Elliptical Semi-minor Axis", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Elliptical Rotation Angle", None))
        self.label_fddnet_center_shift_ci.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_fddnet_center_shift_cj.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_fddnet_elliptical_a.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_fddnet_elliptical_b.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_fddnet_elliptical_angle.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.checkBox_show_shifted_dp.setText(QCoreApplication.translate("Form", u"Display shifted diffraction image", None))
        self.pushButton_generate_shift_vec.setText(QCoreApplication.translate("Form", u"Generate Shift Vectors", None))
    # retranslateUi

