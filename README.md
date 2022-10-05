# 4D-Explorer
-----------

4D-Explorer is a software to analyze four-dimensional scanning transmission electron microscopy (4D-STEM) data. It can import and save 4D-STEM datasets and their metadata, calibrate them and reconstruct images in real spaces. 

The software will be released soon.

## Download 

Download packages according to your operating system. Unzip it, and run 4D-Explorer.exe (in Windows) directly.

## Test Data 

Test 4D-STEM data will be available soon. You can also use 4D-Explorer to open any HDF5 file directly.

## For Developers

It is recommended to use Anaconda to set up the programming environment:

```
conda create -n FourDExplorer
conda activate FourDExplorer
conda install python=3.10
pip install h5py 
pip install numpy
pip install matplotlib
pip install psutil
pip install pyinstaller 
pip install pyside6 
pip install qt-material
pip install scikit-image
pip install scipy  
```

Then, change the working directory to the source directory, and run the software
```
python FourDExplorer.py
```



[![Main Window of 4D-Explorer](https://iili.io/sRI8Ob.md.png)](https://freeimage.host/i/sRI8Ob)

Hu Yiming
Oct 6, 2022
Nanjing University
