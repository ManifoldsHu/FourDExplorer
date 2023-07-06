# 4D - Explorer
-----------

[![4D-Explorer](https://iili.io/QkQPFn.png)](https://freeimage.host/i/QkQPFn)

4D-Explorer 是一款用于分析四维扫描透射电子显微镜 (4D-STEM) 数据的软件。它可以导入、存储 4D-STEM 数据集及其元数据，校正，并生成在实空间中的重构像。关于 4D-STEM 技术，见综述文章 [Colin Ohpus, 2019](https://www.cambridge.org/core/journals/microscopy-and-microanalysis/article/fourdimensional-scanning-transmission-electron-microscopy-4dstem-from-scanning-nanodiffraction-to-ptychography-and-beyond/A7E922A2C5BFD7FD3F208C537B872B7A)

## 可执行文件安装

从发布中，根据操作系统下载压缩包。目前只有 Windows 可用。对于 Linux 而言，请使用从 PyPI 安装。下载好之后解压，然后找到 4D-Explorer.exe 即可运行。

## 从 PyPI 安装

推荐使用 Anaconda 来设置 python 的编程环境：

```
conda update conda
conda create -n FourDExplorer python==3.10
conda activate FourDExplorer
pip install --upgrade FourDExplorer
```

然后启动 python：
```
python
```

进入 python 的交互式窗口后，输入以下命令启动软件：
```
>>> from FourDExplorer import FourDExplorer
>>> FourDExplorer.run()
```

## 测试数据 

测试数据马上就好。如果你手上有 HDF5 文件的话，可以直接用 4D-Explorer 打开。

## 快速上手

[![Main Window](https://iili.io/QktfJs.png)](https://freeimage.host/i/QktfJs)

### 数据管理

4D-Explorer 基于 [HDF5](https://www.hdfgroup.org/solutions/hdf5) 文件格式。要创建一个新的 HDF5 文件，请打开 'File' 菜单，然后按下 'New HDF5 File' 按钮。创建好后，再选好刚才创建的文件并打开。

[![Create a New File](https://iili.io/QkZiiP.png)](https://freeimage.host/i/QkZiiP)

一开始有 3 个群组 (group)：
- Calibration
- Reconstruction
- temp
显示在左边控制面板的 File 栏里。在 HDF5 文件中，群组就像是我们熟悉的文件夹，数据集 (dataset) 就像是文件一样。在这个 HDF5 文件中的群组、数据集都会显示在这个面板里。

[![Open H5](https://iili.io/Qkt9xp.png)](https://freeimage.host/i/Qkt9xp)

找到其中一个群组点鼠标右键，打开其菜单，就会显示可以对群组进行的操作，包括
- 'New' 在该群组下新建一个群组或者数据集。
- 'Import 4D-STEM dataset' 在该群组下导入一个 4D-STEM 数据集
- 'Move/Copy/Rename/Delete' 编辑这个群组.
- 'Attributes' 查看这个群组的属性.

[![Create a New Group 1](https://iili.io/QkZLf1.png)](https://freeimage.host/i/QkZLf1)

[![Create a New Group 2](https://iili.io/QkZPWB.png)](https://freeimage.host/i/QkZPWB)

可以随意增删查改这些群组，只要注意有些操作是不可逆的。

> 在删除某个东西的时候，永远要小心。

### 导入 4D-STEM 数据集
现在假如说我们已经有了一个二进制的 4D-STEM 数据集文件 (raw 文件) 想要导入到 HDF5 中。选好一个群组 (也可以点到根目录上)，右键，点击 'Import 4D-STEM Dataset'，这就打开了加载 4D-STEM 数据集的对话框。

[![Group Context Menu](https://iili.io/QkZQ0F.png)](https://freeimage.host/i/QkZQ0F)

[![Import Raw Data](https://iili.io/QkZDJa.png)](https://freeimage.host/i/QkZDJa)

选择 'General Raw Data'，然后点 'browse' 按钮选择我们要导入的 raw 文件。然后设定正确的参数，包括 4D-STEM 数据集四个维度的尺寸、数据类型、第一张图的起始字节位置、两张图之间间隔的字节数目以及字节序。然后，给我们要导入的数据集起一个名字叫 'gold_particle'。最后，点 OK。

> 目前据我们所知 [EMPAD](https://assets.thermofisher.com/TFS-Assets/MSD/Datasheets/EMPAD-Datasheet.pdf) 以及 [Merlin Medipix3](https://kt.cern/technologies/medipix3) 相机所产生的 RAW/MIB 文件是可以这样导入的。

> 如果你是 EMPAD 所产生的数据集，那么也可以选择 'EMPAD RAW DATA' 选项，然后点选数据集配套的 .xml 文件。这样，4D-Explorer 会自动解析这套数据的元数据，并自动导入。

### 执行任务
在我们加载数据集的时候，可以在左侧控制面板中的 'Task' 栏中查看进度、任务细节以及历史任务。

[![Loading Task](https://iili.io/QkZpbR.png)](https://freeimage.host/i/QkZpbR)

### 数据集的扩展名
现在我们可以在控制面板中的 'File' 栏里看到一个新的项 'gold_particle.4dstem'，就是我们刚刚导入的 4D-STEM 数据集。它有自己的图标和扩展名，4D-Explorer 就是通过这些扩展名来识别数据集的用途的。当然，扩展名不是必须的，就像我们平时在操作系统中识别文件一样。几种常见的扩展名：
- .4dstem : 4D-STEM 数据集，必须是 4 维的。
- .img : 灰度图像, 必须是 2 维的。
- .vec : 二维矢量场，具有两个分量。每个分量各自是张灰度图像。
- .line : 一条线，必须是 1 维的。

### 查看 4D-STEM 数据集
双击那个 'gold_particle.4dstem' 数据集即可打开。我们可以看到右边打开了一个页面。

[![View Dataset](https://iili.io/QktFgn.png)](https://freeimage.host/i/QktFgn)

> 提示：你可以拖动各个组件之间的边界，免得某些区域太小而显示得不好。

[![Set ADF](https://iili.io/QktJsI.png)](https://freeimage.host/i/QktJsI)

页面里面有两个图像，其中中间的是衍射图样，右边的是实空间的重构像。由于我们现在还没有重构，所以右边啥也没有，但我们还是可以点击右边的图像，这样游标就会跟随鼠标移动，左边就会显示不同位置的衍射斑。

### 重构
现在我们要赶紧重构一个看看效果。对着数据集点右键，找到 'Reconstruction' 菜单，然后选 'Virtual Image'。现在，右边打开了一个新的页面，用于选定 Virtual Image 的参数。现在，我们先重构一个环形暗场像 (ADF) 试试。

[![Open Virtual Image](https://iili.io/QktHWN.png)](https://freeimage.host/i/QktHWN)

选好参数后，点最下面 'START CALCULATION' 那个红色按钮。然后一个新的对话框就会问在哪里存储重构的图像。

> 假如说你没有看到红色的按钮，可以试试把最右边的滚动条往下拉。

[![Start Computing ADF](https://iili.io/Qkt2ft.png)](https://freeimage.host/i/Qkt2ft)

都准备好后就开始计算，和之前加载数据集的时候一样，这种长时间的任务都可以在左边的 'Task' 栏里查看细节。

[![View ADF](https://iili.io/Qkt30X.png)](https://freeimage.host/i/Qkt30X)

### 使用重构像作为预览

现在我们终于有了一个重构像，可以回到刚才的 4D-STEM 查看的页面了。我们可以点击 'BROWSE PREVIEW' 按钮，然后选刚才我们创建的重构像。

[![Browse Prevew](https://iili.io/QkZZUg.png)](https://freeimage.host/i/QkZZUg)

之后，我们就可以在4维相空间里探索该 4D-STEM 数据集了。

## 文档

TODO 

## 性能 

目前加载、重构 4D-STEM 数据集的速度基本上由磁盘 IO 的速度所决定。一个典型的 4 GB 的数据集，存储在机械硬盘上，100 MB/s 的IO速度，那么其重构就需要花费 40 秒。

4D-Explorer 不会一次性把整个数据集读进内存里，所以一般其内存占用不会很高，可以运行在个人电脑上。

## 引用

我们撰写的关于 4D-Explorer 的文章，请参考 [Arxiv](https://arxiv.org/abs/2306.08365)

## 协同开发

欢迎开源开发者协同开发~ Github 仓库地址是 (https://github.com/ManifoldsHu/FourDExplorer)

## 支持我们的工作

如果 4D-Explorer 对你有所帮助，请告诉我们~

我们的文章还在准备当中。

## 协议

4D-Explorer 遵循 GPLv3 协议。

胡一鸣
2020年10月8日
于南京大学

