"""
Probe.py

其中包括了 OpticalSTEM 的 class，里面包括各种实验参数，以及 Probe。
"""

from enum import Enum
from collections.abc import Mapping 
from typing import Iterator, Iterable

import numpy as np
from scipy.special import j0 as bessel_j0
# import matplotlib.pyplot as plt

# Constants as defined in CODATA 2022
h = 6.62607015e-34                # 普朗克常量
e = 1.602176634e-19                 # 元电荷
m = 9.1093837139e-31                 # 电子静质量
c = 299792458                   # 光速

# class AberrationTypes(Enum):
#     """
#     Valid Types of Aberrations.
#     """
#     C1 = 10     # defocus
#     A1 = 11     # two-fold astigmatism
#     B2 = 22     # axial coma
#     A2 = 21     # three-fold astigmatism
#     C3 = 30     # spherical aberration
#     S3 = 34     # star aberration
#     A3 = 31     # four-fold astigmatism
#     B4 = 42     # axial coma
#     D4 = 45     # three lobe aberration
#     A4 = 41     # five-fold astigmatism
#     C5 = 50     # spherical aberration
#     A5 = 51     # sixfold astigmatism
   

class AberrationDict(Mapping):
    """
    AberrationDict 记录了像差函数的各项系数，包括

    'C1'    # defocus
    'A1'    # two-fold astigmatism
    'B2'    # axial coma
    'A2'    # three-fold astigmatism
    'C3'    # spherical aberration
    'S3'    # star aberration
    'A3'    # four-fold astigmatism
    'B4'    # axial coma
    'D4'    # three lobe aberration
    'A4'    # five-fold astigmatism
    'C5'    # spherical aberration
    'A5'    # sixfold astigmatism

    其中各项系数都为国际单位制。遵循
    S. Uhlemann, M. Haider Ultramicroscopy, 78(1999): 1-11
    给出的约定。

    该类遵循和 dict 类似的语法，但读取和写入的规则是不同的。读取时，总是会读出 float 或者 complex，但写入时，可以为 float，complex 以及 (模长, 角度) 的 tuple 元组。

        a = aberration_dict['C1']       # a is defocus

        b = aberration_dict['A2']       # b is three-fold astigmatism, which 
                                        # is a complex

        aberration_dict['C1'] = 1e-8    # set defocus to 10 nm, while do not change its angle. (In this case, the angle of defocus does not contribute to the aberration function)

        aberration_dict['B2'] = [2e-8, 30]    # set axial coma to 2e-8 * exp(1j * pi/6)

        aberration_dict['A1'] = 2e-8 + 1j * 1e-8    # set two-fold astigmatism to 2e-8 + 1j * 1e-8 
    """


    # 各个像差的角度，在形成复系数的幅角时需要乘以的系数
    _aberration_angle_multipliers = {
        'C1': 1,    # defocus
        'A1': 2,    # two-fold astigmatism
        'B2': 1,    # axial coma
        'A2': 3,    # three-fold astigmatism
        'C3': 1,    # spherical aberration
        'S3': 2,    # star aberration
        'A3': 4,    # four-fold astigmatism
        'B4': 1,    # axial coma
        'D4': 3,    # three lobe aberration
        'A4': 5,    # five-fold astigmatism
        'C5': 1,    # spherical aberration
        'A5': 6,    # sixfold astigmatism
    }

    def __init__(self, **kw):
        """
        初始化 AberrationDict。

        keyword 参数必须是以下之一：
            'C1'    # defocus
            'A1'    # two-fold astigmatism
            'B2'    # axial coma
            'A2'    # three-fold astigmatism
            'C3'    # spherical aberration
            'S3'    # star aberration
            'A3'    # four-fold astigmatism
            'B4'    # axial coma
            'D4'    # three lobe aberration
            'A4'    # five-fold astigmatism
            'C5'    # spherical aberration
            'A5'    # sixfold astigmatism
        并且值必须为 float, complex 或者长度为 2 的 Interable。
        
        如果值是 float, 则
            - 它表示国际单位制下的各项像差系数的模长，而不改变角度
            - 如果只想改变角度，请使用 setAngle() 方法
        如果值是长度为 2 的 Iterable，则
            - 第一个值表示国际单位制下的各项像差系数
            - 第二个值表示这项像差的旋转的角度，单位为 deg (°)
        如果值为 complex，则
            - 其将直接应用为像差系数，模长单位为国际单位，而不作进一步处理
        
        遵循
        S. Uhlemann, M. Haider Ultramicroscopy, 78(1999): 1-11
        给出的约定。
        """
        super().__init__()
        self._mapping = {}
        for key in self._aberration_angle_multipliers:
            self._mapping[key] = 0

        for key in kw:
            self[key] = kw[key]

    def __getitem__(self, key: str) -> tuple:
        return self._mapping[key] 
    
    def getModule(self, key: str) -> float:
        """
        获取像差系数的模长，单位 m
        """
        return np.abs(self[key])
    
    def getAngle(self, key: str) -> float:
        """
        获取像差系数的角度，单位为 deg (°)

        注意，这里的角度并非是复像差系数的幅角，而是设置像差系数的面板上的角度。它们之间很可能相差一定的倍数。例如，对于 A1 (two-fold astigmatism) 而言，如果其值为 1 + 1j，则函数得到的结果为 22.5。
        """
        return np.angle(self[key], deg=True) / self._aberration_angle_multipliers[key]
    
    def getComplexAngle(self, key: str) -> float:
        """
        获取像差系数作为复数的幅角，单位为 rad。

        注意，这里的角度就是作为复数的俯角，与 getAngle() 的结果不同。
        """
        return np.angle(self[key], deg=False)
    
    def __iter__(self) -> Iterator:
        return iter(self._mapping)

    def __len__(self) -> int:
        return 12 

    def __str__(self) -> str:
        return f"<AberrationDict> defocus: {self['C1']} m, chromatic aberration: {self['C3']} m"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __setitem__(self, key: str, value: list[float]):
        """
        keyword 参数必须是以下之一：
            'C1'    # defocus
            'A1'    # two-fold astigmatism
            'B2'    # axial coma
            'A2'    # three-fold astigmatism
            'C3'    # spherical aberration
            'S3'    # star aberration
            'A3'    # four-fold astigmatism
            'B4'    # axial coma
            'D4'    # three lobe aberration
            'A4'    # five-fold astigmatism
            'C5'    # spherical aberration
            'A5'    # sixfold astigmatism
        并且值必须为 float, complex 或者长度为 2 的 Interable。
        
        如果值是 float, 则
            - 它表示国际单位制下的各项像差系数，角度默认为 0
        如果值是长度为 2 的 Iterable，则
            - 第一个值表示国际单位制下的各项像差系数
            - 第二个值表示这项像差的旋转的角度，单位为 deg (°)
        如果值为 complex，则
            - 其将直接应用为像差系数，模长单位为国际单位，而不作进一步处理
        """
        if key in self._aberration_angle_multipliers:
            if isinstance(value, complex):
                self._mapping[key] = value 
            elif isinstance(value, (float, int)):
                self.setModule(key, value)
            elif isinstance(value, (Iterable, tuple, list,)):
                self._mapping[key] = self._calc_complex_aberration(key, value[0], value[1])
            else:
                raise TypeError(
                    f"The value of {key} must be a float or an Iterable of length 2, rather than {type(value)}"
                )
        else:
            raise KeyError(
                f"{key} is not a valid aberration name, it should be one of " 
                f"{list(self._aberration_angle_multipliers.keys())}"
            )

    def _calc_complex_aberration(self, key: str, module: float, angle: float):
        return module * np.exp(
            1j * np.pi / 180 * self._aberration_angle_multipliers[key] * angle
        )

    def __delitem__(self, key: str):
        if key in self._mapping:
            self._mapping[key] = 0

    def setAngle(self, key: str, value: float):
        """
        设置某项像差的角度，而不改变其复模长。
        
        注意，这里的角度可能并不等于复数的幅角，而可能相差一定的倍数。
        """
        module = self.getModule(key)
        coefficient = self._calc_complex_aberration(key, module, value)
        self._mapping[key] = coefficient

    def setModule(self, key: str, value: float):
        """
        设置某项像差的模长，而不改变其幅角。
        """
        module = value 
        angle = self.getAngle(key)
        coefficient = self._calc_complex_aberration(key, module, angle)
        self._mapping[key] = coefficient

    def setAberrationDictFromList(self, aberration_list: list):
        """
        从 aberration list 中读取数据，并据此构建 AberrationDict。

        aberration list 必须是 12 x 2 的 list，其第一列表示各项球差系数的大小；第二列表示各项球差系数的旋转角度，单位为 deg (°)。

        这个函数方便兼容已有的代码，故 aberration_list 的各项单位也遵循已有代码的约定。具体为：

        C1: nm      defocus
        A1: nm      two-fold astigmatism
        B2: nm      axial coma
        A2: nm      three-fold astigmatism
        C3: um      spherical aberration
        S3: um      star aberration
        A3: um      four-fold astigmatism
        B4: um      axial coma
        D4: um      three lobe aberration
        A4: um      five-fold astigmatism
        C5: mm      spherical aberration
        A5: mm      sixfold astigmatism

        """
        if not isinstance(aberration_list, (Iterable, list, tuple, np.ndarray)):
            raise TypeError("aberration_list must be an Iterable")
        if len(coeffi) != 12:
            raise ValueError("aberration_list must be an list with shape 12 x 2")
        for coeffi in aberration_list:
            if len(coeffi) != 2:
                raise ValueError("aberration_list must be an list with shape 12 x 2")
        tmp_dict = {}
        tmp_dict['C1'] = [aberration_list[0, 0] * 1e-9, aberration_list[0, 1]]
        tmp_dict['A1'] = [aberration_list[1, 0] * 1e-9, aberration_list[1, 1]]
        tmp_dict['B2'] = [aberration_list[2, 0] * 1e-9, aberration_list[2, 1]]
        tmp_dict['A2'] = [aberration_list[3, 0] * 1e-9, aberration_list[3, 1]]
        tmp_dict['C3'] = [aberration_list[4, 0] * 1e-6, aberration_list[4, 1]]
        tmp_dict['S3'] = [aberration_list[5, 0] * 1e-6, aberration_list[5, 1]]
        tmp_dict['A3'] = [aberration_list[6, 0] * 1e-6, aberration_list[6, 1]]
        tmp_dict['B4'] = [aberration_list[7, 0] * 1e-6, aberration_list[7, 1]]
        tmp_dict['D4'] = [aberration_list[8, 0] * 1e-6, aberration_list[8, 1]]
        tmp_dict['A4'] = [aberration_list[9, 0] * 1e-6, aberration_list[9, 1]]
        tmp_dict['C5'] = [aberration_list[10, 0] * 1e-9, aberration_list[10, 1]]
        tmp_dict['A5'] = [aberration_list[11, 0] * 1e-9, aberration_list[11, 1]]
        for key in tmp_dict:
            self[key] = tmp_dict[key]
        

    def calculateAberrationFunction(
            self,
            N: int, 
            wave_length: float,
            object_size: float,
    ) -> np.ndarray:
        """
        这个函数用于生成像差函数 \chi(u). 

        在此，自变量 u 是空间频率，单位是 m^-1，所得的值是相位。

        arguments:
            N: 像素数边长
            wave_length: 波长 (m)
            object_size: 物平面大小 (m)
            aberration_coeffi: 必须是 12 x 2 的矩阵，其中第一列中的各行是
                像差的绝对值大小，第二列的各行是像差的旋转角度。在这个矩阵中
                像差的单位按照文献
                S. Uhlemann, M. Haider Ultramicroscopy, 78(1999): 1-11
                所给出的约定。
        """
        dk = 1 / object_size 
        uxx = dk * np.linspace(-N/2, N/2-1, N)
        uyy = dk * np.linspace(-N/2, N/2-1, N)
        kx, ky = np.meshgrid(uxx, uyy)
        w = wave_length * (kx + 1j * ky)
        wi = wave_length * (kx - 1j * ky)
        chi = 2 * np.pi / wave_length * np.real(
            + 1/2 * w * wi * self['C1'] 
            + 1/2 * wi**2 * self['A1']
            + w**2 * wi * self['B2']
            + 1/3 * wi**3 * self['A2']
            + 1/4 * (w*wi)**2 * self['C3']
            + w**3 * wi * self['S3']
            + 1/4 * wi**4 * self['A3']
            + w**3 * wi**2 * self['B4']
            + w**4 * wi * self['D4']
            + 1/5 * wi**5 * self['A4']
            + 1/6 * (w*wi)**3 * self['C5']
            + 1/6 * wi**6 * self['A5']
        )
        return chi 
    # @property 
    # def complex_coefficients(self) -> dict:
    #     exp = np.exp 
    #     pi = np.pi 
    #     ad = self._mapping
    #     return {
    #         'C1': ad['C1'][0] * exp(1j * ad['C1'][1] * pi/180 * 1),
    #         'A1': ad['A1'][0] * exp(1j * ad['A1'][1] * pi/180 * 2),    
    #         'B2': ad['B2'][0] * exp(1j * ad['B2'][1] * pi/180 * 1),
    #         'A2': ad['A2'][0] * exp(1j * ad['A2'][1] * pi/180 * 3),
    #         'C3': ad['C3'][0] * exp(1j * ad['C3'][1] * pi/180 * 1),
    #         'S3': ad['S3'][0] * exp(1j * ad['S3'][1] * pi/180 * 2),
    #         'A3': ad['A3'][0] * exp(1j * ad['A3'][1] * pi/180 * 4),
    #         'B4': ad['B4'][0] * exp(1j * ad['B4'][1] * pi/180 * 1),
    #         'D4': ad['D4'][0] * exp(1j * ad['D4'][1] * pi/180 * 3),
    #         'A4': ad['A4'][0] * exp(1j * ad['A4'][1] * pi/180 * 5),
    #         'C5': ad['C5'][0] * exp(1j * ad['C5'][1] * pi/180 * 1),
    #         'A5': ad['A5'][0] * exp(1j * ad['A5'][1] * pi/180 * 6), 
    #     }



