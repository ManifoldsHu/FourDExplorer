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
from PySide6.QtCore import Qt, QSize
from Constants import UIThemeDensity

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
# from PySide6.QtGui import 

from bin.TabViewManager import TabViewManager
from bin.UIManager import ThemeHandler
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

        self._initControlPanel()
        
        self._initFile()
        self._initEdit()
        
        self._initTask()
        self._initDataset()
        # self._initCalibration()
        self._initImage()
        self._initTabViewers()
        self._initSettings()
    
    @property
    def tabview_manager(self) -> TabViewManager:
        return self._tabview_manager

    @property
    def theme_handler(self) -> ThemeHandler:
        global qApp 
        return qApp.theme_handler
        
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
        self._menu_vector_field.addAction(self._action_open_vector_field)

        self._action_open_fourdstem = ActionOpenFourDSTEM(self)
        self._action_virtual_image = ActionVirtualImage(self)
        self._action_center_of_mass = ActionCenterOfMass(self)
        self._action_background = ActionBackground(self)
        self._action_align = ActionAlign(self)
        self._action_rotate = ActionRotate(self)
        self._menu_fourdstem.addAction(self._action_open_fourdstem)
        self._menu_fourdstem.addAction(self._action_import_fourdstem)
        self._menu_fourdstem.addSeparator()
        self._menu_fourdstem.addAction(self._action_virtual_image)
        self._menu_fourdstem.addAction(self._action_center_of_mass)
        self._menu_fourdstem.addSeparator()
        self._menu_fourdstem.addAction(self._action_background)
        self._menu_fourdstem.addAction(self._action_align)
        self._menu_fourdstem.addAction(self._action_rotate)
        
        
        
    # def _initDatasetSubmenus(self):
    #     """
    #     Initialize the submenus in the Dataset menu.
    #     """
        

        # self._dataset_submenu_rc = ':/HDFItems/resources/icons/'
        # icon_line = self.theme_handler.iconProvider(
        #     self._dataset_submenu_rc + 'line.png'
        # )


    # def _updateSubMenuIcons(self, rc_path: str):
    #     """
    #     Update the icons using resource path.

    #     arguments:
    #         rc_path: (str) the icon's resource path
    #     """
    #     icon = self.theme_handler.iconProvider(rc_path)


    def _initCalibration(self):
        pass



    def _initImage(self):
        pass


    def _initTabViewers(self):
        """
        Initialize the viewers (tabWidgets)
        """
        self._tabview_manager = TabViewManager(self)
        self._tabview_manager.setTabWidget(self.ui.tabWidget_view)
        self._tabview_manager.initializeTabView()



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
        UIThemeDensity.Large: 36,
        UIThemeDensity.Big: 33,
        UIThemeDensity.Normal: 30,
        UIThemeDensity.Small: 27,
        UIThemeDensity.Tiny: 24,
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

