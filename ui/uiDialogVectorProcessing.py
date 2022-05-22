# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogVectorProcessing.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(314, 306)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_subtract_mean_vector = QPushButton(self.groupBox)
        self.pushButton_subtract_mean_vector.setObjectName(u"pushButton_subtract_mean_vector")

        self.verticalLayout.addWidget(self.pushButton_subtract_mean_vector)

        self.pushButton_rotate_vector_angle = QPushButton(self.groupBox)
        self.pushButton_rotate_vector_angle.setObjectName(u"pushButton_rotate_vector_angle")

        self.verticalLayout.addWidget(self.pushButton_rotate_vector_angle)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_calculate_potential = QPushButton(self.groupBox_2)
        self.pushButton_calculate_potential.setObjectName(u"pushButton_calculate_potential")

        self.verticalLayout_2.addWidget(self.pushButton_calculate_potential)

        self.pushButton_calculate_divergence = QPushButton(self.groupBox_2)
        self.pushButton_calculate_divergence.setObjectName(u"pushButton_calculate_divergence")

        self.verticalLayout_2.addWidget(self.pushButton_calculate_divergence)

        self.pushButton_calculate_curl = QPushButton(self.groupBox_2)
        self.pushButton_calculate_curl.setObjectName(u"pushButton_calculate_curl")

        self.verticalLayout_2.addWidget(self.pushButton_calculate_curl)

        self.pushButton_vec_i = QPushButton(self.groupBox_2)
        self.pushButton_vec_i.setObjectName(u"pushButton_vec_i")

        self.verticalLayout_2.addWidget(self.pushButton_vec_i)

        self.pushButton_vec_j = QPushButton(self.groupBox_2)
        self.pushButton_vec_j.setObjectName(u"pushButton_vec_j")

        self.verticalLayout_2.addWidget(self.pushButton_vec_j)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Generate Vector Field", None))
        self.pushButton_subtract_mean_vector.setText(QCoreApplication.translate("Dialog", u"Subtract Vector Offset", None))
        self.pushButton_rotate_vector_angle.setText(QCoreApplication.translate("Dialog", u"Rotate Vector Angle", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Generate Images", None))
        self.pushButton_calculate_potential.setText(QCoreApplication.translate("Dialog", u"Calculate Potential", None))
        self.pushButton_calculate_divergence.setText(QCoreApplication.translate("Dialog", u"Calculate Divergence", None))
        self.pushButton_calculate_curl.setText(QCoreApplication.translate("Dialog", u"Calculate Curl", None))
        self.pushButton_vec_i.setText(QCoreApplication.translate("Dialog", u"Slice i component", None))
        self.pushButton_vec_j.setText(QCoreApplication.translate("Dialog", u"Slice j component", None))
    # retranslateUi

