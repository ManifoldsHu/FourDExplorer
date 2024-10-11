Virtual Imaging
================

.. note::
   Demonstration with the MoS2 dataset from the 4D-Explorer test dataset

Virtual imaging is a method used to reconstruct sample images from 4D-STEM datasets. The principle behind it is to select a specific region in diffraction space (e.g., an annular region for annular dark field (ADF) imaging), and then integrate the diffraction pattern at each scan position to produce a 2D sample image. This process simulates the way an ADF detector in a conventional transmission electron microscope (TEM) captures images. The advantage of virtual imaging is that it allows for flexible selection of different scattering angle ranges, enabling the generation of sample images with different contrast transfer functions and resolutions. Additionally, because the processing is done in software, parameters can be easily adjusted and optimized.

To reconstruct the 4D-STEM dataset, locate the dataset in the left panel, right-click on it, and select ``Reconstruction`` -> ``Virtual Imaging`` from the menu. In the top right corner of the page, use the **Domain Shape** dropdown to choose the region type for reconstruction. For example, circular regions can be used for calculating Axial BF (bright field) or BF (bright field), annular regions can be used for calculating ABF (annular bright field) or ADF (annular dark field), and sector regions can also be selected. Once the region type is chosen, adjust the region parameters below, such as the radius and center coordinates for a circular region.

.. image:: /fig/AdjustReconstructionEffects.png
   :alt: Adjust Displaying Style of Integral Regions

If you are not satisfied with the appearance of the region (e.g., color or transparency), click the ``Adjust Effects...`` button. In the dialog that opens, you can modify the transparency (Alpha), edge color (Edge Color), interior color (Face Color), fill pattern (Hatch), line style (Line Style), line width (Line Width), and choose whether to fill the region.

After selecting the integration region, click the red ``Start Calculation`` button at the bottom of the page. After choosing the output image path and entering a name, click ``OK`` to begin the calculation.
