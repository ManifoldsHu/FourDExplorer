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
import numpy as np
from functools import partial
from PySide6.QtCore import pyqtSignal


def _packingFunc(func, *args, **kwargs):
    def _wrapper():
        return func(*args, **kwargs)
    return _wrapper

class Subtask:
    '''
    
    '''
    def __init__(self, func, *args, **kwargs):
        self._func = func
        self._name = 'Subtask Ojbect: {0}({1}, {2})'.format(
            func.__name__,
            args,
            kwargs,
        )
        self.future = None
        self._args = args
        self._kwargs = kwargs

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


class Task:
    '''
    
    '''
    def __init__(self, name, *subtasks: Subtask):
        self._name = name
        self._subtasks = subtasks
        self._is_cancelled = False
        self._is_submitted = False
        self._follow_func = None
        self._prepare_func = None

    def getSubtask(self):
        return self._subtasks

    def setSubmitted(self):
        self._is_submitted = True

    def cancel(self):
        if self._is_submitted:
            return False
        else:
            self._is_cancelled = True
            return True

    def isCancelled(self):
        return self._is_cancelled

    def setFollowing(self, func, *args, **kwargs):
        self._follow_func = _packingFunc(func, *args, **kwargs)

    def setPreparing(self, func, *args, **kwargs):
        self._prepare_func = _packingFunc(func, *args, **kwargs)

    def following(self):
        if self._follow_func:
            self._follow_func()

    def preparing(self):
        if self._prepare_func:
            self._prepare_func()

    

class TaskManager:
    '''
    
    '''
    def __init__(self, executor = 'threading'):
        self._task_queue = queue.Queue()
        self._current_task = None
        self.executor_name = executor
        if executor == 'threading':
            self._executor = concurrent.futures.ThreadPoolExecutor()
        elif executor == 'multiprocessing':
            self._executor = concurrent.futures.ProcessPoolExecutor()
        else:
            raise TypeError('executor must be \'threading\' or \'multiprocessing\'')
        self._submit_lock = threading.Lock()
        
    def _addCallBack(self, task: Task):
        for subtask in task.getSubtask():
            subtask.future = self._executor.submit(subtask.getFunc())
            subtask.future.add_done_callback(self._submitNext)


    def _submitNext(self, future = None):
        '''
        这个函数禁止并发执行。然而，这个函数会在线程池中的子线程调用，因此需要加个锁。
        '''
        with self._submit_lock:
            done = True
            if self._current_task:
                for subtask in self._current_task.getSubtask():
                    if not subtask.isCompleted():
                        done = False
            if done:
                if self._current_task:
                    self._current_task.following()
            try:
                next_task = self._task_queue.get_nowait()
                while next_task.isCancelled():
                    next_task = self._task_queue.get_nowait()
            except queue.Empty:
                pass
            else:
                next_task.setSubmitted()
                next_task.preparing()
                self._submit(next_task)
                self._flush_task_queue()
    
    def addTask(self, task: Task):
        self._task_queue.put(task)
        self._submitNext()
        self._flush_task_queue()

    def shutdown(self):
        self._thread_executor.shutdown()

    def _flush_task_queue(self):
        pass

    
                
            
