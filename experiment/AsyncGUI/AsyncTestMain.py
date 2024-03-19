# -*- coding: utf-8 -*- 

"""
这个小项目用来试验，如何将 Asynchronous 无痛地融合进 PySide6 软件中，
把现有的拿到文件的函数该如何做到。
"""

import sys 
import asyncio 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget 
from qasync import QEventLoop, asyncSlot
from PySide6.QtCore import Signal

class MainWindow(QMainWindow):
    async_worker_completed = Signal(object)

    def __init__(self):
        super().__init__()
        self.initUi()

    async def fetch_data(self):
        await asyncio.sleep(2)  # 模拟延迟
        return "获取到的数据"

    @asyncSlot()
    async def on_button_clicked(self):
        data = await self.fetch_data()
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
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    
    app_close_event = asyncio.Event()
    app.aboutToQuit.connect(app_close_event.set)
    mainWindow = MainWindow()
    mainWindow.show()
    
    loop.run_until_complete(app_close_event.wait())
    loop.close()