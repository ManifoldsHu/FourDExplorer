# -*- coding: utf-8 -*-

"""
*--------------------------- FDDNetInference.py ------------------------------*
使用 FDDNet 模型对衍射图像的明场衍射盘作为椭圆的参数进行预测，包括中心位置、长轴、短轴
以及旋转角度。

作者:           胡一鸣
创建日期:       2024年9月21日

Use the FDDNet model to predict the parameters of the bright-field diffraction 
disk in a diffraction image, including the center position, major axis, minor 
axis, and rotation angle.

author:         Hu Yiming
date:           Sep 21, 2024
*--------------------------- FDDNetInference.py ------------------------------*
"""

import importlib.resources
from threading import Lock 

from PySide6.QtCore import Signal 
import onnxruntime as ort 
import numpy as np
from skimage.transform import resize 


def loadFDDNetModel() -> ort.InferenceSession:
    """
    Load the FDDNet model. FDDNet is a neural network model that measures 
    the center position, major axis, and minor axis (as an ellipse) of the 
    bright-field diffraction disk in a diffraction image.

    returns:
        (ort.InferenceSession) The ONNX runtime session for the FDDNet model.
    """
    with importlib.resources.path('models', 'FDDNet.onnx') as model_path:
        session_fddnet_options = ort.SessionOptions()
        session_fddnet_options.log_severity_level = 4 
        session_fddnet_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        session_fddnet = ort.InferenceSession(str(model_path), session_fddnet_options)
    return session_fddnet     
    
def loadFDDNetAngleModel() -> ort.InferenceSession:
    """
    Load the FDDNetAngle model. FDDNetAngle is a neural network model that measures 
    the rotation angle of the bright-field diffraction disk (represented as an ellipse) 
    in a diffraction image.

    returns:
        (ort.InferenceSession) The ONNX runtime session for the FDDNetAngle model.
    """
    with importlib.resources.path('models', 'FDDNetAngle.onnx') as model_path:
        session_fddnet_options = ort.SessionOptions()
        session_fddnet_options.log_severity_level = 4 
        session_fddnet_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        session_fddnet_angle = ort.InferenceSession(str(model_path), session_fddnet_options)
        return session_fddnet_angle

def inferEllipseLoc(image: np.ndarray, ort_session: ort.InferenceSession):
    """
    Use FDDNet to inference the location, major axis and minor axis of the 
    bright field disk.
    
    arguments:
        image: (np.ndarray) A single channel image. 
        
        ort_session: (ort.InferenceSession) The FDDNet model.
        
    returns:
        (tuple[float, float, float, float]) The center position ci, center
        postiion cj, major axis, and minor axis of the bright field disk.
    """
    input_name = ort_session.get_inputs()[0].name
    
    # Preprocessing the image
    h, w = image.shape 
    side_length = min(h, w)
    if h > w:
        start_h = (h - side_length) // 2 
        image = image[start_h:start_h + side_length, :]
    else:
        start_w = (w - side_length) // 2
        image = image[:, start_w:start_w + side_length]
    image = resize(image, (128, 128), anti_aliasing=True)
    vmin, vmax = np.min(image), np.max(image)
    image = (image - vmin) / (vmax - vmin)
    
    # Inference
    outputs = ort_session.run(
        None, 
        {input_name: image[np.newaxis, np.newaxis, :, :].astype(np.float32)}
    )[0][0]
    pred_ci, pred_cj, pred_a, pred_b = outputs
    scale_factor = side_length / 128 
    orig_ci = (pred_ci + 1/2) * scale_factor
    orig_cj = (pred_cj + 1/2) * scale_factor 
    orig_a = pred_a * scale_factor
    orig_b = pred_b * scale_factor
    
    if h > w:
        orig_cj += (h - side_length) // 2 
    else:
        orig_ci += (w - side_length) // 2 
    
    return orig_ci, orig_cj, orig_a, orig_b 

