import matplotlib.pyplot as plt
import pandas as pd


# 載入數據集
file_path = 'movie.csv'
movie_data = pd.read_csv(file_path)

# 顯示前五行的數據
print(movie_data.head())

content_rating_counts = movie_data["content_rating"].value_counts()
print(content_rating_counts)




content_rating_counts.plot(kind = "bar", figsize=(15,12), color="pink")

plt.title('Number of Movies by Content_rating')
plt.xlabel('content_rating')
plt.ylabel('Number of Movies')

plt.show()


