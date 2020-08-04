import pygame
import random
import time
from pygame.locals import *

"""
1.实现飞机的显示   并且可以控制飞机的移动【面向对象】
"""


class HeroPlane(object):
    def __init__(self, screen):
        """

        :param screen: 主窗体对象
        """
        # 飞机的默认位置
        self.x = 150
        self.y = 450
        # 设置要显示内容的窗口
        self.screen = screen
        # 生产飞机的图片对象
        self.imageName = "./img/飞机2.png"
        self.image = pygame.image.load(self.imageName)
        # 用来存放子弹的列表
        self.bullets_list = []
        pass

    def moveleft(self):
        """
        左移动
        :return:
        """
        if self.x > 0:
            self.x -= 10
        pass

    def moveright(self):
        """
        右移动
         :return:
        """
        if self.x < 294:
            self.x += 10
        pass

    def display(self):
        """
        飞机在主屏幕上的显示
        :return:
        """
        self.screen.blit(self.image, (self.x, self.y))
        # 完善子弹的展示逻辑
        needDelItemList = []
        for item in self.bullets_list:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass
        # 重新遍历一下[jn bj
        for i in needDelItemList:
            self.bullets_list.remove(i)
            pass
        for bullet in self.bullets_list:
            bullet.display()    # 显示子弹的位置
            bullet.move()       # 让这个子弹进行移动 下次再显示的时候就会看到子弹在修改后的位置
        pass

    # 发射子弹
    def fire_bullets(self):
        # 创建一个新的子弹对象
        newBullets = Bullet(self.x, self.y, self.screen)
        self.bullets_list.append(newBullets)
        pass
    pass


"""
创建子弹类
"""


class Bullet(object):
    def __init__(self, x, y, screen):
        """
       :param x: 
       :param y: 
       :param screen: 
       """
        self.x = x+13
        self.y = y-20
        self.screen = screen
        self.image = pygame.image.load("./img/子弹1.png")
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def move(self):
        self.y -= 0.5
        pass

    def judge(self):
        """
        判断子弹是否越界
        :return:
        """
        if self.y < 0:
            return True
        else:
            return False
        pass
    pass


# 创建敌机类
class EnemyPlane:
    def __init__(self, screen):
        # 默认设置一个方向
        self.direction = "right"
        self.x = 0
        self.y = 0
        self.screen = screen
        self.image = pygame.image.load("./img/飞机4.png")
        self.enemy_bullets_list = []
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        need_del_list = []
        for item in self.enemy_bullets_list:
            if item.judge():
                need_del_list.append(item)
                pass
            pass
        for i in need_del_list:
            self.enemy_bullets_list.remove(i)
            pass
        for enemyBullet in self.enemy_bullets_list:
            enemyBullet.display()
            enemyBullet.move()
            pass
        pass

    def fire_enemyBullet(self):
        """
        敌机随机发射子弹
        :return:
        """
        num = random.randint(1, 50)
        if num == 3:
            new_enemyBullet = EnemyBullets(self.x, self.y, self.screen)
            self.enemy_bullets_list.append(new_enemyBullet)
        pass

    def move(self):
        """
        敌机移动 随机进行的
        :return:
        """
        if self.direction == "right":
            self.x += 0.1
            pass
        elif self.direction == "left":
            self.x -= 0.1
            pass
        if self.x > 325:
            self.direction = "left"
            pass
        elif self.x < 0:
            self.direction = "right"
            pass
    pass


# 创建敌机子弹类
class EnemyBullets:
    def __init__(self, x, y, screen):
        self.x = x+10
        self.y = y+20
        self.screen = screen
        self.image = pygame.image.load("./img/子弹2.png")
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def move(self):
        self.y += 0.5
        pass

    def judge(self):
        if self.y > 500:
            return True
        else:
            return False
    pass


def key_control(HeroObj):
    """
    定义普通的函数 用来实现键盘的检测
    :param HeroObj:可控制检测的对象
    :return:
    """
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print("退出")
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.type == K_a or event.key == K_LEFT:
                print("left")
                HeroObj.moveleft()  # 调用函数实现左移动
                pass
            elif event.type == K_d or event.key == K_RIGHT:
                print("right")
                HeroObj.moveright()  # 调用函数实现右移动
                pass
            elif event.key == K_SPACE:
                print("按下了空格键 space 发射子弹")
                HeroObj.fire_bullets()      # 发射子弹
                pass
            pass
        pass
    pass


def main():
    screen = pygame.display.set_mode((350, 500), depth=32)
    background = pygame.image.load("./img/背景图1.png")
    pygame.display.set_caption("阶段总结-飞机游戏")

    pygame.mixer.init()
    pygame.mixer.music.load("./img/逆战.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    # 创建一个飞机对象
    hero = HeroPlane(screen)
    # 创建一个敌机对象
    enemy_plane = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        # 显示玩家的飞机图片
        hero.display()
        # 显示敌机
        enemy_plane.display()
        enemy_plane.fire_enemyBullet()
        enemy_plane.move()
        # 获取键盘事件
        key_control(hero)
        pygame.display.update()
        pygame.time.Clock().tick(50)
    pass


if __name__ == '__main__':
    main()
