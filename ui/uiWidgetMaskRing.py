# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiWidgetMaskRing.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(405, 295)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_ring_parameter = QtWidgets.QLabel(Form)
        self.label_ring_parameter.setObjectName("label_ring_parameter")
        self.verticalLayout.addWidget(self.label_ring_parameter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_ring_inner = QtWidgets.QLabel(Form)
        self.label_ring_inner.setObjectName("label_ring_inner")
        self.horizontalLayout.addWidget(self.label_ring_inner)
        self.doubleSpinBox_ring_inner = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_ring_inner.setObjectName("doubleSpinBox_ring_inner")
        self.horizontalLayout.addWidget(self.doubleSpinBox_ring_inner)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_ring_outer = QtWidgets.QLabel(Form)
        self.label_ring_outer.setObjectName("label_ring_outer")
        self.horizontalLayout_2.addWidget(self.label_ring_outer)
        self.doubleSpinBox_ring_outer = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_ring_outer.setObjectName("doubleSpinBox_ring_outer")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_ring_outer)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.checkBox_ring_is_center = QtWidgets.QCheckBox(Form)
        self.checkBox_ring_is_center.setObjectName("checkBox_ring_is_center")
        self.verticalLayout.addWidget(self.checkBox_ring_is_center)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_ring_center_j = QtWidgets.QLabel(Form)
        self.label_ring_center_j.setObjectName("label_ring_center_j")
        self.horizontalLayout_4.addWidget(self.label_ring_center_j)
        self.doubleSpinBox_ring_center_j = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_ring_center_j.setObjectName("doubleSpinBox_ring_center_j")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_ring_center_j)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_ring_center_i = QtWidgets.QLabel(Form)
        self.label_ring_center_i.setObjectName("label_ring_center_i")
        self.horizontalLayout_3.addWidget(self.label_ring_center_i)
        self.doubleSpinBox_ring_center_i = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_ring_center_i.setObjectName("doubleSpinBox_ring_center_i")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_ring_center_i)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_ring_inner.setBuddy(self.doubleSpinBox_ring_inner)
        self.label_ring_outer.setBuddy(self.doubleSpinBox_ring_outer)
        self.label_ring_center_j.setBuddy(self.doubleSpinBox_ring_center_j)
        self.label_ring_center_i.setBuddy(self.doubleSpinBox_ring_center_i)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_ring_parameter.setText(_translate("Form", "Ring parameters"))
        self.label_ring_inner.setText(_translate("Form", "inner radius (pix)(&I)"))
        self.label_ring_outer.setText(_translate("Form", "outer radius (pix)(&O)"))
        self.checkBox_ring_is_center.setText(_translate("Form", "centered"))
        self.label_ring_center_j.setText(_translate("Form", "horizontal shift(&J)"))
        self.label_ring_center_i.setText(_translate("Form", "vertical shift(&I)"))