def inferEllipseAngle(image: np.ndarray, ort_session: ort.InferenceSession):
    """
    Use FDDNetAngle to inference the rotation angle of the bright field disk.
    
    arguments:
        image: (np.ndarray) A single channel image. 
        
        ort_session: (ort.InferenceSession) The FDDNetAngle model.
        
    returns:
        (float) The rotation angle of the bright field disk.
    """
    input_name = ort_session.get_inputs()[0].name 
    
    # Preprocessing image
    h, w = image.shape 
    side_length = min(h, w)
    if h > w:
        start_h = (h - side_length) // 2 
        image = image[start_h:start_h + side_length, :]
    else:
        start_w = (w - side_length) // 2
        image = image[:, start_w:start_w + side_length]
    image = resize(image, (128, 128), anti_aliasing=True)
    vmin, vmax = np.min(image), np.max(image)
    image = (image - vmin) / (vmax - vmin)
    
    # Inference
    pred_xn = ort_session.run(None, {input_name: image[np.newaxis, np.newaxis, :, :].astype(np.float32)})[0][0] 
    theta = _phaseShiftDecoder(pred_xn, mapping_cycle = 2)
    return theta

def _phaseShiftDecoder(x_n: np.ndarray, mapping_cycle: int = 2) -> float:
    """
    Here we use phase-shifting coding. See 
    
    Yi Yu et al. Phase-Shifting Coder: Predicting Accurate Orientation in 
    Oriented Object Detection (CVPR 2023) 
    
    For more information.
    
    arguments:
        x_n: (np.ndarray) The phase-shifted signal.
        
        mapping_cycle: (int) The number of mapping cycles.
    
    returns:
        (float) theta in [0, 180), unit: deg 
    """
    N_step = len(x_n) 
    phase_shift = (np.arange(N_step) + 1) * 2 * np.pi / N_step 
    phi = - np.arctan2(np.sum(x_n * np.sin(phase_shift)), np.sum(x_n * np.cos(phase_shift)))
    
    theta = _from90To180(np.rad2deg(phi)  / mapping_cycle) % 180
    return theta 

def _from90To180(theta: float) -> float:
    """
    turns a angle from [-90, 90) to [0, 180). This is useful for directions of lines, rectangles and ellipse.
    """
    angle = theta % 180 
    return angle % 90 + angle // 90 * 90 

def inferEllipse(image: np.ndarray, ort_session_fddnet: ort.InferenceSession, ort_session_fddnetangle: ort.InferenceSession):
    """
    Infers the parameters of an ellipse from a given image using an ONNX 
    inference session.

    This function preprocesses the input image by cropping it to a square of 
    the minimum dimension, resizing it to 128x128, and normalizing it. It then 
    runs the inference using the provided ONNX session to predict the center 
    coordinates (ci, cj) and the semi-major and semi-minor axes (a, b) of the 
    ellipse. The predicted parameters are scaled back to the original image 
    dimensions. Additionally, it infers the orientation angle (theta) of the 
    ellipse using a phase-shift decoder.

    arguments:
        image: (np.ndarray) The input image as a 2D numpy array.
        
        ort_session: (ort.InferenceSession) The ONNX inference session to use for 
            inference.

        ort_session_fddnetangle: (ort.InferenceSession) The ONNX inference session 
            to use for angle inference.

    returns:
        (tuple) A tuple containing the inferred parameters of the ellipse:
        
            - orig_ci: (float) The x-coordinate of the center of the ellipse in 
                the original image.
            
            - orig_cj: (float) The y-coordinate of the center of the ellipse in 
                the original image.
            
            - orig_a: (float) The length of the semi-major axis of the ellipse in 
                the original image.
            
            - orig_b: (float) The length of the semi-minor axis of the ellipse in 
                the original image.
            
            - theta: (float) The orientation angle of the ellipse in the original 
                image, in degrees.
    """
    
    h, w = image.shape
    side_length = min(h, w)
    if h > w:
        start_h = (h - side_length) // 2 
        image = image[start_h:start_h + side_length, :]
    else:
        start_w = (w - side_length) // 2
        image = image[:, start_w:start_w + side_length]
        
    image = resize(image, (128, 128), anti_aliasing=True)
    vmin, vmax = np.min(image), np.max(image)
    image = (image - vmin) / (vmax - vmin)
    
    input_name_fddnet = ort_session_fddnet.get_inputs()[0].name 
    outputs = ort_session_fddnet.run(
        None, 
        {input_name_fddnet: 
            image[np.newaxis, np.newaxis, :, :].astype(np.float32)
        }
    )[0][0]
    pred_ci, pred_cj, pred_a, pred_b = outputs 
    
    scale_factor = side_length / 128 
    orig_ci = (pred_ci + 1/2) * scale_factor
    orig_cj = (pred_cj + 1/2) * scale_factor
    orig_a = pred_a * scale_factor
    orig_b = pred_b * scale_factor 
    
    if h > w:
        orig_cj += (h - side_length) // 2 
    else:
        orig_ci += (w - side_length) // 2 
        
    input_name_fddnet_angle = ort_session_fddnetangle.get_inputs()[0].name
    pred_xn = ort_session_fddnetangle.run(
        None, 
        {input_name_fddnet_angle: 
            image[np.newaxis, np.newaxis, :, :].astype(np.float32)
        }
    )[0][0]
    theta = _phaseShiftDecoder(pred_xn, mapping_cycle = 2)
    
    return orig_ci, orig_cj, orig_a, orig_b, theta 


