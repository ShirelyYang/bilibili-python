import pygame
import random
from pygame.locals import *


class BasePlane:
    def __init__(self, screen, imagePath):
        self.screen = screen
        self.image = pygame.image.load(imagePath)
        self.bullets_list = []
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        need_del_list = []
        for item in self.bullets_list:
            if item.judege():
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


class HeroPlane(BasePlane):
    def __init__(self, screen):
        super().__init__(screen, "./img/飞机2.png")
        self.x = 150
        self.y = 450
        pass

    def move_left(self):
        if self.x > 0:
            self.x -= 10
            pass
        pass

    def move_right(self):
        if self.x < 294:
            self.x += 10
            pass
        pass
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
            self.x  += 1
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


class CommonBullets:
    def __init__(self, x, y, screen, BulletType):
        self.BulletType = BulletType
        self.screen = screen
        if self.BulletType == "hero":
            self.x = x+20
            self.y = y-10
            self.imagePath = "./img/子弹1.png"
            pass
        elif self.BulletType == "enemy":
            self.x = x+20
            self.y = y+15
            self.imagePath = "./img/子弹3.png"
            pass
        self.image = pygame.image.load(self.imagePath)
        pass

    def move(self):
        if self.BulletType == "hero":
            self.y -= 1
            pass
        elif self.BulletType == "enemy":
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

