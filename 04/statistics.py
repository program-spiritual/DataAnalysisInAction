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
''' output
最小值
1
[1 2 3]
[1 4 7]
最大值
9
[7 8 9]
[3 6 9]

'''

print np.ptp(a)
print np.ptp(a, 0)
print np.ptp(a, 1)

'''
最大值和最小值的差
8
[6 6 6]
[2 2 2]

'''

# 中位数
print u"中位数:"
print np.median(a)
print np.median(a, axis=0)
print np.median(a, axis=1)

'''
中位数:
5.0
[4. 5. 6.]
[2. 5. 8.]

'''

# 求平均数
print u"平均数:"
np.mean(a)
print np.mean(a, axis=0)
print np.mean(a, axis=1)

# 加权平均数
print u"加权平均数:"
b = np.array([1, 2, 3, 4])

wts = np.array([1, 2, 3, 4])
print np.average(b)
print np.average(b, weights=wts)

# 标准差
print u"标准差:"
c = np.array([1, 2, 3, 4])

print np.std(c)

# 方差
print u"方差:"

c = np.array([1, 2, 3, 4])
print np.var(c)

print u'排序'

d = np.array(
  [
    [4, 3, 2],
    [2, 4, 1]
  ]
)
print np.sort(d)
print np.sort(d, axis=None)
print np.sort(d, axis=0)
print np.sort(d, axis=1)
