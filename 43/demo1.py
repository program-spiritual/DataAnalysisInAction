# coding=utf-8
import matplotlib

matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
import pylab
import cv2
import numpy as np
from scipy import signal

# 读取灰度图像
img = cv2.imread("haibao.jpeg", 0)
# 显示灰度图像
plt.imshow(img, cmap="gray")
pylab.show()
# 设置卷积核
fil = np.array(
  [
    [-1, -1, 0],
    [-1, 0, 1],
    [0, 1, 1]
  ]
)
# 卷积操作
res = signal.convolve2d(img, fil, mode='valid')
print(res)
# 显示卷积后的图片
plt.imshow(res, cmap="gray")
pylab.show()
