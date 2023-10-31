# -*- coding: utf-8 -*- 

"""
*---------------------------- FourDSTEMManager.py ----------------------------*
管理 .4dstem 数据集的元数据。

注意，只有那些基本的量会被存储，而其他参数将被实时计算。例如，加速电压会被存储，而波长
会则由加速电压导出，从而被实时计算。

元数据会以树状的形式进行存储，其树枝节点用大驼峰的形式命名，而叶子节点则用下划线命名法。
当然，在程序中我们不会使用这个特性来决定一个节点是否为叶子节点。

在实际的操作中，我们期望为每项元数据都提供单独的修改界面，从而规范输入。这需要大量的工
作。

作者：          胡一鸣
创建时间：      2023年10月31日
*---------------------------- FourDSTEMManager.py ----------------------------*
"""

from PySide6.QtCore import (
    QObject,
)



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
        