# 4D - Explorer
----------------

![4D-Explorer](/docs/fig/View4DSTEM_MoS2.png)

4D-Explorer 是一款用于分析四维扫描透射电子显微镜 (4D-STEM) 数据的软件。它可以导入、存储 4D-STEM 数据集及其元数据，校正，并生成在实空间中的重构像。关于 4D-STEM 技术，见综述文章 [Colin Ohpus, 2019](https://www.cambridge.org/core/journals/microscopy-and-microanalysis/article/fourdimensional-scanning-transmission-electron-microscopy-4dstem-from-scanning-nanodiffraction-to-ptychography-and-beyond/A7E922A2C5BFD7FD3F208C537B872B7A)

## 可执行文件安装

从发布中，根据操作系统下载压缩包。目前支持 Windows 10、Windows 11 及 Mac OS。对于 Linux 而言，请使用从 PyPI 安装。下载好之后解压，然后找到 4D-Explorer.exe 即可运行。

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

我们提供三套测试数据，分别为 gold_nanoparticle_06, gold_nanoparticle_07 和 MoS2_14。三套测试数据的下载地址如下
- [Google Drive: 4D-Explorer Test Dataset](https://drive.google.com/drive/folders/1WaYyQNulZCERJQuW2GMvka0N5DNRpCFz?usp=sharing)
- [百度网盘: 4D-Explorer Test Dataset, 提取码: 64s2](https://pan.baidu.com/s/16G6rZUK95fogkg_GFg14hQ?pwd=64s2)

测试数据的参数见 [4D-Explorer Docs: Test Data](https://fourdexplorer.readthedocs.io/en/latest/test_dataset.html)

## 文档与教程

见 [4D-Explorer Docs](https://fourdexplorer.readthedocs.io/en/latest/index.html)

## 性能 

4D-Explorer 不会一次性把整个数据集读进内存里，所以一般其内存占用不会很高，可以运行在个人电脑上。

## 引用

我们撰写的关于 4D-Explorer 的文章，请参考 [Arxiv](https://arxiv.org/abs/2306.08365)

## 协同开发

欢迎开源开发者协同开发~ Github 仓库地址是 (https://github.com/ManifoldsHu/FourDExplorer)

## 支持我们的工作

如果 4D-Explorer 对你有所帮助，请告诉我们~

## 协议

4D-Explorer 遵循 GPLv3 协议。

胡一鸣
2020年10月8日
于南京大学

