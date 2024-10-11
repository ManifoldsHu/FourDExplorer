Using a Reference Dataset
==========================

This method requires acquiring a vacuum 4D-STEM dataset during the experiment. The optical parameters for this reference dataset should match those used for the dataset containing the sample.

In the left panel, find the 4D-STEM dataset you want to align, right-click, and select ``Calibration`` -> ``Diffraction Alignment`` from the menu. In the opened page, select **Use Reference Dataset** from the **Alignment Method** dropdown at the top right. This will enable alignment using a reference dataset for measuring the shifts.

First, click the ``Browse`` button next to the reference 4D-STEM dataset path to select the reference dataset. Then, you can check the **Display shifted diffraction image** box, which will display the diffraction images shifted based on the reference dataset's center of mass. As you adjust the scan position, observe whether the bright field diffraction disc remains centered. Click the ``Generate Shift Mapping`` button to generate the shift distribution.

Once the shift distribution is generated, you can switch to the ``Displaying Effects`` tab at the top right. In the ``Shift Mapping Path`` section, select the newly generated shift distribution. Now, in the **Auxiliary Circle** section, the ``Set circle to where the shift vector points to`` option becomes available. Check this option to set the circle's center to the position indicated by the measured shift distribution. As you adjust the scan position, the auxiliary circle will move with the diffraction disc, allowing you to verify whether the shift distribution is correct. This effect becomes more noticeable when using the mouse wheel to adjust the scan position.

Once the shift distribution is confirmed to be accurate, click the red ``Start to apply alignment`` button at the bottom of the page. After selecting the output dataset path and entering a name, click ``OK`` to complete the process.
