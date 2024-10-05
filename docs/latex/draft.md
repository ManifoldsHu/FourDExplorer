# 4D-Explorer

[![4D-Explorer](https://iili.io/QkQPFn.png)](https://freeimage.host/i/QkQPFn)

4D-Explorer 是一款用于分析四维扫描透射电子显微镜 (4D-STEM) 数据的软件。它可以导入、存储 4D-STEM 数据集及其元数据，校正，并生成在实空间中的重构像。关于 4D-STEM 技术，见综述文章 [Colin Ohpus, 2019](https://www.cambridge.org/core/journals/microscopy-and-microanalysis/article/fourdimensional-scanning-transmission-electron-microscopy-4dstem-from-scanning-nanodiffraction-to-ptychography-and-beyond/A7E922A2C5BFD7FD3F208C537B872B7A)

## 可执行文件安装

在仓库的发布 (Release) 页面，根据操作系统下载包含可执行文件的压缩包。目前仅支持 Windows 及 MacOS。若您使用的是 Linux，请使用 PyPI 安装。下载好压缩包后解压，找到 4D-Explorer.exe 即可运行。

## 使用 PyPI 安装 

推荐使用 Anaconda 来设置 python 的虚拟环境，要求使用 python 3.10 版本：

```
conda update conda
conda create -n FourDExplorerVenv python==3.10
```

创建好名为 FourDExplorerVenv 的虚拟环境后，激活该虚拟环境，然后使用 pip 安装 4D-Explorer：

```
conda activate FourDExplorerVenv
(FourDExplorerVenv) pip install --upgrade FourDExplorer
```

安装好后，启动 python，进入交互式窗口后，输入以下命令启动软件：
``` 
(FourDExplorerVenv) python 
>>> from FourDExplorer import FourDExplorer
>>> FourDExplorer.run()
```

## 测试数据 

TODO 

## 快速上手 

[![Main Window](https://iili.io/QktfJs.png)](https://freeimage.host/i/QktfJs)

### 数据管理 

4D-Explorer 基于 [HDF5](https://www.hdfgroup.org/solutions/hdf5/) 文件格式。HDF5 是一种用于存储和管理大量数据的文件格式，广泛应用于科学计算和数据分析领域。HDF5 文件由组 (Groups) 和数据集 (Datasets) 组成，类似于电脑操作系统中的文件夹和文件。组可以包含其他组和数据集，形成一个层次结构，便于组织和管理复杂的数据。在透射电子显微镜 (TEM) 领域，HDF5 文件格式因其高效的数据存储和组织能力而被广泛采用，特别适用于处理和存储 4D-STEM 数据集。4D-STEM 数据集通常包含大量的衍射图像，形成一个高维数组，而其处理过程中的中间数据也会形成许多不同维度、尺寸及数据类型的数组。HDF5 的层次结构和压缩功能使得这些数据的存储和访问变得高效且灵活。

要创建一个新的 HDF5 文件，请在主界面的左上角打开 'File' 菜单，然后按下 'New HDF5 File' 按钮。之后，会自动弹出选择 HDF5 文件的对话框，此时选择刚刚创建的新 HDF5 文件即可打开。

[![Create a New File](https://iili.io/QkZiiP.png)](https://freeimage.host/i/QkZiiP)



