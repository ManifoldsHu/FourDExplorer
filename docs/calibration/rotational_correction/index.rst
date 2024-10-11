Rotational Correction
======================

Rotational Correction in 4D-STEM datasets is essential to align the scanning and diffraction coordinate systems. 

In theoretical analysis and programming, we usually assume that the scan space axes of 4D-STEM (the path of the electron beam scanning over the sample) are aligned with the diffraction space axes (the orientation of the electron camera's pixel array). This allows us to conveniently describe both using an $xOy$ coordinate system. However, in actual experiments, the electron camera is fixed to the microscope, while the electron beam scan path can be freely defined. The most common scenario is a Z-shaped scan of the electron beam, where the scan direction differs from the camera's orientation by a certain angle. In such cases, **scan rotation correction** is needed.

4D-Explorer offers two primary methods for this purpose:

1. **Center of Mass (CoM) Curl Method**: This method minimizes the curl of the CoM vector field to determine the rotation angle, assuming the sample is non-magnetic.
2. **Defocused Axial Bright-Field (Axial BF) Method**: This method uses a defocused image to align the diffraction pattern with the reconstructed image, ensuring the correct orientation.

Additionally, users should consider potential 180° extra rotation and coordinate axis flipping to ensure accurate alignment.

In the left control panel, find the 4D-STEM dataset you want to correct, right-click, and choose ``Calibration`` from the menu. Then, in the submenu, select ``Diffraction Rotation`` to open the scan rotation correction page.

.. toctree::
   :maxdepth: 2
   :caption: Rotational Correction

   Axial_BF
   CoM_curl
   additional_180
   coordinate_flip
