axis =0 || acxis =1
## 验证方向问题

![image](./axis0-1.png)

## 创建矩阵

[createArray](./createArray.py)

```python
# encoding:utf-8
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1, 1] = 10
print  a.shape
print b.shape
print a.dtype
print b


```

## 结构矩阵

[structArray](./structArray.py)

```python
# encoding:utf-8
import numpy as np

persontype = np.dtype({
  'names': ['name', 'age', 'chinese', 'math', 'english'],
  'formats': ['S32', 'i', 'i', 'i', 'f']
})

peoples = np.array(
  [
    ('zhangfei', 32, 75, 100, 90),
    ('guanyu', 24, 85, 96, 88.5),
    ('zhaoyun', 28, 85, 92, 96.5),
    ('huangzhong', 29, 65, 85, 100)
  ],
  dtype=persontype
)

ages = peoples[:]['age']
chineses = peoples[:]['chinese']
math = peoples[:]['math']
english = peoples[:]['english']

print np.mean(ages)
print np.mean(chineses)
print np.mean(math)
print np.mean(english)



```
## 分析

[statistics.py](./statistics.py)

```python
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

```

## 算数运算

[arithmetic.py](./arithmetic.py)

```python
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

```

## 求百分比

![image](./axis0-2.png)

[statistics](./statistics.py)

```python
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

```

## 排序



![image](./axis0-3.png)

[statistics](./statistics.py)

```python
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

```
