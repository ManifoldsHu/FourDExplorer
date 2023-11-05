# -*- coding: utf-8 -*- 

"""
*-------------------------- MetaManagerFourDSTEM.py --------------------------*
管理 .4dstem 数据集的元数据。

注意，只有那些基本的量会被存储，而其他参数将被实时计算。例如，加速电压会被存储，而波长
会则由加速电压导出，从而被实时计算。

元数据会以树状的形式进行存储，其树枝节点用大驼峰的形式命名，而叶子节点则用下划线命名法。
当然，在程序中我们不会使用这个特性来决定一个节点是否为叶子节点。

在实际的操作中，我们期望为每项元数据都提供单独的修改界面，从而规范输入。这需要大量的工
作。

作者：          胡一鸣
创建时间：      2023年10月31日

Manages metadata for .4dstem datasets.

Note that only fundamental quantities are stored, whereas other parameters are
calculated in real-time. For example, the acceleration voltage is stored, while
the wavelength is derived from it and thus calculated on-the-fly.

Metadata is stored in a tree-like structure, with branch nodes named using Pa-
scalCase, and leaf nodes using snake_case. Of course, in the program, we will
not use this feature to determine whether a node is a leaf node or not.

In practical operations, we aim to provide individual modification interface 
for each piece of metadata, thereby standardizing input. This requires extens-
ive work.

author:         Hu Yiming
date:           Oct 31, 2023
*-------------------------- MetaManagerFourDSTEM.py --------------------------*
"""

from logging import Logger 
from typing import Type 

from PySide6.QtCore import QObject

from Constants import HDFType 
from bin.HDFManager import HDFHandler 
from bin.MetaManagers.MetadataFields import FloatField, IntField, StringField
from bin.MetaManagers.UnitManager import UnitManager

