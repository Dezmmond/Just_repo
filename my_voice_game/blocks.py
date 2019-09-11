#!/usr/bin/env python
# -*- coding; utf-8 -*-

from pygame import *
import pygame

platform_width = 32
platform_height = 32
platform_color = "#FF6262"

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_width, platform_height))
        self.image.fill(Color(platform_color))
        self.rect = Rect(x, y, platform_width, platform_height)