# -*- coding: utf-8 -*-



import sys
import os
from PySide6.QtWidgets import QMainWindow
from ui.uiMainWindow import Ui_MainWindow




class MainWindow(QMainWindow,):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        

# class MainWindow(QMainWindow, QtStyleTools):
#     def __init__(self):
#         super().__init__()
#         self.ui = QUiLoader().load('uiMainWindow.ui', self)
#         self.apply_stylesheet(self.ui, theme = 'light_blue.xml')


# if __name__ == '__main__':
    
#     # dirname = os.path.dirname(PySide6.__file__)
#     # plugin_path = os.path.join(dirname, 'plugins', 'platforms')
#     # os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     # apply_stylesheet(app, theme='light_blue.xml')
#     # apply_stylesheet(app, theme='dark_blue.xml')
#     # apply_stylesheet(app, theme = 'dark_amber.xml')
#     sys.exit(app.exec())

