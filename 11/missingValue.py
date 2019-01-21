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