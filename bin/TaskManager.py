# -*- coding: utf-8 -*-

"""
*------------------------------ TaskManager.py -------------------------------*
用于异步并发任务的调度器。

使用 concurrent.futures 中的 ThreadExecutor 作为线程池，并且通过 Signal 与主线程
进行异步通信。这个管理器只用于多线程，用于 IO 密集型任务的并发，且避免主界面卡死。多
进程的并行任务后续由单独的管理器给出。

当主线程想执行由某几个函数构成的并发任务时，就将这几个函数打包成 Subtask 对象，然后将
其组合成 Task 对象。接下来，主线程会给每个 Subtask 指定回调函数，它会向主线程发送信号
通知自己执行完毕。

同一时间只能运行一个 Task。如果有多个 Task，则进入任务队列等待。每当主线程添加新的 Task，
或者现有的某个 Subtask 执行完毕时，TaskManager 会检查现有任务是否完成。当现有任务已经
完成时，就切换到下一个任务。

当 Task 在任务队列中时可以取消，但当 Task 正在运行时则无法取消，只能等待其运行完毕。

作者：          胡一鸣
创建时间：      2022年1月9日


This is a Scheduler for asynchronous concurrent tasks.

We use ThreadExecutor from concurrent.futures as the pool, and use signal to 
communicate between the main thread and the child threads. This manager is 
only used in multithread, for those long duration IO tasks, and for avoiding
the main window is blocked. Due to GIL, this manager cannot do parallel calcu-
ations.

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
only wait until it is completed.

author:             Hu Yiming
date:               Jan 9, 2022
*------------------------------ TaskManager.py -------------------------------*
"""


from concurrent import futures
from typing import Iterator, Callable
import traceback

from PySide6.QtCore import (
    Signal, 
    QObject, 
    QAbstractListModel, 
    QModelIndex, 
    Qt,
)

from PySide6.QtWidgets import QMessageBox

