# -*- coding: utf-8 -*-

"""
*---------------------------- ImporterEMPAD.py -------------------------------*
Data importer from the EMPAD.

*---------------------------- ImporterEMPAD.py -------------------------------*
"""

from xml.dom.minidom import Document, parse
import os 

from PySide6.QtCore import QObject 


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
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        
        # pre-defined parameters of EMPAD v1.0.0
        self.scalar_type = 'float'
        self.scalar_size = 4
        self.little_endian = True
        self.offset_to_first_image = 0
        self.dp_i = 128
        self.dp_j = 128
        self.gap_between_images = 2 * self.dp_j * self.scalar_size

        self.meta = {
            'dp_i': 128,
            'dp_j': 128,
            'scalar_type': 'float',
            'scalar_size': 4,
            'little_endian': True,
            'camera': 'EMPAD',
        }

    def parseHead(self, xml_path: str):

        dom_tree = parse(xml_path)
        root: Document = dom_tree.documentElement
        self.xml_path = xml_path 
        self.meta['header_file'] = xml_path

        self._parseLoadingData(root)
        self._parseCalibrateData(root)
        

        # ----- Parsing parameters for calibrating -----
        
        

        

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
        raw_name = raw_name_node.getAttribute('file_name')
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
        except BaseException:
            pass 

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
            
            self.meta['scanning_step_size_i'] = (
                self.meta['full_scan_field_of_view_i'] * 
                self.meta['scale_factor'] * 
                self.meta['scan_size'] / self.scan_i
            )

            self.meta['scanning_step_size_j'] = (
                self.meta['full_scan_field_of_view_j'] *
                self.meta['scale_factor'] * 
                self.meta['scan_size'] / self.scan_j 
            )
        except BaseException:
            pass
        
        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['camera_length'] = float(
                self._getData(iom, 'nominal_camera_length')
            )
        except BaseException:
            pass 

        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['voltage'] = float(
                self._getData(iom, 'high_voltage')
            )
        except BaseException:
            pass 

        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['scan_rotation'] = float(
                self._getData(iom, 'scan_rotation')
            )
        except BaseException:
            pass 

        try:
            iom = root.getElementsByTagName('iom_measurements')[0]
            self.meta['screen_current'] = float(
                self._getData(iom, 'screen_current')
            )
        except BaseException:
            pass 

    def _parseCalibrateData(self, root: Document):
        """
        Parsing other meta data.

        arguments:
            root: (Document) The root of the dom tree.
        """
        try:
            time_node = root.getElementsByTagName('timestamp')[0]
            self.meta['acquire_datetime'] = time_node.getAttribute('isoformat')
        except BaseException:
            pass 



    def _getData(self, doc: Document, tag: str) -> str:
        """
        A helper function to get data from an element.

        arguments:
            doc: (Document) Node of the dom tree.

            tag: (str) child tag's name.
        """
        return doc.getElementsByTagName(tag).childNodes[0].data


class ImporterEMPAD_NJU(QObject):
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
    pass 

        
    