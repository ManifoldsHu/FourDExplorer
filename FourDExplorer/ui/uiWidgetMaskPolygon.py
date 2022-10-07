# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetMaskPolygon.ui'
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
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(488, 386)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.doubleSpinBox_polygon_radius = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_polygon_radius.setObjectName(u"doubleSpinBox_polygon_radius")

        self.horizontalLayout.addWidget(self.doubleSpinBox_polygon_radius)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.spinBox_vertices_number = QSpinBox(self.groupBox)
        self.spinBox_vertices_number.setObjectName(u"spinBox_vertices_number")

        self.horizontalLayout_2.addWidget(self.spinBox_vertices_number)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_wedge_center_j = QLabel(self.groupBox_2)
        self.label_wedge_center_j.setObjectName(u"label_wedge_center_j")

        self.horizontalLayout_6.addWidget(self.label_wedge_center_j)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.doubleSpinBox_polygon_center_j = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_polygon_center_j.setObjectName(u"doubleSpinBox_polygon_center_j")

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_polygon_center_j)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_wedge_center_i = QLabel(self.groupBox_2)
        self.label_wedge_center_i.setObjectName(u"label_wedge_center_i")

        self.horizontalLayout_5.addWidget(self.label_wedge_center_i)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.doubleSpinBox_polygon_center_i = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_polygon_center_i.setObjectName(u"doubleSpinBox_polygon_center_i")

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_polygon_center_i)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_wedge_rotate_angle = QLabel(self.groupBox_2)
        self.label_wedge_rotate_angle.setObjectName(u"label_wedge_rotate_angle")

        self.horizontalLayout_3.addWidget(self.label_wedge_rotate_angle)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.doubleSpinBox_polygon_rotate_angle = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_polygon_rotate_angle.setObjectName(u"doubleSpinBox_polygon_rotate_angle")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_polygon_rotate_angle)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.pushButton_adjust_effects = QPushButton(Form)
        self.pushButton_adjust_effects.setObjectName(u"pushButton_adjust_effects")

        self.verticalLayout_3.addWidget(self.pushButton_adjust_effects)

        self.verticalSpacer = QSpacerItem(20, 98, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

#if QT_CONFIG(shortcut)
        self.label_wedge_center_j.setBuddy(self.doubleSpinBox_polygon_center_j)
        self.label_wedge_center_i.setBuddy(self.doubleSpinBox_polygon_center_i)
        self.label_wedge_rotate_angle.setBuddy(self.doubleSpinBox_polygon_rotate_angle)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Regular Polygon parameters", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Shape", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Radius", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Number of Vertices", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Location", None))
        self.label_wedge_center_j.setText(QCoreApplication.translate("Form", u"Horizontal Shift(&J)", None))
        self.label_wedge_center_i.setText(QCoreApplication.translate("Form", u"Vertical Shift(&I)", None))
        self.label_wedge_rotate_angle.setText(QCoreApplication.translate("Form", u"Rotation Angle (deg)(&R)", None))
        self.pushButton_adjust_effects.setText(QCoreApplication.translate("Form", u"Adjust Effects...", None))
    # retranslateUi

