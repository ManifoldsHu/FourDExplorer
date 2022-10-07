# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogImportImage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(598, 419)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.comboBox_mode = QComboBox(self.groupBox)
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.setObjectName(u"comboBox_mode")

        self.horizontalLayout_2.addWidget(self.comboBox_mode)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_image_path = QLineEdit(self.groupBox)
        self.lineEdit_image_path.setObjectName(u"lineEdit_image_path")

        self.horizontalLayout_5.addWidget(self.lineEdit_image_path)

        self.pushButton_browse_file = QPushButton(self.groupBox)
        self.pushButton_browse_file.setObjectName(u"pushButton_browse_file")

        self.horizontalLayout_5.addWidget(self.pushButton_browse_file)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEdit_parent_path = QLineEdit(self.groupBox_2)
        self.lineEdit_parent_path.setObjectName(u"lineEdit_parent_path")

        self.horizontalLayout_6.addWidget(self.lineEdit_parent_path)

        self.pushButton_browse_parent = QPushButton(self.groupBox_2)
        self.pushButton_browse_parent.setObjectName(u"pushButton_browse_parent")

        self.horizontalLayout_6.addWidget(self.pushButton_browse_parent)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lineEdit_name = QLineEdit(self.groupBox_2)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.horizontalLayout.addWidget(self.lineEdit_name)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_3.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_3.addWidget(self.pushButton_cancel)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Import Image", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Import From", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Import File Type", None))
        self.comboBox_mode.setItemText(0, QCoreApplication.translate("Dialog", u"TIFF", None))
        self.comboBox_mode.setItemText(1, QCoreApplication.translate("Dialog", u"Binary (RAW)", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"File path:", None))
        self.pushButton_browse_file.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"NOTE: The image must be gray scale image.\n"
"RGB colored images are not supported.", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Import to", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Import Image to Location:", None))
        self.pushButton_browse_parent.setText(QCoreApplication.translate("Dialog", u"Browse...", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

