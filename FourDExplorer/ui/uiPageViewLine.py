# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageViewLine.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListView, QPushButton, QSizePolicy, QSplitter,
    QVBoxLayout, QWidget)

from bin.Widgets.WidgetPlots import WidgetPlotLine

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(799, 414)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_line_path = QLineEdit(self.widget)
        self.lineEdit_line_path.setObjectName(u"lineEdit_line_path")

        self.horizontalLayout.addWidget(self.lineEdit_line_path)

        self.pushButton_browse = QPushButton(self.widget)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.widget_plot_line = WidgetPlotLine(self.widget)
        self.widget_plot_line.setObjectName(u"widget_plot_line")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_plot_line.sizePolicy().hasHeightForWidth())
        self.widget_plot_line.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.widget_plot_line)

        self.splitter.addWidget(self.widget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listView_lines = QListView(self.layoutWidget)
        self.listView_lines.setObjectName(u"listView_lines")

        self.verticalLayout.addWidget(self.listView_lines)

        self.pushButton_add_line = QPushButton(self.layoutWidget)
        self.pushButton_add_line.setObjectName(u"pushButton_add_line")

        self.verticalLayout.addWidget(self.pushButton_add_line)

        self.splitter.addWidget(self.layoutWidget)

        self.verticalLayout_3.addWidget(self.splitter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Line Path", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.pushButton_add_line.setText(QCoreApplication.translate("Form", u"Add Line", None))
    # retranslateUi

