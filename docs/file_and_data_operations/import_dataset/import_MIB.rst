Importing 4D-STEM Dataset Collected by Merlin Medipix
=====================================================

The dataset collected by Merlin Medipix3 is in the ``.mib`` format, typically accompanied by a ``.hdr`` file.

Before importing the dataset, you must first open an HDF5 file. In the main interface's menu bar, go to the ``Edit`` menu, find the ``Import 4D-STEM dataset`` button, and click it to open the import dialog. Alternatively, you can select any group from the file panel on the left side of the main interface, right-click, and choose ``Import 4D-STEM dataset`` from the menu.

In the pop-up import dialog, select ``MerlinEM (.mib)`` as the file type in the ``Import File Type`` field. Then, click the ``Browse`` buttons next to ``MerlinEM MIB file`` and ``MerlinEM HDR file`` to select the corresponding files. The ``.hdr`` file contains information related to the scan coordinates. If you check the option to set scan coordinates based on the ``.hdr`` file, this information will be read from the file. If no ``.hdr`` file is provided or you prefer not to use the scan coordinates from the ``.hdr`` file, simply uncheck the option and manually enter the scan coordinate dimensions in the ``Scanning steps`` field.

Finally, after selecting the appropriate files, you can browse for the group where the dataset will be imported in the ``Import Dataset to Location`` field, and assign a name to the dataset in the ``Name`` field.

.. note::
    For 4D-STEM datasets in the .mib format, some metadata, such as scanning step size, may not be automatically parsed. Users may need to consider manually supplementing this metadata.



