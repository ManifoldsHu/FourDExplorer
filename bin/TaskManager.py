# -*- coding: utf-8 -*-

'''
*------------------------------ TaskManager.py -------------------------------*
用于异步并发任务的调度器，使用 concurrent.futures 提供的线程池和进程池，并且通过
 pyqtSignal 与主线程进行异步通信。初步只提供多线程功能，而不提供多进程功能。

当主线程想执行由某几个函数构成的并发任务时，就将这几个函数打包成 Subtask 对象，然后将
其组合成 Task 对象。接下来，主线程会给每个 Subtask 指定回调函数，它会向主线程发送信号
通知自己执行完毕。

同一时间只能运行一个 Task。如果有多个 Task，则进入任务队列等待。每当主线程添加新的 Task，
或者现有的某个 Subtask 执行完毕时，TaskManager 会检查现有任务是否完成。当现有任务已经
完成时，就切换到下一个任务。

当 Task 在任务队列中时可以取消，但当 Task 正在运行时则无法取消，只能等待其运行完毕。
(后续会添加一个通用 flag，用来取消正在运行的 Task )

作者：          胡一鸣
创建时间：      2021年12月28日

These are asynchronous dispatchers of concurrent tasks using threading or mult-
iprocessing pool from concurrent.futures . The task managers communicate with 
the main event loop by pyqtSignals. As for now, only threading pool is availab-
le.

When the main thread wants to submit a concurrent task made up by several func-
tions, it packs these functions into Subtask objects, and then combine them as 
one Task object. Next, the main thread will assign a call-back function to eve-
ry Subtask, which will send a signal to note the main thread that itself has c-
ompleted.

We note that in most case, users would like to execute tasks in order. So this 
task manager will run only one Task once. If a user submits several Tasks, they
will wait in a task queue. Whenever a new Task is submitted, or some Subtask is
completed, TaskManager will check whether the current Task has completed. If so,
the next Task will start.

We will be able to cancel a Task in waiting queue, but if it has started, we can 
only wait until it is completed. (Later a flag will be added to cancel running 
task.)

author:             Hu Yiming
date:               Jan 9, 2022

*------------------------------ TaskManager.py -------------------------------*
'''


import threading
import queue
from collections import deque
import time
import concurrent.futures
from typing import Callable
import numpy as np
from functools import partial
from PySide6.QtCore import Signal



def _packingFunc(func: Callable, *args, **kwargs) -> Callable:         
    '''
    这个函数用来将函数进行打包，类似于偏函数，把参数都打包进一个新的函数，这样新的函数
    调用的时候就可以不用带参数。

    This function is to pack the function with its arguments, just like partial
    functions or lambda functions.

    类似于:
    Example:

    def test_func(pos, opt = 2, *args, **kw):
        print('Positional Arguments: {0}'.format(pos))
        print('Optional Arguments: {0}'.format(opt))
        print('Arguments: {0}'.format(args))
        print('Keyword Arguments: {0}'.format(kw))
    if __name__ == '__main__':
        packed_func = _packingFunc(test_func, 1, 2, 3, 4, other = 5)
        packed_func()

    其结果为:
    The results are:

    Positional Aruguments: 1
    Optional Arguments: 2
    Arguments: (3, 4)
    Keyword Arguments: {'other': 5}
    '''
    def _wrapper():
        return func(*args, **kwargs)
    return _wrapper

class Subtask:
    '''
    并发执行的子任务，通常由一个函数组成，在一个子线程中运行。多个子任务会组成一个任
    务 Task。子任务对应的函数返回后，在子线程中会调用 doneCallBack() 方法作为回调函
    数。

    The Subtask that executes concurrently in a thread, consisting one function.
    Usually there are several Subtask objects in one task object. After the fu-
    nction returns, the doneCallBack() method will be called.
    '''
    def __init__(self, func, *args, **kwargs):
        '''
        arguments           type                description
        ----------------------------------------------------------------------
        func                Callable            The function that will execute 
                                                in the child thread.

        *args               any                 Non-keyword arguments

        **kwargs            any                 Keyword arguments
        -----------------------------------------------------------------------
        '''
        self._func = _packingFunc(func, args, kwargs)
        self._name = 'Subtask Ojbect: {0}({1}, {2})'.format(
            func.__name__,
            args,
            kwargs,
        )

        # self._args = args
        # self._kwargs = kwargs

        # self.future is either a concurrent.futures.Future object or None.
        self.future = None
        
        # Usually the Slot are called in the main thread, though this signal 
        # emits in the child thread.
        self.signal_complete = Signal()     

    def __str__(self):
        return self._name

    def getFunc(self):
        return self._func
        

    def getName(self):
        return self._name

    def isCompleted(self):
        if self.future:
            return self.future.done()
        else:
            return False

    def doneCallBack(self):
        self.signal_complete.emit()


