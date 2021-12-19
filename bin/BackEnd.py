# -*- coding: utf-8 -*-
from bin.BasicIO import HDF5Handler, IOThreadHandler
from bin.Preview import PreviewHandler

class BackEnd:
    
    def __init__(self):
        self.hdf5_handler = HDF5Handler(self)
        self.io_thread_handler = IOThreadHandler(self)
        self.preview_handler = PreviewHandler(self)