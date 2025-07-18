#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame.image
import pygame
from pygame import Surface
from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE


class Entity(ABC):
    surf: Surface
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

    @abstractmethod
    def move(self, ):
        pass