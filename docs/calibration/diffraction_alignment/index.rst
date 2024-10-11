Diffraction Alignment
=======================

This section provides a comprehensive guide on aligning diffraction patterns in 4D-STEM datasets. Accurate alignment is crucial for ensuring high-quality data processing and analysis. The alignment process involves correcting diffraction shifts and wobbles, which can significantly impact the quality of centroid imaging.

In theoretical analysis, it is generally assumed that the optical axis, or the center of the bright field diffraction disc, is perfectly aligned with the center of the camera (or the center of the pixel grid). However, in practice, it is difficult to ensure that the bright field diffraction disc is perfectly aligned with the image center, often resulting in a **diffraction shift**.

When diffraction shift occurs, the quality of CoM (center of mass) imaging is severely affected, as the overall shift of the diffraction disc directly impacts the CoM value. In CoM imaging, to accurately measure the local electric field distribution in thin samples, we need to measure the CoM shift caused by the uneven brightness distribution within the diffraction disc, not the overall shift of the entire disc. Therefore, it is important to minimize diffraction shift as much as possible.

A worse situation occurs when the amount of shift varies with the scan position, a phenomenon known as **diffraction wobble**. This usually happens when the scan range is large, as the further the scan position is from the optical axis, the more pronounced the wobble. In this case, simply shifting the entire diffraction image is insufficient; each diffraction image must be precisely aligned. However, a typical 4D-STEM dataset contains tens of thousands of diffraction images, making manual alignment an unfeasible task.

Fortunately, the magnitude of the wobble can be approximated as linear with respect to the scan position. This means that by measuring the shift for a portion of the diffraction discs and using linear fitting, the shift distribution for all diffraction discs in the 4D-STEM dataset can be calculated. Once this shift distribution is obtained, it can be applied to the entire dataset for alignment.

Three primary methods are discussed for measuring diffraction disk shifts:

1. **Manual Measurement**: Users manually adjust the diffraction disk position at various scan locations and generate a shift distribution using linear regression.
2. **Using Reference Dataset**: This method employs a reference 4D-STEM dataset collected under vacuum conditions to measure the shift distribution.
3. **Using FDDNet Model**: A deep learning model, FDDNet, is utilized to estimate the diffraction disk contours and measure the shifts automatically.

Each method offers a detailed step-by-step guide to ensure precise alignment, enhancing the overall quality of the 4D-STEM data analysis.

.. toctree::
   :maxdepth: 2
   :caption: Diffraction Alignment

   FDDNet
   manually
   reference
