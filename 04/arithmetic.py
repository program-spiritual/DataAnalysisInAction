# encoding:utf-8

import numpy as np

x1 = np.arange(1, 11, 2)  # 默认不包含最终值
x2 = np.linspace(1, 9, 5)  # 默认包含最终值

print np.add(x1, x2)  # 加法
print np.subtract(x1, x2)  # 加法
print np.multiply(x1, x2)  # 乘法
print np.divide(x1, x2)  # 除法
print np.power(x1, x2)  # 求N次方
print np.remainder(x1, x2)  # 取余
