# encoding:utf-8

import matplotlib

matplotlib.use('Qt4Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
## 准备数据
x = range(2010,2020,1)
print x
y = [5,3,6,20,17,16,19,30,32,35]

plt.plot(x,y)
plt.show()