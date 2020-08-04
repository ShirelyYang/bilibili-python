# 写函数， 找出传入的列表或元组的奇位数对应的元素，并返回一个新的列表
def index(lis):
    """
    处理列表数据
    :param lis:接收的是一个列表或者元组
    :return:返回新的列表
    """
    lisNew = []
    for i in range(len(lis)):
        if i % 2 == 0:
            lisNew.append(lis[i])
            pass
    return lisNew

lis = [123, "Amy", 'ant a', "大宝贝儿", 23432, "2岁半", "hsfdhjksfhk", "学轮滑"]
opt = index(lis)
opt2 = index(list(range(20)))
print(opt)
print(opt2)