# coding=UTF-8
# 文件的备份


def copy_file():
    # 接收用户输入的文件名
    old_file = input("请输入要备份的文件名：")
    file_list = old_file.split('.')
    # 构造新的文件名.加上备份的后缀
    new_file = file_list[0]+'_备份.'+file_list[1]
    old_f = open(old_file, 'r')     # 打开需要备份的文件
    new_f = open(new_file, 'w')     # 以写的模式去打开新文件，不存在则创建
    content = old_f.read()      # 将文件内容读取出来
    new_f.write(content)        # 将读取的内容写入到备份文件
    old_f.close()
    new_f.close()
    pass


def copy_big_file():
    # 接收用户输入的文件名
    old_file = input("请输入要备份的文件名：")
    file_list = old_file.split('.')
    # 构造新的文件名.加上备份的后缀
    new_file = file_list[0]+'_备份.'+file_list[1]
    try:
        # 监视要处理的逻辑
        with open(old_file, 'r') as old_f, open(new_file, 'a') as new_f:
            while True:
                content = old_f.read(1024)  # 一次性读取1024字符
                new_f.write(content)
                if len(content) < 1024:
                    break
        pass
    except Exception as msg:
        print(msg)
    pass

copy_file()
