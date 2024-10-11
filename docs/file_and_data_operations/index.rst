File and Data Operations
============================

4D-Explorer is designed to handle complex data operations, particularly for 4D-STEM datasets. The software leverages the HDF5 file format to manage and organize data efficiently. HDF5 (Hierarchical Data Format version 5) is a versatile file format that supports complex data structures, including groups, datasets, and metadata. This format is ideal for scientific data storage due to its ability to handle large datasets and its support for metadata, which provides additional context and information about the data.

### Key Features

- **HDF5 File Management**: Create, open, and close HDF5 files to store and manage your datasets.
- **Data Import**: Import various types of 4D-STEM datasets, including those from EMPAD and Merlin Medipix detectors, as well as general binary files.
- **Data Export**: Currently supports exporting data to HDF5 files, with plans to expand to other formats in the future.
- **Metadata Management**: Utilize metadata to describe and annotate datasets, providing essential information such as data type, units, and additional notes.


.. toctree::
   :maxdepth: 2
   :caption: File and Data Operations

   hdf5_organization
   import_dataset/index
   export_dataset
   manage_metadata
