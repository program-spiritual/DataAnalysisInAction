## 39讲

![](39丨数据挖掘实战（1）：信用卡违约率分析.png)

## 随机森林算法 `demo`

[代码实例](demo.py)

```python
# -*- coding: utf-8 -*-
# 使用 RandomForest 对 IRIS 数据集进行分类
# 利用 GridSearchCV 寻找最优参数
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
rf = RandomForestClassifier()
parameters = {"n_estimators": range(1,11)}
iris = load_iris()
# 使用 GridSearchCV 进行参数调优
clf = GridSearchCV(estimator=rf, param_grid=parameters)
# 对 iris 数据集进行分类
clf.fit(iris.data, iris.target)
print(" 最优分数： %.4lf" %clf.best_score_)
print(" 最优参数：", clf.best_params_)


```

## `Pipeline` 管道机制流水线作业

分类步骤

 1. 数据规范化处理
   - `StandardScaler()` 方法
 2. `PCA` 方法 对数据降维
  
 3. 分类器分类
 
 
 [代码实例](demo2.py)
 
```python
from sklearn.model_selection import GridSearchCV
pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA()),
        ('randomforestclassifier', RandomForestClassifier())
])

``` 
 
 采用 Pipeline 管道机制，用随机森林对 IRIS 数...

 [代码](demo3.py)
 
```python
# -*- coding: utf-8 -*-
# 使用 RandomForest 对 IRIS 数据集进行分类
# 利用 GridSearchCV 寻找最优参数, 使用 Pipeline 进行流水作业
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
rf = RandomForestClassifier()
parameters = {"randomforestclassifier__n_estimators": range(1,11)}
iris = load_iris()
pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('randomforestclassifier', rf)
])
# 使用 GridSearchCV 进行参数调优
clf = GridSearchCV(estimator=pipeline, param_grid=parameters)
# 对 iris 数据集进行分类
clf.fit(iris.data, iris.target)
print(" 最优分数： %.4lf" %clf.best_score_)
print(" 最优参数：", clf.best_params_)
# 运行结果：
# 最优分数： 0.9667
# 最优参数： {'randomforestclassifier__n_estimators': 9}

``` 

## 对信用卡违约率进行分析

数据集字段

