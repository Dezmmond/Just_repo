#!/usr/bin/env python
# -*- coding; utf-8 -*-

import pygame
from pygame import *

move_speed = 10
width = 22
height = 22
p_color = "#999999"

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((width, height))
        self.image.fill(Color(p_color))
        self.rect = Rect(x, y, width, height)
        self.yvel = 0

    def update(self, left, right, up, down, platforms):
        if left:
            self.xvel = -move_speed

        if right:
            self.xvel = move_speed

        if up:
            self.yvel = -move_speed

        if down:
            self.yvel = move_speed

        if not(left or right or up or down):
            self.xvel = self.yvel = 0

        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.onGround = True
                    self.yvel = 0

    def not_win(self):
        if self.rect.x >= 740 and self.rect.y <= 10:
            run = False                
        else:
            run = True

        return run