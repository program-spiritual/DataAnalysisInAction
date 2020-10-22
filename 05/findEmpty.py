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
