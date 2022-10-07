# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogFindRotationAngle.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from bin.Widgets.WidgetPlots import WidgetPlotLine

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(654, 420)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_vector_field_path = QLineEdit(Dialog)
        self.lineEdit_vector_field_path.setObjectName(u"lineEdit_vector_field_path")

        self.horizontalLayout_3.addWidget(self.lineEdit_vector_field_path)

        self.pushButton_browse = QPushButton(Dialog)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout_3.addWidget(self.pushButton_browse)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.widget_curve = WidgetPlotLine(Dialog)
        self.widget_curve.setObjectName(u"widget_curve")

        self.verticalLayout.addWidget(self.widget_curve)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox_rotation_angle = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_rotation_angle.setObjectName(u"doubleSpinBox_rotation_angle")

        self.horizontalLayout.addWidget(self.doubleSpinBox_rotation_angle)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(358, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_2.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Find the rotation angle of every vector, corresponding to convergent field.", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Vector field path:", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Rotation Angle: Maximum Divergence or Minimum Curl (deg):", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

