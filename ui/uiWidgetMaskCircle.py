# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiWidgetMaskCircle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(417, 292)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_circle_parameter = QtWidgets.QLabel(Form)
        self.label_circle_parameter.setObjectName("label_circle_parameter")
        self.verticalLayout.addWidget(self.label_circle_parameter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_circle_radius = QtWidgets.QLabel(Form)
        self.label_circle_radius.setObjectName("label_circle_radius")
        self.horizontalLayout_3.addWidget(self.label_circle_radius)
        self.doubleSpinBox_circle_radius = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_circle_radius.setObjectName("doubleSpinBox_circle_radius")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_circle_radius)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.checkBox_circle_is_center = QtWidgets.QCheckBox(Form)
        self.checkBox_circle_is_center.setObjectName("checkBox_circle_is_center")
        self.verticalLayout.addWidget(self.checkBox_circle_is_center)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_circle_center_j = QtWidgets.QLabel(Form)
        self.label_circle_center_j.setObjectName("label_circle_center_j")
        self.horizontalLayout.addWidget(self.label_circle_center_j)
        self.doubleSpinBox_circle_center_j = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_circle_center_j.setObjectName("doubleSpinBox_circle_center_j")
        self.horizontalLayout.addWidget(self.doubleSpinBox_circle_center_j)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_circle_center_i = QtWidgets.QLabel(Form)
        self.label_circle_center_i.setObjectName("label_circle_center_i")
        self.horizontalLayout_2.addWidget(self.label_circle_center_i)
        self.doubleSpinBox_circle_center_i = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_circle_center_i.setObjectName("doubleSpinBox_circle_center_i")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_circle_center_i)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_circle_radius.setBuddy(self.doubleSpinBox_circle_radius)
        self.label_circle_center_j.setBuddy(self.doubleSpinBox_circle_center_j)
        self.label_circle_center_i.setBuddy(self.doubleSpinBox_circle_center_i)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_circle_parameter.setText(_translate("Form", "Circle parameters"))
        self.label_circle_radius.setText(_translate("Form", "inner radius (pix)(&R)"))
        self.checkBox_circle_is_center.setText(_translate("Form", "centered"))
        self.label_circle_center_j.setText(_translate("Form", "horizontal shift(&J)"))
        self.label_circle_center_i.setText(_translate("Form", "vertical shift(&I)"))

