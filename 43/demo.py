# coding=utf-8

import pylab
import numpy as np
from scipy import signal

# 设置原图像
img = np.array([[10, 10, 10, 10, 10],
                [10, 5, 5, 5, 10],
                [10, 5, 5, 5, 10],
                [10, 5, 5, 5, 10],
                [10, 10, 10, 10, 10]])
# 设置卷积核
fil = np.array([[-1, -1, 0],
                [-1, 0, 1],
                [0, 1, 1]])
# 对原图像进行卷积操作
res = signal.convolve2d(img, fil, mode='valid')
# 输出卷积后的结果
print(res)

'''output
[[ 15  10   0]
 [ 10   0 -10]
 [  0 -10 -15]]
'''
