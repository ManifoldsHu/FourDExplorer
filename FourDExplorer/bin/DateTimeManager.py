# -*- coding: utf-8 -*- 

"""
*--------------------------- DateTimeManager.py ------------------------------*
用于生成标准的日期与时间的管理类。

标准的日期格式为，例如：
2024-01-09
标准的时间格式为，例如：
15:53:02
其中，时间的取值范围是 00:00:00 - 23:59:59
同时也给出时区，标准的时区格式为，例如 UTC+08

作者：          胡一鸣
创建时间：      2024年1月9日

Manages date and time with standard format.

Standard date format is like:
2024-01-09
Standard time format is like:
15:53:02
The value range of time is 00:00:00 - 23:59:59
At the same time, it provides time zone, like UTC+08.

author:         Hu Yiming
date:           Jan 9, 2024
"""

import datetime 
from PySide6.QtCore import QObject 

class DateTimeManager(QObject):
    """
    给出当前按照标准格式的，日期、时间和时区。

    Gives current date, time and timezone.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)

    @property
    def current_time(self) -> str:
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")
    
    @property
    def current_date(self) -> str:
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d")
    
    @property
    def current_timezone(self) -> str:
        now = datetime.datetime.now()
        time_zone = now.astimezone().tzinfo
        utc_offset = time_zone.utcoffset(now)
        offset_hours = int(utc_offset.total_seconds() / 3600)
        return offset_hours 