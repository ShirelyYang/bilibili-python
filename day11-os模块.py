# coding=utf-8
import os
import shutil
# os.rename('../file/test.txt', '../file/testNew.txt')
# os.remove('../file/test1.txt')  # 删除文件  前提是文件必须存在
# os.mkdir('../file/test')      # 创建文件夹 创建一级目录
# os.rmdir('../file/test')        # 删除文件夹 前提是文件夹必须存在
# os.mkdir('d:/Python编程/sub核心')       # 不允许创建多级目录
# os.makedirs('d:/Python编程/sub核心/三级sub')    # 允许创建多级目录
# os.rmdir('d:/Python编程/sub核心/三级sub')     # rmdir 只能删除空目录
# 如果要删除非空目录 就需要调用shutil模块
# shutil.rmtree('d:/Python编程')    # 路径只填写想删除的根目录即可
# 获取当前的目录
# print(os.getcwd())
# 路径的拼接
# print(os.path)
# print(os.path.join(os.getcwd(), 'file'))
# 获取python中的目录列表
# listRs = os.listdir('d:/')    # 老版本的用法
# for i in range(len(listRs)):
#     if i % 10 == 0:
#         print("\n")
#         pass
#     print(listRs[i], end=" ")
# 使用现代版的写法
# scandir 和 with 一起来使用  这样的话  上下文管理器会在迭代器遍历完成后，自动的去释放资源
# with os.scandir('d:/') as entries:
#     for entry in entries:
#         print(entry.name)
basePath = 'd:/'
for entry in os.listdir(basePath):
    if os.path.isfile(os.path.join(basePath, entry)):
        print(entry)
        pass