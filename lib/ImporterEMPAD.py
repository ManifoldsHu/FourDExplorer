# -*- coding: utf-8 -*-

"""
*---------------------------- ImporterEMPAD.py -------------------------------*
从 EMPAD 中读取数据的 Data importer.

4D-STEM 数据集的 Data importer 一般来说包含一个解析器，它是用来解析数据集的头文件的。
这个解析器会收集 4D-STEM 数据集的元数据，以准备把整个数据集复制进 HDF5 文件里。然后，
importer 就会创建一个任务，并把它提交到任务管理器中。

作者：          胡一鸣
创建时间：      2022年5月8日

Data importer from the EMPAD.

The Importers of 4D-STEM dataset has usually a parser to read the header file,
and collect those metadata as a preparation for copying the whole dataset into
the HDF5 file. Then, the importer will create a Task object and submit it to 
the task manager.

author:             Hu Yiming
date:               May 8, 2022
*---------------------------- ImporterEMPAD.py -------------------------------*
"""

from logging import Logger
from xml.dom.minidom import Document, parse
import os 

from PySide6.QtCore import QObject

from bin.TaskManager import TaskManager
from lib.TaskLoadData import TaskLoadFourDSTEMFromRaw 


class ImporterEMPAD(QObject):
    """
    The importer of EMPAD dataset.

    This importer corresponds to EMPAD whose software version is 1.0.0. Use 
    browser to open the .xml file, and we can see the EMPAD software version 
    at the begin of the file:
        ...
        - <root name="[acquisition name]">
            ...
            <software_version>1.0.0 (2020-03-12)</software_version>
            ...

    """
    def __init__(self, 
        item_name: str, 
        item_parent_path: str, 
        parent: QObject = None
    ):
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

        # pre-defined parameters of EMPAD v1.0.0
        self.scalar_type = 'float'
        self.scalar_size = 4
        self.little_endian = True
        self.offset_to_first_image = 0
        self.dp_i = 128
        self.dp_j = 128
        self.gap_between_images = 2 * self.dp_j * self.scalar_size

        self.meta = {
            'data_mode': '4D-STEM',
            'dp_i': 128,
            'dp_j': 128,
            'scalar_type': 'float',
            'scalar_size': 4,
            'little_endian': True,
            'camera': 'EMPAD',
        }

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger

    @property
    def task_manager(self) -> TaskManager:
        global qApp
        return qApp.task_manager

    def parseHead(self, xml_path: str) -> dict:
        """
        Parse the header .xml file.

        arguments:
            xml_path: (str) the absolute path of the xml file.
        """
        dom_tree = parse(xml_path)
        root: Document = dom_tree.documentElement
        self.xml_path = xml_path 
        self.meta['header_file'] = xml_path

        self._parseLoadingData(root)
        self._parseCalibrateData(root)
        self._parseOtherData(root)
        
        return self.meta

    def _parseLoadingData(self, root: Document):
        """
        Parsing the prerequisite meta data that controls how to load the 
        Dataset from the raw file.

        This function will parse:
            scan_i: the number of vertical scanning steps in STEM

            scan_j: the number of horizontal scanning steps in STEM

            raw_path: the absolute path of the raw file storing dataset.

        arguments:
            root: (Document) The root of the dom tree.
        """
        if root.getElementsByTagName('pix_x'):
            self.scan_j = int(self._getData(root, 'pix_x'))
            self.meta['scan_j'] = self.scan_j
        else:
            for mode in root.getElementsByTagName('scan_parameters'):
                if mode.getAttribute('mode') == 'acquire':
                    self.scan_j = int(
                        self._getData(mode, 'scan_resolution_x')
                    )
                    self.meta['scan_j'] = self.scan_j

        if root.getElementsByTagName('pix_y'):
            self.scan_i = int(self._getData(root, 'pix_y'))
            self.meta['scan_i'] = self.scan_i 
        else:
            for mode in root.getElementsByTagName('scan_parameters'):
                if mode.getAttribute('mode') == 'acquire':
                    self.scan_i = int(
                        self._getData(mode, 'scan_resolution_y')
                    )
                    self.meta['scan_i'] = self.scan_i 
        
        dir_name = os.path.dirname(self.xml_path)

        raw_name_node = root.getElementsByTagName('raw_file')[0]
        raw_name = raw_name_node.getAttribute('filename')
        self.raw_path = os.path.join(dir_name, raw_name)

        self.meta['raw_file'] = self.raw_path


    def _parseCalibrateData(self, root: Document):
        """
        Parsing the meta data for calibrating.

        This function will try parsing:
            full_scan_field_of_view: the physical length of the scanning 
                region of the conventional STEM.
            
            scan_size: the ration between the scanning region of EMPAD and the 
                region of the conventional STEM.

            scan_step_size: the scanning step size. In virtual image, it is the
                same as the pixel size of the real space (dx).

            scale_factor: NOTE I don't know what this parameter means. For now
                I use it to calculate step_size, which will actually shows on
                the scale bar in reconstructed images. It is regarded to act
                just like 'scan_size' above. 

                If I was wrong, please raise an issue on GitHub.

            camera_length: the camera length (CL) of STEM.

            voltage: the accelerate voltage of the electron beam.

            screen_current: the total screen current. May use this to calculate
                dose rate.

            scan_rotation: the rotational angle between scanning orientations 
                and the camera.


        arguments:
            root: (Document) The root of the dom tree.
        """
        try:
            for mode in root.getElementsByTagName('scan_parameters'):
                if mode.getAttribute('mode') == 'acquire':
                    self.meta['scan_size'] = float(
                        self._getData(mode, 'scan_size')
                    )
        except BaseException as e:
            self.logger.error('Failed to parse scan_size item.\n'
                '{0}'.format(e), exc_info = True)

        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            full = iom.getElementsByTagName('full_scan_field_of_view')[0]
            self.meta['full_scan_field_of_view_j'] = float(
                self._getData(full, 'x')
            )
            self.meta['full_scan_field_of_view_i'] = float(
                self._getData(full, 'y')
            )
            self.meta['scale_factor'] = float(
                self._getData(full, 'scale_factor')
            )

            # NOTE: I do not know what this 'scale_factor' means, and how to 
            # calibrate the physical step size with it. Here, I use 
            # 
            #   step_size_i = (full_scan_field_of_view_i * 
            #                   scale_factor * scan_size / scan_i) 
            # and
            #   step_size_j = (full_scan_field_of_view_j *
            #                   scale_factor * scan_size / scan_j)
            # 
            # If the formula is wrong, please raise an issue on GitHub.
            
            self.meta['scan_step_size_i'] = (
                self.meta['full_scan_field_of_view_i'] * 
                self.meta['scale_factor'] * 
                self.meta['scan_size'] / self.scan_i
            )

            self.meta['scan_step_size_j'] = (
                self.meta['full_scan_field_of_view_j'] *
                self.meta['scale_factor'] * 
                self.meta['scan_size'] / self.scan_j 
            )
        except BaseException as e:
            self.logger.error('Failed to parse scanning_step_size items.\n'
                '{0}'.format(e), exc_info = True)
        
        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['camera_length'] = float(
                self._getData(iom, 'nominal_camera_length')
            )
        except BaseException as e:
            self.logger.error('Failed to parse camera_length item.\n'
                '{0}'.format(e), exc_info = True)

        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['voltage'] = float(
                self._getData(iom, 'high_voltage')
            )
        except BaseException as e:
            self.logger.error('Failed to parse voltage item.\n'
                '{0}'.format(e), exc_info = True)

        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['scan_rotation'] = float(
                self._getData(iom, 'scan_rotation')
            )
        except BaseException as e:
            self.logger.error('Failed to parse scan_rotation item.\n'
                '{0}'.format(e), exc_info = True)

        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['screen_current'] = float(
                self._getData(iom, 'screen_current')
            )
        except BaseException as e:
            self.logger.error('Failed to parse screen_current item.\n'
                '{0}'.format(e))

    def _parseOtherData(self, root: Document):
        """
        Parsing other meta data, which may illustrate some property of the 
        4D-STEM dataset.

        These metadata will not affect calibration or reconstruction.

        arguments:
            root: (Document) The root of the dom tree.
        """
        try:
            time_node = root.getElementsByTagName('timestamp')[0]
            self.meta['acquire_datetime'] = time_node.getAttribute('isoformat')
        except BaseException as e:
            self.logger.error('Failed to parse acquire_datetime item.\n'
                '{0}'.format(e), exc_info = True)

        try:
            self.meta['empad_version'] = str(
                self._getData(root, 'software_version')
            )
            version = self.meta['empad_version'].split(' ')[0]
            if version != '1.0.0':
                self.logger.warning(
                    'The parser is designed to parse 4D-STEM header file from '
                    'EMPAD software v1.0.0, but the given header file is from '
                    'version {0}. This may cause incompatibility '
                    'problems.'.format(version)
                )
        except BaseException as e:
            self.logger.error('Failed to parse empad_version item.\n'
                '{0}'.format(e), exc_info = True)
            

    def _getData(self, doc: Document, tag: str) -> str:
        """
        A helper function to get data from an element.

        arguments:
            doc: (Document) Node of the dom tree.

            tag: (str) child tag's name.
        """
        return doc.getElementsByTagName(tag)[0].childNodes[0].data

    def loadData(self):
        """
        This method will submit a load task to the task manager.

        Before this method is called, parseHead() method must be called. Some
        key arguments will be initialized by that method.
        """
        shape = (self.scan_i, self.scan_j, self.dp_i, self.dp_j)
        self.task = TaskLoadFourDSTEMFromRaw(
            shape = shape,
            file_path = self.raw_path,
            item_parent_path = self.item_parent_path,
            item_name = self.item_name,
            offset_to_first_image = self.offset_to_first_image,
            gap_between_images = self.gap_between_images,
            parent = self, 
            **self.meta,
        )
        self.task_manager.addTask(self.task)
        



