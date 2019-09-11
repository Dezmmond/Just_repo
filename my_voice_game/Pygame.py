#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
from player import *
from blocks import *
from pygame import *
from voice_controller import Voice_Controller

win_width = 800
win_height = 640
display = (win_width, win_height)
background_c = '#000000'

hero = Player(55, 580)

platform_width = 32
platform_height = 32
platform_c = '#FF6262'

entities = pygame.sprite.Group()
platforms = []
entities.add(hero)

level=[
    "####################### #",
    "#   #   #   #   # #   # #",
    "# #   #   #   #     # # #",
    "# ############# ##### # #",
    "#       #       #   #   #",
    "####### ####### # ### ###",
    "#             # # # # # #",
    "# ###### # ###### # # # #",
    "#      # # #      # ### #",
    "###### ### # ######     #",
    "#      # # #      # #####",
    "# ###### # ###### # # # #",
    "#    #   # #      # #   #",
    "#### ### # # ####   # ###",
    "#      #   #    # # #   #",
    "# ###### ###### ##### ###",
    "# #                     #",
    "# # ### # ############# #",
    "#    #    #             #",
    "#########################",]

timer = pygame.time.Clock()

def manual_control():
    bg = Surface(display)
    screen = pygame.display.set_mode(display)
    bg.fill(Color(background_c))

    left = right = False
    up = down = False

    while hero.not_win():
        timer.tick(30)
        for i in pygame.event.get(): 

            if i.type == QUIT:
                sys.exit(0)

            if i.type == KEYDOWN and i.key == K_LEFT:
               left = True
            if i.type == KEYDOWN and i.key == K_RIGHT:
               right = True
            if i.type == KEYDOWN and i.key == K_UP:
               up = True
            if i.type == KEYDOWN and i.key == K_DOWN:
               down = True

            if i.type == KEYUP and i.key == K_RIGHT:
               right = False
            if i.type == KEYUP and i.key == K_LEFT:
               left = False
            if i.type == KEYUP and i.key == K_UP:
               up = False
            if i.type == KEYUP and i.key == K_DOWN:
               down = False

        screen.blit(bg, (0, 0))

        hero.update(left, right, up, down, platforms)
        entities.draw(screen)
        pygame.display.update()

def voice_control():
    VC = Voice_Controller()
    VC.talk("Привет! Я голосовой контроллер для этой игры. Для передвижения используй команды вперед, влево, вправо и вниз")

    bg = Surface(display)
    screen = pygame.display.set_mode(display)
    bg.fill(Color(background_c))

    left = right = False
    up = down = False

    while hero.not_win():
        timer.tick(30)

        outp = VC.zadanie()
        print(outp)
        
        if "влево" in outp:
            left = True
        if "вправо" in outp:
            right = True
        if "вверх" in outp:
            up = True
        if "вниз" in outp:
            down = True

        screen.blit(bg, (0, 0))

        hero.update(left, right, up, down, platforms)
        entities.draw(screen)
        pygame.display.update()


def trunk():
    pygame.init()
    pygame.display.set_caption("Labirint")

    x=y=0
    for row in level:
        for col in row:
            if  col == '#':
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)

            x += platform_width
        y += platform_height
        x = 0

    manual_control()
    #voice_control()

if __name__ == "__main__":
    trunk()