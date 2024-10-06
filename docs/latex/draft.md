# 4D-Explorer

[![4D-Explorer](https://iili.io/QkQPFn.png)](https://freeimage.host/i/QkQPFn)

4D-Explorer 是一款用于分析四维扫描透射电子显微镜 (4D-STEM) 数据的软件。它可以导入、存储 4D-STEM 数据集及其元数据，校正，并生成在实空间中的重构像。关于 4D-STEM 技术，见综述文章 [Colin Ohpus, 2019](https://www.cambridge.org/core/journals/microscopy-and-microanalysis/article/fourdimensional-scanning-transmission-electron-microscopy-4dstem-from-scanning-nanodiffraction-to-ptychography-and-beyond/A7E922A2C5BFD7FD3F208C537B872B7A)

## 安装方法
### 可执行文件安装

在仓库的发布 (Release) 页面，根据操作系统下载包含可执行文件的压缩包。目前仅支持 Windows 及 MacOS。若您使用的是 Linux，请使用 PyPI 安装。下载好压缩包后解压，找到 4D-Explorer.exe 即可运行。

### 使用 PyPI 安装 

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
- 'New' 在该群组下新建一个群组或者数据集。
- 'Import 4D-STEM dataset' 在该群组下导入一个 4D-STEM 数据集
- 'Move/Copy/Rename/Delete' 编辑这个群组(移动、复制、重命名、删除).
- 'Attributes' 查看这个群组的属性.

可以随意增删查改这些群组，只要注意有些操作是不可逆的。

> 在删除某个东西的时候，永远要小心。

### 导入 4D-STEM 数据集 
现在假如说我们已经有了一个二进制的 4D-STEM 数据集文件 (raw 文件) 想要导入到 HDF5 中。选好一个群组 (也可以点到根目录上)，右键，点击 'Import 4D-STEM Dataset'，这就打开了加载 4D-STEM 数据集的对话框。

[![Group Context Menu](https://iili.io/QkZQ0F.png)](https://freeimage.host/i/QkZQ0F)

[![Import Raw Data](https://iili.io/QkZDJa.png)](https://freeimage.host/i/QkZDJa)

选择 'General Raw Data'，然后点 'browse' 按钮选择我们要导入的 raw 文件。在这里，我们选择测试数据集 gold nanoparticle 中所提供的 scan_x256_y256.raw 文件。然后设定正确的参数，包括： 
- Scalar Type, 4D-STEM 数据集的像素值类型，这里选择 float。
- Scalar Size, 4D-STEM 数据集的像素值大小，这里选择 32 bit。
- Image Width, 衍射图像的宽度，这里设置为 128。
- Image Height, 衍射图像的高度，这里设置为 128。
- Number of Scanning Columns (scan_i), i 方向扫描的数目，这里设置为 256。
- Number of Scanning Rows (scan_j), j 方向扫描的数目，这里设置为 256。
- Offset to First Image (bytes), 第一张衍射图像的偏移量，以字节为单位，这里设置为 0。
- Gap Between Images, 每张衍射图像之间的间隔，以字节为单位，这里设置为 1024。 
- Little-endian Byte Order, 数据集的存储顺序，这里勾选上

接下来还要选取在读取时需要进行旋转和翻转的操作。对于提供的测试数据集 gold nanoparticle，进行如下设定： 
- Flip Diffraction Pattern (Transpose) 将衍射图像翻转，即沿着从左上到右下的线翻转，这里勾选上
- Rotate n×90° 将衍射图像进行逆时针旋转 90° 的次数。旋转 3 次等效于顺时针旋转 90°，这里设为 1。

然后，给我们要导入的数据集起一个名字叫 'gnp_01'。最后，点 OK 按钮。

### 执行任务 
在我们加载数据集的时候，可以在左侧控制面板中的 'Task' 栏中查看进度、任务细节以及历史任务。

### 数据集的扩展名
现在我们可以在控制面板中的 'File' 栏里看到一个新的项 'gnp_01.4dstem'，就是我们刚刚导入的 4D-STEM 数据集。它有自己的图标和扩展名，4D-Explorer 就是通过这些扩展名来识别数据集的用途的。当然，扩展名不是必须的，就像我们平时在操作系统中识别文件一样。目前 4D-Explorer 可以识别这几种扩展名：
- .4dstem : 4D-STEM 数据集，必须是 4 维数组
- .img : 灰度图像，必须是 2 维数组。不支持 RGB 彩色图像或其他多通道图像。
- .vec : 二维矢量场，具有两个分量。每个分量各自是一张灰度图像。
- .line : 一条线，必须是 1 维的。

### 查看 4D-STEM 数据集 
双击那个 gnp_01.4dstem 数据集即可打开。我们可以看到右边打开了一个页面。

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

## 校正 4D-STEM 数据集 

对于精确的、定量化的 4D-STEM 成像而言，细致的校正往往是很重要的。目前 4D-Explorer 内置了四个校正 4D-STEM 数据集的步骤，分别是：
- 完善数据集的实验参数
- 去除背景噪声
- 扫描旋转校正
- 衍射合轴

### 完善数据集的实验参数 

### 去除背景噪声 

我们提供两种去除背景噪声的办法，分别是
