# -*- coding: utf-8 -*-

'''
用于预览的类
'''

# from bin.BasicIO import HDF5Handler, IOThreadHandler
# from BackEnd import BackEnd
import queue
import numpy as np
import threading

class PreviewHandler:
    '''
        这里的 PreviewHandler 只能用于本地数据，用于读取、加载数据时进行实时虚
        拟成像，或对已有 HDF5 文件中的 Dataset 生成预览虚拟成像。在开始计算前，
        应当调用 initializePreview 进行初始化。预览的虚拟成像是一种简单的计算，
        只用了收集像素内径 inn_r 和收集像素外径 out_r 两个参数，用以对 preview 
        以及 preview_mask 变量进行修改。这四个变量是多线程共享的，因此在修改时
        必须加锁。
    '''

    def __init__(
        self, 
        backend,
        # hdf5handler: HDF5Handler, 
        # io_thread_handler: IOThreadHandler
    ):
        # self.hdf5_handler = hdf5handler
        # self.io_thread_handler = io_thread_handler
        self._backend = backend
        self._lock = threading.Lock()
        self._buffer = queue.Queue(maxsize=1024)

        self.preview = None
        self.preview_mask = None
        self.preview_max = 0
        self.preview_min = 0
        self.inn_r = 0
        self.out_r = 0

    @property
    def preview_buffer(self):
        return self._buffer

    def setInnerRadius(self, inn_r):
        if not isinstance(inn_r, (int, float)):
            raise TypeError('inn_r must be an int or a float!')
        self.inn_r = inn_r
        self.setPreviewMask()

    def setOuterRadius(self, out_r):
        if not isinstance(out_r, (int, float)):
            raise TypeError('out_r must be an int or a float!')
        self.out_r = out_r
        self.setPreviewMask()

    def _initializePreview(self):
        if self._backend.hdf5_handler.shape == None:
            return
        else:
            scan_i, scan_j, dp_i, dp_j = self._backend.hdf5_handler.shape
        self.preview = np.zeros((scan_i, scan_j))
        self.setPreviewMask()
        # scan_i, scan_j, dp_i, dp_j = self.hdf5_handler.shape
        # self.preview = np.zeros((scan_i, scan_j))
        # self.setPreviewMask()
        # self.preview_mask = np.zeros((dp_i, dp_j))

    def calculatePreview(
          self, 
          timeout = None,
    ):
        '''
        传入一个队列作为缓冲区，与主线程 (事件循环) 共享变量 preview_mask 以及
        preview 。主线程根据事件调整 preview_mask 的计算，同时每隔一定时间渲染
        一次 preview。当 buffer 中传来终止符，该线程停止循环。
        '''
        # if not isinstance(buffer, queue.Queue):
        #     raise TypeError('buffer must be a queue.Queue object')
        # scan_i, scan_j, dp_i, dp_j = self.hdf5_handler.shape
        self._initializePreview()
        while True:
            tmp = self._buffer.get(timeout=timeout)
            if tmp == -1:
                break
            # elif not self.preview_event.is_set():
                # self.preview_event.wait()
            else:
                r_ii, r_jj, data = tmp
                preview_pixel = np.sum(data*self.preview_mask)
                with self._lock:
                    self.preview[r_ii, r_jj] = preview_pixel
                    if preview_pixel > self.preview_max:
                        self.preview_max = preview_pixel
                    if self.preview_min == 0:
                        self.preview_min = preview_pixel
                    elif self.preview_min > 0 and \
                            self.preview_min > preview_pixel:
                        self.preview_min = preview_pixel

        
    def setPreviewMask(self):
        if self._backend.hdf5_handler.shape == None:
            return 
        else:
            scan_i, scan_j, dp_i, dp_j = self._backend.hdf5_handler.shape
        mask = np.zeros((dp_i, dp_j))
        c_i = (dp_i - 1)/ 2
        c_j = (dp_j - 1)/ 2
        for q_ii in range(dp_i):
            for q_jj in range(dp_j):
                q_sq = (q_ii - c_i)**2 + (q_jj - c_j)**2
                mask[q_ii, q_jj] = \
                    (q_sq >= self.inn_r**2) and (q_sq <= self.out_r**2)
        with self._lock:
            self.preview_mask = mask
            


    def viewDataset(self):
        self.view_dataset_thread = threading.Thread(
            target = self._backend.hdf5_handler.loopDataset,
            args = (self._buffer)
        )
        self.view_dataset_thread.start()
        
        
        