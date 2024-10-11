Defocused Axial BF Method
=========================

.. tip::
   Using the ``gold_particle_07`` dataset from the 4D-Explorer test dataset as an example.

Another method to measure the scan rotation angle involves collecting defocused datasets during the experiment, where the sample's morphology is visible in the diffraction images (which makes it easier to determine the direction).

In scanning transmission electron microscopy (STEM), if we use a point detector, the optical path becomes the reverse of that in conventional transmission electron microscopy (TEM) using parallel electron beams. In this optical path, the point detector corresponds to the point source in TEM, and the condenser lens corresponds to the objective lens in TEM. As a result, the imaging obtained using a point detector shares characteristics with TEM imaging, particularly having a similar contrast transfer function.

What is the significance of this? TEM imaging typically has a large depth of field, meaning that even with significant defocus, the overall shape of the object can still be seen (though the resolution will be lower compared to in-focus or slightly under-focused imaging). Therefore, when a defocused 4D-STEM dataset is acquired and the defocus is large enough for the object’s shape to be visible in the diffraction images, we can use the point detector to perform virtual imaging reconstruction. Among the available virtual imaging modes, only the point detector can reconstruct a relatively clear image in this scenario, while modes like bright field, annular bright field, and annular dark field produce blurred images due to their shallow depth of field.

The image obtained with the point detector is called the **Axial Bright Field (Axial BF)** image. Since the sample's morphology is visible in this image, it can be compared with the diffraction image's morphology. If there is an angular difference between the two, this indicates a relative rotation between the diffraction coordinates and the scan coordinates. After all, the morphology in the diffraction image comes from a single scan point and reflects the diffraction coordinates, while each pixel in the reconstructed image corresponds to a scan point, reflecting the scan coordinates.

In the software's left control panel, find the 4D-STEM dataset you want to correct, right-click, and select ``Calibration`` from the menu. Then, in the submenu, select ``Diffraction Rotation`` to open the scan rotation correction page.

On the opened correction page, you can select the **Axial BF Method** from the top right to display the corresponding operation panel. Click the ``Browse`` button next to **Axial BF Path** to choose the reconstructed image for this dataset. If you haven't yet created one, you can first reconstruct one using virtual imaging, ensuring that you select the point detector by setting the bright field detector radius to about one pixel.

.. image:: /fig/RotationWithAxialBF.png
   :alt: Rotational Offset Correction Using Defocused Axial BF Image

Once the Axial BF image is selected, it will be displayed. By adjusting the **Rotation Angle** input box, you can see the effect of rotating the diffraction image in the center of the page. When the diffraction image is aligned with the Axial BF image on the right, the correct scan-to-diffraction coordinate rotation angle has been found.

.. image:: /fig/RotationWithAxialBF2.png
   :alt: Rotate Diffraction Pattern

Once you confirm an angle, click the red ``Apply Rotation and Start Calculation`` button at the bottom of the page (if you can't see this button, it might be hidden at the bottom; scroll down or drag the right scrollbar). After selecting the output path and name for the new 4D-STEM dataset, all the diffraction images in the 4D-STEM dataset will be rotated by this angle and saved as a new dataset.

.. note::
   When you have rotated to the correct angle, you can observe the movement of the sample morphology in the diffraction image by adjusting the scan position using the input boxes at the bottom of the page. As you change the scan position in the **i** direction, the morphology in the diffraction image moves up or down. When you adjust the scan position in the **j** direction, the morphology in the diffraction image moves left or right. Using the mouse scroll wheel to adjust these input boxes makes this phenomenon more noticeable and intuitive.