class OpticalSTEM(object):
    """
    STEM 光路参数的类。

    需要由用户输入的参数有：
        加速电压
        相机边长像素数
        扫描像素数
        会聚半角 alpha
        扫描步长
        明场衍射盘半径
        相机长度
        相机像素的物理尺寸 

    这其中，相机像素的物理尺寸、会聚半角、相机长度、明场衍射盘像素半径四者只有三个自由度。因此，我们在引导用户 calibration 的时候，会让用户确定像素的物理尺寸、会聚半角、明场衍射盘像素半径，来决定相机长度。在用户想要调整这些参数的时候，都会直接导致明场衍射盘像素半径的变化，而维持其他参数不变。然而，我们也提供用户直接调整明场衍射盘半径像素的选项，此时相机长度会随之改变，而固定住其他参数。

    确定了以上八个参数之后，即可接着导出以下参数，包括：
        衍射空间像素尺寸 dk
        实空间像素尺寸 dx
        电子波长
    等。基于此，即可完成定量化的重构与校正。

    """

    def __init__(
            self, 
            accelerate_voltage: float = None, 
            detector_shape: list[int] = None,
            scan_shape: list[int] = None,
            alpha: float = None,
            scan_step_size: float = None,
            bright_field_disk_radius: float = None,
            camera_length: float = None,
            detector_pixel_size: float = None,
            defocus: float = None,
            Cs: float = None,
    ):
        """
        OpticalSTEM 的光路参数。

        在计算 CTF 的过程中，scan_i 和 scan_j 不起作用；而 dp_i 和 dp_j 起作用。为了简化计算，强制使用正方形的衍射空间和实空间，此时其像素数 dp_N 选择为 max(dp_i, dp_j)。

        注意，bright_field_disk_radius, camera_length, detector_pixel_size, alpha 四者中，存在如下关系：

            bright_field_disk_radius * detector_pixel_size = alpha * camera_length 
        
        上面的式子表明，这四者其实只有三个自由度。对此，bright_field_disk_radius 作为可直接显示在图像上的部分，优先级最低，任何参数的变化都会调整该参数 (从而影响图像)。然而，用户有时候也会希望直接调整半径的像素数，所以当他们调整该参数时，我们选择一个最灵活而无害 (在实验中本来就经常变化，而且对 CTF 不起直接作用) 的参数，那就是 camera_length 来联动调整。换句话说：

            - detector_pixel_size 固定。其界面应当是和 camera_length 一起，作为二级界面给出的 (毕竟它不影响 CTF 计算)。当用户调整 detector_pixel_size 时，联动调整 bright_field_disk_radius 而保持其他参数不变。

            - alpha 放置在一级界面中，但其隐含逻辑也相对固定。当用户调整 alpha 时，联动调整 bright_field_disk_radius 而保持其他参数不变。

            - camera_length 放置在二级界面中，相对可变。当用户调整 camera_length 时，联动调整 bright_field_disk_radius 而保持其他参数不变。

            - bright_field_disk_radius 放置在一级界面中，其隐含逻辑经常变化。当用户调整 bright_field_disk_radius 时，联动调整 camera_length 而保持其他参数不变。

        arguments:
            accelerate_voltage: (float) 加速电压，单位 V

            detector_shape: (list[int]) 相机形状，(dp_i, dp_j)

            scan_shape: (list[int]) 扫描阵列形状，(scan_i, scan_j)

            alpha: (float) 会聚半角，单位为 rad

            scan_step_size: (float) 扫描步长，单位为 m

            bright_field_disk_radius: (float) 明场衍射盘半径像素数，可以不为整数

            camera_length: (float) 相机长度，单位为 m

            detector_pixel_size: (float) 相机像素的物理长度，单位为 m

            aberration_dict: (AberrationDict) 各项像差系数
        
            defocus: (float) 离焦量。小于零表示欠焦，大于零表示过焦，单位为 m

            Cs: (float) 球差系数。单位为 m
        """
        self._accelerate_voltage = 1.0
        self._dp_i = 32
        self._dp_j = 32
        self._scan_i = 32
        self._scan_j = 32
        self._alpha = 1.0
        self._scan_step_size = 1.0
        self._bright_field_disk_radius = 1.0
        self._camera_length = 1.0
        self._detector_pixel_size = 1.0
        self._aberration_dict = AberrationDict()
        self._probe = np.zeros((self.dp_N, self.dp_N))

        self.initializeParameters( 
            accelerate_voltage = accelerate_voltage, 
            detector_shape = detector_shape, 
            scan_shape = scan_shape,
            alpha = alpha,
            scan_step_size = scan_step_size,
            bright_field_disk_radius = bright_field_disk_radius,
            camera_length = camera_length,
            detector_pixel_size = detector_pixel_size,
            defocus = defocus,
            Cs = Cs,
        )

        

    @staticmethod
    def calcWaveLength(accelerate_voltage: float):
        """
        相对论性电子的物质波波长的计算。

        arguments:
            accelerate_voltage (float): 加速电压，单位 V
        
        returns:
            (float) 波长，单位 m
        """
        return h*c/np.sqrt(
            (e*accelerate_voltage + 2*m*c**2) * e * accelerate_voltage
        )

    def _update_optical_config(self, update_cache: bool = True):
        """
        当参数更新时，应当调用此函数以更新缓存的计算结果。

        arguments:
            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        if update_cache:
            self._probe = self.generateProbe()
        

    def _adjust_bright_field_disk_radius(self):
        """
        当会聚半角 alpha、相机像素的物理尺寸 camera_pixel_size 以及相机长度 camera_length 改变时，需要调用此函数，调整明场衍射盘的半径。
        """
        self._bright_field_disk_radius = self._alpha * self._camera_length / self._detector_pixel_size

    def _adjust_camera_length(self):
        """
        当明场衍射盘的半径像素数 bright_field_disk_radius 改变时，需要调用此函数，调整相机长度。
        """
        self._camera_length = self._bright_field_disk_radius * self._detector_pixel_size / self._alpha 

    def setAccelerateVoltage(self, voltage: float, update_cache: bool = True):
        """
        设置此光路的加速电压

        arguments:
            voltage (float): 加速电压, 单位 V

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        if not isinstance(voltage, (int, float)):
            raise TypeError("voltage must be a float")
        if voltage <= 0:
            raise ValueError("voltage must be positive")
        self._accelerate_voltage = voltage 
        self._update_optical_config(update_cache)
        
    def getAccelerateVoltage(self) -> float:
        """
        获取此光路的加速电压。

        returns:
            (float) 加速电压，单位 V
        """
        return self.accelerate_voltage

    def setAberrationDict(self, aberration_dict: AberrationDict, update_cache: bool = True):
        """
        设置此光路的各项像差

        arguments:
            aberration_dict: (AberrationDict)

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        if not isinstance(aberration_dict, AberrationDict):
            raise TypeError(f"aberration_dict must be {AberrationDict}")
        
        self._aberration_dict = aberration_dict
        self._update_optical_config(update_cache)

    def setAlpha(self, alpha: float, update_cache: bool = True):
        """
        设置会聚半角。

        改变这个参数的时候，会同时改变 bright_field_disk_radius 也就是明场衍射盘半径所占的像素数。

        Alias of setConvergentAngle()

        arguments:
            alpha: (float) 会聚半角 (由会聚镜光阑半径决定)。单位为 rad

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        return self.setConvergentAngle(alpha, update_cache)
    
    def getAlpha(self) -> float:
        """
        获取此光路的会聚半角。

        returns:
            (float) 会聚半角。单位 rad
        """
        return self._alpha

    def setDetectorN(self, dp_N: int, update_cache: bool = True):
        """
        设置相机的边长像素数。会把 dp_i 和 dp_j 都设置为该值

        arguments:
            dp_N: (int)

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        if not isinstance(dp_N, int):
            raise TypeError("dp_N must be int")
        elif dp_N <= 0:
            raise ValueError("dp_N must be positive")
        self._dp_i = dp_N 
        self._dp_j = dp_N
        self._update_optical_config(update_cache)

    def getDetectorN(self) -> int:
        """
        获取相机的边长像素数。当相机边长不一致(长方形)时，返回其中的最大值。

        returns:
            (int) 相机的边长像素数
        """
        return self.dp_N 

    def setScanN(self, scan_N: int, update_cache: bool = True):
        """
        设置扫描的边长像素数。会把 scan_i 和 scan_j 都设置为该值

        arguments:
            scan_N: (int)

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        if not isinstance(scan_N, int):
            raise TypeError("scan_N must be int")
        elif scan_N <= 0:
            raise ValueError("scan_N must be positive")
        self._scan_i = scan_N 
        self._scan_j = scan_N
        self._update_optical_config(update_cache)

    def getScanN(self) -> int:
        """
        获取扫描的边长像素数。当扫描变长不一致 (长方形的阵列) 时，返回其中的最大值。

        returns:
            (int) 扫描的边长像素数
        """
        return self.scan_N

    def setDetectorShape(self, shape: list[int], update_cache: bool = True):
        """
        设置相机/衍射图样的边长像素数。

        arguments:
            shape: (list[int]) 长度必须为 2, 分别为 dp_i 和 dp_j

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        dp_i, dp_j = shape 
        if not isinstance(shape, Iterable):
            raise TypeError("shape must be a list of integers with length 2")
        if len(shape) != 2:
            raise ValueError("shape must be a list of integers with length 2")
        if not isinstance(dp_i, int):
            raise TypeError("shape must be a list of integers with length 2")
        if not isinstance(dp_j, int):
            raise TypeError("shape must be a list of integers with length 2")
        self._dp_i = dp_i
        self._dp_j = dp_j 
        self._update_optical_config(update_cache) 

    def getDetectorShape(self) -> tuple[int]:
        """
        获取相机的边长像素数。

        returns:
            (tuple[int]) 返回两个数，分别是 dp_i 和 dp_j
        """
        return self.detector_shape

    def setScanShape(self, shape: list[int], update_cache: bool = True):
        """
        设置扫描的边长像素数。

        arguments:
            shape: (list[int]) 长度必须为 2, 分别为 scan_i 和 scan_j 

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        scan_i, scan_j = shape 
        if not isinstance(shape, Iterable):
            raise TypeError("shape must be a list of integers with length 2")
        if len(shape) != 2:
            raise ValueError("shape must be a list of integers with length 2")
        if not isinstance(scan_i, int):
            raise TypeError("shape must be a list of integers with length 2")
        if not isinstance(scan_j, int):
            raise TypeError("shape must be a list of integers with length 2")
        self._scan_i = scan_i 
        self._scan_j = scan_j 
        self._update_optical_config(update_cache)

    def getScanShape(self) -> tuple[int]:
        """
        获取扫描的边长像素数。

        returns:
            (tuple[int]) 返回两个数，分别是 scan_i 和 scan_j
        """
        return self.scan_shape
        
    def setConvergentAngle(self, alpha: float, update_cache: bool = True):
        """
        设置会聚半角。

        改变这个参数的时候，会同时改变 bright_field_disk_radius 也就是明场衍射盘半径所占的像素数。

        Alias of setAlpha().

        arguments:
            alpha: (float) 会聚半角 (由会聚镜光阑半径决定)。单位为 rad

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        if not isinstance(alpha, (float, int)):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        self._alpha = alpha 
        self._adjust_bright_field_disk_radius()
        self._update_optical_config(update_cache)

    def getConvergentAngle(self) -> float:
        """
        获取会聚半角。

        returns:
            (float) 会聚半角，单位 rad
        """
        return self._alpha

    def setDetectorPixelSize(self, detector_pixel_size: float, update_cache: bool = True):
        """
        设置相机像素在物理上的尺寸。

        该参数是相机固有的性质，无法在实验中进行调整。在计算时，如果用户改变了这项参数，会同时改变 bright_field_disk_radius 也就是明场衍射盘半径所占的像素数。

        arguments:
            pixel_size: (float) 相机像素在物理上的尺寸。单位为 m

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        if not isinstance(detector_pixel_size, (float, int)):
            raise TypeError("detector_pixel_size msut be a float")
        if detector_pixel_size <= 0:
            raise ValueError("detector_pixel_size must be positive")
        self._detector_pixel_size = detector_pixel_size
        self._adjust_bright_field_disk_radius()
        self._update_optical_config(update_cache)

    def getDetectorPixelSize(self) -> float:
        """
        获取相机像素在物理上的尺寸。

        returns:
            (float) 相机像素在物理上的尺寸，单位为 m
        """
        return self._detector_pixel_size

    def setCameraLength(self, camera_length: float, update_cache: bool = True):
        """
        设置相机长度。

        该参数可从电镜中直接读取，但往往并不准确，需要标定。在计算时，如果用户改变了这项参数，会同时改变 bright_field_disk_radius 也就是明场衍射盘半径所占的像素数。

        arguments:
            camera_length: (float) 相机长度

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        if not isinstance(camera_length, (float, int)):
            raise TypeError("camera_length must be a float")
        if camera_length <= 0:
            raise ValueError("camera_length must be positive")
        self._camera_length = camera_length
        self._adjust_bright_field_disk_radius()
        self._update_optical_config(update_cache)

    def getCameraLength(self) -> float:
        """
        获取相机长度。

        returns:
            (float) 相机长度。单位 m
        """
        return self._camera_length

    def setBrightFieldDiskRadius(self, bright_field_disk_radius: float, update_cache: bool = True):
        """
        设置明场衍射盘的半径 (像素数)。实际上也会修改会聚镜光阑的半径。

        该参数可以直接从衍射图样中测量出来，也可以随意调整。在计算时，如果用户想要改变这项参数，我们视为用户通过改变相机长度来实现该目的。因此，在更改这项参数时，会同步改变相机长度。

        arguments:
            bright_field_disk_radius: (float) 明场衍射盘的半径 (像素数)。实际上，决定的是会聚镜光阑尺寸。

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        if not isinstance(bright_field_disk_radius, (float, int)):
            raise TypeError("bright_field_disk_radius must be a float")
        if bright_field_disk_radius <= 0:
            raise ValueError("bright_field_disk_radius must be postiive")
        self._bright_field_disk_radius = bright_field_disk_radius
        self._adjust_camera_length()
        self._update_optical_config(update_cache)

    def getBrightFieldDiskRadius(self) -> float:
        """
        获取明场衍射盘的半径 (像素数)。实际上就是会聚镜光阑的半径。

        returns:
            (float) 明场衍射盘的半径 (像素数), 可以为小数
        """
        return self._bright_field_disk_radius

    def setConvergentApertureRadius(self, radius: float, update_cache: bool = True):
        """
        设置会聚镜光阑的半径 (像素数)。实际上也会修改明场衍射盘的半径。

        arguments:
            radius: (float) 会聚镜光阑半径 (像素数)，可以为浮点数。实际上就是明场衍射盘的半径。

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        self.setBrightFieldDiskRadius(radius, update_cache)

    def getConvergentApertureRadius(self) -> float:
        """
        获取会聚镜光阑的半径 (像素数)。实际上就是明场衍射盘的半径。

        returns:
            (float) 会聚镜光阑的半径 (像素数)，可以为小数。
        """
        return self._bright_field_disk_radius

    def setScanStepSize(self, scan_step_size: float, update_cache: bool = True):
        """
        设置扫描步长 (扫描坐标系中每个格子的边长)。

        arguments:
            scan_step_size: (float) 扫描步长，单位 m
        """
        if not isinstance(scan_step_size, (float, int)):
            raise TypeError("scan_step_size must be a float")
        if scan_step_size <= 0:
            raise ValueError("scan_step_size must be positive")
        self._scan_step_size = scan_step_size 
        self._update_optical_config(update_cache)

    def getScanStepSize(self) -> float:
        """
        获取扫描步长 (扫描坐标系中每个格子的边长)。

        arguments:
            scan_step_size: (float) 扫描步长，单位 m
        """
        return self._scan_step_size

    def getDiffractionSpacePixelSize(self) -> float:
        """
        获取衍射空间的格子长度 du，其由
        du = alpha / wave_length / bright_field_disk_radius 决定。

        Alias 是 getDu()，单位为 m^{-1}

        returns:
            (float) 衍射空间的格子长度
        """
        return self.alpha / self.wave_length / self.bright_field_disk_radius 
    
    def getDu(self) -> float:
        """
        获取频域空间的格子长度 du，其由
        du = alpha / wave_length / bright_field_disk_radius 
        决定。

        Alias 是 getDiffractionSpacePixelSize()，单位为 m^{-1}

        returns:
            (float) 衍射空间的格子长度
        """
        return self.getDiffractionSpacePixelSize()

    def getRealSpacePixelSize(self) -> float:
        """
        获取实空间的格子长度 dx，其由
        dx = wave_length * bright_field_disk_radius / alpha / dp_N 
        决定。
        
        注意，它的意义和扫描步长不同。它指的是在某个扫描点上，对 probe 的分布进行采样的格子间隔。即使不进行扫描，dx 也是有意义的，但扫描步长此时就没有意义了。

        Alias 是 getDx()，单位为 m

        returns:
            (float) 实空间的格子长度。
        """
        return self.wave_length * self.bright_field_disk_radius / self.alpha / self.dp_N 
    
    def getDx(self) -> float:
        """
        获取实空间的格子长度 dx，其由
        dx = wave_length * bright_field_disk_radius / alpha / dp_N 
        决定。
        
        注意，它的意义和扫描步长不同。它指的是在某个扫描点上，对 probe 的分布进行采样的格子间隔。即使不进行扫描，dx 也是有意义的，但扫描步长此时就没有意义了。

        Alias 是 getRealSpacePixelSize()，单位为 m

        returns:
            (float) 实空间的格子长度。
        """
        return self.getRealSpacePixelSize()
    
    def getDiffractionSpaceSize(self) -> float:
        """
        衍射空间 (倒空间/频域空间) 的尺寸。单位为 m^{-1}。

        returns:
            (float) 衍射空间的边长
        """
        return self.alpha * self.dp_N / self.wave_length / self.bright_field_disk_radius 
    
    def getRealSpaceSize(self) -> float:
        """
        实空间的尺寸。单位为 m。

        这里的实空间，指的是单个扫描位置所对应的范围，与扫描过程无关。对于扫描范围，参见 getScanSize()。
        """
        return self.wave_length * self.bright_field_disk_radius / self.alpha 
    
    def getScanSize(self) -> float:
        """
        扫描范围的尺寸。单位为 m。

        这里的扫描范围，指的是扫描步长乘以扫描步数。它与 getRealSpaceSize() 有所区别。
        """
        return self.scan_step_size * self.scan_N 

    @property
    def scan_shape(self) -> tuple[int]:
        return self._scan_i, self._scan_j 
    
    @scan_shape.setter 
    def scan_shape(self, shape: list[int]):
        self.setScanShape(shape)
    
    @property
    def detector_shape(self) -> tuple[int]:
        return self._dp_i, self._dp_j 
    
    @detector_shape.setter 
    def detector_shape(self, shape: list[int]):
        self.setDetectorShape(shape)

    @property
    def scan_N(self) -> int:
        return max((self._scan_i, self._scan_j))
    
    @scan_N.setter 
    def scan_N(self, N: int):
        self.setScanN(N)
    
    @property 
    def dp_N(self) -> int:
        return max((self._dp_i, self._dp_j))
    
    @dp_N.setter 
    def dp_N(self, N: int):
        self.setDetectorN(N)

    @property 
    def wave_length(self) -> float:
        return self.calcWaveLength(self._accelerate_voltage)
    
    @property
    def accelerate_voltage(self) -> float:
        return self._accelerate_voltage
    
    @accelerate_voltage.setter
    def accelerate_voltage(self, voltage: float):
        self.setAccelerateVoltage(voltage)

    @property 
    def alpha(self) -> float:
        return self._alpha 
    
    @alpha.setter 
    def alpha(self, angle: float):
        self.setConvergentAngle(angle)

    @property 
    def convergent_angle(self) -> float:
        return self._alpha 
    
    @convergent_angle.setter
    def convergent_angle(self, angle: float):
        self.setConvergentAngle(angle)

    @property 
    def detector_pixel_size(self) -> float:
        return self._detector_pixel_size
    
    @detector_pixel_size.setter 
    def detector_pixel_size(self, pixel_size: float):
        self.setDetectorPixelSize(pixel_size)
    
    @property
    def camera_length(self) -> float:
        return self._camera_length 
    
    @camera_length.setter 
    def camera_length(self, cl: float):
        self.setCameraLength(cl)

    @property
    def bright_field_disk_radius(self) -> float:
        return self._bright_field_disk_radius

    @bright_field_disk_radius.setter 
    def bright_field_disk_radius(self, radius: float):
        self.setBrightFieldDiskRadius(radius)

    @property
    def convergent_aperture_radius(self) -> float:
        return self._bright_field_disk_radius
    
    @convergent_aperture_radius.setter 
    def convergent_aperture_radius(self, radius: float):
        self.setConvergentApertureRadius(radius)

    @property
    def scan_step_size(self) -> float:
        return self._scan_step_size 

    @scan_step_size.setter 
    def scan_step_size(self, value: float):
        self.setScanStepSize(value)

    @property
    def scan_size(self) -> float:
        return self.getScanSize()

    @property
    def du(self) -> float:
        return self.getDiffractionSpacePixelSize()
    
    @property
    def dx(self) -> float:
        return self.getRealSpacePixelSize()
    
    @property
    def diffraction_space_size(self) -> float:
        return self.getDiffractionSpaceSize()
    
    @property
    def real_space_size(self) -> float:
        return self.getRealSpaceSize()

    def setAberrationFromList(self, aberration_list: list, update_cache: bool = True):
        """
        从 list 中设置此光路的各项像差。该 list 必须是 12 x 2 的矩阵，其中第一列表示的是各项值，第二列表示的是各项的旋转角度，单位是 deg。这个函数用于兼容性，提供给现有代码一个接口。

        arguments:
            aberration_list: (list) 必须是 12 x 2 的矩阵。

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        self._aberration_dict.setAberrationDictFromList(aberration_list)
        self._update_optical_config(update_cache)
    
    def setAberrationCoefficient(self, key: str, value: float|complex|list[float], update_cache: bool = True):
        """
        设置某项像差系数。

        key 参数必须是以下之一：
            'C1'    # defocus
            'A1'    # two-fold astigmatism
            'B2'    # axial coma
            'A2'    # three-fold astigmatism
            'C3'    # spherical aberration
            'S3'    # star aberration
            'A3'    # four-fold astigmatism
            'B4'    # axial coma
            'D4'    # three lobe aberration
            'A4'    # five-fold astigmatism
            'C5'    # spherical aberration
            'A5'    # sixfold astigmatism

        value 必须为 float, complex 或者长度为 2 的 Interable。
        
        如果 value 是 float, 则
            - 它表示国际单位制下的各项像差系数，角度默认为 0
        如果 value 是长度为 2 的 Iterable，则
            - 第一个值表示国际单位制下的各项像差系数
            - 第二个值表示这项像差的旋转的角度，单位为 deg (°)
        如果 value 为 complex，则
            - 其将直接应用为像差系数，模长单位为国际单位，而不作进一步处理

        arguments:
            key: (str) 

            value: (float|complex|list[float])

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        self._aberration_dict[key] = value 
        self._update_optical_config(update_cache)

    def setDefocus(self, defocus: float, update_cache: bool = True):
        """
        设置离焦量 defocus。
        
        正值表示过焦，即会聚镜的后焦面 (probe 会聚点) 处于样品上方
        负值表示欠焦，即会聚镜的后焦面 (probe 会聚点) 处于样品下方

        arguments:
            defocus: (float) 离焦量

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        self._aberration_dict['C1'] = (defocus, 0)
        self._update_optical_config(update_cache)

    @property
    def defocus(self) -> float:
        return np.real(self._aberration_dict['C1'])
    
    @defocus.setter 
    def defocus(self, value: float):
        return self.setDefocus(value)

    def setCs(self, Cs: float, update_cache: bool = True):
        """
        设置 (三级) 球差系数。

        对于电子显微镜而言，磁透镜的球差系数只能取到正值。但球差校正电镜似无此限制。

        arguments:
            Cs: (float) 三级球差系数

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        self._aberration_dict['C3'] = (Cs, 0) 
        self._update_optical_config(update_cache)
    
    @property
    def Cs(self) -> float:
        return np.real(self._aberration_dict['C3'])
    
    @Cs.setter
    def Cs(self, value: float):
        self.setCs(value)
    
    def getAberrationCoefficient(self, key: str) -> tuple[float]:
        """
        取得某个像差系数。返回该系数对应的大小 (模长) 以及旋转角度。

        key 参数必须是以下之一：
            'C1'    # defocus
            'A1'    # two-fold astigmatism
            'B2'    # axial coma
            'A2'    # three-fold astigmatism
            'C3'    # spherical aberration
            'S3'    # star aberration
            'A3'    # four-fold astigmatism
            'B4'    # axial coma
            'D4'    # three lobe aberration
            'A4'    # five-fold astigmatism
            'C5'    # spherical aberration
            'A5'    # sixfold astigmatism

        arguments:
            key: (str) 要取得的像差系数的项

        returns:
            (tuple[float]) 返回两个数字，第一个数字是像差系数的模长，第二个数字是像差项对应的旋转角。注意，这里的旋转角不一定等于复像差系数的幅角。
        """
        coefficient_module = self._aberration_dict.getModule(key)
        coefficient_angle = self._aberration_dict.getAngle(key)
        return (coefficient_module, coefficient_angle)
    
    def getComplexAberrationCoefficient(self, key: str) -> complex:
        """
        取得某个复像差系数。

        key 参数必须是以下之一：
            'C1'    # defocus
            'A1'    # two-fold astigmatism
            'B2'    # axial coma
            'A2'    # three-fold astigmatism
            'C3'    # spherical aberration
            'S3'    # star aberration
            'A3'    # four-fold astigmatism
            'B4'    # axial coma
            'D4'    # three lobe aberration
            'A4'    # five-fold astigmatism
            'C5'    # spherical aberration
            'A5'    # sixfold astigmatism

        arguments:
            key: (str) 要取得像差系数的项
        """
        return self._aberration_dict[key]

    def setAberrationCoefficientModule(self, key: str, value: float, update_cache: bool = True):
        """
        设置某项像差系数的模长。

        key 参数必须是以下之一：
            'C1'    # defocus
            'A1'    # two-fold astigmatism
            'B2'    # axial coma
            'A2'    # three-fold astigmatism
            'C3'    # spherical aberration
            'S3'    # star aberration
            'A3'    # four-fold astigmatism
            'B4'    # axial coma
            'D4'    # three lobe aberration
            'A4'    # five-fold astigmatism
            'C5'    # spherical aberration
            'A5'    # sixfold astigmatism

        arguments:
            key: (str) 要取得像差系数的项

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        self._aberration_dict.setModule(key, value)
        self._update_optical_config(update_cache)
    
    def setAberrationCoefficientAngle(self, key: str, value: float, update_cache: bool = True):
        """
        设置某项像差系数的旋转角度，单位为 deg。

        注意，这里的旋转角度不等于复像差系数的幅角。

        key 参数必须是以下之一：
            'C1'    # defocus
            'A1'    # two-fold astigmatism
            'B2'    # axial coma
            'A2'    # three-fold astigmatism
            'C3'    # spherical aberration
            'S3'    # star aberration
            'A3'    # four-fold astigmatism
            'B4'    # axial coma
            'D4'    # three lobe aberration
            'A4'    # five-fold astigmatism
            'C5'    # spherical aberration
            'A5'    # sixfold astigmatism

        arguments:
            key: (str) 要取得像差系数的项

            update_cache: (bool) 是否要重新计算缓存的图像。
        """
        self._aberration_dict.setAngle(key, value)
        self._update_optical_config(update_cache)

    def initializeParameters(self, 
            accelerate_voltage: float = None, 
            detector_shape: list[int] = None,
            scan_shape: list[int] = None,
            scan_step_size: float = None,
            bright_field_disk_radius: float = None,
            camera_length: float = None,
            alpha: float = None,
            detector_pixel_size: float = None,
            defocus: float = None,
            Cs: float = None,
    ):
        """
        一次性更新大量参数。将在更新完所有参数之后再更新缓存。

        bright_field_disk_radius, camera_length, detector_pixel_size 和 alpha 四个参数只有三个自由度。如果同时传入了这四个参数，则 bright_field_disk_radius 将由其它三个参数决定。

        arguments:
            accelerate_voltage: (float) 加速电压，单位 V

            detector_shape: (list[int]) 相机形状，(dp_i, dp_j)

            scan_shape: (list[int]) 扫描阵列形状，(scan_i, scan_j)

            alpha: (float) 会聚半角，单位为 rad

            scan_step_size: (float) 扫描步长，单位为 m

            bright_field_disk_radius: (float) 明场衍射盘半径像素数，可以不为整数

            camera_length: (float) 相机长度，单位为 m

            detector_pixel_size: (float) 相机像素的物理长度，单位为 m

            aberration_dict: (AberrationDict) 各项像差系数
        
            defocus: (float) 离焦量。小于零表示欠焦，大于零表示过焦，单位为 m

            Cs: (float) 球差系数。单位为 m
        """
        if accelerate_voltage is not None:
            self.setAccelerateVoltage(accelerate_voltage, False)
        if detector_shape is not None:
            self.setDetectorShape(detector_shape, False)
        if scan_shape is not None:
            self.setScanShape(scan_shape, False)
        if scan_step_size is not None:
            self.setScanStepSize(scan_step_size, False)
        if defocus is not None:
            self.setDefocus(defocus, False)
        if Cs is not None:
            self.setCs(Cs, False)
        
        self._update_diffraction_params(
            detector_pixel_size = detector_pixel_size,
            alpha = alpha,
            camera_length = camera_length,
            bright_field_disk_radius = bright_field_disk_radius,
        )
        
        self._update_optical_config()

    def _update_diffraction_params(
            self, 
            detector_pixel_size = None, 
            alpha = None, 
            camera_length = None, 
            bright_field_disk_radius = None
        ):
        """
        由于这四个参数满足一个约束
        alpha * camera_length * bright_field_disk_radius**(-1) * detector_pixel_size**(-1) == 1

        我们设置优先级为
        detector_pixel_size > alpha > camera_length > bright_field_disk_radius

        如果什么参数都不传递，就什么都不做。

        如果传递的参数大于零个、小于四个，那么除了会修改传递的参数之外，还会修改除传递的参数以外最低优先级的那个参数，以满足约束条件。

        如果传递的参数等于四个，那么无视传递的最低优先级的参数 (bright_field_disk_radius)，而将其交由前三个参数以及约束来决定。
        """
        _param_dict = {     # 传入的参数字典
            'detector_pixel_size': detector_pixel_size,
            'alpha': alpha,
            'camera_length': camera_length,
            'bright_field_disk_radius': bright_field_disk_radius,
        }

        _ordered_keys = [   # 参数优先级的顺序
            'detector_pixel_size', 
            'alpha', 
            'camera_length', 
            'bright_field_disk_radius'
        ]

        _current_dict = {   # 现有的参数字典
            'detector_pixel_size': self.detector_pixel_size,
            'alpha': self.alpha,
            'camera_length': self.camera_length,
            'bright_field_disk_radius': self.bright_field_disk_radius
        }

        _updated_dict = {   # 更新后的参数字典
            'detector_pixel_size': None,
            'alpha': None,
            'camera_length': None,
            'bright_field_disk_radius': None,
        }

        _prod_power = {     # 这四个参数所满足的约束为，其各幂次的乘积等于 1
            'detector_pixel_size': -1,
            'bright_field_disk_radius': -1,
            'camera_length': 1,
            'alpha': 1,
        }

        for key in _param_dict:     # 检查传入的参数
            if _param_dict[key] is not None:
                if not isinstance(_param_dict[key], (float, int)):
                    raise TypeError(f"{key} must be a float")
                if _param_dict[key] <= 0:
                    raise ValueError(f"{key} must be positive")
            

        _count_none = sum(1 for k in _ordered_keys if _param_dict[k] is None)

        if _count_none == 4:    # 如果什么参数都不传递，就什么都不做。
            return
        if _count_none == 0:    # 如果传递了四个参数，那么无视最低优先级的参数，即 
                                # bright_field_disk_radius
            _param_dict['bright_field_disk_radius'] = None 
            _count_none += 1
        
        # 找出优先级最低的 None 参数，它将由传入的参数与现有的参数来决定。
        param_to_be_determined = None 
        for key in _ordered_keys[::-1]:
            if _param_dict[key] is None:
                param_to_be_determined = key 
                break 

        for key in _updated_dict:   # 除最后要决定的参数外，其他参数已定下
            if key == param_to_be_determined:
                _updated_dict[key] = None
            elif _param_dict[key] is None:
                _updated_dict[key] = _current_dict[key]
            else:
                _updated_dict[key] = _param_dict[key]

        _prod_num = 1               # 计算最后要决定的参数的值
        for key in _updated_dict:
            if key == param_to_be_determined:
                _prod_num *= 1
            else:
                _prod_num = _prod_num * (_updated_dict[key] ** _prod_power[key])
        _updated_dict[param_to_be_determined] = 1 / _prod_num

        self._alpha = _updated_dict['alpha']    # 将这些参数都保存下来
        self._detector_pixel_size = detector_pixel_size
        self._camera_length = _updated_dict['camera_length']
        self._bright_field_disk_radius = _updated_dict['bright_field_disk_radius']

    def generateConvergentAperture(self) -> np.ndarray:
        """
        绘制会聚镜光阑的分布 (尺寸是基于衍射空间的)。

        它也是真空下明场衍射斑的分布。

        returns:
            (np.ndarray) 返回会聚镜光阑的矩阵，为 dp_N x dp_N。
        """
        convergent_aperture = np.zeros((self.dp_N, self.dp_N))
        ui, uj = self.generateDiffractionMeshgrid()
        convergent_aperture[np.sqrt(ui**2+uj**2) <= self.alpha/self.wave_length] = 1
        return convergent_aperture

    def generateVirtualAnnularDetector(self, beta_min: float, beta_max: float) -> np.ndarray:
        """
        绘制虚拟环形探头的分布 (尺寸是基于衍射空间的)。

        arguments:
            beta_min: (float) 环形探头的收集角内径。单位: rad

            beta_max: (float) 环形探头的收集角外径。单位: rad
        """
        if not isinstance(beta_min, (float,int)):
            raise TypeError("beta_min must be a float")
        if not isinstance(beta_max, (float,int)):
            raise TypeError("beta_max must be a float")
        virtual_detector = np.zeros((self.dp_N, self.dp_N))
        ui, uj = self.generateDiffractionMeshgrid()
        virtual_detector[np.sqrt(ui**2+uj**2) <= beta_max/self.wave_length] = 1
        virtual_detector[np.sqrt(ui**2+uj**2) < beta_min/self.wave_length] = 0
        return virtual_detector 
    
    def generateRealSpaceMaskCircle(self, rho: float) -> np.ndarray:
        """
        绘制在实空间下的圆形 Mask，半径为 rho。在 rho 以外的值为零，rho 以内的值为 1。

        arguments:
            rho: (float) Mask 的半径。单位 m。
        """
        if not isinstance(rho, (float, int)):
            raise TypeError("rho must be a float")
        mask = np.zeros((self.dp_N, self.dp_N))
        ri, rj = self.generateRealSpaceMeshgrid()
        mask[np.sqrt(ri**2 + rj**2) <= rho] = 1
        return mask 

    def generateDiffractionMeshgrid(self) -> tuple[np.ndarray]:
        """
        建立衍射空间的 meshgird。

        returns:
            ui, uj 两个 dp_N x dp_N 的矩阵
        """
        uii = self.du * np.linspace(-self.dp_N/2, self.dp_N/2 - 1, self.dp_N)
        ujj = self.du * np.linspace(-self.dp_N/2, self.dp_N/2 - 1, self.dp_N)
        ui, uj = np.meshgrid(uii, ujj, indexing = 'ij')
        return ui, uj

    def generateRealSpaceMeshgrid(self) -> tuple[np.ndarray]:
        """
        建立实空间的 meshgrid。注意这里的实空间是单个扫描位置的范围，用以描述 probe，与扫描过程无关。

        returns:
            ri, rj 两个 dp_N x dp_N 的矩阵
        """
        rii = self.dx * np.linspace(-self.dp_N/2, self.dp_N/2 - 1, self.dp_N)
        rjj = self.dx * np.linspace(-self.dp_N/2, self.dp_N/2 - 1, self.dp_N)
        ri, rj = np.meshgrid(rii, rjj, indexing = 'ij')
        return ri, rj 
    
    def generateScanMeshgrid(self) -> tuple[np.ndarray]:
        """
        建立扫描位置的 meshgrid。

        returns:
            scan_ri, scan_rj 两个 scan_N x scan_N 的矩阵
        """
        scan_rii = self.dx * np.linspace(-self.scan_N/2, self.scan_N/2 - 1, self.scan_N)
        scan_rjj = self.dx * np.linspace(-self.scan_N/2, self.scan_N/2 - 1, self.scan_N)
        scan_rii, scan_rjj = np.meshgrid(scan_rii, scan_rjj, indexing = 'ij')
        return scan_rii, scan_rjj 
    
    @staticmethod
    def fft2(matrix: np.ndarray, pixel_size: float) -> np.ndarray:
        """
        以 (N//2, N//2) 为中心的 FFT2。它对应的连续空间傅里叶变换为
        F[f(r)](u) = ∫∫ f(r) exp(-2πiu·r) d²r

        相比于离散傅里叶变换，上述连续空间傅里叶变换的离散采样应当为
        F[f(r)](u) = DFT[f(n)] · (dr)² 

        其中 dr 是 L/N, L 是 object size, n = -N/2, ..., N/2 - 1

        arguments:
            matrix: (np.ndarray) 需要作二维傅里叶变换的矩阵，应为 N * N

            pixel_size: (float) 作二维傅里叶变换的输入矩阵的格子边长。这里的格子边长可以是实空间的格子边长，也可以是倒空间的。只需要遵从同样的单位制即可。
        """
        return np.fft.fftshift(np.fft.fft2(
            np.fft.fftshift(matrix), 
            norm = 'backward',
        )) * pixel_size**2

    @staticmethod 
    def ifft2(matrix: np.ndarray, pixel_size: float) -> np.ndarray:
        """
        以 (N//2, N//2) 为中心的 iFFT2。它对应的连续空间傅里叶逆变换为
        F^{-1}[g(u)](r) = ∫∫ g(u) exp(2πiu·r) d²u

        相比于离散傅里叶逆变换，上述连续空间傅里叶逆变换的离散采样应当为
        F^{-1}[g(u)](r) = DFT[g(k)] · (du)²

        其中 du 是格子边长, k = -N/2, ..., N/2 - 1

        arguments:
            matrix: (np.ndarray) 需要作二维傅里叶逆变换的矩阵，应为 N * N

            pixel_size: (float) 作二维傅里叶逆变换的输入矩阵的格子边长。这里的格子边长可以是实空间的格子边长，也可以是倒空间的。只需要遵从同样的单位制即可。
        """

        return np.fft.ifftshift(np.fft.ifft2(
            np.fft.ifftshift(matrix),
            norm = 'forward',
        )) * pixel_size**2
    
    def generateAberrationFunction(self) -> np.ndarray:
        """
        绘制透镜的像差函数 χ(u)。

        在此，自变量 u 是空间频率，单位是 m^-1，所得的值是无量纲的相位。

        returns:
            (np.ndarray) 像差函数在衍射空间的分布
        """
        ui, uj = self.generateDiffractionMeshgrid()
        w = self.wave_length * (ui + 1j * uj)
        wi = self.wave_length * (ui - 1j * uj)
        chi = 2 * np.pi / self.wave_length * np.real(
            + 1/2 * w * wi * self._aberration_dict['C1'] 
            + 1/2 * wi**2 * self._aberration_dict['A1']
            + w**2 * wi * self._aberration_dict['B2']
            + 1/3 * wi**3 * self._aberration_dict['A2']
            + 1/4 * (w*wi)**2 * self._aberration_dict['C3']
            + w**3 * wi * self._aberration_dict['S3']
            + 1/4 * wi**4 * self._aberration_dict['A3']
            + w**3 * wi**2 * self._aberration_dict['B4']
            + w**4 * wi * self._aberration_dict['D4']
            + 1/5 * wi**5 * self._aberration_dict['A4']
            + 1/6 * (w*wi)**3 * self._aberration_dict['C5']
            + 1/6 * wi**6 * self._aberration_dict['A5']
        )
        return chi 
    
    def generateConvergentBeam(self) -> np.ndarray:
        """
        在衍射空间中，绘制电子波在会聚镜光阑处的分布。

        注意，这里的分布是已经经过归一化的。归一化的方法是，probe 在全实空间的模平方的积分等于 1。

        returns:
            (np.ndarray) 电子波在会聚镜光阑处的分布
        """
        probe = self.generateProbe()
        beam = self.ifft2(probe, self.dx)
        return beam

    def generateProbe(self) -> np.ndarray:
        """
        绘制照射在样品上的 probe，也即是入射波。注意，

        注意，这里的分布是已经经过归一化了的。归一化的方法是，probe 在全实空间的模平方的积分等于 1。

        returns:
            (np.ndarray) 入射波在实空间的分布
        """
        aperture = self.generateConvergentAperture()
        chi = self.generateAberrationFunction()
        beam = aperture * np.exp(-1j * chi)
        probe = self.fft2(beam, self.du)
        norm = np.sqrt(np.sum(probe * np.conj(probe)) * self.dx**2)
        normalized_probe = probe / norm
        return normalized_probe
        
    def getProbe(self, update_cache: bool = True) -> np.ndarray:
        """
        获取照射在样品上的 probe，也即是入射波。它是 Virtual Image 和 CoM 的 CTF 计算的基础。

        注意，这里的 probe 是已经经过归一化了的。归一化的方法是，probe 在全实空间的模平方的积分等于 1。

        arguments:
            update_cache: (bool) 是否重新计算 probe。如果是，则会根据现有参数重新计算 probe。如果在相邻两次计算中并未更改任何决定 probe 的光学参数，那么可以令 update = False 来直接返回上一次计算的 probe。这样能加快 CTF 的计算速度。

        returns:
            (np.ndarray) 入射波在实空间的分布
        """
        if update_cache:
            self._probe = self.generateProbe()
        return self._probe
    
    def generateProbePositions(self, scan_angle) -> np.ndarray:
        """
        Generate probe positions based on the given scan rotational angle.

        Args:
            scan_angle (float): The scan angle in degrees.

        Returns:
            numpy.ndarray: A 3-dimensional numpy array representing the probe positions.
                           The shape of the array is (scan_i, scan_j, 2), where scan_i
                           and scan_j are the dimensions of the scan and 2 represents
                           the x and y coordinates of each probe position.
        """
        dx = self.dx
        scan_step_size = self.scan_step_size
        _scan_i, _scan_j = self.scan_shape
        probe_positions = np.zeros((_scan_i, _scan_j, 2))
        for i in range(_scan_i):
            for j in range(_scan_j):
                probe_positions[i, j, 0] = (i+1) * scan_step_size / dx * np.cos(scan_angle) - (j+1) * scan_step_size / dx * np.sin(scan_angle)
                probe_positions[i, j, 1] = (i+1) * scan_step_size / dx * np.sin(scan_angle) + (j+1) * scan_step_size / dx * np.cos(scan_angle)
        return probe_positions
    
    def generatePaddedProbePositions(self, scan_angle, padding: int = 50) -> np.ndarray:
        """
        Generate probe positions based on the given scan rotational angle with padding.

        Args:
            scan_angle (float): The scan angle in degrees.

            padding (int): The padding size.

        Returns:
            numpy.ndarray: A 3-dimensional numpy array representing the probe positions.
                           The shape of the array is (scan_i, scan_j, 2), where scan_i
                           and scan_j are the dimensions of the scan and 2 represents
                           the x and y coordinates of each probe position.
        """
        probe_positions = self.generateProbePositions(scan_angle)
        padded_probe_positions = np.empty_like(probe_positions)
        padded_probe_positions[:, :, 0] = probe_positions[:, :, 0] - np.floor(np.min(probe_positions[:, :, 0])) + padding
        padded_probe_positions[:, :, 1] = probe_positions[:, :, 1] - np.floor(np.min(probe_positions[:, :, 1])) + padding
        padded_probe_positions = np.round(padded_probe_positions).astype(int)

        return padded_probe_positions
    
    def generatePaddedObject(self, scan_angle, padding: int = 50) -> np.ndarray:
        """
        Generate padded object based on the given scan rotational angle.

        Args:
            scan_angle (float): The scan angle in degrees.

            padding (int): The padding size.

        Returns:
            numpy.ndarray: A 2-dimensional numpy array representing the padded object.
        """
        padded_probe_positions = self.generatePaddedProbePositions(scan_angle, padding)
        padded_object_shape = (
            np.max(padded_probe_positions[:, :, 0]) - np.min(padded_probe_positions[:, :, 0]) + self._dp_i + 2 * padding,
            np.max(padded_probe_positions[:, :, 1]) - np.min(padded_probe_positions[:, :, 1]) + self._dp_j + 2 * padding
        )
        padded_object = np.ones(padded_object_shape, dtype = complex)

        return padded_object
    
    def generateRonchigram(self) -> np.ndarray:
        """
        Generate Ronchigram based on the current probe and a random phase slice.

        Returns:
            numpy.ndarray: A 2-dimensional numpy array representing the Ronchigram.
        """
        dp_N = self.dp_N
        du = self.du
        dx = self.dx

        # Generate a random phase slice
        transmission = np.ones((dp_N, dp_N)) + np.random.rand(dp_N, dp_N) * 2 * np.pi * 1j

        # Limit transmission function to 2/3 of the maximum spatial frequency
        k_max = 1/(2*dx)
        mask = np.zeros((dp_N, dp_N))
        ri, rj = self.generateDiffractionMeshgrid()
        mask[ri**2 + rj**2 < 2/3*k_max] = 1

        transmission = self.ifft2((self.fft2(transmission, du)*mask), dx)
        probe = self.getProbe()
        ronchigram = self.fft2(probe * transmission, du)
        return np.abs(ronchigram)**2



