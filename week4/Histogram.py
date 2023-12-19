import matplotlib.pyplot as plt
import pandas as pd

# Load the data
file_path = 'movie.csv'
movie_data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(movie_data.head())



# 繪製 IMDb 評分的直方圖
plt.figure(figsize=(10, 6))
plt.hist(movie_data['imdb_score'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('IMDb Score Distribution')
plt.xlabel('IMDb Score')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()

# 繪製電影片長的箱形圖
plt.figure(figsize=(10, 6))
plt.boxplot(movie_data['duration'].dropna())
plt.title('Movie Duration Boxplot')
plt.ylabel('Minutes')
plt.grid(axis='y', alpha=0.75)
plt.show()

# 計算並繪製不同 content_rating 的電影數量的條形圖
content_rating_counts = movie_data['content_rating'].value_counts()
plt.figure(figsize=(10, 6))
content_rating_counts.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Number of Movies by Content Rating')
plt.xlabel('Content Rating')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.75)
plt.show()

# 繪製預算與全球票房的散點圖
plt.figure(figsize=(10, 6))
plt.scatter(movie_data['budget'], movie_data['gross'], alpha=0.5, color='purple')
plt.title('Budget vs. Gross Worldwide')
plt.xlabel('Budget')
plt.ylabel('Gross Worldwide')
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e3, 1e9)  # Set the limits of x-axis
plt.ylim(1e3, 1e9)  # Set the limits of y-axis
plt.show()


