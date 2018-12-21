# encoding:utf-8

import numpy as np

a = np.array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])

print np.amin(a)
print np.amin(a, 0)
print np.amin(a, 1)

print np.amax(a)
print np.amax(a, 0)
print np.amax(a, 1)
