# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetAlignmentFDDNet.ui'
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
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(400, 392)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")

        self.verticalLayout_3.addWidget(self.label_16)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")

        self.verticalLayout.addWidget(self.label_17)

        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")

        self.verticalLayout.addWidget(self.label_18)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName("label_19")

        self.verticalLayout.addWidget(self.label_19)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName("label_20")

        self.verticalLayout.addWidget(self.label_20)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName("label_21")

        self.verticalLayout.addWidget(self.label_21)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_fddnet_center_shift_ci = QLabel(self.groupBox_2)
        self.label_fddnet_center_shift_ci.setObjectName("label_fddnet_center_shift_ci")

        self.verticalLayout_2.addWidget(self.label_fddnet_center_shift_ci)

        self.label_fddnet_center_shift_cj = QLabel(self.groupBox_2)
        self.label_fddnet_center_shift_cj.setObjectName("label_fddnet_center_shift_cj")

        self.verticalLayout_2.addWidget(self.label_fddnet_center_shift_cj)

        self.label_fddnet_elliptical_a = QLabel(self.groupBox_2)
        self.label_fddnet_elliptical_a.setObjectName("label_fddnet_elliptical_a")

        self.verticalLayout_2.addWidget(self.label_fddnet_elliptical_a)

        self.label_fddnet_elliptical_b = QLabel(self.groupBox_2)
        self.label_fddnet_elliptical_b.setObjectName("label_fddnet_elliptical_b")

        self.verticalLayout_2.addWidget(self.label_fddnet_elliptical_b)

        self.label_fddnet_elliptical_angle = QLabel(self.groupBox_2)
        self.label_fddnet_elliptical_angle.setObjectName(
            "label_fddnet_elliptical_angle"
        )

        self.verticalLayout_2.addWidget(self.label_fddnet_elliptical_angle)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.checkBox_show_shifted_dp = QCheckBox(self.groupBox_2)
        self.checkBox_show_shifted_dp.setObjectName("checkBox_show_shifted_dp")

        self.verticalLayout_3.addWidget(self.checkBox_show_shifted_dp)

        self.checkBox_show_measured_ellipse = QCheckBox(self.groupBox_2)
        self.checkBox_show_measured_ellipse.setObjectName(
            "checkBox_show_measured_ellipse"
        )

        self.verticalLayout_3.addWidget(self.checkBox_show_measured_ellipse)

        self.pushButton_adjust_ellipse_effects = QPushButton(self.groupBox_2)
        self.pushButton_adjust_ellipse_effects.setObjectName(
            "pushButton_adjust_ellipse_effects"
        )

        self.verticalLayout_3.addWidget(self.pushButton_adjust_ellipse_effects)

        self.verticalSpacer_2 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_generate_shift_vec = QPushButton(self.groupBox)
        self.pushButton_generate_shift_vec.setObjectName(
            "pushButton_generate_shift_vec"
        )

        self.verticalLayout_4.addWidget(self.pushButton_generate_shift_vec)

        self.verticalLayout_5.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(
            20, 54, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.groupBox_2.setTitle(
            QCoreApplication.translate("Form", "Shift Diffraction Patterns", None)
        )
        self.label_16.setText(
            QCoreApplication.translate("Form", "FDDNet Prediction Result", None)
        )
        self.label_17.setText(
            QCoreApplication.translate("Form", "Disk Center Shift (i)", None)
        )
        self.label_18.setText(
            QCoreApplication.translate("Form", "Disk Center Shift (j)", None)
        )
        self.label_19.setText(
            QCoreApplication.translate("Form", "Elliptical Semi-major Axis", None)
        )
        self.label_20.setText(
            QCoreApplication.translate("Form", "Elliptical Semi-minor Axis", None)
        )
        self.label_21.setText(
            QCoreApplication.translate("Form", "Elliptical Rotation Angle", None)
        )
        self.label_fddnet_center_shift_ci.setText(
            QCoreApplication.translate("Form", "TextLabel", None)
        )
        self.label_fddnet_center_shift_cj.setText(
            QCoreApplication.translate("Form", "TextLabel", None)
        )
        self.label_fddnet_elliptical_a.setText(
            QCoreApplication.translate("Form", "TextLabel", None)
        )
        self.label_fddnet_elliptical_b.setText(
            QCoreApplication.translate("Form", "TextLabel", None)
        )
        self.label_fddnet_elliptical_angle.setText(
            QCoreApplication.translate("Form", "TextLabel", None)
        )
        self.checkBox_show_shifted_dp.setText(
            QCoreApplication.translate(
                "Form", "Display shifted diffraction image", None
            )
        )
        self.checkBox_show_measured_ellipse.setText(
            QCoreApplication.translate("Form", "Show the measured ellipse", None)
        )
        self.pushButton_adjust_ellipse_effects.setText(
            QCoreApplication.translate("Form", "Adjust Ellipse Effects...", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("Form", "Inference Whole 4D-STEM Dataset", None)
        )
        self.pushButton_generate_shift_vec.setText(
            QCoreApplication.translate("Form", "Generate Shift Mapping", None)
        )

    # retranslateUi
