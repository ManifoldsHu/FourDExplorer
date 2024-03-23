# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogEditMeta.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(445, 712)
        self.verticalLayout_6 = QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_item_path = QLineEdit(Dialog)
        self.lineEdit_item_path.setObjectName(u"lineEdit_item_path")

        self.verticalLayout_2.addWidget(self.lineEdit_item_path)

        self.lineEdit_meta_key = QLineEdit(Dialog)
        self.lineEdit_meta_key.setObjectName(u"lineEdit_meta_key")

        self.verticalLayout_2.addWidget(self.lineEdit_meta_key)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_browse_item_path = QPushButton(Dialog)
        self.pushButton_browse_item_path.setObjectName(u"pushButton_browse_item_path")

        self.verticalLayout_3.addWidget(self.pushButton_browse_item_path)

        self.pushButton_browse_meta_key = QPushButton(Dialog)
        self.pushButton_browse_meta_key.setObjectName(u"pushButton_browse_meta_key")

        self.verticalLayout_3.addWidget(self.pushButton_browse_meta_key)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.label_current_dtype = QLabel(Dialog)
        self.label_current_dtype.setObjectName(u"label_current_dtype")

        self.horizontalLayout.addWidget(self.label_current_dtype)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_change_dtype = QPushButton(Dialog)
        self.pushButton_change_dtype.setObjectName(u"pushButton_change_dtype")

        self.horizontalLayout.addWidget(self.pushButton_change_dtype)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.stackedWidget_set_value = QStackedWidget(Dialog)
        self.stackedWidget_set_value.setObjectName(u"stackedWidget_set_value")
        self.page_edit_integer = QWidget()
        self.page_edit_integer.setObjectName(u"page_edit_integer")
        self.verticalLayout_5 = QVBoxLayout(self.page_edit_integer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.page_edit_integer)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.spinBox_edit_integer = QSpinBox(self.page_edit_integer)
        self.spinBox_edit_integer.setObjectName(u"spinBox_edit_integer")
        self.spinBox_edit_integer.setMinimum(-2147483468)
        self.spinBox_edit_integer.setMaximum(2147483467)

        self.horizontalLayout_2.addWidget(self.spinBox_edit_integer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.label_unit_int_hint = QLabel(self.page_edit_integer)
        self.label_unit_int_hint.setObjectName(u"label_unit_int_hint")

        self.horizontalLayout_7.addWidget(self.label_unit_int_hint)

        self.label_unit_int = QLabel(self.page_edit_integer)
        self.label_unit_int.setObjectName(u"label_unit_int")

        self.horizontalLayout_7.addWidget(self.label_unit_int)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 180, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.stackedWidget_set_value.addWidget(self.page_edit_integer)
        self.page_edit_float = QWidget()
        self.page_edit_float.setObjectName(u"page_edit_float")
        self.verticalLayout_4 = QVBoxLayout(self.page_edit_float)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.page_edit_float)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.doubleSpinBox_float_decimal = QDoubleSpinBox(self.page_edit_float)
        self.doubleSpinBox_float_decimal.setObjectName(u"doubleSpinBox_float_decimal")
        self.doubleSpinBox_float_decimal.setDecimals(7)
        self.doubleSpinBox_float_decimal.setMinimum(-9.999999000000001)
        self.doubleSpinBox_float_decimal.setMaximum(9.999999000000001)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_float_decimal)

        self.label_5 = QLabel(self.page_edit_float)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.spinBox_float_exp = QSpinBox(self.page_edit_float)
        self.spinBox_float_exp.setObjectName(u"spinBox_float_exp")
        self.spinBox_float_exp.setMinimum(-307)
        self.spinBox_float_exp.setMaximum(307)

        self.horizontalLayout_5.addWidget(self.spinBox_float_exp)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_unit_float_hint = QLabel(self.page_edit_float)
        self.label_unit_float_hint.setObjectName(u"label_unit_float_hint")

        self.horizontalLayout_6.addWidget(self.label_unit_float_hint)

        self.label_unit_float = QLabel(self.page_edit_float)
        self.label_unit_float.setObjectName(u"label_unit_float")

        self.horizontalLayout_6.addWidget(self.label_unit_float)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 180, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.stackedWidget_set_value.addWidget(self.page_edit_float)
        self.page_edit_string = QWidget()
        self.page_edit_string.setObjectName(u"page_edit_string")
        self.verticalLayout_7 = QVBoxLayout(self.page_edit_string)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.label_6 = QLabel(self.page_edit_string)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.plainTextEdit_edit_string = QPlainTextEdit(self.page_edit_string)
        self.plainTextEdit_edit_string.setObjectName(u"plainTextEdit_edit_string")

        self.verticalLayout_7.addWidget(self.plainTextEdit_edit_string)

        self.stackedWidget_set_value.addWidget(self.page_edit_string)

        self.verticalLayout_6.addWidget(self.stackedWidget_set_value)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.plainTextEdit_note = QPlainTextEdit(Dialog)
        self.plainTextEdit_note.setObjectName(u"plainTextEdit_note")

        self.verticalLayout_6.addWidget(self.plainTextEdit_note)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_3.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_3.addWidget(self.pushButton_cancel)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)

        self.stackedWidget_set_value.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Edit Metadata", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Item Path", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Metadata Key", None))
        self.pushButton_browse_item_path.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.pushButton_browse_meta_key.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Value Type:", None))
        self.label_current_dtype.setText(QCoreApplication.translate("Dialog", u"Integer", None))
        self.pushButton_change_dtype.setText(QCoreApplication.translate("Dialog", u"Change Data Type", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Value", None))
        self.label_unit_int_hint.setText(QCoreApplication.translate("Dialog", u"Unit: ", None))
        self.label_unit_int.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Value", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"x10^", None))
        self.label_unit_float_hint.setText(QCoreApplication.translate("Dialog", u"Unit: ", None))
        self.label_unit_float.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Value", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Note", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

