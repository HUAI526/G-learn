import pandas as pd
data = pd.read_csv("scores3.csv", header=0, index_col=0)
print(data)
print(type(data))