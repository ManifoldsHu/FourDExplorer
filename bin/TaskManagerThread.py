# -*- coding: utf-8 -*-

"""
测试的任务调度器。使用 concurrent.futures 中的 ThreadExecutor。
"""

import threading
import queue
from collections import deque
import time
from concurrent import futures
from typing import Iterator, Callable

from PySide6.QtCore import Signal, QObject

from Constants import TaskState

def _packing(func: Callable, *arg, **kw) -> Callable:
    """
    This function is to pack the function with its arguments, just like partial
    functions or lambda functions.

    Example:

    def test_func(pos, opt = 2, *args, **kw):
        print('Positional Arguments: {0}'.format(pos))
        print('Optional Arguments: {0}'.format(opt))
        print('Arguments: {0}'.format(args))
        print('Keyword Arguments: {0}'.format(kw))
    if __name__ == '__main__':
        packed_func = _packingFunc(test_func, 1, 2, 3, 4, other = 5)
        packed_func()

    The results are:

    Positional Aruguments: 1
    Optional Arguments: 2
    Arguments: (3, 4)
    Keyword Arguments: {'other': 5}
    """
    def _wrapper():
        return func(*arg, **kw)
    return _wrapper 


class TaskManager(QObject):
    """
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
    """

    # task_submitted = Signal()
    # task_completed = Signal()
    # task_excepted = Signal()
    # task_terminated = Signal()
    
    # _subtask_completed = Signal()
    # _subtask_submitted = Signal()
    # _subtask_excepted = Signal()
    # _subtask_terminated = Signal()

    # waiting_task_added = Signal()
    # waiting_task_cancelled = Signal()

    def __init__(self):
        self._task_queue = TaskQueue()
        self._current_task = None
        self._executor = futures.ThreadPoolExecutor()

    @property
    def task_queue(self) -> 'TaskQueue':
        return self._task_queue
    
    def addTask(self, task: 'Task'):
        """
        Add a task to the waiting queue.

        arguments:
            task: (Task)
        """
        if not isinstance(task, Task):
            raise TypeError('task must be a Task, not '
                '{0}'.format(type(task).__name__))
        self.task_queue.addTask(task)
        self.startNextTask()

    def startNextTask(self):
        """
        if a task is completed, it will send task_completed signal. Then this 
        slot will be called. 
        """
        self._clearLastTask()
        self._submitNextTask()
        self._refresh()


    def _clearLastTask(self):
        """
        Set the _current_task to None.
        """
        if self._current_task is None:
            return True
        elif self._current_task.state in (TaskState.Completed,):
            self._current_task.follow()
            self._current_task = None
            return True
        else:
            return False

    def _submitNextTask(self):
        """
        Get a new task from the waiting queue.
        """
        if self._current_task:
            return False
        task = self.task_queue.popTask()
        if task is None:
            return False
        task.state = TaskState.Submitted
        task.task_completed.connect(self.startNextTask)
        task.prepare()
        self._submit(task)
        return True

    def _submit(self, task: 'Task'):
        """
        Submit all of the subtasks in the task.
        """
        for subtask in task:
            subtask.future = self._executor.submit(subtask.getFunction())
            subtask.future.add_done_callback(subtask.complete)

    def refresh(self):
        pass


