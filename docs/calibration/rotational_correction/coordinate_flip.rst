Axis Flip
=========

An **axis flip** refers to a situation where the scan coordinate system and the diffraction coordinate system follow different chirality conventions. Both the xOy coordinate system and the ij coordinate system used in 4D-Explorer are right-handed systems, differing only by a 90° rotation. However, if either the diffraction images or the scan coordinate system follows a left-handed convention, it will lead to incorrect results, regardless of how the scan rotation correction is applied. This can result in an incorrect coordinate system and an inaccurate reconstruction of the center of mass (CoM) vector field.

Data collected using the same electron microscope and camera will adhere to the same chirality convention for the coordinate system. Therefore, when using data from a particular piece of equipment for the first time, it is important to carefully decide whether the diffraction images need to be flipped when reading the 4D-STEM dataset.