class CTFCalculator(object):
    """
    用于计算 CTF 曲线的类。
    """
    def __init__(self, optical_stem: OpticalSTEM = None):
        """
        初始化 CTFCalculator 对象。

        arguments:
            optical_stem: (OpticalSTEM) 需要先初始化一个 OpticalSTEM 对象，然后将其传递给 CTFCalculator。
        """
        if optical_stem is None:
            optical_stem = OpticalSTEM()
        if not isinstance(optical_stem, OpticalSTEM):
            raise TypeError("optical_stem must be an OpticalSTEM object")
        self._optical_stem = optical_stem 

    def getOpticalSTEM(self) -> OpticalSTEM:
        """
        获取其内部的 OpticalSTEM 对象。

        returns:
            (OpticalSTEM)
        """
        return self._optical_stem 
    
    def setOpticalSTEM(self, optical_stem: OpticalSTEM):
        """
        使用新的 OpticalSTEM 对象。

        arguments:
            optical_stem: (OpticalSTEM) 
        """
        if not isinstance(optical_stem, OpticalSTEM):
            raise TypeError("optical_stem must be an OpticalSTEM object")
        self._optical_stem = optical_stem 

    @property
    def optical_stem(self) -> OpticalSTEM:
        return self._optical_stem 
    
    @optical_stem.setter 
    def optical_stem(self, opt_s: OpticalSTEM):
        self.setOpticalSTEM(opt_s)

    def calcCTFofVirtualImageFirstOrder(self, beta_min: float, beta_max: float, update_cache: bool = True):
        """
        计算 Virtual Image 的关于 sin φ 的衬度传递函数。

        具体的计算公式见 
            E.G.T. Bosch, I. Lazić. Ultramicroscopy 156 (2015) 59-72 
        

        arguments:
            beta_min: (float) 环形探测器的最小收集角。如果是 0 则为圆形探测器。

            beta_max: (float) 环形探测器的最大收集角。

            update_cache: (bool) 是否要更新 OpticalSTEM 中的 cache。如果两次计算之间没有更新 OpticalSTEM 之间的参数，可以令 update_cache = False，这样可以无需重新计算 probe，加快计算速度。
        """
        mask = self.optical_stem.generateVirtualAnnularDetector(beta_min, beta_max)
        probe = self.optical_stem.getProbe(update_cache)
        dx = self.optical_stem.dx 
        du = self.optical_stem.du 
        fft2 = self.optical_stem.fft2 
        ifft2 = self.optical_stem.ifft2 
        B_tmp = probe * fft2(mask * ifft2(np.conj(probe), dx), du)
        ctfs = -2 * np.conj(fft2(np.imag(B_tmp), dx))
        return np.real(ctfs)
    
    def calcCTFsFromBosch(self, beta_min: float, beta_max: float, update_cache: bool = True):
        """
        计算 Virtual Image 的关于 sin φ 的衬度传递函数。

        它与 calcCTFofVirtualImageFirstOrder 所遵循的公式有所不同，但二者是等价的。这个函数所遵循的不过是展开式。

        arguments:
            beta_min: (float) 环形探测器的最小收集角。如果是 0 则为圆形探测器。

            beta_max: (float) 环形探测器的最大收集角。

            update_cache: (bool) 是否要更新 OpticalSTEM 中的 cache。如果两次计算之间没有更新 OpticalSTEM 之间的参数，可以令 update_cache = False，这样可以无需重新计算 probe，加快计算速度。
        """
        mask = self.optical_stem.generateVirtualAnnularDetector(beta_min, beta_max)
        probe = self.optical_stem.getProbe()
        dx = self.optical_stem.dx 
        du = self.optical_stem.du 
        fft2 = self.optical_stem.fft2 
        ifft2 = self.optical_stem.ifft2 
        b = probe*fft2(mask*ifft2(np.conj(probe), dx), du)
        bi = np.conj(probe) * ifft2(mask*fft2(probe, dx), du) 
        ctfs = -1j * np.conj(fft2(b - bi, dx))
        return np.real(ctfs)
        

    def calcCTFofVirtualImageSecondOrder(self, beta_min: float, beta_max: float, rho = 1e-10, update_cache: bool = True):
        """
        计算 Virtual Image 的关于 1 - cos φ 的衬度传递函数。

        具体的计算公式见 
            E.G.T. Bosch, I. Lazić. Ultramicroscopy 156 (2015) 59-72 

        arguments:
            beta_min: (float) 环形探测器的最小收集角。如果是 0 则为圆形探测器。

            beta_max: (float) 环形探测器的最大收集角。

            rho: (float) 与样品有关的参数。见 
            E.G.T. Bosch, I. Lazić. Ultramicroscopy 156 (2015) 59-72 
            对于晶体样品，rho 的取值为 0.055 nm
            对于非晶体样品，rho 的取值为 0.090 nm

            update_cache: (bool) 是否要更新 OpticalSTEM 中的 cache。如果两次计算之间没有更新 OpticalSTEM 之间的参数，可以令 update_cache = False，这样可以无需重新计算 probe，加快计算速度。
        """
        mask = self.optical_stem.generateVirtualAnnularDetector(beta_min, beta_max)
        probe = self.optical_stem.getProbe(update_cache)
        dx = self.optical_stem.dx 
        du = self.optical_stem.du 
        fft2 = self.optical_stem.fft2 
        ifft2 = self.optical_stem.ifft2 
        wave_length = self.optical_stem.wave_length 
        B_tmp = probe * fft2(mask * ifft2(np.conj(probe), dx), du) 
        ctfc = -2 * np.conj(fft2(np.real(B_tmp), dx))

        # 这个 G_D 的计算结果是和数值计算 (直接计算积分) 结果吻合的。
        G_D = (bessel_j0(2*np.pi/wave_length*beta_min*rho)
            - bessel_j0(2*np.pi/wave_length*beta_max*rho))  

        ctfkk = 2 * G_D * np.conj(fft2(probe * np.conj(probe), dx))
        return np.real(ctfc + ctfkk)

    def calcCTFofICoM(self, update_cache = True):
        """
        计算 iCoM 成像的关于 φ 的衬度传递函数。

        arguments:
            update_cache: (bool) 是否要更新 OpticalSTEM 中的 cache。如果两次计算之间没有更新 OpticalSTEM 之间的参数，可以令 update_cache = False，这样可以无需重新计算 probe，加快计算速度。
        """
        probe = self.optical_stem.getProbe(update_cache)
        dx = self.optical_stem.dx 
        fft2 = self.optical_stem.fft2 
        ctfi = (1/(2*np.pi)) * np.conj(fft2(probe * np.conj(probe), dx))
        return np.real(ctfi) 
    
    def calcCTFofDCoM(self, update_cache = True):
        """
        计算 dCoM 成像的关于 φ 的衬度传递函数。

        arguments:
            update_cache: (bool) 是否要更新 OpticalSTEM 中的 cache。如果两次计算之间没有更新 OpticalSTEM 之间的参数，可以令 update_cache = False，这样可以无需重新计算 probe，加快计算速度。
        """
        probe = self.optical_stem.getProbe(update_cache)
        dx = self.optical_stem.dx 
        fft2 = self.optical_stem.fft2 
        ui, uj = self.optical_stem.generateDiffractionMeshgrid()
        ctfd = 2 * np.pi * (ui**2 + uj**2) * np.conj(fft2(probe * np.conj(probe), dx))
        return np.real(ctfd) 
    
    def calcCTFofAxialBF(self, update_cache = True):
        """
        计算近轴明场像的关于 sin φ 的衬度传递函数。

        注意，这里的衬度实际上是取虚拟探测器为狄拉克 δ 函数。这是因为，近轴明场像的探测器面积太小了，如果不在强度上予以补偿的话，其成像强度就很弱。此外，这也具有实际意义——其衬度传递函数正好等于传统平行光的 TEM。这种性质来源于光路的可逆性。

        此外，需要注意在公式中，delta 函数作傅里叶变换，相当于 $F^{-1}[\psi_{in}^*](0)$ 的取值。在公式中，这个值为 1。但在数值计算时，由于使用了 probe 在全空间的模平方积分等于 1 的归一化条件，所以 $F^{-1}[\psi_{in}^*](0)$ 值此时并不为 1。因此，我们需要现场计算这个值。

        还需要注意到以上 delta 函数发挥的是选择作用，但它也应当与面积挂钩，尤其是在与 LaBF 进行比较的时候。例如，当我们让 LaBF 乘以了一个倍数，那么 delta 函数 (从量纲上来说) 也应当乘以一个倍数才能作比较。如果我们将 mask 函数设为一个半径逐渐收敛至 0 的圆盘函数列 {fn} 的极限，并保持 fn 在全倒空间的积分为 MaBF 的收集区域面积，那么就是一个合适的比较方法。如果我们要用 AxialBF 来计算 TEM 的话，那么结果应当乘以 pi * u_BF**2 。如果我们要和 MaBF 作比较的话，那么结果应当乘以 pi * (u_BF/2)**2 。

        具体的计算公式见 
            E.G.T. Bosch, I. Lazić. Ultramicroscopy 156 (2015) 59-72 

        arguments:
            update_cache: (bool) 是否要更新 OpticalSTEM 中的 cache。如果两次计算之间没有更新 OpticalSTEM 之间的参数，可以令 update_cache = False，这样可以无需重新计算 probe，加快计算速度。
        """
        probe = self.optical_stem.getProbe(update_cache)
        dx = self.optical_stem.dx
        fft2 = self.optical_stem.fft2 
        norm = np.sum(np.conj(probe)) * (dx**2)
        ctfab = -2 * np.conj(fft2(np.imag(probe * norm), dx))
        return np.real(ctfab) * np.pi * (self.optical_stem.alpha/self.optical_stem.wave_length) ** 2
    
    @staticmethod 
    def generateRadialPreimage(
        matrix_shape: tuple[int],
        target: tuple[float|int] = None,
        pixel_size: float = None,
    ) -> tuple:
        """
        这个函数用来取得矩阵各个点相对于目标点的整数距离的原像。

        该函数的作用，是将矩阵中每个坐标按照极坐标系中的 r 进行分类。这样，便可以完成从直角坐标系到极坐标系的变换。此外，也可以用它来生成图像的平均径向分布。

        例如，对于 2x3 矩阵而言，目标点为 (1, 1)，则此时根据各个坐标与中心点之间的距离，生成

            locate = [
                [(1,1),], 
                [(0,1),(1,0),(1,2),], 
                [(0,0), (0,2),],
            ]
            distance = [0, 1, sqrt(2)]

        其中：
            locate 的第一行对应于与 target 点距离为 0 的点，就是 target 点本身；
            locate 的第二行对应于与 target 点距离为 1 的点，有三个；
            locate 的第三行对应于与 target 点距离为 sqrt(2) 的点，有两个。

        在实际的计算中，我们会使用 round 函数，将小数距离四舍五入为整数。因此，实际的输出为
            locate = [
                [(1,1),], 
                [(0,1),(1,0),(1,2),(0,0),(0,2),],
            ]
            distance = [0, 1]

        该函数的运行效率是 O(MN) 的，与矩阵元素数成正比。作为参考，计算 1024 x 1024 矩阵的坐标所花费时间为 0.53 s。

        如果需要多次计算相同尺寸、极坐标中心的平均径向分布，可以只调用一次 generateRadialPreimage 并缓存结果，这样可以大幅度地加速计算。
        
        arguments:
            matrix_shape: (tuple) 矩阵的形状，必须是两个整数

            target: (tuple) 目标点，必须是两个数，分别是对应于目标点的 i 坐标和 j 坐标。如果不传入，那么默认为 (M//2, N//2)

            pixel_size: (float) 每个格子的大小。如果传入了 pixel_size，那么输出的 distance 列表结果将乘以 pixel_size。注意，此时 target 参数依然应当传入整数的 index 而不是物理距离。

        returns:    (locate, distance)
            locate: (list) 一个列表，每行中包含一个或多个坐标。

            distance: (np.ndarray) 一个和 locate 相同长度的列表，对应于 locate 各行的坐标点离目标点的距离。
        """
        i_range = np.arange(matrix_shape[0])
        j_range = np.arange(matrix_shape[1])
        i_index, j_index = np.meshgrid(i_range, j_range, indexing='ij')
        if target is None:
            target = (matrix_shape[0]//2, matrix_shape[1]//2)

        distance_distribution = np.round(np.sqrt(
            (i_index - target[0])**2 + (j_index - target[0])**2
        ))
        max_distance = np.max(distance_distribution)
        min_distance = np.min(distance_distribution)
        distance = np.arange(min_distance, max_distance + 1)
        locate = [[] for _ in distance]

        for ii in range(matrix_shape[0]):
            for jj in range(matrix_shape[1]):
                locate[int(distance_distribution[ii, jj] - min_distance)].append((ii, jj))
        for ii, locate_list in enumerate(locate):
            locate[ii] = np.array(locate_list)
        
        if pixel_size is not None:
            distance *= pixel_size 
        return locate, distance 
    
    @staticmethod
    def generateRotationalAverage(
        distribution_function: np.ndarray, 
        target: tuple[float|int] = None,
        pixel_size: float = None,
        preimage_locate: list = None,
        preimage_distance: np.ndarray = None,
    ):
        """
        这个函数用于计算旋转平均分布 (径向分布)。

        基于函数 generateRadialPreimage()，根据其结果，找到距离中心为特定值的所有点，取到这些点的分布值并计算其平均。
    
        对于 N = 1024 的数据耗时 1.0 s。其中，函数 generateRadialPreimage() 耗时 0.97 s，而剩余部分耗时 0.02 s。如果要计算多张图片的旋转平均分布，则可以复用函数 generateRadialPreimage 的计算结果，因此每多一张耗时只增加 0.02 s。经过不懈努力，我们终于 (在需要计算大量图片的径向分布时) 超越了 skimage 用极坐标变换计算的速度，这应该很难再有优化空间了。

        arguments:
            distribution_function: (np.ndarray) 分布矩阵，必须是正方形。

            target: (tuple) 目标点，必须是两个数，分别是对应于目标点的 i 坐标和 j 坐标。如果不传入，那么默认为 (M//2, N//2)

            pixel_size: (float) 每个格子的大小。如果传入了 pixel_size，那么输出的 distance 列表结果将乘以 pixel_size。注意，此时 target 参数依然应当传入整数的 index 而不是物理距离。

            preimage_locate: (list) 如果已经事先计算好了每个位置所对应的距离，那么可以将其传入它以节约计算时间。注意，如果传入了这个参数，也必须传入配套的 如果想要物理上的参考 generateRoundDistancePreimage() 函数。

        returns:
            (tuple) 其中第一项为
                rotational_average_x: (np.ndarray) 径向分布的横坐标
                    其中第二项为
                rotational_average_y: (np.ndarray) 径向分布的纵坐标
        """
        shape = distribution_function.shape
        if preimage_locate is None:
            if target is None:
                target = (shape[0]//2, shape[1]//2)
            locate, distance = CTFCalculator.generateRadialPreimage(
                shape, target, pixel_size = pixel_size
            )
        else:
            locate, distance = preimage_locate, preimage_distance
            if preimage_distance is None:
                raise RuntimeError("Must pass preimage_distance parameter when using preimage_locate")

        radial_distribution = np.zeros_like(distance)
    
        # 这里如果使用二维 indexing 的话，numpy 似乎会以 N^3 的速度来取到各个指标
        # 所以这里我们选择将矩阵重新排列为一维的，然后通过一维 indexing 来计算
        shape = distribution_function.shape
        distribution_array = distribution_function.reshape((shape[0] * shape[1],))
        for ii in range(len(distance)):
            radial_distribution[ii] = np.mean(distribution_array[
                locate[ii][:,0]*shape[1] + locate[ii][:,1]
            ])
        return distance, radial_distribution 

    def calcCTFofTEM(self, objective_aperture_radius: float = None, chromatic_delta: float = 0):
        """
        计算相同条件 (满足光路可逆原理) 下 TEM 的 CTF。

        推导过程见 
        E. J. Kirkland. Advanced Computing in Electron Microscopy. (2010) 30-35

        应当注意，在不添加色差以及物镜光阑时，该函数所计算的 CTF 曲线的范围为 -2 到 2，这与
            D. B. Williams, C. B. Carter. Transmission Electron Microscopy: A Textbook for Materials Science. (2009) 487-490 
        是一致的。但该结果是
            E. J. Krikland. Advanced Computing in Electron Microscopy. (2010) 30-35
        中所列的公式，及 ctfExplorer 软件的生成结果的 2 倍大小。

        arguments:
            objective_aperture_radius: (float) 物镜光阑在倒空间中的半径，单位 rad. 如果为 None，则默认不添加物镜光阑。

            chromatic_delta: (float) 色差所导致的等效离焦量，单位 m。这个参量是用来计算包络函数的。
        """
        chi = self.optical_stem.generateAberrationFunction()
        beam = np.exp(-1j * chi)


        if chromatic_delta != 0:
            ui, uj = self.optical_stem.generateDiffractionMeshgrid()
            Ecexp = np.exp(- 1/2 * (
                np.pi * self.optical_stem.wave_length * chromatic_delta
            )**2 * (ui**2 + uj**2)**2)
        else:
            Ecexp = np.ones((
                self.optical_stem.getDetectorN(), 
                self.optical_stem.getDetectorN()
            ))
        if objective_aperture_radius is not None:
            aperture = self.optical_stem.generateVirtualAnnularDetector(
                beta_min = 0, 
                beta_max = objective_aperture_radius
            )
        else:
            aperture = np.ones((
                self.optical_stem.getDetectorN(), 
                self.optical_stem.getDetectorN()
            ))
        
        # tem_ctf = 2 * aperture * Ecexp * np.sin(chi)
        tem_ctf = - 2 * aperture * Ecexp * np.imag(beam)
        return tem_ctf 
        
    def calcEnvelopeFunctionTEM(self, chromatic_delta: float = 0):
        """
        计算相同条件 (满足光路可逆原理) 下 TEM 的包络函数。

        计算公式为
            E(u) = exp(-(πλδu/2)^2) 

        arguments:
            chromatic_delta: (float) 色差所导致的等效离焦量，单位 m。这个参量是用来计算包络函数的。
        """
        if chromatic_delta != 0:
            ui, uj = self.optical_stem.generateDiffractionMeshgrid()
            Ecexp = np.exp(- 1/2 * (
                np.pi * self.optical_stem.wave_length * chromatic_delta
            )**2 * (ui**2 + uj**2)**2)
        else:
            Ecexp = np.ones((
                self.optical_stem.getDetectorN(), 
                self.optical_stem.getDetectorN()
            ))
        return Ecexp 



