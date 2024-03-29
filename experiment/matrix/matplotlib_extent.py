# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# 创建一个8x8的矩阵，初始值为0
matrix = np.zeros((8, 8))

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 使用imshow绘制矩阵（使用默认的extent）
# cax = ax.imshow(matrix, cmap='viridis')

# 创建一个中心在(4,4)半径为4的圆
circle = Circle((4, 4), 4, edgecolor='red', facecolor='red', alpha = 0.5)
# ax.add_patch(circle)

# 显示结果
# plt.show()

# 使用matplotlib的方法判断哪些点在圆内，并将这些点的值加1
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        # 检查点是否在圆内
        if circle.contains_point((j, i)):
            matrix[i, j] += 1

# 手动计算各像素点与中心点(4,4)的距离，并判断是否在圆内
# 如果在圆内，则将像素点的值再加1
radius = 4
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        # 计算距离中心(4,4)的欧几里得距离
        distance = np.sqrt((j - 4)**2 + (i - 4)**2)
        # 判断是否在圆内
        if distance <= radius:
            matrix[i, j] += 1

# 输出最终的矩阵
print(matrix)

ax.add_patch(circle)
cax = ax.imshow(matrix, cmap = 'viridis', extent=[0,8,0,8])
try:
    plt.show()
except BaseException as e:
    print(e)