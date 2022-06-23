# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageViewVectorField.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSplitter,
    QVBoxLayout, QWidget)

from bin.Widgets.WidgetPlots import (WidgetPlotBackground, WidgetPlotQuiver)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(863, 591)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_vector_path = QLineEdit(self.widget)
        self.lineEdit_vector_path.setObjectName(u"lineEdit_vector_path")

        self.horizontalLayout.addWidget(self.lineEdit_vector_path)

        self.pushButton_browse = QPushButton(self.widget)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.widget_quiver = WidgetPlotQuiver(self.widget)
        self.widget_quiver.setObjectName(u"widget_quiver")

        self.verticalLayout_3.addWidget(self.widget_quiver)

        self.verticalLayout_3.setStretch(1, 1)
        self.splitter.addWidget(self.widget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_background_path = QLineEdit(self.layoutWidget)
        self.lineEdit_background_path.setObjectName(u"lineEdit_background_path")

        self.horizontalLayout_3.addWidget(self.lineEdit_background_path)

        self.pushButton_browse_background = QPushButton(self.layoutWidget)
        self.pushButton_browse_background.setObjectName(u"pushButton_browse_background")

        self.horizontalLayout_3.addWidget(self.pushButton_browse_background)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.widget_background = WidgetPlotBackground(self.layoutWidget)
        self.widget_background.setObjectName(u"widget_background")

        self.verticalLayout_2.addWidget(self.widget_background)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_background_visible = QCheckBox(self.layoutWidget)
        self.checkBox_background_visible.setObjectName(u"checkBox_background_visible")

        self.verticalLayout.addWidget(self.checkBox_background_visible)

        self.pushButton_adjust_effects = QPushButton(self.layoutWidget)
        self.pushButton_adjust_effects.setObjectName(u"pushButton_adjust_effects")

        self.verticalLayout.addWidget(self.pushButton_adjust_effects)

        self.pushButton_show_stream_line = QPushButton(self.layoutWidget)
        self.pushButton_show_stream_line.setObjectName(u"pushButton_show_stream_line")

        self.verticalLayout.addWidget(self.pushButton_show_stream_line)

        self.pushButton_show_color_wheel = QPushButton(self.layoutWidget)
        self.pushButton_show_color_wheel.setObjectName(u"pushButton_show_color_wheel")

        self.verticalLayout.addWidget(self.pushButton_show_color_wheel)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2.setStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget)

        self.verticalLayout_4.addWidget(self.splitter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Vector Field Path", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Background Path", None))
        self.pushButton_browse_background.setText(QCoreApplication.translate("Form", u"Browse Background", None))
        self.checkBox_background_visible.setText(QCoreApplication.translate("Form", u"Background Image Visible", None))
        self.pushButton_adjust_effects.setText(QCoreApplication.translate("Form", u"Adjust Quiver Effects...", None))
        self.pushButton_show_stream_line.setText(QCoreApplication.translate("Form", u"Show Stream Line Image...", None))
        self.pushButton_show_color_wheel.setText(QCoreApplication.translate("Form", u"Show Color Wheel Image...", None))
    # retranslateUi

