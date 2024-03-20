# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetMetaViewer.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QSplitter,
    QVBoxLayout, QWidget)

from bin.Widgets.WidgetMetaViewerBase import WidgetMetaViewerBase
from bin.Widgets.WidgetMetaViewerBaseNotPathlike import WidgetMetaViewerBaseNotPathlike

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(463, 739)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.widget_meta_viewer = WidgetMetaViewerBase(self.widget)
        self.widget_meta_viewer.setObjectName(u"widget_meta_viewer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_meta_viewer.sizePolicy().hasHeightForWidth())
        self.widget_meta_viewer.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.widget_meta_viewer)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.widget_meta_viewer_not_pathlike = WidgetMetaViewerBaseNotPathlike(self.widget1)
        self.widget_meta_viewer_not_pathlike.setObjectName(u"widget_meta_viewer_not_pathlike")
        sizePolicy.setHeightForWidth(self.widget_meta_viewer_not_pathlike.sizePolicy().hasHeightForWidth())
        self.widget_meta_viewer_not_pathlike.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.widget_meta_viewer_not_pathlike)

        self.splitter.addWidget(self.widget1)

        self.verticalLayout_3.addWidget(self.splitter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Predefined Metadata:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Other Metadata:", None))
    # retranslateUi

