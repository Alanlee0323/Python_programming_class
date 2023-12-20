import matplotlib.pyplot as plt
import pandas as pd


# 載入數據集
file_path = 'C:\\Users\\alana\\Dropbox\\Github\\Python_programming_class\\week4\\movie.csv'
movie_data = pd.read_csv(file_path)

# 顯示前五行的數據
print(movie_data.head())

num_voted_users = movie_data["num_voted_users"]
print(num_voted_users)


num_voted_users.hist(bins=15, figsize=(20, 8), color='blue')

plt.title('Histogram')
plt.xlabel('num_voted_users')
plt.ylabel('data')

plt.show()
