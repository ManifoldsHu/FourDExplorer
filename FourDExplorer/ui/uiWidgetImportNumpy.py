# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetImportNumpy.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_file_path = QLineEdit(Form)
        self.lineEdit_file_path.setObjectName(u"lineEdit_file_path")

        self.horizontalLayout_2.addWidget(self.lineEdit_file_path)

        self.pushButton_browse_file = QPushButton(Form)
        self.pushButton_browse_file.setObjectName(u"pushButton_browse_file")

        self.horizontalLayout_2.addWidget(self.pushButton_browse_file)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_npz = QWidget()
        self.page_npz.setObjectName(u"page_npz")
        self.verticalLayout = QVBoxLayout(self.page_npz)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.page_npz)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox_array_name = QComboBox(self.page_npz)
        self.comboBox_array_name.setObjectName(u"comboBox_array_name")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_array_name.sizePolicy().hasHeightForWidth())
        self.comboBox_array_name.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.comboBox_array_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_npz)
        self.page_npy = QWidget()
        self.page_npy.setObjectName(u"page_npy")
        self.stackedWidget.addWidget(self.page_npy)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Numpy NPY/NPZ file", None))
        self.pushButton_browse_file.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"The array must be 4-dimensional", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Array Name", None))
    # retranslateUi

