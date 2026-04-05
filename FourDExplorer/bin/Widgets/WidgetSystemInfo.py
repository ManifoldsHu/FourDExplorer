# -*- coding: utf-8 -*-

"""
*-------------------------- WidgetSystemInfo.py ------------------------------*
对系统信息进行显示的模块。

这个 Widget 是用在主界面的，使用 QTimer 每隔一定时间刷新一次 CPU 占用、内存占用、磁
盘占用以及磁盘IO速度。

作者：          胡一鸣
创建时间：      2022年3月10日

The module to show system information

This widget is used in the main window. It use QTimer to refresh CPU, memory,
disk and IO rate information.

author:         Hu Yiming
date:           Mar 10, 2022
*-------------------------- WidgetSystemInfo.py ------------------------------*
"""

from logging import Logger
import os
import time
import psutil
# import sys

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer

from ui import uiWidgetSystemInfo
from bin.HDFManager import HDFHandler


class WidgetSystemInfo(QWidget):
    """
    用于显示系统信息的模块。包含 3 个进度条以及一些标签。

    Widget to show system information (in Task tab). It includes 3 progress bars
    and some labels.
    """

    def __init__(self, parent: QWidget = None):
        """
        arguments:
            parent: (QWidget)
        """
        super().__init__(parent)
        self.ui = uiWidgetSystemInfo.Ui_Form()
        self.ui.setupUi(self)
        self._process = psutil.Process()
        self._cpu_count = max(psutil.cpu_count() or 1, 1)
        self._interval = 1000  # msec
        self._last_disk_io_timestamp = time.monotonic()
        self._last_app_read_bytes = 0
        self._last_app_write_bytes = 0
        psutil.cpu_percent(None)
        self._process.cpu_percent()
        process_io = self._getProcessIOCounters()
        if process_io is not None:
            self._last_app_read_bytes = getattr(process_io, "read_bytes", 0)
            self._last_app_write_bytes = getattr(process_io, "write_bytes", 0)
        self._setupTimer()

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    def _setupTimer(self):
        """
        This function will set up a timer to update the
        system info periodically.
        """
        self._timer = QTimer(self)
        self._timer.start(self._interval)
        self._timer.timeout.connect(self._updateCPU)
        self._timer.timeout.connect(self._updateMemory)
        self._timer.timeout.connect(self._updateDiskIO)

    def _clampPercentage(self, percentage: float) -> int:
        """
        Clamp a percentage value to the range [0, 100].

        arguments:
            percentage: (float)

        returns:
            (int)
        """
        return max(0, min(100, int(round(percentage))))

    def _getProcessIOCounters(self):
        """
        Get process-level disk IO counters when the platform supports it.

        returns:
            psutil._common.pio: process IO counters. Returns None when the
                current platform does not support this feature.
        """
        try:
            return self._process.io_counters()
        except (AttributeError, NotImplementedError, psutil.Error):
            return None

    def _updateCPU(self):
        """
        Update CPU information.
        """
        cpu_percent = psutil.cpu_percent(None)
        self.ui.label_cpu_percent.setText("{0:.1f}%".format(cpu_percent))
        self.ui.label_cpu_count.setText(str(self._cpu_count))
        app_cpu_percent = self._process.cpu_percent() / self._cpu_count
        app_cpu_percent = max(0.0, min(100.0, app_cpu_percent))
        self.ui.label_app_cpu_percent.setText(
            "{0:.1f}%".format(app_cpu_percent)
        )
        self.ui.progressBar_cpu_percent.setValue(
            self._clampPercentage(cpu_percent)
        )

    def _updateMemory(self):
        """
        Update memory information.
        """
        memory = psutil.virtual_memory()
        # memory.total
        # memory.used
        # memory.free
        self.ui.label_memory_total.setText(
            "{0:.2f}".format(memory.total / 2**20) + " MiB"
        )
        self.ui.label_memory_available.setText(
            "{0:.2f}".format(memory.available / 2**20) + " MiB"
        )
        self.ui.progressBar_memory_percent.setValue(
            self._clampPercentage(memory.percent)
        )
        app_memory = self._process.memory_info()
        self.ui.label_app_memory.setText(
            "{0:.2f}".format(app_memory.rss / 2**20) + " MiB"
        )

    def _updateDiskIO(self):
        """
        Update the disk IO information.
        """
        disk_usage = psutil.disk_usage(os.getcwd())
        self.ui.label_disk_total.setText(
            "{0:.2f}".format(disk_usage.total / 2**30) + " GiB"
        )
        self.ui.label_disk_available.setText(
            "{0:.2f}".format(disk_usage.free / 2**30) + " GiB"
        )
        self.ui.progressBar_disk_percent.setValue(
            self._clampPercentage(disk_usage.percent)
        )

        current_timestamp = time.monotonic()
        elapsed_seconds = max(
            current_timestamp - self._last_disk_io_timestamp,
            1e-6,
        )
        process_io = self._getProcessIOCounters()
        if process_io is None:
            self.ui.label_app_disk_read.setText("N/A")
            self.ui.label_app_disk_write.setText("N/A")
            self._last_disk_io_timestamp = current_timestamp
            return

        current_read_bytes = getattr(process_io, "read_bytes", 0)
        current_write_bytes = getattr(process_io, "write_bytes", 0)
        app_read_rate = max(
            current_read_bytes - self._last_app_read_bytes,
            0,
        ) / elapsed_seconds / 2**20
        app_write_rate = max(
            current_write_bytes - self._last_app_write_bytes,
            0,
        ) / elapsed_seconds / 2**20
        self.ui.label_app_disk_read.setText(
            "{0:.2f}".format(app_read_rate) + " MiB/s"
        )
        self.ui.label_app_disk_write.setText(
            "{0:.2f}".format(app_write_rate) + " MiB/s"
        )
        self._last_app_read_bytes = current_read_bytes
        self._last_app_write_bytes = current_write_bytes
        self._last_disk_io_timestamp = current_timestamp
