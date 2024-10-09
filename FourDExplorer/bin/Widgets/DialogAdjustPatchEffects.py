# -*- coding: utf-8 -*-

"""
*----------------------- DialogAdjustPatchEffects.py -------------------------*
包含了一些适合于调整 matplotlib 库的 patch 属性的对话框。

作者：          胡一鸣
创建日期：      2024年9月24日

Some dialogs that can adjust patches of matplotlib.

author:         Hu Yiming
date:           Sep 24, 2024
*----------------------- DialogAdjustPatchEffects.py -------------------------*
"""

from logging import Logger 

from PySide6.QtWidgets import QDialog 
from PySide6.QtWidgets import QWidget

import numpy as np 
from matplotlib.patches import Patch
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
from matplotlib.patches import Ellipse 
from matplotlib.patches import Wedge
from matplotlib.patches import Annulus
from matplotlib.patches import Arc 
from matplotlib.patches import Polygon 
from matplotlib.patches import RegularPolygon
from matplotlib.patches import CirclePolygon
from matplotlib.lines import Line2D
from matplotlib.axes import Axes 
from matplotlib.figure import Figure 
from matplotlib.colors import to_hex 

from bin.BlitManager import BlitManager

from ui.uiDialogAdjustPatchEffects import Ui_Dialog

TableauColors = {
    'black': '#000000',
    'white': '#FFFFFF',
    'tab:blue': '#1f77b4',
    'tab:orange': '#ff7f0e',
    'tab:green': '#2ca02c',
    'tab:red': '#d62728',
    'tab:purple': '#9467bd',
    'tab:brown': '#8c564b',
    'tab:pink': '#e377c2',
    'tab:gray': '#7f7f7f',
    'tab:olive': '#bcbd22',
    'tab:cyan': '#17becf'
}

