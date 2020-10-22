# encoding=utf-8
import pandas as pd
from pandas import Series, DataFrame

df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
df2 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data1': range(5)})

##　 基于指定列进行连接

df3 = pd.merge(df1, df2, on='name')

print df3
print '\n'
## inner 连接

df4 = pd.merge(df1, df2, how='inner')

print df4
print '\n'

## 左连接

df5 = pd.merge(df1, df2, how='left')
print df5
print '\n'

## 右连接

df6 = pd.merge(df1, df2, how='right')
print df6
print '\n'

## 外连接

df7 = pd.merge(df1, df2, how='outer')
print df7
print '\n'

##



