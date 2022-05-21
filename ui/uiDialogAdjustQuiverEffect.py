# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogAdjustQuiverEffect.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 65, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.doubleSpinBox_scale = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_scale.setObjectName(u"doubleSpinBox_scale")

        self.verticalLayout_2.addWidget(self.doubleSpinBox_scale)

        self.doubleSpinBox_width = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_width.setObjectName(u"doubleSpinBox_width")

        self.verticalLayout_2.addWidget(self.doubleSpinBox_width)

        self.comboBox_color = QComboBox(Dialog)
        self.comboBox_color.addItem("")
        self.comboBox_color.addItem("")
        self.comboBox_color.addItem("")
        self.comboBox_color.addItem("")
        self.comboBox_color.addItem("")
        self.comboBox_color.addItem("")
        self.comboBox_color.addItem("")
        self.comboBox_color.addItem("")
        self.comboBox_color.setObjectName(u"comboBox_color")

        self.verticalLayout_2.addWidget(self.comboBox_color)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 65, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout.addWidget(self.pushButton_cancel)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Adjust Vector Field Quiver Display Effect", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Arrow Length Scale", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Arrow Width", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Arrow Color", None))
        self.comboBox_color.setItemText(0, QCoreApplication.translate("Dialog", u"blue", None))
        self.comboBox_color.setItemText(1, QCoreApplication.translate("Dialog", u"cyan", None))
        self.comboBox_color.setItemText(2, QCoreApplication.translate("Dialog", u"green", None))
        self.comboBox_color.setItemText(3, QCoreApplication.translate("Dialog", u"black", None))
        self.comboBox_color.setItemText(4, QCoreApplication.translate("Dialog", u"magenta", None))
        self.comboBox_color.setItemText(5, QCoreApplication.translate("Dialog", u"red", None))
        self.comboBox_color.setItemText(6, QCoreApplication.translate("Dialog", u"white", None))
        self.comboBox_color.setItemText(7, QCoreApplication.translate("Dialog", u"yellow", None))

        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

