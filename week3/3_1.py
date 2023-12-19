import numpy as np

# 建立一個包含0到99的NumPy數組
numbers = np.arange(100)

# 從數組中隨機選取5個數字
selected_numbers = np.random.choice(numbers, 5)

# 打印選取的數字
print(selected_numbers)
