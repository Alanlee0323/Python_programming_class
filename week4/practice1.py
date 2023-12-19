import pandas as pd

# 用字典建立一個 DataFrame
data = {'column1': [1, 2, 3, 4], 'column2': [5, 6, 7, 8], 'column3': [9, 10, 11, 12]}
df = pd.DataFrame(data)
print("選擇所有 dataframe")
print(df)

# 選擇所有row (沒有選擇column的時候會預設選擇所有的column)
print("選擇所有row (沒有選擇column的時候會預設選擇所有的column)")
print(df.iloc[:])

# 選擇前三row
print("選擇前三row")
print(df.iloc[:3])

# 選擇所有row 但只有第二column
print("選擇所有row 但只有第二column")
print(df.iloc[:, 1])

#選擇所有row ，但只有第一column 與 第三column
print("選擇所有row ，但只有第一column 與 第三column")
print(df.loc[:, ["column1", "column3"]])

#選擇 一 至 三 row ，但只有第一column 與 第三column
print("選擇 一 至 三 row ，但只有第一column 與 第三column")
print(df.loc[0: 2, ["column1", "column3"]])

#選擇 一 與 三 row ，有第一column 至 第三column
print("選擇 一 與 三 row ，有第一column 至 第三column")
print(df.loc[[0, 2], "column1" : "column3"])
