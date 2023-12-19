import matplotlib.pyplot as plt
import pandas as pd


# 載入數據集
file_path = 'movie.csv'
movie_data = pd.read_csv(file_path)

# 顯示前五行的數據
print(movie_data.head())

IMDB = movie_data["imdb_score"]
print(IMDB)


IMDB.hist(bins=10, figsize=(10, 5), color='purple')

plt.title('Histogram of Your Data')
plt.xlabel('IMDB_Value')
plt.ylabel('How_many_people_vote')

plt.show()
