# 100 个和尚吃100个馒头，大和尚一人吃3个馒头，小和尚三人吃1个馒头。请问大小和尚各多少人？
total = 100
steamBrad = 100
# total = monk + littleMonk
# steamBrad = 3*monk + littleMonk/3
# for i in range(1, steamBrad+1):
#     if i % 3 == 0:
#         monk = i/3
#         littleMonk = total-monk
#         if littleMonk/3 == steamBrad-i:
#             print("大和尚：%d,小和尚：%d" % (monk, littleMonk))
#             pass
#         pass
#     pass
# pass


# 老师范例
def PersonCount():
    """
    计算各有多少个和尚
    假设大和尚a，小和尚就是100-a
    :return:
    """
    for a in range(1, 100):
        if a*3+(100-a)/3 == 100:
            return (a, 100-a)
        pass
    pass
resObj = PersonCount()
print("大和尚{}人 小和尚{}人".format(resObj[0], resObj[1]))