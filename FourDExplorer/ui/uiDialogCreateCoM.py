# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogCreateCoM.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(408, 416)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")

        self.verticalLayout_4.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(
            20, 9, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_parent_path = QLineEdit(Dialog)
        self.lineEdit_parent_path.setObjectName("lineEdit_parent_path")

        self.horizontalLayout.addWidget(self.lineEdit_parent_path)

        self.pushButton_browse = QPushButton(Dialog)
        self.pushButton_browse.setObjectName("pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName("label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.checkBox_CoM = QCheckBox(Dialog)
        self.checkBox_CoM.setObjectName("checkBox_CoM")

        self.verticalLayout_2.addWidget(self.checkBox_CoM)

        self.checkBox_CoMi = QCheckBox(Dialog)
        self.checkBox_CoMi.setObjectName("checkBox_CoMi")

        self.verticalLayout_2.addWidget(self.checkBox_CoMi)

        self.checkBox_CoMj = QCheckBox(Dialog)
        self.checkBox_CoMj.setObjectName("checkBox_CoMj")

        self.verticalLayout_2.addWidget(self.checkBox_CoMj)

        self.checkBox_dCoM = QCheckBox(Dialog)
        self.checkBox_dCoM.setObjectName("checkBox_dCoM")

        self.verticalLayout_2.addWidget(self.checkBox_dCoM)

        self.checkBox_iCoM = QCheckBox(Dialog)
        self.checkBox_iCoM.setObjectName("checkBox_iCoM")

        self.verticalLayout_2.addWidget(self.checkBox_iCoM)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName("label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit_CoM = QLineEdit(Dialog)
        self.lineEdit_CoM.setObjectName("lineEdit_CoM")

        self.verticalLayout_3.addWidget(self.lineEdit_CoM)

        self.lineEdit_CoMi = QLineEdit(Dialog)
        self.lineEdit_CoMi.setObjectName("lineEdit_CoMi")

        self.verticalLayout_3.addWidget(self.lineEdit_CoMi)

        self.lineEdit_CoMj = QLineEdit(Dialog)
        self.lineEdit_CoMj.setObjectName("lineEdit_CoMj")

        self.verticalLayout_3.addWidget(self.lineEdit_CoMj)

        self.lineEdit_dCoM = QLineEdit(Dialog)
        self.lineEdit_dCoM.setObjectName("lineEdit_dCoM")

        self.verticalLayout_3.addWidget(self.lineEdit_dCoM)

        self.lineEdit_iCoM = QLineEdit(Dialog)
        self.lineEdit_iCoM.setObjectName("lineEdit_iCoM")

        self.verticalLayout_3.addWidget(self.lineEdit_iCoM)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_use_CoM = QRadioButton(Dialog)
        self.radioButton_use_CoM.setObjectName("radioButton_use_CoM")

        self.verticalLayout.addWidget(self.radioButton_use_CoM)

        self.radioButton_use_electric = QRadioButton(Dialog)
        self.radioButton_use_electric.setObjectName("radioButton_use_electric")

        self.verticalLayout.addWidget(self.radioButton_use_electric)

        self.checkBox_normalize = QCheckBox(Dialog)
        self.checkBox_normalize.setObjectName("checkBox_normalize")

        self.verticalLayout.addWidget(self.checkBox_normalize)

        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(
            20, 9, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName("pushButton_ok")

        self.horizontalLayout_3.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.horizontalLayout_3.addWidget(self.pushButton_cancel)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.label.setText(
            QCoreApplication.translate(
                "Dialog", "Calculating Center of Mass (CoM)", None
            )
        )
        self.label_2.setText(
            QCoreApplication.translate("Dialog", "Save results to...", None)
        )
        self.pushButton_browse.setText(
            QCoreApplication.translate("Dialog", "Browse...", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("Dialog", "Calculate Items", None)
        )
        self.checkBox_CoM.setText(
            QCoreApplication.translate("Dialog", "CoM vector field", None)
        )
        self.checkBox_CoMi.setText(
            QCoreApplication.translate("Dialog", "CoM vertical component (CoMi)", None)
        )
        self.checkBox_CoMj.setText(
            QCoreApplication.translate(
                "Dialog", "CoM horizontal component (CoMj)", None
            )
        )
        self.checkBox_dCoM.setText(
            QCoreApplication.translate("Dialog", "differentiated CoM (dCoM)", None)
        )
        self.checkBox_iCoM.setText(
            QCoreApplication.translate("Dialog", "integrated CoM (iCoM)", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("Dialog", "New dataset name", None)
        )
        self.radioButton_use_CoM.setText(
            QCoreApplication.translate("Dialog", "Use Center of Mass mapping", None)
        )
        self.radioButton_use_electric.setText(
            QCoreApplication.translate(
                "Dialog", "Use projected electric field mapping", None
            )
        )
        self.checkBox_normalize.setText(
            QCoreApplication.translate(
                "Dialog", "Normalize: set mean field to be zero vector", None
            )
        )
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", "OK", None))
        self.pushButton_cancel.setText(
            QCoreApplication.translate("Dialog", "Cancel", None)
        )

    # retranslateUi
