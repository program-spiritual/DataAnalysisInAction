## K-Means

1. 类型： 非监督学习
2. 目的 ： 解决聚类问题
3. `K` == `K` 类
4. `Means` 代表的是 中心
5. 本质： 确定 `K` 类的中心点

### 工作原理

1. 选择 `K` 点作为初始的类中心点
2. 将每个点分配到最近的类中心点
3. 重复第二部 直到状态稳定

### 数据

根目录下面的 `kmeans-master`文件夹


### 示例文件

[示例代码](./demo/index.py)

```python
# coding=utf-8
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# 输入数据
data = pd.read_csv('data.csv', encoding='gbk')
train_x = data[["2019 年国际排名 ", "2018 世界杯 ", "2015 亚洲杯 "]]
df = pd.DataFrame(train_x)
kmeans = KMeans(n_clusters=3)
# 规范化到 [0,1] 空间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
# kmeans 算法
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0: u'聚类'}, axis=1, inplace=True)
print(result)


```