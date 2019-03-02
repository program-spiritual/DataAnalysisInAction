# coding=utf-8
import pandas as pd

# 数据加载
train_data = pd.read_csv('./Titanic_Data/train.csv')
test_data = pd.read_csv('./Titanic_Data/test.csv')
# 数据探索
print(train_data.info())
'''output
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
PassengerId    891 non-null int64
Survived       891 non-null int64
Pclass         891 non-null int64
Name           891 non-null object
Sex            891 non-null object
Age            714 non-null float64
SibSp          891 non-null int64
Parch          891 non-null int64
Ticket         891 non-null object
Fare           891 non-null float64
Cabin          204 non-null object
Embarked       889 non-null object
dtypes: float64(2), int64(5), object(5)
memory usage: 83.6+ KB
None

'''
print('-' * 30)
print(train_data.describe())
'''output
       PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200

'''
print('-' * 30)
print(train_data.describe(include=['O']))
'''output
                          Name   Sex Ticket    Cabin Embarked
count                      891   891    891      204      889
unique                     891     2    681      147        3
top     Andrews, Mr. Thomas Jr  male   1601  B96 B98        S
freq                         1   577      7        4      644

'''
print('-' * 30)
print(train_data.head())
'''output
   PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S

'''
print('-' * 30)
print(train_data.tail())
'''output
    PassengerId  Survived  Pclass                                      Name     Sex   Age  SibSp  Parch      Ticket   Fare Cabin Embarked
886          887         0       2                     Montvila, Rev. Juozas    male  27.0      0      0      211536  13.00   NaN        S
887          888         1       1              Graham, Miss. Margaret Edith  female  19.0      0      0      112053  30.00   B42        S
888          889         0       3  Johnston, Miss. Catherine Helen "Carrie"  female   NaN      1      2  W./C. 6607  23.45   NaN        S
889          890         1       1                     Behr, Mr. Karl Howell    male  26.0      0      0      111369  30.00  C148        C
890          891         0       3                       Dooley, Mr. Patrick    male  32.0      0      0      370376   7.75   NaN        Q

'''