class TaskQueue(QObject):
    """
    任务的等待队列。

    任务初始化以后，就加入到等待队列中。只要当前任务完成了，就从等待队列中拿出一个
    任务，提交给 TaskManager，交由线程池处理。

    当一个任务加入到等待队列中时，就也同时会加入到任务历史中。使用 clearHistory 可以
    清空任务历史。

    Waiting task queue.

    After a task is initialized, it is enqueued to this task queue. Any time
    a task is completed, one task should be poped, and sumbitted to the pool.
    
    Whenever a task is added to waiting list, it is also added to history list.
    Use clearHistory() to clear the history list.
    """
    def __init__(self):
        self._maxlen = 10
        self._maxhistory = 100
        self._tq = []
        self._history = []
        
    @property 
    def maxlen(self) -> int:
        """
        returns:
            (int) the maximum length of waiting queue.
        """
        return self._maxlen

    @maxlen.setter
    def maxlen(self, mlen: int):
        """
        Set the maximum length of waiting queue.

        arguments:
            mlen: (int)
        """
        if not isinstance(mlen, int):
            raise TypeError(('maxlen must be int, not '
                '{0}'.format(type(mlen).__name__)))
        self._maxlen = mlen 

    @property
    def maxhistory(self) -> int:
        """
        returns:
            (int) the maximum length of history list.
        """
        return self._maxhistory

    @maxhistory.setter
    def maxhistory(self, mlen: int):
        """
        Set the maximum length of history list.

        arguments:
            mlen: (int)
        """
        if not isinstance(mlen, int):
            raise TypeError(('maxhistory must be int, not '
                '{0}'.format(type(mlen).__name__)))
        self._maxhistory = mlen 

    def addTask(self, task: 'Task'):
        """
        Add a task into waiting queue.

        arguments:
            task: (Task)
        """
        if not isinstance(task, Task):
            raise TypeError('task must be a Task, not '
                '{0}'.format(type(task).__name__))
        if len(self) >= self.maxlen:
            raise ValueError('Cannot add task: too many task waiting')
        self._tq.append(task)

        if len(self._history) >= self.maxhistory:
            self._history.pop(0)
        self._history.append(task)
    
    def popTask(self) -> 'Task'|None:
        """
        Get the task from the front of the waiting queue.

        returns:
            (Task)
        """
        if len(self._tq) > 0:
            return self._tq.pop(0)
        else:
            return None

    def cancelTask(self, index: int) -> 'Task':
        """
        Delete a task from the waiting queue.

        arguments:
            index: (int) 
        
        returns:
            (Task)
        """
        return self._tq.pop(index)

    def __str__(self) -> str:
        return '<TaskQueue>: {0} members.'.format(len(self._tq))

    def __repr__(self) -> str:
        return self.__str__()

    def __getitem__(self, index: int) -> 'Task':
        return self._tq[index]

    def __setitem__(self, index: int, task: 'Task'):
        if not isinstance(task, Task):
            raise TypeError(('task must be Task object, not '
                '{0}'.format(type(task).__name__)))
        self._tq[index] = task

    def __len__(self):
        return len(self._tq)

    def __iter__(self) -> Iterator:
        return iter(self._tq)

    def __contains__(self, task: 'Task') -> bool:
        return task in self._tq 

    @property 
    def waiting_view(self):
        return [task.name for task in self._tq]

    @property
    def history_view(self):
        return [task.name for task in self._history]

    def clearHistory(self):
        self._history = []


