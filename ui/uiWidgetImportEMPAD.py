# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetImportEMPAD.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(415, 109)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_xml_path = QLineEdit(Form)
        self.lineEdit_xml_path.setObjectName(u"lineEdit_xml_path")

        self.gridLayout.addWidget(self.lineEdit_xml_path, 0, 1, 1, 1)

        self.pushButton_browse = QPushButton(Form)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.gridLayout.addWidget(self.pushButton_browse, 0, 2, 2, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 2, 1)

        self.lineEdit_raw_path = QLineEdit(Form)
        self.lineEdit_raw_path.setObjectName(u"lineEdit_raw_path")

        self.gridLayout.addWidget(self.lineEdit_raw_path, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 26, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"EMPAD XML file", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse...", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"EMPAD RAW file", None))
    # retranslateUi

