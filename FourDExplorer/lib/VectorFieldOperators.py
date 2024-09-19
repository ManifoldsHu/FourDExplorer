# -*- coding: utf-8 -*-

"""
*------------------------ VectorFieldOperators.py ----------------------------*
提供了表示矢量场的矩阵对应的函数或算符。

作者：          胡一鸣
创建时间：      2022年5月20日

Here provides some functions or operators of vector fields.

author:         Hu Yiming
date:           May 20, 2022
*------------------------ VectorFieldOperators.py ----------------------------*
"""


import h5py
import numpy as np

def _fft2(scalar: np.ndarray) -> np.ndarray:
    return np.fft.fftshift(np.fft.fft2(np.fft.fftshift(scalar)))

def _ifft2(scalar: np.ndarray) -> np.ndarray:
    return np.fft.ifftshift(np.fft.ifft2(np.fft.ifftshift(scalar)))

def _getCoord(scalar: np.ndarray) -> np.ndarray:
    """
    returns the location vector distribution.
    """
    height, width = scalar.shape 
    array_h = np.linspace(-height/2, height/2 - 1, height)
    array_w = np.linspace(-width/2, width/2 - 1, width)
    return np.meshgrid(array_h, array_w, indexing = 'ij')

def CenterOfMass(scalar: np.ndarray) -> tuple[float]:
    """
    Returns the center of mass vector of an image.
    
    arguments:
        scalar: (np.ndarray) the scalar function, typically 2D matrix.
        
    returns:
        (Tuple[float]) center of mass vector, (CoM_i, CoM_j).
    """
    dp_i, dp_j = scalar.shape 
    center_i = (dp_i - 1)/2
    center_j = (dp_j - 1)/2
    total_mass = np.sum(scalar)
    if total_mass == 0:
        return (center_i, center_j)  # Default to the center if the total mass is zero

    array_i = np.linspace(- center_i, dp_i - center_i - 1, dp_i)
    array_j = np.linspace(- center_j, dp_j - center_j - 1, dp_j)
    i_coords, j_coords = np.meshgrid(array_i, array_j, indexing = 'ij')
    CoM_i = np.sum(i_coords * scalar) / total_mass
    CoM_j = np.sum(j_coords * scalar) / total_mass
    return (CoM_i, CoM_j)


def Gradient(scalar: np.ndarray) -> tuple[np.ndarray]:
    """
    Returns the gradient vector field of a scalar function.

    arguments:
        scalar: (np.ndarray) the scalar function, typically 2D matrix.

    returns:
        (Tuple[np.ndarray]) gradient components along all axis.
    """
    return np.gradient(scalar)

def Divergence2D(vec_i: np.ndarray, vec_j: np.ndarray) -> np.ndarray:
    """
    Returns the divergence scalar function of a vector function.

    arguments:
        vec_i: (np.ndarray) the i-component of the vector field.

        vec_j: (np.ndarray) the j-component of the vector field.

    returns:
        (np.ndarray) divergence distribution matrix.
    """
    vec_ii, vec_ij = np.gradient(vec_i)
    vec_ji, vec_jj = np.gradient(vec_j)
    return vec_ii + vec_jj 

def Curl2D(vec_i: np.ndarray, vec_j: np.ndarray) -> np.ndarray:
    """
    Returns the curl scalar function of a vector function.

    arguments:
        vec_i: (np.ndarray) the i-component of the vector field

        vec_j: (np.ndarray) the j-component of the vector field

    returns:
        (np.ndarray) curl distribution matrix (as a 2D matrix)
    """
    vec_ii, vec_ij = np.gradient(vec_i)
    vec_ji, vec_jj = np.gradient(vec_j)
    return vec_ji - vec_ij 

def Laplacian2D(scalar: np.ndarray) -> np.ndarray:
    """
    Returns the laplacian scalar function of a scalar function.

    arguments:
        scalar: (np.ndarray) the scalar function, typically 2D matrix.

    returns:
        (np.ndarray) laplacian distribution matrix.
    """
    scalar_i, scalar_j = np.gradient(scalar)
    scalar_ii, scalar_ij = np.gradient(scalar_i)
    scalar_ji, scalar_jj = np.gradient(scalar_j)
    return scalar_ii +  scalar_jj 

def Potential2D(vec_i: np.ndarray, vec_j: np.ndarray) -> np.ndarray:
    """
    Returns the potential scalar function of a vector function.

    We have
        v_x, v_y = - grad U
    of which
        v_x = - ∂U / ∂x
    and
        v_y = - ∂U / ∂y
    
    Now we calculate their Fourier transform:

        FT(v_x) = - FT(∂U / ∂x) = - 2πi k_x F(U)
    and
        FT(v_y) = - FT(∂U / ∂y) = - 2πi k_y F(U)

    where i is the imaginary unit, k_x and k_y are space frequencies, and FT 
    is the Fourier transfrom operator. Here

        FT(v(x)) = ∫v(x)exp(- 2πi k x) dx

    The value is staightly corresponds to the value in discreted fourier 
    transform, and the unit of space frequency is 1/m .

    Hence

        k_x FT(v_x) + k_y FT(v_y) = - 2πi (k_x^2 + k_y^2) FT(U)

    So

        F(U) = - [k_x FT(v_x) + k_y FT(v_y)] / [2πi (k_x^2 + k_y^2)]

    Finally, we have

        U = - IFT{[k_x FT(v_x) + k_y FT(v_y)] / [2πi (k_x^2 + k_y^2)]}


    arguments:
        vec_i: (np.ndarray) the i-component of the vector field

        vec_j: (np.ndarray) the j-component of the vector field

    returns:
        (np.ndarray) potential distribution matrix.
    """

    f_i = _fft2(vec_i)
    f_j = _fft2(vec_j)
    k_i, k_j = _getCoord(vec_i)
    f_ivec = (k_i * f_i + k_j * f_j ) / (k_i**2 + k_j**2 + 1e-12)
    potent = np.real(- _ifft2(f_ivec) / (2 * np.pi * complex(0, 1)))
    return potent 




