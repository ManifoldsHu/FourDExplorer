# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetAlignmentRef.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(345, 436)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_measured_dp_shift = QLabel(self.groupBox)
        self.label_measured_dp_shift.setObjectName(u"label_measured_dp_shift")

        self.horizontalLayout_2.addWidget(self.label_measured_dp_shift)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.checkBox_show_shifted_dp = QCheckBox(self.groupBox)
        self.checkBox_show_shifted_dp.setObjectName(u"checkBox_show_shifted_dp")

        self.verticalLayout.addWidget(self.checkBox_show_shifted_dp)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_reference_4dstem = QLineEdit(self.groupBox)
        self.lineEdit_reference_4dstem.setObjectName(u"lineEdit_reference_4dstem")

        self.horizontalLayout.addWidget(self.lineEdit_reference_4dstem)

        self.pushButton_browse_reference_4dstem = QPushButton(self.groupBox)
        self.pushButton_browse_reference_4dstem.setObjectName(u"pushButton_browse_reference_4dstem")

        self.horizontalLayout.addWidget(self.pushButton_browse_reference_4dstem)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_generate_shift_vec = QPushButton(self.groupBox_2)
        self.pushButton_generate_shift_vec.setObjectName(u"pushButton_generate_shift_vec")

        self.verticalLayout_2.addWidget(self.pushButton_generate_shift_vec)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalSpacer_4 = QSpacerItem(20, 362, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Shift Diffraction Patterns", None))
        self.label.setText(QCoreApplication.translate("Form", u"Measured DP shift:", None))
        self.label_measured_dp_shift.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.checkBox_show_shifted_dp.setText(QCoreApplication.translate("Form", u"Display shifted diffraction image", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Reference 4D-STEM Dataset", None))
        self.pushButton_browse_reference_4dstem.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Calculate CoM of Reference", None))
        self.pushButton_generate_shift_vec.setText(QCoreApplication.translate("Form", u"Generate Shift Mapping", None))
    # retranslateUi

