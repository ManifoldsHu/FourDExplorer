# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogHDFCreateItem.ui'
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
    QComboBox,
    QDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(492, 296)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_info = QLabel(Dialog)
        self.label_info.setObjectName("label_info")

        self.verticalLayout_4.addWidget(self.label_info)

        self.verticalSpacer_2 = QSpacerItem(
            20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.widget_set_path = QWidget(Dialog)
        self.widget_set_path.setObjectName("widget_set_path")
        self.verticalLayout_3 = QVBoxLayout(self.widget_set_path)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_location = QLabel(self.widget_set_path)
        self.label_location.setObjectName("label_location")

        self.horizontalLayout_4.addWidget(self.label_location)

        self.lineEdit_parent_path = QLineEdit(self.widget_set_path)
        self.lineEdit_parent_path.setObjectName("lineEdit_parent_path")

        self.horizontalLayout_4.addWidget(self.lineEdit_parent_path)

        self.pushButton_browse = QPushButton(self.widget_set_path)
        self.pushButton_browse.setObjectName("pushButton_browse")

        self.horizontalLayout_4.addWidget(self.pushButton_browse)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_name = QLabel(self.widget_set_path)
        self.label_name.setObjectName("label_name")

        self.horizontalLayout_2.addWidget(self.label_name)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lineEdit_name = QLineEdit(self.widget_set_path)
        self.lineEdit_name.setObjectName("lineEdit_name")

        self.horizontalLayout_2.addWidget(self.lineEdit_name)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_type = QLabel(self.widget_set_path)
        self.label_type.setObjectName("label_type")

        self.horizontalLayout_3.addWidget(self.label_type)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.comboBox_type = QComboBox(self.widget_set_path)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName("comboBox_type")

        self.horizontalLayout_3.addWidget(self.comboBox_type)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_4.addWidget(self.widget_set_path)

        self.verticalSpacer_3 = QSpacerItem(
            20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_group = QWidget()
        self.page_group.setObjectName("page_group")
        self.verticalLayout_2 = QVBoxLayout(self.page_group)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalSpacer = QSpacerItem(
            20, 103, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_group)
        self.page_data = QWidget()
        self.page_data.setObjectName("page_data")
        self.horizontalLayout = QHBoxLayout(self.page_data)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_dimensions = QLabel(self.page_data)
        self.label_dimensions.setObjectName("label_dimensions")

        self.verticalLayout.addWidget(self.label_dimensions)

        self.label_shape = QLabel(self.page_data)
        self.label_shape.setObjectName("label_shape")

        self.verticalLayout.addWidget(self.label_shape)

        self.label_data_type = QLabel(self.page_data)
        self.label_data_type.setObjectName("label_data_type")

        self.verticalLayout.addWidget(self.label_data_type)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_dim_2 = QSpinBox(self.page_data)
        self.spinBox_dim_2.setObjectName("spinBox_dim_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.spinBox_dim_2.sizePolicy().hasHeightForWidth()
        )
        self.spinBox_dim_2.setSizePolicy(sizePolicy)
        self.spinBox_dim_2.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.spinBox_dim_2, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(
            28, 20, QSizePolicy.Preferred, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 1, 1, 1)

        self.comboBox_dtype = QComboBox(self.page_data)
        self.comboBox_dtype.addItem("")
        self.comboBox_dtype.setObjectName("comboBox_dtype")

        self.gridLayout.addWidget(self.comboBox_dtype, 2, 2, 1, 2)

        self.spinBox_dim_3 = QSpinBox(self.page_data)
        self.spinBox_dim_3.setObjectName("spinBox_dim_3")
        sizePolicy.setHeightForWidth(
            self.spinBox_dim_3.sizePolicy().hasHeightForWidth()
        )
        self.spinBox_dim_3.setSizePolicy(sizePolicy)
        self.spinBox_dim_3.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.spinBox_dim_3, 1, 1, 1, 1)

        self.comboBox_dimensions = QComboBox(self.page_data)
        self.comboBox_dimensions.addItem("")
        self.comboBox_dimensions.addItem("")
        self.comboBox_dimensions.addItem("")
        self.comboBox_dimensions.addItem("")
        self.comboBox_dimensions.addItem("")
        self.comboBox_dimensions.setObjectName("comboBox_dimensions")

        self.gridLayout.addWidget(self.comboBox_dimensions, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)

        self.spinBox_dim_4 = QSpinBox(self.page_data)
        self.spinBox_dim_4.setObjectName("spinBox_dim_4")
        sizePolicy.setHeightForWidth(
            self.spinBox_dim_4.sizePolicy().hasHeightForWidth()
        )
        self.spinBox_dim_4.setSizePolicy(sizePolicy)
        self.spinBox_dim_4.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.spinBox_dim_4, 1, 0, 1, 1)

        self.spinBox_dim_1 = QSpinBox(self.page_data)
        self.spinBox_dim_1.setObjectName("spinBox_dim_1")
        sizePolicy.setHeightForWidth(
            self.spinBox_dim_1.sizePolicy().hasHeightForWidth()
        )
        self.spinBox_dim_1.setSizePolicy(sizePolicy)
        self.spinBox_dim_1.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.spinBox_dim_1, 1, 3, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_10, 2, 0, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.page_data)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.verticalSpacer_4 = QSpacerItem(
            20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName("pushButton_ok")

        self.horizontalLayout_6.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog)
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.horizontalLayout_6.addWidget(self.pushButton_cancel)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.label_info.setText(
            QCoreApplication.translate("Dialog", "Create a new item", None)
        )
        self.label_location.setText(
            QCoreApplication.translate("Dialog", "Location: ", None)
        )
        self.pushButton_browse.setText(
            QCoreApplication.translate("Dialog", "Browse...", None)
        )
        self.label_name.setText(QCoreApplication.translate("Dialog", "Name:", None))
        self.label_type.setText(QCoreApplication.translate("Dialog", "Type:", None))
        self.comboBox_type.setItemText(
            0, QCoreApplication.translate("Dialog", "Group", None)
        )
        self.comboBox_type.setItemText(
            1, QCoreApplication.translate("Dialog", "General Data", None)
        )

        self.label_dimensions.setText(
            QCoreApplication.translate("Dialog", "Dimensions", None)
        )
        self.label_shape.setText(QCoreApplication.translate("Dialog", "Shape", None))
        self.label_data_type.setText(
            QCoreApplication.translate("Dialog", "data type", None)
        )
        self.comboBox_dtype.setItemText(
            0, QCoreApplication.translate("Dialog", "32bit float", None)
        )

        self.comboBox_dimensions.setItemText(
            0, QCoreApplication.translate("Dialog", "0", None)
        )
        self.comboBox_dimensions.setItemText(
            1, QCoreApplication.translate("Dialog", "1", None)
        )
        self.comboBox_dimensions.setItemText(
            2, QCoreApplication.translate("Dialog", "2", None)
        )
        self.comboBox_dimensions.setItemText(
            3, QCoreApplication.translate("Dialog", "3", None)
        )
        self.comboBox_dimensions.setItemText(
            4, QCoreApplication.translate("Dialog", "4", None)
        )

        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", "OK", None))
        self.pushButton_cancel.setText(
            QCoreApplication.translate("Dialog", "Cancel", None)
        )

    # retranslateUi
