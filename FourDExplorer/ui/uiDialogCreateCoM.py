# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogCreateCoM.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(408, 416)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 9, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_parent_path = QLineEdit(Dialog)
        self.lineEdit_parent_path.setObjectName(u"lineEdit_parent_path")

        self.horizontalLayout.addWidget(self.lineEdit_parent_path)

        self.pushButton_browse = QPushButton(Dialog)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.checkBox_CoM = QCheckBox(Dialog)
        self.checkBox_CoM.setObjectName(u"checkBox_CoM")

        self.verticalLayout_2.addWidget(self.checkBox_CoM)

        self.checkBox_CoMi = QCheckBox(Dialog)
        self.checkBox_CoMi.setObjectName(u"checkBox_CoMi")

        self.verticalLayout_2.addWidget(self.checkBox_CoMi)

        self.checkBox_CoMj = QCheckBox(Dialog)
        self.checkBox_CoMj.setObjectName(u"checkBox_CoMj")

        self.verticalLayout_2.addWidget(self.checkBox_CoMj)

        self.checkBox_dCoM = QCheckBox(Dialog)
        self.checkBox_dCoM.setObjectName(u"checkBox_dCoM")

        self.verticalLayout_2.addWidget(self.checkBox_dCoM)

        self.checkBox_iCoM = QCheckBox(Dialog)
        self.checkBox_iCoM.setObjectName(u"checkBox_iCoM")

        self.verticalLayout_2.addWidget(self.checkBox_iCoM)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit_CoM = QLineEdit(Dialog)
        self.lineEdit_CoM.setObjectName(u"lineEdit_CoM")

        self.verticalLayout_3.addWidget(self.lineEdit_CoM)

        self.lineEdit_CoMi = QLineEdit(Dialog)
        self.lineEdit_CoMi.setObjectName(u"lineEdit_CoMi")

        self.verticalLayout_3.addWidget(self.lineEdit_CoMi)

        self.lineEdit_CoMj = QLineEdit(Dialog)
        self.lineEdit_CoMj.setObjectName(u"lineEdit_CoMj")

        self.verticalLayout_3.addWidget(self.lineEdit_CoMj)

        self.lineEdit_dCoM = QLineEdit(Dialog)
        self.lineEdit_dCoM.setObjectName(u"lineEdit_dCoM")

        self.verticalLayout_3.addWidget(self.lineEdit_dCoM)

        self.lineEdit_iCoM = QLineEdit(Dialog)
        self.lineEdit_iCoM.setObjectName(u"lineEdit_iCoM")

        self.verticalLayout_3.addWidget(self.lineEdit_iCoM)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_use_CoM = QRadioButton(Dialog)
        self.radioButton_use_CoM.setObjectName(u"radioButton_use_CoM")

        self.verticalLayout.addWidget(self.radioButton_use_CoM)

        self.radioButton_use_electric = QRadioButton(Dialog)
        self.radioButton_use_electric.setObjectName(u"radioButton_use_electric")

        self.verticalLayout.addWidget(self.radioButton_use_electric)

        self.checkBox_normalize = QCheckBox(Dialog)
        self.checkBox_normalize.setObjectName(u"checkBox_normalize")

        self.verticalLayout.addWidget(self.checkBox_normalize)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 9, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_3.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_3.addWidget(self.pushButton_cancel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Calculating Center of Mass (CoM)", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Save results to...", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Dialog", u"Browse...", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Calculate Items", None))
        self.checkBox_CoM.setText(QCoreApplication.translate("Dialog", u"CoM vector field", None))
        self.checkBox_CoMi.setText(QCoreApplication.translate("Dialog", u"CoM vertical component (CoMi)", None))
        self.checkBox_CoMj.setText(QCoreApplication.translate("Dialog", u"CoM horizontal component (CoMj)", None))
        self.checkBox_dCoM.setText(QCoreApplication.translate("Dialog", u"differentiated CoM (dCoM)", None))
        self.checkBox_iCoM.setText(QCoreApplication.translate("Dialog", u"integrated CoM (iCoM)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"New dataset name", None))
        self.radioButton_use_CoM.setText(QCoreApplication.translate("Dialog", u"Use Center of Mass mapping", None))
        self.radioButton_use_electric.setText(QCoreApplication.translate("Dialog", u"Use projected electric field mapping", None))
        self.checkBox_normalize.setText(QCoreApplication.translate("Dialog", u"Normalize: set mean field to be zero vector", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

