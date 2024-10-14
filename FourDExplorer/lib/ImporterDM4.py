# -*- coding: utf-8 -*-

"""
*---------------------------- ImporterDM4.py ---------------------------------*
针对 Gatan Digital Micrograph .dm4 文件导入 4D-STEM 数据集的解析器

作者:           Sean
创建日期:       2024年10月12日

Parser to import 4D-STEM dataset from Gatan Digital Micrograph .dm4 file.

author:         Sean
date:           Oct 12, 2024
*---------------------------- ImporterDM4.py ---------------------------------*
"""

from logging import Logger 
import os 
import struct
import datetime

from PySide6.QtCore import QObject 
from dateutil import parser as dt_parser

from bin.TaskManager import TaskManager 
from bin.MetaManager import MetaManager
from bin.DateTimeManager import DateTimeManager
from lib.TaskLoadData import TaskLoadFourDSTEMFromDM4
from lib.CalibrationMisc import Voltage2WaveLength
from Constants import APP_VERSION

class TagObject:
    def __init__(self):
        self.name = None
        self.length = None

class TagDirectory(TagObject):
    def __init__(self, parent, name, length, closed, sorted, num_tags):
        self.parent_directory = parent
        self.name = name
        self.length = length
        self.tagtype = 'directory'
        self.closed = closed
        self.sorted = sorted
        self.num_tags = num_tags
        self.tags = []

    def __str__(self):
        return f"Tag Directory: {self.name}, Number of tags: {self.num_tags}, Closed: {self.closed}, Sorted: {self.sorted}"

    def append_tag(self, tag):
        if isinstance(tag, TagObject):
            if len(self.tags) < self.num_tags:
                self.tags.append(tag)
            else:
                raise ValueError("Number of tags exceeded")
        else:
            raise TypeError("Expected Tag object")
        
    def get_parent_directory(self):
        return self.parent_directory
    
    def get_name(self) -> str:
        return self.name
    
    def get_length(self) -> int:
        return self.length
    
    def get_type(self) -> str:
        return self.tagtype
    
    def is_closed(self) -> bool:
        return self.closed
    
    def is_sorted(self) -> bool:
        return self.sorted
    
    def get_num_tags(self) -> int:
        return self.num_tags
    
    def count_tags_recursive(self) -> int:
        count = 0
        for tag in self.tags:
            if tag.get_type() == 'directory':
                count += tag.count_tags_recursive()
            else:
                count += 1
        return count
    
    def show_tags(self, level = 0, show_max_level = 0):
        if show_max_level < 0:
            raise ValueError("show_max_level must be a non-negative integer")
        for i in range(self.num_tags):
            current_tag = self.tags[i]
            print(f"{'    '*level}{self.name} ({i+1}/{self.num_tags}), {current_tag.get_name()}, type: {current_tag.get_type()}")
            if current_tag.get_type() == 'directory' and level < show_max_level:
                current_tag.show_tags(level= level+1, show_max_level=show_max_level)

    def get_tags(self):
        return self.tags
    
    def get_tag(self, index):
        if index < self.num_tags:
            return self.tags[index]
        else:
            raise IndexError("Index out of range")
        
    def get_tag_by_name_raw(self, tag_name):
        for tag in self.tags:
            if tag.get_name() == tag_name:
                return tag
            if tag.get_type() == 'directory':
                result = tag.get_tag_by_name_raw(tag_name)
                if result is not None:
                    return result
        return None
    
    def get_tag_by_name(self, tag_name):
        result = self.get_tag_by_name_raw(tag_name)
        if result is None:
            raise ValueError(f"Tag not found: {tag_name}")
        return result
    
    def get_all_tags_with_name(self, tag_name) -> list:
        results = []
        for tag in self.tags:
            if tag.get_name() == tag_name:
                results.append(tag)
            if tag.get_type() == 'directory':
                results.extend(tag.get_all_tags_with_name(tag_name))
        return results

