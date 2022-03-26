# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageHome.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(866, 627)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(32, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.commandLinkButton = QCommandLinkButton(Form)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.verticalLayout_4.addWidget(self.commandLinkButton)

        self.commandLinkButton_2 = QCommandLinkButton(Form)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")

        self.verticalLayout_4.addWidget(self.commandLinkButton_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(238, 78, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(26)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer_2 = QSpacerItem(20, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.verticalSpacer_3 = QSpacerItem(20, 114, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(142, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 20)
        self.horizontalLayout_3.setStretch(2, 3)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:26pt;\">Hello, 4D-Explorer!</span></p></body></html>", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Form", u"Watch tutorials about 4D-Explorer", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("Form", u"How does 4D-STEM work?", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Start Work", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Start work by getting </span></p><p><span style=\" font-size:12pt;\">an HDF5 file.</span></p><p><br/></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"New File", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Open File", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Import Data", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Import data, </span></p><p><span style=\" font-size:12pt;\">view them,</span></p><p><span style=\" font-size:12pt;\">and analyze.</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Import Image", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Import 4D-STEM Data", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Calibration", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Calibrate,</span></p><p><span style=\" font-size:12pt;\">makes accurate</span></p></body></html>", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Start Calibration", None))
    # retranslateUi

