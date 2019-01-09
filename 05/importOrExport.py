import pandas as pd
from pandas import Series, DataFrame

score =DataFrame(pd.read_excel('data.xlsx'))
score.to_excel('data1.xlsx')

print  score