from Constants import TaskState
from logging import Logger


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
    并发任务调度器。

    异步任务调度器，对 Executor 的进一步封装，保证一次只能执行一个 Task。绝大部分
    4D-STEM 任务都有先后顺序要求，所以我们用事件循环来协调这些任务的顺序，而单个的本
    地任务往往涉及到 IO 与计算，因此可以用并发处理。

    该任务调度器的各种操作都是依托于主线程事件循环的，因此可以使用 Qt 的信号-槽机制来
    调用其函数。具体来讲，就是把任务加入队列、取消任务、提交任务、任务执行完毕通知等
    等各种操作都是需要通过信号进行调度的。

    如果想向线程池提交任务，则要先实例化 Task，然后调用 Task.addSubtask 方法，将需要
    并发执行的各个函数都作为子任务加到 Task 中。然后调用管理器的 addTask 方法即可将任
    务加入等待队列，稍后便会自动执行。

    A concurrent task manager.

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

    If we want to submit a task to the tread pool, we need to instantiate an 
    Task object, and then use Task.addSubtask() method to add those functions 
    that need to execute concurrently. After that, we call addTask() method of
    the TaskManager, which will enqueue the task. At last, after a moment the
    task will execute automatically.

    signals:
        progress_updated: (int) emits whenever the current task's progress is
            updated. The progress will show in the progress bar on the screen.

        task_info_refresh: emits whenever the current task is changed, e.g. a
            new task is submitted.

    attributes:
        task_queue: (TaskQueue)

        model_waiting: (TaskQueueModel)

        current_task: (Task or None)
    """

    progress_updated = Signal(int)      
    # emits whenever the current task's progress update

    task_info_refresh = Signal()
    # emits whenever the current task is changed, e.g. a new task is submitted.

    TaskState = TaskState

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._task_queue = TaskQueue()
        self._current_task = None
        self._executor = futures.ThreadPoolExecutor()
        self._model_waiting = TaskQueueModel(self)

    @property
    def task_queue(self) -> 'TaskQueue':
        return self._task_queue
    
    @property
    def model_waiting(self) -> 'TaskQueueModel':
        return self._model_waiting

    @property
    def current_task(self) -> 'Task':
        return self._current_task

    @current_task.setter
    def current_task(self, task: 'Task'):
        if task == None:
            self._current_task = None
        elif isinstance(task, Task):
            self._current_task = task
        else:
            raise TypeError('current task must be a Task or None, not '
                '{0}'.format(type(task).__name__))

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger


    def addTask(self, task: 'Task'):
        """
        Add a task to the waiting queue.

        arguments:
            task: (Task)
        """
        if not isinstance(task, Task):
            raise TypeError('task must be a Task, not '
                '{0}'.format(type(task).__name__))
        task.state = TaskState.Waiting
        task.setParent(self)
        self.model_waiting.addTask(task)
        self._startNextTask()

    def cancelTask(self, index: int|QModelIndex):
        """
        Cancel the task in the waiting queue.

        arguments:
            index: (int or QModelIndex) 
        """
        if isinstance(index, int):
            _index = self.model_waiting.createIndex(index, 0)
        elif isinstance(index, QModelIndex):
            _index = index
        else:
            raise TypeError('index must be int or QModelIndex, not '
                '{0}'.format(type(index).__name__))
        if not _index.isValid():
            return None
        
        task = self.model_waiting.cancelTask(_index)
        task.state = TaskState.Cancelled

    def _startNextTask(self):
        """
        if a task is completed, it will send task_completed signal. Then this 
        slot will be called. 
        """
        self._clearLastTask()
        self._refresh()         # Reinitialize the state of task manager

        _call_submitNextTask = True
        while _call_submitNextTask:
            _call_submitNextTask = self._submitNextTask()

        self._refresh()         # Update the state of task manager


    def _clearLastTask(self) -> bool:
        """
        Set the _current_task to None, and do follow work of the task.

        returns:
            (bool) whether the last task is cleared.
        """
        if self.current_task is None:
            return True

        elif self.current_task.state in (TaskState.Completed,):
            self._currentDoFollowWork()
            return True

        elif self.current_task.state in (TaskState.Excepted,):
            # Handle the exception, but still try doing following work.
            for subtask in self.current_task:
                if subtask.exception:
                    self.logger.error(
                        '{0}'.format(subtask.exception), 
                        exc_info = True,
                    )
                    # QMessageBox.warning(
                    #     None,
                    #     'Error: {0}'.format(self.current_task.name),
                    #     'Error in subtask {0} occurred:\n {1}'.format(
                    #         subtask.name, subtask.exception),
                    #     QMessageBox.Ok,
                    # )

            self._currentDoFollowWork()
            return True

        else:
            return False


    def _currentDoFollowWork(self):
        """
        Do follow work, and handle its exceptions.
        """
        try:
            self.logger.info('Task {0} completed.'.format(
                self.current_task.name
            ))
            self.current_task.follow()
        except BaseException as e:
            self.logger.error('{0}'.format(e), exc_info = True)
            # QMessageBox.warning(
            #     None,
            #     'Error: {0}'.format(self.current_task.name),
            #     'Error when do follow work: \n {0}'.format(e),
            #     QMessageBox.Ok,
            # )
        finally:
            self.current_task = None


    def _submitNextTask(self) -> bool:
        """
        Get a new task from the waiting queue
        
        Will do prepare work of the task.

        If this function returns False, then the task is submitted to the exec-
        utor successfully, or the current task is still running, or there is no
        waiting task. In other words, we do not need call this function again.

        However, if this function returns True, then the task is not submitted
        successfully. Some exceptions occured during the preparation of this t-
        ask. So we abandon this task, try getting another task from the the
        waiting queue, and submit it to the executor.

        returns:
            (bool) indicates whether task manager should recall this function
                to get another task into the threading pool. 
        """
        
        if self.current_task:
            return False

        task = self.model_waiting.popTask()
        if task is None:
            return False

        task.state = TaskState.Submitted
        self.logger.info('Task {0} submitted.'.format(task.name))
        task.task_completed.connect(self._startNextTask)
        task.task_progress.connect(self._sendProgress)

        try:
            task.prepare()
        except BaseException as e:
            # Abandon submitting if errors happen
            task.state = TaskState.Excepted
            self.logger.error('{0}'.format(e), exc_info = True)
            # QMessageBox.warning(
            #     None, 
            #     'Error: {0}'.format(self.current_task.name), 
            #     'Error when do preparing work:\n {0}'.format(e),
            #     QMessageBox.Ok,
            # )
            self.logger.info('Task {0} aborted.'.format(task.name))
            return True # This function need to be called again.

        else:
            self.current_task = task
            for subtask in task:
                subtask.future = self._executor.submit(
                    subtask.getFunction()
                )
                subtask.future.add_done_callback(subtask.complete)
                self.logger.debug(
                    'subtask {0} submitted to the executor and has added '
                    'done callback'.format(subtask.name)
                )
            return False


    def _refresh(self):
        self.task_info_refresh.emit()


    def _sendProgress(self):
        self.progress_updated.emit(self.current_task.progress)


    def _abortForce(self):
        """
        Force terminating the current task. 
        
        It seems we cannot do this for now.
        """
        pass

    def shutDown(self):
        """
        Shut down the executor. 
        
        The python process will end until the last task completes. Use this
        function before close 4D-Explorer software to clear resources. 

        And also the waiting queue will be cleared.
        """
        self.task_queue.clearWaiting()
        self.task_queue.clearHistory()
        self._executor.shutdown(wait = False, cancel_futures = True)
        self.logger.debug('Executor in TaskManager shuts down')
    
    def clearHistory(self):
        """
        Clear the list of history tasks.
        """
        self.task_queue.clearHistory()

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

    attributes:
        maxlen: (int) the maximum length of waiting queue

        maxhistory: (int) the maximum length of history queue
    """
    def __init__(self):
        self._maxlen = 10
        self._maxhistory = 100
        self._tq = []       # waiting list of tasks (task queue)
        self._history = []  # history list of tasks
        
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

    @property
    def history_list(self) -> list:
        return self._history

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
    
    def popTask(self) -> 'Task':
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

    def clearHistory(self):
        """
        Clear the history lists.
        """
        self._history = []

    def clearWaiting(self):
        """
        Clear all of the waiting tasks.
        """
        self._tq = []



