import pygame
import math

from animated_sprite import AnimatedSprite
from wall import Wall


class Enemy(AnimatedSprite):
    def get_damage(self, damage):
        for i, enemy in enumerate(self.level.enemies):
            if enemy.rect == self.rect:
                enemy.health -= damage
                if enemy.health <= 0:
                    self.die(enemy)

    def die(self, enemy):
        for i, enemy in enumerate(self.level.enemies):
            if enemy.rect == self.rect:
                del self.level.enemies[i]
        self.game.entities.remove(self)
        self.game.all_sprites.remove(self)
