flag = "y"
while flag in ["Y", "y"]:
    high = float(input("请输入身高："))
    weight = float(input("请输入体重："))
    BMI = weight / (high ** 2)
    print("BMI=%d" % BMI)
    if BMI > 32:
        print("严重肥胖")
        pass
    elif BMI > 28:
        print("肥胖")
        pass
    elif BMI > 25:
        print("过重")
        pass
    elif BMI > 18.5:
        print("正常")
        pass
    else:
        print("过轻")
        pass
    flag = input("是否继续？Y或y继续，任意按键退出：")
else:
    print("您已退出……")