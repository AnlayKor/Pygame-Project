import pygame

from sprite import Sprite


class Pixel(Sprite):
    image = None

    def __init__(self, level, x, y, x_direction, y_direction, *groups):
        Pixel.image = pygame.transform.scale_by(self.load_image('pixel.png'), 2)
        super().__init__(level.game, Pixel.image, *groups)
        self.level = level
        self.level.projectiles.append(self)
        self.rect.topleft = x, y
        self.x = self.rect.x
        self.y = self.rect.y
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.speed = 200
        self.damage = 50
        if level.game.character == 'anton':
            self.damage *= 1.5

    def update(self, delta):
        self.move(self.x_direction * self.speed * delta,
                  self.y_direction * self.speed * delta)

        if self.rect.colliderect(self.level.player.rect):
            self.remove()
            self.level.player.get_damage(self.damage)

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
