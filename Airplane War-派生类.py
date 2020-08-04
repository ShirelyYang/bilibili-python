import pygame
import random
import time
from pygame.locals import *


# 抽象出来一个飞机的基类
class BasePlane:
    def __init__(self, screen, imagePath):
        """
        初始化基类函数
        :param screen: 主窗体对象
        :param imageName: 加载的图片
        """
        self.screen = screen
        self.image = pygame.image.load(imagePath)
        self.bullets_list = []   # 存储所有的子弹
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        need_del_list = []
        for item in self.bullets_list:
            if item.judge():
                need_del_list.append(item)
                pass
            pass
        for i in need_del_list:
            self.bullets_list.remove(i)
            pass
        for bullet in self.bullets_list:
            bullet.display()
            bullet.move()
            pass
        pass
    pass


class CommonBullets:
    """
    公共的子弹类
    """
    def __init__(self, x, y, screen, bulletType):
        self.type = bulletType
        self.screen = screen
        if self.type == "hero":
            self.x = x+20
            self.y = y-10
            self.imagePath = "./img/子弹3.png"
            pass
        elif self.type == "enemy":
            self.x = x+15
            self.y = y+20
            self.imagePath = "./img/子弹2.png"
            pass
        self.image = pygame.image.load(self.imagePath)
        pass

    def move(self):
        """
        子弹的移动
        :return:
        """
        if self.type == "hero":
            self.y -= 1
            pass
        elif self.type == "enemy":
            self.y += 1
            pass
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def judge(self):
        if self.y > 500 or self.y < 0:
            return True
        else:
            return False
        pass
    pass


class HeroPlane(BasePlane):
    def __init__(self, screen):
        super().__init__(screen, "./img/飞机2.png")     # 调用父类的构造方法
        self.x = 150
        self.y = 450
        pass

    def moveLeft(self):
        if self.x > 0:
            self.x -= 10
            pass
        pass

    def moveRight(self):
        if self.x < 294:
            self.x += 10
            pass
        pass

    def fire_bullet(self):
        new_bullet = CommonBullets(self.x, self.y, self.screen, "hero")
        self.bullets_list.append(new_bullet)
    pass


class EnemyPlane(BasePlane):
    def __init__(self, screen):
        super().__init__(screen, "./img/飞机4.png")
        self.x = 0
        self.y = 0
        self.direction = "right"
        pass

    def move(self):
        if self.direction == "right":
            self.x += 1
            pass
        elif self.direction == "left":
            self.x -= 1
            pass
        if self.x < 0:
            self.direction = "right"
            pass
        elif self.x > 325:
            self.direction = "left"
            pass
        pass

    def fire_enemy_bullet(self):
        num = random.randint(1, 50)
        if num == 3:
            new_enemy_bullet = CommonBullets(self.x, self.y, self.screen, "enemy")
            self.bullets_list.append(new_enemy_bullet)
            pass
        pass
    pass


def keyControl(obj):
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == QUIT:
            print("退出")
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                print("left")
                obj.moveLeft()
                pass
            elif event.key == K_RIGHT:
                print("right")
                obj.moveRight()
                pass
            elif event.key == K_SPACE:
                print("按下了空格键 space 发射子弹")
                obj.fire_bullet()
                pass
            pass
        pass
    pass


def main():
    screen = pygame.display.set_mode((350, 500), depth=32)
    background = pygame.image.load("./img/背景图1.png")
    pygame.display.set_caption("Airplane War")

    pygame.mixer.init()
    pygame.mixer.music.load("./img/逆战.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    plane = HeroPlane(screen)
    enemy_plane = EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        plane.display()
        enemy_plane.display()
        enemy_plane.move()
        enemy_plane.fire_enemy_bullet()
        keyControl(plane)
        pygame.display.update()
        pygame.time.Clock().tick(50)
        pass
    pass


if __name__ == '__main__':
    main()
    pass
