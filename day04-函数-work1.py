# 写函数，接收n个数字，求这些参数数字的和
def sumFunc(*args):
    """
    处理接收的数据
    :param args:可变参数
    :return: 总和
    """
    sum = 0
    for i in args:
        sum += i
    return sum
# 调用函数
sum = sumFunc(1, 2, 3, 5, 7, 4, 7, 3, 5445, 33)
# format 格式化输出
print("sum={}".format(sum))