# 定義串列
words = ["apple", "book", "cat", "dog", "elephant"]
# 創建一個新的空串列用於儲存長度大於3的單詞
long_words = []

# 遍歷串列中的每個單詞
for word in words:
    # 檢查單詞的長度是否大於3
    if len(word) > 3:
        # 如果是，則添加到long_words串列中
        long_words.append(word)

# 輸出結果
print(long_words)
