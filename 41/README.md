## 问题

比特币走势预测 那个方法比较好呢
  - 分类
  - 聚类
  - 回归
  - 关联分析

## 时间序列分析算法

时间序列分析模型建立了观察结果与时间变化的关系
可以帮助我们预测未来一段时间内的结果变化

## 时间序列和回归分析有哪些区别

1. 确定结果和变量之间的关系
2. 时间序列分析得到的是目标变量 `y` 与时间的相关性
3. 回归分析训练得到的是目标变量y 与 字段量 x( >=1 个) 的关联性  

4. 回归擅长的是多变量和目标结果之间的分析
5.时间序列分析建立在时间变化的基础上
    - 趋势
    - 周期
    - 时期
    - 不稳定因素


## 掌握

1. 概念
2. ARMA模型工具
3. 比特币历史数据时间序列建模并预测未来6个月的走势

经典模型

  - AR Auto Regressive 自回归模型
  - MA
  - ARMA
  - ARIMA

思想

过去若干时刻的点通过线性组合 加上白噪声 即可预测未来某个时刻的点

白噪声

  - 一个期望值为 `0` 方差为常数的纯随机过程

### 概念分类

- `AR` 模型还存在一个阶数，称为 `AR（p`）模型, `p` 阶自回归模型, 指定时刻 前 p 个点 通过线性组合加上白噪声来预测 `current` 的值

- `  MA` 滑动平均模型 历史时序值的线性组合， MA 是通过历史白噪声进行线性组合来影响当前时刻点

- ` ARMA` 是 `AR` 模型和 `MA` 模型的混合 同样 `ARMA` 模型存在 `p` 和 `q` 两个阶数，称为 `ARMA(p,q)` 模型

- `ARIMA`  差分自回归滑动平均模型 、 求合自回归滑动平均模型

相比于 `ARMA`，`ARIMA `多了一个差分的过程 不平稳数据进行差分平稳
平稳后建模

- `ARIMA` 是一个三元组的阶数 `(p,d,q)`，`ARIMA(p,d,q)` 模型 `d` 是差分阶数


引入

```python
from statsmodels.tsa.arima_model import ARMA
```
代码实例

1. [测试](demo1.py)

```python
# coding:utf-8
# 用 ARMA 进行时间序列预测
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARMA
from statsmodels.graphics.api import qqplot
# 创建数据
data = [5922, 5308, 5546, 5975, 2704, 1767, 4111, 5542, 4726, 5866, 6183, 3199, 1471, 1325, 6618, 6644, 5337, 7064, 2912, 1456, 4705, 4579, 4990, 4331, 4481, 1813, 1258, 4383, 5451, 5169, 5362, 6259, 3743, 2268, 5397, 5821, 6115, 6631, 6474, 4134, 2728, 5753, 7130, 7860, 6991, 7499, 5301, 2808, 6755, 6658, 7644, 6472, 8680, 6366, 5252, 8223, 8181, 10548, 11823, 14640, 9873, 6613, 14415, 13204, 14982, 9690, 10693, 8276, 4519, 7865, 8137, 10022, 7646, 8749, 5246, 4736, 9705, 7501, 9587, 10078, 9732, 6986, 4385, 8451, 9815, 10894, 10287, 9666, 6072, 5418]
data=pd.Series(data)
data_index = sm.tsa.datetools.dates_from_range('1901','1990')
# 绘制数据图
data.index = pd.Index(data_index)
data.plot(figsize=(12,8))
plt.show()
# 创建 ARMA 模型 # 创建 ARMA 模型
arma = ARMA(data,(7,0)).fit()
print('AIC: %0.4lf' %arma.aic)
# 模型预测
predict_y = arma.predict('1990', '2000')
# 预测结果绘制
fig, ax = plt.subplots(figsize=(12, 8))
ax = data.ix['1901':].plot(ax=ax)
predict_y.plot(ax=ax)
plt.show()

```

2. 结果对比

![](WX20190318-122721.png)
预测走势
![](WX20190318-122744.png)

```python
AIC: 1619.6323
```
字段

