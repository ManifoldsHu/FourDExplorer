# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogChangeDataType.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(482, 300)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_item_path = QLineEdit(Dialog)
        self.lineEdit_item_path.setObjectName(u"lineEdit_item_path")

        self.horizontalLayout.addWidget(self.lineEdit_item_path)

        self.pushButton_browse = QPushButton(Dialog)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit_current_type = QLineEdit(Dialog)
        self.lineEdit_current_type.setObjectName(u"lineEdit_current_type")

        self.verticalLayout_3.addWidget(self.lineEdit_current_type)

        self.comboBox_target_type = QComboBox(Dialog)
        self.comboBox_target_type.addItem("")
        self.comboBox_target_type.addItem("")
        self.comboBox_target_type.addItem("")
        self.comboBox_target_type.addItem("")
        self.comboBox_target_type.addItem("")
        self.comboBox_target_type.setObjectName(u"comboBox_target_type")

        self.verticalLayout_3.addWidget(self.comboBox_target_type)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.stackedWidget_introduce = QStackedWidget(Dialog)
        self.stackedWidget_introduce.setObjectName(u"stackedWidget_introduce")
        self.page_data = QWidget()
        self.page_data.setObjectName(u"page_data")
        self.verticalLayout_8 = QVBoxLayout(self.page_data)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.textBrowser_data = QTextBrowser(self.page_data)
        self.textBrowser_data.setObjectName(u"textBrowser_data")

        self.verticalLayout_8.addWidget(self.textBrowser_data)

        self.stackedWidget_introduce.addWidget(self.page_data)
        self.page_line = QWidget()
        self.page_line.setObjectName(u"page_line")
        self.verticalLayout_7 = QVBoxLayout(self.page_line)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.textBrowser_line = QTextBrowser(self.page_line)
        self.textBrowser_line.setObjectName(u"textBrowser_line")

        self.verticalLayout_7.addWidget(self.textBrowser_line)

        self.stackedWidget_introduce.addWidget(self.page_line)
        self.page_image = QWidget()
        self.page_image.setObjectName(u"page_image")
        self.verticalLayout_6 = QVBoxLayout(self.page_image)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textBrowser_image = QTextBrowser(self.page_image)
        self.textBrowser_image.setObjectName(u"textBrowser_image")

        self.verticalLayout_6.addWidget(self.textBrowser_image)

        self.stackedWidget_introduce.addWidget(self.page_image)
        self.page_vector_field = QWidget()
        self.page_vector_field.setObjectName(u"page_vector_field")
        self.verticalLayout_5 = QVBoxLayout(self.page_vector_field)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textBrowser_vector_field = QTextBrowser(self.page_vector_field)
        self.textBrowser_vector_field.setObjectName(u"textBrowser_vector_field")

        self.verticalLayout_5.addWidget(self.textBrowser_vector_field)

        self.stackedWidget_introduce.addWidget(self.page_vector_field)
        self.page_fourdstem = QWidget()
        self.page_fourdstem.setObjectName(u"page_fourdstem")
        self.verticalLayout = QVBoxLayout(self.page_fourdstem)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser_fourdstem = QTextBrowser(self.page_fourdstem)
        self.textBrowser_fourdstem.setObjectName(u"textBrowser_fourdstem")

        self.verticalLayout.addWidget(self.textBrowser_fourdstem)

        self.stackedWidget_introduce.addWidget(self.page_fourdstem)

        self.verticalLayout_4.addWidget(self.stackedWidget_introduce)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_3.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_3.addWidget(self.pushButton_cancel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)

        self.stackedWidget_introduce.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Item's Path", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Current Type:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Target Type:", None))
        self.comboBox_target_type.setItemText(0, QCoreApplication.translate("Dialog", u"Data", None))
        self.comboBox_target_type.setItemText(1, QCoreApplication.translate("Dialog", u"Line", None))
        self.comboBox_target_type.setItemText(2, QCoreApplication.translate("Dialog", u"Image", None))
        self.comboBox_target_type.setItemText(3, QCoreApplication.translate("Dialog", u"VectorField", None))
        self.comboBox_target_type.setItemText(4, QCoreApplication.translate("Dialog", u"FourDSTEM", None))

        self.textBrowser_data.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dataset with arbitrary shape. </p></body></html>", None))
        self.textBrowser_line.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The shape of Line should be (length,), i.e. it must be a 1-dimensional array.</p></body></html>", None))
        self.textBrowser_image.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The shape of Image should be like (height, width). NOTE: all images considered here are single channel, NOT RGB/RGBA or other colored images. </p></body></html>", None))
        self.textBrowser_vector_field.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The shape of the Vector Field should be like (2,  height, width), in which the first layer of the tensor is the i-direction component distribution of the vector field, while the second layer is the j-direction distribution. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In 4D-STEM, vector"
                        " field can be produced by Differentiate Phase Contrast (DPC) with segmented electron detectors, Center of Mass (CoM) and by calculating gradient of a 2D scalar matrix (typically potential or phase). </p></body></html>", None))
        self.textBrowser_fourdstem.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The shape of the 4D-STEM dataset should be like (scan_i, scan_j, dp_i, dp_j), where scan_i and scan_j indicate scanning steps of electron beam (probe), and dp_i and dp_j are the length of every single image (diffraction pattern) acquired by the camera.</p></body></html>", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

