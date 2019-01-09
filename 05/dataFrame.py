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