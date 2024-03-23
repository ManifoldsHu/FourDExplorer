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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

from bin.Widgets.WidgetMetaViewerBase import WidgetMetaViewerBase
from bin.Widgets.WidgetMetaViewerBaseNotPathlike import WidgetMetaViewerBaseNotPathlike

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(463, 739)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_meta_viewer = WidgetMetaViewerBase(self.tab)
        self.widget_meta_viewer.setObjectName(u"widget_meta_viewer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_meta_viewer.sizePolicy().hasHeightForWidth())
        self.widget_meta_viewer.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.widget_meta_viewer)

        self.tabWidget.addTab(self.tab, "")
        self.tab_not_pathlike = QWidget()
        self.tab_not_pathlike.setObjectName(u"tab_not_pathlike")
        self.verticalLayout_2 = QVBoxLayout(self.tab_not_pathlike)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_meta_viewer_not_pathlike = WidgetMetaViewerBaseNotPathlike(self.tab_not_pathlike)
        self.widget_meta_viewer_not_pathlike.setObjectName(u"widget_meta_viewer_not_pathlike")
        sizePolicy.setHeightForWidth(self.widget_meta_viewer_not_pathlike.sizePolicy().hasHeightForWidth())
        self.widget_meta_viewer_not_pathlike.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.widget_meta_viewer_not_pathlike)

        self.tabWidget.addTab(self.tab_not_pathlike, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Predefined Metadata", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_not_pathlike), QCoreApplication.translate("Form", u"Other Metadata", None))
    # retranslateUi

