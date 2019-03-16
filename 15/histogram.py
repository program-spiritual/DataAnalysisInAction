import matplotlib

matplotlib.use('Qt4Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = np.random.randn(100)
s = pd.Series(a)

plt.hist(s)
plt.show()