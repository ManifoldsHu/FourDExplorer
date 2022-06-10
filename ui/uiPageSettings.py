# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPageSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(611, 425)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tab_theme = QWidget()
        self.tab_theme.setObjectName(u"tab_theme")
        self.verticalLayout_9 = QVBoxLayout(self.tab_theme)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_3 = QGroupBox(self.tab_theme)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_7.addWidget(self.label_2)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_7.addWidget(self.label_8)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.comboBox_theme_mode = QComboBox(self.groupBox_3)
        self.comboBox_theme_mode.addItem("")
        self.comboBox_theme_mode.addItem("")
        self.comboBox_theme_mode.addItem("")
        self.comboBox_theme_mode.addItem("")
        self.comboBox_theme_mode.setObjectName(u"comboBox_theme_mode")

        self.verticalLayout_6.addWidget(self.comboBox_theme_mode)

        self.comboBox_theme_color = QComboBox(self.groupBox_3)
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.addItem("")
        self.comboBox_theme_color.setObjectName(u"comboBox_theme_color")

        self.verticalLayout_6.addWidget(self.comboBox_theme_color)

        self.comboBox_theme_density = QComboBox(self.groupBox_3)
        self.comboBox_theme_density.addItem("")
        self.comboBox_theme_density.addItem("")
        self.comboBox_theme_density.addItem("")
        self.comboBox_theme_density.addItem("")
        self.comboBox_theme_density.addItem("")
        self.comboBox_theme_density.addItem("")
        self.comboBox_theme_density.setObjectName(u"comboBox_theme_density")

        self.verticalLayout_6.addWidget(self.comboBox_theme_density)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 263, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_theme, "")
        self.tab_log = QWidget()
        self.tab_log.setObjectName(u"tab_log")
        self.verticalLayout_5 = QVBoxLayout(self.tab_log)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.tab_log)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.comboBox_level_window = QComboBox(self.groupBox)
        self.comboBox_level_window.addItem("")
        self.comboBox_level_window.addItem("")
        self.comboBox_level_window.addItem("")
        self.comboBox_level_window.addItem("")
        self.comboBox_level_window.addItem("")
        self.comboBox_level_window.addItem("")
        self.comboBox_level_window.setObjectName(u"comboBox_level_window")

        self.horizontalLayout_2.addWidget(self.comboBox_level_window)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.comboBox_level_file = QComboBox(self.groupBox)
        self.comboBox_level_file.addItem("")
        self.comboBox_level_file.addItem("")
        self.comboBox_level_file.addItem("")
        self.comboBox_level_file.addItem("")
        self.comboBox_level_file.addItem("")
        self.comboBox_level_file.addItem("")
        self.comboBox_level_file.setObjectName(u"comboBox_level_file")

        self.horizontalLayout.addWidget(self.comboBox_level_file)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab_log)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_log_file_folder = QLineEdit(self.groupBox_2)
        self.lineEdit_log_file_folder.setObjectName(u"lineEdit_log_file_folder")

        self.horizontalLayout_4.addWidget(self.lineEdit_log_file_folder)

        self.pushButton_browse = QPushButton(self.groupBox_2)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout_4.addWidget(self.pushButton_browse)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_use_default_path = QPushButton(self.groupBox_2)
        self.pushButton_use_default_path.setObjectName(u"pushButton_use_default_path")

        self.verticalLayout_3.addWidget(self.pushButton_use_default_path)

        self.pushButton_open_log_folder = QPushButton(self.groupBox_2)
        self.pushButton_open_log_folder.setObjectName(u"pushButton_open_log_folder")

        self.verticalLayout_3.addWidget(self.pushButton_open_log_folder)

        self.pushButton_clear_log_file = QPushButton(self.groupBox_2)
        self.pushButton_clear_log_file.setObjectName(u"pushButton_clear_log_file")

        self.verticalLayout_3.addWidget(self.pushButton_clear_log_file)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_log, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Theme", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Select Theme Mode and Color", None))
        self.label.setText(QCoreApplication.translate("Form", u"Theme Mode", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Theme Color", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Theme Density", None))
        self.comboBox_theme_mode.setItemText(0, QCoreApplication.translate("Form", u"default", None))
        self.comboBox_theme_mode.setItemText(1, QCoreApplication.translate("Form", u"Light", None))
        self.comboBox_theme_mode.setItemText(2, QCoreApplication.translate("Form", u"Dark", None))
        self.comboBox_theme_mode.setItemText(3, QCoreApplication.translate("Form", u"Classical", None))

        self.comboBox_theme_color.setItemText(0, QCoreApplication.translate("Form", u"default", None))
        self.comboBox_theme_color.setItemText(1, QCoreApplication.translate("Form", u"Amber", None))
        self.comboBox_theme_color.setItemText(2, QCoreApplication.translate("Form", u"Blue", None))
        self.comboBox_theme_color.setItemText(3, QCoreApplication.translate("Form", u"BlueGray", None))
        self.comboBox_theme_color.setItemText(4, QCoreApplication.translate("Form", u"Brown", None))
        self.comboBox_theme_color.setItemText(5, QCoreApplication.translate("Form", u"Cyan", None))
        self.comboBox_theme_color.setItemText(6, QCoreApplication.translate("Form", u"DeepOrange", None))
        self.comboBox_theme_color.setItemText(7, QCoreApplication.translate("Form", u"DeepPurple", None))
        self.comboBox_theme_color.setItemText(8, QCoreApplication.translate("Form", u"Gray", None))
        self.comboBox_theme_color.setItemText(9, QCoreApplication.translate("Form", u"Green", None))
        self.comboBox_theme_color.setItemText(10, QCoreApplication.translate("Form", u"Indigo", None))
        self.comboBox_theme_color.setItemText(11, QCoreApplication.translate("Form", u"LightBlue", None))
        self.comboBox_theme_color.setItemText(12, QCoreApplication.translate("Form", u"LightGreen", None))
        self.comboBox_theme_color.setItemText(13, QCoreApplication.translate("Form", u"Lime", None))
        self.comboBox_theme_color.setItemText(14, QCoreApplication.translate("Form", u"Orange", None))
        self.comboBox_theme_color.setItemText(15, QCoreApplication.translate("Form", u"Pink", None))
        self.comboBox_theme_color.setItemText(16, QCoreApplication.translate("Form", u"Purple", None))
        self.comboBox_theme_color.setItemText(17, QCoreApplication.translate("Form", u"Red", None))
        self.comboBox_theme_color.setItemText(18, QCoreApplication.translate("Form", u"Teal", None))
        self.comboBox_theme_color.setItemText(19, QCoreApplication.translate("Form", u"Yellow", None))

        self.comboBox_theme_density.setItemText(0, QCoreApplication.translate("Form", u"default", None))
        self.comboBox_theme_density.setItemText(1, QCoreApplication.translate("Form", u"Large", None))
        self.comboBox_theme_density.setItemText(2, QCoreApplication.translate("Form", u"Big", None))
        self.comboBox_theme_density.setItemText(3, QCoreApplication.translate("Form", u"Normal", None))
        self.comboBox_theme_density.setItemText(4, QCoreApplication.translate("Form", u"Small", None))
        self.comboBox_theme_density.setItemText(5, QCoreApplication.translate("Form", u"Tiny", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_theme), QCoreApplication.translate("Form", u"Display", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Log Filter", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"The Levels of the logging filters.", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Log Widget in the Main Window:", None))
        self.comboBox_level_window.setItemText(0, QCoreApplication.translate("Form", u"DEBUG", None))
        self.comboBox_level_window.setItemText(1, QCoreApplication.translate("Form", u"INFO", None))
        self.comboBox_level_window.setItemText(2, QCoreApplication.translate("Form", u"WARNING", None))
        self.comboBox_level_window.setItemText(3, QCoreApplication.translate("Form", u"ERROR", None))
        self.comboBox_level_window.setItemText(4, QCoreApplication.translate("Form", u"CRITICAL", None))
        self.comboBox_level_window.setItemText(5, QCoreApplication.translate("Form", u"FATAL", None))

        self.label_6.setText(QCoreApplication.translate("Form", u"Log Files:", None))
        self.comboBox_level_file.setItemText(0, QCoreApplication.translate("Form", u"DEBUG", None))
        self.comboBox_level_file.setItemText(1, QCoreApplication.translate("Form", u"INFO", None))
        self.comboBox_level_file.setItemText(2, QCoreApplication.translate("Form", u"WARNING", None))
        self.comboBox_level_file.setItemText(3, QCoreApplication.translate("Form", u"ERROR", None))
        self.comboBox_level_file.setItemText(4, QCoreApplication.translate("Form", u"CRITICAL", None))
        self.comboBox_level_file.setItemText(5, QCoreApplication.translate("Form", u"FATAL", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Log Files", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Log File Saved in", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.pushButton_use_default_path.setText(QCoreApplication.translate("Form", u"Use Default  Path", None))
        self.pushButton_open_log_folder.setText(QCoreApplication.translate("Form", u"Open Log Folder", None))
        self.pushButton_clear_log_file.setText(QCoreApplication.translate("Form", u"Clear Log Files", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_log), QCoreApplication.translate("Form", u"Logging", None))
    # retranslateUi

