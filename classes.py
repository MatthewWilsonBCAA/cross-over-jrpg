import pygame
from constants import *

pygame.init()

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_b,
    K_f,
    K_g,
    K_h,
    K_w,
    K_a,
    K_s,
    K_d,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
)


class Object(pygame.sprite.Sprite):
    def __init__(self, pos, tile):
        super(Object, self).__init__()
        self.surf = pygame.image.load("sprites/tiles/" + tile + ".png").convert_alpha()
        self.rect = self.surf.get_rect(center=pos)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Player, self).__init__()
        self.surf = pygame.image.load(r"sprites/entities/player.png").convert_alpha()
        self.rect = self.surf.get_rect(center=pos)

class Fighter(pygame.sprite.Sprite):
    def __init__(self, pos, hp, max_hp, move_list):
        super(Fighter, self).__init__()
        self.hp = hp
        self.max_hp = max_hp
        self.move_list = move_list
