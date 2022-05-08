# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetImportRaw.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 316)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit_raw_path = QLineEdit(Form)
        self.lineEdit_raw_path.setObjectName(u"lineEdit_raw_path")

        self.horizontalLayout_3.addWidget(self.lineEdit_raw_path)

        self.pushButton_browse = QPushButton(Form)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout_3.addWidget(self.pushButton_browse)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox_scalar_type = QComboBox(Form)
        self.comboBox_scalar_type.addItem("")
        self.comboBox_scalar_type.addItem("")
        self.comboBox_scalar_type.addItem("")
        self.comboBox_scalar_type.setObjectName(u"comboBox_scalar_type")

        self.verticalLayout_3.addWidget(self.comboBox_scalar_type)

        self.comboBox_scalar_size = QComboBox(Form)
        self.comboBox_scalar_size.addItem("")
        self.comboBox_scalar_size.addItem("")
        self.comboBox_scalar_size.addItem("")
        self.comboBox_scalar_size.setObjectName(u"comboBox_scalar_size")

        self.verticalLayout_3.addWidget(self.comboBox_scalar_size)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.spinBox_dp_j = QSpinBox(Form)
        self.spinBox_dp_j.setObjectName(u"spinBox_dp_j")
        self.spinBox_dp_j.setMinimum(1)
        self.spinBox_dp_j.setMaximum(65536)

        self.verticalLayout.addWidget(self.spinBox_dp_j)

        self.spinBox_dp_i = QSpinBox(Form)
        self.spinBox_dp_i.setObjectName(u"spinBox_dp_i")
        self.spinBox_dp_i.setMinimum(1)
        self.spinBox_dp_i.setMaximum(65536)

        self.verticalLayout.addWidget(self.spinBox_dp_i)

        self.spinBox_scan_i = QSpinBox(Form)
        self.spinBox_scan_i.setObjectName(u"spinBox_scan_i")
        self.spinBox_scan_i.setMinimum(1)
        self.spinBox_scan_i.setMaximum(65536)

        self.verticalLayout.addWidget(self.spinBox_scan_i)

        self.spinBox_scan_j = QSpinBox(Form)
        self.spinBox_scan_j.setObjectName(u"spinBox_scan_j")
        self.spinBox_scan_j.setMinimum(1)
        self.spinBox_scan_j.setMaximum(65536)

        self.verticalLayout.addWidget(self.spinBox_scan_j)

        self.spinBox_offset_to_first_image = QSpinBox(Form)
        self.spinBox_offset_to_first_image.setObjectName(u"spinBox_offset_to_first_image")
        self.spinBox_offset_to_first_image.setMaximum(16777215)

        self.verticalLayout.addWidget(self.spinBox_offset_to_first_image)

        self.spinBox_gap_between_images = QSpinBox(Form)
        self.spinBox_gap_between_images.setObjectName(u"spinBox_gap_between_images")
        self.spinBox_gap_between_images.setMaximum(16777215)

        self.verticalLayout.addWidget(self.spinBox_gap_between_images)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.checkBox_little_endian = QCheckBox(Form)
        self.checkBox_little_endian.setObjectName(u"checkBox_little_endian")

        self.verticalLayout_5.addWidget(self.checkBox_little_endian)

        self.verticalSpacer = QSpacerItem(20, 11, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Raw file", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse...", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Scalar Type", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Scalar Size", None))
        self.comboBox_scalar_type.setItemText(0, QCoreApplication.translate("Form", u"integer", None))
        self.comboBox_scalar_type.setItemText(1, QCoreApplication.translate("Form", u"usigned integer", None))
        self.comboBox_scalar_type.setItemText(2, QCoreApplication.translate("Form", u"float", None))

        self.comboBox_scalar_size.setItemText(0, QCoreApplication.translate("Form", u"8 bit", None))
        self.comboBox_scalar_size.setItemText(1, QCoreApplication.translate("Form", u"16 bit", None))
        self.comboBox_scalar_size.setItemText(2, QCoreApplication.translate("Form", u"32 bit", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"Image Width (pixel)", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Image Height (pixel)", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Number of Scanning Columns (scan_i)", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Number of Scanning Rows (scan_j)", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Offset to first Image (bytes)", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Gap between Images (bytes)", None))
        self.checkBox_little_endian.setText(QCoreApplication.translate("Form", u"Little-endian byte order", None))
    # retranslateUi

