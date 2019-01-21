# encoding=utf-8

import pandas as pd

from pandas import DataFrame

from pandasql import sqldf, load_meat, load_births

df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})

pysqldf = lambda sql: sqldf(sql, globals())

sql = "select * from df1 where name='ZhangFei'"

print pysqldf(sql)

'''output
   data1      name
0      0  ZhangFei
'''
