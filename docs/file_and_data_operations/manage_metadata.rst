Metadata Management in 4D-Explorer
==================================

.. tip::
   Using the annular dark field image reconstructed from the ``gold_particle_06`` test dataset as an example.


4D-Explorer manages experimental parameters using the metadata functionality provided by HDF5. Metadata is stored as key-value pairs. Furthermore, 4D-Explorer has a built-in metadata specification that defines the purpose, units, description, and data type for certain keys associated with specific dataset extensions. These keys are strings that follow a path-style format, beginning with a slash, such as: ``/Acquisition/Microscope/accelerate_voltage``. This represents the acceleration voltage for 4D-STEM. The ``Acquisition`` and ``Microscope`` parts mainly serve as groupings to aid in organization and display.

To modify metadata, locate the corresponding dataset in the dataset list on the left, right-click to open the menu, and select ``Attributes`` at the bottom. This opens a dialog where the metadata is displayed in a tree structure, grouped for easy navigation. On the left side, you can see the metadata names (note: the names shown are provided by 4D-Explorer based on its internal metadata specification and are not the same as the keys), while on the right side, the values and the units are displayed.

.. image:: /fig/ViewMetadata.png
   :alt: View Metadata

Select a metadata entry in the list, right-click to open the menu, and you can add, edit, or delete metadata. Clicking ``Edit Metadata`` opens the edit metadata dialog. The fields in the dialog are:

- **Item Path**: The path of the dataset or group to which the metadata belongs.
- **Metadata Key**: The key for the metadata entry.
- **Value Type**: The data type of the metadata. Supported types are integer, float, or string. You can click the button on the right to change the data type.
- **Value**: For string values, you can enter any text. For floating-point values, the input is divided into a fractional part and an exponent part, following the conventions of scientific notation. The unit for the input value is displayed below the input field.
- **Note**: For keys included in 4D-Explorer's internal specification, the note provides guidance on the intended use of the key. When modifying these metadata values, additional warnings may be shown to remind users to make changes carefully.

.. image:: /fig/EditMetadata.png
   :alt: Edit Metadata
