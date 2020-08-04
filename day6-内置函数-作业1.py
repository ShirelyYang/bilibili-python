# 求三组连续自然数的和： 求出 1 到 10、20到30和35到45的三个和
# list1 = list(range(11))
# list2 = list(range(20, 31))
# list3 = list(range(35, 46))
# print(sum(list1))
# print(sum(list2))
# print(sum(list3))

# def sumRange(lis):
#     res = sum(lis)
#     print(res)
#     return res
# list1 = list(range(11))
# list2 = list(range(20, 31))
# list3 = list(range(35, 46))
# sumRange(list1)
# sumRange(list2)
# sumRange(list3)


# 老师范例
def sumRang(m, n):
    '''
    求从m到n的连续自然数的和
    :param m:开始值 int
    :param n:结束值 int
    :return:
    '''
    return sum(range(m, n+1))
    pass
print(sumRang(1, 10))
print(sumRang(20, 30))
print(sumRang(35, 45))