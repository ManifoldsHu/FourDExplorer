HDF5 File and Data Organization
===============================

HDF5 (Hierarchical Data Format version 5) is a file format used for storing and organizing large amounts of data. It supports complex data structures, including groups, datasets, and metadata, which make HDF5 an ideal choice for scientific data storage.

Groups
------

A group is a container within an HDF5 file, similar to a directory in a file system. Groups can contain other groups and datasets. By using groups, you can organize and manage complex hierarchical data. For example, a group might represent an experiment, with subgroups representing different datasets or processing steps.

Datasets
--------

A dataset is the object that stores the actual data within an HDF5 file. It is similar to an array or table and can store multi-dimensional data. Datasets can contain any type of data, including integers, floating-point numbers, and strings. The dimensions of a dataset can vary from one-dimensional to multi-dimensional. For example, a 4D-STEM dataset can be stored as a four-dimensional dataset.

.. note::

   In the documentation, "Dataset" and "4D-STEM dataset" may refer to different objects depending on the context. Be sure to distinguish between them accordingly.

Metadata
--------

Metadata is data about data, used to describe the properties of datasets or groups. Metadata can include information such as the name, units, creation time, and author of a dataset. It is stored as key-value pairs, where the key is a string and the value can be of any data type. Metadata helps in the description and interpretation of data, which is especially useful in scientific data analysis.

Benefits of Using HDF5
----------------------

- HDF5 supports complex hierarchies, making it easy to organize and manage large datasets.
- HDF5 uses compression and chunking techniques to store and access large datasets efficiently.
- HDF5 is a cross-platform format and can be used on different operating systems and hardware.
- Metadata allows for detailed descriptions of data attributes, making data management and interpretation easier.
- With deferred reading, it reduces memory requirements, allowing you to handle 100 GB datasets even on a laptop.
- It is compatible with many open-source 4D-STEM processing software tools.
- Data can be easily further processed using Python, MATLAB, and other languages.

Using HDF5 in 4D-Explorer
-------------------------

4D-Explorer uses HDF5 files to store data by default. Before performing any operations, you should first select an HDF5 file to use as a container for storing the data. If no HDF5 file exists, you will need to create one. To create a new HDF5 file, open the ``File`` menu at the top left of the main interface and press the ``New HDF5 File`` button. You can then select the directory where the file should be saved and specify a name for the file. Afterward, a dialog will automatically appear for selecting the HDF5 file, at which point you can open the newly created file.

To open an existing HDF5 file, open the ``File`` menu at the top left of the main interface and choose ``Open HDF5 File``. You can then select the HDF5 file you wish to open.

An HDF5 file that is already open cannot be opened again by other processes, including another 4D-Explorer instance or user scripts. If you want to open the file in another software or script, you need to close it in the current 4D-Explorer session. To do this, open the ``File`` menu in the main interface and select ``Close File``. The HDF5 file list on the left will become blank. Be careful not to close the file while a calculation task is in progress, as this can lead to task failure.

Naming and Dataset Extensions in HDF5
-------------------------------------

In an HDF5 file, each group and dataset has its own name. In 4D-Explorer, groups and datasets are displayed in a tree structure, and the main display panel for this is on the left side of the control interface. For datasets, 4D-Explorer recognizes extensions separated by dots (``.``) to determine the dataset's type and assign an intuitive icon for display. Currently, 4D-Explorer recognizes the following extensions:

- ``.4dstem``: 4D-STEM dataset, must be a 4D array.
- ``.img``: Grayscale image, must be a 2D array. RGB or other multi-channel images are not supported.
- ``.vec``: 2D vector field, with two components. Each component is a grayscale image.
- ``.line``: A line, must be 1D.

In the future, more extensions may be added to distinguish between different types, dimensions, and uses of datasets as needed.

.. warning::

   Names cannot contain the following special characters: ``/``, ``\``, ``:``, ``*``, ``?``, ``"``, ``'``, ``<``, ``>``, ``|``. Names cannot begin or end with a space, and names such as ``.`` or ``..`` are not allowed. These restrictions are similar to those found in file systems, so it's recommended to choose simple, error-free naming conventions, such as using underscores to separate words.
