# -*- coding: utf-8 -*-
'''
*--------------------------- DataLoaderEMPAD.py ------------------------------*
加载 FEI Electron Microscope Pixel Array Detector (EMPAD) 文件的数据。

由于 4D-STEM 的数据集一般都很大，所以应当使用异步或并发的方式加载。在这里，我们使用生
产者-消费者模型，每次将读取一张衍射图样，并将其放入队列中，以供后续其他线程取用(例如将
这张衍射图样写入 HDF5 文件中，以及实时计算预览的虚拟成像)。

在加载 4D-STEM 数据集之前，应当首先读取其元数据，然后如果此时没打开 HDF5 文件，就应当
创建或打开一个 HDF5 文件，并将读取的元数据填入 HDF5 文件中。然后，根据元数据创建 HDF5
文件中的 Dataset。最后，才根据元数据(主要是 shape 以及 is_flipped)读取 4D-STEM 的原
始数据

作者：          胡一鸣
创建时间：      2021年12月15日

To load the data from the file produced by FEI Electron Microscope Pixel Array 
Detector (EMPAD).

Due to the large size of 4D-STEM datasets, reading the whole data into memories 
is time-consuming. So we usually use asynchronous and concurrent IO method to 
load them. Here, we use a simple producer-consumer model, and start a thread to 
read one diffraction pattern every time. The thread puts it into a queue, and 
then another thread gets the pattern from the queue and write it into the Data-
set in HDF5 file.

Before loading 4D-STEM dataset, we first read the metadata. If there is no HDF5
file opened, we create or open a HDF5 file, write the metadata, and then create 
Dataset in the HDF5 file according to the metadata. At last, after all these p-
reparation, we call readData() to read 4D-STEM dataset.

author:             Hu Yiming
date:               Dec 12, 2021

All rights reserved.
*--------------------------- DataLoaderEMPAD.py ------------------------------*
'''

import threading
import queue
import numpy as np
from bin.Log import LogUtil
import time
from xml.dom.minidom import parse

logger = LogUtil(__name__)

def readData(
    buffer: queue.Queue, 
    event: threading.Event, 
    raw_path: str,
    shape: tuple,
    is_flipped: bool,
    timeout = None,
):
    '''
        Read data from .raw files produced by EMPAD. This function is designed 
        according to producer-consumer model, and works asynchoronously. Every 
        time it reads one diffraction pattern, and put it into the buffer (whi-
        ch is a queue) immediately. To receive the data, we need another thread 
        that get items from buffer and load them into a four-dimensional matrix 
        (usually, the HDF5 dataset). 

        Everytime a tuple will be put into the buffer like this:
        (r_ii, r_jj, data)
        where r_ii and r_jj are the index of the diffraction pattern, which in-
        dicate the location of the scanning point in the real space.

        In the end, a integer -1 will be put into the buffer to note the main 
        thread that reading data has been completed.

        This function also accept a threading.Event object as an argument, whi-
        ch is used to receive pause signal from the main thread. When the event 
        is set to False (calling event.clear()) by the main thread, this funct-
        ion will keep sleeping until it is set to True (calling event.set()).

        This function is used in multithreading environment. If we want use mu-
        ltiprocessing io, simply use a pipe instead of event to communicate be-
        tween processes.

        Between every diffraction pattern, two lines need to be given up. So t-
        he offset is dp_j (pixels) x 2 (lines) x 4 (bytes). But the offset does 
        not exist at the beginning of the file, so we calculate 
        np.bool(r_ii + r_jj) to evaluate if the pointer is at the first diffra-
        ction pattern.

        arguments       type            description
        -----------------------------------------------------------------------
        buffer          queue.Queue         A queue that puts a tuple like
                                            (r_ii, r_jj, data)
                                            every time. In the end, use -1 as 
                                            the flag to inform the main thread.

        event           threading.Event     A flag controlled by the main thre-
                                            ad. This function will wait if eve-
                                            nt is set to False, until it is set
                                            to True.

        raw_path        str                 The file path of raw data.

        shape           tuple               The shape of 4D-STEM dataset, like
                                            (scan_i, scan_j, dp_i, dp_j)

        is_flipped      bool                Indicating whether the diffraction
                                            pattern need to be transposed befo-
                                            re put into the buffer.

        time_out        float or None       [Optional] If the buffer is full f-
                                            or a long time, longer than time_out, 
                                            then it will raise Full exception.
                                            If time_out = None, this function 
                                            will always wait (be blocked) until
                                            the buffer is not full.
        -----------------------------------------------------------------------
            
    '''
    
    logger.info('Start reading from the EMPAD raw file:\n{0}'.format(raw_path))
    start_time = time.time()
    scan_i, scan_j, dp_i, dp_j = shape
    with open(raw_path, 'rb') as raw_file:
        raw_file.seek(0)
        if is_flipped:
            for r_ii in range(scan_i):
                for r_jj in range(scan_j):
                    if not event.is_set():
                        event.wait()
                    data = np.nan_to_num(np.fromfile(
                        raw_file,
                        dtype = 'float32',
                        count = dp_i * dp_j,
                        sep = '',
                        offset = np.bool(r_ii + r_jj) * 4 * 2 * dp_j
                    )).reshape((dp_i, dp_j)).T
                    buffer.put((r_ii, r_jj, data), timeout = timeout)

        else:
            for r_ii in range(scan_i):
                for r_jj in range(scan_j):
                    if not event.is_set():
                        event.wait()
                    data = np.nan_to_num(np.fromfile(
                        raw_file,
                        dtype = 'float32',
                        count = dp_i * dp_j,
                        sep = '',
                        offset = np.bool(r_ii + r_jj) * 4 * 2 * dp_j
                    )).reshape((dp_i, dp_j))
                    buffer.put((r_ii, r_jj, data), timeout = timeout)

        # end flag
        buffer.put(-1)
        end_time = time.time()
        logger.info('Complete reading. Time consumed: {0}'\
            .format(start_time - end_time))


