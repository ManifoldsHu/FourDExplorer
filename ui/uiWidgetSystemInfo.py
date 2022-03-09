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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(325, 427)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_8.addWidget(self.label)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_8.addWidget(self.label_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_cpu_count = QLabel(Form)
        self.label_cpu_count.setObjectName(u"label_cpu_count")

        self.verticalLayout_5.addWidget(self.label_cpu_count)

        self.label_cpu_percent = QLabel(Form)
        self.label_cpu_percent.setObjectName(u"label_cpu_percent")

        self.verticalLayout_5.addWidget(self.label_cpu_percent)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.progressBar_cpu_percent = QProgressBar(Form)
        self.progressBar_cpu_percent.setObjectName(u"progressBar_cpu_percent")
        self.progressBar_cpu_percent.setValue(24)

        self.verticalLayout.addWidget(self.progressBar_cpu_percent)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_9.addWidget(self.label_4)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_memory_total = QLabel(Form)
        self.label_memory_total.setObjectName(u"label_memory_total")

        self.verticalLayout_6.addWidget(self.label_memory_total)

        self.label_memory_available = QLabel(Form)
        self.label_memory_available.setObjectName(u"label_memory_available")

        self.verticalLayout_6.addWidget(self.label_memory_available)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.progressBar_memory_percent = QProgressBar(Form)
        self.progressBar_memory_percent.setObjectName(u"progressBar_memory_percent")
        self.progressBar_memory_percent.setValue(24)

        self.verticalLayout.addWidget(self.progressBar_memory_percent)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_10.addWidget(self.label_14)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_10.addWidget(self.label_7)


        self.horizontalLayout_5.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_disk_partition = QLabel(Form)
        self.label_disk_partition.setObjectName(u"label_disk_partition")

        self.verticalLayout_7.addWidget(self.label_disk_partition)

        self.label_disk_total = QLabel(Form)
        self.label_disk_total.setObjectName(u"label_disk_total")

        self.verticalLayout_7.addWidget(self.label_disk_total)

        self.label_disk_available = QLabel(Form)
        self.label_disk_available.setObjectName(u"label_disk_available")

        self.verticalLayout_7.addWidget(self.label_disk_available)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.progressBar_disk_percent = QProgressBar(Form)
        self.progressBar_disk_percent.setObjectName(u"progressBar_disk_percent")
        self.progressBar_disk_percent.setValue(24)

        self.verticalLayout.addWidget(self.progressBar_disk_percent)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_process_io = QLabel(Form)
        self.label_process_io.setObjectName(u"label_process_io")

        self.horizontalLayout_6.addWidget(self.label_process_io)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"CPU count", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"CPU percent", None))
        self.label_cpu_count.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_cpu_percent.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Memory Total", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Memory Available", None))
        self.label_memory_total.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_memory_available.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Disk Partition", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Disk Total", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Disk Available", None))
        self.label_disk_partition.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_disk_total.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_disk_available.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Process IO", None))
        self.label_process_io.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

