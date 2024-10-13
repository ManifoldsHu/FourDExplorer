# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetImportHDF5.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(457, 579)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_file_path = QLineEdit(Form)
        self.lineEdit_file_path.setObjectName(u"lineEdit_file_path")

        self.horizontalLayout.addWidget(self.lineEdit_file_path)

        self.pushButton_browse = QPushButton(Form)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.treeWidget_other_hdf5 = QTreeWidget(Form)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_other_hdf5.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_other_hdf5.setObjectName(u"treeWidget_other_hdf5")

        self.verticalLayout.addWidget(self.treeWidget_other_hdf5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"HDF5 File", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Choose 4D-STEM Dataset to Import", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Only 4-dimensional datasets are listed", None))
    # retranslateUi

