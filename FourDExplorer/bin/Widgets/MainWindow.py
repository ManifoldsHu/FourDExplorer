# -*- coding: utf-8 -*-

"""
*------------------------------ MainWindow.py --------------------------------*

4D-Explorer 程序主界面。

作者：          胡一鸣
创建时间：      2021年8月21日

The Main Window of the 4D-Explorer software.

author:             Hu Yiming
date:               Feb 24, 2022
*------------------------------ MainWindow.py --------------------------------*
"""

import sys
import os

from PySide6.QtWidgets import QMainWindow 
from PySide6.QtWidgets import QToolBar
from PySide6.QtWidgets import QWidget 
from PySide6.QtWidgets import QToolButton 
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QProgressBar
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtCore import QSize
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon

from Constants import ROOT_PATH
from Constants import UIThemeDensity

import psutil

from bin.Actions.ControlActions import ActionSettings
from bin.Actions.ControlActions import ControlActionGroup

from bin.Actions.DataActions import ActionOpenDataAs
from bin.Actions.DataActions import ActionOpenLine
from bin.Actions.DataActions import ActionOpenImage 
from bin.Actions.DataActions import ActionOpenVectorField
from bin.Actions.DataActions import ActionOpenFourDSTEM

from bin.Actions.EditActions import ActionAttributes
from bin.Actions.EditActions import ActionChangeHDFType
from bin.Actions.EditActions import ActionCopy
from bin.Actions.EditActions import ActionDelete
from bin.Actions.EditActions import ActionImportFourDSTEM
from bin.Actions.EditActions import ActionImportImage
from bin.Actions.EditActions import ActionMove
from bin.Actions.EditActions import ActionNew
from bin.Actions.EditActions import ActionRename

from bin.Actions.FileActions import ActionCloseFile
from bin.Actions.FileActions import ActionNewFile
from bin.Actions.FileActions import ActionOpenFile
from bin.Actions.FileActions import ActionQuit

from bin.Actions.FourDSTEMActions import ActionAlign
from bin.Actions.FourDSTEMActions import ActionBackground
from bin.Actions.FourDSTEMActions import ActionCenterOfMass
from bin.Actions.FourDSTEMActions import ActionRotate
from bin.Actions.FourDSTEMActions import ActionVirtualImage
from bin.Actions.FourDSTEMActions import ActionPlotCTF
from bin.Actions.FourDSTEMActions import ActionEditParam
from bin.Actions.VectorFieldActions import ActionCurl
from bin.Actions.VectorFieldActions import ActionFlipComponents
from bin.Actions.VectorFieldActions import ActionPotential
from bin.Actions.VectorFieldActions import ActionRotateVector
from bin.Actions.VectorFieldActions import ActionSliceI
from bin.Actions.VectorFieldActions import ActionSliceJ
from bin.Actions.VectorFieldActions import ActionSubtractMeanVector
from bin.Actions.VectorFieldActions import ActionSubtractReferenceVector

from bin.Actions.HelpActions import ActionAbout
# from PySide6.QtGui import 

from bin.TabViewManager import TabViewManager
from bin.UIManager import ThemeHandler
from bin.TaskManager import TaskManager
from bin.Widgets.PageHome import PageHome
from bin.Widgets.PageSettings import PageSettings
from ui.uiMainWindow import Ui_MainWindow
from ui import icon_rc


