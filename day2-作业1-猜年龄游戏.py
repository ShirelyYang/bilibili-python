import random
year = random.randint(20, 30)
flag = "Y"
while flag == "Y" or flag == "y":
    for i in range(3):
        inp = int(input("请输入年龄："))
        if year == inp:
            print("恭喜您猜对了！")
            print("即将退出游戏……")
            flag = "n"
            break
        elif year > inp:
            print("猜小了~")
        else:
            print("猜大了……")
        pass
    else:
        flag = input("是否还想继续玩？输入Y或y继续，输入N或n退出游戏：")
        if flag == "N" or flag == 'n':
            print("游戏已结束……")
        else:
            flag = input("输入错误！请输入Y/N 或 y/n，谢谢配合:")
        pass
