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

作者：          胡一鸣
创建时间：      2021年12月28日

These are asynchronous dispatchers of concurrent tasks using threading or mult-
iprocessing pool from concurrent.futures . The task managers communicate with 
the main event loop by pyqtSignals. As for now, the only threading pool is ava-
ilable.

*------------------------------ TaskManager.py -------------------------------*
'''