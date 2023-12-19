import pandas as pd
dataframe = pd.read_csv('C:\\Users\\alana\\Dropbox\\程式設計課\\week3\\Student_Health_Passport.csv')


print(dataframe)


index = dataframe.index
columns = dataframe.columns
data = dataframe.values

print("Index為:\n", index)
print("columns為:\n", columns)
print("data為:\n", data)

print(type(index))
print(type(columns))
print(type(data))


type = dataframe.dtypes
print(type)