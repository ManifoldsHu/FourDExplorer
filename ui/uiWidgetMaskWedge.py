# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiWidgetMaskWedge.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(522, 385)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_wedge_parameter = QtWidgets.QLabel(Form)
        self.label_wedge_parameter.setObjectName("label_wedge_parameter")
        self.verticalLayout.addWidget(self.label_wedge_parameter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_wedge_inner = QtWidgets.QLabel(Form)
        self.label_wedge_inner.setObjectName("label_wedge_inner")
        self.horizontalLayout.addWidget(self.label_wedge_inner)
        self.doubleSpinBox_wedge_inner = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_wedge_inner.setObjectName("doubleSpinBox_wedge_inner")
        self.horizontalLayout.addWidget(self.doubleSpinBox_wedge_inner)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_wedge_outer = QtWidgets.QLabel(Form)
        self.label_wedge_outer.setObjectName("label_wedge_outer")
        self.horizontalLayout_2.addWidget(self.label_wedge_outer)
        self.doubleSpinBox_wedge_outer = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_wedge_outer.setObjectName("doubleSpinBox_wedge_outer")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_wedge_outer)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_wedge_rotate_angle = QtWidgets.QLabel(Form)
        self.label_wedge_rotate_angle.setObjectName("label_wedge_rotate_angle")
        self.horizontalLayout_3.addWidget(self.label_wedge_rotate_angle)
        self.doubleSpinBox_wedge_rotate_angle = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_wedge_rotate_angle.setObjectName("doubleSpinBox_wedge_rotate_angle")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_wedge_rotate_angle)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_wedge_open_angle = QtWidgets.QLabel(Form)
        self.label_wedge_open_angle.setObjectName("label_wedge_open_angle")
        self.horizontalLayout_4.addWidget(self.label_wedge_open_angle)
        self.doubleSpinBox_wedge_open_angle = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_wedge_open_angle.setObjectName("doubleSpinBox_wedge_open_angle")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_wedge_open_angle)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.checkBox_wedge_is_center = QtWidgets.QCheckBox(Form)
        self.checkBox_wedge_is_center.setObjectName("checkBox_wedge_is_center")
        self.verticalLayout.addWidget(self.checkBox_wedge_is_center)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_wedge_center_j = QtWidgets.QLabel(Form)
        self.label_wedge_center_j.setObjectName("label_wedge_center_j")
        self.horizontalLayout_6.addWidget(self.label_wedge_center_j)
        self.doubleSpinBox_wedge_center_j = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_wedge_center_j.setObjectName("doubleSpinBox_wedge_center_j")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_wedge_center_j)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_wedge_center_i = QtWidgets.QLabel(Form)
        self.label_wedge_center_i.setObjectName("label_wedge_center_i")
        self.horizontalLayout_5.addWidget(self.label_wedge_center_i)
        self.doubleSpinBox_wedge_center_i = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_wedge_center_i.setObjectName("doubleSpinBox_wedge_center_i")
        self.horizontalLayout_5.addWidget(self.doubleSpinBox_wedge_center_i)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_wedge_inner.setBuddy(self.doubleSpinBox_wedge_inner)
        self.label_wedge_outer.setBuddy(self.doubleSpinBox_wedge_outer)
        self.label_wedge_rotate_angle.setBuddy(self.doubleSpinBox_wedge_rotate_angle)
        self.label_wedge_open_angle.setBuddy(self.doubleSpinBox_wedge_open_angle)
        self.label_wedge_center_j.setBuddy(self.doubleSpinBox_wedge_center_j)
        self.label_wedge_center_i.setBuddy(self.doubleSpinBox_wedge_center_i)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_wedge_parameter.setText(_translate("Form", "Wedge parameters"))
        self.label_wedge_inner.setText(_translate("Form", "inner radius (pix)(&I)"))
        self.label_wedge_outer.setText(_translate("Form", "outer radius (pix)(&O)"))
        self.label_wedge_rotate_angle.setText(_translate("Form", "rotation angle (deg)(&R)"))
        self.label_wedge_open_angle.setText(_translate("Form", "open angle (deg)(&A)"))
        self.checkBox_wedge_is_center.setText(_translate("Form", "centered"))
        self.label_wedge_center_j.setText(_translate("Form", "horizontal shift(&J)"))
        self.label_wedge_center_i.setText(_translate("Form", "vertical shift(&I)"))

