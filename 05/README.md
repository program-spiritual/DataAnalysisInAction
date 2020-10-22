## 列表
[一般用法](./usePandas.py)

```python
import pandas as pd
from pandas import Series,DataFrame

x1 = Series([1,2,3,4])
x2 = Series(data=[1,2,3,4],index=['a','b','c','d'])

print x1
print x2


```

[Frame](./dataFrame.py)

```python
import pandas as pd
from pandas import Series, DataFrame

data = {
  'Chinese': [66, 95, 93, 90, 80],
  'English': [65, 85, 92, 88, 90],
  'Math': [30, 98, 96, 77, 90],
}

data_frame1  = DataFrame(data)

print data_frame1

'''
   Chinese  English  Math
0       66       65    30
1       95       85    98
2       93       92    96
3       90       88    77
4       80       90    90
'''

data_frame2 = DataFrame(data,index=['guan','zhang','zhao','ma','huang'])

print data_frame2

'''
       Chinese  English  Math
guan        66       65    30
zhang       95       85    98
zhao        93       92    96
ma          90       88    77
huang       80       90    90
'''
```

[词典](./dictionary.py)

```python
import pandas as pd
from pandas import Series,DataFrame

d = {'a':1,'b':2,'c':3,'d':4}
x3 = Series(d)
print x3

'''
a    1
b    2
c    3
d    4
dtype: int64
'''
```

[导入导出](./importOrExport.py)

```python
import pandas as pd
from pandas import Series, DataFrame

score =DataFrame(pd.read_excel('data.xlsx'))
score.to_excel('data1.xlsx')

print  score
```

[其他内容]('./findEmpty.py')

```python
# encoding:utf-8

import pandas as pd
from pandas import Series, DataFrame

data = {
  'Chinese': [66, 95, 93, 90, None],
  'English': [65, 85, 92, 88, 90],
  'Math': [30, 98, 96, 77, 90],
  'name':['xiaoguan','xiaozhang','xiaozhao','xiaoma','xiaohuang']
}

data_frame2 = DataFrame(data, index=['guan', 'zhang', 'zhao', 'ma', 'huang'])

# print data_frame2

print data_frame2.isnull()
print '\n'


print data_frame2.isnull().any()


##use apply function

data_frame2['name'] = data_frame2['name'].apply(str.upper)

print data_frame2



## 使用函数

def double_df(x):
  return 2*x

data_frame2['Chinese'] = data_frame2['Chinese'].apply(double_df)
print '\n'
print data_frame2

'''
       Chinese  English  Math       name
guan     132.0       65    30   XIAOGUAN
zhang    190.0       85    98  XIAOZHANG
zhao     186.0       92    96   XIAOZHAO
ma       180.0       88    77     XIAOMA
huang      NaN       90    90  XIAOHUANG
'''

## 使用更加复杂的函数

def plus(df,n,m):
  df['new1'] = (df['Chinese']+df['English'])*m
  df['new2'] = (df['Chinese']+df['English'])*n
  return df

print '\n'
df1 = data_frame2.apply(plus,axis=1,args=(2,3,))
print df1


```

## 常用统计函数

1. `count()` 统计个数 NaN 和 None 除外
2. `describe()` 一次性输出多个统计指标
3. `min()` 最小值
4. `max()` 最大值
5. `sum()` 求和
6. `mean()` 平均值
7. `median()` 中位数
8. `var()` 方差
9. `std()` 标准差
10. `argmin()` 统计最小值的索引位置
11. `argmax()` 统计最大值的索引位置
12. `idxmin()` 统计最小值的索引值
13. `idxmax()` 统计最大值的索引值

##　数据表合并

[合并]('combination.py')

```python
import pandas as pd
from pandas import Series, DataFrame

data = {
  'Chinese': [66, 95, 93, 90, 80],
  'English': [65, 85, 92, 88, 90],
  'Math': [30, 98, 96, 77, 90],
}

data_frame1  = DataFrame(data)

print data_frame1

'''
   Chinese  English  Math
0       66       65    30
1       95       85    98
2       93       92    96
3       90       88    77
4       80       90    90
'''

data_frame2 = DataFrame(data,index=['guan','zhang','zhao','ma','huang'])

print data_frame2

'''
       Chinese  English  Math
guan        66       65    30
zhang       95       85    98
zhao        93       92    96
ma          90       88    77
huang       80       90    90
'''
```
## SQL操作

[合并]('./pandasSql.py')

```python
# encoding=utf-8

import pandas as pd

from pandas import DataFrame

from pandasql import sqldf, load_meat, load_births

df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})

pysqldf = lambda sql: sqldf(sql, globals())

sql = "select * from df1 where name='ZhangFei'"

print pysqldf(sql)



```