def readMetaData(xml_path: str) -> dict:
    '''
        解析 EMPAD 产生的 xml 文件的函数。返回一个包含元数据的字典。该字典中包含：

        acquire_time                                str
    *   raw_file_name                               str
    *   scan_i                                      int
    *   scan_j                                      int
    *   dp_i                                        int
    *   dp_j                                        int
    ^   voltage                                     Unit: V
    ^   camera_length                               Unit: m
    ^   dk_i                                        Unit: rad
    ^   dk_j                                        Unit: rad
        scan_scope_ratio_compared_to_HAADF          float
        scan_scope_HAADF_i                          Unit: m
        scan_scope_HAADF_j                          Unit: m
        scan_scope_i                                Unit: m
        scan_scope_j                                Unit: m
    ^   dr_i                                        Unit: m
    ^   dr_j                                        Unit: m
    ^   scan_rotation                               Unit: rad
    *   is_flipped                                  bool

        其中标了 * 的，是读取 4D-STEM 数据必备的、也是最为基础的信息。如果这几个元数
        据读取失败或者有误，用户[必须]在读取数据前就手动正确填写、修改，而在数据读取完
        毕后就无法更改。
        
        而其中标了 ^ 的，则是用于图像校正、定量的重要参数，这些由机器读取的数据未必可
        靠。为了得到正确的图像及定量化结果，用户[应当]小心校准、更改这些数据。
        
        其他元数据则不用于后续计算，但为了实验数据的完整性，我们[建议]用户正确填写这些
        数据。

        Parse the .xml file produced by EMPAD. Return a dict with metadata. Th-
        is function returns a dict contains the metadata of 4D-STEM dataset. T-
        hey are listed above. 
        
        Among all the items, those with * are the base parameters that will be 
        passed to read the .raw dataset. If these items are not parsed success-
        fully or there are errors, users MUST first correct them manually. Aft-
        er the Dataset is loaded, these parameters are not allowed to change. 
        
        Those with ^ script are the parameters that are significant to calibra-
        tion and quantification, so users SHOULD carefully calibrate and corre-
        ct them manually, in order to get accurate experimental results. 
        
        Others are not used to calculation later, but for data integrity users 
        are SUGGESTED to correct them.

        arguments           type            description
        -----------------------------------------------------------------------
        xml_path            str             The file path of xml data.
        -----------------------------------------------------------------------
        '''
    DOMTree = parse(xml_path)
    root = DOMTree.documentElement
    meta = {}

    # meta['scan_i'] = int(root.getElementsByTagName('pix_y')[0].childNodes[0].data)
    # meta['scan_j'] = int(root.getElementsByTagName('pix_x')[0].childNodes[0].data)

    meta['acquire_time'] = root.getElementsByTagName('timestamp')[0].getAttribute('isoformat')
    meta['raw_file_name'] = root.getElementsByTagName('raw_file')[0].getAttribute('filename')

    scan_parameters = root.getElementsByTagName('scan_parameters')
    for mode in scan_parameters:
        if mode.getAttribute('mode') == 'acquire':
            # The shape of 4D-STEM Dataset is (scan_i, scan_j, dp_i, dp_j)
            meta['scan_i'] = int(mode.getElementsByTagName('scan_resolution_y')[0].childNodes[0].data)
            meta['scan_j'] = int(mode.getElementsByTagName('scan_resolution_x')[0].childNodes[0].data)
            scan_size = float(mode.getElementsByTagName('scan_size')[0].childNodes[0].data)

    # The default size of one diffraction pattern of EMPAD is 128 x 128.
    meta['dp_i'] = 128
    meta['dp_j'] = 128

    
    iom_measurements = root.getElementsByTagName('iom_measurements')[0]
    
    # Accelerate voltage of the electron beam. Unit: V
    meta['voltage'] = float(iom_measurements.getElementsByTagName('source.get_voltage')[0].childNodes[0].data)

    # Camera Length of the beam path. Unit: m
    meta['camera_length'] = float(iom_measurements.getElementsByTagName('optics.get_cameralength')[0].childNodes[0].data)

    # dk here is the length of one pixel in the reciprocal space (diffraction 
    # space). Unit: rad
    dk = float(iom_measurements.getElementsByTagName('calibrated_diffraction_angle')[0].childNodes[0].data)
    meta['dk_i'] = dk
    meta['dk_j'] = dk

    # full_view_str is like '[1.85753e-08, 1.85753e-08]', which is a string.
    full_view_str = iom_measurements.getElementsByTagName('optics.get_full_scan_field_of_view')[0].childNodes[0].data
    
    # This is the raio between the full scanning lengths acquired by EMPAD and 
    # by companioned traditional HAADF. 
    # NOTE: 南京大学的 FEI TITAN 的真实比值应该是这里的两倍。也就是说，EMPAD 的扫描
    #       边长为 scan_size x scan_scope_HAADF x 2 ，所以在读取完成后，如果要做
    #       定量化的标定、计算，就要记得手动更改相应的元数据。
    meta['scan_scope_ratio_compared_to_HAADF'] = scan_size
    

    meta['scan_scope_HAADF_i'] = float(full_view_str.split(',')[1][0:-1])
    meta['scan_scope_HAADF_j'] = float(full_view_str.split(',')[0][1:])

    # scan_scope_i and scan_scope_j are the full scanning lengths acquired by 
    # EMPAD. Unit: m
    meta['scan_scope_i'] = meta['scan_scope_HAADF_i'] * scan_size
    meta['scan_scope_j'] = meta['scan_scope_HAADF_j'] * scan_size

    # dr_i and dr_j here are the length of one pixel in the real space (specim-
    # en space). Sometimes these parameters need careful calibration. Unit: m
    meta['dr_i'] = meta['scan_scope_i'] / meta['scan_i']
    meta['dr_j'] = meta['scan_scope_j'] / meta['scan_j']

    # There is usually an angular offset between the specimen plane and the ca-
    # mera plane. It has at least two causes: 
    #    - the scanning path may not be parallel to the side of the camera,
    #    - and due to magnetic lens, the electron beam proceeds spiral motion.
    # We call the first cause the scanning rotation, and the second cause the 
    # pattern rotation. Usually in microscopy the scanning rotation can be set 
    # by users, and the pattern rotation has already been set to zero by engin-
    # eers. However, there are cases in which they are not known and need care-
    # ful calibration, so we provide some algorithms to do that.
    meta['scan_rotation'] = float(iom_measurements.getElementsByTagName('column.get_scanrotation')[0].childNodes[0].data)

    # For FEI EMPAD, the chirality of the coordinates of diffraction patterns 
    # is different from the scanning path. So when meta[is_flipped] is set to 
    # True, every diffraction pattern is set to be transposed.
    meta['is_flipped'] = True

    return meta




    