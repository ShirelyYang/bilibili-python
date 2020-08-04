# 等腰直角三角形
# i控制外层循环，即行数；j空格数；k星号
rows = int(input("请输入行数："))
i = j = k = 1
# print("等腰直角三角形：")
# while rows > 0:
#     while j <= rows:
#         print(" * ", end="")
#         j += 1
#         pass
#     print("\n")
#     j = 1
#     rows -= 1
#     pass

# 正直角等腰三角形
# print("正直角等腰三角形:")
# while i <= rows:
#     while j <= i:
#         print(" * ", end="")
#         j += 1
#         pass
#     print("\n")
#     j = 1
#     i += 1
#     pass


# 实心等边三角形
# i控制外层循环，即行数；j空格数；k星号

# print("实心等边三角形")
# while i <= rows:
#     for j in range(0, rows-i):
#         print("  ", end="")
#         j += 1
#         pass
#     for k in range(0, 2*i-1):
#         if k % 2 == 0:
#             print(" * ", end=" ")
#         k += 1
#         pass
#     print()
#     i += 1
#     pass

# 空心等边三角形
# i控制外层循环，即行数；j空格数；k星号
print("空心等边三角形")
lis = []
while i <= rows:
    j = 1
    k = 1
    while j < rows - i:
        print(" ", end=" ")
        j += 1
        pass
    while k <= rows:
        if k == 1:
            print("*", end=" ")
            pass
        elif k < rows:
            if k % 2 == 0:
                lis.append(k)
                if k in (lis[0], lis[len(lis)-1]):
                    print("*", end=" ")
        elif k == rows:
            print("*", end=" ")
            pass
        k += 1
    print()
    i += 1
    pass


# 等腰三角形
# while i <= rows:
#     while j < rows-i:
#         print(" ", end=" ")
#         j += 1
#         pass
#     while k <= 2*i-1:
#         print("*", end=" ")
#         k += 1
#         pass
#     j = 1
#     k = 1
#     print()
#     i += 1
#     pass
# 菱形（空心）
# i控制外层循环，即行数；j空格数；k星号