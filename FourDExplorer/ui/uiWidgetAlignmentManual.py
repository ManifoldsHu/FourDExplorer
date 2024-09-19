# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetAlignmentManual.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(371, 673)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_measured_shift = QLabel(self.groupBox)
        self.label_measured_shift.setObjectName(u"label_measured_shift")

        self.horizontalLayout_2.addWidget(self.label_measured_shift)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.checkBox_show_shifted_dp = QCheckBox(self.groupBox)
        self.checkBox_show_shifted_dp.setObjectName(u"checkBox_show_shifted_dp")

        self.verticalLayout_3.addWidget(self.checkBox_show_shifted_dp)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout.addWidget(self.label_13)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.spinBox_manual_shift_i = QSpinBox(self.groupBox)
        self.spinBox_manual_shift_i.setObjectName(u"spinBox_manual_shift_i")

        self.verticalLayout_2.addWidget(self.spinBox_manual_shift_i)

        self.spinBox_manual_shift_j = QSpinBox(self.groupBox)
        self.spinBox_manual_shift_j.setObjectName(u"spinBox_manual_shift_j")

        self.verticalLayout_2.addWidget(self.spinBox_manual_shift_j)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_up = QPushButton(self.groupBox)
        self.pushButton_up.setObjectName(u"pushButton_up")

        self.gridLayout.addWidget(self.pushButton_up, 0, 1, 1, 1)

        self.pushButton_left = QPushButton(self.groupBox)
        self.pushButton_left.setObjectName(u"pushButton_left")

        self.gridLayout.addWidget(self.pushButton_left, 1, 0, 1, 1)

        self.pushButton_down = QPushButton(self.groupBox)
        self.pushButton_down.setObjectName(u"pushButton_down")

        self.gridLayout.addWidget(self.pushButton_down, 1, 1, 1, 1)

        self.pushButton_right = QPushButton(self.groupBox)
        self.pushButton_right.setObjectName(u"pushButton_right")

        self.gridLayout.addWidget(self.pushButton_right, 1, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_sample_records = QGroupBox(Form)
        self.groupBox_sample_records.setObjectName(u"groupBox_sample_records")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_sample_records)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableWidget_manual_sample = QTableWidget(self.groupBox_sample_records)
        self.tableWidget_manual_sample.setObjectName(u"tableWidget_manual_sample")

        self.verticalLayout_4.addWidget(self.tableWidget_manual_sample)

        self.pushButton_generate_shift_vec = QPushButton(self.groupBox_sample_records)
        self.pushButton_generate_shift_vec.setObjectName(u"pushButton_generate_shift_vec")

        self.verticalLayout_4.addWidget(self.pushButton_generate_shift_vec)


        self.verticalLayout_5.addWidget(self.groupBox_sample_records)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Shift Diffraction Patterns", None))
        self.label.setText(QCoreApplication.translate("Form", u"Measured DP shift:", None))
        self.label_measured_shift.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.checkBox_show_shifted_dp.setText(QCoreApplication.translate("Form", u"Display shifted diffraction image", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Translate DP i-direct", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Translate DP j-direct", None))
        self.pushButton_up.setText(QCoreApplication.translate("Form", u"\u2191", None))
        self.pushButton_left.setText(QCoreApplication.translate("Form", u"\u2190", None))
        self.pushButton_down.setText(QCoreApplication.translate("Form", u"\u2193", None))
        self.pushButton_right.setText(QCoreApplication.translate("Form", u"\u2192", None))
        self.groupBox_sample_records.setTitle(QCoreApplication.translate("Form", u"Sample Records", None))
        self.pushButton_generate_shift_vec.setText(QCoreApplication.translate("Form", u"Generate Shift Vectors", None))
    # retranslateUi

