# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageHome.ui'
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
        self.commandLinkButton_tutorials = QCommandLinkButton(Form)
        self.commandLinkButton_tutorials.setObjectName(u"commandLinkButton_tutorials")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_tutorials.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_tutorials.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.commandLinkButton_tutorials)

        self.commandLinkButton_work = QCommandLinkButton(Form)
        self.commandLinkButton_work.setObjectName(u"commandLinkButton_work")

        self.verticalLayout_4.addWidget(self.commandLinkButton_work)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)


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

        self.pushButton_new_file = QPushButton(self.groupBox)
        self.pushButton_new_file.setObjectName(u"pushButton_new_file")

        self.verticalLayout.addWidget(self.pushButton_new_file)

        self.pushButton_open_file = QPushButton(self.groupBox)
        self.pushButton_open_file.setObjectName(u"pushButton_open_file")

        self.verticalLayout.addWidget(self.pushButton_open_file)


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

        self.pushButton_import_image = QPushButton(self.groupBox_2)
        self.pushButton_import_image.setObjectName(u"pushButton_import_image")

        self.verticalLayout_2.addWidget(self.pushButton_import_image)

        self.pushButton_import_fourDSTEM = QPushButton(self.groupBox_2)
        self.pushButton_import_fourDSTEM.setObjectName(u"pushButton_import_fourDSTEM")

        self.verticalLayout_2.addWidget(self.pushButton_import_fourDSTEM)

        self.pushButton_open_fourDSTEM = QPushButton(self.groupBox_2)
        self.pushButton_open_fourDSTEM.setObjectName(u"pushButton_open_fourDSTEM")

        self.verticalLayout_2.addWidget(self.pushButton_open_fourDSTEM)


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

        self.pushButton_background_subtraction = QPushButton(self.groupBox_3)
        self.pushButton_background_subtraction.setObjectName(u"pushButton_background_subtraction")

        self.verticalLayout_3.addWidget(self.pushButton_background_subtraction)

        self.pushButton_rotational_correction = QPushButton(self.groupBox_3)
        self.pushButton_rotational_correction.setObjectName(u"pushButton_rotational_correction")

        self.verticalLayout_3.addWidget(self.pushButton_rotational_correction)

        self.pushButton_diffraction_alignment = QPushButton(self.groupBox_3)
        self.pushButton_diffraction_alignment.setObjectName(u"pushButton_diffraction_alignment")

        self.verticalLayout_3.addWidget(self.pushButton_diffraction_alignment)


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
        self.commandLinkButton_tutorials.setText(QCoreApplication.translate("Form", u"Watch tutorials about 4D-Explorer", None))
        self.commandLinkButton_work.setText(QCoreApplication.translate("Form", u"How does 4D-STEM work?", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Start Work", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Start work by getting </span></p><p><span style=\" font-size:12pt;\">an HDF5 file.</span></p><p><br/></p></body></html>", None))
        self.pushButton_new_file.setText(QCoreApplication.translate("Form", u"New HDF5 File", None))
        self.pushButton_open_file.setText(QCoreApplication.translate("Form", u"Open HDF5 File", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Import Data", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Import data, </span></p><p><span style=\" font-size:12pt;\">view them,</span></p><p><span style=\" font-size:12pt;\">and analyze.</span></p></body></html>", None))
        self.pushButton_import_image.setText(QCoreApplication.translate("Form", u"Import Image", None))
        self.pushButton_import_fourDSTEM.setText(QCoreApplication.translate("Form", u"Import 4D-STEM Data", None))
        self.pushButton_open_fourDSTEM.setText(QCoreApplication.translate("Form", u"View 4D-STEM Data", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Calibration", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Calibrate,</span></p><p><span style=\" font-size:12pt;\">makes accurate</span></p></body></html>", None))
        self.pushButton_background_subtraction.setText(QCoreApplication.translate("Form", u"Background Subtraction", None))
        self.pushButton_rotational_correction.setText(QCoreApplication.translate("Form", u"Rotational Offset Correction", None))
        self.pushButton_diffraction_alignment.setText(QCoreApplication.translate("Form", u"Diffraction Alignment", None))
    # retranslateUi

