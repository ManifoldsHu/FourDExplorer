# -*- coding: utf-8 -*- 

"""
*---------------------------- ImporterMIB.py ---------------------------------*
从 Merlin .mib 文件中读取数据的 Data importer.

4D-STEM 数据集的 Data importer 一般来说包含一个解析器，它是用来解析数据集的头文件的。
这个解析器会收集 4D-STEM 数据集的元数据，以准备把整个数据集复制进 HDF5 文件里。然后，
importer 就会创建一个任务，并把它提交到任务管理器中。

作者：          胡一鸣 
创建时间：      2024年1月12日 

Data importer for Merlin Medipix3 Detector.

The Importers of 4D-STEM dataset has usually a parser to read the header file,
and collect those metadata as a preparation for copying the whole dataset into
the HDF5 file. Then, the importer will create a Task object and submit it to 
the task manager.

author:         Hu Yiming 
date:           Jan 12, 2024
*---------------------------- ImporterMIB.py ---------------------------------*
"""

from logging import Logger 
import os 
import datetime

from PySide6.QtCore import QObject 
from dateutil import parser as dt_parser

from bin.TaskManager import TaskManager 
from bin.MetaManager import MetaManager
from bin.DateTimeManager import DateTimeManager
from lib.TaskLoadData import TaskLoadFourDSTEMFromRaw
from lib.CalibrationMisc import Voltage2WaveLength
from Constants import APP_VERSION 

