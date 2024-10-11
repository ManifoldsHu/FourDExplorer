Test Data
=========

We provide three test datasets: ``gold_nanoparticle_06``, ``gold_nanoparticle_07``, and ``MoS2_14``. The download links for these datasets are as follows:

- `Google Drive: 4D-Explorer Test Dataset <https://drive.google.com/drive/folders/1WaYyQNulZCERJQuW2GMvka0N5DNRpCFz?usp=sharing>`_
- `Baidu Netdisk: 4D-Explorer Test Dataset, code: 64s2 <https://pan.baidu.com/s/16G6rZUK95fogkg_GFg14hQ?pwd=64s2>`_

The parameters for these datasets are as follows:

gold_nanoparticle_06
---------------------

- **Scan points**: 256 x 256
- **Diffraction image size**: 128 x 128
- **Microscope model**: Thermofisher FEI Titan G2 60-300
- **Camera model**: Thermofisher EMPAD
- **Accelerating voltage (U)**: 60 kV
- **Camera length (CL)**: 576.6 mm
- **Convergence angle (α)**: 22.5 mrad
- **Scan step size**: 1.80 nm
- **Defocus**: In-focus
- **Notes**: This dataset was captured at focus with gold nanoparticles embedded in DNA. It was pre-configured with a 30° scan rotation angle and exhibits some diffraction drift. This dataset is suitable for demonstrating the process of **Rotational Offset Correction** by calculating the curl of the CoM and the process of **Diffraction Shift Alignment** using FDDNet to measure the shift in each diffraction spot.

.. note::
   On Google Drive, this dataset is split into multiple compressed files with extensions like `.z01`, `.z02`, etc. You need to download all compressed files before extracting them correctly.

gold_nanoparticle_07
---------------------

- **Scan points**: 128 x 128
- **Diffraction image size**: 128 x 128
- **Microscope model**: Thermofisher FEI Titan G2 60-300
- **Camera model**: Thermofisher EMPAD
- **Accelerating voltage (U)**: 60 kV
- **Camera length (CL)**: 576.6 mm
- **Convergence angle (α)**: 22.5 mrad
- **Scan step size**: 1.31 nm
- **Defocus**: -2.11 μm (under-focused)
- **Notes**: This dataset was captured under under-focus conditions, with gold nanoparticles embedded in DNA. In each diffraction image, the shape of the gold particles (real-space information) is visible. The sample stage height was adjusted to achieve the under-focus while maintaining the same scan rotation angle as the ``gold_nanoparticle_06`` dataset. This dataset is suitable for demonstrating the process of **Rotational Offset Correction** using Axial BF images.

MoS2_14
-------

- **Scan points**: 128 x 128
- **Diffraction image size**: 128 x 128
- **Microscope model**: Thermofisher FEI Titan G2 60-300
- **Camera model**: Thermofisher EMPAD
- **Accelerating voltage (U)**: 60 kV
- **Camera length (CL)**: 286.3 mm
- **Convergence angle (α)**: 22.5 mrad
- **Scan step size**: 0.029 nm
- **Defocus**: In-focus
- **Notes**: This dataset represents atomic-level imaging of molybdenum disulfide (MoS₂), a 2D material. It is suitable for demonstrating the effects of different reconstruction methods.
