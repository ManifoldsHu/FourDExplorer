# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetTaskManager.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListView,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(327, 532)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_current_task_name = QLabel(Form)
        self.label_current_task_name.setObjectName(u"label_current_task_name")

        self.horizontalLayout.addWidget(self.label_current_task_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar_task = QProgressBar(Form)
        self.progressBar_task.setObjectName(u"progressBar_task")
        self.progressBar_task.setValue(24)

        self.verticalLayout.addWidget(self.progressBar_task)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_detail = QPushButton(Form)
        self.pushButton_detail.setObjectName(u"pushButton_detail")

        self.horizontalLayout_2.addWidget(self.pushButton_detail)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.listView_waiting_queue = QListView(Form)
        self.listView_waiting_queue.setObjectName(u"listView_waiting_queue")

        self.verticalLayout.addWidget(self.listView_waiting_queue)

        self.pushButton_history = QPushButton(Form)
        self.pushButton_history.setObjectName(u"pushButton_history")

        self.verticalLayout.addWidget(self.pushButton_history)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Executing Task:", None))
        self.label_current_task_name.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_detail.setText(QCoreApplication.translate("Form", u"Details", None))
        self.pushButton_history.setText(QCoreApplication.translate("Form", u"History Task", None))
    # retranslateUi