class Tag(TagObject):
    def __init__(self, parent, name, length, tag_type, data):
        self.parent_directory = parent
        self.name = name
        self.length = length
        self.tagtype = tag_type
        self.data = data

    def __str__(self):
        return f"Tag: {self.name}, Length: {self.length}, Type: {self.get_tag_type()['description']}, Data: {self.data}"

    def get_parent_directory(self):
        return self.parent_directory
    
    def get_name(self) -> str:
        return self.name
    
    def get_length(self) -> int:
        return self.length

    def get_type(self) -> str:
        return tagDataType[self.tagtype]['description']
    
    def get_data(self):
        if isinstance(self.data, TagArrayData):
            return self.data.read()
        else:
            return self.data
    
    def get_number_of_entries(self) -> int:
        if isinstance(self.get_data(), str):
            return 1
        else:
            return len(self.get_data())
        
class TagArrayData():
    def __init__(self, filepath, offset, dtype, dsize, byte_order, number_of_entries):
        self.path = filepath
        self.offset = offset
        self.dtype = dtype
        self.dsize = dsize
        self.byte_order = byte_order
        self.number_of_entries = number_of_entries

    def read(self):
        with open(self.path, 'rb') as f:
            f.seek(self.offset)
            data_entries = []
            for i in range(self.number_of_entries):
                data = struct.unpack(self.byte_order + self.dtype, f.read(self.dsize))[0]
                data_entries.append(data)
            return data_entries

    @property    
    def type(self):
        if self.dtype == 'h' or self.dtype == 'i' or self.dtype == 'q':
            return 'int'
        elif self.dtype == 'H' or self.dtype == 'I' or self.dtype == 'Q':
            return 'uint'
        elif self.dtype == 'f' or self.dtype == 'd':
            return 'float'
        else:
            raise TypeError(f"Unknown data type: {self.dtype}.")
        

tagDataType = {
    0x02: {'format': 'h', 'description': 'short (i2*)', 'size': 2},
    0x03: {'format': 'i', 'description': 'signed long (i4*)', 'size': 4},
    0x04: {'format': 'H', 'description': 'unsigned short (i2*) or unicode string', 'size': 2},
    0x05: {'format': 'I', 'description': 'unsigned long (i4*)', 'size': 4},
    0x06: {'format': 'f', 'description': 'float (f4*)', 'size': 4},
    0x07: {'format': 'd', 'description': 'double (f8*)', 'size': 8},
    0x08: {'format': 'b', 'description': 'boolean (i1)', 'size': 1},
    0x09: {'format': 'c', 'description': 'char (a1)', 'size': 1},
    0x0A: {'format': 'b', 'description': 'i1', 'size': 1},
    0x0B: {'format': 'q', 'description': 'long long (i8*)', 'size': 8}, # ?
    0x0C: {'format': 'Q', 'description': 'unsigned long long (i8*)', 'size': 8}, # ?
    0x0F: {'format': 'struct', 'description': 'group of data', 'size': None},  # Size varies
    0x12: {'format': 's', 'description': 'string (a)', 'size': None},  # Size varies
    0x14: {'format': 'array', 'description': 'array of data/array of group', 'size': None}  # Size varies
} 