class Task(QObject):
    """
    应当顺次执行的独立任务。
    
    内部包含一个或多个可并发执行的子任务，可以使用 for 循环遍历地取到这些子任务。

    在该任务执行前，主线程会调用 prepare()，做一些任务的初始化工作；在该任务执行后，
    也就是所有子任务都返回后，主线程会调用 follow()，做一些任务的后续工作。

    任务在执行开始前，也就是在队列等待的时候，可以被取消；一旦其提交到了 Executor 后
    就无法取消了。

    注意，同一个任务对象只能提交、执行一次。如果要再次执行该任务，需要重新实例化一个
    Task 对象。

    要使用 Task 对象，可以直接实例化 Task，然后使用 addSubtask() 方法，即可组装成
    完整的并发任务。也可以使用继承对象。每个任务最好能为其指定名字和注释，它们会显示
    在主界面里。

    一个任务具有多种状态，TaskManager 会自动调整其状态：
        Initialized             初始化
        Waiting                 已经加入到等待队列
        Cancelled               在等待时被取消
        Submitted               已提交到 executor 并正在执行
        Completed               任务已经完成(所有子任务均已完成)
        Aborted                 在执行时被用户强制终止
        Excepted                在执行时因为异常而终止
    其中 Aborted 状态目前无法达到。

    An independent task that should execute in order. 
    
    In a task there is one or several concurrent subtasks, and we can use for
    loop to get all of these subtasks.

    Before the task is executed, prepare() is called in the main thread, which 
    is used to do some preparation work. After all of the subtasks return, the
    main thread will call follow() and do some following work.

    Before a task is submitted to the executor, it can be cancelled. Once it is
    submitted, it cannot be cancelled.

    NOTE: A task object can be submitted and executed only ONCE. If we want to
    execute this task again, we need to instantiate a task again.

    If we want to use Task object, we can instantiate Task, and use addSubtask()
    method. We can also use inheritance objects. It would be better to give the
    task a name and comments, because they will be shown on the screen.

    A Task has multiple kinds of states:
        Initialized     The task is initialized.
        Waiting         The task is added to waiting queue.
        Cancelled       The task in the waiting queue is cancelled.
        Submitted       The task in the waiting queue is about to execute.
        Completed       The task has executed and already completed.
        Aborted         The task is aborted when executing, forced by user.
        Excepted        The task is aborted when executing, due to exceptions.
    Among them Aborted cannot be a valid state for now.

    signals:
        task_completed: emits when this task is completed.

        task_progress:  emits when the progress of this task is updated.

    attributes:
        name: (str) name of this task
        
        state: (TaskState) the state of the task

        comment: (str) comment of this task
    """

    task_completed = Signal()   # emits when this task is completed.
    task_progress = Signal()    # emits when progress is updated

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._name = 'untitled'
        self._subtasks = []
        self._follows = [self._doNothing]
        self._prepares = [self._doNothing]
        self._comment = ''
        self._progress = 0
        self._state = TaskState.Initialized
        self._has_progress = False

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, _name: str):
        if not isinstance(_name, str):
            raise TypeError('name must be a str, not '
                '{0}'.format(type(_name).__name__))
        self._name = _name

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
            (TaskState) the state of this task.
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
        self._state = _tstate

    def __iter__(self):
        return iter(self._subtasks)

    def __len__(self):
        return len(self._subtasks)

    def __contains__(self, subtask: 'Subtask') -> bool:
        return subtask in self._subtasks

    def __getitem__(self, index: int):
        return self.subtasks[index]

    def _doNothing(self):
        """
        Default preparation and following function.

        This function will do nothing.
        """
        pass

    def setFollow(self, func: Callable, *arg, **kw):
        """
        Set the following function.
        
        The function will be called after the task is completed. We can set 
        following function multiple times, and those functions will be called
        according to the order they were added.

        arguments:
            func: (Callable) the following function

            *args: those positional arguments of the function

            **kw: those key word arguments of the function
        """
        if not isinstance(func, Callable):
            raise TypeError(('func must be a Callable, not '
                '{0}'.format(type(func).__name__)))
        self._follows.append(_packing(func, *arg, **kw))

    def setPrepare(self, func: Callable, *arg, **kw):
        """
        Set the preparing function.

        The function will be called before the task is submitted. We can set
        prepare function multiple times, and those functions will be called 
        according to the order they were added.

        arguments:
            func: (Callable) the preparing function

            *args: those positional arguments of the function

            **kw: those key word arguments of the function
        """
        if not isinstance(func, Callable):
            raise TypeError(('func must be a Callable, not '
                '{0}'.format(type(func).__name__)))
        self._prepares.append(_packing(func, *arg, **kw))

    def follow(self):
        """
        Call the following function.
        """
        # self._follow()
        for func in self._follows:
            func()

    def prepare(self):
        """
        Call the preparing function.
        """
        # self._prepare()
        for func in self._prepares:
            func()

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
                '{0}'.format(type(_comm).__name__)))
        self._comment = _comm
        
    def addSubtask(self, subtask: 'Subtask') -> 'Subtask':
        """
        Add a subtask to this task.

        All of the subtask will be submitted to the threading pool, and they
        will execute concurrently.

        arguments:
            subtask: (Subtask) the subtask to be added.
        """
        if not isinstance(subtask, Subtask):
            raise TypeError('subtask must be Subtask object, not '
                '{0}'.format(type(subtask).__name__))
        subtask.setParent(self)
        subtask.subtask_excepted.connect(self.setExcepted)
        subtask.subtask_completed.connect(self.checkCompleted)
        self._subtasks.append(subtask)
        return subtask

    def addSubtaskWithProgress(self, subtask: 'Subtask') -> 'Subtask':
        """
        Add a subtask with progress to this task by a function.

        All of the subtask will be submitted to the threading pool, and they
        will execute concurrently. Usually, only one subtask is with progress,
        whose progress will show in the screen.

        arguments:
            name: (str)

            func: (Callable) this function must accept the first argument as 
                the progress signal, while the other arguments are accepted as
                usual. Inside the function, the progress signal needs to emit
                periodically (which is controlled by the function).

            *arg: other positional arguments except the progress signal

            **kw: other keyword arguments
        """
        if not isinstance(subtask, Subtask):
            raise TypeError('subtask must be Subtask object, not '
                '{0}'.format(type(subtask).__name__))

        if self._has_progress:
            raise RuntimeError('Only one subtask with progress can be added. ' 
                'Use addSubtask() instead.')
            
        self.progress = 0
        subtask.setParent(self)
        subtask.subtask_progress.connect(self.setProgress)
        subtask.subtask_excepted.connect(self.setExcepted)
        subtask.subtask_completed.connect(self.checkCompleted)
        self._subtasks.append(subtask)
        self._has_progress = True
        return subtask

    def addSubtaskFunc(self, name: str, func: Callable, *arg, **kw) -> 'Subtask':
        """
        Add a subtask to this task by a function.

        All of the subtask will be submitted to the threading pool, and they
        will execute concurrently.

        arguments:
            name: (str) the name of subtask

            func: (Callable) the function to be executed concurrently

            *arg: positional arguments of the function

            **kw: keyword arguments of the function
        """
        subtask = Subtask(self)
        packed_func = _packing(func, *arg, **kw)
        subtask.setFunction(packed_func)
        subtask.name = name
        subtask.subtask_excepted.connect(self.setExcepted)
        subtask.subtask_completed.connect(self.checkCompleted)
        
        self._subtasks.append(subtask)
        return subtask



    def addSubtaskFuncWithProgress(self, 
            name: str, 
            func: Callable, 
            *arg, 
            **kw) -> 'SubtaskWithProgress':
        """
        Add a subtask with progress to this task by a function.

        All of the subtask will be submitted to the threading pool, and they
        will execute concurrently. Usually, only one subtask is with progress,
        whose progress will show in the screen.

        arguments:
            name: (str)

            func: (Callable) this function must accept the first argument as 
                the progress signal, while the other arguments are accepted as
                usual. Inside the function, the progress signal needs to emit
                periodically (which is controlled by the function).

            *arg: other positional arguments except the progress signal

            **kw: other keyword arguments
        """
        if self._has_progress:
            raise RuntimeError('Only one subtask with progress can be added. ' 
                'Use addSubtaskFunc() instead.')
            
        self.progress = 0
        subtask = SubtaskWithProgress(self)
        packed_func = _packing(func, 
            progress_signal = subtask.subtask_progress, *arg, **kw)
        subtask.setFunction(packed_func)
        subtask.name = name
        subtask.subtask_progress.connect(self.setProgress)
        subtask.subtask_excepted.connect(self.setExcepted)
        subtask.subtask_completed.connect(self.checkCompleted)
        self._subtasks.append(subtask)
        self._has_progress = True
        return subtask 

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
    def progress(self, _pg: int):
        """
        Set progress of the task.

        Usually we need to use a subtask to send signals about progressing.

        arguments:
            _pg: (int or None)
        """
        if not isinstance(_pg, int):
            # self._progress = 0
            raise TypeError('progress must be int, not '
                '{0}'.format(type(_pg).__name__))
        if _pg < 0 or _pg > 100:
            # self._progress = 0
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

        elif self.state == TaskState.Excepted:
            for subtask in self:
                if not subtask.completed:
                    return False
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
        self.task_progress.emit()
    
    def hasProgress(self) -> bool:
        """
        Returns whether this task has progress.

        If there is no progress, in screen the progress bar will show a busy
        indicator instead of a percentage of steps.
        """
        return self._has_progress

    def setExcepted(self):
        """
        Set the state of the task to TaskState.Excepted.

        When this function is called, this task or some of its subtask raised
        an exception. The exception will be recorded in log, and may open a 
        dialog to note the user.
        """
        self.state = TaskState.Excepted


