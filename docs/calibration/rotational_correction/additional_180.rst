Additional 180° Rotation of Diffraction Image
=============================================

The angle found through scan rotation correction might differ by 180° from the actual angle. Neither the **CoM curl method** nor the **defocused Axial BF method** can determine whether this additional 180° rotation is needed. If this is not correctly identified, the resulting electric field direction may be opposite to the real field, and imaging modes such as **dCoM** and **iCoM** may produce reversed contrast.

A practical way to determine whether an additional 180° rotation is needed is as follows: First, reconstruct an **annular dark field (ADF)** image using virtual imaging. In this image, the bright regions (those with higher values) correspond to areas of higher potential in the sample, while dark regions correspond to lower potential areas. Then, in the **center of mass (CoM)** imaging mode, check the option **Use projected electric field mapping** and reconstruct the **integrated CoM (iCoM)** image and the **differential CoM (dCoM)** image. Next, compare the iCoM/dCoM image with the ADF image (you can zoom in on a small area for more accurate comparison).

If the brighter regions in the iCoM/dCoM images match the brighter regions in the ADF image, no additional 180° rotation is required. However, if the contrast in the ADF image is opposite to that in the iCoM/dCoM images, then an additional 180° rotation is needed.
