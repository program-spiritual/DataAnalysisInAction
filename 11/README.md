## 数据质量的准则
 1. 完整性
  - 是否存在空值 统计字段是否完善
 2. 全面性
  - 通过常识判断该列是否有问题
 3. 合法性
  - 类型 内容 大小 合法性
 4. 唯一性
  - 记录是否重复 行列数据不应重复

## 完整性

- [缺失值](./missingValue.py)

```python
# enciding=utf-8

import pandas as pd
from pandas import Series, DataFrame

data = {
  'Chinese': [66, 95, 93, 90, None],
  'English': [65, 85, 92, 88, 90],
  'Math': [30, 98, 96, 77, 90],
  'name':['xiaoguan','xiaozhang','xiaozhao','xiaoma','xiaohuang']
}

data_frame2 = DataFrame(data, index=['guan', 'zhang', 'zhao', 'ma', 'huang'])

data_frame2['Chinese'].fillna(data_frame2['Chinese'].mean(),inplace=True)

print data_frame2

'''
       Chinese  English  Math       name
guan      66.0       65    30   xiaoguan
zhang     95.0       85    98  xiaozhang
zhao      93.0       92    96   xiaozhao
ma        90.0       88    77     xiaoma
huang     86.0       90    90  xiaohuang
'''
```

- [空行](./blankLine.py)

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

data_frame2.dropna(how='all',inplace=True)

print data_frame2


## 全面性
  - 单位不统一 转换单位

## 合理性
  - 删除非ASCII字符

## 唯一性
  - 将一列的多个参数拆分
  - 删除重复数据行
