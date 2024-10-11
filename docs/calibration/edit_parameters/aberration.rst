Aberration Coefficients
=======================

The last two pages contain parameters related to aberrations, specifically the coefficients for various orders of aberrations. The significance of these coefficients is described as follows:

.. list-table::
   :header-rows: 1
   :widths: 10 40

   * - **Symbol**
     - **Description**
   * - ``C1``
     - Defocus (defocus)
   * - ``A1``
     - Two-fold astigmatism
   * - ``B2``
     - Axial coma
   * - ``A2``
     - Three-fold astigmatism
   * - ``C3``
     - Spherical aberration
   * - ``S3``
     - Star aberration
   * - ``A3``
     - Four-fold astigmatism
   * - ``B4``
     - Axial coma
   * - ``D4``
     - Three-lobe aberration
   * - ``A4``
     - Five-fold astigmatism
   * - ``C5``
     - Spherical aberration
   * - ``A5``
     - Six-fold astigmatism

The symbols and their meanings follow the conventions given by `S. Uhlemann, M. Haider, Ultramicroscopy, 78(1999): 1-11`.

In addition to setting the magnitude of the aberrations, you can also set the angles for each order of aberration. However, defocus (``C1``) and spherical aberration (``C3``, ``C5``) are symmetric, so setting an angle will not affect them.

Once these aberrations are configured, they can be used to simulate the shape of the electron probe and vacuum diffraction disc. The aberration settings can also be used to calculate the contrast transfer function for virtual imaging and center-of-mass (CoM) imaging under the current aberration conditions.
