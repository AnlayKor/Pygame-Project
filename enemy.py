import pygame
import math

from animated_sprite import AnimatedSprite
from wall import Wall


class Enemy(AnimatedSprite):
    def get_damage(self, damage):
        self.die()

    def die(self):
        for i, enemy in enumerate(self.level.enemies):
            if enemy.rect == self.rect:
                del self.level.enemies[i]
        self.game.entities.remove(self)
        self.game.all_sprites.remove(self)
