import pygame
from constants import *
from random import random
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

font = pygame.font.SysFont("Consolas", 20)

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
    def __init__(self, pos, hp, max_hp, strength, power, defense, move_list):
        super(Fighter, self).__init__()
        self.hp = hp
        self.max_hp = max_hp
        self.strength = strength
        self.power = power
        self.defense = defense
        self.move_list = move_list
        self.surf = pygame.image.load(r"sprites/entities/player.png").convert_alpha()
        self.rect = self.surf.get_rect(center=pos)

    def use_move(self, input, enemy_defense):
        move = self.move_list[input-1]
        m_type = move[0]
        if m_type == 0 or m_type == 1:
            if random() * 100 < move[2]:
                if m_type == 0:
                    stat = self.strength
                else:
                    stat = self.power
                dmg = move[1] * (stat / 100)
                b = enemy_defense / dmg
                return dmg - (dmg * (enemy_defense / (75 + 50 * b)))
            else:
                return "f"
        elif m_type == 3:
            self.hp += move[1] * (self.power // 100)
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            return "h"

