#Data type (資料種類)
price = 10
pen = 0.38
rain = True
name = "Parker"
print(type(price)) #印出Price的資料類型
print(type(pen))   #印出pen的資料類型
print(type(rain))  #印出rain的資料類型
print(type(name))  #印出name的資料類型
print(price, pen, rain, name)

#同種資列類型的變數可以做運算
name = "Alan "
bev = "is "
action = "coding "
price = 10
print(name + bev + action)
print(price + name) #不同種資料類型相加會出現錯誤