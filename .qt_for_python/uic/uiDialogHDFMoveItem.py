# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogHDFMoveItem.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(389, 198)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 26, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_item_path = QLineEdit(Dialog)
        self.lineEdit_item_path.setObjectName(u"lineEdit_item_path")

        self.horizontalLayout_2.addWidget(self.lineEdit_item_path)

        self.pushButton_browse_item = QPushButton(Dialog)
        self.pushButton_browse_item.setObjectName(u"pushButton_browse_item")

        self.horizontalLayout_2.addWidget(self.pushButton_browse_item)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_dest_path = QLineEdit(Dialog)
        self.lineEdit_dest_path.setObjectName(u"lineEdit_dest_path")

        self.horizontalLayout.addWidget(self.lineEdit_dest_path)

        self.pushButton_browse_dest = QPushButton(Dialog)
        self.pushButton_browse_dest.setObjectName(u"pushButton_browse_dest")

        self.horizontalLayout.addWidget(self.pushButton_browse_dest)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 26, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

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


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Move: move a group or data into a new group.", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Item to be moved", None))
        self.pushButton_browse_item.setText(QCoreApplication.translate("Dialog", u"Browse...", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Destination", None))
        self.pushButton_browse_dest.setText(QCoreApplication.translate("Dialog", u"Browse...", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

