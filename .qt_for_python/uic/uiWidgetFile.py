# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetFile.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLineEdit, QListView,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

from bin.Widgets.WidgetHDFViewer import WidgetHDFViewer

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(346, 892)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 309, 1384))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 720))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_HDFTreeView = WidgetHDFViewer(self.groupBox)
        self.widget_HDFTreeView.setObjectName(u"widget_HDFTreeView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_HDFTreeView.sizePolicy().hasHeightForWidth())
        self.widget_HDFTreeView.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.widget_HDFTreeView)

        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_new_or_close_file = QPushButton(self.widget)
        self.pushButton_new_or_close_file.setObjectName(u"pushButton_new_or_close_file")

        self.verticalLayout.addWidget(self.pushButton_new_or_close_file)

        self.pushButton_import_data = QPushButton(self.widget)
        self.pushButton_import_data.setObjectName(u"pushButton_import_data")

        self.verticalLayout.addWidget(self.pushButton_import_data)

        self.pushButton_export_data = QPushButton(self.widget)
        self.pushButton_export_data.setObjectName(u"pushButton_export_data")

        self.verticalLayout.addWidget(self.pushButton_export_data)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(0, 640))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineEdit_working_directory = QLineEdit(self.groupBox_2)
        self.lineEdit_working_directory.setObjectName(u"lineEdit_working_directory")

        self.verticalLayout_5.addWidget(self.lineEdit_working_directory)

        self.listView_working_directory = QListView(self.groupBox_2)
        self.listView_working_directory.setObjectName(u"listView_working_directory")

        self.verticalLayout_5.addWidget(self.listView_working_directory)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"HDF Hierarchy", None))
        self.pushButton_new_or_close_file.setText(QCoreApplication.translate("Form", u"New H5 File", None))
        self.pushButton_import_data.setText(QCoreApplication.translate("Form", u"Import Data", None))
        self.pushButton_export_data.setText(QCoreApplication.translate("Form", u"Export Data", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Working Directory", None))
    # retranslateUi

