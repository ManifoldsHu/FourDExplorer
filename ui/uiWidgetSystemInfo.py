# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWidgetSystemInfo.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QProgressBar,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(325, 652)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label_cpu_count = QLabel(Form)
        self.label_cpu_count.setObjectName(u"label_cpu_count")

        self.gridLayout.addWidget(self.label_cpu_count, 0, 2, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.label_cpu_percent = QLabel(Form)
        self.label_cpu_percent.setObjectName(u"label_cpu_percent")

        self.gridLayout.addWidget(self.label_cpu_percent, 1, 2, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.label_app_cpu_percent = QLabel(Form)
        self.label_app_cpu_percent.setObjectName(u"label_app_cpu_percent")

        self.gridLayout.addWidget(self.label_app_cpu_percent, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.progressBar_cpu_percent = QProgressBar(Form)
        self.progressBar_cpu_percent.setObjectName(u"progressBar_cpu_percent")
        self.progressBar_cpu_percent.setValue(24)

        self.verticalLayout.addWidget(self.progressBar_cpu_percent)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.label_memory_total = QLabel(Form)
        self.label_memory_total.setObjectName(u"label_memory_total")

        self.gridLayout_2.addWidget(self.label_memory_total, 0, 2, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 1, 1, 1, 1)

        self.label_memory_available = QLabel(Form)
        self.label_memory_available.setObjectName(u"label_memory_available")

        self.gridLayout_2.addWidget(self.label_memory_available, 1, 2, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 2, 1, 1, 1)

        self.label_app_memory = QLabel(Form)
        self.label_app_memory.setObjectName(u"label_app_memory")

        self.gridLayout_2.addWidget(self.label_app_memory, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.progressBar_memory_percent = QProgressBar(Form)
        self.progressBar_memory_percent.setObjectName(u"progressBar_memory_percent")
        self.progressBar_memory_percent.setValue(24)

        self.verticalLayout.addWidget(self.progressBar_memory_percent)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)

        self.label_disk_total = QLabel(Form)
        self.label_disk_total.setObjectName(u"label_disk_total")

        self.gridLayout_3.addWidget(self.label_disk_total, 0, 2, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_10, 2, 1, 1, 1)

        self.label_app_disk_read = QLabel(Form)
        self.label_app_disk_read.setObjectName(u"label_app_disk_read")

        self.gridLayout_3.addWidget(self.label_app_disk_read, 2, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_9, 1, 1, 1, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_disk_available = QLabel(Form)
        self.label_disk_available.setObjectName(u"label_disk_available")

        self.gridLayout_3.addWidget(self.label_disk_available, 1, 2, 1, 1)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_app_disk_write = QLabel(Form)
        self.label_app_disk_write.setObjectName(u"label_app_disk_write")

        self.gridLayout_3.addWidget(self.label_app_disk_write, 3, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.progressBar_disk_percent = QProgressBar(Form)
        self.progressBar_disk_percent.setObjectName(u"progressBar_disk_percent")
        self.progressBar_disk_percent.setValue(24)

        self.verticalLayout.addWidget(self.progressBar_disk_percent)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"CPU count", None))
        self.label_cpu_count.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"CPU percent", None))
        self.label_cpu_percent.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"4D-Explorer CPU percent", None))
        self.label_app_cpu_percent.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Memory Total", None))
        self.label_memory_total.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Memory Available", None))
        self.label_memory_available.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"4D-Explorer Memory Usage", None))
        self.label_app_memory.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_disk_total.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Disk Available", None))
        self.label_app_disk_read.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"4D-Explorer Disk Read", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Disk Total", None))
        self.label_disk_available.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"4D-Explorer Disk Write", None))
        self.label_app_disk_write.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