class Task:
    '''
    应当顺次执行的独立任务，内部包含一个或多个可并发执行的子任务，例如遍历四维数据计
    算虚拟成像。

    在该任务执行前，主线程会调用 prepare()，做一些任务的初始化工作；在该任务执行后，
    也就是所有子任务都返回后，主线程会调用 follow()，做一些任务的后续工作。

    任务在执行开始前，也就是在队列等待的时候，可以被取消；一旦其提交到了 Executor 后
    就无法取消了。

    注意，同一个任务对象只能提交、执行一次。如果要再次执行该任务，需要重新实例化一个
    Task 对象。


    A independent task that should execute in order, in which there is one or 
    several concurrent subtasks, e.g. loop the 4D-STEM dataset and calculate a 
    virtual image.

    Before the task is executed, prepare() is called in the main thread, which 
    is used to do some preparation work. After all of the subtasks return, the
    main thread will call follow() and do some following work.

    Before a task is submitted to the executor, it can be cancelled. Once it is
    submitted, it cannot be cancelled.

    Note: A task object can be submitted and executed only ONCE. If we want to
    execute this task again, we need to instantiate a task again.
    '''
    def __init__(self, name: str, *subtasks: Subtask):
        '''
        arguments           type                description
        -----------------------------------------------------------------------
        name                str                 The name of task

        subtasks            Subtask             The subtask object that execut-
                                                es concurrently.
        -----------------------------------------------------------------------
        '''
        self._name = name
        self._subtasks = subtasks
        self._is_cancelled = False
        self._is_submitted = False
        self._follow_func = None
        self._prepare_func = None

    def getSubtask(self) -> tuple:
        '''
        列出该任务下属的各个子任务对象。

        Returns a tuple that includes Subtask objects of this task.
        '''
        return self._subtasks

    def setSubmitted(self):
        '''
        提交任务给 executor 时，设置其状态为 True.

        When this task is submitted to the executor, the state is set to True.
        '''
        self._is_submitted = True

    def cancel(self) -> bool:
        '''
        取消任务。取消了的任务不会提交给 executor. 一个任务只有在被提交给 executor 
        之前才能被取消。

        Cancel this task. A cancelled task will not be submitted to the execut-
        or. The task can be cancelled only before it is submitted.
        '''
        if self._is_submitted:
            return False
        else:
            self._is_cancelled = True
            return True

    def isCancelled(self) -> bool:
        return self._is_cancelled

    def setFollowing(self, func, *args, **kwargs):
        '''
        设置该任务在执行完所有子任务后需要调用的函数。用来做一些后续工作。

        Set the function that will be called after the task has been done.

        arguments           type                description
        -----------------------------------------------------------------------
        func                Callable            The function that will be call-
                                                ed after the whole task is done.
                                                It is called in the main thread.

        *args               any                 Non-keyword arguments

        **kwargs            any                 Keyword arguments
        -----------------------------------------------------------------------
        '''
        self._follow_func = _packingFunc(func, *args, **kwargs)

    def setPreparing(self, func, *args, **kwargs):
        '''
        设置该任务在提交给 executor 之前需要调用的函数。用来做一些准备工作。

        Set the function that will be called before the task is submitted.

        arguments           type                description
        -----------------------------------------------------------------------
        func                Callable            The function that will be call-
                                                ed before the whole task is su-
                                                bmitted. It is called in the m-
                                                ain thread.

        *args               any                 Non-keyword arguments

        **kwargs            any                 Keyword arguments
        -----------------------------------------------------------------------
        '''
        self._prepare_func = _packingFunc(func, *args, **kwargs)

    def following(self):
        '''
        执行任务完成的后续工作。

        Call the following function.
        '''
        if self._follow_func:
            self._follow_func()

    def preparing(self):
        '''
        执行任务之前的准备工作。

        Call the preparing function.
        '''
        if self._prepare_func:
            self._prepare_func()

    

