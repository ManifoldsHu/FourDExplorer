Reconstruction
==================

4D-Explorer supports various methods for reconstructing images from 4D-STEM datasets, including Virtual Imaging and Center of Mass Imaging (CoM).

### Virtual Imaging

Virtual Imaging reconstructs sample images by selecting a specific region in the diffraction space, such as an annular region for annular dark field (ADF) imaging. This method simulates traditional STEM imaging with an annular dark field detector. It offers flexibility in choosing scattering angle ranges and easy parameter adjustments.

### Center of Mass Imaging (CoM)

Center of Mass Imaging (CoM) reconstructs sample images by quantifying electron beam deflection due to the sample's electric field. It calculates the center of mass (CoM) of diffraction patterns at each scan position and maps these CoM positions to the sample space. CoM imaging is highly sensitive to weak scattering signals and can compute iCoM (Integrated CoM) and dCoM (Differential CoM), representing the sample's potential and charge density, respectively.


.. toctree::
   :maxdepth: 2
   :caption: Reconstruction

   virtual_image
   CoM
   