class DialogAdjustPatchEffects(QDialog):
    """
    用于调整 Patch 的显示效果的对话框。包括：
        - 透明度 (alpha)
        - 边缘颜色
        - 内部颜色
        - 是否填充
        - 线样式
        - 线宽
        - 点形 (hatch)
    
    Dialog to adjust displaying effects, including:
        - alpha
        - edge color
        - face color
        - fill
        - line style
        - line width
        - hatch
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        
        self._patch = None 
        self._blit_manager = None 
        self.initial_alpha = 1
        self.initial_edge_color = 'k'
        self.initial_face_color = 'k'
        self.initial_hatch = None
        self.initial_line_style = '-'
        self.initial_line_width = 2
        self.initial_fill = False 
        self._patches = []
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._initUi()
        
    @property 
    def patch(self) -> Patch:
        return self._patch 
    
    @property
    def patches(self) -> list[Patch]:
        return self._patches
    
    @property
    def axes(self) -> Axes:
        return self.patch.axes

    @property
    def figure(self) -> Figure:
        return self.patch.figure

    @property
    def blit_manager(self) -> BlitManager:
        return self._blit_manager

    @property
    def logger(self) -> Logger:
        global qApp
        return qApp.logger


    def initialize(self, patch: Patch, blit_manager: BlitManager):
        """
        Set the patch and blit manager.
        
        arguments:
            patch: (Patch) the patch to be adjusted.
            
            blit_manager: (BlitManager) the blit manager to be used.
        """
        if patch not in blit_manager.artists():
            raise RuntimeError("patch not in blit manager")
        self._patches.append(patch)
        self._patch = patch
        self._blit_manager = blit_manager
        
        # Set dialog name and label artist name according to the kind of the patch
        patch_type_mapping = {
            Arc: "Arc",
            Polygon: "Polygon",
            Circle: "Circle",
            Annulus: "Ring",
            Wedge: "Wedge",
            Rectangle: "Rectangle",
            Ellipse: "Ellipse",
            RegularPolygon: "Regular Polygon",
            CirclePolygon: "Circle Polygon",
            Patch: "Patch"
        }
        
        patch_type = type(patch)
        patch_name = patch_type_mapping.get(patch_type, "Patch")
        
        self.setWindowTitle(f"Adjust {patch_name} Effects")
        self.ui.label_patch_kind.setText(patch_name)
        
        self.initialize_effects()
        
    def initializePatches(self, patches: list[Patch], blit_manager: BlitManager):
        """
        Set the patches and blit manager.
        
        arguments:
            patches: (list[Patch]) the patches to be adjusted.
            
            blit_manager: (BlitManager) the blit manager to be used.
        """
        for p in patches:
            if p not in blit_manager.artists():
                raise RuntimeError(f"patch not in blit manager: {p}")
            self._patches.append(p) 
        self._patch = patches[0]
        self._blit_manager = blit_manager 
        
        # Set dialog name and label artist name according to the kind of the patch
        patch_type_mapping = {
            Arc: "Arc",
            Polygon: "Polygon",
            Circle: "Circle",
            Annulus: "Ring",
            Wedge: "Wedge",
            Rectangle: "Rectangle",
            Ellipse: "Ellipse",
            RegularPolygon: "Regular Polygon",
            CirclePolygon: "Circle Polygon",
            Patch: "Patch",
        }
        patch_type = type(patches[0])
        patch_name = patch_type_mapping.get(patch_type, "Patch")
        
        self.setWindowTitle(f"Adjust {patch_name} Effects")
        self.ui.label_patch_kind.setText(patch_name)
        
        self.initialize_effects()
            
        
        
    def _initUi(self):
        """
        Initialize the UI.
        """
        # Connect signals to slots
        self.ui.doubleSpinBox_alpha.valueChanged.connect(self.update_alpha)
        self.ui.comboBox_edge_color.currentIndexChanged.connect(self.update_edge_color)
        self.ui.comboBox_face_color.currentIndexChanged.connect(self.update_face_color)
        self.ui.comboBox_hatch.currentIndexChanged.connect(self.update_hatch)
        self.ui.comboBox_line_style.currentIndexChanged.connect(self.update_line_style)
        self.ui.doubleSpinBox_line_width.valueChanged.connect(self.update_line_width)
        self.ui.checkBox_fill.stateChanged.connect(self.update_fill)
        
        self.ui.pushButton_ok.clicked.connect(self.ok)
        self.ui.pushButton_cancel.clicked.connect(self.cancel)        
        
    def initialize_effects(self):
        """
        Initialize the UI with the current patch effects.
        """
        
        known_colors = TableauColors
        # Convert the edge and face colors to hex and find the corresponding name
        edge_color_hex = to_hex(self.patch.get_edgecolor())
        face_color_hex = to_hex(self.patch.get_facecolor())
        edge_color_name = 'others'
        face_color_name = 'others'
        for name, hex_value in known_colors.items():
            if edge_color_hex == hex_value:
                edge_color_name = name
            if face_color_hex == hex_value:
                face_color_name = name
        
        
        self.initial_alpha = self.patch.get_alpha()
        self.initial_edge_color = self.patch.get_edgecolor()
        self.initial_face_color = self.patch.get_facecolor()
        self.initial_hatch = self.patch.get_hatch()
        self.initial_line_style = self.patch.get_linestyle()
        self.initial_line_width = self.patch.get_linewidth()
        self.initial_fill = self.patch.get_fill()
        
        self.ui.doubleSpinBox_alpha.setValue(self.patch.get_alpha())
        self.ui.comboBox_edge_color.setCurrentText(edge_color_name)
        self.ui.comboBox_face_color.setCurrentText(face_color_name)
        self.ui.comboBox_hatch.setCurrentText(self.patch.get_hatch())
        self.ui.comboBox_line_style.setCurrentText(self.patch.get_linestyle())
        self.ui.doubleSpinBox_line_width.setValue(self.patch.get_linewidth())
        self.ui.checkBox_fill.setChecked(self.patch.get_fill())


    def update_alpha(self):
        """
        Update the alpha value of each patch in self.patches.

        This method retrieves the current value from the doubleSpinBox_alpha UI 
        element and sets it as the alpha value of each patch in self.patches. 
        It then updates the blit manager to reflect the changes.
        """
        alpha = self.ui.doubleSpinBox_alpha.value()
        for patch in self.patches:
            patch.set_alpha(alpha)
        self.blit_manager.update()


    def update_edge_color(self):
        """
        Update the edge color of each patch in self.patches.

        This method retrieves the current value from the comboBox_edge_color UI 
        element and sets it as the edge color of each patch in self.patches. 
        It then updates the blit manager to reflect the changes. Note that the 
        color is prefixed with 'tab:' to ensure it is recognized by the 
        matplotlib color system.
        """
        color = self.ui.comboBox_edge_color.currentText()
        if color == 'others':
            return 
        if color not in ('black', 'white',):
            color = 'tab:' + color 
        for patch in self.patches:
            patch.set_edgecolor(color)
        self.blit_manager.update()


    def update_face_color(self):
        """
        Update the face color of each patch in self.patches.

        This method retrieves the current value from the comboBox_face_color UI 
        element and sets it as the face color of each patch in self.patches. 
        It then updates the blit manager to reflect the changes. Note that the 
        color is prefixed with 'tab:' to ensure it is recognized by the 
        matplotlib color system.
        """
        color = self.ui.comboBox_face_color.currentText()
        if color == 'others':
            return 
        if color not in ('black', 'white',):
            color = 'tab:' + color 
        for patch in self.patches:
            patch.set_facecolor(color)
        self.blit_manager.update()


    def update_hatch(self):
        """
        Update the hatch pattern of each patch in self.patches.

        This method retrieves the current value from the comboBox_hatch UI 
        element and sets it as the hatch pattern of each patch in self.patches. 
        It then updates the blit manager to reflect the changes. The hatch 
        pattern is mapped from the UI text to the corresponding matplotlib 
        hatch symbol.
        """
        hatch_map = {
            'none': '',
            'diagonal hatching (/)': '/',
            'back diagonal (\\)': '\\',
            'vertical (|)': '|',
            'horizontal (-)': '-',
            'crossed (+)': '+',
            'crossed diagonal (x)': 'x',
            'small circle (o)': 'o',
            'large circle (O)': 'O',
            'dots (.)': '.',
            'stars (*)': '*'
        }
        hatch = self.ui.comboBox_hatch.currentText()
        for patch in self.patches:
            patch.set_hatch(hatch_map[hatch])
        self.blit_manager.update()


    def update_line_style(self):
        """
        Update the line style of each patch in self.patches.

        This method retrieves the current value from the comboBox_line_style UI 
        element and sets it as the line style of each patch in self.patches. 
        It then updates the blit manager to reflect the changes. The line style 
        is directly set based on the UI text, which should match the matplotlib 
        linestyle options.
        """
        style = self.ui.comboBox_line_style.currentText()
        for patch in self.patches:
            patch.set_linestyle(style)
        self.blit_manager.update()


    def update_line_width(self):
        """
        Update the line width of each patch in self.patches.

        This method retrieves the current value from the doubleSpinBox_line_width UI 
        element and sets it as the line width of each patch in self.patches. 
        It then updates the blit manager to reflect the changes. The line width 
        is directly set based on the UI value.
        """
        line_width = self.ui.doubleSpinBox_line_width.value()
        for patch in self.patches:
            patch.set_linewidth(line_width)
        self.blit_manager.update()


    def update_fill(self):
        """
        Update the fill status of each patch in self.patches.

        This method retrieves the current value from the checkBox_fill UI 
        element and sets the fill status of each patch in self.patches 
        accordingly. If the checkbox is checked, the patch will be filled; 
        otherwise, it will not be filled. The blit manager is then updated to 
        reflect the changes.
        """
        is_fill = self.ui.checkBox_fill.isChecked()
        for patch in self.patches:
            patch.set_fill(is_fill)
        self.blit_manager.update()
    
    def ok(self):
        """
        Accept the changes and close the dialog.
        """
        self.accept()

    def cancel(self):
        """
        Reject the changes, recover the initial state, and close the dialog.
        """
        # Recover the initial state of the patches
        for patch in self.patches:
            patch.set_alpha(self.initial_alpha)
            patch.set_edgecolor(self.initial_edge_color)
            patch.set_facecolor(self.initial_face_color)
            patch.set_hatch(self.initial_hatch)
            patch.set_linestyle(self.initial_line_style)
            patch.set_linewidth(self.initial_line_width)
            patch.set_fill(self.initial_fill)
        
        # Update the blit manager to reflect the changes
        self.blit_manager.update()
        
        # Close the dialog
        self.reject()

