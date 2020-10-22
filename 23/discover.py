# 加载数据集，你需要把数据放到目录中
import pandas as pd

data = pd.read_csv("./breast_cancer_data/data.csv")
# 数据探索
# 因为数据集中列比较多，我们需要把 dataframe 中的列全部显示出来
pd.set_option('display.max_columns', None)
print(data.columns)
print('_' * 30)
print(data.head(5))
print('_' * 30)
print(data.describe())