"""
Implementation of a parser for the Digital Micrograph DM4 file format. The parser reads the header, tag directory, and tags in the file.
"""
class ParseDM4(QObject):
    def __init__(self, file_path, parent=None):
        super().__init__()
        self.file_path = file_path
        self.io = None  # io object
        self.byte_order = '>'  # Default to big-endian ('>' for big-endian, '<' for little-endian)
        self.byte_size = None # Size of the root tag directory 

    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger

    def open_file(self):
        self.logger.debug("Opening file...")
        try:
            self.io = open(self.file_path, 'rb')
            self.logger.debug("File opened successfully.")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")
        

    def read_header(self):
        self.logger.debug("Reading header...")
        f = self.io
        # The header consists of 16 bytes (DM version, root tag length, byte order)
        dm_version = struct.unpack('>I', f.read(4))[0]
        root_len = struct.unpack('>Q', f.read(8))[0]
        byte_order = struct.unpack('>I', f.read(4))[0]

        self.byte_size = root_len

        # Update byte order
        if byte_order == 1:
            self.byte_order = '<'  # Little-endian

        self.logger.debug(f"Header read successfully, DM version: {dm_version}, Root length: {root_len}, Byte order: {self.byte_order}.")

    def read_tag_directory(self, parent_dir_name = None, tag_dir_name=None, tag_dir_len=None):
        f = self.io
        # Read the sorted flag (1 byte), closed flag (1 byte), number of tags (8 bytes)
        sorted_flag = struct.unpack(self.byte_order + 'B', f.read(1))[0]
        # 1 = sorted, 0 = unsorted
        sorted_flag = True if sorted_flag == 1 else False
        closed_flag = struct.unpack(self.byte_order + 'B', f.read(1))[0]
        # 1 = open, 0 = closed
        closed_flag = True if closed_flag == 1 else False
        num_tags = struct.unpack('>Q', f.read(8))[0]

        tagdir = TagDirectory(parent_dir_name, tag_dir_name, tag_dir_len, closed_flag, sorted_flag, num_tags)
        
        # Read the tags in this directory
        for i in range(num_tags):
            tag = self.parse_tag(tag_dir_name)
            tagdir.append_tag(tag)

        return tagdir

    def parse_tag(self, parent_dir_name = None):
        f = self.io
        # A tag starts with 1 byte (tag indicator), 2 bytes (tag name length), and tag name
        tag_type = struct.unpack(self.byte_order + 'B', f.read(1))[0]

        # Read tag name length
        tag_name_len = struct.unpack('>H', f.read(2))[0]

        # Attempt to read the tag name as a UTF-8 string
        if tag_name_len > 0:
            try:
                tag_name = f.read(tag_name_len).decode('utf-8')
            except UnicodeDecodeError:
                # Handle decoding error - you can log or skip this tag, or try another encoding
                self.logger.warning(f"Failed to decode tag name at position {f.tell()}")
                tag_name = None
        else:
            tag_name = None
       
        if tag_type == 20:  # Tag Directory
            tag_len = struct.unpack('>Q', f.read(8))[0]
            tag_object = self.read_tag_directory(parent_dir_name=parent_dir_name, tag_dir_name=tag_name, tag_dir_len=tag_len)
        elif tag_type == 21:  # Tag
            tag_object = self.read_tag(parent_dir_name=parent_dir_name, tag_name = tag_name)
        elif tag_type == 00:  # End of file (8 nulls)
            self.logger.debug("End of file reached")
            return
        else:
            raise TypeError(f"Unknown tag type: {tag_type}")
        
        return tag_object

    def read_tag(self, parent_dir_name = None, tag_name = None):
        f = self.io
        # Read tag data size (8 bytes)
        tag_data_len = struct.unpack('>Q', f.read(8))[0]
        # Move past %%%%
        f.read(4)

        # Read the information about the tag
        tag_info_len = struct.unpack('>Q', f.read(8))[0]
        tag_info = [0] * tag_info_len
        for i in range(tag_info_len):
            tag_info[i] = struct.unpack('>q', f.read(8))[0]

        # Read the tag data
        if tag_info_len == 1: # Single data entry
            data_type = tagDataType[tag_info[0]]['format']
            data_size = tagDataType[tag_info[0]]['size']
            tag_data = struct.unpack(self.byte_order + data_type, f.read(data_size))[0]
        elif tag_info_len == 2: # String
            if tag_info[0] != 18:
                raise TypeError("Expected string tag")
            string_len = tag_info[1]
            tag_data = f.read(string_len).decode('utf-8')
        else:
            if tag_info[0] == 15: # Group of data i.e. struct
                # Read the number of data entries
                num_entries = tag_info[2]

                # Read the data entries
                data_entries = []
                for i in range(num_entries):
                    data_type = tagDataType[tag_info[i*2+4]]['format']
                    data_size = tagDataType[tag_info[i*2+4]]['size']
                    data = struct.unpack(self.byte_order + data_type, f.read(data_size))[0]
                    data_entries.append(data)
                tag_data = data_entries
            elif tag_info[0] == 20: # Array tag
                if tag_info_len == 3: # Single array
                    data_type = tagDataType[tag_info[1]]['format']
                    data_size = tagDataType[tag_info[1]]['size']
                    num_entries = tag_info[2]

                    offset = f.tell()
                    f.read(data_size * num_entries)
                    tag_data = TagArrayData(self.file_path, offset, data_type, data_size, self.byte_order, num_entries)
                else: # Arrays of groups
                    if tag_info[1] != 15:
                        raise TypeError("Expected group of data")
                    num_groups = tag_info[3]
                    array_size = tag_info[-1]
                    data_entries = []
                    for i in range(array_size):
                        struct_entries = []
                        for j in range(num_groups):
                            data_type = tagDataType[tag_info[5+j*2]]['format']
                            data_size = tagDataType[tag_info[5+j*2]]['size']
                            data = struct.unpack(self.byte_order + data_type, f.read(data_size))[0]
                            struct_entries.append(data)
                        data_entries.append(struct_entries)
                    tag_data = data_entries
            else:
                raise TypeError("Unknown tag data type", tag_info)
        
        return Tag(parent_dir_name, tag_name, tag_data_len, tag_info[0], tag_data)

    def parse(self):
        self.logger.debug("Starting parsing DM4 file...")
        self.open_file()
        self.read_header()
        self.logger.debug("Reading root directory of DM4 file...")
        dm4obj = self.read_tag_directory(parent_dir_name= "", tag_dir_name='/', tag_dir_len=self.byte_size)
        self.logger.debug("Parsing DM4 file completed.")

        return dm4obj