class Subtask(QObject):
    """
    并发执行的子任务。
    
    通常由一个函数组成，在一个子线程中运行。多个子任务会组成一个任务 Task。子任务对应
    的函数返回后，在子线程中会调用 complete() 方法作为回调函数，从而发射信号表示该子
    任务已经完成。

    The Subtask that executes concurrently in a thread.
    
    A subtask consists one function. Usually there are several Subtask objects 
    in one Task object. After the function returns, the complete() method will 
    be called as the callback function, and emit a signal showing the subtask
    has been completed.

    signals:
        subtask_completed: emits when the function returns.

        subtask_excepted: emits when there is an unhandled exception raised.

    attributes:
        name: (str) the name of this subtask

        future: (futures.Future) the future object of the function. After the
            function returns, we can call future.result() method to get the 
            return values. However, if the function is still being executed,
            calling future.result() will block the main thread.

        completed: (bool) whether this subtask is completed.

        result: returns the result of the function. Will raise an exception
            if there has been an exception raised.

        exception: (None or BaseException) if there is an exception, it will
            saved in this variable.

        rec_exc: (None or str) traceback information if there is an exception
    """
    subtask_completed = Signal()    # emits when the subtask is completed
    subtask_excepted = Signal()     # emits when there is an exception raised

    def __init__(self, parent: QObject = None):
        super().__init__(parent)

        self._func = None
        self._name = 'anonymous'
        self._future = None
        self._result = None
        self._exception = None  # exception, if an exception occured
        self._rec_exc = None    # trace back exc when an exception occured
    
    def __str__(self):
        return '<Subtask> name: {0}'.format(self.name)

    def __repr__(self):
        return self.__str__()

    @property
    def completed(self) -> bool:
        """
        Returns whether the function has been completed.
        """
        if self.future:
            return self.future.done()
        else:
            return False

    @property
    def future(self) -> futures.Future:
        """
        Will return the Future object if the Task is submitted to the executor.
        If the task is still waiting or has never been submitted, this function
        will return None.
        """
        return self._future

    @future.setter
    def future(self, _ft: futures.Future):
        if not isinstance(_ft, futures.Future):
            raise TypeError('future must be Future object, not '
                '{0}'.format(type(_ft).__name__))
        self._future = _ft

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, _name: str):
        if not isinstance(_name, str):
            raise TypeError('name must be str, not '
                '{0}'.format(type(_name).__name__))
        self._name = _name

    @property
    def result(self):
        """
        If the subtask is not completed, returns None. 
        
        Otherwise, when the subtask is completed, self.complete() method is 
        called, and then the result can be gotten by this property.
        """
        return self._result

    @property
    def exception(self) -> BaseException:
        """
        If there is an exception raised when this subtask running, this method
        will return the exception. Otherwise, it will return None.
        """
        return self._exception

    @property
    def rec_exc(self) -> str:
        """
        If there is an exception raised when this subtask sunning, this method
        will return the traceback information. Otherwise, it will return None.
        """
        return self._rec_exc

    def getFunction(self) -> Callable:
        return self._func

    def complete(self, future: futures.Future):
        """
        Will emits a completed signal, and save the result.

        This function will act as a callback function, as an argument by 
        futures.Future.add_call_back() function.

        argument:
            future: (futures.Future) The same as self.future
        """
        try:
            self._result = future.result()
        except BaseException:   # set the task to TaskState.Excepted, 
                                # so there will be some exception handle work.
            self._exception = future.exception()
            self._rec_exc = traceback.format_exc()
            self.subtask_excepted.emit()
        finally:
            self.subtask_completed.emit()

    def setFunction(self, func: Callable):
        """
        Set the function to be executed in the threading pool.

        To use this method, we must first packing all the arguments into the
        callable (by lambda or other means). 

        If we use addSubtask() method from the Task object, it will help us to
        pack these arguments. 
        """
        if not isinstance(func, Callable):
            raise TypeError('func must be Callable, not '
                '{0}'.format(type(func).__name__))
        self._func = func

    # def getResult(self):
    #     """
    #     Returns the result of this subtask.

    #     NOTE: this function will returns None if the calculation
    #     has not been completed. Make sure the calculation is done
    #     when calling this function.
    #     """
    #     if not self.completed:
    #         print('Get Result is called, but not completed')
    #         return None
    #     else:
    #         return self.future.result()

