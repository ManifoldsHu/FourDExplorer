Space Parameters
================

The fourth page contains parameters related to **Space**, which mainly refers to the physical dimensions corresponding to each pixel in the 4D-STEM dataset. Therefore, these parameters are equally important as they determine the quantitative analysis results of the dataset and must be modified with caution.

The parameter **:math:`\Delta u`** represents the pixel size in diffraction space, with units consistent with spatial frequency. It satisfies the following equation:

.. math::

    N_{br}\Delta u = \alpha / \lambda

where **:math:`N_{br}`** is the radius of the bright field diffraction disc in pixels, **:math:`\alpha`** is the convergence angle, and **:math:`\lambda`** is the electron beam wavelength. The **:math:`\Delta u`** parameter, along with the convergence angle and camera length, typically requires calibration using standard samples.

**:math:`\Delta r`** represents the pixel size in real space, where real space and diffraction space are reciprocal to each other. The relationship between **:math:`\Delta r`** and **:math:`\Delta u`** is given by:

.. math::

    \Delta r \Delta u = N

where **:math:`N`** is the number of pixels along one edge of the diffraction image.

The parameter **:math:`\Delta r_p`** refers to the distance between the center points of adjacent sampling positions in the dataset, corresponding to neighboring diffraction images. In most cases, **:math:`\Delta r_p`** matches the scan step size from the microscope parameters. The distinction between these two keys exists to account for cases where multiple diffraction images may be discarded or merged in the dataset. For quantitative calculations in the software, **:math:`\Delta r_p`** is the reference.

.. note::
   While both **:math:`\Delta r_p`** and **:math:`\Delta r`** are measured in physical length units, they are typically not the same. In applications such as virtual imaging and center-of-mass imaging, the pixel size of the reconstructed sample image is **:math:`\Delta r_p`**. However, in applications like ptychography, the pixel size of the image is **:math:`\Delta r`**.
