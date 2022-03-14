import numpy as np
import pandas as pd
import datetime
from datetime import datetime, date
import matplotlib.pyplot as plt

print(pd.DataFrame(np.arange(1,6)))

df = pd.DataFrame(np.array([[10,11], [20,21]]))
print(df)

print(df.columns)

df = pd.DataFrame(np.array([[70,71], [90,91]]),
                  columns=['Missoula', 'Philadelphia'])
print(df)

print(len(df))

print(df.shape)

temps_missoula = [70,71]
temps_philly = [90,91]
temperatures = {'Missoula':temps_missoula,
                'Philadelphia':temps_philly}
print(pd.DataFrame(temperatures))

temps_at_time0 = pd.Series([70,90])
temps_at_time1 = pd.Series([71,91])
df = pd.DataFrame([temps_at_time0, temps_at_time1])
print(df)

df = pd.DataFrame([temps_at_time0, temps_at_time1])
df.columns = ['Missoula', 'Philadelphia']

print(df)
temps_mso_series = pd.Series(temps_missoula)
temps_ph1_series = pd.Series(temps_philly)
df = pd.DataFrame({'Missoula':temps_mso_series,
                   "Philadelphia":temps_ph1_series})
print(df)
temps_nyc_series = pd.Series([85,87], index=[1,2])
df = pd.DataFrame({'Missoula':temps_mso_series,
                   "Philadelphia":temps_ph1_series,
                   'New York':temps_nyc_series})
print(df)

sp500 = pd.read_csv("data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0,2,3,7])

print(len(sp500))
print(sp500.size)
print(sp500.index)
print(sp500.columns)
print(sp500['Sector'].head())
print(type(sp500['Sector']))

print(sp500[['Price', 'Book Value']].head())

print(type(sp500[['Price', 'Book Value']]))
print(sp500.Price)
print(sp500.loc['MMM'])
print(sp500.loc[['MMM', 'MSFT']])
print(sp500.iloc[[0,2]])

i1 = sp500.index.get_loc('MMM')
i2 = sp500.index.get_loc('A')
print(i1,i2)

print (sp500.iloc[[i1,i2]])

print(sp500.iat[0,1])

print(sp500[:5])
print(sp500['ABT':'ACN'])

print(sp500.Price < 100)

print(sp500[sp500.Price < 100])

r = sp500[(sp500.Price < 10) &
          (sp500.Price > 6)] ['Price']
          
print(r)

r = sp500[(sp500.Sector == 'Health Care') &
          (sp500.Price > 100.00)] [['Price', 'Sector']]
print(r)
    
print(sp500.loc[['ABT', 'ZTS']][['Sector', 'Price']])    