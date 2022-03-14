#codeing: utf-8
import numpy as np
import pandas as pd
import datetime
from datetime import datetime, date
import matplotlib.pyplot as plt

sp500 = pd.read_csv("data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0,2,3,7])

omh = pd.read_csv("data/omh.csv")

np.random.seed(123456)

df = pd.DataFrame(np.random.rand(5,4),
                  columns=['A','B','C','D'])
print(df)

print(df*2)

s = df.iloc[0]

diff = df - s
print(diff)

diff2= s - df
print(diff2)

s2 = s[1:3]
s2['E'] = 0

print(df+s2)

subframe = df[1:4][['B','C']]

print(subframe)

print(df - subframe)

a_col = df['A']
print(df.sub(a_col, axis=0))

s = pd.Series(['a', 'a', 'b', 'c', np.NaN])

print(s.count())

print(s.unique())
print(s.nunique())
print(s.nunique(dropna=False))
print(omh[['MSFT', 'AAPL']].min())
print(omh[['MSFT', 'AAPL']].max())

print(omh[['MSFT', 'AAPL']].idmin())
print(omh[['MSFT', 'AAPL']].idmax())

print(omh.nsmallest(4, ['MSFT'])['MSFT'])
print(omh.nlargest(4, ['MSFT'])['MSFT'])
print(omh.MSFT.nsmallest(4))

print(pd.Series([1,2,3,4]).cumprod())
print(pd.Series([1,2,3,4]).cumsum())

print(omh.describe())
print(omh.MSFT.describe())

print(omh.MSFT.describe()['mean'])
s = pd.Series(['a', 'a', 'b', 'c', np.NaN])
print(s.describe())

print(omh.mean())

s = pd.Series([1,2,3,3,5])
print(s.mode())
s = pd.Series([1,2,3,3,5,1])
print(s.mode())

print(omh.var())

print(omh.std())

print(omh.MSFT.cov(omh.AAPL))
print(omh.MSFT.corr(omh.AAPL))

dist = np.random.normal(size = 10000)
print(dist)

print((dist.mean(), dist.std()))
bins = pd.cut(dist, 5)
print(bins)

print(bins.categories)

print(bins.codes)

print(pd.cut(dist, 5, right=False).categories)

np.random.seed(123456)
ages = np.random.randint(6,45,50)
print(ages)

ranges = [6,12,18,35,50]
agebins = pd.cut(ages, ranges)
print(agebins.describe())

ranges = [6,12,18,35,50]
labels = ['Youth', 'Young Adult', 'Adult', 'Middle Aged']
agebins = pd.cut(ages, ranges, labels=labels)
print(agebins.describe())

qbin = pd.qcut(dist, 5)
print(qbin.describe())

quantiles = [0,
             0.001,
             0.021,
             0.5-0.341,
             1.0-0.021,
             1.0-0.001,
             1.0]
qbin = pd.qcut(dist, quantiles)

print(qbin.describe())

np.random.seed(12345)
s = pd.Series(np.random.randn(5), index=list('abcde'))
print(s)

print(s.rank())
print(omh[['MSFT']].pct_change()[:5])

np.random.seed(123456)
s = pd.Series(np.random.randn(1000)).cumsum()
print(s[:5])
s[0:100].plot();
plt.show()

r = s.rolling(window=3)
print(r)

means = r.mean()
print(means[:7])

print(s[0:3].mean())

means[0:100].plot();