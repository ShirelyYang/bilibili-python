import pygame
from pygame.locals import *


def main():
    # 首先创建一个窗口 用来显示内容
    screen = pygame.display.set_mode((350, 500), depth=32)
    # 设定一个背景图片
    background = pygame.image.load("./img/背景图1.png")
    # 设置一个title
    pygame.display.set_caption("阶段总结-飞机游戏")

    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load("./img/逆战.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)     # 循环次数 -1表示无限循环

    # 载入玩家的飞机图片
    plane = pygame.image.load("./img/飞机2.png")

    # 初始化玩家的位置
    x, y = 0, 0
    while True:
        # 设定要显示的内容
        screen.blit(background, (0, 0))
        # 显示玩家飞机的图片
        screen.blit(plane, (x, y))
        # 获取键盘事件
        enventList = pygame.event.get()
        for event in enventList:
            if event.type == QUIT:
                print("退出")
                exit()
                pass
            elif event.type == KEYDOWN:
                if event.type == K_a or event.key == K_LEFT:
                    print("left")
                    if x > 0:
                        x -= 5
                    pass
                elif event.type == K_d or event.key == K_RIGHT:
                    print("right")
                    if x < 294:
                        x += 5
                    pass
                elif event.key == K_SPACE:
                    print("K_SPACE")
        # 更新显示内容
        pygame.display.update()
    pass


if __name__ == '__main__':
    main()
