import random
# 0:拳头 1：见剪刀 2：布
flag = True
while flag != "N" or flag != "n":
    inp = int(input("请出拳[0:拳头 1：见剪刀 2：布]："))
    while inp not in range(0, 3):
       inp = int(input("输入错误！请重新输入[0:拳头 1：见剪刀 2：布]："))
       continue
    computer = random.randint(0, 2)
    print("电脑出拳：%d" % computer)
    if inp == 0 and computer == 1 or inp == 1 and computer == 2 or inp == 2 and computer == 0:
        print("恭喜你赢了！")
        pass
    elif inp == 0 and computer == 2 or inp == 1 and computer == 0 or inp == 2 and computer == 1:
        print("对不起，你输了……")
        pass
    else:
        print("平局哦~")
        pass
    flag = input("是否继续？Y继续，N结束:")
    if flag == "N":
        print("游戏结束！")
        pass
    pass
