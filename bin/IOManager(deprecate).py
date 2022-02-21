# -*- coding: utf-8 -*-


''' Deprecated '''




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
                    
     
class DataCubeManager(object):
    """
    管理 4D-STEM DataCube 的 Manager。
    """
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

          
    def createDataset(self, shape: tuple, dtype = 'float32', chunks = None,):
        '''
        Create a four-dimensional dataset. The dataset must be created before 
        loaded.

          
        arguments           type                description
        -----------------------------------------------------------------------
        shape               tuple               Must be (scan_i, scan_j, dp_i, 
                                                dp_j)

        dtype               str                 Data type of the dataset

        ischunked           bool                Set the dataset if it is chu-
                                                nk stored.
        -----------------------------------------------------------------------
          
        '''
        if not isinstance(shape, tuple):
            raise TypeError('shape must be a tuple with the lenth 4.')
        elif len(shape) != 4:
            raise TypeError('shape must be a tuple with the lenth 4.')

        scan_i, scan_j, dp_i, dp_j = shape
        success = False


        if self.isFileOpened():
            if 'Dataset' in self.file:
                logger.warning('There has been dataset in the file. '\
                        'No new dataset is created.')
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
        -----------------------------------------------------------------------
        key                 str                 Dataset attribution

        value                                   the value of the Dataset attri-
                                                bution. Most likely it should 
                                                not be too large in size.
        -----------------------------------------------------------------------
        '''
        if self.isFileOpened():
            if 'Dataset' in self.file:
                Dataset = self.file['Dataset']
                if isinstance(key, str):
                    Dataset.attrs[key] = value
            else:
                logger.warning('There is no Dataset in the file.')
        else:
            logger.warning('File must be opened before setting attributes'\
                ' of Datasets.')


    def deleteDatasetAttribute(self, key: str):
        '''
        Delete the Dataset attribute. The Dataset must exist.

        arguments           type                description
        -----------------------------------------------------------------------
        key                 str                 Dataset attribution
        -----------------------------------------------------------------------
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

        

