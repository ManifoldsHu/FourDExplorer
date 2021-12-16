# -*- coding: utf-8 -*-
'''
*--------------------------- DataLoaderEMPAD.py ------------------------------*
加载 FEI Electron Microscope Pixel Array Detector (EMPAD) 文件的数据。

由于 4D-STEM 的数据集一般都很大，所以应当使用异步或并发的方式加载。在这里，我们使用生
产者-消费者模型，每次将读取一张衍射图样，并将其放入队列中，以供后续其他线程取用(例如将
这张衍射图样写入 HDF5 文件中，以及实时计算预览的虚拟成像)。

在加载 4D-STEM 数据集之前，应当首先读取其元数据。

作者：          胡一鸣
创建时间：      2021年12月15日
*--------------------------- DataLoaderEMPAD.py ------------------------------*
'''

import threading
import queue
import numpy as np
from bin.Log import LogUtil
import time

logger = LogUtil(__name__)

def readData(
    buffer: queue.Queue, 
    event: threading.Event, 
    shape: tuple,
    raw_path: str,
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
                
                data = np.fromfile(
                    raw_file,
                    dtype = 'float32',
                    count = dp_i * dp_j,
                    sep = '',
                    offset = np.bool(r_ii + r_jj) * 4 * 2 * dp_j
                ).reshape((dp_i, dp_j)).T

                buffer.put((r_ii, r_jj, data), timeout = timeout)

        buffer.put(-1)
        end_time = time.time()
        logger.info('Complete reading. Time consumed: {0}'\
            .format(start_time - end_time))


def readMetaData():
    pass


    