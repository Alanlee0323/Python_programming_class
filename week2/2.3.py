# 創建一個空串列
Students = []


a = int(input("分數:"))

# 添加學生信息
Students.append({"姓名": "張三", "分數":a})
Students.append({"姓名": "李四", "分數": 90})
Students.append({"姓名": "王五", "分數": 78})

# 定義計算平均分數的函數
def 計算平均分數(學生串列):
    總分 = sum(學生["分數"] for 學生 in 學生串列)
    平均分 = 總分 / len(學生串列)
    return 平均分

# 打印結果
print("班級平均分數是:", 計算平均分數(Students))
