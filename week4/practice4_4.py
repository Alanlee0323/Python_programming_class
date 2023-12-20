import matplotlib.pyplot as plt
import pandas as pd

# 載入數據集
file_path = 'C:\\Users\\alana\\Dropbox\\Github\\Python_programming_class\\week4\\movie.csv'
movie_data = pd.read_csv(file_path)

# 顯示前五行的數據
print(movie_data.head())

imdb_score = movie_data["imdb_score"]
print(imdb_score)

imdb_score.plot(kind = "box", figsize = (12, 14), color = "blue")
plt.title('Boxplot')
plt.ylabel('imdb_score')

plt.show()




