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

4D-Explorer 基于 [HDF5](https://www.hdfgroup.org/solutions/hdf5/) 文件格式。HDF5 是一种用于存储和管理大量数据的文件格式，广泛应用于科学计算和数据分析领域。HDF5 文件由群组 (Groups) 和数据集 (Datasets) 组成，类似于电脑操作系统中的文件夹和文件。群组可以包含其他群组和数据集，形成一个层次结构，便于组织和管理复杂的数据。在透射电子显微镜 (TEM) 领域，HDF5 文件格式因其高效的数据存储和组织能力而被广泛采用，特别适用于处理和存储 4D-STEM 数据集。4D-STEM 数据集通常包含大量的衍射图像，形成一个高维数组，而其处理过程中的中间数据也会形成许多不同维度、尺寸及数据类型的数组。HDF5 的层次结构和压缩功能使得这些数据的存储和访问变得高效且灵活。

要创建一个新的 HDF5 文件，请在主界面的左上角打开 'File' 菜单，然后按下 'New HDF5 File' 按钮。之后，会自动弹出选择 HDF5 文件的对话框，此时选择刚刚创建的新 HDF5 文件即可打开。

[![Create a New File](https://iili.io/QkZiiP.png)](https://freeimage.host/i/QkZiiP)

在新创建的 HDF5 文件中空无一物，因而在左边控制面板的 File 栏里，只有一个 mydata.h5 的项，表示刚刚新建的 HDF5 文件。我们先创建一个群组，以放置我们将要导入的数据集。要创建群组，在左边的面板中，右击 mydata.h5，在弹出的菜单中选择 'New' (带有 + 号的图标)。在打开的创建项 (Create Item) 对话框中，有三个需要填写的地方：
- Location，也就是需要把群组创建在哪个群组下面。默认是 '/'，熟悉 Unix/Linux 的同学应该知道这表示根目录，而在 HDF5 文件中这也表示我们正在创建的项在根目录下，而不隶属于任何群组。点击 Browse... 按钮可以浏览并选择群组，从而把新创建的项放进这个群组中。不过，目前我们的 h5 文件中还没有任何群组，所以只能选择根目录。
- Name，也就是新建群组的名字。默认是 untitled，这里我们把它改成我们想要的名字，比如 gold_nanoparticle。注意，名字中不能包含斜杠 /、反斜杠 \ 、冒号 : 、星号 * 、问号 ? 、引号 " 、单引号 '、小于号 <、大于号 >、竖线 | 等特殊字符，不能以空格开头或结尾，也不能将点号 . 或者两个点号 .. 作为名字。总之，取名的限制和操作系统中文件名的限制差不多，建议选择不容易出错的取名方式，比如用下划线连接两个单词。
- Type，这里选 Group，也就是我们需要创建的是群组，而不是数据集 (Dataset)。

[![Create a New Group 1](https://iili.io/QkZLf1.png)](https://freeimage.host/i/QkZLf1)

[![Create a New Group 2](https://iili.io/QkZPWB.png)](https://freeimage.host/i/QkZPWB)

如果一切顺利的话，这时在左边控制面板的 File 栏里，应该能看到 mydata.h5 下面多挂了一个 gold_nanoparticle，并且图标是文件夹的项了。这就是我们刚刚创建的群组。鼠标右击这个群组，可以看到和刚刚差不多的菜单，里面有对一个群组可以进行的操作，包括：


