# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDialogTaskDetail.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QListView, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 411)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_task_name = QLabel(Dialog)
        self.label_task_name.setObjectName(u"label_task_name")

        self.horizontalLayout.addWidget(self.label_task_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_task_state = QLabel(Dialog)
        self.label_task_state.setObjectName(u"label_task_state")

        self.horizontalLayout_2.addWidget(self.label_task_state)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.plainTextEdit_comment = QPlainTextEdit(Dialog)
        self.plainTextEdit_comment.setObjectName(u"plainTextEdit_comment")

        self.verticalLayout.addWidget(self.plainTextEdit_comment)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.listView_subtask = QListView(Dialog)
        self.listView_subtask.setObjectName(u"listView_subtask")

        self.verticalLayout.addWidget(self.listView_subtask)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButton_refresh = QPushButton(Dialog)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.horizontalLayout_3.addWidget(self.pushButton_refresh)

        self.pushButton_OK = QPushButton(Dialog)
        self.pushButton_OK.setObjectName(u"pushButton_OK")

        self.horizontalLayout_3.addWidget(self.pushButton_OK)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.label_task_name.setText(QCoreApplication.translate("Dialog", u"None", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"State:", None))
        self.label_task_state.setText(QCoreApplication.translate("Dialog", u"Submitted", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Comments:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Subtasks", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("Dialog", u"Refresh", None))
        self.pushButton_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

