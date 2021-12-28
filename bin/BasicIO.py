# -*- coding utf-8 -*-

'''
*--------------------------------- BasicIO.py ---------------------------------*
对 HDF5 文件进行读取与写入的操作。

4dExplorer 软件默认使用 HDF5 进行四维数据及其元数据的管理。对于其他格式的文件，例如由
EMPAD 所产生的数据，4dExplorer 将其转换为hdf5进行管理并生成临时文件，用户可自行决定是
否要保存该临时文件为 HDF5 数据集。出于对内存空间资源节约的考虑，所有有关四维数据的计算
都是基于硬盘 IO 的，而在代码层面上不会将数据一次性全部读入内存中(尽管操作系统会尝试这样
做，但即使是内存空间不足，也无需担心会对性能造成影响。)

这样，对于由仪器采集而来的数据，使用 4dExplorer 软件进行数据读取的步骤就是：
     - 在某个文件夹内创建临时 HDF5 数据文件，该文件的主要部分是原四维数据的副本；
     - 根据 HDF5 的特性进行内存映射；
     - 校正与分析，结果都将存储于 HDF5 文件中；
     - 输出分析结果；
     - 保存或删除 HDF5 文件。

在这样的工作流程中，将四维数据复制一份的时间代价较大。为节约后续分析的时间，可以保存 HDF5 
文件，后续重新打开该数据集时可直接建立内存映射，省下加载四维数据的时间开销。在后续打开时，
就将直接调用 BasicIO.py 中的代码。


作者：          胡一鸣
创建时间：      2021年8月21日

Basic IO operation of HDF5 files.

By default, the 4dExplorer software uses HDF5 to manage 4d data and metadata. 
For other files, such as the data generated by EMPAD, 4dExplorer converts them 
to HDF5 for management and generates temporary files. Users can decide whether 
to save the temporary files as HDF5 data sets or not. In order to save memory 
resources, all computation of the four-dimensional data is based on disk IO, a-
nd the data is not read into memory all at once at the code level (although the 
operating system will try to do this, there is no need to worry about the perf-
ormance impact of running out of memory).

In this way, for the data collected by the specific instrument, the steps of u-
sing 4dExplorer software to read the data are as follows:
      - Create a temporary HDF5 data file in some folder, the main part of whi-
        ch is a copy of the original 4-dimensional data;
      - Memory mapping based on HDF5 features;
      - Calibration and analysis, the results will be stored in the HDF5 file;
      - Output the analysis result;
      - save or delete the HDF5 file.

In such a workflow, the time cost of making a copy of the four-dimensional data 
is large. In order to save the time of subsequent analysis, the HDF5 file can 
be saved, and the memory mapping can be directly established when the data set 
is reopened, saving the time cost of loading the four-dimensional data. On sub-
sequent opens, the code in basicio.py is called directly.

author:             Hu Yiming
date:               Aug 21, 2021

All rights reserved.
                                                                               

*--------------------------------- BasicIO.py ---------------------------------*
'''


import os
import sys
ROOTPATH = os.path.dirname(__file__)    # Root path of the software
if not ROOTPATH in sys.path:
    sys.path.append(ROOTPATH)


import h5py
import numpy as np

from datetime import datetime
import threading
import queue
import time


from bin.Log import LogUtil
import traceback
logger = LogUtil(__name__)

from bin import DataReaderEMPAD
# from bin.BackEnd import BackEnd
# from bin.Preview import PreviewHandler

