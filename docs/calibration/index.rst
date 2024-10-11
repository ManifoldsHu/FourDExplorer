Calibration
==================

Accurate and quantitative 4D-STEM imaging requires meticulous calibration. 4D-Explorer includes four main steps for calibrating 4D-STEM datasets:

1. **Refinement of Experimental Parameters**: Adjust general, microscope, camera, space, and aberration parameters.
2. **Background Noise Removal**: Utilize methods like subtracting a reference background image or pixel histogram filtering.
3. **Rotational Correction**: Ensure proper alignment of the scan.
4. **Diffraction Alignment**: Correct diffraction shifts and wobbles using manual measurement, reference datasets, or FDDNet models.

These steps ensure high-quality data processing and analysis.


.. toctree::
   :maxdepth: 2
   :caption: Calibration
   
   edit_parameters/index
   background_subtraction/index
   rotational_correction/index
   diffraction_alignment/index
   
