# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetLog.ui'
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
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(400, 213)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_clear_log = QPushButton(Form)
        self.pushButton_clear_log.setObjectName("pushButton_clear_log")
        self.pushButton_clear_log.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_clear_log)

        self.pushButton_open_log_directory = QPushButton(Form)
        self.pushButton_open_log_directory.setObjectName(
            "pushButton_open_log_directory"
        )
        self.pushButton_open_log_directory.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_open_log_directory)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textBrowser_log = QTextBrowser(Form)
        self.textBrowser_log.setObjectName("textBrowser_log")

        self.verticalLayout.addWidget(self.textBrowser_log)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText(
            QCoreApplication.translate("Form", "Messages and Logs", None)
        )
        self.pushButton_clear_log.setText(
            QCoreApplication.translate("Form", "Clear", None)
        )
        self.pushButton_open_log_directory.setText(
            QCoreApplication.translate("Form", "Open Log Folder", None)
        )

    # retranslateUi
