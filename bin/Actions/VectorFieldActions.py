# -*- coding: utf-8 -*-

"""
*------------------------- VectorFieldActions.py -----------------------------*
针对矢量场操作的 Action。

作者：          胡一鸣
创建日期：      2022年6月24日

This module includes actions towards vector fields.

author:         Hu Yiming
date:           Jun 24, 2022
*------------------------- VectorFieldActions.py -----------------------------*
"""

from PySide6.QtCore import QObject 
from PySide6.QtWidgets import QWidget, QInputDialog

from bin.Actions.EditActions import ActionEditBase 
from bin.Actions.EditActions import failLogging
from bin.HDFManager import HDFType
from bin.TaskManager import TaskManager
from bin.Widgets.DialogChooseItem import DialogHDFChoose
from bin.Widgets.PageViewVectorField import DialogSaveVectorField
from bin.Widgets.PageVirtualImage import DialogSaveImage
from lib.TaskVectorFieldProcess import TaskCurl
from lib.TaskVectorFieldProcess import TaskDivergence
from lib.TaskVectorFieldProcess import TaskFlipVectorField
from lib.TaskVectorFieldProcess import TaskPotential
from lib.TaskVectorFieldProcess import TaskRotateVectorAngle
from lib.TaskVectorFieldProcess import TaskSliceI
from lib.TaskVectorFieldProcess import TaskSliceJ
from lib.TaskVectorFieldProcess import TaskSubtractVectorOffset
from lib.TaskVectorFieldProcess import TaskSubtractVectorField


class ActionVectorFieldProcessingBase(ActionEditBase):
    """
    用于对 VectorField 进行计算的 Action 的基类。
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)

    @property
    def task_manager(self) -> TaskManager:
        global qApp
        return qApp.task_manager

    def getResultPath(self, result_type: HDFType) -> tuple[str]:
        """
        Open a dialog to get the path of the result.

        The result_type must be HDFType.Image or HDFType.VectorField.

        arguments:
            result_type: (Literal[HDFType.Image, HDFType.VectorField])

        returns:
            (tuple[str]) returns image_name and image_parent_path
        """
        if result_type == HDFType.VectorField:
            dialog_save = DialogSaveVectorField()
        elif result_type == HDFType.Image:
            dialog_save = DialogSaveImage()
        else:
            raise TypeError('The result_type must be HDFType.Image or '
                'HDFType.VectorField, not {0}'.format(
                    type(result_type).__name__
            ))
        dialog_save.setParentPath(self.item_path)
        dialog_code = dialog_save.exec()
        if not dialog_code == dialog_save.Accepted:
            return 
        image_name = dialog_save.getNewName()
        image_parent_path = dialog_save.getParentPath()
        return image_parent_path, image_name 
        



class ActionRotateVector(ActionVectorFieldProcessingBase):
    """
    对矢量场中的每个矢量的方向进行旋转的 Action。

    矢量场中的每个矢量都定义在 2-流形(实空间)的切空间上。但在产生矢量场的时候，可能在
    切空间坐标系和 2-流形坐标系之间产生旋转。例如，在 STEM 中电子束的扫描方向相对于相
    机的放置方向有一定的偏转，就会导致这种现象。如果不校正这种旋转，会使得恢复出来的静
    电场分布不满足保守场的特性，从而在物理上是不合法的。

    在这里，我们提供简单的办法来校正这种旋转偏差：将每个矢量都旋转一定的角度，使得它重
    新变成保守场(或者对于磁场而言，有旋无源场)。

    Action to rotate every vector's orientation in the field.

    Each vector in a vector field is defined on the tangent space of a 
    2-manifold (real space). However, when generating the vector field, it is 
    possible to generate rotation between the tangent space coordinate system 
    and the 2-manifold coordinate system. For example, a deflection of the 
    scanning direction of the electron beam in STEM relative to where the 
    camera is placed can cause this phenomenon. If this rotational offset is 
    not corrected, the recovered electrostatic field distribution will not meet 
    the characteristics of conservative field, so it is physically illegal.

    Here we offer a simple way to correct for this rotation bias: rotate each 
    vector by an Angle so that it becomes a conservative field again (or, in 
    the case of magnetic field, a solenoidal field).
    """
    
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Rotate Vector Angle')
        self.triggered.connect(lambda: self.rotateVectors(self))

    @failLogging 
    def rotateVectors(self):
        """
        Open a dialog to rotate an angle for every vector.
        """
        angle, is_accpeted = QInputDialog.getDouble(
            self,
            'Input rotation angle',
            'Here input a rotation angle for every vector. Unit: deg',
            0,
            minValue = -360,
            maxValue = 360,
            decimals = 1,
            step = 1,
        )

        if not is_accpeted:
            return 

        image_parent_path, image_name = self.getResultPath(
            HDFType.VectorField
        )
        meta = self.hdf_handler.file[self.item_path].attrs 
        self.task = TaskRotateVectorAngle(
            self.item_path,
            image_parent_path,
            image_name,
            angle = angle,
            parent = self,
            **meta
        )
        self.task_manager


class ActionSubtractMeanVector(ActionVectorFieldProcessingBase):
    """
    对矢量场中的每个矢量都减去该矢量场的平均矢量的 Action。

    Subtract every vector by their mean vector.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Subtract Mean Vector')
        self.triggered.connect(lambda: self.subtractMean(self))

    @property
    def task_manager(self) -> TaskManager:
        global qApp 
        return qApp.task_manager

    @failLogging
    def subtractMean(self):
        """
        Open a dialog to subtract vectors by their mean vector.
        """
        image_parent_path, image_name = self.getResultPath(HDFType.VectorField)
        meta = self.hdf_handler.file[self.item_path].attrs 
        self.task = TaskSubtractVectorOffset(
            self.item_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )


