# -*- coding: utf-8 -*-

"""
这个小项目用来试验，如何将 Asynchronous 无痛地融合进 PySide6 软件中。

在这个文件中，使用的方法是: 另起一个线程，并在其中跑事件循环。
"""

import sys 
import asyncio 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget 
from PySide6.QtCore import QObject, Signal, QThread 

class AsyncLoopRunner(QObject):
    def __init__(self, loop):
        super().__init__()
        self.loop = loop 

    def run(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

global_thread = QThread()
global_loop = asyncio.new_event_loop()

loop_runner = AsyncLoopRunner(global_loop)
loop_runner.moveToThread(global_thread)

global_thread.started.connect(loop_runner.run)
global_thread.start()

def run_async(func, *args, **kwargs):
    task = asyncio.ensure_future(func(*args, **kwargs), loop = global_loop)
    return task 

# 异步执行装饰器 
def async_execute(callback_signal_name: str):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            async def async_func():
                result = await func(self, *args, **kwargs)
                getattr(self, callback_signal_name).emit(result)
            asyncio.run_coroutine_threadsafe(async_func(), global_loop)
        return wrapper
    return decorator 


class MainWindow(QMainWindow):
    async_worker_completed = Signal(object)

    def __init__(self):
        super().__init__()
        self.initUi()
        self.async_worker_completed.connect(self.on_data_fetched)

    @async_execute("async_worker_completed")
    async def fetch_data(self):
        await asyncio.sleep(2)  # 模拟延迟
        return "获取到的数据"

    def on_button_clicked(self):
        self.fetch_data()

    def on_data_fetched(self, data):
        self.label.setText(data)

    def initUi(self):
        self.setWindowTitle("Async Task Example")
        self.resize(300, 200)
        layout = QVBoxLayout()

        self.label = QLabel("按下按钮开始异步操作", self)
        self.button = QPushButton("开始", self)
        self.button.clicked.connect(self.on_button_clicked)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
