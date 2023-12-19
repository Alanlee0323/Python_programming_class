import matplotlib.pyplot as plt
import pandas as pd


# 載入數據集
file_path = 'movie.csv'
movie_data = pd.read_csv(file_path)

# 顯示前五行的數據
print(movie_data.head())

country = movie_data["country"]
print(country)
country_counts = country.value_counts()
print(country_counts)




country_counts.plot(kind = "bar", figsize=(30,25), color="green")

plt.title('Number of Movies by Country')
plt.xlabel('Country')
plt.ylabel('Number of Movies')

plt.show()


