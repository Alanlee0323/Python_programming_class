import numpy as np

#製作一個陣列
data = np.array([9, 2, 3, 4, 10, 6, 7, 8, 1, 5])
print(type(data))
print("第一組的維度: ", data.ndim)

data2 = np.array([[9, 2, 3],[4, 10, 6],[7, 8, 1]])
print("第二組的維度: ", data2.ndim)

data3 = np.array([[[9, 2],[2, 3]],[[4, 10],[7, 8]]])
print("第三組的維度: ", data3.ndim)









#Min
print("Min: ", data.min())
print("Max: ", data.max())
print("Sum: ", data.sum())
print("Cum: ", data.cumsum())
print("Ratio:", data.cumsum()/data.sum())