class SubtaskWithProgress(Subtask):
    """
    带有 Progress 的子任务。
        
    该子任务需要将信号作为参数传递到函数中，并且在函数中定期发射信号说明进度。
    因此，所对应的函数也需要特殊定制，一般是在第一个参数设置为信号对象。

    This is a subtask with progress. 
        
    This subtask need to transfer a progress signal as an argument to the 
    function, and emit the signal periodically. So, the function need to be
    custom-made: the function must accept the signal as the first argument.
    """

    subtask_progress = Signal(int)

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        


class TaskQueueModel(QAbstractListModel):
    """
    用来查看等待队列中任务的 Model。

    这是 Qt 中 Model/View 架构的一部分。要显示等待队列，通过实例化 QListView，
    然后调用其 setModel() 方法，把这个类的实例传递进去。

    为了实现只读的、显示与数据分离的架构，这个 Model 类必须实现如下方法：
        - rowCount(self, parent: QModelIndex) -> int
            返回相应的 parent 之下有多少行

        - data(self, index: QModelIndex, role: int)
            根据 role 的不同，返回数据结构中内部存储的数据

    This is a model for viewing the tasks in the waiting queue.

    This is a part of Model/View architecture of Qt. If we want to display the
    path tree, we can instantiate QTreeView, and call its setModel() method.

    In order to realize a read-only and data-display decoupled architecture, we
    need to reimplement the following methods:
        - rowCount(self, parent: QModelIndex) -> int
            Get number of rows under the parent

        - data(self, index: QModelIndex, role: int)
            Return the internal data according to the role
    """
    def __init__(self, task_manager: TaskManager):
        """
        arguments
            task_manager: (TaskManager) to get the waiting queue.
        """
        super().__init__()
        self._task_manager = task_manager

    @property
    def task_manager(self) -> TaskManager:
        return self._task_manager

    @property
    def task_queue(self) -> TaskQueue:
        return self.task_manager.task_queue

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        arguments:
            parent: (QModelIndex) usually must be QModelIndex()

        returns:
            (int) length of task queue.
        """
        if not parent.isValid():
            return len(self.task_queue)
        else:
            return 0

    def data(self, index: QModelIndex, role: int):
        """
        arguments:
            index: (QModelIndex)

            role: (Qt.ItemDataRole)

        returns:
            If role is Qt.DisplayRole, returns str.
        """
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            _task = self.task_queue[index.row()]
            return _task.name
        elif role == Qt.ToolTipRole:
            _task = self.task_queue[index.row()]
            return '<Task>: {0}, state: {1}'.format(
                _task.name, _task.state
            )
        else:
            return None

    def addTask(self, task: Task):
        """
        Add a task to the task queue.

        arguments:
            task: (Task)
        """
        self.beginInsertRows(
            QModelIndex(), 
            self.rowCount(), 
            self.rowCount()
        )
        self.task_queue.addTask(task)
        self.endInsertRows()
        
    def popTask(self) -> Task:
        """
        Get a task from the task queue to submit.

        arguments:
            task: (Task)
        """
        self.beginRemoveRows(QModelIndex(), 0, 0)
        task = self.task_queue.popTask()
        self.endRemoveRows()
        return task

    def cancelTask(self, index: QModelIndex) -> Task:
        """
        Remove a task from the task queue.

        arguments:
            index: (QModelIndex) 
        """
        if not index.isValid():
            raise ValueError('Cannot cancel task: invalid index')
        self.beginRemoveRows(
            QModelIndex(),
            index.row(),
            index.row(),
        )
        task = self.task_queue.cancelTask(index.row())
        self.endRemoveRows()
        return task


class SubtaskListModel(QAbstractListModel):
    """
    用来查看 Task 中下属 Subtask 信息的 Model。

    这是 Qt 中 Model/View 架构的一部分。要显示等待队列，通过实例化 QListView，
    然后调用其 setModel() 方法，把这个类的实例传递进去。

    为了实现只读的、显示与数据分离的架构，这个 Model 类必须实现如下方法：
        - rowCount(self, parent: QModelIndex) -> int
            返回相应的 parent 之下有多少行

        - data(self, index: QModelIndex, role: int)
            根据 role 的不同，返回数据结构中内部存储的数据

    This is a model for viewing information of subtasks of the task.

    This is a part of Model/View architecture of Qt. If we want to display the
    path tree, we can instantiate QTreeView, and call its setModel() method.

    In order to realize a read-only and data-display decoupled architecture, we
    need to reimplement the following methods:
        - rowCount(self, parent: QModelIndex) -> int
            Get number of rows under the parent

        - data(self, index: QModelIndex, role: int)
            Return the internal data according to the role
    """

    def __init__(self, task: Task):
        super().__init__()
        self._task = task

    @property
    def task(self) -> Task:
        return self._task 

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        arguments:
            parent: (QModelIndex) usually must be QModelIndex()

        returns:
            (int) number of subtasks.
        """
        return len(self.task)

    def data(self, index: QModelIndex, role: int):
        """
        arguments:
            index: (QModelIndex)

            role: (Qt.ItemDataRole)

        returns:
            If role is Qt.DisplayRole, returns str.
        """
        if not index.isValid():
            return None

        subtask = self.task[index.row()]
        name = subtask.name

        if role == Qt.DisplayRole:
            if subtask.completed:
                return '{0} (completed)'.format(name)
            else:
                return '{0}'.format(name)

        elif role == Qt.ToolTipRole:
            if subtask.completed:
                return '<Subtask>: {0} (completed)'.format(name)
            else:
                return '<Subtask>: {0}'.format(name)


