import pandas as pd
import matplotlib.pyplot as plt

# 載入數據集
file_path = 'movie.csv'
movie_data = pd.read_csv(file_path)

# 顯示前五行的數據
print(movie_data.head())



# 使用 num_critic_for_reviews 作為 x 軸數據，director_facebook_likes 作為 y 軸數據
plt.figure(figsize=(15, 12)) # 設定圖形大小
plt.scatter(movie_data['num_critic_for_reviews'], movie_data['director_facebook_likes'], color="pink") # 繪製散點圖
 

# 添加標題和軸標籤
plt.title('Relationship between Number of Critic Reviews and Director Facebook Likes')
plt.xlabel('Number of Critic Reviews')
plt.ylabel('Director Facebook Likes')

# 顯示圖形
plt.show()
