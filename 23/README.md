## 如何进行乳腺癌检测

### 如何使用 `SVM`
1. `SVM` 可以做回归
  - 使用 `SVR`
2. 也可以做分类器
  - 使用 `SVC` -- 非线性      
  - 或者 `LinearSVC` -- 线性分类器

## 实例

> 乳腺癌诊断数据集在本讲的根目录

### 肿瘤可以分为良性和恶性

### 数据表共32个字段

![](WechatIMG70.jpeg)

### 分类器执行流程

![](WechatIMG71.jpeg)

### 代码
- 探索

  [数据探索代码](./discover.py)
  
```python
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


```

- 清洗

  `id` 没有实际含义  去掉

  `diagnosis` 取值 为  `B || M` 替换为 `0 || 1`

  `mean` `se` `worst` 代表不同的度量方式

  [数据清洗代码](./breastCancerData/breast_svm.py)

```python
import matplotlib
matplotlib.use('Qt4Agg')
# 乳腺癌诊断分类
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

# 加载数据集，你需要把数据放到目录中
data = pd.read_csv("./data.csv")

# 数据探索
# 因为数据集中列比较多，我们需要把dataframe中的列全部显示出来
pd.set_option('display.max_columns', None)
print(data.columns)
print(data.head(5))
print(data.describe())

# 将特征字段分成3组
features_mean= list(data.columns[2:12])
features_se= list(data.columns[12:22])
features_worst=list(data.columns[22:32])

# 数据清洗
# ID列没有用，删除该列
data.drop("id",axis=1,inplace=True)
# 将B良性替换为0，M恶性替换为1
data['diagnosis']=data['diagnosis'].map({'M':1,'B':0})

# 将肿瘤诊断结果可视化
sns.countplot(data['diagnosis'],label="Count")
plt.show()
# 用热力图呈现features_mean字段之间的相关性
corr = data[features_mean].corr()
plt.figure(figsize=(14,14))
# annot=True显示每个方格的数据
sns.heatmap(corr, annot=True)
plt.show()


# 特征选择
features_remain = ['radius_mean','texture_mean', 'smoothness_mean','compactness_mean','symmetry_mean', 'fractal_dimension_mean'] 

# 抽取30%的数据作为测试集，其余作为训练集
train, test = train_test_split(data, test_size = 0.3)# in this our main data is splitted into train and test
# 抽取特征选择的数值作为训练和测试数据
train_X = train[features_remain]
train_y=train['diagnosis']
test_X= test[features_remain]
test_y =test['diagnosis']

# 采用Z-Score规范化数据，保证每个特征维度的数据均值为0，方差为1
ss = StandardScaler()
train_X = ss.fit_transform(train_X)
test_X = ss.transform(test_X)

# 创建SVM分类器
model = svm.SVC()
# 用训练集做训练
model.fit(train_X,train_y)
# 用测试集做预测
prediction=model.predict(test_X)
print('准确率: ', metrics.accuracy_score(prediction,test_y))

```