class HistoryTaskModel(QAbstractListModel):
    """
    用来查看历史任务的 Model。

    这是 Qt 中 Model/View 架构的一部分。要显示等待队列，通过实例化 QListView，
    然后调用其 setModel() 方法，把这个类的实例传递进去。

    为了实现只读的、显示与数据分离的架构，这个 Model 类必须实现如下方法：
        - rowCount(self, parent: QModelIndex) -> int
            返回相应的 parent 之下有多少行

        - data(self, index: QModelIndex, role: int)
            根据 role 的不同，返回数据结构中内部存储的数据

    This is a model for viewing history tasks.

    This is a part of Model/View architecture of Qt. If we want to display the
    path tree, we can instantiate QTreeView, and call its setModel() method.

    In order to realize a read-only and data-display decoupled architecture, we
    need to reimplement the following methods:
        - rowCount(self, parent: QModelIndex) -> int
            Get number of rows under the parent

        - data(self, index: QModelIndex, role: int)
            Return the internal data according to the role
    """

    def __init__(self, task_manager: TaskManager):
        super().__init__()
        self._task_manager = task_manager

    @property
    def task_manager(self) -> TaskManager:
        return self._task_manager

    @property
    def history_list(self) -> list:
        return self._task_manager.task_queue.history_list

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        arguments:
            parent: (QModelIndex) usually must be QModelIndex()

        returns:
            (int) number of history tasks.
        """
        return len(self.history_list)

    def data(self, index: QModelIndex, role: int):
        """
        arguments:
            index: (QModelIndex)

            role: (Qt.ItemDataRole)

        returns:
            If role is Qt.DisplayRole, returns str.
        """
        if not index.isValid():
            return None
        task = self.history_list[index.row()]
        if role == Qt.DisplayRole:
            return task.name
        elif role == Qt.ToolTipRole:
            return '<Task>: {0}, state: {1}'.format(
                task.name, task.state
            )


        

