import pandas as pd
dic = {"A": [1, 2, 3], "B": [4, 5, 6], "C":[7, 8, 9]}
df = pd.DataFrame(dic)
print(df)

print(df.iloc[:, [0, 2]])
print(df.loc[[0, 2], "B":"C"])


ax = df.loc[[0, 2], "B":"C"].plot.bar(figsize=(16, 4))