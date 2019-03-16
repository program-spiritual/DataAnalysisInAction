# encoding:utf-8

import matplotlib

matplotlib.use('Qt4Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')
data = flights.pivot('year', 'month', 'passengers')
sns.heatmap(data)
sns.show()
