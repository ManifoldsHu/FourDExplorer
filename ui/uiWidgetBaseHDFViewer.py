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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTreeView,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(343, 549)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_HDF = QLabel(Form)
        self.label_HDF.setObjectName(u"label_HDF")

        self.verticalLayout.addWidget(self.label_HDF)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_search = QLineEdit(Form)
        self.lineEdit_search.setObjectName(u"lineEdit_search")

        self.horizontalLayout.addWidget(self.lineEdit_search)

        self.pushButton_search = QPushButton(Form)
        self.pushButton_search.setObjectName(u"pushButton_search")

        self.horizontalLayout.addWidget(self.pushButton_search)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.treeView_HDF = QTreeView(Form)
        self.treeView_HDF.setObjectName(u"treeView_HDF")

        self.verticalLayout.addWidget(self.treeView_HDF)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_refresh = QPushButton(Form)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.horizontalLayout_2.addWidget(self.pushButton_refresh)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_HDF.setText(QCoreApplication.translate("Form", u"Hierarchical Data Format (HDF) Tree", None))
        self.pushButton_search.setText(QCoreApplication.translate("Form", u"Search Next", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("Form", u"Refresh", None))
    # retranslateUi