class ActionFlipComponents(ActionVectorFieldProcessingBase):
    """
    对矢量场中的每个矢量都交换其 i, j 方向的分量值。

    矢量场中的每个矢量都定义在 2-流形(实空间)的切空间上。但在产生矢量场的时候，可能在
    切空间坐标系和 2-流形坐标系之间产生手性翻转。例如，在 STEM 中电子束的扫描方向相对
    于相机的放置方向有所翻转，就会导致这种现象。此外，不同硬件、软件所依照的坐标系约定
    也可能有所不同。在处理矩阵、图像、直角坐标系时，常用的坐标约定有：

        ┌------------> j        ^ y
        |                       |
        |                       |
        |                       |
        |                       |
        v                       |
        i                       └----------------> x

    很明显这两种坐标系都是右手系。但有时也会碰到左手系：

        ┌------------> x       
        |                       
        |                      
        |                       
        |                       
        v                       
        y

    在 4D-Explorer 中我们使用 i-j 坐标系，这是一种右手系。这样计算、展示的图像结果就
    和采用左手系约定的程序有所不同。两种情形下的矢量场只有一种在物理上是合法的。

    我们提供一种简单的方法来修正这种问题：将每个矢量的 i, j 分量进行调换，从而将其手性
    变成在物理上合法的状态。

    For each vector in the vector field we swap its I and j components.

    Each vector in a vector field is defined on the tangent space of a 
    2-manifold (real space). However, when generating the vector field, it is 
    possible to produce a chiral inversion between the tangent space coordinate 
    system and the 2-manifold coordinate system. For example, a reversal of the 
    scanning direction of the electron beam in STEM relative to the orientation 
    of the camera can cause this phenomenon. In addition, the coordinate system 
    conventions in different hardwares or softwares can also be different. In 
    dealing with matrix, image and cartesian coordinate system, commonly used 
    coordinate conventions are:

        ┌------------> j        ^ y
        |                       |
        |                       |
        |                       |
        |                       |
        v                       |
        i                       └----------------> x

    It's clear that both of these coordinate systems are right-handed.But you 
    can sometimes meet into left-handed systems:

        ┌------------> x       
        |                       
        |                      
        |                       
        |                       
        v                       
        y

    In 4D-Explorer we use the i-J coordinate system, which is a right-handed 
    system.In this way, the results of the calculation and display of the image 
    are different from the program using the left hand system convention. Only 
    one of the two cases of a vector field is physically valid.

    We provide a simple way to fix this problem: transpose the I and j 
    components of each vector, thereby turning its chirality into a physically 
    legal state.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Flip Vector Components')
        self.triggered.connect(lambda: self.flipComponents(self))

    @failLogging
    def flipComponents(self):
        """
        Open a dialog to flip the components of vector fields.
        """
        image_parent_path, image_name = self.getResultPath(HDFType.VectorField)
        meta = self.hdf_handler.file[self.item_path].attrs 
        self.task = TaskFlipVectorField(
            self.item_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)


class ActionSubtractReferenceVector(ActionVectorFieldProcessingBase):
    """
    让矢量场减去参考/背景的矢量场。

    Subtract a reference/background vector field.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Subtract Reference')
        self.triggered.connect(lambda: self.subtractReference(self))

    @failLogging 
    def subtractReference(self):
        """
        Open a dialog to subtract the reference.
        """
        dialog = DialogHDFChoose()
        dialog_code = dialog.exec()
        if dialog_code == dialog.Accepted:
            reference_path = dialog.getCurrentPath()
        image_parent_path, image_name = self.getResultPath(HDFType.VectorField)
        meta = self.hdf_handler.file[self.item_path].attrs 
        self.task = TaskSubtractVectorField(
            self.item_path,
            reference_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)

