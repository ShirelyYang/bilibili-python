# 决战紫禁之巅有两个人物，西门吹雪以及叶孤城
# 属性：
# name 玩家的名字
# blood 玩家血量
#
# 方法：
# tong() 捅对方一刀,对方掉血10滴
# kanren() 砍对方一刀，对方掉血15滴
# chiyao() 吃一颗药，补血10滴
# __str__ 打印玩家状态。

import time
import random
class Hero:
    def __init__(self, name, blood):
        """
        初始化属性
        :param name: 玩家的名字
        :param blood: 玩家的血量
        :return:
        """
        self.name = name
        self.blood = blood
        pass
    def tong(self, opp):
        """
        捅对方一刀
        :param opp: 对方
        :return:
        """
        opp.blood -= 10
        info = "%s 捅了 %s 一刀" % (self.name, opp.name)
        print(info)
        pass
    def kanren(self, opp):
        """
        砍对方一刀，对方掉血15滴
        :param opp: 对方
        :return:
        """
        opp.blood -= 15
        info = "%s 砍了 %s 一刀" % (self.name, opp.name)
        print(info)
        pass
    def chiyao(self):
        """
        吃一颗药，补血10滴
        :return:
        """
        self.blood += 10
        info = "%s 吃了一颗补血药，加了10滴血" % self.name
        print(info)
        pass
    def __str__(self):
        return "%s 还剩 %s 滴血" % (self.name, self.blood)
    pass
xmc = Hero("西门吹雪", 100)
ygc = Hero("叶孤城", 100)
while True:
    i = random.randint(1, 6)
    if i == 1:
        xmc.tong(ygc)
        pass
    elif i == 2:
        xmc.kanren(ygc)
        pass
    elif i == 3:
        xmc.chiyao()
        pass
    elif i == 4:
        ygc.tong(xmc)
        pass
    elif i == 5:
        ygc.kanren(xmc)
        pass
    else:
        ygc.chiyao()
        pass
    if xmc.blood <= 0 or ygc.blood <= 0:
        break
        pass
    print(xmc)
    print(ygc)
    print("*" * 20)
    time.sleep(2)
    pass
print(xmc)
print(ygc)
print("游戏结束！")