class HDF5Handler:
     '''
          使用HDF5文件处理的封装类。其应当包含以下方法：
                - 设置指向的h5文件的路径
                - 创建h5文件并初始化
                - 读取h5文件，对不合规的文件进行初始化
                - 删除h5文件            # 安全性问题？
                - 填充dataset
                - 填充attributes
                - 读取dataset
                - 读取attributes
          
          初始化完成的h5文件应当有如下结构：

          /Dataset                                四维数据集。

          /Calibration                            作为Group，其Attribution内有各种
                                                  校正操作类。

          /Reconstruction                         作为Group，储存每一次的计算结果

          /Reconstruction/1_iCoM/Matrix           某一次重构的计算结果，作为二维矩阵。
                                                  其Attribute包含了数据类型、计算类
                                                  型、计算参数、计算时所使用的Cali-
                                                  bration配置。“1_iCoM”指的是计算任
                                                  务名字，其为“数字-算法”的结构。

          /Reconstruction/1_iCoM/1_imshow         作为Group，其Attribution保存的是
                                                  封装的画图类，储存了对这次重构得到
                                                  的结果进行画图所使用的参数。

          /tmp                                    临时数据，用来保存当Calibration不
                                                  变时，上一次计算得到的CoM矢量，及其
                                                  他未来可能出现的中间结果。关闭时应
                                                  当删除该Group下所有数据。

          
          This is the encapsulated classes that use HDF5 file processing. It s-
          hould contain the following methods:    
                - set the path of the h5 file,
                - create the h5 file and initialize,
                - read the h5 file, and initialize those invalid files,
                - delete the h5 file (will be used to delete temp files),
                - load dataset,
                - load attributes,
                - read dataset,
                - and set the attributes of dataset

          An initialized h5 file should have the following structure:

          /Dataset                                Four-dimensional data set

          /Calibration                            As a group, there are various 
                                                  calibration classes inside its 
                                                  attribution

          /Reconstruction                         As a group, each calculation 
                                                  are saved here

          /Reconstruction/1_iCoM/Matrix           The result of a reconstructi-
                                                  on, as a two-dimensional mat-
                                                  rix. Attribute contains the 
                                                  data type, calculation type, 
                                                  calculation parameters, and 
                                                  the Calibration configuration 
                                                  used in the calculation.  
                                                  "1_iCoM" is the name of the 
                                                  calculation task, which is a 
                                                  "number-algorithm" structure.  

          /Reconstruction/1_iCoM/1_imshow         As a Group, its attribution 
                                                  preserves the encapsulated d-
                                                  rawing class that stores the 
                                                  parameters to use to draw the 
                                                  results of the matrix. 

          /tmp                                    Temporary group, used to sto-
                                                  re the CoM vector from the l-
                                                  ast calculation when the Cal-
                                                  ibration is unchanged, as we-
                                                  ll as other intermediate res-
                                                  ults that may occur in the f-
                                                  uture. When closing, all data 
                                                  in this Group should be dele-
                                                  ted.
     '''


     def __init__(self, backend):
          '''
          arguments           type                description
          ---------------------------------------------------------------------
          backend             BackEnd             a handle of backend
          ---------------------------------------------------------------------
          '''
          self._backend = backend
          # self.has_file = False
          self._file = None
          self._path = ''
          self._lock = threading.Lock()
          
          



     @property
     def path(self):
          return self._path

     @path.setter
     def path(self, value: str):
          '''
          Set the h5 file path. Will close the current file.

          arguments           type                description
          ---------------------------------------------------------------------
          value               str                 the absolute path of the new 
                                                  h5 file
          ---------------------------------------------------------------------
          '''
          if not isinstance(value, str):
               raise TypeError('Expected a string.')
          if value != self.path and self.isFileOpened():
               self.file.close()

          self._path = value


     def isPathValid(self) -> bool:
          '''
          Return if the file is a valid h5 file.
          '''
          try:
               with h5py.File(self.path, mode = 'r') as file:
                    is_valid = isinstance(file, h5py.File)
               return is_valid
          except OSError as e:
               # logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
               return False
          
     
     @property
     def file(self):
          return self._file

     @file.setter
     def file(self, value):
          '''
          Set the h5 file.

          arguments           type                description
          ---------------------------------------------------------------------
          value               h5py.File           Must be h5py.File object or 
                                                  None.
          ---------------------------------------------------------------------
          '''
          if value == None or isinstance(value, h5py.File):
               self._file = value
          else:
               raise TypeError('file must be a h5py.File or None.')
               

     @property
     def shape(self):    # the shape of dataset, (scan_i, scan_j, dp_i, dp_j)
          if self.isFileOpened():
               if 'Dataset' in self.file:
                    scan_i = self.file['Dataset'].attrs['scan_i']
                    scan_j = self.file['Dataset'].attrs['scan_j']
                    dp_i = self.file['Dataset'].attrs['dp_i']
                    dp_j = self.file['Dataset'].attrs['dp_j']
                    return (scan_i, scan_j, dp_i, dp_j)
          return None

     
     @property
     def is_flipped(self):    
          # Return if raw_data is flipped. When it is True, every diffraction 
          # pattern should be transposed when reading.
          if self.isFileOpened():
               if 'Dataset' in self.file:
                    if 'is_flipped' in self.file['Dataset'].attrs:
                         is_flipped = self.file['Dataset'].attrs['is_flipped']
                         return is_flipped
          return False


     def createFile(self) -> str:
          '''
          Create a new standard h5 file. Read/write the current file if there 
          exists a file.
          '''
          try:
               with h5py.File(self.path, mode = 'w-') as file:   # create, fail if exists
                    self._initializeFile(file)
          except OSError as e:
               logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
               return ''
          return self.path


     def _initializeFile(self, file):
          '''
          Initialize a h5 file. Some groups and attributes will be added.

          arguments           type                description
          ---------------------------------------------------------------------
          file                h5py.File           
          ---------------------------------------------------------------------
          '''
                    
          if 'Reconstruction' not in file:
               file.create_group('Reconstruction')
          if 'Calibration' not in file:
               file.create_group('Calibration')
          if 'tmp' not in file:
               file.create_group('tmp')

          root = file['/']
          root.attrs['4dExplorer'] = True
          root.attrs['FileCreateTime'] = '{0}'.format(datetime.now)
          root.attrs['Version'] = '0.5'
          
     
     def openFile(self):
          '''
          Read a h5 file. Fail if there is no file corresponding to the path. 
          The file must be read before it is handled by BasicIO modules.
          '''
          try:
               if not self.isFileOpened():
                    # Read/write, file must exist
                    self.file = h5py.File(self.path, mode='r+')  
          except OSError as e:
               logger.error('{0}\n{1}'.format(e, traceback.format_exc()))
               return None
          return self.file


     def closeFile(self):
          '''
          Close the h5 file. The file must be closed before:
               - the path is changed
               - the file is deleted
               - the application is exit
          '''
          if self.isFileOpened():
               self.file.close()
          self.file = None
          

     def isFileOpened(self):
          '''
          Return if the hdf5 file is opened.
          '''
          if self.file is None:
               return False
          if self.file.id: 
               # It seems in h5py they use this to estimate if the file is closed.   
               return True
          else:
               return False


     def deleteFile(self):
          '''
          Delete the h5 file. Fail if there is no file.
          '''
          if self.isFileOpened():
               self.file.close()
          if self.isPathValid():
               try:
                    os.remove(self.path)
               except OSError as e:
                    logger.error('{0}\n{1}'.format(e, traceback.format_exc()))


          
     def createDataset(self, shape: tuple, dtype = 'float32', chunks = None,):
          '''
          Create a four-dimensional dataset. The dataset must be created before 
          loaded.

          
          arguments           type                description
          ---------------------------------------------------------------------
          shape               tuple               Must be (scan_i, scan_j, dp_i, 
                                                  dp_j)

          dtype               str                 Data type of the dataset

          ischunked           bool                Set the dataset if it is chu-
                                                  nk stored.
          ---------------------------------------------------------------------
          
          '''
          if not isinstance(shape, tuple):
               raise TypeError('shape must be a tuple with the lenth 4.')
          elif len(shape) != 4:
               raise TypeError('shape must be a tuple with the lenth 4.')

          scan_i, scan_j, dp_i, dp_j = shape
          success = False


          if self.isFileOpened():
               if 'Dataset' in self.file:
                    logger.warning('There has been dataset in the file.'\
                             + ' No new dataset is created.')
               else:
                    Dataset = self.file.create_dataset(
                         'Dataset', 
                         shape = shape, 
                         dtype = dtype, 
                         chunks = chunks,
                    )
                    self.setDatasetAttribute('scan_i', scan_i,)
                    self.setDatasetAttribute('scan_j', scan_j,)
                    self.setDatasetAttribute('dp_i', dp_i)
                    self.setDatasetAttribute('dp_j', dp_j)
                    success = True
          else:
               logger.warning('File must be opened before creating Dataset.')
          return success


     def writeDataset(self, pos: tuple, data: np.ndarray):
          '''
          Write data into the four-dimensional dataset. Basically, the pos arg-
          ument will be a tuple with two elements, (scan_i, scan_j). While the 
          shape of loaded matrix will be (dp_i, dp_j). Only one diffraction pa-
          ttern will be loaded at a time, in order to save memory.
          

          arguments           type                description
          ---------------------------------------------------------------------
          pos                 tuple               Must be (ii, jj) where 
                                                  0 <= ii < scan_i and 
                                                  0 <= jj < scan_j .

          data                numpy.ndarray       The matrix that will be copi-
                                                  ed into the dataset
          ---------------------------------------------------------------------
          '''
          with self._lock:
               self.file['Dataset'][pos[0],pos[1],:,:] = data

     
     def deleteDataset(self) -> bool:
          '''
          Delete the four-dimensional dataset in the file.
          '''
          if not self.isFileOpened():
               logger.warning('File must be opened before deleting dataset.')
               return False
          if self.file['Dataset']:
               del self.file['Dataset']
               return True
          else:
               logger.warning('There is no Dataset in the file.')
               return False


     def loopDataset(self, buffer: queue.Queue,):
          '''
          Loop the whole dataset, and put one diffraction pattern into the buf-
          fer each time. Designed to run in another thread instead of the main 
          thread.
          '''
          scan_i, scan_j, dp_i, dp_j = self.shape
          dataset = self.file['Dataset']
          for r_ii in range(scan_i):
               for r_jj in range(scan_j):
                    with self._lock:
                         buffer.put(r_ii, r_jj, dataset[r_ii, r_jj])
          buffer.put(-1)


     def setDatasetAttribute(self, key: str, value):
          '''
          Set the Dataset attribute. The Dataset must be created before setting
          the attributes.

          arguments           type                description
          ---------------------------------------------------------------------
          key                 str                 Dataset attribution

          value                                   the value of the Dataset att-
                                                  ribution. Most likely it sho-
                                                  uld not be too large in size.
          ---------------------------------------------------------------------
          '''
          if self.isFileOpened():
               if 'Dataset' in self.file:
                    Dataset = self.file['Dataset']
                    if isinstance(key, str):
                         Dataset.attrs[key] = value
               else:
                    logger.warning('There is no Dataset in the file.')
          else:
               logger.warning('File must be opened before setting attributes' \
                   + ' of Datasets.')


     def deleteDatasetAttribute(self, key: str):
          '''
          Delete the Dataset attribute. The Dataset must exist.

          arguments           type                description
          ---------------------------------------------------------------------
          key                 str                 Dataset attribution
          ---------------------------------------------------------------------
          '''
          if self.isFileOpened():
               if 'Dataset' in self.file:
                    Dataset = self.file['Dataset']
                    if key in Dataset.attrs:
                         del Dataset.attrs[key]
               else:
                    logger.warning('There is no Dataset in the file')
          else:
               logger.warning('File must be opened before setting attributes' \
                    ' of Dataset.')


     def traverseAllNodes(self) -> list:
          '''
          将 HDF5 文件中的 groups 和 datasets 遍历地显示出来。

          Traverse the groups and datasets in the HDF5 file.
          '''
          nodelist = []
          def appendAllNodes(node, nodelist):
               nodelist.append(node)
               if isinstance(node, h5py.Group):
                    for keys in node:
                         appendAllNodes(node[keys], nodelist = nodelist)
          appendAllNodes(self.file['/'], nodelist = nodelist)
          return nodelist


     



