# 4D-Explorer
----------------

![4D-Explorer](/docs/fig/View4DSTEM_MoS2.png)

4D-Explorer is a software to analyze four-dimensional scanning transmission electron microscopy (4D-STEM) data. It can import and save 4D-STEM datasets and their metadata, calibrate them and reconstruct images in real space. See [Colin Ohpus, 2019](https://www.cambridge.org/core/journals/microscopy-and-microanalysis/article/fourdimensional-scanning-transmission-electron-microscopy-4dstem-from-scanning-nanodiffraction-to-ptychography-and-beyond/A7E922A2C5BFD7FD3F208C537B872B7A) for more information.

## Installation FourDExplorer from Executable 

From releases, we download packages according to the operating system. Currently, Windows 10, Windows 11 and MacOS are supported. For Linux, see Installation FourDExplorer from Source instead.

Next, unzip the downloaded packages, and execute 4D-Explorer.exe to open the software.

## Installation FourDExplorer from PyPI

It is recommended to use Anaconda to set up the programming environment:

```
conda update conda
conda create -n FourDExplorer python==3.10
conda activate FourDExplorer
pip install --upgrade FourDExplorer
```

Then, run python
```
python
```

Now, we import the FourDExplorer module and run the GUI:
```
>>> from FourDExplorer import FourDExplorer
>>> FourDExplorer.run()
```

## Test Data 

We provide three sets of test data, namely gold_nanoparticle_06, gold_nanoparticle_07, and MoS2_14. The download links for these datasets are as follows:
- [Google Drive: 4D-Explorer Test Dataset](https://drive.google.com/drive/folders/1WaYyQNulZCERJQuW2GMvka0N5DNRpCFz?usp=sharing)
- [Baidu Netdisk: 4D-Explorer Test Dataset, Extraction Code: 64s2](https://pan.baidu.com/s/16G6rZUK95fogkg_GFg14hQ?pwd=64s2)

The parameters of the test data can be found in the [4D-Explorer Docs: Test Data](https://fourdexplorer.readthedocs.io/en/latest/test_dataset.html)

## Documentation and Tutorials

See [4D-Explorer Docs](https://fourdexplorer.readthedocs.io/en/latest/index.html) for detailed documentation and tutorials.


## Performance 

4D-Explorer never read the whole dataset into memory at once. It usually does not require large memory for computing. 

## Cite

Our article about this software can be found in [Arxiv](https://arxiv.org/abs/2306.08365)

## Contribution 

It is welcome for contributing. See [Github Repository](https://github.com/ManifoldsHu/FourDExplorer)

## Support Our Work

If this work helps you in your research, please let us know! 

## LICENSE 

4D-Explorer is under GPLv3 license. See LICENSE file in the repository. 


Hu Yiming
Oct 8, 2022
Nanjing University