class MetaManagerFourDSTEM(QObject):
    """
    管理 .4dstem 数据集元数据的封装类。其包含：

    General/
    title                   str         initialized by dataset name, but not necessarily the same.
    original_name           str         original file name without extension
    original_path           str         original file path
    authors                 str         in LaTeX format, i.e. Surname1, Name1 and Surname2, Name2 and ...
    notes                   str         may support rich text (html?)
    time                    str         creation time in ISO 8601, 13:29:10
    date                    str         creation date in ISO 8601, 2018-01-28
    time_zone               str         supported by the python-dateutil library, the same as the system
    doi                     str         

    FileIO/
    fourd_explorer_version  str         e.g. 0.5.2

    AcquisitionInstrument/Microscope/
    name                    str         e.g. Titan3 Cubed 60-300
    manufacturer            str         e.g. FEI 
    beam_current            float       A       nA 
    accelerate_voltage      float       V       kV
    probe_area              float       m^2     nm^2
    camera_length           float       m       mm
    convergence_angle       float       rad     mrad        alpha/convergent semi-angle 
    magnification           float
    dwell_time              float       s       ms          
    step_size_i             float       m       nm 
    step_size_j             float       m       nm 

    AcquisitionInstrument/Camera/
    name                    str         e.g. EMPAD 
    manufacturer            str         e.g. FEI 
    pixel_number_i          int         
    pixel_number_j          int 
    pixel_size_i            float       m       um
    pixel_size_j            float       m       um          

    AcquisitionInstrument/Stage/
    (Not Implemented)
    tilt_alpha              float       mrad    deg 
    tilt_beta               float       mrad    deg 
    rotation                float       mrad    deg 
    x                       float       m       mm 
    y                       float       m       mm 
    z                       float       m       mm 

    Calibration/Space/
    du_i                    float       m^-1    nm^-1       pixel size of the diffraction space, can be calibrated by alpha / wave_length / bright_field_disk_radius (in pixel). Note that dr_i and dr_j can be induced from du_i and du_j, and are not equal to scan_dr_i and scan_dr_j.
    du_j                    float       m^-1    nm^-1       pixel size of the diffraction space, can be calibrated by alpha / wave_length / bright_field_disk_radius(in pixel) 
    scan_dr_i               float       m       nm          equal to scan_step_size_i (only to be displayed)
    scan_dr_j               float       m       nm          equal to scan_step_size_j (only to be displayed)
    dr_i                    float       m       nm          equal to wave_length * bright_field_disk_radius (in pixel) / alpha / dp_i (only to be displayed)
    dr_j                    float       m       nm          equal to wave_length * bright_field_disk_radius (in pixel) / alpha / dp_j (only to be displayed)
    dp_i                    int         pixel number (only to be displayed) 
    dp_j                                pixel number (only to be displayed)
    scan_i                  int         pixel number (only to be displayed)
    scan_j                  int         pixel number (only to be displayed)

    Calibration/RotationalOffsetCorrection/
    scan_rotation           float       rad     mrad 

    Calibration/DiffractionAlignment/
    alignment_pixel_i       int
    alignment_pixel_j       int
    alignment_moving_path   str         record the path of the vector field that records the center of the diffraction pattern should be moved at each scanning point.
    
    Aberration/
    (Not Implemented)
    C1                      float       m       nm          defocus
    A1                      float       m       nm          2-fold astigmatism
    B2                      float       m       nm          axial coma
    A2                      float       m       nm          3-fold astigmatism
    C3                      float       m       um          spherical aberration
    S3                      float       m       um          star aberration
    A3                      float       m       um          4-fold astigmatism
    B4                      float       m       um          axial coma
    D4                      float       m       um          3 lobe aberration
    A4                      float       m       um          5-fold astigmatism
    C5                      float       m       mm          spherical aberration
    A5                      float       m       mm          6-fold astigmatism

    Quantify/
    display_vmin            float 
    display_vmax            float 
    display_norm_mode       str         'linear' or 'logarithm'
    display_colormap        str 

    """


    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        # 需要在这里将所有涉及到的 attribute 进行初始化。例如，
        self._initializeMetadata()
        self._meta = {}
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp 
        return qApp.hdf_handler
    
    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger
    
    def _initializeMetadata(self):
        """
        Initialize all of the metadata. All values will be set to None.
        """
        

    def _initializeGeneralMetaItems(self): 
        """
        Initialize the metadata that is under /General/
        """
        self._meta['/General/title'] = StringField(
            value=None, 
            description="initialized by dataset name, but not necessarily the same.",
            parent=self,
        )
        self._meta['/General/original_name'] = StringField(
            value=None,
            description="original file name without extension",
            parent=self,
        )
        self._meta['/General/original_path'] = StringField(
            value=None,
            description="original file path",
            parent=self,
        )
        self._meta['/General/authors'] = StringField(
            value=None,
            description="authors in LaTeX format, i.e., 'Surname1, Name1 and Surname2, Name2 and ...'",
            parent=self,
        )
        self._meta['/General/notes'] = StringField(
            value=None,
            description="notes which may support rich text (html?)",
            parent=self,
        )
        self._meta['/General/time'] = StringField(
            value=None,
            description="creation time in ISO 8601 format, e.g., '13:29:10'",
            parent=self,
        )
        self._meta['/General/date'] = StringField(
            value=None,
            description="creation date in ISO 8601 format, e.g., '2018-01-28'",
            parent=self,
        )
        self._meta['/General/time_zone'] = StringField(
            value=None,
            description="time zone supported by the python-dateutil library, same as the system",
            parent=self,
        )
        self._meta['/General/doi'] = StringField(
            value=None,
            description="Digital Object Identifier (DOI) of the dataset",
            parent=self,
        )


    def _initializeAcquisitionInstrumentMetaItems(self):
        """
        Initialize the metadata that is under /AcquisitionInstrument
        """
        # Metadata for AcquisitionInstrument/Microscope
        self._meta['/AcquisitionInstrument/Microscope/name'] = StringField(
            value=None,
            description='the name of microscope. e.g. Titan3 Cubed 60-300',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Microscope/manufacturer'] = StringField(
            value=None,
            description='the name of manufacturer of microscope, e.g. FEI',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Microscope/beam_current'] = FloatField(
            value=None,
            unit='A',
            display_unit='nA',
            description='beam current',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Microscope/accelerate_voltage'] = FloatField(
            value=None,
            unit='V',
            display_unit='kV',
            description='accelerating voltage',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Microscope/probe_area'] = FloatField(
            value=None,
            unit='m^2',
            display_unit='nm^2',
            description='probe area',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Microscope/camera_length'] = FloatField(
            value=None,
            unit='m',
            display_unit='mm',
            description='camera length',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Microscope/convergence_angle'] = FloatField(
            value=None,
            unit='rad',
            display_unit='mrad',
            description='convergence semi-angle',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Microscope/magnification'] = FloatField(
            value=None,
            unit=None,
            description='magnification',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Microscope/dwell_time'] = FloatField(
            value=None,
            unit='s',
            display_unit='ms',
            description='dwell time',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Microscope/step_size_i'] = FloatField(
            value=None,
            unit='m',
            display_unit='nm',
            description='step size in i direction',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Microscope/step_size_j'] = FloatField(
            value=None,
            unit='m',
            display_unit='nm',
            description='step size in j direction',
            parent=self,
        )

        # Metadata for AcquisitionInstrument/Camera
        self._meta['/AcquisitionInstrument/Camera/name'] = StringField(
            value=None,
            description='the name of camera, e.g., EMPAD',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Camera/manufacturer'] = StringField(
            value=None,
            description='the name of camera manufacturer, e.g., FEI',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Camera/pixel_number_i'] = IntField(
            value=None,
            description='number of pixels in i direction',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Camera/pixel_number_j'] = IntField(
            value=None,
            description='number of pixels in j direction',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Camera/pixel_size_i'] = FloatField(
            value=None,
            unit='m',
            display_unit='um',
            description='pixel size in i direction',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Camera/pixel_size_j'] = FloatField(
            value=None,
            unit='m',
            display_unit='um',
            description='pixel size in j direction',
            parent=self,
        )

        # Metadata for AcquisitionInstrument/Stage
        self._meta['/AcquisitionInstrument/Stage/tilt_alpha'] = FloatField(
            value=None,
            unit='mrad',
            display_unit='deg',
            description='stage tilt alpha angle',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Stage/tilt_beta'] = FloatField(
            value=None,
            unit='mrad',
            display_unit='deg',
            description='stage tilt beta angle',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Stage/rotation'] = FloatField(
            value=None,
            unit='mrad',
            display_unit='deg',
            description='stage rotation angle',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Stage/x'] = FloatField(
            value=None,
            unit='m',
            display_unit='mm',
            description='stage x position',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Stage/y'] = FloatField(
            value=None,
            unit='m',
            display_unit='mm',
            description='stage y position',
            parent=self,
        )
        self._meta['/AcquisitionInstrument/Stage/z'] = FloatField(
            value=None,
            unit='m',
            display_unit='mm',
            description='stage z position',
            parent=self,
        )