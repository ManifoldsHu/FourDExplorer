# -*- coding: utf-8 -*-

"""
*---------------------------- DialogAbout.py ---------------------------------*
软件的关于界面。

作者:           胡一鸣
创建日期:       2022年10月6日

The dialog to show the 'about' information.

author:         Hu Yiming
date:           Oct 6, 2022
*---------------------------- DialogAbout.py ---------------------------------*
"""

import os
from PySide6.QtCore import QUrl, Qt
from PySide6.QtWidgets import (
    QDialog,
    QWidget,
    QLabel,
    QLineEdit,
    QMessageBox,
    QVBoxLayout,
    QDialogButtonBox,
)
from PySide6.QtGui import QPixmap, QDesktopServices
from Constants import ROOT_PATH, APP_VERSION
from ui import uiDialogAbout, icon_rc


class DialogAbout(QDialog):
    """
    用于查看软件信息的对话框。

    Dialog to view the information of the software.
    """

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.ui = uiDialogAbout.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("About")

        icon_path = os.path.join(ROOT_PATH, "ui", "resources", "icons", "4D.png")
        _pic = QPixmap(icon_path)
        _pic.setDevicePixelRatio(4)
        self.ui.label_icon.setPixmap(_pic)
        # self.ui.graphicsView.setPixmap(_pic)
        # self.ui.graphicsView.setStyleSheet(
        #     "border-image: url(:/WindowIcon/resources/icons/4D.png;"
        # )

        version = ".".join([str(v) for v in APP_VERSION])
        self.ui.label_version.setText(version)
        self.ui.label_version_en.setText(version)

        link_labels = [
            self.ui.label_website_cn,
            self.ui.label_repo_cn,
            self.ui.label_doc_cn,
            self.ui.label_website,
            self.ui.label_repo,
            self.ui.label_doc,
        ]
        for label in link_labels:
            label.setOpenExternalLinks(False)
            label.setTextInteractionFlags(
                Qt.LinksAccessibleByMouse | Qt.LinksAccessibleByKeyboard
            )
            label.linkActivated.connect(self._showLinkDialog)

    def _showLinkDialog(self, url: str):
        """
        Show the dialog used to confirm opening an external link.

        arguments:
            url: (str) the external link to be opened.
        """
        dialog = DialogOpenLink(url, self)
        dialog.exec()


class DialogOpenLink(QDialog):
    """
    Dialog to confirm whether an external link should be opened.
    """

    def __init__(self, url: str, parent: QWidget = None):
        """
        arguments:
            url: (str) the external link to be displayed.

            parent: (QWidget) the parent widget.
        """
        super().__init__(parent)
        self._url = url

        self.setWindowTitle("Open Link")

        self._label = QLabel("Open this link in your default browser?", self)
        self._line_edit = QLineEdit(self)
        self._line_edit.setReadOnly(True)
        self._line_edit.setText(url)
        self._line_edit.setCursorPosition(0)
        self._line_edit.selectAll()

        self._button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            parent=self,
        )
        self._button_box.accepted.connect(self._openLink)
        self._button_box.rejected.connect(self.reject)

        self._layout = QVBoxLayout(self)
        self._layout.addWidget(self._label)
        self._layout.addWidget(self._line_edit)
        self._layout.addWidget(self._button_box)

    def _openLink(self):
        """
        Open the current link with the default external browser.
        """
        if QDesktopServices.openUrl(QUrl(self._url)):
            self.accept()
            return

        QMessageBox.warning(
            self,
            "Open Link Failed",
            "Failed to open the external browser. Please copy the URL and open it manually.",
        )
        self._line_edit.setFocus()
        self._line_edit.selectAll()
        