class ImporterMIB(QObject):
    """
    The importer of Merlin MIB dataset. 
    
    There are usually 2 files, including a .mib file and a .hdr file. Although 
    use .mib file only is enough for dataset reading and basic anaylsis, we 
    still recommend to parse .hdr file for more information. 

    The key usage of the importer is to fill meta items according to schema 
    defined in /schema/MetaStructures/4dstem.json
    """
    def __init__(self, item_name: str, item_parent_path: str, parent: QObject = None):
        """
        arguments:
            item_name: (str) the created Dataset's name as an HDF object.

            item_parent_path: (str) the path of the created Dataset's parent 
                group.

            parent: (QObject)
        """
        super().__init__(parent)
        
        self.item_name = item_name 
        self.item_parent_path = item_parent_path

        self._scan_i = 1
        self._scan_j = 1 
        self._dp_i = 1
        self._dp_j = 1
        self._num_images = 1
        
        self._mib_path = ''
        self._hdr_path = ''
        self._scalar_type = 'uint'
        self._scalar_size = 1
        self._little_endian = True 

        self._is_flipped = False    # When loading the dataset, do images should be transposed? TODO: Confirm it.
        self._rotate90 = False      # When loading the dataset, do images should be rotated? TODO: Confirm it.

        # pre-defined parameters for Merlin Medipix3
        self.meta = {
            '/General/fourd_explorer_version': '.'.join([str(i) for i in APP_VERSION]),
            '/General/date': self.datetime_manager.current_date,
            '/General/time': self.datetime_manager.current_time,
            '/General/time_zone': self.datetime_manager.current_timezone,
            '/Acquisition/Camera/name': 'MerlinEM (Medipix3)',
            '/Acquisition/Cemera/manufacturer': 'Quantum Detectors',
            '/Acquisition/Camera/pixel_number_i': 256,
            '/Acquisition/Camera/pixel_number_j': 256,
            '/Acquisition/Camera/pixel_size_i': 55e-6,
            '/Acquisition/Camera/pixel_size_j': 55e-6,
        }

        self._scan_i_in_hdr = False     # Whether scan_i can be read in .hdr file
        self._scan_j_in_hdr = False     # Whether scan_j can be read in .hdr file 


    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger 
    
    @property
    def task_manager(self) -> TaskManager:
        global qApp 
        return qApp.task_manager 
    
    @property
    def datetime_manager(self) -> DateTimeManager:
        global qApp 
        return qApp.datetime_manager 


    def parseHdrFile(self, hdr_path: str):
        """
        DEPRECATED

        This function will parse the companion .hdr file.

        It is a text file that includes important information such as:
            Frames per Trigger      columns of scanning (scan_j)
            Frames in Acquisition   total image number (scan_i x scan_j)
        without it (especially frames per trigger) we cannot findout scanning 
        coordinates. If user does not provide .hdr file, the scanning coordinate
        should be decided through user input.

        arguments:
            hdr_path: (str) the path of the .hdr file
        """
        _hdr_meta = {}
        with open(hdr_path, encoding = 'utf-8') as hdr_file:
            self._hdr_path = hdr_path 
            for line in hdr_file:
                if line.startswith("HDR") or line.startswith("END"):
                    continue 
                key, value = line.split(':')
                value = value.lstrip('\t').rstrip('\n')
                _hdr_meta[key] = value 
            self.meta['/General/header_path'] = hdr_path

            try:
                self._scan_j = int(_hdr_meta["Frames per Trigger (Number)"])
                self.meta['/Calibration/Space/scan_j'] = self._scan_j 
                self._scan_j_in_hdr = True 
            except Exception as e:
                self.logger.error(f"Failed to parse Frames per Trigger in .hdr file: {e}  ", exc_info = True)
                self._scan_j_in_hdr = False 

            try:
                self._scan_i = int(_hdr_meta["Frames in Acquisition (Number)"]) // self._scan_j 
                self.meta['/Calibration/Space/scan_i'] = self._scan_i 
                self._scan_i_in_hdr = True 
            except Exception as e:
                self.logger.error(f"Failed to parse Frames in Acquisition in .hdr file: {e}", exc_info = True)
                self._scan_i_in_hdr = False 
            
            if self._scan_i_in_hdr and self._scan_j_in_hdr:
                self._num_images = self._scan_i * self._scan_j 

         
    def parseMibHead(self, mib_path: str):
        """
        This function will parse the head of the .mib file.

        arguments:
            mib_path: (str) The path of the .mib file 
        """
        with open(mib_path, 'rb') as file:
            head_str = file.read(1024).decode()
            file.seek(0, os.SEEK_END)
            file_size = file.tell()
            file.seek(0)

        self._mib_path = mib_path 

        head_test = head_str.split(',')
        if head_test[2] == "00384":
            head_size = 384
            self._gap_between_images = 384 
            self._first_image_offset = 384 
        elif head_test[2] == "00768":
            head_size = 768 
            self._gap_between_images = 768
            self._first_image_offset = 768
        else:
            raise NotImplementedError(f"Unrecognizied length of head: {mib_path}")
        head = [p for p in head_str[0:head_size].split(',') if '\x00' not in p]
            
        image_size = (int(head[4]), int(head[5]))
        self._dp_i, self._dp_j = image_size 
        self.meta['/Calibration/Space/dp_i'] = self._dp_i 
        self.meta['/Calibration/Space/dp_j'] = self._dp_j 
            
        if head[6] == "R64":
            raise NotImplementedError(f"Unsupported raw data: {head[6]}")
        elif head[6] == "U08":
            self._scalar_size = 1 
        elif head[6] == "U16":
            self._scalar_size = 2
        elif head[6] == "U32":
            self._scalar_size = 4
        else:
            raise NotImplementedError(f"Unsupported data type: {head[6]}")
            
        self._scalar_type = 'uint'
        self._little_endian = True 
            
        self._time_stamp = head[-3]     # ISO 8601
        date_str, time_str, timezone_str = self._parseMibDatetime(self._time_stamp)
        self.meta['/Acquisition/Microscope/acquisition_date'] = date_str 
        self.meta['/Acquisition/Microscope/acquisition_time'] = time_str 
        self.meta['/Acquisition/Microscope/acquisition_timezone'] = timezone_str 

        if not self._scan_i_in_hdr or not self._scan_j_in_hdr:
            bytes_per_image = image_size[0] * image_size[1] * self._scalar_size
            self._num_images = file_size // (bytes_per_image + self._gap_between_images)


    @property 
    def is_scan_parsed(self) -> bool:
        """
        Returns whether scanning coordinate (scan_i, scan_j) is parsed successfully.

        returns:
            (bool)
        """
        return self._scan_i_in_hdr and self._scan_j_in_hdr 
    
    @property 
    def scan_i(self) -> int:
        return self._scan_i 
    
    @scan_i.setter 
    def scan_i(self, si: int):
        if not isinstance(si, int):
            raise TypeError("scan_i must be a integer.")
        elif si <= 0:
            raise ValueError("scan_i must be larger than 0.")
        self._scan_i = si 
    
    @property
    def scan_j(self) -> int:
        return self._scan_j 

    @scan_j.setter 
    def scan_j(self, sj: int):
        if not isinstance(sj, int):
            raise TypeError("scan_j must be a integer.")
        elif sj <= 0:
            raise ValueError("scan_j must be larger than 0.")
        self._scan_j = sj 

    def _parseMibDatetime(self, dt_str: str):
        """
        Parse the date, time and time zone information from .mib file.

        It follows ISO-8601.

        arguments:
            dt_str: (str) the time stamp. e.g. "2021-12-15T18:20:44.325553+02:00"

        returns:
            (Tuple[str]) date string e.g. "2024-01-17", 
                time string e.g. "21:11:32", and 
                time zone string e.g. "UTC+08:00"
        """
        dt = dt_parser.isoparse(dt_str)
        date_str = dt.strftime("%Y-%m-%d")
        time_str = dt.strftime("%H:%M:%S")

        if dt.tzinfo is not None and dt.utcoffset() is not None:
            offset_seconds = dt.utcoffset().total_seconds()
            offset_hours = int(offset_seconds // 3600)
            offset_minutes = int((offset_seconds % 3600) // 60)
            timezone_str = f"UTC{offset_hours:+03d}:{offset_minutes:02d}"
        else:
            timezone_str = "UTC"
        
        return (date_str, time_str, timezone_str) 

    def loadData(self):
        """
        This method will submit a load task to the task manager.

        Before this method is called, parseMibHead() and parseHdrFile() need be
        called. Metadata will be initialized by those methods.
        """
        if not self._mib_path:
            raise RuntimeError("No .mib file is assigned.")
        shape = (self._scan_i, self._scan_j, self._dp_i, self._dp_j)
        # print(f"shape: {shape}")
        # print(f"file_path: {self._mib_path}")
        # print(f"item_parent_path: {self.item_parent_path}")
        self.task = TaskLoadFourDSTEMFromRaw(
            shape = shape,
            file_path = self._mib_path,
            item_parent_path = self.item_parent_path,
            item_name = self.item_name,
            offset_to_first_image = self._first_image_offset,
            gap_between_images = self._gap_between_images,
            scalar_type = self._scalar_type,
            scalar_size = self._scalar_size,
            little_endian = True,
            is_flipped = self._is_flipped,
            rotate90 = self._rotate90,
            parent = self,
            **self.meta,
        )
        self.task_manager.addTask(self.task)
