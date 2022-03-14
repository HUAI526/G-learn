import pandas as pd
scores = {'國文':{'王曉明':65,'李曉玫':55,'陳大同':88,'林曉諭':45},
         '英文':{'王曉明':62,'李曉玫':21,'陳大同':48,'林曉諭':65},
         '數學':{'王曉明':88,'李曉玫':97,'陳大同':63,'林曉諭':78},
         '自然':{'王曉明':61,'李曉玫':85,'陳大同':32,'林曉諭':98},
         '社會':{'王曉明':64,'李曉玫':84,'陳大同':87,'林曉諭':51}}
df = pd.DataFrame(scores)   

#排序
print(df.sort_values(by='數學', ascending=False))
print(df.sort_index(axis=0))

#修改
df1 = df.loc["王曉明"]["數學"] = 90
print(df)
df2 = df.loc["王曉明", :] = 80
print(df)

#刪除
df.drop("王曉明")
df.drop(["數學", "自然"], axis=1)
df.drop(df.index[1:4])
df.drop(df.columns[1:4], axis=1)