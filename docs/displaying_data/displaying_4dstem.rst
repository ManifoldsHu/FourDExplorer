Displaying 4D-STEM Data
=======================

.. tip::
   Using the MoS2_14 test dataset from 4D-Explorer as an example.

In the dataset list on the left side of the interface, locate the 4D-STEM dataset (``.4dstem`` data) you want to display, right-click, and select ``Open``. This will open a page displaying the dataset. At this point, 4D-Explorer automatically creates an empty 2D image named ``MoS2_14_preview.img``. It has the same dimensions as the scan coordinates of the 4D-STEM dataset, but its values are set to zero. Its purpose is to represent the scan coordinates on the right side of the page. When you click on the image on the right with the left mouse button, you can position the scan point at the mouse click location and view the corresponding diffraction image.

If a reconstructed image already exists for this dataset, you can click the ``Browse Preview`` button and select the reconstructed image to display on the right, replacing the empty dataset. This provides a more intuitive visualization of the relationship between different scan positions and their corresponding diffraction images. At this point, the temporary ``MoS2_14_preview.img`` dataset can be deleted.

.. note::
   The preview image should have the same dimensions as the scanning steps of the 4D-STEM dataset.

.. image:: /fig/View4DSTEM_MoS2.png
   :alt: View 4D-STEM Dataset

Below the scan image on the right side of the page, there are sliders and selection boxes that allow you to adjust the brightness, contrast, data scale (``Norm``, linear or logarithmic), and color map of the diffraction images.

Below the diffraction image in the center of the page, you can adjust the currently displayed scan position.
