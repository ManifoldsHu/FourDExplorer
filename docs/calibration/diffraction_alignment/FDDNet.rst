Using FDDNet Model to Measure Diffraction Shift
===============================================

.. note::
   Demonstration with the gold_particle_06 dataset from the 4D-Explorer test dataset

FDDNet is a deep learning-based model designed to estimate the bright field diffraction disc contour and can be used to measure the diffraction shift.

First, locate the 4D-STEM dataset you want to align from the left panel, right-click on it, and select ``Calibration`` -> ``Diffraction Alignment`` from the menu. In the opened page, choose ``Use FDDNet`` from the **Alignment Method** dropdown at the top right to use FDDNet for the measurement.

You can check the ``Display shifted diffraction image`` option to automatically shift the current diffraction image to the center based on FDDNet's measurement results. This way, if you observe that the diffraction disc always remains centered when adjusting the scan position, it indicates that FDDNet has accurately measured the diffraction shift.

You can also check the ``Show the measured ellipse`` option, which will display an ellipse based on FDDNet's measurement in the center. If the ellipse consistently overlaps with the boundary of the bright field diffraction disc as you adjust the scan position, it confirms that FDDNet has accurately measured the diffraction disc contour.

.. tip::
   It is not recommended to check both ``Display shifted diffraction image`` and ``Show the measured ellipse`` simultaneously. Doing so may prevent the ellipse from aligning with the diffraction disc boundary, making it difficult to judge the accuracy of FDDNet's measurement.

If you are not satisfied with the appearance of the ellipse (e.g., if it is too thick, thin, or the color is undesirable), you can adjust it using the ``Adjust Ellipse Effects`` button.

.. image:: /fig/DiffractionAlignmentFDDNet.png
   :alt: Diffraction Shift Alignment Using FDDNet

Next, click the ``Generate Shift Mapping`` button to generate the shift distribution. For a typical 4D-STEM dataset, this process might take a bit longer because the FDDNet model is applied to each diffraction image. You can switch to the ``Task Panel`` on the left to view the progress bar.

.. tip::
   Before using FDDNet for generating diffraction shift, consider applying a histogram filter to reduce background noise for better results. See :doc:`../background_subtraction/histogram_filter`


Once the shift distribution is generated, you can switch to the ``Displaying Effects`` tab at the top right. In the ``Shift Mapping Path`` section, select the newly generated shift distribution. Now, in the **Auxiliary Circle** section, the ``Set circle to where the shift vector points to`` option becomes available. Check this option to set the circle's center to the position indicated by the measured shift distribution. As you adjust the scan position, the auxiliary circle will move with the diffraction disc, allowing you to verify whether the shift distribution is accurate. This effect becomes more noticeable when using the mouse wheel to adjust the scan position.

.. image:: /fig/DiffractionAlignmentFDDNet2.png
   :alt: View Shift Mapping from FDDNet

Once the shift distribution is confirmed to be accurate, click the red ``Start to apply alignment`` button at the bottom of the page. After selecting the output dataset path and entering a name, click ``OK`` to complete the process.
