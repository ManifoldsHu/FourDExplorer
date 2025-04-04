# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogAttrViewer.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
    QDialog,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QTabWidget,
    QTableView,
    QTreeView,
    QVBoxLayout,
    QWidget,
)

from bin.Widgets.WidgetMetaViewer import WidgetMetaViewer


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(381, 643)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_item_path = QLineEdit(Dialog)
        self.lineEdit_item_path.setObjectName("lineEdit_item_path")

        self.horizontalLayout.addWidget(self.lineEdit_item_path)

        self.pushButton_browse = QPushButton(Dialog)
        self.pushButton_browse.setObjectName("pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.Legacy = QWidget()
        self.Legacy.setObjectName("Legacy")
        self.verticalLayout = QVBoxLayout(self.Legacy)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView_attr = QTableView(self.Legacy)
        self.tableView_attr.setObjectName("tableView_attr")

        self.verticalLayout.addWidget(self.tableView_attr)

        self.tabWidget.addTab(self.Legacy, "")
        self.Current = QWidget()
        self.Current.setObjectName("Current")
        self.verticalLayout_2 = QVBoxLayout(self.Current)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeView = QTreeView(self.Current)
        self.treeView.setObjectName("treeView")

        self.verticalLayout_2.addWidget(self.treeView)

        self.tabWidget.addTab(self.Current, "")
        self.New = QWidget()
        self.New.setObjectName("New")
        self.verticalLayout_4 = QVBoxLayout(self.New)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = WidgetMetaViewer(self.New)
        self.widget.setObjectName("widget")

        self.verticalLayout_4.addWidget(self.widget)

        self.tabWidget.addTab(self.New, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_search = QLineEdit(Dialog)
        self.lineEdit_search.setObjectName("lineEdit_search")

        self.horizontalLayout_2.addWidget(self.lineEdit_search)

        self.pushButton_search_next = QPushButton(Dialog)
        self.pushButton_search_next.setObjectName("pushButton_search_next")

        self.horizontalLayout_2.addWidget(self.pushButton_search_next)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", "Item's Path", None))
        self.pushButton_browse.setText(
            QCoreApplication.translate("Dialog", "Browse...", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Legacy),
            QCoreApplication.translate("Dialog", "Legacy", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Current),
            QCoreApplication.translate("Dialog", "Current", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.New),
            QCoreApplication.translate("Dialog", "New", None),
        )
        self.label_2.setText(
            QCoreApplication.translate("Dialog", "Search Attribution", None)
        )
        self.pushButton_search_next.setText(
            QCoreApplication.translate("Dialog", "Search Next", None)
        )

    # retranslateUi
