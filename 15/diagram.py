# encoding:utf-8
import matplotlib

matplotlib.use('Qt4Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## 数据准备

x = ['Cat1', 'Cat2', 'Cat3', 'Cat4','Cat5' ]
y = [5, 4, 8, 12, 7]

plt.bar(x, y)
plt.show()
