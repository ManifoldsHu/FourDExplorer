# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetImportMerlin.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_mib_path = QLineEdit(Form)
        self.lineEdit_mib_path.setObjectName("lineEdit_mib_path")

        self.verticalLayout_3.addWidget(self.lineEdit_mib_path)

        self.lineEdit_hdr_path = QLineEdit(Form)
        self.lineEdit_hdr_path.setObjectName("lineEdit_hdr_path")

        self.verticalLayout_3.addWidget(self.lineEdit_hdr_path)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_browse_mib = QPushButton(Form)
        self.pushButton_browse_mib.setObjectName("pushButton_browse_mib")

        self.verticalLayout_2.addWidget(self.pushButton_browse_mib)

        self.pushButton_browse_hdr = QPushButton(Form)
        self.pushButton_browse_hdr.setObjectName("pushButton_browse_hdr")

        self.verticalLayout_2.addWidget(self.pushButton_browse_hdr)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.checkBox_default_scan = QCheckBox(Form)
        self.checkBox_default_scan.setObjectName("checkBox_default_scan")

        self.verticalLayout_6.addWidget(self.checkBox_default_scan)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName("label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName("label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.spinBox_scan_i = QSpinBox(Form)
        self.spinBox_scan_i.setObjectName("spinBox_scan_i")

        self.verticalLayout_5.addWidget(self.spinBox_scan_i)

        self.spinBox_scan_j = QSpinBox(Form)
        self.spinBox_scan_j.setObjectName("spinBox_scan_j")

        self.verticalLayout_5.addWidget(self.spinBox_scan_j)

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(
            20, 133, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText(
            QCoreApplication.translate("Form", "MerlinEM MIB file", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("Form", "MerlinEM HDR file", None)
        )
        self.pushButton_browse_mib.setText(
            QCoreApplication.translate("Form", "Browse...", None)
        )
        self.pushButton_browse_hdr.setText(
            QCoreApplication.translate("Form", "Browse...", None)
        )
        self.checkBox_default_scan.setText(
            QCoreApplication.translate(
                "Form", "Set scanning coordinate according to the .hdr file", None
            )
        )
        self.label_3.setText(
            QCoreApplication.translate("Form", "scanning steps (i-direction)", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("Form", "scanning steps (j-direction)", None)
        )

    # retranslateUi
