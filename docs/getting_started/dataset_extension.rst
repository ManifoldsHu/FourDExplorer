Dataset Extensions
===================

Now, in the ``File`` panel of the control interface, we can see a new item named ``gold_nanoparticle_06.4dstem``, which is the 4D-STEM dataset we just imported. It has its own icon and the extension ``.4dstem``. 4D-Explorer uses these extensions to identify the purpose of the datasets. Of course, extensions are not mandatory, just like how we recognize file types in an operating system. Currently, 4D-Explorer supports the following extensions:

- ``.4dstem``: 4D-STEM dataset, must be a 4D array.
- ``.img``: Grayscale image, must be a 2D array. RGB or other multi-channel images are not supported.
- ``.vec``: 2D vector field, with two components. Each component is represented as a grayscale image.
- ``.line``: A line, must be 1D.
