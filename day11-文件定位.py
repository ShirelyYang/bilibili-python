# coding=utf-8
# tell 返回指针当前所在的位置
# 对于中文来讲    每次读取到的一个汉子 实际上占用了 2个字符
# with open('../file/test.txt', 'r') as f:
#     print(f.read(3))
#     print(f.tell())

# truncate  可以对源文件进行截取操作
# fobjB = open('../file/test.txt', 'r')
# print(fobjB.read())
# fobjB.close()
# print("截取之后：")      # 保留前15个字符
#
# fobjA = open('../file/test.txt', 'r+')
# fobjA.truncate(15)
# print(fobjA.read())
# fobjA.close()


# seek()    可以控制光标所在的位置
with open('../file/test.txt', 'rb') as f:
    data = f.read(2)
    print(data.decode('gbk'))
    f.seek(-2, 1)   # 相当于光标又设置到了0的位置
    print(f.read(4).decode('gbk'))
    f.seek(-6, 2)   # 2表示光标在末尾处  -6往回移动了6个字符
    print(f.read(2).decode('gbk'))
    pass

# 用'r'这种模式打开文件，在文本文件中，如果没有使用二进制的选项打开文件，只允许从文件的开头计算相对位置，从文件尾部计算或者当前计算的话  就会引发异常