class ImporterDM4(QObject):
    """
    The importer calss for Gatan Digital Micrograph DM4 file format.
    """
    def __init__(self, item_name: str, item_parent_path: str, parent: QObject = None):
        super().__init__(parent)

        self.item_name = item_name
        self.item_parent_path = item_parent_path

        self._scan_i = 1
        self._scan_j = 1 
        self._dp_i = 1
        self._dp_j = 1
        self._num_images = 1
        self._scalar_type = 'uint'
        self._scalar_size = 1
        self._dm4_path = ''
        self._little_endian = True

        self._first_image_offset = 0

        self.meta = {
            '/General/fourd_explorer_version': '.'.join([str(i) for i in APP_VERSION]),
            '/General/date': self.datetime_manager.current_date,
            '/General/time': self.datetime_manager.current_time,
            '/General/time_zone': self.datetime_manager.current_timezone, 
            '/Acquisition/Camera/name': '',
            '/Acquisition/Camera/pixel_number_i': 1024,
            '/Acquisition/Camera/pixel_number_j': 1024,
            '/Acquisition/Camera/pixel_size_i': 15e-6,
            '/Acquisition/Camera/pixel_size_j': 15e-6,
            '/Acquisition/Camera/accelerating_voltage': 300000,
            '/Acquisition/Camera/camera_length': 0.0,
            '/Acquisition/Camera/step_size_i': 1.0,
            '/Acquisition/Camera/step_size_j': 1.0,
            '/Calibration/Space/dp_i': 1024,
            '/Calibration/Space/dp_j': 1024,
            '/Calibration/Space/du_i': 1.0,
            '/Calibration/Space/du_j': 1.0,
            '/Calibration/Space/scan_dr_i': 1.0,
            '/Calibration/Space/scan_dr_j': 1.0,
        }

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

    def parseDM4(self, dm4_path: str):
        self._dm4_path = dm4_path
        dm4obj = ParseDM4(dm4_path)
        root = dm4obj.parse()
        self._little_endian = True if dm4obj.byte_order == '<' else False
        image_list = root.get_tag_by_name('ImageList')
        taglist = []
        for tag in image_list.tags:
            dims = tag.get_tag_by_name('Dimensions')
            if dims.get_num_tags() == 4:
                taglist.append(tag)
            else:
                continue
        if len(taglist) == 0:
            raise ValueError("No 4D-STEM data found in the .dm4 file.")
        if len(taglist) > 1:
            self.logger.warning(f"Multiple 4D-STEM dataset found in the .dm4 file. Using the first one.")

        tagdir_4dstem = taglist[0]
        dims = tagdir_4dstem.get_tag_by_name('Dimensions')
        self.scan_i = dims.get_tag(0).get_data()
        self.scan_j = dims.get_tag(1).get_data()
        self._dp_i = dims.get_tag(2).get_data()
        self._dp_j = dims.get_tag(3).get_data()

        self._num_images = self.scan_i * self.scan_j

        data_tag = tagdir_4dstem.get_tag_by_name('Data')
        self._first_image_offset = data_tag.data.offset
        self._scalar_type = data_tag.data.type
        self._scalar_size = data_tag.data.dsize

        # Retrieve useful metadata
        device = tagdir_4dstem.get_tag_by_name('Device')
        active_size = device.get_tag_by_name('Active Size (pixels)').get_data()
        camera_pixel_size = device.get_tag_by_name('Pixel Size (um)').get_data() # um
        camera_name = ''.join(chr(i) for i in device.get_tag_by_name('Name').get_data())

        microscope_info = tagdir_4dstem.get_tag_by_name('Microscope Info')
        voltage = microscope_info.get_tag_by_name('Voltage').get_data() # V
        camera_length = microscope_info.get_tag_by_name('STEM Camera Length').get_data() # mm

        digiscan = tagdir_4dstem.get_tag_by_name('DigiScan')
        horizontal_spacing = digiscan.get_tag_by_name('Horizontal Spacing').get_data() # nm ?
        vertical_spacing = digiscan.get_tag_by_name('Vertical Spacing').get_data() # nm ?

        wavelength = Voltage2WaveLength(voltage)

        # Update metadata
        self.meta['/Acquisition/Camera/name'] = camera_name
        self.meta['/Acquisition/Camera/pixel_number_i'] = active_size[0]
        self.meta['/Acquisition/Camera/pixel_number_j'] = active_size[1]
        self.meta['/Acquisition/Camera/pixel_size_i'] = camera_pixel_size[0] * 1e-6
        self.meta['/Acquisition/Camera/pixel_size_j'] = camera_pixel_size[1] * 1e-6
        self.meta['/Acquisition/Camera/accelerating_voltage'] = voltage
        self.meta['/Acquisition/Camera/camera_length'] = camera_length
        self.meta['/Acquisition/Camera/step_size_i'] = horizontal_spacing * 1e-9
        self.meta['/Acquisition/Camera/step_size_j'] = vertical_spacing * 1e-9
        self.meta['/Calibration/Space/dp_i'] = self._dp_i
        self.meta['/Calibration/Space/dp_j'] = self._dp_j
        self.meta['/Calibration/Space/du_i'] = camera_pixel_size[0] * 1e-6 / (camera_length * 1e-3 * wavelength)
        self.meta['/Calibration/Space/du_j'] = camera_pixel_size[1] * 1e-6 / (camera_length * 1e-3 * wavelength)
        self.meta['/Calibration/Space/scan_dr_i'] = horizontal_spacing * 1e-9
        self.meta['/Calibration/Space/scan_dr_j'] = vertical_spacing * 1e-9
    
    def loadData(self):
        """
        This method will submit a load task to the task manager.

        Before this method is called, parseDM4() needs be
        called. Metadata will be initialized by those methods.
        """
        if not self._dm4_path:
            raise RuntimeError("No .mib file is assigned.")
        shape = (self._scan_i, self._scan_j, self._dp_i, self._dp_j)

        self.task = TaskLoadFourDSTEMFromDM4(
            shape = shape,
            file_path = self._dm4_path,
            item_parent_path = self.item_parent_path,
            item_name = self.item_name,
            offset_to_first_image = self._first_image_offset,
            scalar_type = self._scalar_type,
            scalar_size = self._scalar_size,
            little_endian = self._little_endian,
            parent = self,
            **self.meta,
        )
        self.task_manager.addTask(self.task)

