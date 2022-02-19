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
                    
     
     


