# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetMaskRectangle.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_rectangle_parameter = QLabel(Form)
        self.label_rectangle_parameter.setObjectName(u"label_rectangle_parameter")

        self.verticalLayout_3.addWidget(self.label_rectangle_parameter)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_rectangle_width = QLabel(self.groupBox)
        self.label_rectangle_width.setObjectName(u"label_rectangle_width")

        self.horizontalLayout_4.addWidget(self.label_rectangle_width)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.doubleSpinBox_rectangle_width = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_rectangle_width.setObjectName(u"doubleSpinBox_rectangle_width")

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_rectangle_width)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_rectangle_height = QLabel(self.groupBox)
        self.label_rectangle_height.setObjectName(u"label_rectangle_height")

        self.horizontalLayout_5.addWidget(self.label_rectangle_height)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox_rectangle_height = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_rectangle_height.setObjectName(u"doubleSpinBox_rectangle_height")

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_rectangle_height)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_rectangle_rotation_angle = QLabel(self.groupBox_2)
        self.label_rectangle_rotation_angle.setObjectName(u"label_rectangle_rotation_angle")

        self.horizontalLayout_21.addWidget(self.label_rectangle_rotation_angle)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_3)

        self.doubleSpinBox_rectangle_rotation_angle = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_rectangle_rotation_angle.setObjectName(u"doubleSpinBox_rectangle_rotation_angle")

        self.horizontalLayout_21.addWidget(self.doubleSpinBox_rectangle_rotation_angle)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_rectangle_center_j = QLabel(self.groupBox_2)
        self.label_rectangle_center_j.setObjectName(u"label_rectangle_center_j")

        self.horizontalLayout_6.addWidget(self.label_rectangle_center_j)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.doubleSpinBox_rectangle_center_j = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_rectangle_center_j.setObjectName(u"doubleSpinBox_rectangle_center_j")

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_rectangle_center_j)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_rectangle_center_i = QLabel(self.groupBox_2)
        self.label_rectangle_center_i.setObjectName(u"label_rectangle_center_i")

        self.horizontalLayout_7.addWidget(self.label_rectangle_center_i)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.doubleSpinBox_rectangle_center_i = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_rectangle_center_i.setObjectName(u"doubleSpinBox_rectangle_center_i")

        self.horizontalLayout_7.addWidget(self.doubleSpinBox_rectangle_center_i)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.pushButton_adjust_effects = QPushButton(Form)
        self.pushButton_adjust_effects.setObjectName(u"pushButton_adjust_effects")

        self.verticalLayout_3.addWidget(self.pushButton_adjust_effects)

        self.verticalSpacer_2 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

#if QT_CONFIG(shortcut)
        self.label_rectangle_width.setBuddy(self.doubleSpinBox_rectangle_width)
        self.label_rectangle_height.setBuddy(self.doubleSpinBox_rectangle_height)
        self.label_rectangle_rotation_angle.setBuddy(self.doubleSpinBox_rectangle_rotation_angle)
        self.label_rectangle_center_j.setBuddy(self.doubleSpinBox_rectangle_center_j)
        self.label_rectangle_center_i.setBuddy(self.doubleSpinBox_rectangle_center_i)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_rectangle_parameter.setText(QCoreApplication.translate("Form", u"Rectangle parameters", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Shape", None))
        self.label_rectangle_width.setText(QCoreApplication.translate("Form", u"Width(&W)", None))
        self.label_rectangle_height.setText(QCoreApplication.translate("Form", u"Height(&H)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Location", None))
        self.label_rectangle_rotation_angle.setText(QCoreApplication.translate("Form", u"rotation angle(&R)", None))
        self.label_rectangle_center_j.setText(QCoreApplication.translate("Form", u"horizontal shift(&J)", None))
        self.label_rectangle_center_i.setText(QCoreApplication.translate("Form", u"vertical shift(&I)", None))
        self.pushButton_adjust_effects.setText(QCoreApplication.translate("Form", u"Adjust Effects...", None))
    # retranslateUi

