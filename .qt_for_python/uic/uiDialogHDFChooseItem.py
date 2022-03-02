# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogHDFChooseItem.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from bin.Widgets.WidgetBaseHDFViewer import WidgetBaseHDFViewer

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(357, 510)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_info = QLabel(Dialog)
        self.label_info.setObjectName(u"label_info")

        self.verticalLayout.addWidget(self.label_info)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_parent_path = QLabel(Dialog)
        self.label_parent_path.setObjectName(u"label_parent_path")

        self.horizontalLayout.addWidget(self.label_parent_path)

        self.lineEdit_parent_path = QLineEdit(Dialog)
        self.lineEdit_parent_path.setObjectName(u"lineEdit_parent_path")

        self.horizontalLayout.addWidget(self.lineEdit_parent_path)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget_viewer = WidgetBaseHDFViewer(Dialog)
        self.widget_viewer.setObjectName(u"widget_viewer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_viewer.sizePolicy().hasHeightForWidth())
        self.widget_viewer.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.widget_viewer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_2.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_info.setText(QCoreApplication.translate("Dialog", u"Browse: choose an item", None))
        self.label_parent_path.setText(QCoreApplication.translate("Dialog", u"Parent Path", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

