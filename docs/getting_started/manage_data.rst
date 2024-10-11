Data Management
===============

4D-Explorer is based on the `HDF5 <https://www.hdfgroup.org/solutions/hdf5/>`_ file format. HDF5 files consist of groups and datasets, similar to folders and files in a computer operating system. Groups can contain other groups and datasets, forming a hierarchical structure that facilitates the organization and management of complex data.

Creating a New HDF5 File
------------------------

To create a new HDF5 file, open the "File" menu at the top left of the main interface and press the ``New HDF5 File`` button. This will open a dialog to choose the name and storage path for the new HDF5 file. We will name the new HDF5 file ``4D-Explorer-test-dataset.h5``. Afterward, a dialog will automatically pop up to select the newly created HDF5 file, which you can then open.

.. image:: /fig/CreateH5.png
   :alt: Create a New File

In the newly created HDF5 file, which is empty, there is only one item in the File panel on the left, representing the newly created HDF5 file ``4D-Explorer-test-dataset.h5``. We will first create a group to place the datasets we are about to import. To create a group, right-click on ``4D-Explorer-test-dataset.h5`` in the left panel and select ``New`` (with a ``+`` icon) from the pop-up menu.

.. image:: /fig/NewGroup.png
   :alt: Create a New Group 1

Creating a New Group
--------------------

In the opened Create Item dialog, there are three fields to fill in:

- **Location**: This specifies where the group should be created. The default is ``/``, which, for those familiar with Unix/Linux, represents the root directory. In HDF5 files, this means the item is being created at the root level and does not belong to any group. Clicking the ``Browse...`` button allows you to browse and select a group to place the new item in. However, since our HDF5 file currently has no groups, we can only select the root directory.
- **Name**: This is the name of the new group. The default is ``untitled``, but we will change it to a desired name, such as ``gold_nanoparticle``.
- **Type**: Here, we select ``Group``, indicating that we are creating a group rather than a dataset.

.. image:: /fig/NewGroup2.png
   :alt: Create a New Group 2

If everything goes smoothly, you should see a new item under ``4D-Explorer-test-dataset.h5`` in the File panel on the left, named ``gold_nanoparticle_06``, with a folder icon. This is the group we just created.

Creating Multiple Groups
------------------------

We provide three test datasets, so we will create three groups here, named:

- ``gold_nanoparticle_06``
- ``gold_nanoparticle_07``
- ``MoS2_14``

Group Operations
----------------

Right-clicking on a group will reveal a menu similar to the one we just saw, with operations that can be performed on a group, including:

- ``New``: Create a new group or dataset within the group.
- ``Import 4D-STEM dataset``: Import a 4D-STEM dataset into the group.
- ``Move/Copy/Rename/Delete``: Edit the group (move, copy, rename, delete).
- ``Attributes``: View the group's attributes.

Feel free to add, delete, or modify these groups as needed, but be aware that some operations are irreversible.

.. warning::

   Always be cautious when deleting something.

