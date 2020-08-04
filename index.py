#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2020-06-02 11:13:32
# @Last Modified by:   anchen
# @Last Modified time: 2020-06-02 11:16:22
# name = ['小明', '胖虎', '小叮当']
# for i in range(0, len(name)):
#     # % 占位符，后边加数据类型
#     print("我是%s，我来自一班" % name[i])

name = "yang"
# print("姓名首字母转换大写%s" % name.capitalize())
# 复制后，内存地址不变
# a = name
# print("name 的内存地址%d" % id(name))
# print("a 的内存地址%d" % id(a))

data = 'Shirely_yang'
# find函数 可以查找目标在序列中的位置，如果没找到，则返回-1
# print(data.find("yang"))

lis = [1, 2, 3, "你好"]
# print(type(lis))
# print(len(lis))
# 查找
listA = ["abcd", 785, 12.23, "qiuzhi", True]
# 输出完整的列表
# print("输出完整的列表:", listA)
# # 输出第一个元素
# print("输出第一个元素:", listA[0])
# # 输出第二和第三个元素
# print("输出第二和第三个元素:", listA[1:3])
# # 输出第三个元素开始之后的所有数据
# print("输出第三个元素看开始之后的所有数据:", listA[2:])
# # 倒序输出
# print("倒序输出:", listA[::-1])
# # 连续2次输出
# print("连续2次输出:", listA*2)
# print("-------------------增加--------------------")
# # 增加数据
# listA.append("yang")
# print("增加数据:", listA[len(listA)-1])
# # 增加列表
# listA.append(["Amy", "Femail", 2.5, "轮滑"])
# print("增加列表:", listA[len(listA)-1])
# print(listA)
# # 插入,2个参数，需指定位置，insert(index,object)
# listA.insert(6, "我要学习测试开发")
# print("插入后的列表：", listA)
# # 批量添加
# rsData = list(range(10))
# listA.extend(rsData)
# print("批量添加后的列表：", listA)
# print("-------------------修改-------------------------")
# print("----------------------删除list数据项--------------------------------")
# listB = list(range(10, 50))
# print("删除前列表：", listB)
# # 删除列表中某个元素
# # del listB[0]
# # 批量删除
# # del listB[1:3]
# # remove 移除指定的元素(具体值）  remove(value)
# # listB.remove(20)
# # pop 移除指定的元素（索引值） 默认删除最后一个元素   pop(index)
# listB.pop(1)
# print("删除后列表：", listB)
# # 批量删除



# print("-----------------元组-------------------------")


# print("-----------------------函数的学习---------------------------")
# def output(name, high, weight, hobby, pro):
#     """
#     备注信息
#     :param name:
#     :param high:
#     :param weight:
#     :param hobby:
#     :param pro:
#     :return:
#     """
#     print("%s的身高是：%0.2fcm" % (name, high))
#     print("%s的体重是：%0.2fkg" % (name, weight))
#     print("%s的爱好是：%s" % (name, hobby))
#     print("%s的专业是：%s" % (name, pro))
#     return
#
# name = input("请输入姓名：")
# high = float(input("请输入身高："))
# weight = float(input("请输入体重："))
# hobby = input("请输入爱好：")
# pro = input("请输入专业：")
# output(name, high, weight, hobby, pro)



# 匿名函数 lambda
# resut = lambda a, b, c: a*b*c
# age = 15
# # print("可以参军" if age > 18 else "继续上学")
# # funcTest = lambda x, y: x if x > y else y
# # print(funcTest(12, 2))
# # 直接调用
# rs = (lambda x, y: x if x > y else y)(12, 24)
# print(rs)

# 递归函数
# 求5！
# 循环的方式
# def facorial(n):
#     result = 1
#     i = 1
#     while i <= n:
#         result *= i
#         i += 1
#     return result
# 递归方式
# def facorial(n):
#     """
#     递归实现
#     :param n: 阶乘参数
#     :return:
#     """
#     if n == 1:
#         return 1
#     return n*facorial(n-1)
# print(facorial(5))

# 递归案例 模拟实现 树形结构的遍历
# import os # 引入文件模块
# def findFile(file_path):
#     listRs = os.listdir(file_path)  # 得到该路径下所有文件夹
#     for fileItem in listRs:
#         full_path = os.path.join(file_path, fileItem)   # 获取完整的文件路径
#         if os.path.isdir(full_path):    # 判断是否是文件夹
#             findFile(fileItem)  # 如果是一个文件夹，再次去递归
#             pass
#         else:
#             print(fileItem)
#             pass
#         pass
#     else:
#         return
#     pass
# findFile("D:\workspace-Python\\求知讲堂\\file\Day03\代码\Python-DataType")

# 类型转换函数
# bin() 转换为二进制
# print(bin(10))
# hex() 转换十六进制
# print(hex(23))
# 元组转换为列表 lsit()
# 列表转换为元组 tuple()
# 字典操作 dict()