class TaskManager:
    '''
    异步任务调度器，对 Executor 的进一步封装，保证一次只能执行一个 Task。绝大部分
    4D-STEM 任务都有先后顺序要求，所以我们用事件循环来协调这些任务的顺序，而单个的本
    地任务往往涉及到 IO 与计算，因此可以用并发处理。

    该任务调度器的各种操作都是依托于主线程事件循环的，因此可以使用 Qt 的信号-槽机制来
    调用其函数。具体来讲，就是把任务加入队列、取消任务、提交任务、任务执行完毕通知等
    等各种操作都是需要通过信号进行调度的。

    This is an asynchronous task manager, which encapsulates executors to ensu-
    re that only one task executes once. Most of the 4D-STEM task should be ex-
    ecuted in order, and we use event-loop to handle this. In one whole task t-
    here usually exists IO operations and calculations, so we do that concurre-
    ntly.

    Since the operations of the TaskManager rely on the event loop in the main 
    thread, so we can use signal-slot mechanism in Qt to call its functions. To
    be more specific, we can use signals to call the slot functions like add t-
    ask into the task queue, cancel tasks, submit a task, and notify users the 
    current task has been done. 
    '''
    def __init__(self, executor_name = 'threading'):
        # 使用 popleft() 方法来从队列里取出；使用 append() 方法来加入队列
        self._task_queue = deque(maxlen=20)

        # 当前任务，要么是 None, 要么是 Task 对象。
        self._current_task = None

        # 该 TaskManager 对应的 executor 的类型。
        self.executor_name = executor_name
        if executor_name == 'threading':
            self._executor = concurrent.futures.ThreadPoolExecutor()
        elif executor_name == 'multiprocessing':
            self._executor = concurrent.futures.ProcessPoolExecutor()
        else:
            raise TypeError('executor must be \'threading\' or \'multiprocessing\'')
        
        
    def _submit(self, task: Task):
        '''
        提交每个子任务。每个子任务都会绑定一个回调函数，发送自己完成任务的信号。

        Submit every subtask. A callback function is bounded to each subtask, 
        in order to send a Signal that this subtask has been completed.
        '''
        for subtask in task.getSubtask():
            subtask.signal_complete.connect(self._submitNext,)
            subtask.future = self._executor.submit(subtask.getFunc())
            subtask.future.add_done_callback(subtask.doneCallBack)
            # subtask.future.add_done_callback(self._submitNext)
            

    def _submitNext(self,):
        '''
        提交下一个任务。在以下情况下，会调用这个函数：
            - 现有任务中的某个子任务完成
            - 用户添加了一个新任务

        这个函数不是原子操作，因此很可能发生并发问题。比如说，可能会有倒数第二个子任务
        完成时发送了信号，调用了这个函数。当这个函数检查的时候，最后一个子任务却也恰好
        完成了。那么，这个函数就会直接从队列中取出一个任务提交。问题在于，最后一个子任
        务也会进行检查、调用这个函数。
        
        但是，这不会产生什么影响，因为只要我们能保证各个任务之间是互斥地、顺次地执行，
        然后又不漏掉任何任务，就可以了。由于我们确保了一般只有主线程(事件循环)能调用这
        个函数，所以这个函数对于主线程而言是不可以并发执行的。

        Submit the next task. This function is called in the following case:
            - some subtask of the current task is completed,
            - or a user enqueues a new task.

        This function is not an atomic operation, so there may exist some conc-
        urrent problems. For example, there may be the second last subtask emit
        a signal that itself has been completed, and call this function. When 
        this function is checking, the last subtask is completed at the same t-
        ime. Then, this function will pop a task and submit it. The problem is,
        the last subtask will also emit a signal and try to call this function.

        I personally suppose this will not cause any critical problems, because
        the only goal is to ensure that each task is executed mutual exclusive-
        ly, and in order. This function, as a slot, can only be called in the 
        main thread event, and hence we can safely call this function multiple 
        times and do not need to worry about it.
        '''
        if threading.current_thread().name != 'MainThread':
            raise RuntimeError('TaskManager._submitNext() must be called in MainThread!')
        done = True
        if self._current_task:
            for subtask in self._current_task.getSubtask():
                if not subtask.isCompleted():
                    done = False
        if done:
            if self._current_task:
                self._current_task.following()
            try:
                # next_task = self._task_queue.get_nowait()
                next_task = self._task_queue.popleft()
                while next_task.isCancelled():
                    next_task = self._task_queue.popleft()
            except IndexError:
                self._current_task = None
            else:
                self._current_task = next_task
                next_task.setSubmitted()
                next_task.preparing()
                self._submit(next_task)
                
                # 通知 GUI 及时更改显示任务队列以及正在进行的任务的界面
                self._flush_task_queue()
    
    def addTask(self, task: Task):
        '''
        往任务队列里添加任务。
        '''
        if not isinstance(task, Task):
            raise TypeError('task must be a Task object.')
        self._task_queue.append(task)
        self._submitNext()
        self._flush_task_queue()

    def shutdown(self):
        '''
        关闭 executor 并释放资源。这个操作会等待所有子任务都执行完毕之后才执行。
        '''
        self._executor.shutdown(wait=True)

    def _flush_task_queue(self):
        pass

    
                
            
