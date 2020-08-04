# name = "老夫子"
# QQ = 666666
# phone = 150241935030
# address = "广州市白云区"

# input
name = input("请输入您的姓名：")
QQ = input("请输入您的QQ：")
phone = input("请输入您的电话：")
addr = input("请输入您的地址：")

print("===================\n姓名：%s\nQQ：%s\n电话：%s\n地址：%s\n===================" % (name, QQ, phone, addr))
# 格式化输出,{}占坑，format里只填写变量名，不用在乎类型
# print("姓名：{}，年龄：{}".format(name, age))