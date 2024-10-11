Importing 4D-STEM Dataset from General Binary Files
===================================================

Many 4D-STEM datasets are stored in uncompressed binary formats, where the file begins with a header of a certain byte length, followed by sequentially stored diffraction patterns. If the dataset format you wish to import is not natively supported by 4D-Explorer, you can use this method to import it into an HDF5 file, provided the storage format is known.

Before importing the dataset, you must first open an HDF5 file. In the main interface's menu bar, go to the ``Edit`` menu, find the ``Import 4D-STEM dataset`` button, and click it to open the import dialog. Alternatively, you can select any group from the file panel on the left side of the main interface, right-click, and choose ``Import 4D-STEM dataset`` from the menu.

In the pop-up import dialog, select ``General Raw Data (Binary)`` as the file type in the ``Import File Type`` field. Then, click the ``Browse`` button next to ``Raw file`` to select the binary file you wish to import. Next, fill in the following parameters:

- **Scalar Type**: Choose between ``unsigned integer``, ``integer``, or ``float``.
- **Scalar Size**: Supported sizes include 8-bit, 16-bit, 32-bit, and 64-bit. For certain 6-bit datasets, use 8-bit.
- **Image Width**: The number of pixels along the width of the diffraction image.
- **Image Height**: The number of pixels along the height of the diffraction image.
- **Number of Scanning Columns (scan_i)**: The number of scanning columns.
- **Number of Scanning Rows (scan_j)**: The number of scanning rows.
- **Offset to first image, bytes**: The number of bytes in the file header to skip before reaching the first image.
- **Gap between Images, bytes**: The number of bytes to skip between successive diffraction images.
- **Little-endian byte order**: Check this option if the data is stored in little-endian byte order.

Next, two additional parameters can be set:

- **Flip diffraction patterns (exchange i, j coordinates)**: If checked, the diffraction patterns will be flipped along the top-left to bottom-right diagonal.
- **Rotate nx90°, clock-wise**: Select how many times the diffraction images should be rotated 90° clockwise (1, 2, or 3 times for 90°, 180°, and 270° rotations).

These options are primarily used when the dataset's coordinate convention differs from that of 4D-Explorer. For a given dataset format, the same settings should be used consistently.

Finally, in the ``Import Dataset to Location`` field, browse to select the group where the dataset will be imported, and assign a name to the dataset in the ``Name`` field.

As an example, the test datasets can be imported with the following parameters (when selecting the file, choose the `.raw` file from the dataset folder):

+--------------------------+-----------------------+-----------------------+------------------+
| Parameter                | gold_nanoparticle_06  | gold_nanoparticle_07  | MoS2_14          |
+--------------------------+-----------------------+-----------------------+------------------+
| Scalar Type              | float                 | float                 | float            |
+--------------------------+-----------------------+-----------------------+------------------+
| Scalar Size              | 32 bit                | 32 bit                | 32 bit           |
+--------------------------+-----------------------+-----------------------+------------------+
| Image Width              | 256                   | 128                   | 128              |
+--------------------------+-----------------------+-----------------------+------------------+
| Image Height             | 256                   | 128                   | 128              |
+--------------------------+-----------------------+-----------------------+------------------+
| Scanning Columns         | 128                   | 128                   | 128              |
+--------------------------+-----------------------+-----------------------+------------------+
| Scanning Rows            | 128                   | 128                   | 128              |
+--------------------------+-----------------------+-----------------------+------------------+
| Offset to first image    | 0                     | 0                     | 0                |
+--------------------------+-----------------------+-----------------------+------------------+
| Gap between images       | 1024                  | 1024                  | 1024             |
+--------------------------+-----------------------+-----------------------+------------------+
| Little-endian            | Yes                   | Yes                   | Yes              |
+--------------------------+-----------------------+-----------------------+------------------+
| Flip diffraction         | Yes                   | Yes                   | Yes              |
+--------------------------+-----------------------+-----------------------+------------------+
| Rotate nx90°             | 3                     | 3                     | 3                |
+--------------------------+-----------------------+-----------------------+------------------+

Datasets imported using this method may lack important experimental parameters, so it is recommended to manually fill in these parameters as soon as possible after importing.
