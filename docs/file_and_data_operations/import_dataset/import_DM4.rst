Importing 4D-STEM Dataset in DM4 Format 
==========================================

The .dm4 file format is a proprietary file format used by Gatan's Digital Micrograph software, which is commonly employed for storing and analyzing microscopy data, including 4D-STEM datasets. Unlike the EMPAD format, which requires both an XML and a RAW file, the .dm4 format encapsulates all necessary data within a single file with the extension `.dm4`.

To import a 4D-STEM dataset stored in the .dm4 format, follow these steps:

1. **Open an HDF5 File**: Ensure that you have an HDF5 file open in the main interface.
2. **Access the Import Dialog**: In the main interface's menu bar, navigate to the ``Edit`` menu and locate the ``Import 4D-STEM dataset`` button. Click it to open the import dialog. Alternatively, you can right-click on any group in the file panel on the left side of the main interface and select ``Import 4D-STEM dataset`` from the context menu.
3. **Select the File Type**: In the pop-up import dialog, choose ``Digital Micrograph (.dm4)`` as the file type in the ``Import File Type`` field.
4. **Browse for the .dm4 File**: Click the ``Browse`` button to select the .dm4 file you wish to import.
5. **Specify the Import Location**: In the ``Import Dataset to Location`` field, browse and select the group where you want to import the dataset. You can also specify the name of the dataset in the ``Name`` field.
6. **Complete the Import**: Once all fields are correctly filled, click the ``Import`` button to load the dataset into the HDF5 file.

.. note::

   The dataset being imported in the .dm4 format should be a 4D-STEM dataset. Importing 2D images is not supported in this context.
