#製作串列
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(data_list)
print(type(data_list))



print(data_list[0])
print(data_list[2])
print('元素數量',len(data_list))

data_list.append(11)
data_list.append("haha")
data_list.append(True)
print(data_list)

print('元素數量',len(data_list))



# data_list.remove(11)
# print(data_list)
# data_list.remove("haha")
# print(data_list)
# data_list.remove(True)
# print(data_list)