![](https://static001.geekbang.org/resource/image/17/88/1730fb3a809c99950739e7f50e1a6988.jpg)

构建分类器

  1. 加载数据
  2.  准备阶段
      - train_test_split 划分数据集
  3. 分类阶段
     - 管道机制
     - 数据规范
     - 分类
 
实战

 [官方代码](./credit_default/credit_default_analysis.py)

```python
# -*- coding: utf-8 -*-
# 信用卡违约率分析
import pandas as pd
from sklearn.model_selection import learning_curve, train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
import seaborn as sns
# 数据加载
data = data = pd.read_csv('./UCI_Credit_Card.csv')
# 数据探索
print(data.shape) # 查看数据集大小
print(data.describe()) # 数据集概览
# 查看下一个月违约率的情况
next_month = data['default.payment.next.month'].value_counts()
print(next_month)
df = pd.DataFrame({'default.payment.next.month': next_month.index,'values': next_month.values})
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.figure(figsize = (6,6))
plt.title('信用卡违约率客户\n (违约：1，守约：0)')
sns.set_color_codes("pastel")
sns.barplot(x = 'default.payment.next.month', y="values", data=df)
locs, labels = plt.xticks()
plt.show()
# 特征选择，去掉ID字段、最后一个结果字段即可
data.drop(['ID'], inplace=True, axis =1) #ID这个字段没有用
target = data['default.payment.next.month'].values
columns = data.columns.tolist()
columns.remove('default.payment.next.month')
features = data[columns].values
# 30%作为测试集，其余作为训练集
train_x, test_x, train_y, test_y = train_test_split(features, target, test_size=0.30, stratify = target, random_state = 1)
    
# 构造各种分类器
classifiers = [
    SVC(random_state = 1, kernel = 'rbf'),    
    DecisionTreeClassifier(random_state = 1, criterion = 'gini'),
    RandomForestClassifier(random_state = 1, criterion = 'gini'),
    KNeighborsClassifier(metric = 'minkowski'),
]
# 分类器名称
classifier_names = [
            'svc', 
            'decisiontreeclassifier',
            'randomforestclassifier',
            'kneighborsclassifier',
]
# 分类器参数
classifier_param_grid = [
            {'svc__C':[1], 'svc__gamma':[0.01]},
            {'decisiontreeclassifier__max_depth':[6,9,11]},
            {'randomforestclassifier__n_estimators':[3,5,6]} ,
            {'kneighborsclassifier__n_neighbors':[4,6,8]},
]
 
# 对具体的分类器进行GridSearchCV参数调优
def GridSearchCV_work(pipeline, train_x, train_y, test_x, test_y, param_grid, score = 'accuracy'):
    response = {}
    gridsearch = GridSearchCV(estimator = pipeline, param_grid = param_grid, scoring = score)
    # 寻找最优的参数 和最优的准确率分数
    search = gridsearch.fit(train_x, train_y)
    print("GridSearch最优参数：", search.best_params_)
    print("GridSearch最优分数： %0.4lf" %search.best_score_)
    predict_y = gridsearch.predict(test_x)
    print("准确率 %0.4lf" %accuracy_score(test_y, predict_y))
    response['predict_y'] = predict_y
    response['accuracy_score'] = accuracy_score(test_y,predict_y)
    return response
 
for model, model_name, model_param_grid in zip(classifiers, classifier_names, classifier_param_grid):
    pipeline = Pipeline([
            ('scaler', StandardScaler()),
            (model_name, model)
    ])
    result = GridSearchCV_work(pipeline, train_x, train_y, test_x, test_y, model_param_grid , score = 'accuracy')
``` 
 
 [demo4](demo4.py)
```python
# -*- coding: utf-8 -*-
# 信用卡违约率分析
import matplotlib
import pandas as pd
from sklearn.model_selection import learning_curve, train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
# 打印配置文件路径 我的是在个人文件夹
print(matplotlib.matplotlib_fname())
import seaborn as sns

# 数据加载
data = data = pd.read_csv('./UCI_Credit_Card.csv')
# 数据探索
print(data.shape)  # 查看数据集大小
print(data.describe())  # 数据集概览
# 查看下一个月违约率的情况
next_month = data['default.payment.next.month'].value_counts()
print(next_month)
df = pd.DataFrame({'default.payment.next.month': next_month.index, 'values': next_month.values})
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.figure(figsize=(6, 6))
plt.title(u'信用卡违约率客户\n (违约：1，守约：0)')
sns.set_color_codes("pastel")
sns.barplot(x='default.payment.next.month', y="values", data=df)
locs, labels = plt.xticks()
plt.show()
# 特征选择，去掉ID字段、最后一个结果字段即可
data.drop(['ID'], inplace=True, axis=1)  # ID这个字段没有用
target = data['default.payment.next.month'].values
columns = data.columns.tolist()
columns.remove('default.payment.next.month')
features = data[columns].values
# 30%作为测试集，其余作为训练集
train_x, test_x, train_y, test_y = train_test_split(features, target, test_size=0.30, stratify=target, random_state=1)

# 构造各种分类器
classifiers = [
  SVC(random_state=1, kernel='rbf'),
  DecisionTreeClassifier(random_state=1, criterion='gini'),
  RandomForestClassifier(random_state=1, criterion='gini'),
  KNeighborsClassifier(metric='minkowski'),
]
# 分类器名称
classifier_names = [
  'svc',
  'decisiontreeclassifier',
  'randomforestclassifier',
  'kneighborsclassifier',
]
# 分类器参数
classifier_param_grid = [
  {'svc__C': [1], 'svc__gamma': [0.01]},
  {'decisiontreeclassifier__max_depth': [6, 9, 11]},
  {'randomforestclassifier__n_estimators': [3, 5, 6]},
  {'kneighborsclassifier__n_neighbors': [4, 6, 8]},
]


# 对具体的分类器进行GridSearchCV参数调优
def GridSearchCV_work(pipeline, train_x, train_y, test_x, test_y, param_grid, score='accuracy'):
  response = {}
  gridsearch = GridSearchCV(estimator=pipeline, param_grid=param_grid, scoring=score)
  # 寻找最优的参数 和最优的准确率分数
  search = gridsearch.fit(train_x, train_y)
  print("GridSearch最优参数：", search.best_params_)
  print("GridSearch最优分数： %0.4lf" % search.best_score_)
  predict_y = gridsearch.predict(test_x)
  print("准确率 %0.4lf" % accuracy_score(test_y, predict_y))
  response['predict_y'] = predict_y
  response['accuracy_score'] = accuracy_score(test_y, predict_y)
  return response


for model, model_name, model_param_grid in zip(classifiers, classifier_names, classifier_param_grid):
  pipeline = Pipeline([
    ('scaler', StandardScaler()),
    (model_name, model)
  ])
  result = GridSearchCV_work(pipeline, train_x, train_y, test_x, test_y, model_param_grid, score='accuracy')
```
 ## 总结
 
 ![](https://static001.geekbang.org/resource/image/14/16/14f9cddc17d6cceb0b8cbc4381c65216.png)
 