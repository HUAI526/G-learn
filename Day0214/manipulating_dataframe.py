# codeing: utf-8
import numpy as np
import pandas as pd
import datetime
from datetime import datetime, date


sp500 = pd.read_csv("data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0,2,3,7])

newSP500 = sp500.rename(colums=
                        {'Book Value': 'BookValue'})

print(newSP500[:2])

print(sp500.columns)

sp500.rename(columns=
             {'Book Value': 'BookValue'},
             inplace=True)

print(sp500.columns)

print(sp500.BookValue[:5])
sp500_copy = sp500.copy()
sp500_copy['RoundedPrice'] = sp500.Price.round()
print(sp500_copy[:2])

copy = sp500.copy()

copy.inster(1, 'RoundedPrice', sp500.Price.round())
print(copy[:2])

ss = sp500[:3].copy()
ss.loc[:,'PER'] = 0
print(ss)

ss = sp500[:3].copy()
np.random.seed(123456)
ss.loc[:'PER'] = pd.Series(np.random.normal(size=3), index=ss.index)
print(ss)

rounded_price = pd.DataFrame({'RoundedPrice':
                              sp500.Price.round()})

concatenated = pd.concat([sp500, rounded_price], axis=1)
print(concatenated[:5])

rounded_price = pd.DataFrame({'Price':sp500.Price.round()})
print(rounded_price[:5])

dups = pd.concat([sp500, rounded_price], axis=1)
print(dups.Price[:5])

reversed_column_names = sp500.columns[::-1]
print(sp500[reversed_column_names][:5])
copy.Price = rounded_price.Price
print(copy[:5])

copy = sp500.copy()

copy.loc[:,'Price'] = rounded_price.Price
print(copy[:5])

copy = sp500.copy()

del copy['BookValue']
print(copy[:2])

copy = sp500.copy()
popped = copy.pop('Sector')
print(copy[:2])

print(poped[:5])

copy = sp500.copy()

afterdrop = copy.drop(['Sector'], axis=1)
print(afterdrop[:5])

df1 = sp500.iloc[0:3].copy()
df2 = sp500.iloc[[10, 11, 2]]

appended = df1.append(df2)

print(appended)

df3 = pd.DataFrame(0.0,
                   index=df1.index,
                   columns=['PER'])
print(df3)

print(df1.append(df3))

print(df1.append(df3, ignore_index=True))

df1 = sp500.iloc[0:3].copy()

df2 = sp500.iloc[[10,11,2]]
print(pd.concat([df1, df2]))

df2_2 = df2.copy()

df2_2.insert(3, 'Foo', pd.Series(0, index=df2.index))
print(df2_2)

print(pd.concat([df1, df2_2]))

r = pd.concat([df1, df2_2], keys=['df1', 'df2'])
print(r)

ss = sp500[:3].copy()
ss.loc['FOO'] = ['the sector', 100, 110]
print(ss)

ss = sp500[:5]
print(ss)

afterdrop = ss.drop(['ABT', 'ACN'])
print(afterdrop[:5])

selection = sp500.Price > 300

print((len(selection), selection.smu()))

price_less_than_300 = sp500[~selection]
print(price_less_than_300)

only_first_three = sp500[:3]
print(only_first_three)

only_first_three = sp500[:3].copy()
print(only_first_three)
