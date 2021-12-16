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
    logger.info('Start reading from the EMPAD raw file:\n{0}'.format(raw_path))
    start_time = time.time()
    scan_i, scan_j, dp_i, dp_j = shape
    with open(raw_path, 'rb') as raw_file:
        raw_file.seek(0)
        for r_ii in range(scan_i):
            for r_jj in range(scan_j):
                if not event.is_set():
                    event.wait()
                
                # Between every diffraction pattern, two lines need to be given 
                # up. So the offset is dp_j (pixels) x 2 (lines) x 4 (bytes).
                # But the offset does not exist at the beginning of the file,
                # so we calculate np.bool(r_ii + r_jj) to evaluate if the poin-
                # ter is at the first diffraction pattern.
                data = np.nan_to_num(np.fromfile(
                    raw_file,
                    dtype = 'float32',
                    count = dp_i * dp_j,
                    sep = '',
                    offset = np.bool(r_ii + r_jj) * 4 * 2 * dp_j
                ))
                
                if is_flipped:
                    data = data.reshape((dp_i, dp_j)).T
                else:
                    data = data.reshape((dp_i, dp_j))

                buffer.put((r_ii, r_jj, data), timeout = timeout)

        # end flag
        buffer.put(-1)
        end_time = time.time()
        logger.info('Complete reading. Time consumed: {0}'\
            .format(start_time - end_time))


def readMetaData(xml_path: str) -> dict:
    '''
    解析 EMPAD 产生的数据集中 xml 文件的函数。
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
    #       定量化的标定、计算，就要手动更改相应的元数据。
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




    