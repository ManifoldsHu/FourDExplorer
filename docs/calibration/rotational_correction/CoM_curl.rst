Center of Mass (CoM) Curl Method
================================

.. tip::
   Using the ``gold_particle_06`` dataset from the 4D-Explorer test dataset as an example.

In a 4D-STEM dataset, the center of mass (CoM) of each diffraction image is proportional to the electric field strength at the corresponding scan position on the sample (assuming the sample is non-magnetic). It is well-known that the distribution of the electric field is irrotational, especially around spherical objects like gold nanoparticles, where all electric field vectors radiate outward from the center (or converge inward) without any rotational components around the sphere.

Therefore, if the CoM image reconstructed from the dataset shows rotational components around the nanoparticles, it indicates that there is a rotational offset between the coordinate axes of the diffraction space and the scan space, causing each CoM vector to be rotated by a certain angle. We can manually rotate these vectors to return them to their irrotational state, where the field radiates outward from the sphere. This process is equivalent to minimizing the curl of the CoM vectors, which is the principle behind the CoM curl method.

In the software's left control panel, find the 4D-STEM dataset you want to correct, right-click, and choose ``Calibration`` from the menu. Then, in the submenu, select ``Diffraction Rotation`` to open the scan rotation correction page.

On the opened correction page, the initial method displayed on the top right is the CoM curl method for scan rotation correction. First, click the ``Browse`` button next to the **Vector Field Path** to select the CoM vector field dataset of the current 4D-STEM dataset. If you haven't reconstructed one yet, you can do so to see the effect. Once the vector field is selected, it will be displayed on the right side of the page. If the vector field's display is unclear, click the ``Adjust Quiver Effect`` button below to adjust the length, width, and color of the arrows.

.. image:: /fig/DiffractionRotation.png
   :alt: Rotational Offset Correction Using CoM Method

Below the vector field, there is an input box to adjust the rotation angle. To apply the rotation, click the refresh button to see the effect of rotating each vector by a certain angle.

Click the ``Calculate Rotation Angle`` button to open a dialog that shows the sum of the squares of the curl and divergence for each rotation angle. The dialog will automatically fill in the angle with the minimum curl on the curve. Click ``Confirm`` to apply this angle back to the vector field on the page, allowing you to observe whether the CoM distribution is now an irrotational field.

.. image:: /fig/MinimizeCurl.png
   :alt: Minimize Curl of CoM

Once you confirm an angle, click the red ``Apply Rotation and Start Calculation`` button at the bottom of the page (if you can't see the button, it might be hidden at the bottom of the page; scroll down or drag the right scrollbar). After selecting the output path and name for the new 4D-STEM dataset, all diffraction images in the 4D-STEM dataset will be rotated by the calculated angle and saved as a new dataset.

.. note::
   Although we assume the sample is non-magnetic, the CoM distribution remains irrotational even for magnetic samples. This is because the magnetic flux density forms a rotational but source-free field, which can be visualized as a magnetic field circling around a point. When electrons are deflected by the Lorentz force, their deflection is perpendicular to the magnetic field. This effectively rotates each vector by 90°, turning the rotational source-free field into an irrotational one, similar to the effect of an electric field. 

   This allows us to apply the CoM curl minimization method to datasets from magnetic samples as well. However, a limitation is that we can no longer use the divergence and curl properties of the field to distinguish between electric and magnetic fields in the sample.

