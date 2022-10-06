# 4D-Explorer
-----------

4D-Explorer is a software to analyze four-dimensional scanning transmission electron microscopy (4D-STEM) data. It can import and save 4D-STEM datasets and their metadata, calibrate them and reconstruct images in real spaces. See [Colin Ohpus, 2019](https://www.cambridge.org/core/journals/microscopy-and-microanalysis/article/fourdimensional-scanning-transmission-electron-microscopy-4dstem-from-scanning-nanodiffraction-to-ptychography-and-beyond/A7E922A2C5BFD7FD3F208C537B872B7A) for more information.

## Installation FourDExplorer from Executable 

From releases, we download packages according to the operating system. Currently only Windows is available. For linux, see Installation FourDExplorer from Source instead.

Next, unzip the downloaded packages, and execute 4D-Explorer.exe to open the software.

## Installation FourDExplorer from Source

It is recommended to use Anaconda to set up the programming environment:

```
conda update conda
conda create -n FourDExplorer
conda activate FourDExplorer
conda install python==3.10
pip install FourDExplorer
```

Then, change the working directory to the source directory, and run python
```
python
```

Now, we import FourDExplorer module and run the GUI:
```
>>> import FourDExplorer
>>> ForDExplorer.run()
```

## Test Data 

Test 4D-STEM data will be available soon. You can use 4D-Explorer to open any HDF5 file directly.

## Quick Start

### Data manipulation
4D-Explorer is based on [HDF5](https://www.hdfgroup.org/solutions/hdf5). To create a new HDF5 file, find 'File' menu, and click 'New HDF5 File' option. Then, click 'Open HDF5 File' to open the created file before.

There are three groups initialized:
    - Calibration
    - Reconstruction
    - temp
which is shown in 'File' page of the left control panel. In a HDF5 file, groups are like folders or directories, and datasets are like files, and they are editable just like what we do in our operating system. All of the groups and datasets in the HDF5 file will display here. 

Right-click one of these groups and open a context menu, there are options available for this group, including:
    - 'New' to create a subgroup or a dataset
    - 'Import 4D-STEM dataset' to import a 4D-STEM dataset into this group.
    - 'Move/Copy/Rename/Delete' Edit this group.
    - 'Attributes' view the attributions of this group.

You can also create, move, copy, rename or delete these groups as you like, just note that undo may be NOT available. 
> Be careful when you delete something. 

### Import a 4D-STEM dataset 
Now, suppose we have a raw file from the Electron Microscopy. There are abundant diffraction images in that file, which is 4D-STEM dataset. Choose one group (root itself is also available), right click it, and click the 'Import 4D-STEM Dataset' option in the context menu. Then we have a dialog to import 4D-STEM dataset.

Choose 'General Raw Data' option as our Import File Type. Then, click the 'browse' button to choose the raw file we want to import. Then set correct parameters, including dataset size, data type, offset of the first image, gap between two images, and whether it is little-endian. Next, name it in the bottom 'IMPORT TO' region. Here, we set the name of imported dataset to be 'mydataset'. When all is ready, click 'OK'.

> As far as we know, raw data from [EMPAD](https://assets.thermofisher.com/TFS-Assets/MSD/Datasheets/EMPAD-Datasheet.pdf) and from [Merlin Medipix3](https://kt.cern/technologies/medipix3) can be imported using this method. 

> If you have an EMPAD dataset, you can choose 'EMPAD RAW Data' option, and use the .xml file. 4D-Explorer will parse the metadata of the dataset automatically.

### Executing Tasks
When we loading the dataset, a task is created and executed in the 'Task' panel at the left of the software. We can see task details, proceeding rates, and history tasks here.

### Dataset Extension
we can see a new item in the HDF5 file control panel at the left of the main window. This item, with 'mydataset.4dstem' as its name and a cube as its icon, is what we imported above. 4D-Explorer use extension name to recognize what a dataset is, but this is not absolute, just like what we do in Linux system. There are several usual extensions:
    - .4dstem : This is 4D-STEM dataset, with demension 4
    - .img : This is gray-scale image, with dimension 2.
    - .vec : This is vector field, with two components. Each component is an 2D-image.
    - .line : This is a line, with dimension 1.

### View 4D-STEM dataset
Double click the 4D-STEM dataset we imported above: 'mydataset.4dstem' at the left control panel. We will see a opened page at the right side. 

> Hint: for best visualization, maximize the main window, and adjust the width, height of the visual window and its companion control panel.

There are 2 images, one is the diffraction image, at the middle; the other is the real space image. However, we have not reconstruct any image yet, so its just idle. Nevertheless, we can still drag the cursor of the real space, and 'explore' diffraction images at different locations.

### Recontruction 
What we need is a quick reconstruction. Right click the dataset at the file panel, and open 'Reconstruction' menu, choose the 'Virtual Image' option. After that, a new page is opened for reconstruction. Here, we first compute a bright field image (BF). 

After choose our parameters, click the red button 'START CALCULATION' at the bottom of the page. Then, a dialog is opened to choose where to save the output image. 

> If you don't see any button, try dragging the scroll bar at the right of the page to the bottom.

After all is ready, again, a task is submitted and executed. Wait for a moment, and we can view our BF image.

### Use Image for Previewing
Now, we have generated a new image. Back to 4D-Explorer viewing page, we can click the 'BROWSE PREVIEW' button, and choose the reconstructed image we produced above.

After that, we can explore the 4D-STEM dataset in both real space and diffraction space.


## Further Topics

### Calibration 
TODO

### DPC 
TODO 


## Performance 

The speed of the 4D-STEM dataset loading and reconstruction is basically determined by the disk IO speed. For a typical 1 GB dataset stored in HDD hard disk with 100 MB/s read-out speed, it takes about 10 seconds for reconstruction. 

4D-Explorer never read the whole dataset into memory at once. It usually does not requires large memory for computing. 


## Contribution 

It is welcome for contributing. See [Github Repository](https://github.com/ManifoldsHu/FourDExplorer)

## Support Our Work

If this work helps you in your research, please let us know! 

Our article is in preparation.

## LICENSE 

4D-Explorer is under GPLv3 license. See LICENSE file in the repository. 










[![Main Window of 4D-Explorer](https://iili.io/sRI8Ob.md.png)](https://freeimage.host/i/sRI8Ob)

Hu Yiming
Oct 6, 2022
Nanjing University