def mapInferenceFDDNet(
    item_path: str, 
    progress_signal: Signal = None,
) -> tuple[np.ndarray]:
    global qApp 
    hdf_handler = qApp.hdf_handler 
    dataset = hdf_handler.file[item_path]
    if len(dataset.shape) != 4:
        raise ValueError('The item path is not a 4D-STEM dataset.')
    if progress_signal is None:
        progress_signal = Signal(int)
        
    scan_i, scan_j, dp_i, dp_j = dataset.shape 
    result_lock = Lock()
    ci, cj, a, b = [np.zeros((scan_i, scan_j), dtype = 'float32') for _ in range(4)]
    fddnet_model = loadFDDNetModel()
    
    for ii in range(scan_i):
        for jj in range(scan_j):
            dp = np.asarray(dataset[ii, jj, :, :])
            with result_lock:
                ci[ii, jj], cj[ii, jj], a[ii, jj], b[ii, jj] = inferEllipseLoc(fddnet_model)
        progress_signal.emit(int((ii + 1) / scan_i * 100))
            
    return ci, cj, a, b 


def mapInferenceFDDNetAngle(
    item_path: str,
    progress_signal: Signal = None,
) -> tuple[np.ndarray]:
    global qApp 
    hdf_handler = qApp.hdf_handler
    dataset = hdf_handler.file[item_path]
    if len(dataset.shape) != 4:
        raise ValueError('The item path is not a 4D-STEM dataset.')
    if progress_signal is None:
        progress_signal = Signal(int)
    
    scan_i, scan_j, dp_i, dp_j = dataset.shape
    result_lock = Lock()
    angle = np.zeros((scan_i, scan_j), dtype = 'float32')
    fddnet_angle_model = loadFDDNetAngleModel()
    for ii in range(scan_i):
        for jj in range(scan_j):
            dp = np.asarray(dataset[ii, jj, :, :])
            with result_lock:
                angle[ii, jj] = inferEllipseAngle(fddnet_angle_model)
        progress_signal.emit(int((ii + 1) / scan_i * 100))
    return angle 


def mapInferenceFDDNetEllipse(
    item_path: str,
    progress_signal: Signal = None,
) -> tuple[np.ndarray]:
    global qApp
    hdf_handler = qApp.hdf_handler
    dataset = hdf_handler.file[item_path]
    if len(dataset.shape) != 4:
        raise ValueError('The item path is not a 4D-STEM dataset.')
    if progress_signal is None:
        progress_signal = Signal(int)
    
    scan_i, scan_j, dp_i, dp_j = dataset.shape
    result_lock = Lock()
    ci, cj, a, b, angle = [np.zeros((scan_i, scan_j), dtype = 'float32') for _ in range(5)]
    fddnet_model = loadFDDNetModel()
    for ii in range(scan_i):
        for jj in range(scan_j):
            dp = np.asarray(dataset[ii, jj, :, :])
            with result_lock:
                ci[ii, jj], cj[ii, jj], a[ii, jj], b[ii, jj], angle[ii, jj] = inferEllipse(fddnet_model)
        progress_signal.emit(int((ii + 1) / scan_i * 100))
    return angle 