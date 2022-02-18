# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetBaseHDFViewer.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QSizePolicy, QTreeView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(343, 474)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_current_item = QLabel(Form)
        self.label_current_item.setObjectName(u"label_current_item")

        self.verticalLayout.addWidget(self.label_current_item)

        self.lineEdit_current_path = QLineEdit(Form)
        self.lineEdit_current_path.setObjectName(u"lineEdit_current_path")

        self.verticalLayout.addWidget(self.lineEdit_current_path)

        self.label_HDF = QLabel(Form)
        self.label_HDF.setObjectName(u"label_HDF")

        self.verticalLayout.addWidget(self.label_HDF)

        self.treeView_HDF = QTreeView(Form)
        self.treeView_HDF.setObjectName(u"treeView_HDF")

        self.verticalLayout.addWidget(self.treeView_HDF)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_current_item.setText(QCoreApplication.translate("Form", u"Current Item", None))
        self.label_HDF.setText(QCoreApplication.translate("Form", u"Hierarchical Data Format (HDF) Tree", None))
    # retranslateUi

