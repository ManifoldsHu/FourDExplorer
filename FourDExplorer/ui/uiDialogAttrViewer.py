# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogAttrViewer.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableView, QTreeView, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(381, 643)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_item_path = QLineEdit(Dialog)
        self.lineEdit_item_path.setObjectName(u"lineEdit_item_path")

        self.horizontalLayout.addWidget(self.lineEdit_item_path)

        self.pushButton_browse = QPushButton(Dialog)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Legacy = QWidget()
        self.Legacy.setObjectName(u"Legacy")
        self.verticalLayout = QVBoxLayout(self.Legacy)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView_attr = QTableView(self.Legacy)
        self.tableView_attr.setObjectName(u"tableView_attr")

        self.verticalLayout.addWidget(self.tableView_attr)

        self.tabWidget.addTab(self.Legacy, "")
        self.Current = QWidget()
        self.Current.setObjectName(u"Current")
        self.verticalLayout_2 = QVBoxLayout(self.Current)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeView = QTreeView(self.Current)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_2.addWidget(self.treeView)

        self.tabWidget.addTab(self.Current, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_search = QLineEdit(Dialog)
        self.lineEdit_search.setObjectName(u"lineEdit_search")

        self.horizontalLayout_2.addWidget(self.lineEdit_search)

        self.pushButton_search_next = QPushButton(Dialog)
        self.pushButton_search_next.setObjectName(u"pushButton_search_next")

        self.horizontalLayout_2.addWidget(self.pushButton_search_next)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Item's Path", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Dialog", u"Browse...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Legacy), QCoreApplication.translate("Dialog", u"Legacy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Current), QCoreApplication.translate("Dialog", u"Current", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Search Attribution", None))
        self.pushButton_search_next.setText(QCoreApplication.translate("Dialog", u"Search Next", None))
    # retranslateUi