![](https://static001.geekbang.org/resource/image/b0/36/b0db4047723ec5e649240e2a87196a36.png)

流程

![](https://static001.geekbang.org/resource/image/95/1e/95f8294c1f4805b86f9947178499181e.jpg)

数据按月压缩

```python
df_month = df.resample('M').mean()
```

## 代码实例

```python
# -*- coding: utf-8 -*-
# 比特币走势预测，使用时间序列ARMA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARMA
import warnings
from itertools import product
from datetime import datetime

warnings.filterwarnings('ignore')
# 数据加载
df = pd.read_csv('./bitcoin_2012-01-01_to_2018-10-31.csv')
# 将时间作为df的索引
df.Timestamp = pd.to_datetime(df.Timestamp)
df.index = df.Timestamp
# 数据探索
print(df.head())
# 按照月，季度，年来统计
df_month = df.resample('M').mean()
df_Q = df.resample('Q-DEC').mean()
df_year = df.resample('A-DEC').mean()
# 按照天，月，季度，年来显示比特币的走势
fig = plt.figure(figsize=[15, 7])
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.suptitle('比特币金额（美金）', fontsize=20)
plt.subplot(221)
plt.plot(df.Weighted_Price, '-', label='按天')
plt.legend()
plt.subplot(222)
plt.plot(df_month.Weighted_Price, '-', label='按月')
plt.legend()
plt.subplot(223)
plt.plot(df_Q.Weighted_Price, '-', label='按季度')
plt.legend()
plt.subplot(224)
plt.plot(df_year.Weighted_Price, '-', label='按年')
plt.legend()
plt.show()
# 设置参数范围
ps = range(0, 3)
qs = range(0, 3)
parameters = product(ps, qs)
parameters_list = list(parameters)
# 寻找最优ARMA模型参数，即best_aic最小
results = []
best_aic = float("inf")  # 正无穷
for param in parameters_list:
  try:
    model = ARMA(df_month.Weighted_Price, order=(param[0], param[1])).fit()
  except ValueError:
    print('参数错误:', param)
    continue
  aic = model.aic
  if aic < best_aic:
    best_model = model
    best_aic = aic
    best_param = param
  results.append([param, model.aic])
# 输出最优模型
result_table = pd.DataFrame(results)
result_table.columns = ['parameters', 'aic']
print('最优模型: ', best_model.summary())
# 比特币预测
df_month2 = df_month[['Weighted_Price']]
date_list = [datetime(2018, 11, 30), datetime(2018, 12, 31), datetime(2019, 1, 31), datetime(2019, 2, 28),
             datetime(2019, 3, 31),
             datetime(2019, 4, 30), datetime(2019, 5, 31), datetime(2019, 6, 30)]
future = pd.DataFrame(index=date_list, columns=df_month.columns)
df_month2 = pd.concat([df_month2, future])
df_month2['forecast'] = best_model.predict(start=0, end=91)
# 比特币预测结果显示
plt.figure(figsize=(20, 7))
df_month2.Weighted_Price.plot(label='实际金额')
df_month2.forecast.plot(color='r', ls='--', label='预测金额')
plt.legend()
plt.title('比特币金额（月）')
plt.xlabel('时间')
plt.ylabel('美金')
plt.show()

```

比特币金额

![](WX20190318-123530.png)
打印日志

```python
最优模型:                                ARMA Model Results
==============================================================================
Dep. Variable:         Weighted_Price   No. Observations:                   83
Model:                     ARMA(1, 1)   Log Likelihood                -688.761
Method:                       css-mle   S.D. of innovations            957.761
Date:                Mon, 18 Mar 2019   AIC                           1385.523
Time:                        12:35:34   BIC                           1395.198
Sample:                    12-31-2011   HQIC                          1389.410
                         - 10-31-2018
========================================================================================
                           coef    std err          z      P>|z|      [0.025      0.975]
----------------------------------------------------------------------------------------
const                 2133.3881   1571.958      1.357      0.179    -947.592    5214.368
ar.L1.Weighted_Price     0.9252      0.042     22.031      0.000       0.843       1.008
ma.L1.Weighted_Price     0.2680      0.116      2.310      0.023       0.041       0.495
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.0808           +0.0000j            1.0808            0.0000
MA.1           -3.7313           +0.0000j            3.7313            0.5000
```
实际金额 预测金额
![](WX20190318-123541@2x.png)
## 总结

![](https://static001.geekbang.org/resource/image/24/94/24f8ee2f600a2451eecd58a98f7db894.png)
