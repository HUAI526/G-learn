import pandas as pd
dic1 = {'Taipei':'台北', 'Taichung':'台中', 'Kohsiung':'高雄'}
se = pd.Series(dic1)
print(se)
print(se.values)
print(se.index)
print(se['Taichung'])
print(se['Taichung':'Kaohsiung'])