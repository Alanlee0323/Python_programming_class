#讀取函式庫的標準格式
import numpy as np
# data = np.arange(9)  
# print(data)


#使用from功能引入 random() 這個功能的函式
from numpy import random 
data1 = np.array(np.arange(9))
print(random.choice(data1,3))