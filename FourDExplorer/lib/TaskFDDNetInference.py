# -*- coding: utf-8 -*- 

"""
*------------------------- TaskFDDNetInference.py ----------------------------*
这个任务对 4D-STEM 数据集的每张衍射图像都进行 FDDNet 预测，并生成对应的结果文件。

作者:           胡一鸣
创建日期:       2024年9月21日


This task performs FDDNet prediction on each diffraction image of the 4D-STEM dataset and generates the corresponding result file.

author:         Hu Yiming
date:           Sep 21, 2024
*------------------------- TaskFDDNetInference.py ----------------------------*
"""

from logging import Logger 

from PySide6.QtCore import QObject
from PySide6.QtCore import Signal 
import numpy as np
from scipy.optimize import curve_fit

from bin.TaskManager import Task 
from bin.HDFManager import HDFHandler
from lib.FDDNetInference import mapInferenceFDDNet
from lib.FDDNetInference import mapInferenceFDDNetAngle
from lib.FDDNetInference import mapInferenceFDDNetEllipse
from lib.DiffractionAlignment import linearModel
from lib.DiffractionAlignment import quadraticModel

class TaskFDDNetInference(Task):
    """
    使用 FDDNet 推理整个 4D-STEM 数据集中每个衍射图像的任务类。
    
    The task 
    """
    
    _available_modes = {
        'center',
        'ci',
        'cj',
        'a',
        'b',
        'angle',
    }
    
    def __init__(
        self, 
        item_path: str, 
        image_parent_path: str, 
        calc_dict: dict,
        names_dict: dict,
        metas_dict: dict,
        fit_models_dict: dict = None,
        parent: QObject = None, 
    ):
        """
        arguments:
            item_path: (str) the 4D-STEM dataset path.
            
            image_parent_path: (str) the parent path of the result dataset.
            
            calc_dict: (dict[str: bool]) which parameters of ellipse fitting to be calculated. There must be 6 entries:
                - 'center': vector field mapping, the center location of the ellipse.
                - 'ci': i component of ellipse center
                - 'cj': j component of ellipse center
                - 'a': half major axis of the ellipse
                - 'b': half minor axis of the ellipse
                - 'angle': angle of the ellipse
            
            names_dict: (dict[str: str]) the names of the result datasets.
            
            metas_dict: (dict[str: dict]) the metadata of the result datasets.
            
            fit_model_dict: (dict[str: str|None]) the fit model of the result datasets. 
                - None: do not use fitting 
                - 'Linear': use linear fitting
                - 'Quadratic': use quadratic fitting
            
            parent: (QObject) the parent object of this task.
        """
        super().__init__(parent)
        self._item_path = item_path 
        self._image_parent_path = image_parent_path
        
        if not set(self._calc_dict.keys()).issubset(self._available_modes):
            raise ValueError(f"calc_dict keys must be a subset of {self._available_modes}")
        self._calc_dict = calc_dict
        
        for key in self._calc_dict:
            if self._calc_dict[key] and key not in names_dict:
                raise ValueError(f"The key '{key}' in calc_dict is True but not found in names_dict.")
        self._names_dict = names_dict
        
        for key in self._calc_dict:
            if self._calc_dict[key] and key not in metas_dict:
                raise ValueError(f"The key '{key}' in calc_dict is True but not found in metas_dict.")
        self._metas_dict = metas_dict
        
        for key in self._calc_dict:
            if self._calc_dict[key] and key not in fit_models_dict:
                fit_models_dict[key] = None 
        self._fit_models_dict = fit_models_dict
        
        self.comment = (
            'FDDNet inference on all diffraction images in the 4D-STEM dataset.\n'
            f'4D-STEM dataset: {self._item_path}\n'
            f'Inference results are saved in: {self._image_parent_path}\n'
        )
        
        self.setPrepare(self._createImages)
        self._bindSubtask()
        self.setFollow(self._showImage)
        
    @property
    def stem_path(self) -> str:
        """
        The 4D-STEM dataset path.
        """
        return self._item_path
    
    @property
    def image_path(self) -> str:
        """
        The path to the 
        """
        return self._image_parent_path
    
    @property
    def logger(self) -> Logger:
        global qApp 
        return qApp.logger
    
    @property
    def hdf_handler(self) -> HDFHandler:
        global qApp
        return qApp.hdf_handler
    
    def _createImages(self):
        """
        Will create multiple datasets in HDF5 file according to the calc_dict.
        
        This function works as the preparing function that will be called just 
        before the task is submitted.
        """
        data_object = self.hdf_handler.file[self.stem_path]
        scan_i, scan_j, dp_i, dp_j = data_object.shape
        for mode, is_calced in self._calc_dict.items():
            if is_calced:
                if mode == 'center':
                    shape = (2, scan_i, scan_j)
                else:
                    shape = (scan_i, scan_j)
                    
                self.hdf_handler.addNewData(
                    self._image_parent_path,
                    self._names_dict[mode],
                    shape,
                    'float32',
                )
                
                for key, value in self._metas_dict[mode].items():
                    data_path = self._getDataPath(mode)
                    self.hdf_handler.file[data_path].attrs[key] = value 
                    
    def _getDataPath(self, mode: str) -> str:
        """
        Returns the path of the created dataset according to the mode.
        
        arguments:
            mode: (str) the mode of the dataset, must be one of the keys in self._calc_dict, i.e. 'center', 'ci', 'cj', 'a', 'b', 'angle'.
            
        returns:
            (str) the path of the created dataset.
            
        raises:
            KeyError: if the mode is not found in self._names_dict.
        """
        if mode not in self._names_dict:
            raise KeyError(f"The key '{mode}' is not found in self._names_dict")
        if self._image_parent_path == '/':
            return self._image_parent_path + self._names_dict[mode]
        else:
            return self._image_parent_path + '/' + self._names_dict[mode]
        
    
    def _bindSubtask(self):
        """
        Add subtask, which is the pratical worker.
        """
        self.addSubtaskFuncWithProgress(
            'Inference with FDDNet',
            self._workerFDDNetInference,
        )
        
        
    def _workerFDDNetInference(self, progress_signal: Signal = None):
        """
        Calculate the ellipse parameters of each diffraction image.
        
        arguments:
            progress_signal: (Signal) the signal to report the progress.
        """
        data_object = self.hdf_handler.file[self.stem_path]
        scan_i, scan_j, dp_i, dp_j = data_object.shape
        
        _is_angle = self._calc_dict.get('angle', False)
        _is_scale = any(
            self._calc_dict.get(key, False) for key in self._available_modes
        )
        
        ci, cj, a, b, angle = [None for _ in range(5)]
                
        if _is_angle and _is_scale:
            ci, cj, a, b, angle = mapInferenceFDDNetEllipse(self.stem_path, progress_signal)
        elif _is_angle:
            angle = mapInferenceFDDNetAngle(self.stem_path, progress_signal)
        elif _is_scale:
            ci, cj, a, b = mapInferenceFDDNet(self.stem_path, progress_signal)
        else:
            raise RuntimeError('No calculation mode is selected.')
        
        center = np.stack([ci, cj], axis=0)
        result_dict = {
            'center': center,
            'ci': ci,
            'cj': cj,
            'a': a,
            'b': b,
            'angle': angle,
        }
        
        for mode, is_calced in self._calc_dict.items():
            if is_calced:
                data_path = self._getDataPath(mode)
                result = result_dict[mode]
                fit_model_name = self._fit_models_dict.get(mode, None)
                
                if fit_model_name is not None:
                    i_grid, j_grid = np.meshgrid(np.arange(scan_i), np.arange(scan_j), indexing='ij')
                    locations = np.vstack([i_grid.ravel(), j_grid.ravel()]).T
                    values = result.ravel()
                    
                    params = self._fitModel(fit_model_name, locations, values)
                    if params is not None:
                        if fit_model_name == 'Linear':
                            result = linearModel(locations.T, *params).reshape(scan_i, scan_j)
                        elif fit_model_name == 'Quadratic':
                            result = quadraticModel(locations.T, *params).reshape(scan_i, scan_j)
                
                self.hdf_handler.file[data_path][:] = result
        
        for mode, is_calced in self._calc_dict.items():
            if is_calced:
                data_path = self._getDataPath(mode)
                self.hdf_handler.file[data_path][:] = result_dict[mode]
        
        
    def _showImage(self):
        """
        Will open the inferenced image.
        
        This function works as the following function that will be called just
        after the task is finished.
        
        #TODO
        """
        self.logger.debug(f"Task {self.name} completed.")
        
        
    def _fitModel(self, model_name: str, locations: np.ndarray, values: np.ndarray) -> np.ndarray|None:
        """
        Fit the model to the given locations and values.

        arguments:
            model_name: (str) The name of the model to fit ('Linear' or 'Quadratic').
            
            locations: (np.ndarray) The locations (coordinates) to fit the model to.
            
            values: (np.ndarray) The values corresponding to the locations.

        returns:
            (np.ndarray|None) The fitted parameters for the model, or None if the model name is not recognized.
        """
        if model_name == 'Linear':
            return curve_fit(linearModel, locations.T, values)[0]
        elif model_name == 'Quadratic':
            return curve_fit(quadraticModel, locations.T, values)[0]
        else:
            return None