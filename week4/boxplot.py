import matplotlib.pyplot as plt
import pandas as pd

# 載入數據集
file_path = 'movie.csv'
movie_data = pd.read_csv(file_path)

# 顯示前五行的數據
print(movie_data.head())

title_year = movie_data["title_year"]
print(title_year)

title_year.plot(kind = "box", figsize = (13, 15), color = "skyblue")
plt.title('Title_year of Movies')
plt.ylabel('title_year')

plt.show()




