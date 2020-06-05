#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 安装Pygame所依赖的库
# brew install hg sdl sdl_image sdl_ttf

# 如果要启用Pygame的更高级功能，如游戏中包含声音，还需要安装以下库
# brew install sdl_mixer portmidi

# pip install pygame


import pygame

pygame.init()

# 创建游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("Resource/bg.png")
# 2> blit 绘制图像
screen.blit(bg, (0, 0))
# 3> update 更新屏幕显示
pygame.display.update()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()

exit()
