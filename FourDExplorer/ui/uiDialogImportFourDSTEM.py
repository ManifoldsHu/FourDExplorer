# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogImportFourDSTEM.ui'
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
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

from bin.Widgets.WidgetImportDM4 import WidgetImportDM4
from bin.Widgets.WidgetImportEMPAD import (WidgetImportEMPAD, WidgetImportEMPAD_NJU)
from bin.Widgets.WidgetImportHDF5 import WidgetImport4DSTEMFromHDF5
from bin.Widgets.WidgetImportMerlin import WidgetImportMerlin
from bin.Widgets.WidgetImportNumpy import WidgetImportNumpy
from bin.Widgets.WidgetImportRaw import WidgetImportRaw

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(646, 595)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.comboBox_mode = QComboBox(self.groupBox)
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.setObjectName(u"comboBox_mode")

        self.horizontalLayout_5.addWidget(self.comboBox_mode)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.groupBox)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_empad = WidgetImportEMPAD()
        self.page_empad.setObjectName(u"page_empad")
        self.stackedWidget.addWidget(self.page_empad)
        self.page_empad_nju = WidgetImportEMPAD_NJU()
        self.page_empad_nju.setObjectName(u"page_empad_nju")
        self.stackedWidget.addWidget(self.page_empad_nju)
        self.page_medipix = WidgetImportMerlin()
        self.page_medipix.setObjectName(u"page_medipix")
        self.stackedWidget.addWidget(self.page_medipix)
        self.page_dm4 = WidgetImportDM4()
        self.page_dm4.setObjectName(u"page_dm4")
        self.stackedWidget.addWidget(self.page_dm4)
        self.page_raw = WidgetImportRaw()
        self.page_raw.setObjectName(u"page_raw")
        self.stackedWidget.addWidget(self.page_raw)
        self.page_npy = WidgetImportNumpy()
        self.page_npy.setObjectName(u"page_npy")
        self.stackedWidget.addWidget(self.page_npy)
        self.page_h5 = WidgetImport4DSTEMFromHDF5()
        self.page_h5.setObjectName(u"page_h5")
        self.stackedWidget.addWidget(self.page_h5)
        self.page_mat = QWidget()
        self.page_mat.setObjectName(u"page_mat")
        self.stackedWidget.addWidget(self.page_mat)
        self.page_mat_folder = QWidget()
        self.page_mat_folder.setObjectName(u"page_mat_folder")
        self.stackedWidget.addWidget(self.page_mat_folder)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_parent_path = QLineEdit(self.groupBox_2)
        self.lineEdit_parent_path.setObjectName(u"lineEdit_parent_path")

        self.horizontalLayout_2.addWidget(self.lineEdit_parent_path)

        self.pushButton_browse_parent = QPushButton(self.groupBox_2)
        self.pushButton_browse_parent.setObjectName(u"pushButton_browse_parent")

        self.horizontalLayout_2.addWidget(self.pushButton_browse_parent)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEdit_name = QLineEdit(self.groupBox_2)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.horizontalLayout.addWidget(self.lineEdit_name)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

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

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Import 4D-STEM dataset", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Import From", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Import File Type", None))
        self.comboBox_mode.setItemText(0, QCoreApplication.translate("Dialog", u"EMPAD v1.0", None))
        self.comboBox_mode.setItemText(1, QCoreApplication.translate("Dialog", u"EMPAD v0.51 (for NJU)", None))
        self.comboBox_mode.setItemText(2, QCoreApplication.translate("Dialog", u"MerlinEM (.mib)", None))
        self.comboBox_mode.setItemText(3, QCoreApplication.translate("Dialog", u"Digital Micrograph (.dm4)", None))
        self.comboBox_mode.setItemText(4, QCoreApplication.translate("Dialog", u"General Raw Data (Binary)", None))
        self.comboBox_mode.setItemText(5, QCoreApplication.translate("Dialog", u"Numpy 4D Array (.npy)", None))
        self.comboBox_mode.setItemText(6, QCoreApplication.translate("Dialog", u"Other HDF5 Dataset (.h5)", None))
        self.comboBox_mode.setItemText(7, QCoreApplication.translate("Dialog", u"MATLAB 4D Matrix (.mat)", None))
        self.comboBox_mode.setItemText(8, QCoreApplication.translate("Dialog", u"MATLAB Matrix Sequence", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Import To", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Import Dataset to Location:", None))
        self.pushButton_browse_parent.setText(QCoreApplication.translate("Dialog", u"Browse...", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

