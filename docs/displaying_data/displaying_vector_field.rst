Displaying Vector Field Data
============================

.. tip::
   Using the iCoM image reconstructed from the ``MoS2_14`` test dataset as an example.

In the dataset list on the left side of the interface, locate the vector field (``.vec`` data) you want to display, right-click, and select ``Open``. This will open a page displaying the vector field. At this point, 4D-Explorer automatically creates an empty 2D image named ``{vector_field_name}_bkgrd.img``. It has the same width and height as the vector field, but its values are set to zero. Its purpose is to represent the background of the vector field on the right side of the page.

If there is an image that corresponds to the vector field in the same spatial domain (for example, for a CoM vector field, you might already have an iCoM image or an annular dark field image), you can click the ``Browse Background`` button to select an appropriate background image to replace the empty one. This makes it easier to visualize the sample information near the positions corresponding to each vector in the field. Once the background image is set, you can delete the temporary empty background image.

If you find that the vector arrows are not sized correctly (e.g., they are too long, too short, too thick, or too thin) or you want to change their color, you can click the ``Adjust Quiver Effects`` button to make adjustments.

.. image:: /fig/ViewVectorField.png
   :alt: View Vector Field

.. note::
   In the dialog for adjusting the vector field effects, the ``Arrow Length Scale`` parameter is used to adjust the arrow length. Counterintuitively, the higher the value, the shorter each arrow becomes.
