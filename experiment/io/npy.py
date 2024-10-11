# -*- coding: utf-8 -*- 

import sys
import os

import numpy as np 
import scipy as sp 
import h5py 
import matplotlib.pyplot as plt

# 把 path 加入到 sys 里
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from FourDExplorer.lib.Probe import OpticalSTEM 

convergence_angle = 22.5e-3
scan_i = 64 
scan_j = 256 
dp_i = 128
dp_j = 128 
bright_field_disk_radius = 19
accelerate_voltage = 60e3
defocus = 2e-8 
Cs = 1e-8 
dose = 1e6

optical_stem = OpticalSTEM(
    accelerate_voltage=accelerate_voltage,
    detector_shape = (dp_i, dp_j),
    scan_shape = (scan_i, scan_j),
    alpha = convergence_angle,
    scan_step_size = 1.8e-9,
    bright_field_disk_radius=bright_field_disk_radius,
    defocus = defocus, 
    Cs = Cs,
)

if __name__ == '__main__':
    probe = optical_stem.generateProbe()
    sample_object = np.random.random(size = (scan_i, scan_j, dp_i, dp_j))
    exit_wave = sample_object * probe[np.newaxis, np.newaxis, :, :]
    # dp = np.abs(optical_stem.fft2(exit_wave, pixel_size = optical_stem.dx))**2

    dps = np.zeros((scan_i, scan_j, dp_i, dp_j), dtype = 'float32')
    for ii in range(scan_i):
        for jj in range(scan_j):
            dp = np.abs(optical_stem.fft2(exit_wave[ii, jj, :, :], pixel_size = optical_stem.dx))**2
            pd = dp / np.sum(dp)
            dps[ii, jj, :, :] = np.random.poisson(pd * dose)
    
    plt.imshow(dps[0,0,:,:])
    plt.show()
    
    
    # # Save dps as npy format
    # np.save('D:\\Projects\\ReadDM4Test\\dps.npy', dps)

    # # Save dps as mat format
    # sp.io.savemat('D:\\Projects\\ReadDM4Test\\dps.mat', {'dps': dps}, format = '5')
    
    # Save dps as npz format
    np.savez('D:\\Projects\\ReadDM4Test\\dps.npz', dps=dps)
    
    

