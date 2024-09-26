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
        self._interval = 1000   # msec
        self._setupTimer()
        self._last_app_read_bytes = 0
        self._last_app_write_bytes = 0

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
        

    def _updateCPU(self):
        """
        Update CPU information.
        """
        # _process = psutil.Process()

        cpu_percent = psutil.cpu_percent()
        self.ui.label_cpu_percent.setText(
            str(cpu_percent)+'%'
        )
        cpu_count = psutil.cpu_count()
        self.ui.label_cpu_count.setText(
            str(cpu_count)
        )
        app_cpu_percent = self._process.cpu_percent()
        self.ui.label_app_cpu_percent.setText(str(app_cpu_percent)+'%')
        self.ui.progressBar_cpu_percent.setValue(cpu_percent)
        # self.logger.info('_updateCPU() is called')

    def _updateMemory(self):
        """
        Update memory information.
        """
        memory = psutil.virtual_memory()
        # memory.total
        # memory.used
        # memory.free
        self.ui.label_memory_total.setText(
            '{0:.2f}'.format(memory.total/2**20)+' MiB'
        )
        self.ui.label_memory_available.setText(
            '{0:.2f}'.format(memory.free/2**20)+' MiB'
        )
        self.ui.progressBar_memory_percent.setValue(
            memory.used/memory.total*100
        )
        app_memory = self._process.memory_info()
        self.ui.label_app_memory.setText(
            '{0:.2f}'.format(app_memory.rss/2**20) + 'MiB'
        )
        

    def _updateDiskIO(self):
        """
        Update the disk IO information.
        """
        disk_usage = psutil.disk_usage(os.getcwd())
        self.ui.label_disk_total.setText(
            '{0:.2f}'.format(disk_usage.total/2**30)+' GiB'
        )
        self.ui.label_disk_available.setText(
            '{0:.2f}'.format(disk_usage.free/2**30)+' GiB'
        )
        self.ui.progressBar_disk_percent.setValue(
            disk_usage.percent
        )
        app_disk_io = psutil.disk_io_counters()
        app_read_rate = (
            (app_disk_io.read_bytes - self._last_app_read_bytes)
                / self._interval * 1000 / 2**20
        )
        app_write_rate = (
            (app_disk_io.write_bytes - self._last_app_write_bytes)
                / self._interval * 1000 / 2**20
        )
        self.ui.label_app_disk_read.setText(
            '{0:.2f}'.format(app_read_rate) + ' MiB/s'
        )
        self.ui.label_app_disk_write.setText(
            '{0:.2f}'.format(app_write_rate) + ' MiB/s'
        )
        self._last_app_read_bytes = app_disk_io.read_bytes
        self._last_app_write_bytes = app_disk_io.write_bytes



