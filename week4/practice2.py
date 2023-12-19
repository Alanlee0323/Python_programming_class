import pandas as pd
import matplotlib.pyplot as plt

# 創建一個簡單的 DataFrame
data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6]
})

# 繪製線形圖
data.plot(kind='line')
plt.show()

# 繪製直方圖
data.plot(kind='hist', alpha=0.5)
plt.show()

# 繪製箱形圖
data.plot(kind='box')
plt.show()

# 繪製散點圖，需要指定 x 和 y 軸的數據
data.plot(kind='scatter', x='A', y='B')
plt.show()
