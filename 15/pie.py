# encoding:utf-8

import matplotlib

matplotlib.use('Qt4Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nums = [25, 37, 33, 37, 6]
labels = ['High-school', 'Bachelor', 'Master', 'Ph.d', 'Others']
plt.pie(x=nums, labels=labels)
plt.show()