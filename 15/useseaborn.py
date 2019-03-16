# encoding:utf-8
import matplotlib

matplotlib.use('Qt4Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set(style="darkgrid")

N = 1000
x = np.random.randn(N)
y = np.random.rand(N)

## use matplotlib
plt.scatter(x, y, marker='x')
plt.show()

## use seaborn

# df = pd.DataFrame({'x': x, 'y': y})
#
# sns.jointplot(x='x', y='y', data=df, kind='scatter')
# plt.show()
