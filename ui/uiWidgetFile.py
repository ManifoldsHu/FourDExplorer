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
from PySide6.QtWidgets import (QApplication, QLineEdit, QListView, QSizePolicy,
    QToolBox, QVBoxLayout, QWidget)

from bin.Widgets.WidgetHDFViewer import WidgetHDFViewer

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(253, 892)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 9, 2)
        self.toolBox_file = QToolBox(Form)
        self.toolBox_file.setObjectName(u"toolBox_file")
        self.page_hdf_viewer = WidgetHDFViewer()
        self.page_hdf_viewer.setObjectName(u"page_hdf_viewer")
        self.page_hdf_viewer.setGeometry(QRect(0, 0, 235, 830))
        self.toolBox_file.addItem(self.page_hdf_viewer, u"Hierarchy Data Format")
        self.page_working_directory = QWidget()
        self.page_working_directory.setObjectName(u"page_working_directory")
        self.page_working_directory.setGeometry(QRect(0, 0, 235, 823))
        self.verticalLayout = QVBoxLayout(self.page_working_directory)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.lineEdit_working_directory = QLineEdit(self.page_working_directory)
        self.lineEdit_working_directory.setObjectName(u"lineEdit_working_directory")

        self.verticalLayout.addWidget(self.lineEdit_working_directory)

        self.listView_working_directory = QListView(self.page_working_directory)
        self.listView_working_directory.setObjectName(u"listView_working_directory")

        self.verticalLayout.addWidget(self.listView_working_directory)

        self.toolBox_file.addItem(self.page_working_directory, u"Working Directory")

        self.verticalLayout_2.addWidget(self.toolBox_file)


        self.retranslateUi(Form)

        self.toolBox_file.setCurrentIndex(0)
        self.toolBox_file.layout().setSpacing(6)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.toolBox_file.setItemText(self.toolBox_file.indexOf(self.page_hdf_viewer), QCoreApplication.translate("Form", u"Hierarchy Data Format", None))
        self.toolBox_file.setItemText(self.toolBox_file.indexOf(self.page_working_directory), QCoreApplication.translate("Form", u"Working Directory", None))
    # retranslateUi

