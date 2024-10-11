Background Subtraction
==========================

4D-Explorer offers two methods for background noise removal: subtracting a reference background image and histogram filtering. The former involves selecting a background image from HDF5, ensuring it matches the dataset's dimensions, and applying the subtraction. The latter uses histogram limits to filter out noise, setting values outside the limits to either the maximum limit or zero.




.. toctree::
   :maxdepth: 2
   :caption: Background Subtraction

   histogram_filter
   reference
