# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogAdjustPatchEffects.ui'
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
    QComboBox,
    QDialog,
    QDoubleSpinBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(252, 276)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_patch_kind = QLabel(Dialog)
        self.label_patch_kind.setObjectName("label_patch_kind")

        self.horizontalLayout_2.addWidget(self.label_patch_kind)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(
            20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName("label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName("label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName("label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName("label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName("label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.doubleSpinBox_alpha = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_alpha.setObjectName("doubleSpinBox_alpha")
        self.doubleSpinBox_alpha.setMaximum(1.000000000000000)
        self.doubleSpinBox_alpha.setSingleStep(0.010000000000000)
        self.doubleSpinBox_alpha.setValue(1.000000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBox_alpha)

        self.comboBox_edge_color = QComboBox(Dialog)
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.addItem("")
        self.comboBox_edge_color.setObjectName("comboBox_edge_color")

        self.verticalLayout.addWidget(self.comboBox_edge_color)

        self.comboBox_face_color = QComboBox(Dialog)
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.addItem("")
        self.comboBox_face_color.setObjectName("comboBox_face_color")

        self.verticalLayout.addWidget(self.comboBox_face_color)

        self.comboBox_hatch = QComboBox(Dialog)
        self.comboBox_hatch.addItem("")
        self.comboBox_hatch.addItem("")
        self.comboBox_hatch.addItem("")
        self.comboBox_hatch.addItem("")
        self.comboBox_hatch.addItem("")
        self.comboBox_hatch.addItem("")
        self.comboBox_hatch.addItem("")
        self.comboBox_hatch.addItem("")
        self.comboBox_hatch.addItem("")
        self.comboBox_hatch.addItem("")
        self.comboBox_hatch.addItem("")
        self.comboBox_hatch.setObjectName("comboBox_hatch")

        self.verticalLayout.addWidget(self.comboBox_hatch)

        self.comboBox_line_style = QComboBox(Dialog)
        self.comboBox_line_style.addItem("")
        self.comboBox_line_style.addItem("")
        self.comboBox_line_style.addItem("")
        self.comboBox_line_style.addItem("")
        self.comboBox_line_style.addItem("")
        self.comboBox_line_style.setObjectName("comboBox_line_style")

        self.verticalLayout.addWidget(self.comboBox_line_style)

        self.doubleSpinBox_line_width = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_line_width.setObjectName("doubleSpinBox_line_width")
        self.doubleSpinBox_line_width.setValue(2.000000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBox_line_width)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.checkBox_fill = QCheckBox(Dialog)
        self.checkBox_fill.setObjectName("checkBox_fill")

        self.verticalLayout_3.addWidget(self.checkBox_fill)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(
            20, 2, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

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
        self.label.setText(QCoreApplication.translate("Dialog", "Artist:", None))
        self.label_patch_kind.setText(
            QCoreApplication.translate("Dialog", "Patch", None)
        )
        self.label_2.setText(QCoreApplication.translate("Dialog", "Alpha", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", "Edge Color", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", "Face Color", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", "Hatch", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", "Line Style", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", "Line Width", None))
        self.comboBox_edge_color.setItemText(
            0, QCoreApplication.translate("Dialog", "black", None)
        )
        self.comboBox_edge_color.setItemText(
            1, QCoreApplication.translate("Dialog", "white", None)
        )
        self.comboBox_edge_color.setItemText(
            2, QCoreApplication.translate("Dialog", "blue", None)
        )
        self.comboBox_edge_color.setItemText(
            3, QCoreApplication.translate("Dialog", "orange", None)
        )
        self.comboBox_edge_color.setItemText(
            4, QCoreApplication.translate("Dialog", "green", None)
        )
        self.comboBox_edge_color.setItemText(
            5, QCoreApplication.translate("Dialog", "red", None)
        )
        self.comboBox_edge_color.setItemText(
            6, QCoreApplication.translate("Dialog", "purple", None)
        )
        self.comboBox_edge_color.setItemText(
            7, QCoreApplication.translate("Dialog", "brown", None)
        )
        self.comboBox_edge_color.setItemText(
            8, QCoreApplication.translate("Dialog", "pink", None)
        )
        self.comboBox_edge_color.setItemText(
            9, QCoreApplication.translate("Dialog", "gray", None)
        )
        self.comboBox_edge_color.setItemText(
            10, QCoreApplication.translate("Dialog", "olive", None)
        )
        self.comboBox_edge_color.setItemText(
            11, QCoreApplication.translate("Dialog", "cyan", None)
        )
        self.comboBox_edge_color.setItemText(
            12, QCoreApplication.translate("Dialog", "others", None)
        )

        self.comboBox_face_color.setItemText(
            0, QCoreApplication.translate("Dialog", "black", None)
        )
        self.comboBox_face_color.setItemText(
            1, QCoreApplication.translate("Dialog", "white", None)
        )
        self.comboBox_face_color.setItemText(
            2, QCoreApplication.translate("Dialog", "blue", None)
        )
        self.comboBox_face_color.setItemText(
            3, QCoreApplication.translate("Dialog", "orange", None)
        )
        self.comboBox_face_color.setItemText(
            4, QCoreApplication.translate("Dialog", "green", None)
        )
        self.comboBox_face_color.setItemText(
            5, QCoreApplication.translate("Dialog", "red", None)
        )
        self.comboBox_face_color.setItemText(
            6, QCoreApplication.translate("Dialog", "purple", None)
        )
        self.comboBox_face_color.setItemText(
            7, QCoreApplication.translate("Dialog", "brown", None)
        )
        self.comboBox_face_color.setItemText(
            8, QCoreApplication.translate("Dialog", "pink", None)
        )
        self.comboBox_face_color.setItemText(
            9, QCoreApplication.translate("Dialog", "gray", None)
        )
        self.comboBox_face_color.setItemText(
            10, QCoreApplication.translate("Dialog", "olive", None)
        )
        self.comboBox_face_color.setItemText(
            11, QCoreApplication.translate("Dialog", "cyan", None)
        )
        self.comboBox_face_color.setItemText(
            12, QCoreApplication.translate("Dialog", "others", None)
        )

        self.comboBox_hatch.setItemText(
            0, QCoreApplication.translate("Dialog", "none", None)
        )
        self.comboBox_hatch.setItemText(
            1, QCoreApplication.translate("Dialog", "diagonal hatching (/)", None)
        )
        self.comboBox_hatch.setItemText(
            2, QCoreApplication.translate("Dialog", "back diagonal (\\)", None)
        )
        self.comboBox_hatch.setItemText(
            3, QCoreApplication.translate("Dialog", "vertical (|)", None)
        )
        self.comboBox_hatch.setItemText(
            4, QCoreApplication.translate("Dialog", "horizontal (-)", None)
        )
        self.comboBox_hatch.setItemText(
            5, QCoreApplication.translate("Dialog", "crossed (+)", None)
        )
        self.comboBox_hatch.setItemText(
            6, QCoreApplication.translate("Dialog", "crossed diagonal (x)", None)
        )
        self.comboBox_hatch.setItemText(
            7, QCoreApplication.translate("Dialog", "small circle (o)", None)
        )
        self.comboBox_hatch.setItemText(
            8, QCoreApplication.translate("Dialog", "large circle (O)", None)
        )
        self.comboBox_hatch.setItemText(
            9, QCoreApplication.translate("Dialog", "dots (.)", None)
        )
        self.comboBox_hatch.setItemText(
            10, QCoreApplication.translate("Dialog", "stars (*)", None)
        )

        self.comboBox_line_style.setItemText(
            0, QCoreApplication.translate("Dialog", "solid", None)
        )
        self.comboBox_line_style.setItemText(
            1, QCoreApplication.translate("Dialog", "dashed", None)
        )
        self.comboBox_line_style.setItemText(
            2, QCoreApplication.translate("Dialog", "dashdot", None)
        )
        self.comboBox_line_style.setItemText(
            3, QCoreApplication.translate("Dialog", "dotted", None)
        )
        self.comboBox_line_style.setItemText(
            4, QCoreApplication.translate("Dialog", "none", None)
        )

        self.checkBox_fill.setText(QCoreApplication.translate("Dialog", "Fill", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", "OK", None))
        self.pushButton_cancel.setText(
            QCoreApplication.translate("Dialog", "Cancel", None)
        )

    # retranslateUi