# 序列操作函数：str、list、tuple
# all() 对象中的元素除了是 0、空、、FALSE 外都算是TRUE
# any() 参数全部为FALSE，则返回FALSE，如果有一个TRUE，则返回TRUE
# print(any((3, 4, 0)))  # True
# sorted() 对所有可迭代的对象进行排序操作
# sort 与 sorted 区别：
# 1、sort是应用在list上的方法，sorted可以对所有可迭代的对象进行排序操作
# 2、list的sort方法返回的是对已经存在的列表进行操作，而sorted返回的是一个新的list，而不是在原来的基础上进行操作
# sort()
# listA = [9, 2, 5, 3, 8, 7]
# listB = ['123', 'Google', 'Runoob', 'Taobao', 'Facebook']
# listA.sort()    # 升序排列
# listA.sort(reverse=True)    # 降序列排列
# listB.sort()
# print(listA)
# print(listB)

# sorted()
# lis = [2, 45, 1, 67, 23, 10]
# print("sorted排序之前：{}".format(lis))
# # listNew = sorted(lis)    # 升序
# lisNew = sorted(lis, reverse=True)  # 降序
# print("sorted排序之后：", lisNew)

# tupleA = (2, 45, 1, 67, 23, 10)
# print("sorted排序之前：{}".format(tupleA))
# tupleB = sorted(tupleA)
# print("sorted排序之后：", tuple(tupleB))

# zip() 用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回有这些元组组成的列表
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用*号操作符，可以将元组解压为列表
# s1 = ["a", "b", "c"]
# s2 = ["你", "我", "他"]
# s3 = ["你", "我", "他", "哈哈", "嘿嘿", "呵呵"]
# # print(list(zip(s1)))  # 压缩一个数据
# ziplist = zip(s1, s2, s3)
# print(list(ziplist))

# def printBookInfo():
#     books = []  # 存储所有的图书信息
#     id = input("请输入编号：每个项以空格分隔：")
#     bookeNanme = input("请输入书名：每个项以空格分隔：")
#     bookPos = input("请输入位置：每个项以空格分隔：")
#     idList = id.split(" ")
#     nameList = bookeNanme.split(" ")
#     posList = bookPos.split(" ")
#     bookInfo = zip(idList, nameList, posList)
#     for bookItem in bookInfo:
#         '''
#         遍历图书信息进行存储
#         '''
#         dictInfo = {"编号": bookItem[0], "书名": bookItem[1], "位置": bookItem[2]}
#         books.append(dictInfo)  #将字典对象添加到list容器中
#         pass
#     for item in books:
#         print(item)
#     # print(list(bookInfo))
#     pass
# printBookInfo()

# enumerate 用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，一般用在for 循环当中
# listObj = ["a", "b", "c"]
# for item in enumerate(listObj):
#     print(item)
#     pass
# dictObj = {}
# dictObj["name"] = "Amy"
# dictObj["hobby"] = "Roller skating"
# dictObj["Pro"] = "kindergarten"
# print(dictObj)
# for item in enumerate(dictObj):
#     print(item)
#     print(dictObj[item[1]])
#     pass

# 集合操作函数
# set 不支持索引和切片，是一个无需的且不重复的容器
# 类似于字典 但是只有key， 没有value
# 创建集合
set1 = {32, 12, 34}
set2 = {12, 43, 23}
# print(type(set1))
# 添加
set1.add("python")
# print(set1)
# 清空
# set1.clear()
# print(set1)
# 差集 两个集合的差集，a中存在，不中不存在
# set3 = set1.difference(set2)
# print(set3)
# set4 = set1 - set2
# print(set4)
# 交集
# set3 = set1.intersection(set2)
# print(set3)
# set4 = set1 & set2
# print(set4)
# 并集
# set5 = set1.union(set2)
# print(set5)
# set6 = set1 | set2
# print(set6)
# pop 从集合中拿数据，并且同时删除
# print(set1)
# print(set1.pop())
# print(set1)

# discard 移除指定元素
# print(set1)
# print(set1.discard(34))
# print(set1)
# update 更新
# set1.update(set2)
# print(set1)
# print(set2)
# print(set1)

# 面向对象
# 定义类和对象
# 类结构 类名 属性 方法
# class Person:
#     """
#     对应人的特征
#     """
#     name = "小米"
#     age = 18
#     def eat(self):
#         print("吃饭")
#         pass
#     pass
# # 创建对象  对象名=类名()
# xm = Person()
# xm.eat()    # 调用函数
# print("{}的年龄是：{}".format(xm.name, xm.age))
# __init__()方法
# class People:
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         pass
#     pass
# zp = People("帐篷", "男", 20)
# print(zp.name, zp.age)

# self
class Person:
    """
    定义类
    """
    def eat(self):
        """
        实例方法
        :return:
        """
        print("self=%s" % id(self))
        pass
    pass
xw = Person()
print("xw=%s" % id(xw))
xw.eat()