class ImporterEMPAD_NJU(ImporterEMPAD):
    """
    The importer of EMPAD dataset.

    This importer corresponds to EMPAD whose software version is 0.51. Use 
    browser to open the .xml file, and we can see the EMPAD software version 
    at the begin of the file:
        ...
        - <root name="[acquisition name]">
            ...
            <software_version>0.51 211118</software_version>
            ...

    This importer corresponds to the EMPAD installed in Nanjing University.
    """

    def _parseCalibrateData(self, root: Document):
        """
        Parsing the meta data for calibrating.

        This function will try parsing:
            full_scan_field_of_view: the physical length of the scanning 
                region of the conventional STEM.
            
            scan_size: the ration between the scanning region of EMPAD and the 
                region of the conventional STEM.

            scan_step_size: the scanning step size. In virtual image, it is the
                same as the pixel size of the real space (dx).

            camera_length: the camera length (CL) of STEM.

            voltage: the accelerate voltage of the electron beam.

            screen_current: the total screen current. May use this to calculate
                dose rate.

            scan_rotation: the rotational angle between scanning orientations 
                and the camera.

            reciprocal_pixel_size: the dk of the diffraction space, unit: rad.
            
        arguments:
            root: (Document) The root of the dom tree.
        """
        self.meta['is_flipped'] = True 

        try:
            for mode in root.getElementsByTagName('scan_parameters'):
                if mode.getAttribute('mode') == 'acquire':
                    self.meta['scan_size'] = float(
                        self._getData(mode, 'scan_size')
                    )
        except BaseException as e:
            self.logger.error('Failed to parse scan_size item.\n'
                '{0}'.format(e), exc_info = True)
        
        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            full = self._getData(iom, 'optics.get_full_scan_field_of_view')

            self.meta['full_scan_field_of_view_j'] = float(
                full.split(', ')[0].lstrip('[')
            )
            
            self.meta['full_scan_field_of_view_i'] = float(
                full.split(', ')[1].rstrip(']')
            )
            
            self.meta['scan_step_size_i'] = (
                self.meta['full_scan_field_of_view_i'] * 
                self.meta['scan_size'] / self.scan_i
            )

            self.meta['scan_step_size_j'] = (
                self.meta['full_scan_field_of_view_j'] * 
                self.meta['scan_size'] / self.scan_j 
            )
        except BaseException as e:
            self.logger.error('Failed to parse scanning_step_size items.\n'
                '{0}'.format(e), exc_info = True)

        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['camera_length'] = float(
                self._getData(iom, 'optics.get_cameralength')
            )
        except BaseException as e: 
            self.logger.error('Failed to parse camera_length item.\n'
                '{0}'.format(e), exc_info = True)

        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['voltage'] = float(
                self._getData(iom, 'source.get_voltage')
            )
        except BaseException as e:
            self.logger.error('Failed to parse voltage item.\n'
                '{0}'.format(e), exc_info = True)
            
        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['scan_rotation'] = float(
                self._getData(iom, 'column.get_scanrotation')
            )
        except BaseException as e:
            self.logger.error('Failed to parse scan_rotation item.\n'
                '{0}'.format(e), exc_info = True)

        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['screen_current'] = float(
                self._getData(iom, 'source.get_screencurrent')
            )
        except BaseException as e:
            self.logger.error('Failed to parse screen_current item.\n'
                '{0}'.format(e), exc_info = True)

        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['dp_pixel_size_reciprocal'] = float(
                self._getData(iom, 'calibrated_diffraction_angle')
            )
        except BaseException as e:
            self.logger.error('Failed to parse reciprocal_pixel_size item.\n'
                '{0}'.format(e), exc_info = True)

    def _parseOtherData(self, root: Document):
        """
        Parsing other meta data, which may illustrate some property of the 
        4D-STEM dataset.

        These metadata will not affect calibration or reconstruction.

        arguments:
            root: (Document) The root of the dom tree.
        """
        try:
            time_node = root.getElementsByTagName('timestamp')[0]
            self.meta['acquire_datetime'] = time_node.getAttribute('isoformat')
        except BaseException as e:
            self.logger.error('Failed to parse acquire_datetime item.\n'
                '{0}'.format(e), exc_info = True)

        try:
            self.meta['empad_version'] = str(
                self._getData(root, 'software_version')
            )
            version = self.meta['empad_version'].split(' ')[0]
            if version != '0.51':
                self.logger.warning(
                    'The parser is designed to parse 4D-STEM header file from '
                    'EMPAD software v0.51 (installed in Nanjing University), '
                    'but the given header file is from version {0}. This may '
                    'cause incompatibility problems.'.format(version)
                )
        except BaseException as e:
            self.logger.error('Failed to parse empad_version item.\n'
                '{0}'.format(e), exc_info = True)
