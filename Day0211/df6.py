import pandas as pd
scores = {'國文':{'王曉明':65,'李曉玫':55,'陳大同':88,'林曉諭':45},
         '英文':{'王曉明':62,'李曉玫':21,'陳大同':48,'林曉諭':65},
         '數學':{'王曉明':88,'李曉玫':97,'陳大同':63,'林曉諭':78},
         '自然':{'王曉明':61,'李曉玫':85,'陳大同':32,'林曉諭':98},
         '社會':{'王曉明':64,'李曉玫':84,'陳大同':87,'林曉諭':51}}
df = pd.DataFrame(scores)   
print(df["自然"]) 
print(df[["國文", "數學", "自然"]])
print(df[df["國文"] >= 80])
print(df.values)
print(df.values[1])
print(df.values[1][2])

print(df.loc["王曉明", "社會"])
print(df.loc["李曉玫", ["社會", "國文"]])
print(df.loc[["王曉明","陳大同"], ["社會","數學"]])
print(df.loc["王曉明":"陳大同", "社會":"數學"])
print(df.loc["陳大同", :])
print(df.loc[:"王曉明", "社會":"數學"])
print(df.loc["王曉明", "社會":"數學"])
print(df.iloc[3,4])

df.iloc[0,[0,4]]
df.iloc[[0,1],[2,3]]
df.iloc[0:3,2:5]
df.iloc[2, :]
df.iloc[:2, 2:5]
df.iloc[1: , 2:5]
df.head(2)
df.tail(2)

