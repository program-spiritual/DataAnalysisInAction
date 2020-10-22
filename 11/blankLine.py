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