class ActionPotential(ActionVectorFieldProcessingBase):
    """
    计算矢量场的势。

    矢量场应当是无旋场 (保守场)，否则结果在物理上是非法的。

    Calculate the potential of the vector fields.

    The vector field should be a non-curl field, otherwise the result is 
    invalid in physics.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Calculate Potential')
        self.triggered.connect(lambda: self.calculatePotential(self))

    @failLogging
    def calculatePotential(self):
        """
        Open a dialog to calculate potential.
        """
        image_parent_path, image_name = self.getResultPath(HDFType.Image)
        meta = self.hdf_handler.file[self.item_path].attrs 
        self.task = TaskPotential(
            self.item_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)


class ActionDivergence(ActionVectorFieldProcessingBase):
    """
    计算矢量场的散度。

    Calculate the divergence of the vector fields.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Calculate Divergence')
        self.triggered.connect(lambda: self.calculateDivergence(self))
    
    @failLogging
    def calculateDivergence(self):
        """
        Open a dialog to calculate divergence.
        """
        image_parent_path, image_name = self.getResultPath(HDFType.Image)
        meta = self.hdf_handler.file[self.item_path].attrs 
        self.task = TaskDivergence(
            self.item_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)

    
class ActionCurl(ActionVectorFieldProcessingBase):
    """
    计算矢量场的旋度。

    Calculate the curl of the vector field.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Calculate Curl')
        self.triggered.connect(lambda: self.calculateCurl(self))

    @failLogging
    def calculateCurl(self):
        """
        Open a dialog to calculate the curl of the vector fields.
        """
        image_parent_path, image_name = self.getResultPath(HDFType.Image)
        meta = self.hdf_handler.file[self.item_path].attrs 
        self.task = TaskCurl(
            self.item_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)


class ActionSliceI(ActionVectorFieldProcessingBase):
    """
    提取矢量场的 i 方向分量的 Action。

    Slice i-component for the vector field.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Slice i-Components')
        self.triggered.connect(lambda: self.sliceIComponent(self))

    @failLogging
    def sliceIComponent(self):
        """
        Open a dialog to slice i-component of the vectors.
        """
        image_parent_path, image_name = self.getResultPath(HDFType.Image)
        meta = self.hdf_handler.file[self.item_path].attrs 
        self.task = TaskSliceI(
            self.item_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)


class ActionSliceJ(ActionVectorFieldProcessingBase):
    """
    提取矢量场的 j 方向分量的 Action。

    Slice j-component for the vector field.
    """
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.setText('Slice j-Components')
        self.triggered.connect(lambda: self.sliceJComponent(self))

    @failLogging
    def sliceJComponent(self):
        """
        Open a dialog to slice i-component of the vectors.
        """
        image_parent_path, image_name = self.getResultPath(HDFType.Image)
        meta = self.hdf_handler.file[self.item_path].attrs 
        self.task = TaskSliceJ(
            self.item_path,
            image_parent_path,
            image_name,
            parent = self,
            **meta,
        )
        self.task_manager.addTask(self.task)






