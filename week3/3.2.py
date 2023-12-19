import pandas as pd

dataframe = pd.read_csv('C:\\Users\\alana\\Dropbox\\程式設計課\\week3\\Student_Health_Passport.csv')
# print(dataframe)

print(pd.read_csv('C:\\Users\\alana\\Dropbox\\程式設計課\\week3\\Student_Health_Passport.csv').head())
print("-------------------------------------------------------------------------")
print(dataframe.head())

print("-------------------------------------------------------------------------")
index = dataframe.index
print(index)

type = dataframe.dtypes
print(type)

print(dataframe.describe)

