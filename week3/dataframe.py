import pandas as pd
Student_Health_Passport = pd.read_csv('C:\\Users\\alana\\Dropbox\\程式設計課\\week3\\Student_Health_Passport.csv')

columns = Student_Health_Passport.columns
print(columns)

Age = Student_Health_Passport["Age"]
print(Age)

Age1 = Student_Health_Passport.Age
print(Age1)

Age2 = Student_Health_Passport.loc[2, 'Age']
print(Age2)

Age3 = Student_Health_Passport.iloc[:, 2]
print(Age3)