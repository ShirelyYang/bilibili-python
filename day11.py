# 文件的操作
# 打开文件  open()
# 默认的编码是gbk 这个是中文编码，最好的习惯就是我们在打开一个文件的时候给它指定一个编码类型
# fobj = open("../file/test.txt", 'w', encoding="utf-8")
# # 开始操作 读/写操作
# fobj.write('在苍茫的大海上')
# fobj.write('狂风卷积着乌云')
# fobj.close()

# 以二进制的形式去写数据
# fobj1 = open("../file/test1.txt", 'wb')       # str --> bytes
# fobj1.write('在乌云和大海之间'.encode('utf-8'))
# fobj1.close()
# fobj1 = open("../file/test.txt", 'a', encoding='utf-8')       # 用于追加数据
# fobj1.write('在乌云和大海之间\r\n')
# fobj1.write('海燕像黑色的闪电\r\n')
# fobj1.close()
# fobj = open('../file/test.txt', 'w+')
# fobj.write('在苍茫的大海上\n')
# fobj.write('狂风卷积着乌云\n')
# fobj.write('在乌云和大海之间\n')
# fobj.write('海燕像黑色的闪电\n')

# 读数据操作
# f = open('../file/test.txt', 'rb')
# data = f.read()
# print(data.decode('gbk'))     # 读取所有的数据
# # print(f.read(12))
# # print(f.read())
# # print(f.readline())     # 读一行
# # print(f.readline())
# # print(f.readlines(2))
# f.close()

# with 上下文管理对象
# 优点    自动释放打开关联的对象
with open('../file/test.txt', 'a') as f:
    # print(f.read())
    f.write('我觉得python非常的好学\n')
    pass

# 小结
# 文件读写的集中操作方式
# read：r r+ rb rb+
# r r+ 只读  适用普通读取场景
# rb rb+ 适用于 文件、图片、视频、音频 这样的文件读取
# write w w+ wb wb+ a ab
# w wb+ w+ 每次都会去创建文件
# 二进制读写的时候  要注意编码问题 默认情况下   我们写入文件的编码是gbk
# a ab a+   在原有的文件的基础之上去【文件指针的末尾】追加，并不会每次的都去创建一个新的文件

