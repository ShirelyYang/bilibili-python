# 制定有一个列表，列表里含有唯一一个只出现过一次的数字。写程序找出这个“独一无二”的数字
lis = [1, 1, 2, 4, 4, 3, 4, 4, 3]
for i in lis:
    if lis.count(i) == 1:
        print(i)
        pass
    pass