class IOThreadHandler:
     '''
          使用生产者-消费者模型的线程管理器，用于管理写入 HDF5 四维数据的IO行为。一般而
          言，写入四维数据的情形分为以下两种：
               - 本地存储的四维数据集；
               - 其他进程(例如由局域网连接的相机)不断生成的数据流。

          在读取、填入四维数据之前，应当首先确保：
               - 已经创建好了 HDF5 文件并打开
               - 先行读取四维数据的元数据，并填入 HDF5 文件中。
               - 根据元数据，创建好 HDF5 文件中的 Dataset
          
          在要读取其他进程生成的数据流时，要是中途改变 shape 和 is_flipped，则应当删除
          已经创建了的 Dataset，然后重新创建 Dataset。或者，也可以保存修改之前的 HDF5 
          文件，然后重新建立新的文件，并读取数据。在 GUI 中，除非重新加载，否则用户不能
          直接修改 shape 和 is_flipped。

          此外，还要开一个线程用于计算预览的虚拟成像。其将根据主线程发送的信号 (比如虚拟
          成像对应收集角的范围) 来实时地计算虚拟成像，并将其填入主线程的变量 preview 中。
          注意，这个线程只能用来在本地读取数据的时候进行计算。如果想要使用监视器，请使用
          Monitor 模块内的线程。
     '''
     def __init__(self, backend):
          self._load_buffer = queue.Queue(maxsize=16384)
          self._loading_event = threading.Event()
          self._reading_event = threading.Event()
          self._backend = backend
          # self._preview_buffer = queue.Queue(maxsize=1024)
          # self.hdf5_handler = backend.hdf5_handler
          # self.preview_handler = backend.preview_handler
          
     
     def loadingData(self, data_reader: str, raw_path: str):
          
          # 写入 HDF5 数据的线程
          self.loading_thread = threading.Thread(
               target = self.loadFromBuffer,
               args = (
                    self._load_buffer, 
                    self._backend.preview_handler.preview_buffer,
                    self._loading_event, 
                    None,
               ),
               name = 'WriteHDF5Dataset',
          )

          # 本地读取 EMPAD 数据的线程
          shape = self._backend.hdf5_handler.shape
          is_flipped = self._backend.hdf5_handler.is_flipped

          if data_reader == 'EMPAD':
               self.reading_thread = threading.Thread(
                    target = DataReaderEMPAD.readData,
                    args = (
                         self._load_buffer, 
                         self._reading_event,
                         raw_path,
                         shape, 
                         is_flipped,
                         None,
                    ),
                    name = 'ReadEMPAD',
               )
          
          # 计算预览图的线程
          self.previewing_thread = threading.Thread(
               target = self._backend.preview_handler.calculatePreview,
               args=(None,)
          )

          self.reading_thread.start()
          self.loading_thread.start()
          self.previewing_thread.start()

          self._loading_event.set()
          self._reading_event.set()
          

          
     def loadFromBuffer(
          self, 
          buffer_read: queue.Queue, 
          buffer_preview: queue.Queue,
          event: threading.Event, 
          timeout = None
     ):
          '''
          传入一个队列作为缓冲区，从缓冲区中不断地读取数据，并且写入到 HDF5 文件中。
          当 buffer 中传来终止符，停止写入，break 循环。

          This function is passed a queue as a buffer, always reads data from 
          the buffer, and writes them into the HDF5 file. When there is a flag
          as a terminator from the buffer, the loop breaks. 

          arguments           type                description
          ---------------------------------------------------------------------
          buffer              queue.Queue         A queue as a buffer. The data
                                                  from this queue are tuples p-
                                                  ickled as
                                                  (int, int, np.ndarray)
                                                  where in default mean
                                                  (ii, jj, Dataset[ii,jj,:,:]).

                                                  The end flag is -1.

          event               threading.Event     A flag managed by the main t-
                                                  hread.          
          ---------------------------------------------------------------------
          '''
          
          start_time = time.time()
          if not isinstance(buffer_read, queue.Queue):
               raise TypeError('buffer must be a queue.Queue object')
          if not isinstance(buffer_preview, queue.Queue):
               raise TypeError('buffer must be a queue.Queue object')

          logger.info('Start loading data into HDF5 file:\n{0}'\
               .format(self._backend.hdf5_handler.path))

          while True:
               tmp = buffer_read.get(timeout = timeout)
               buffer_preview.put_nowait(tmp)
               if tmp == -1:
                    end_time = time.time()
                    # logger.info('Loading completes. Time consumed: {0} s'\
                         # .format(end_time - start_time))
                    break
               elif not event.is_set():
                    event.wait()
               else:
                    r_ii, r_jj, data = tmp
                    if isinstance(data, np.ndarray):
                         self._backend.hdf5_handler.writeDataset((r_ii, r_jj), data)
                    
     
     


          