class Task(QObject):
    """
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
    """

    # task_cancelled = Signal()
    # task_submitted = Signal()
    task_completed = Signal()   # emits when this task is completed.

    def __init__(self, name: str):
        self._name = name
        self._subtasks = []
        self._follow = None
        self._prepare = None
        self._comment = ''
        self._progress = None
        self._state = TaskState.Initialized

    @property
    def subtasks(self):
        """
        returns:
            (list) all of the subtasks
        """
        return self._subtasks

    @property
    def state(self) -> TaskState:
        """
        returns:
            (TaskState) the state of this task. There are:
                Initialized     
                    The task is initialized

                Waiting         
                    The task is added to waiting queue.

                Cancelled       
                    The task in the waiting queue is cancelled.

                Submitted       
                    The task in the waiting queue is about to execute.

                Completed       
                    The task has executed and already completed.

                Aborted         
                    The task is aborted when executing, forced by user.

                Excepted        
                    The task is aborted when executing, due to exceptions.
        """
        return self._state

    @state.setter
    def state(self, _tstate: TaskState):
        """
        arguments:
            _tstate: (TaskState)
        """
        if not isinstance(_tstate, TaskState):
            raise TypeError('state must be one of TaskState, not'
                '{0}'.format(type(_tstate).__name__))

    def __iter__(self):
        return iter(self._subtasks)

    def __len__(self):
        return len(self._subtasks)

    def __contains__(self, subtask: 'Subtask') -> bool:
        return subtask in self._subtasks

    def setFollow(self, func: Callable, *arg, **kw):
        """
        Set the following function.
        
        The function will be called after the task is completed.

        arguments:
            func: (Callable) the following function

            *args: those positional arguments of the function

            **kw: those key word arguments of the function
        """
        if not isinstance(func, Callable):
            raise TypeError(('func must be a Callable, not '
                '{0}'.format(type(func).__name__)))
        self._follow = _packing(func, *arg, **kw)

    def setPrepare(self, func: Callable, *arg, **kw):
        """
        Set the preparing function.

        The function will be called before the task is submitted.

        arguments:
            func: (Callable) the preparing function

            *args: those positional arguments of the function

            **kw: those key word arguments of the function
        """
        if not isinstance(func, Callable):
            raise TypeError(('func must be a Callable, not '
                '{0}'.format(type(func).__name__)))
        self._prepare = _packing(func, *arg, **kw)

    def follow(self):
        """
        Call the following function.
        """
        if self._follow:
            self._follow()

    def prepare(self):
        """
        Call the preparing function.
        """
        if self._prepare:
            self._prepare()

    @property
    def comment(self) -> str:
        """
        returns:
            (str) the comment of this task.
        """
        return self._comment

    @comment.setter
    def comment(self, _comm: str):
        """
        Set the comment of this task. 
        
        Describing what the task to do and how.

        arguments:
            _comm: (str)
        """
        if not isinstance(_comm, str):
            raise TypeError(('comment must be a str, not '
                '{0}'.format(type(_comm).__name)))
        self._comment = _comm
        
    def addSubtask(self, name: str, func: Callable, *arg, **kw):
        """
        Add a subtask to this task.

        All of the subtask will be submitted to the threading pool, and they
        will execute concurrently.

        arguments:
            name: (str) the name of subtask

            func: (Callable) the function to be executed concurrently

            *arg: positional arguments of the function

            **kw: keyword arguments of the function
        """
        packed_func = _packing(func, *arg, **kw)
        subtask = Subtask(packed_func)
        subtask.name = name
        subtask.subtask_completed.connect(self.checkCompleted)
        self._subtasks.append(subtask)

    @property
    def progress(self) -> int|None:
        """
        The progress of the task.

        Usually we need to use a subtask to send signals about progressing.

        returns:
            (int or None)
        """
        return self._progress

    @progress.setter
    def progress(self, _pg: int|None):
        """
        Set progress of the task.

        Usually we need to use a subtask to send signals about progressing.

        arguments:
            _pg: (int or None)
        """
        if not isinstance(_pg, int):
            self._progress = None
            raise TypeError('progress must be int, not '
                '{0}'.format(type(_pg).__name__))
        if _pg < 0 or _pg > 100:
            self._progress = None
            raise ValueError('progress must larger than 0 '
                'and smaller than 100')
        self._progress = _pg 

    def checkCompleted(self) -> bool:
        """
        Check wheter this taks is completed.

        If true, a task_completed signal will be emitted.
        """
        if self.state == TaskState.Completed:
            return True
        elif self.state == TaskState.Submitted:
            for subtask in self:
                if not subtask.completed:
                    return False
            self.state = TaskState.Completed
            self.task_completed.emit()
            return True
        else:
            return False
        
    def setProgress(self, progress: int):
        """
        Set the progress of the task.
        
        This acts like a slot. Use a signal from a subtask to set progress. 
        Progress must be a integer between 0 and 100

        arguments:
            progress: (int)
        """
        self.progress = progress
    

    # def cancel(self):
    #     if self.state in (TaskState.Initialized, 
    #                       TaskState.Waiting,
    #                       TaskState.Cancelled):
    #         self.state = TaskState.Cancelled
    #     else:
    #         raise RuntimeError('Cannot cancel task. '
    #             'Only initialized or waiting tasks can be cancelled.')

    # def abort(self):
    #     if self.state in (TaskState.Submitted, TaskState.Aborted):
    #         self.state = TaskState.Aborted
    #     else:
    #         raise RuntimeError('Cannot abort task. '
    #             'Only submitted tasks can be aborted')

    # def excepting(self):
    #     if self.state in (TaskState.Submitted, TaskState.Excepted):
    #         self.state = TaskState.Excepted
    #     else:
    #         raise RuntimeError('Cannot excepting task. '
    #             'Only submitted tasks can be aborted')

    # def wait(self):
    #     if self.state in (TaskState.Initialized, TaskState.Waiting):
    #         self.state = TaskState.Waiting
    #     else:
    #         raise RuntimeError('Cannot set task to be waiting. '
    #             'Only initialized tasks can be set to be waiting')

    # def submit(self):
    #     if self.state in (TaskState.Initialized, TaskState.Waiting):
    #         self.state = TaskState.Submitted
    #     else:
    #         raise RuntimeError('Cannot set task to be submitted. '
    #             'Only initialized or waiting task can be set to be submitted')

    
class Subtask(QObject):
    """
    并发执行的子任务，通常由一个函数组成，在一个子线程中运行。多个子任务会组成一个任
    务 Task。子任务对应的函数返回后，在子线程中会调用 doneCallBack() 方法作为回调函
    数。

    The Subtask that executes concurrently in a thread, consisting one function.
    Usually there are several Subtask objects in one task object. After the fu-
    nction returns, the doneCallBack() method will be called.
    """
    subtask_completed = Signal()
    subtask_progress = Signal(int)

    def __init__(self, func: Callable):
        if not isinstance(func, Callable):
            raise TypeError('func must be Callable, not '
                '{0}'.format(type(func).__name__))
        self._func = func
        self._name = 'anonymous'
        self._future = None
    
    def __str__(self):
        return '<Subtask> name: {0}'.format(self.name)

    def __repr__(self):
        return self.__str__()

    @property
    def completed(self) -> bool:
        if self.future:
            return self.future.done()
        else:
            return False

    @property
    def future(self):
        return self._future

    @future.setter
    def future(self, _ft: futures.Future):
        if not isinstance(_ft, futures.Future):
            raise TypeError('future must be Future object, not '
                '{0}'.format(type(_ft).__name__))
        self._future = _ft

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name: str):
        if not isinstance(_name, str):
            raise TypeError('name must be str, not '
                '{0}'.format(type(_name).__name__))

    def getFunction(self):
        return self._func

    def complete(self):
        self.subtask_completed.emit()