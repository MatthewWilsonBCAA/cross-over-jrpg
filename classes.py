import pygame
from constants import *
import random
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
    def __init__(self, pos, tile, coll):
        super(Object, self).__init__()
        self.surf = pygame.image.load("sprites/tiles/" + tile + ".png").convert_alpha()
        self.rect = self.surf.get_rect(center=pos)
        self.coll = coll


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Player, self).__init__()
        self.surf = pygame.image.load(r"sprites/entities/player.png").convert_alpha()
        self.rect = self.surf.get_rect(center=pos)

class Fighter(pygame.sprite.Sprite):
    def __init__(self, pos, hp, max_hp, strength, power, defense, move_list, image, name):
        super(Fighter, self).__init__()
        self.hp = hp
        self.max_hp = max_hp
        self.strength = strength
        self.power = power
        self.defense = defense
        self.move_list = move_list
        self.surf = pygame.image.load(r"sprites/entities/"+image).convert_alpha()
        self.rect = self.surf.get_rect(center=pos)
        self.name = name

    def use_move(self, input, enemy_defense):
        move = self.move_list[input-1]
        m_type = move[0]
        if m_type == 0 or m_type == 1:
            if random.random() * 100 < move[2]:
                if m_type == 0:
                    stat = self.strength
                else:
                    stat = self.power
                dmg = move[1] * (stat / 100)
                b = enemy_defense / dmg
                return dmg - (dmg * (enemy_defense / (75 + 50 * b)))
            else:
                return 0
        elif m_type == 3:
            self.hp += move[1] * (self.power // 100)
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            return "h"

class AttackAnimation(pygame.sprite.Sprite):
    def __init__(self, image, style, pos, anim):
        super(AttackAnimation, self).__init__()
        self.surf = pygame.image.load(r"sprites/attacks/"+image).convert_alpha()
        self.const_surf = self.surf
        self.const_pos = pos
        self.rect = self.surf.get_rect(center=pos)
        self.style = style
        self.timer = 0
        self.anim = anim
    
    def play_animation(self):
        self.timer += 1
        if self.anim == 1:
            if self.timer % 5 == 0:
                self.surf = pygame.transform.scale(self.const_surf, (100, 100))
            if self.timer % 15 == 0:
                self.surf = pygame.transform.scale(self.const_surf, (64, 64))
                self.rect.x = random.randint(self.const_pos[0]-100, self.const_pos[0])
                self.rect.y = random.randint(self.const_pos[1]-100, self.const_pos[1])
        if self.anim == 2:
            self.surf = pygame.transform.rotate(self.const_surf, int(self.timer*7.5))
        if self.anim == 3:
            self.surf = pygame.transform.rotate(self.const_surf, int(self.timer*2))
            e = int(self.timer/250)
            self.surf = pygame.transform.scale(self.surf, (128-e,128-e))
        if self.anim == 4:
            if self.timer % 50==0 or self.timer < 2:
                self.rect.x = self.const_pos[0]-150
                self.rect.y = self.const_pos[1]-250
            self.rect.x = self.rect.x+4
            self.rect.y = self.rect.y+6
        if self.timer == 250:
            self.rect = self.surf.get_rect(center=self.const_pos)
            return 1

