import pandas as pd

data1 = [{'Apple': 100, 'Banana': 20}, {'Apple': 70, 'Banana': 10, 'Grape': 20}]
df1 = pd.DataFrame(data1)
print(df1)


#使用二維數組
data2 = [[1, 2], [5, 10]]
Column_name = ['A', 'B']
df2 = pd.DataFrame(data2, columns=Column_name)
print(df2)


#合併成一個dataframe
df3 = pd.concat([df1, df2], axis=1)
print(df3)


