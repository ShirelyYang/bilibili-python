import random
win = 0
while True:
    if win >= 3:
        print("你已经胜利3次，自动退出游戏！")
        break
    else:
        # 0:石头 1：剪刀 2：布
        person = int(input("请出拳[0][1][2]："))
        if person > 2:
            person = int(input("您出拳不符合规定，请重新输入[0][1][2]："))
        computer = random.randint(0, 2)
        print("电脑出拳：%d" % computer)
        if person == 0 and computer == 1 or person == 1 and computer == 2 or person == 2 and computer == 0:
            print("恭喜你赢了！")
            win += 1
        elif person == 0 and computer == 2 or person == 1 and computer == 0 or person == 2 and computer == 1:
            print("很遗憾，你输了……")
            pass
        else:
            print("不错哦，是平局~")
            pass