class MainWindow(QMainWindow):
    """
    4D-Explorer 主界面类。

    Ui 文件地址: ROOT_PATH/ui/uiMainWindow.ui

    This is the class to control the main window of 4D-Explorer.

    The path of Ui file: ROOT_PATH/ui/uiMainWindow.ui
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global qApp
        self._app = qApp

        self.setWindowTitle('4D-Explorer')
        icon = QIcon()
        icon_path = os.path.join(ROOT_PATH, 'ui', 'resources', 'icons', '4D.ico')
        icon.addFile(icon_path)
        self.setWindowIcon(icon)
        self.showMaximized()

        self._initControlPanel()
        
        self._initFile()
        self._initEdit()
        
        self._initTask()
        self._initDataset()
        # self._initCalibration()
        self._initImage()
        self._initTabViewers()
        self._initSettings()
        self._initHelp()

        self.ui.tab_pages.initModel()
        self.tabview_manager.signal_tab_closed.connect(self.ui.tab_pages.initModel)
        self.tabview_manager.signal_tab_opened.connect(self.ui.tab_pages.initModel)
        self._status_bar = self.statusBar()
        self._initStatusBar()
    
    @property
    def tabview_manager(self) -> TabViewManager:
        return self._tabview_manager

    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler
    
    @property
    def task_manager(self) -> TaskManager:
        global qApp 
        return qApp.task_manager
        
    def _initControlPanel(self):
        """
        Initialize the control panel on the left of the MainWindow.
        """
        self.control_tool_bar = ControlToolBar(self)
        self.control_tool_bar.initActions(self)
        self.addToolBar(Qt.LeftToolBarArea, self.control_tool_bar)
        self.ui.menuView_V.addActions(
            self.control_tool_bar.action_group.actions()
        )

    def _initFile(self):
        """
        Initialize the file menu.
        """
        self._action_new_file = ActionNewFile(self)
        self._action_open_file = ActionOpenFile(self)
        self._action_close_file = ActionCloseFile(self)
        
        self._action_quit = ActionQuit(self)
        self.ui.menuFile_F.addAction(self._action_new_file)
        self.ui.menuFile_F.addAction(self._action_open_file)
        self.ui.menuFile_F.addAction(self._action_close_file)
        self.ui.menuFile_F.addSeparator()
        
        self.ui.menuFile_F.addAction(self._action_quit)
        
    def _initEdit(self):
        """
        Initialize the edit menu.
        """
        self._action_new = ActionNew(self)
        self._action_import_fourdstem = ActionImportFourDSTEM(self)
        self._action_import_image = ActionImportImage(self)
        self._action_move = ActionMove(self)
        self._action_copy = ActionCopy(self)
        self._action_delete = ActionDelete()
        self._action_rename = ActionRename(self)
        self._action_attributes = ActionAttributes(self)
        self._action_change = ActionChangeHDFType(self)

        self.ui.menuEdit_E.addActions([
            self._action_new,
            self._action_change,
            self._action_import_fourdstem,
            self._action_import_image,
            self._action_move,
            self._action_copy,
            self._action_delete,
            self._action_rename,
            self._action_attributes,
        ])
        self.ui.menuEdit_E.insertSeparator(self._action_change)
        self.ui.menuEdit_E.insertSeparator(self._action_move)
        self.ui.menuEdit_E.insertSeparator(self._action_attributes)

    def _initSettings(self):
        """
        Initialize the settings menu.
        """
        self._action_settings = self.control_tool_bar._action_settings
        self.ui.menuSettings_S.addAction(self._action_settings)

    def _initTask(self):
        pass

    def _initDataset(self):
        """
        Initialize the dataset menu.
        """
        self._action_open_data_as = ActionOpenDataAs(self)
        self.ui.menuDataset_D.addAction(self._action_open_data_as)
        self.ui.menuDataset_D.addAction(self._action_change)
        self.ui.menuDataset_D.addSeparator()

        self._menu_line = self.ui.menuDataset_D.addMenu('Line')
        self._menu_image = self.ui.menuDataset_D.addMenu('Image')
        self._menu_vector_field = self.ui.menuDataset_D.addMenu('Vector Field')
        self._menu_fourdstem = self.ui.menuDataset_D.addMenu('4D-STEM')

        self._action_open_line = ActionOpenLine(self)
        self._menu_line.addAction(self._action_open_line)

        self._action_open_image = ActionOpenImage(self)
        self._menu_image.addAction(self._action_open_image)
        self._menu_image.addAction(self._action_import_image)

        self._action_open_vector_field = ActionOpenVectorField(self)
        self._action_rotate_vector = ActionRotateVector(self)
        self._action_subtract_mean_vector = ActionSubtractMeanVector(self)
        self._action_subtract_reference_vector = ActionSubtractReferenceVector(self)
        self._action_flip_components = ActionFlipComponents(self)
        self._action_potential = ActionPotential(self)
        self._action_curl = ActionCurl(self)
        self._action_slice_i = ActionSliceI(self)
        self._action_slice_j = ActionSliceJ(self)
        self._menu_vector_field.addAction(self._action_open_vector_field)
        self._menu_vector_field.addSeparator()
        self._menu_vector_field.addAction(self._action_subtract_mean_vector)
        self._menu_vector_field.addAction(self._action_subtract_reference_vector)
        self._menu_vector_field.addAction(self._action_rotate_vector)
        self._menu_vector_field.addAction(self._action_flip_components)
        self._menu_vector_field.addSeparator()
        self._menu_vector_field.addAction(self._action_potential)
        self._menu_vector_field.addAction(self._action_curl)
        self._menu_vector_field.addAction(self._action_slice_i)
        self._menu_vector_field.addAction(self._action_slice_j)

        self._action_open_fourdstem = ActionOpenFourDSTEM(self)
        self._action_virtual_image = ActionVirtualImage(self)
        self._action_center_of_mass = ActionCenterOfMass(self)
        self._action_background = ActionBackground(self)
        self._action_align = ActionAlign(self)
        self._action_rotate = ActionRotate(self)
        self._action_plot_ctf = ActionPlotCTF(self)
        self._action_edit_param = ActionEditParam(self)
        self._menu_fourdstem.addAction(self._action_open_fourdstem)
        self._menu_fourdstem.addAction(self._action_import_fourdstem)
        self._menu_fourdstem.addSeparator()
        self._menu_fourdstem.addAction(self._action_virtual_image)
        self._menu_fourdstem.addAction(self._action_center_of_mass)
        self._menu_fourdstem.addSeparator()
        self._menu_fourdstem.addAction(self._action_edit_param)
        self._menu_fourdstem.addAction(self._action_background)
        self._menu_fourdstem.addAction(self._action_align)
        self._menu_fourdstem.addAction(self._action_rotate)
        self._menu_fourdstem.addSeparator()
        self._menu_fourdstem.addAction(self._action_plot_ctf)


    def _initCalibration(self):
        pass


    def _initImage(self):
        pass

    def _initHelp(self):
        """
        Initialize the help menu.
        """
        self._action_about = ActionAbout(self)
        self.ui.menuHelp_H.addAction(self._action_about)

    def _initTabViewers(self):
        """
        Initialize the viewers (tabWidgets)
        """
        self._tabview_manager = TabViewManager(self)
        self._tabview_manager.setTabWidget(self.ui.tabWidget_view)
        self._tabview_manager.initializeTabView()

        
    def _initStatusBar(self):
        """
        Initialize the status bar to show the current progress of task (from 
        TaskManager) and system information.
        """
        self._status_label = QLabel("Ready")
        self._status_bar.addWidget(self._status_label)
        
        self._task_progress_bar = QProgressBar()
        self._task_progress_bar.setMaximumWidth(200)
        self._task_progress_bar.setMaximumHeight(10)
        self._task_progress_bar.setVisible(False)
        self._status_bar.addWidget(self._task_progress_bar)
        
        self.task_manager.task_info_refresh.connect(self._updateTaskStatus)
        self.task_manager.progress_updated.connect(self._updateTaskStatus)
        self.task_manager.task_exception.connect(self._updateTaskStatus)
        
        # Add system information widget
        self._system_info_label = QLabel("CPU: 0%  Memory: 0%  Disk: 0%")
        self._status_bar.addPermanentWidget(self._system_info_label)
        
        disk_io = psutil.disk_io_counters()
        if hasattr(disk_io, 'read_bytes') and hasattr(disk_io, 'write_bytes'):
            self._last_read_bytes = disk_io.read_bytes
            self._last_write_bytes = disk_io.write_bytes
        else:
            self._last_read_bytes = 0
            self._last_write_bytes = 0
        
        # Set up a timer to update system information periodically
        self._system_info_timer = QTimer(self)
        self._system_info_timer.timeout.connect(self._updateSystemInfo)
        self._system_info_timer.start(1000)  # Update every 1000 ms (1 second)
        
        
        
    def _updateSystemInfo(self):
        """
        Update the system information labels in the status bar.
        """
        # Update CPU usage
        cpu_percent = psutil.cpu_percent()
        
        # Update memory usage
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        
        # Update disk usage
        disk_usage = psutil.disk_usage(os.getcwd())
        disk_percent = disk_usage.percent
        
        # Update IO rate
        disk_io = psutil.disk_io_counters()
        if hasattr(disk_io, 'read_bytes') and hasattr(disk_io, 'write_bytes'):
            read_rate = (disk_io.read_bytes - self._last_read_bytes) / 2**20
            write_rate = (disk_io.write_bytes - self._last_write_bytes) / 2**20
            io_rate = read_rate + write_rate
            self._last_read_bytes = disk_io.read_bytes
            self._last_write_bytes = disk_io.write_bytes
            io_info = f"  IO: {io_rate:.1f} MiB/s"
        else:
            io_info = ""
        
        self._system_info_label.setText(f"CPU: {cpu_percent:.0f}%  Memory: {memory_percent:.0f}%  Disk: {disk_percent:.0f}%{io_info}")
        

    def _updateTaskStatus(self):
        """
        Update the status bar to show the current progress of the task.
        """
        if self.task_manager.current_task is None:
            self._task_progress_bar.setVisible(False)
            self._status_label.setText("Ready")
        else:
            self._status_label.setText("Executing Task")
            self._task_progress_bar.setVisible(True)
            self._task_progress_bar.setValue(self.task_manager.current_task.progress)

            if self.task_manager.current_task.hasProgress():
                self._task_progress_bar.setRange(0, 100)  # Percentage of step
            else:
                self._task_progress_bar.setRange(0, 0)  # Busy indicator
        
        


    def close(self) -> bool:
        self._app.cleanResources()
        super(MainWindow, self).close()



class ControlToolBar(QToolBar):
    """
    This toolbar is used to show the control panel.

    A toolbar that do not show the border line.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        
        self._action_group = ControlActionGroup(self)
        self._action_settings = ActionSettings(self)
        self.setMovable(False)
        self.setContentsMargins(0,0,0,0)
        self.layout().setContentsMargins(0,0,0,0)
        self.setOrientation(Qt.Vertical)
        
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self._updateStyle()
        self.theme_handler.theme_changed.connect(self._updateStyle)

    @property
    def action_group(self) -> ControlActionGroup:
        return self._action_group

    @property
    def action_settings(self) -> ActionSettings:
        return self._action_settings

    @property 
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler

    def initActions(self, main_window: MainWindow):
        """
        Initialize Actions to their corresponding widgets.
        """
        stacked_widget = main_window.ui.stackedWidget_control
        self.action_group.setStackedWidget(stacked_widget)
        for index, action in enumerate(self.action_group.actions()):
            action.setLinkedWidget(stacked_widget.widget(index))
            self.addAction(action)
        self.initSettingButton()

    def initSettingButton(self):
        """
        Initialize Setting Action.
        """
        self._setting_button = QToolButton(self)
        self._setting_button.setIcon(self._action_settings.icon())
        self._setting_button.clicked.connect(self._action_settings.trigger)
        self._vertical_spacer = QWidget(self)
        self._vertical_spacer.setSizePolicy(
            QSizePolicy.Preferred, 
            QSizePolicy.Expanding,
        )
        self.addWidget(self._vertical_spacer)
        self.addWidget(self._setting_button)
        self.theme_handler.theme_changed.connect(
            lambda: self._setting_button.setIcon(
                self._action_settings.icon()
            )
        )
        
    density_to_button_width = {
        UIThemeDensity.VeryHuge: 48,
        UIThemeDensity.Huge: 45,
        UIThemeDensity.VeryLarge: 42,
        UIThemeDensity.Large: 39,
        UIThemeDensity.VeryBig: 36,
        UIThemeDensity.Big: 33,
        UIThemeDensity.Normal: 30,
        UIThemeDensity.Small: 27,
        UIThemeDensity.VerySmall: 24,
        UIThemeDensity.Tiny: 21,
        UIThemeDensity.VeryTiny: 18,
    }

    def _updateStyle(self):
        """
        Update the style according to the current theme.
        """
        _width = self.density_to_button_width[
            self.theme_handler.theme_density
        ]
        _height = _width + 20
        
        self.setStyleSheet(
            "ControlToolBar{{border: none; padding: 0px;}}"
            "ControlToolBar::separator{{width: 0px;}}"
            "ControlToolBar QToolButton{{padding: 0; margin: 0;}}"
            "ControlToolBar QToolButton{{height: {0}px; width: {1}px;}}"
            "".format(_height, _width)
        )
        self.setIconSize(QSize(_width - 5, _width - 5))


