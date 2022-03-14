import pandas as pd
from _operator import index
df = pd.DataFrame([[65,54,88,55,33],
                  [85,47,98,54,44],
                  [78,22,33,64,94],
                  [84,51,23,49,77]],
                  index=['王曉明','李曉玫','陳大同','林曉諭'],
                  columns=['國文','英文','數學','自然','社會'])
print(df)