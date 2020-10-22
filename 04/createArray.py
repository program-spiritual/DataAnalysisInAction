# encoding:utf-8
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1, 1] = 10
print  a.shape
print b.shape
print a.dtype
print b

