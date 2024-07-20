# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetAlignmentRef.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(345, 493)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_reference_4dstem = QLineEdit(Form)
        self.lineEdit_reference_4dstem.setObjectName(u"lineEdit_reference_4dstem")

        self.horizontalLayout.addWidget(self.lineEdit_reference_4dstem)

        self.pushButton_browse_reference_4dstem = QPushButton(Form)
        self.pushButton_browse_reference_4dstem.setObjectName(u"pushButton_browse_reference_4dstem")

        self.horizontalLayout.addWidget(self.pushButton_browse_reference_4dstem)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.checkBox_show_shifted_dp = QCheckBox(Form)
        self.checkBox_show_shifted_dp.setObjectName(u"checkBox_show_shifted_dp")

        self.verticalLayout.addWidget(self.checkBox_show_shifted_dp)

        self.verticalSpacer_4 = QSpacerItem(20, 362, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pushButton_generate_shift_vec = QPushButton(Form)
        self.pushButton_generate_shift_vec.setObjectName(u"pushButton_generate_shift_vec")

        self.verticalLayout.addWidget(self.pushButton_generate_shift_vec)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Reference 4D-STEM Dataset", None))
        self.pushButton_browse_reference_4dstem.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.checkBox_show_shifted_dp.setText(QCoreApplication.translate("Form", u"Display shifted diffraction image", None))
        self.pushButton_generate_shift_vec.setText(QCoreApplication.translate("Form", u"Generate Shift Vectors", None))
    # retranslateUi

