import math

import pygame

from sprite import Sprite


class Arrow(Sprite):
    image = None

    def __init__(self, level, x, y, x_direction, y_direction, angle, *groups):
        Arrow.image = pygame.transform.scale_by(self.load_image('arrow.png'), 1 / 4)
        super().__init__(level.game, Arrow.image, *groups)
        self.level = level
        self.level.projectiles.append(self)
        self.rect.topleft = x, y
        self.x = self.rect.x
        self.y = self.rect.y
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.rotate(Arrow.image, math.degrees(-angle))
        self.default_speed = 500
        self.speed = self.default_speed
        self.damage = 50

    def update(self, delta):
        self.speed -= 100 * delta
        self.move(self.x_direction * self.speed * delta,
                  self.y_direction * self.speed * delta)
        for enemy in self.level.enemies:
            if enemy.rect.colliderect(self.rect):
                enemy.get_damage(self.damage)
                self.remove()

    def remove(self):
        for i, projectile in enumerate(self.level.projectiles):
            if projectile.rect == self.rect:
                del self.level.projectiles[i]
        self.game.projectiles.remove(self)
        self.game.all_sprites.remove(self)

    def move(self, x_speed, y_speed):
        self.x += x_speed
        self.y += y_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def event(self, event: pygame.event.Event):
        pass
